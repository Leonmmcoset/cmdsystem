# encoding: utf-8
# module PyQt5.QtCore
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtCore.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum
import sip as __sip


class QLoggingCategory(__sip.simplewrapper):
    """
    QLoggingCategory(category: Optional[str])
    QLoggingCategory(category: Optional[str], severityLevel: QtMsgType)
    """
    def categoryName(self): # real signature unknown; restored from __doc__
        """ categoryName(self) -> Optional[str] """
        pass

    def defaultCategory(self): # real signature unknown; restored from __doc__
        """ defaultCategory() -> Optional[QLoggingCategory] """
        pass

    def isCriticalEnabled(self): # real signature unknown; restored from __doc__
        """ isCriticalEnabled(self) -> bool """
        return False

    def isDebugEnabled(self): # real signature unknown; restored from __doc__
        """ isDebugEnabled(self) -> bool """
        return False

    def isEnabled(self, type): # real signature unknown; restored from __doc__
        """ isEnabled(self, type: QtMsgType) -> bool """
        return False

    def isInfoEnabled(self): # real signature unknown; restored from __doc__
        """ isInfoEnabled(self) -> bool """
        return False

    def isWarningEnabled(self): # real signature unknown; restored from __doc__
        """ isWarningEnabled(self) -> bool """
        return False

    def setEnabled(self, type, enable): # real signature unknown; restored from __doc__
        """ setEnabled(self, type: QtMsgType, enable: bool) """
        pass

    def setFilterRules(self, rules, p_str=None): # real signature unknown; restored from __doc__
        """ setFilterRules(rules: Optional[str]) """
        pass

    def __call__(self, *args, **kwargs): # real signature unknown
        """ Call self as a function. """
        pass

    def __init__(self, category, p_str=None, *args=None, **kwargs=None): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



