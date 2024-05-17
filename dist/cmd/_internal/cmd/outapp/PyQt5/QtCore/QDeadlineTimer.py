# encoding: utf-8
# module PyQt5.QtCore
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtCore.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum
import sip as __sip


class QDeadlineTimer(__sip.simplewrapper):
    """
    QDeadlineTimer(type: Qt.TimerType = Qt.CoarseTimer)
    QDeadlineTimer(a0: QDeadlineTimer.ForeverConstant, type: Qt.TimerType = Qt.CoarseTimer)
    QDeadlineTimer(msecs: int, type: Qt.TimerType = Qt.CoarseTimer)
    QDeadlineTimer(a0: QDeadlineTimer)
    """
    def addNSecs(self, dt, nsecs): # real signature unknown; restored from __doc__
        """ addNSecs(dt: QDeadlineTimer, nsecs: int) -> QDeadlineTimer """
        return QDeadlineTimer

    def current(self, type=None): # real signature unknown; restored from __doc__
        """ current(type: Qt.TimerType = Qt.CoarseTimer) -> QDeadlineTimer """
        return QDeadlineTimer

    def deadline(self): # real signature unknown; restored from __doc__
        """ deadline(self) -> int """
        return 0

    def deadlineNSecs(self): # real signature unknown; restored from __doc__
        """ deadlineNSecs(self) -> int """
        return 0

    def hasExpired(self): # real signature unknown; restored from __doc__
        """ hasExpired(self) -> bool """
        return False

    def isForever(self): # real signature unknown; restored from __doc__
        """ isForever(self) -> bool """
        return False

    def remainingTime(self): # real signature unknown; restored from __doc__
        """ remainingTime(self) -> int """
        return 0

    def remainingTimeNSecs(self): # real signature unknown; restored from __doc__
        """ remainingTimeNSecs(self) -> int """
        return 0

    def setDeadline(self, msecs, type=None): # real signature unknown; restored from __doc__
        """ setDeadline(self, msecs: int, type: Qt.TimerType = Qt.CoarseTimer) """
        pass

    def setPreciseDeadline(self, secs, nsecs=0, type=None): # real signature unknown; restored from __doc__
        """ setPreciseDeadline(self, secs: int, nsecs: int = 0, type: Qt.TimerType = Qt.CoarseTimer) """
        pass

    def setPreciseRemainingTime(self, secs, nsecs=0, type=None): # real signature unknown; restored from __doc__
        """ setPreciseRemainingTime(self, secs: int, nsecs: int = 0, type: Qt.TimerType = Qt.CoarseTimer) """
        pass

    def setRemainingTime(self, msecs, type=None): # real signature unknown; restored from __doc__
        """ setRemainingTime(self, msecs: int, type: Qt.TimerType = Qt.CoarseTimer) """
        pass

    def setTimerType(self, type): # real signature unknown; restored from __doc__
        """ setTimerType(self, type: Qt.TimerType) """
        pass

    def swap(self, other): # real signature unknown; restored from __doc__
        """ swap(self, other: QDeadlineTimer) """
        pass

    def timerType(self): # real signature unknown; restored from __doc__
        """ timerType(self) -> Qt.TimerType """
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


    Forever = 0
    __hash__ = None


