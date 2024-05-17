# encoding: utf-8
# module PyQt5.QtGui
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtGui.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


class QPixmapCache(__sip.simplewrapper):
    """
    QPixmapCache()
    QPixmapCache(a0: QPixmapCache)
    """
    def cacheLimit(self): # real signature unknown; restored from __doc__
        """ cacheLimit() -> int """
        return 0

    def clear(self): # real signature unknown; restored from __doc__
        """ clear() """
        pass

    def find(self, key, p_str=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        find(key: Optional[str]) -> QPixmap
        find(key: QPixmapCache.Key) -> QPixmap
        """
        return QPixmap

    def insert(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        insert(key: Optional[str], a1: QPixmap) -> bool
        insert(pixmap: QPixmap) -> QPixmapCache.Key
        """
        pass

    def remove(self, key, p_str=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        remove(key: Optional[str])
        remove(key: QPixmapCache.Key)
        """
        pass

    def replace(self, key, pixmap): # real signature unknown; restored from __doc__
        """ replace(key: QPixmapCache.Key, pixmap: QPixmap) -> bool """
        return False

    def setCacheLimit(self, a0): # real signature unknown; restored from __doc__
        """ setCacheLimit(a0: int) """
        pass

    def __init__(self, a0=None): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""




