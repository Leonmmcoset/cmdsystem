# encoding: utf-8
# module PyQt5.QtGui
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtGui.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


class QDropEvent(__PyQt5_QtCore.QEvent):
    """
    QDropEvent(pos: Union[QPointF, QPoint], actions: Union[Qt.DropActions, Qt.DropAction], data: Optional[QMimeData], buttons: Union[Qt.MouseButtons, Qt.MouseButton], modifiers: Union[Qt.KeyboardModifiers, Qt.KeyboardModifier], type: QEvent.Type = QEvent.Drop)
    QDropEvent(a0: QDropEvent)
    """
    def acceptProposedAction(self): # real signature unknown; restored from __doc__
        """ acceptProposedAction(self) """
        pass

    def dropAction(self): # real signature unknown; restored from __doc__
        """ dropAction(self) -> Qt.DropAction """
        pass

    def keyboardModifiers(self): # real signature unknown; restored from __doc__
        """ keyboardModifiers(self) -> Qt.KeyboardModifiers """
        pass

    def mimeData(self): # real signature unknown; restored from __doc__
        """ mimeData(self) -> Optional[QMimeData] """
        pass

    def mouseButtons(self): # real signature unknown; restored from __doc__
        """ mouseButtons(self) -> Qt.MouseButtons """
        pass

    def pos(self): # real signature unknown; restored from __doc__
        """ pos(self) -> QPoint """
        pass

    def posF(self): # real signature unknown; restored from __doc__
        """ posF(self) -> QPointF """
        pass

    def possibleActions(self): # real signature unknown; restored from __doc__
        """ possibleActions(self) -> Qt.DropActions """
        pass

    def proposedAction(self): # real signature unknown; restored from __doc__
        """ proposedAction(self) -> Qt.DropAction """
        pass

    def setDropAction(self, action): # real signature unknown; restored from __doc__
        """ setDropAction(self, action: Qt.DropAction) """
        pass

    def source(self): # real signature unknown; restored from __doc__
        """ source(self) -> Optional[QObject] """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass


