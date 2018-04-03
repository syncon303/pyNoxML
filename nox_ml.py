import os
import binascii
from time import time
from collections import OrderedDict
import sys
from shutil import copyfile
from PyQt4 import QtGui, QtCore
from noxML_ui import Ui_MainWindow
from noxML_box_ui import Ui_form_edit_macro
from datetime import datetime

# To make an executable run (executable size ~14MB):
# pyinstaller --onefile -w nox_ml.py


def get_timestamp():
    d = datetime.now()
    return "{}{:02d}{:02d}_{:02d}{:02d}{:02d}".format(d.year, d.month, d.day, d.hour, d.minute, d.second)


def get_random_hex_string(length=32):
    """ Returns randomized string of hexadecimal characters of given length.

    :param length: Number of characters in output string.
    :return: Hexadecimal string
    """
    return binascii.b2a_hex(os.urandom(int(length//2)))


class MacroEdit(QtGui.QWidget, Ui_form_edit_macro):
    def __init__(self, parent):
        super(MacroEdit, self).__init__()
        self.setupUi(self)
        self.parent = parent
        self.btn_box.accepted.connect(self.parent.save_edit_box)
        self.btn_box.rejected.connect(self.parent.close_edit_box)
        self.txt = ''
        self.filename = None
        self.existing_macro = False


class GUIForm(Ui_MainWindow):
    def __init__(self, parent=None):
        Ui_MainWindow.setupUi(self, parent)
        self.parent = parent
        self.w_sub = MacroEdit(self)

        # connect functions to the events
        self.btn_prop_save.clicked.connect(self.save_macro_properties)
        self.btn_prop_rst.clicked.connect(self.reset_macro_properties)
        self.btn_nox_save.clicked.connect(self.generate_records)
        self.btn_import_file.clicked.connect(self.import_macro_file)
        self.btn_new_macro.clicked.connect(self._open_edit_macro_window)
        self.btn_edit_macro.clicked.connect(self.open_macro_file)
        self.list_macros.currentItemChanged.connect(self.change_current_macro)

        # use delete key to remove currently selected macro from the list (note, this does nt delete the file):
        # - make shortcut for the delete key when used in macro list
        self.shortcut_list_delete = QtGui.QShortcut(QtGui.QKeySequence(QtCore.Qt.Key_Delete), self.list_macros)
        # - assign shortcut to the call of delete macro entry function
        self.parent.connect(self.shortcut_list_delete, QtCore.SIGNAL('activated()'), self.delete_entry)

        # use numeric validators for loop all input fields
        self.e_loop_count.setValidator(QtGui.QIntValidator(0, int(1E9)))
        self.e_loop_interval.setValidator(QtGui.QIntValidator(0, 65535))
        self.e_loop_hr.setValidator(QtGui.QIntValidator(0, 65535))
        self.e_loop_min.setValidator(QtGui.QIntValidator(0, 59))
        self.e_loop_sec.setValidator(QtGui.QIntValidator(0, 59))

        # bundle logically connected controls together to clean some code up
        self.loop_duration_handles = self.e_loop_hr, self.e_loop_min, self.e_loop_sec
        self.loop_mode_handles = self.rd_loop_no, self.rd_loop_till_stop, self.rd_loop_time

        # assign drop of object into macro list to the function macro_dropped
        # note: all objects are pre-filtered for 'url' property, so it is assumed they are links to files
        self.parent.connect(self.list_macros, QtCore.SIGNAL("dropped"), self.macro_dropped)

        # initialize macro library
        self.macro_lib = OrderedDict()
        # native macro directory (in normal installation it would be $LOCALAPPDATA$\Nox\record )
        self.lib_directory = os.path.join(os.getenv('localappdata'), 'Nox', 'record')

        self.current_macro = None

        # read records file and populate library
        self.read_record_file()
        self.update_macro_library()

    def macro_dropped(self, l):
        """ Generates new macro entries based on list of objects that were dropped into macro list

        :param l: List of macros as prepared by dropEvent function of modified QListWidget (see file qt_custom.py)
        :return: (no value)
        """
        for url in l:
            self.import_macro_file(url)

    # def update_macro_order(self):
    #     """ ---OBSOLETE---  Function regenerates internal macro library based on current state of macro list.
    #
    #     :return: (no value)
    #     """
    #     ml_tmp = OrderedDict()
    #     for i in range(self.list_macros.count()):
    #         alias = str(self.list_macros.item(i).text())
    #         for k, v in self.macro_lib.items():
    #             if v.alias == alias:
    #                 break
    #         else:
    #             continue
    #         ml_tmp[k] = v
    #     self.macro_lib = ml_tmp

    # --------- Management of the macro editor window -----------------------------------------------------------------

    def save_edit_box(self):
        """ Function gets macro text from the edit box and stores it into file

        :return: (no value)
        """
        txt = str(self.w_sub.edit_macro.toPlainText())
        if txt != self.w_sub.txt:
            if not self.w_sub.filename:
                # on new macro create an entry at same time
                self.w_sub.filename = self.get_unique_filename() if self.w_sub.filename is None else self.w_sub.filename
                self._new_macro_entry(self.w_sub.filename, force_name=True)
            with open(os.path.join(self.lib_directory, self.w_sub.filename), 'w+') as h_f:
                h_f.write(txt)
        self.w_sub.close()

    def close_edit_box(self):
        """ Closes edit box if user pressed Cancel """
        self.w_sub.close()

    def _open_edit_macro_window(self, file_):
        data = ''
        self.w_sub.filename = None
        if file_:
            self.w_sub.filename = file_
            try:
                with open(os.path.join(self.lib_directory, file_), 'r') as h_f:
                    data = ''.join(h_f.readlines())

            except IOError:
                data = ''
        if data:
            self.w_sub.edit_macro.setText(data)
            self.w_sub.txt = data
        else:
            self.w_sub.edit_macro.clear()
            self.w_sub.txt = ''
        self.w_sub.show()

    def open_macro_file(self):
        """ Function reads the content of the currently selected macro and uses an internal function to
            open the edit windows and displays it in the edit box.

        :return: (no value)
        """
        if not self.current_macro or not self.current_macro.filename:
            return
        self._open_edit_macro_window(self.current_macro.filename)

    # ------------------------------------------------------------------------------------------------------------------

    def import_macro_file(self, url=None):
        """ Function imports the given macro file into the Nox record directory. If no file is given the function will
        show an Open file dialog where user can select the file to import.

        :param url: File path. If None, the function will open a dialog
        :return: (no value)
        """
        if url is None:
            url = QtGui.QFileDialog.getOpenFileName(self.parent, "Import macro file",
                                                    self.lib_directory,
                                                    "All Files (*)")
        if os.path.exists(url):
            filename = os.path.basename(url)
            print 'Existing name =', filename
            if os.path.dirname(url) != self.lib_directory.replace('\\', '/'):
                new_name = self.get_unique_filename(filename, check_folder=False)
                print 'New name =', new_name
                copyfile(url, os.path.join(self.lib_directory, new_name))
                filename = new_name
            self._new_macro_entry(filename, force_name=True)

    def get_unique_filename(self, filename=None, check_folder=True):
        """ Function will generate a random 32 hexadecimal digit string as a unique file name.

        :param filename: Preferred file name
        :param check_folder: If True, the function will check if such file already exists in the record directory
        :return: Filename string
        """
        if filename in ('', None):
            filename = get_random_hex_string(32)
        while True:
            if filename not in self.macro_lib:
                if not (check_folder and os.path.exists(os.path.join(self.lib_directory, filename))):
                    print 'Final name =', filename
                    break
            filename = get_random_hex_string(32)
        return filename

    def _new_macro_entry(self, filename=None, force_name=False):
        """ Function adds a new macro entry to the library. It creates a unique file name, adds a new entry into
        internal macro database, presets macro properties to default, and adds an entry to the list

        :param filename: Preferred macro file name
        :param force_name: If True, it forces the use of the given file name, potentially overwriting already
                           existing file
        :return: (no value)
        """
        if not force_name:
            filename = self.get_unique_filename(filename)
        self.macro_lib[filename] = MacroEntry()
        self.macro_lib[filename].alias = self.get_macro_name_string(self.macro_lib[filename].macroname, filename)
        self.macro_lib[filename].filename = filename
        self.list_macros.addItem(self.macro_lib[filename].alias)
        # TODO: Select new macro in the macro list
        self.list_macros.setCurrentRow(int(self.list_macros.count())-1)
        pass

    def change_current_macro(self):
        alias = self.list_macros.currentItem().text()
        for k, v in self.macro_lib.items():
            if v.alias == alias:
                break
        else:
            return
        self.current_macro = v
        self.update_macro_properties()

    @staticmethod
    def get_macro_name_string(name, file_, truncate=False):
        if truncate:
            if len(file_) > 7:
                file_ = '{}...'.format(file_[:4])
            return '{} ({})'.format(name, file_)
        else:
            return '{}     (file: {})'.format(name, file_)

    def update_macro_library(self):
        self.list_macros.clear()
        for k, v in self.macro_lib.items():
            alias = self.get_macro_name_string(v.macroname, k)
            v.alias = alias
            self.list_macros.addItem(alias)

    def get_loop_mode(self):
        # mode number corresponds to the active radio button
        # use loop # of times as default if no button is checked for some reason
        for i, v in enumerate(self.loop_mode_handles):
            if v.isChecked():
                return i
        return 0

    def update_macro_properties(self):
        self.e_macro_name.setText(self.current_macro.macroname)

        mode = int(self.current_macro.playset.get('mode', 0))
        mode = mode if mode in range(3) else 0
        self.loop_mode_handles[mode].setChecked(True)

        self.e_loop_count.setText(str(self.current_macro.playset.get('repeatTimes', 0)))
        p_time = self.current_macro.playset.get('playSeconds', '0#0#0').split('#')
        if len(p_time) != 3:
            p_time = 0, 0, 0
        for s, d in zip(p_time, self.loop_duration_handles):
            d.setText(s)
        self.e_loop_interval.setText(str(self.current_macro.playset.get('interval', 0)))
        self.hslid_accel.setValue(int(self.current_macro.playset.get('accelerator', 1)))
        self.lbl_slider_value.setNum(self.hslid_accel.value())

    def delete_entry(self):
        """ Removes macro entry from list of macros
        """
        if self.current_macro is None:
            return
        self.list_macros.takeItem(self.list_macros.currentRow())
        self.change_current_macro()


    def save_macro_properties(self):
        # print 'save!!1'
        if self.current_macro is None:
            return
        name = str(self.e_macro_name.text())
        if self.current_macro.macroname != name:
            # if name changed update the name in the library list as well
            self.current_macro.macroname = name
            self.current_macro.alias = self.get_macro_name_string(name, self.current_macro.filename)
            self.list_macros.currentItem().setText(self.current_macro.alias)
        # extract loop mode value from current state of radio buttons
        self.current_macro.playset['mode'] = self.get_loop_mode()
        # loop count
        tmp = str(self.e_loop_count.text())
        self.current_macro.playset['repeatTimes'] = '0' if not tmp else tmp
        # loop play duration
        p_time = '#'.join(str(x.text()) for x in self.loop_duration_handles)
        self.current_macro.playset['playSeconds'] = p_time
        # loop interval
        self.current_macro.playset['interval'] = str(self.e_loop_interval.text())

        self.current_macro.playset['accelerator'] = int(self.hslid_accel.value())

    def reset_macro_properties(self):
        # print 'reset!!1'
        if self.current_macro is None:
            return
        self.loop_mode_handles[0].setChecked(True)
        self.e_loop_count.setText(str(0))
        for d in self.loop_duration_handles:
            d.setText(str(0))
        self.e_loop_interval.setText(str(0))
        self.hslid_accel.setValue(1)

    # ----- Read / Store records file ----------------------------------------------------------------------------------

    def read_record_file(self, filename=None):
        record_filename = 'records'
        if type(filename) != str or not filename:
            filename = os.path.join(self.lib_directory, record_filename)
        if not os.path.exists(filename):
            filename = QtGui.QFileDialog.getOpenFileName(self.parent, 'Select records file', self.lib_directory,
                                                         'All files (*)')
            filename = str(filename)
            if filename == '':
                return
        with open(filename, 'r') as h_f:
            temp_rec = dict()
            try:
                # records file is in form of a Python dictionary. Convert it to ordered dict to maintain the order
                # of existing macros, and populate the library with them.
                lines = h_f.read()
                from ast import literal_eval
                temp_rec = literal_eval(lines)
            except (ValueError, SyntaxError, TypeError):
                print 'Error: Could not find an existing records file, starting with blank library'
                lines = ''

            # as the order of the literals from the eval is not guaranteed, get a proper order by
            #   comparing the field names with their position in the file
            temp_rec = OrderedDict(sorted(temp_rec.items(), key=lambda x: lines.find('"{}":'.format(x[0]))))
            for k, v in temp_rec.items():
                if k in self.macro_lib:
                    continue  # skip existing entries
                if not os.path.exists(os.path.join(self.lib_directory, k)):
                    print 'Error: No file for macro {}'.format(v['name'])
                    continue
                v['filename'] = k
                self.macro_lib[k] = MacroEntry(**v)
        # print '\n'.join(self.macro_lib.keys())
        self.lib_directory = os.path.dirname(filename)

    def generate_records(self):
        make_backup = self.chk_backup.isChecked()
        record_filename = 'records'
        filename = os.path.join(self.lib_directory, record_filename)
        if os.path.exists(filename) and make_backup:
            copyfile(filename, '_'.join((filename, get_timestamp())))
        # Nox determines the order of macros by time of creation therefore insert random time into macros
        c_time = int(time())
        with open(filename, 'w+b') as h_f:
            l_txt = list()
            for i in range(self.list_macros.count()):
                alias = str(self.list_macros.item(i).text())
                for k, v in self.macro_lib.items():
                    if v.alias == alias:
                        break
                else:
                    continue
                v.time = c_time
                c_time -= 60
                l_txt.append(str(v))
            h_f.write('{\n')  # open dictionary
            h_f.write(',\n'.join(l_txt))  # string entries together using comma
            h_f.write('\n}\n')  # terminate last entry with new line and close dictionary


class MacroEntry(object):
    """ MacroEntry is an class for an object mimicking the

    """
    def __init__(self, **kw):
        self.filename = kw.get('filename')
        self.macroname = kw.get('name', 'New macro')
        self.time = int(kw.get('time', time()))
        self.playset = dict(accelerator=1, interval=0, mode=1, playSeconds='0#0#0', repeatTimes=1)
        self.description = ''
        self.alias = ''
        ps = kw.get('playSet')
        if type(ps) == dict:
            for k, v in ps.items():
                if k in self.playset:
                    self.playset[k] = v

    def update_interval(self, hours, minutes, seconds):
        self.playset['playSeconds'] = '{}#{}#{}'.format(hours, minutes, seconds)

    def __str__(self):
        return ''.join(('    \"{}\": {{\n'.format(self.filename),
                        '        "name": "{}",\n'.format(self.macroname),
                        '        "new": "false",\n',
                        '        "playSet": {\n',
                        '            "accelerator": "{}",\n'.format(self.playset['accelerator']),
                        '            "interval": "{}",\n'.format(self.playset['interval']),
                        '            "mode": "{}",\n'.format(self.playset['mode']),
                        '            "playSeconds": "{}",\n'.format(self.playset['playSeconds']),
                        '            "repeatTimes": "{}"\n'.format(self.playset['repeatTimes']),
                        '        },\n',
                        '        "time": "{}"\n'.format(self.time),
                        '    }'
                        ))


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    myapp = QtGui.QMainWindow()
    ui = GUIForm(myapp)

    myapp.show()
    sys.exit(app.exec_())
