# encoding: utf-8
# module PyQt5.QtGui
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtGui.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


class QCursor(__sip.simplewrapper):
    """
    QCursor()
    QCursor(bitmap: QBitmap, mask: QBitmap, hotX: int = -1, hotY: int = -1)
    QCursor(pixmap: QPixmap, hotX: int = -1, hotY: int = -1)
    QCursor(cursor: Union[QCursor, Qt.CursorShape])
    QCursor(variant: Any)
    """
    def bitmap(self): # real signature unknown; restored from __doc__
        """ bitmap(self) -> Optional[QBitmap] """
        pass

    def hotSpot(self): # real signature unknown; restored from __doc__
        """ hotSpot(self) -> QPoint """
        pass

    def mask(self): # real signature unknown; restored from __doc__
        """ mask(self) -> Optional[QBitmap] """
        pass

    def pixmap(self): # real signature unknown; restored from __doc__
        """ pixmap(self) -> QPixmap """
        return QPixmap

    def pos(self, screen=None, QScreen=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        pos() -> QPoint
        pos(screen: Optional[QScreen]) -> QPoint
        """
        pass

    def setPos(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setPos(x: int, y: int)
        setPos(p: QPoint)
        setPos(screen: Optional[QScreen], x: int, y: int)
        setPos(screen: Optional[QScreen], p: QPoint)
        """
        pass

    def setShape(self, newShape): # real signature unknown; restored from __doc__
        """ setShape(self, newShape: Qt.CursorShape) """
        pass

    def shape(self): # real signature unknown; restored from __doc__
        """ shape(self) -> Qt.CursorShape """
        pass

    def swap(self, other, QCursor=None, Qt_CursorShape=None): # real signature unknown; restored from __doc__
        """ swap(self, other: Union[QCursor, Qt.CursorShape]) """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __hash__ = None


