# encoding: utf-8
# module PyQt5.QtMultimedia
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtMultimedia.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


class QMediaTimeRange(__sip.simplewrapper):
    """
    QMediaTimeRange()
    QMediaTimeRange(start: int, end: int)
    QMediaTimeRange(a0: QMediaTimeInterval)
    QMediaTimeRange(range: QMediaTimeRange)
    """
    def addInterval(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        addInterval(self, start: int, end: int)
        addInterval(self, interval: QMediaTimeInterval)
        """
        pass

    def addTimeRange(self, a0): # real signature unknown; restored from __doc__
        """ addTimeRange(self, a0: QMediaTimeRange) """
        pass

    def clear(self): # real signature unknown; restored from __doc__
        """ clear(self) """
        pass

    def contains(self, time): # real signature unknown; restored from __doc__
        """ contains(self, time: int) -> bool """
        return False

    def earliestTime(self): # real signature unknown; restored from __doc__
        """ earliestTime(self) -> int """
        return 0

    def intervals(self): # real signature unknown; restored from __doc__
        """ intervals(self) -> List[QMediaTimeInterval] """
        return []

    def isContinuous(self): # real signature unknown; restored from __doc__
        """ isContinuous(self) -> bool """
        return False

    def isEmpty(self): # real signature unknown; restored from __doc__
        """ isEmpty(self) -> bool """
        return False

    def latestTime(self): # real signature unknown; restored from __doc__
        """ latestTime(self) -> int """
        return 0

    def removeInterval(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        removeInterval(self, start: int, end: int)
        removeInterval(self, interval: QMediaTimeInterval)
        """
        pass

    def removeTimeRange(self, a0): # real signature unknown; restored from __doc__
        """ removeTimeRange(self, a0: QMediaTimeRange) """
        pass

    def __add__(self, *args, **kwargs): # real signature unknown
        """ Return self+value. """
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

    def __iadd__(self, *args, **kwargs): # real signature unknown
        """ Return self+=value. """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    def __isub__(self, *args, **kwargs): # real signature unknown
        """ Return self-=value. """
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

    def __radd__(self, *args, **kwargs): # real signature unknown
        """ Return value+self. """
        pass

    def __rsub__(self, *args, **kwargs): # real signature unknown
        """ Return value-self. """
        pass

    def __sub__(self, *args, **kwargs): # real signature unknown
        """ Return self-value. """
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __hash__ = None


