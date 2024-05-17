# encoding: utf-8
# module PyQt5.QtCore
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtCore.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum
import sip as __sip


class QCommandLineOption(__sip.simplewrapper):
    """
    QCommandLineOption(name: Optional[str])
    QCommandLineOption(names: Iterable[Optional[str]])
    QCommandLineOption(name: Optional[str], description: Optional[str], valueName: Optional[str] = '', defaultValue: Optional[str] = '')
    QCommandLineOption(names: Iterable[Optional[str]], description: Optional[str], valueName: Optional[str] = '', defaultValue: Optional[str] = '')
    QCommandLineOption(other: QCommandLineOption)
    """
    def defaultValues(self): # real signature unknown; restored from __doc__
        """ defaultValues(self) -> List[str] """
        return []

    def description(self): # real signature unknown; restored from __doc__
        """ description(self) -> str """
        return ""

    def flags(self): # real signature unknown; restored from __doc__
        """ flags(self) -> QCommandLineOption.Flags """
        pass

    def isHidden(self): # real signature unknown; restored from __doc__
        """ isHidden(self) -> bool """
        return False

    def names(self): # real signature unknown; restored from __doc__
        """ names(self) -> List[str] """
        return []

    def setDefaultValue(self, defaultValue, p_str=None): # real signature unknown; restored from __doc__
        """ setDefaultValue(self, defaultValue: Optional[str]) """
        pass

    def setDefaultValues(self, defaultValues, Optional=None, p_str=None): # real signature unknown; restored from __doc__
        """ setDefaultValues(self, defaultValues: Iterable[Optional[str]]) """
        pass

    def setDescription(self, description, p_str=None): # real signature unknown; restored from __doc__
        """ setDescription(self, description: Optional[str]) """
        pass

    def setFlags(self, aflags, QCommandLineOption_Flags=None, QCommandLineOption_Flag=None): # real signature unknown; restored from __doc__
        """ setFlags(self, aflags: Union[QCommandLineOption.Flags, QCommandLineOption.Flag]) """
        pass

    def setHidden(self, hidden): # real signature unknown; restored from __doc__
        """ setHidden(self, hidden: bool) """
        pass

    def setValueName(self, name, p_str=None): # real signature unknown; restored from __doc__
        """ setValueName(self, name: Optional[str]) """
        pass

    def swap(self, other): # real signature unknown; restored from __doc__
        """ swap(self, other: QCommandLineOption) """
        pass

    def valueName(self): # real signature unknown; restored from __doc__
        """ valueName(self) -> str """
        return ""

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    HiddenFromHelp = 1
    ShortOptionStyle = 2


