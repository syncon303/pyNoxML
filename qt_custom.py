from PyQt4 import QtGui, QtCore

# from qt_custom import QLineEditDragDrop, QListWidgetDrag


class QLineEditDragDrop(QtGui.QLineEdit):
    def __init__(self, *args):
        super(QLineEditDragDrop, self).__init__(*args)
        self.setAcceptDrops(True)

    def dragEnterEvent(self, event):
        print 'yay'
        if event.mimeData().hasUrls():
            event.accept()
        else:
            super(QLineEditDragDrop, self).dragEnterEvent(event)

    def dragMoveEvent(self, event):
        print 'yay'
        if event.mimeData().hasUrls():
            event.setDropAction(QtCore.Qt.CopyAction)
            event.accept()
        else:
            super(QLineEditDragDrop, self).dragMoveEvent(event)

    def dropEvent(self, event):
        print 'dropEvent', event
        print event.mimeData().text()
        if event.mimeData().hasUrls():
            event.setDropAction(QtCore.Qt.CopyAction)
            event.accept()
            links = []
            for url in event.mimeData().urls():
                links.append(str(url.toLocalFile()))
            self.emit(QtCore.SIGNAL("dropped"), links)
        else:
            event.setDropAction(QtCore.Qt.MoveAction)
            super(QLineEditDragDrop, self).dropEvent(event)


class TestListWidget(QtGui.QListWidget):
    def __init__(self, parent=None):
        super(TestListWidget, self).__init__(parent)
        self.setAcceptDrops(True)

    def dragEnterEvent(self, event, *args, **kw):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            super(TestListWidget, self).dragEnterEvent(event)

    def dragMoveEvent(self, event, *args, **kw):
        if event.mimeData().hasUrls():
            event.setDropAction(QtCore.Qt.CopyAction)
            event.accept()
        else:
            super(TestListWidget, self).dragMoveEvent(event, *args)

    def dropEvent(self, event, *args, **kw):
        if event.mimeData().hasUrls():
            event.setDropAction(QtCore.Qt.CopyAction)
            event.accept()
            links = []
            for url in event.mimeData().urls():
                links.append(str(url.toLocalFile()))
            self.emit(QtCore.SIGNAL("dropped"), links)
        else:
            super(TestListWidget, self).dropEvent(event)


class QListWidgetDragDrop(QtGui.QListWidget):
    itemDropped = QtCore.pyqtSignal()

    def __init__(self, parent=None):
        super(QListWidgetDragDrop, self).__init__(parent)
        self.installEventFilter(self)

    def dropEvent(self, event):
        super(QListWidgetDragDrop, self).dropEvent(event)
        self.itemDropped.emit()

    def eventFilter(self, obj, event):
        print QtCore.QEvent.MouseButtonRelease
        print event, event.type() == QtCore.QEvent
        if event.type() == QtCore.QEvent:
            zz = QtCore.QEvent(event)
            print zz
        return QtGui.QListWidget.eventFilter(self, obj, event)

    #
    # def mouseMoveEvent(self, event):
    #     if event.button() != QtCore.Qt.LeftButton:
    #         return
    #     print 'se tu'
    #     if self.currentItem() is None:
    #         return
    #     print 'dragging'
