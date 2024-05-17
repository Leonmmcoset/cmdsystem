# encoding: utf-8
# module PyQt5.QtGui
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtGui.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


from .QInputEvent import QInputEvent

class QMouseEvent(QInputEvent):
    """
    QMouseEvent(type: QEvent.Type, pos: Union[QPointF, QPoint], button: Qt.MouseButton, buttons: Union[Qt.MouseButtons, Qt.MouseButton], modifiers: Union[Qt.KeyboardModifiers, Qt.KeyboardModifier])
    QMouseEvent(type: QEvent.Type, pos: Union[QPointF, QPoint], globalPos: Union[QPointF, QPoint], button: Qt.MouseButton, buttons: Union[Qt.MouseButtons, Qt.MouseButton], modifiers: Union[Qt.KeyboardModifiers, Qt.KeyboardModifier])
    QMouseEvent(type: QEvent.Type, pos: Union[QPointF, QPoint], windowPos: Union[QPointF, QPoint], globalPos: Union[QPointF, QPoint], button: Qt.MouseButton, buttons: Union[Qt.MouseButtons, Qt.MouseButton], modifiers: Union[Qt.KeyboardModifiers, Qt.KeyboardModifier])
    QMouseEvent(type: QEvent.Type, localPos: Union[QPointF, QPoint], windowPos: Union[QPointF, QPoint], screenPos: Union[QPointF, QPoint], button: Qt.MouseButton, buttons: Union[Qt.MouseButtons, Qt.MouseButton], modifiers: Union[Qt.KeyboardModifiers, Qt.KeyboardModifier], source: Qt.MouseEventSource)
    QMouseEvent(a0: QMouseEvent)
    """
    def button(self): # real signature unknown; restored from __doc__
        """ button(self) -> Qt.MouseButton """
        pass

    def buttons(self): # real signature unknown; restored from __doc__
        """ buttons(self) -> Qt.MouseButtons """
        pass

    def flags(self): # real signature unknown; restored from __doc__
        """ flags(self) -> Qt.MouseEventFlags """
        pass

    def globalPos(self): # real signature unknown; restored from __doc__
        """ globalPos(self) -> QPoint """
        pass

    def globalX(self): # real signature unknown; restored from __doc__
        """ globalX(self) -> int """
        return 0

    def globalY(self): # real signature unknown; restored from __doc__
        """ globalY(self) -> int """
        return 0

    def localPos(self): # real signature unknown; restored from __doc__
        """ localPos(self) -> QPointF """
        pass

    def pos(self): # real signature unknown; restored from __doc__
        """ pos(self) -> QPoint """
        pass

    def screenPos(self): # real signature unknown; restored from __doc__
        """ screenPos(self) -> QPointF """
        pass

    def source(self): # real signature unknown; restored from __doc__
        """ source(self) -> Qt.MouseEventSource """
        pass

    def windowPos(self): # real signature unknown; restored from __doc__
        """ windowPos(self) -> QPointF """
        pass

    def x(self): # real signature unknown; restored from __doc__
        """ x(self) -> int """
        return 0

    def y(self): # real signature unknown; restored from __doc__
        """ y(self) -> int """
        return 0

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass


