# encoding: utf-8
# module PyQt5.QtGui
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtGui.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


from .QDropEvent import QDropEvent

class QDragMoveEvent(QDropEvent):
    """
    QDragMoveEvent(pos: QPoint, actions: Union[Qt.DropActions, Qt.DropAction], data: Optional[QMimeData], buttons: Union[Qt.MouseButtons, Qt.MouseButton], modifiers: Union[Qt.KeyboardModifiers, Qt.KeyboardModifier], type: QEvent.Type = QEvent.DragMove)
    QDragMoveEvent(a0: QDragMoveEvent)
    """
    def accept(self, r=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        accept(self)
        accept(self, r: QRect)
        """
        pass

    def answerRect(self): # real signature unknown; restored from __doc__
        """ answerRect(self) -> QRect """
        pass

    def ignore(self, r=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        ignore(self)
        ignore(self, r: QRect)
        """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass


