# encoding: utf-8
# module PyQt5.QtCore
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtCore.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum
import sip as __sip


class QRunnable(__sip.wrapper):
    """
    QRunnable()
    QRunnable(a0: QRunnable)
    """
    def autoDelete(self): # real signature unknown; restored from __doc__
        """ autoDelete(self) -> bool """
        return False

    def create(self, functionToRun, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ create(functionToRun: Callable[[], None]) -> Optional[QRunnable] """
        pass

    def run(self): # real signature unknown; restored from __doc__
        """ run(self) """
        pass

    def setAutoDelete(self, _autoDelete): # real signature unknown; restored from __doc__
        """ setAutoDelete(self, _autoDelete: bool) """
        pass

    def __init__(self, a0=None): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



