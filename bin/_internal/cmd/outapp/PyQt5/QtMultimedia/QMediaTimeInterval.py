# encoding: utf-8
# module PyQt5.QtMultimedia
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtMultimedia.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


class QMediaTimeInterval(__sip.simplewrapper):
    """
    QMediaTimeInterval()
    QMediaTimeInterval(start: int, end: int)
    QMediaTimeInterval(a0: QMediaTimeInterval)
    """
    def contains(self, time): # real signature unknown; restored from __doc__
        """ contains(self, time: int) -> bool """
        return False

    def end(self): # real signature unknown; restored from __doc__
        """ end(self) -> int """
        return 0

    def isNormal(self): # real signature unknown; restored from __doc__
        """ isNormal(self) -> bool """
        return False

    def normalized(self): # real signature unknown; restored from __doc__
        """ normalized(self) -> QMediaTimeInterval """
        return QMediaTimeInterval

    def start(self): # real signature unknown; restored from __doc__
        """ start(self) -> int """
        return 0

    def translated(self, offset): # real signature unknown; restored from __doc__
        """ translated(self, offset: int) -> QMediaTimeInterval """
        return QMediaTimeInterval

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


