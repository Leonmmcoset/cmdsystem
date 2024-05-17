# encoding: utf-8
# module PyQt5.QtGui
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtGui.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


class QDrag(__PyQt5_QtCore.QObject):
    """ QDrag(dragSource: Optional[QObject]) """
    def actionChanged(self, *args, **kwargs): # real signature unknown
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
        pass

    def cancel(self): # real signature unknown; restored from __doc__
        """ cancel() """
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def defaultAction(self): # real signature unknown; restored from __doc__
        """ defaultAction(self) -> Qt.DropAction """
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def dragCursor(self, action): # real signature unknown; restored from __doc__
        """ dragCursor(self, action: Qt.DropAction) -> QPixmap """
        return QPixmap

    def exec(self, supportedActions, Qt_DropActions=None, Qt_DropAction=None, *args, **kwargs): # real signature unknown; restored from __doc__ with multiple overloads
        """
        exec(self, supportedActions: Union[Qt.DropActions, Qt.DropAction] = Qt.MoveAction) -> Qt.DropAction
        exec(self, supportedActions: Union[Qt.DropActions, Qt.DropAction], defaultDropAction: Qt.DropAction) -> Qt.DropAction
        """
        pass

    def exec_(self, supportedActions, Qt_DropActions=None, Qt_DropAction=None, *args, **kwargs): # real signature unknown; restored from __doc__ with multiple overloads
        """
        exec_(self, supportedActions: Union[Qt.DropActions, Qt.DropAction] = Qt.MoveAction) -> Qt.DropAction
        exec_(self, supportedActions: Union[Qt.DropActions, Qt.DropAction], defaultDropAction: Qt.DropAction) -> Qt.DropAction
        """
        pass

    def hotSpot(self): # real signature unknown; restored from __doc__
        """ hotSpot(self) -> QPoint """
        pass

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def mimeData(self): # real signature unknown; restored from __doc__
        """ mimeData(self) -> Optional[QMimeData] """
        pass

    def pixmap(self): # real signature unknown; restored from __doc__
        """ pixmap(self) -> QPixmap """
        return QPixmap

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setDragCursor(self, cursor, action): # real signature unknown; restored from __doc__
        """ setDragCursor(self, cursor: QPixmap, action: Qt.DropAction) """
        pass

    def setHotSpot(self, hotspot): # real signature unknown; restored from __doc__
        """ setHotSpot(self, hotspot: QPoint) """
        pass

    def setMimeData(self, data, QMimeData=None): # real signature unknown; restored from __doc__
        """ setMimeData(self, data: Optional[QMimeData]) """
        pass

    def setPixmap(self, a0): # real signature unknown; restored from __doc__
        """ setPixmap(self, a0: QPixmap) """
        pass

    def source(self): # real signature unknown; restored from __doc__
        """ source(self) -> Optional[QObject] """
        pass

    def supportedActions(self): # real signature unknown; restored from __doc__
        """ supportedActions(self) -> Qt.DropActions """
        pass

    def target(self): # real signature unknown; restored from __doc__
        """ target(self) -> Optional[QObject] """
        pass

    def targetChanged(self, *args, **kwargs): # real signature unknown
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, dragSource, QObject=None): # real signature unknown; restored from __doc__
        pass


