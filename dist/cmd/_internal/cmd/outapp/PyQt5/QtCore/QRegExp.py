# encoding: utf-8
# module PyQt5.QtCore
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtCore.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum
import sip as __sip


class QRegExp(__sip.simplewrapper):
    """
    QRegExp()
    QRegExp(pattern: Optional[str], cs: Qt.CaseSensitivity = Qt.CaseSensitive, syntax: QRegExp.PatternSyntax = QRegExp.RegExp)
    QRegExp(rx: QRegExp)
    """
    def cap(self, nth=0): # real signature unknown; restored from __doc__
        """ cap(self, nth: int = 0) -> str """
        return ""

    def captureCount(self): # real signature unknown; restored from __doc__
        """ captureCount(self) -> int """
        return 0

    def capturedTexts(self): # real signature unknown; restored from __doc__
        """ capturedTexts(self) -> List[str] """
        return []

    def caseSensitivity(self): # real signature unknown; restored from __doc__
        """ caseSensitivity(self) -> Qt.CaseSensitivity """
        pass

    def errorString(self): # real signature unknown; restored from __doc__
        """ errorString(self) -> str """
        return ""

    def escape(self, p_str, p_str=None): # real signature unknown; restored from __doc__
        """ escape(str: Optional[str]) -> str """
        return ""

    def exactMatch(self, p_str, p_str=None): # real signature unknown; restored from __doc__
        """ exactMatch(self, str: Optional[str]) -> bool """
        return False

    def indexIn(self, p_str, p_str=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ indexIn(self, str: Optional[str], offset: int = 0, caretMode: QRegExp.CaretMode = QRegExp.CaretAtZero) -> int """
        pass

    def isEmpty(self): # real signature unknown; restored from __doc__
        """ isEmpty(self) -> bool """
        return False

    def isMinimal(self): # real signature unknown; restored from __doc__
        """ isMinimal(self) -> bool """
        return False

    def isValid(self): # real signature unknown; restored from __doc__
        """ isValid(self) -> bool """
        return False

    def lastIndexIn(self, p_str, p_str=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ lastIndexIn(self, str: Optional[str], offset: int = -1, caretMode: QRegExp.CaretMode = QRegExp.CaretAtZero) -> int """
        pass

    def matchedLength(self): # real signature unknown; restored from __doc__
        """ matchedLength(self) -> int """
        return 0

    def pattern(self): # real signature unknown; restored from __doc__
        """ pattern(self) -> str """
        return ""

    def patternSyntax(self): # real signature unknown; restored from __doc__
        """ patternSyntax(self) -> QRegExp.PatternSyntax """
        pass

    def pos(self, nth=0): # real signature unknown; restored from __doc__
        """ pos(self, nth: int = 0) -> int """
        return 0

    def setCaseSensitivity(self, cs): # real signature unknown; restored from __doc__
        """ setCaseSensitivity(self, cs: Qt.CaseSensitivity) """
        pass

    def setMinimal(self, minimal): # real signature unknown; restored from __doc__
        """ setMinimal(self, minimal: bool) """
        pass

    def setPattern(self, pattern, p_str=None): # real signature unknown; restored from __doc__
        """ setPattern(self, pattern: Optional[str]) """
        pass

    def setPatternSyntax(self, syntax): # real signature unknown; restored from __doc__
        """ setPatternSyntax(self, syntax: QRegExp.PatternSyntax) """
        pass

    def swap(self, other): # real signature unknown; restored from __doc__
        """ swap(self, other: QRegExp) """
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

    def __hash__(self, *args, **kwargs): # real signature unknown
        """ Return hash(self). """
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

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    CaretAtOffset = 1
    CaretAtZero = 0
    CaretWontMatch = 2
    FixedString = 2
    RegExp = 0
    RegExp2 = 3
    W3CXmlSchema11 = 5
    Wildcard = 1
    WildcardUnix = 4


