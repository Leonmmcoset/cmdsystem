# encoding: utf-8
# module PyQt5.QtGui
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtGui.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


class QFont(__sip.simplewrapper):
    """
    QFont()
    QFont(family: Optional[str], pointSize: int = -1, weight: int = -1, italic: bool = False)
    QFont(a0: QFont, pd: Optional[QPaintDevice])
    QFont(a0: QFont)
    QFont(variant: Any)
    """
    def bold(self): # real signature unknown; restored from __doc__
        """ bold(self) -> bool """
        return False

    def cacheStatistics(self): # real signature unknown; restored from __doc__
        """ cacheStatistics() """
        pass

    def capitalization(self): # real signature unknown; restored from __doc__
        """ capitalization(self) -> QFont.Capitalization """
        pass

    def cleanup(self): # real signature unknown; restored from __doc__
        """ cleanup() """
        pass

    def defaultFamily(self): # real signature unknown; restored from __doc__
        """ defaultFamily(self) -> str """
        return ""

    def exactMatch(self): # real signature unknown; restored from __doc__
        """ exactMatch(self) -> bool """
        return False

    def families(self): # real signature unknown; restored from __doc__
        """ families(self) -> List[str] """
        return []

    def family(self): # real signature unknown; restored from __doc__
        """ family(self) -> str """
        return ""

    def fixedPitch(self): # real signature unknown; restored from __doc__
        """ fixedPitch(self) -> bool """
        return False

    def fromString(self, a0, p_str=None): # real signature unknown; restored from __doc__
        """ fromString(self, a0: Optional[str]) -> bool """
        return False

    def hintingPreference(self): # real signature unknown; restored from __doc__
        """ hintingPreference(self) -> QFont.HintingPreference """
        pass

    def initialize(self): # real signature unknown; restored from __doc__
        """ initialize() """
        pass

    def insertSubstitution(self, a0, p_str=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ insertSubstitution(a0: Optional[str], a1: Optional[str]) """
        pass

    def insertSubstitutions(self, a0, p_str=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ insertSubstitutions(a0: Optional[str], a1: Iterable[Optional[str]]) """
        pass

    def isCopyOf(self, a0): # real signature unknown; restored from __doc__
        """ isCopyOf(self, a0: QFont) -> bool """
        return False

    def italic(self): # real signature unknown; restored from __doc__
        """ italic(self) -> bool """
        return False

    def kerning(self): # real signature unknown; restored from __doc__
        """ kerning(self) -> bool """
        return False

    def key(self): # real signature unknown; restored from __doc__
        """ key(self) -> str """
        return ""

    def lastResortFamily(self): # real signature unknown; restored from __doc__
        """ lastResortFamily(self) -> str """
        return ""

    def lastResortFont(self): # real signature unknown; restored from __doc__
        """ lastResortFont(self) -> str """
        return ""

    def letterSpacing(self): # real signature unknown; restored from __doc__
        """ letterSpacing(self) -> float """
        return 0.0

    def letterSpacingType(self): # real signature unknown; restored from __doc__
        """ letterSpacingType(self) -> QFont.SpacingType """
        pass

    def overline(self): # real signature unknown; restored from __doc__
        """ overline(self) -> bool """
        return False

    def pixelSize(self): # real signature unknown; restored from __doc__
        """ pixelSize(self) -> int """
        return 0

    def pointSize(self): # real signature unknown; restored from __doc__
        """ pointSize(self) -> int """
        return 0

    def pointSizeF(self): # real signature unknown; restored from __doc__
        """ pointSizeF(self) -> float """
        return 0.0

    def rawMode(self): # real signature unknown; restored from __doc__
        """ rawMode(self) -> bool """
        return False

    def rawName(self): # real signature unknown; restored from __doc__
        """ rawName(self) -> str """
        return ""

    def removeSubstitutions(self, a0, p_str=None): # real signature unknown; restored from __doc__
        """ removeSubstitutions(a0: Optional[str]) """
        pass

    def resolve(self, a0): # real signature unknown; restored from __doc__
        """ resolve(self, a0: QFont) -> QFont """
        return QFont

    def setBold(self, enable): # real signature unknown; restored from __doc__
        """ setBold(self, enable: bool) """
        pass

    def setCapitalization(self, a0): # real signature unknown; restored from __doc__
        """ setCapitalization(self, a0: QFont.Capitalization) """
        pass

    def setFamilies(self, a0, Optional=None, p_str=None): # real signature unknown; restored from __doc__
        """ setFamilies(self, a0: Iterable[Optional[str]]) """
        pass

    def setFamily(self, a0, p_str=None): # real signature unknown; restored from __doc__
        """ setFamily(self, a0: Optional[str]) """
        pass

    def setFixedPitch(self, a0): # real signature unknown; restored from __doc__
        """ setFixedPitch(self, a0: bool) """
        pass

    def setHintingPreference(self, hintingPreference): # real signature unknown; restored from __doc__
        """ setHintingPreference(self, hintingPreference: QFont.HintingPreference) """
        pass

    def setItalic(self, b): # real signature unknown; restored from __doc__
        """ setItalic(self, b: bool) """
        pass

    def setKerning(self, a0): # real signature unknown; restored from __doc__
        """ setKerning(self, a0: bool) """
        pass

    def setLetterSpacing(self, type, spacing): # real signature unknown; restored from __doc__
        """ setLetterSpacing(self, type: QFont.SpacingType, spacing: float) """
        pass

    def setOverline(self, a0): # real signature unknown; restored from __doc__
        """ setOverline(self, a0: bool) """
        pass

    def setPixelSize(self, a0): # real signature unknown; restored from __doc__
        """ setPixelSize(self, a0: int) """
        pass

    def setPointSize(self, a0): # real signature unknown; restored from __doc__
        """ setPointSize(self, a0: int) """
        pass

    def setPointSizeF(self, a0): # real signature unknown; restored from __doc__
        """ setPointSizeF(self, a0: float) """
        pass

    def setRawMode(self, a0): # real signature unknown; restored from __doc__
        """ setRawMode(self, a0: bool) """
        pass

    def setRawName(self, a0, p_str=None): # real signature unknown; restored from __doc__
        """ setRawName(self, a0: Optional[str]) """
        pass

    def setStretch(self, a0): # real signature unknown; restored from __doc__
        """ setStretch(self, a0: int) """
        pass

    def setStrikeOut(self, a0): # real signature unknown; restored from __doc__
        """ setStrikeOut(self, a0: bool) """
        pass

    def setStyle(self, style): # real signature unknown; restored from __doc__
        """ setStyle(self, style: QFont.Style) """
        pass

    def setStyleHint(self, hint, strategy=None): # real signature unknown; restored from __doc__
        """ setStyleHint(self, hint: QFont.StyleHint, strategy: QFont.StyleStrategy = QFont.PreferDefault) """
        pass

    def setStyleName(self, styleName, p_str=None): # real signature unknown; restored from __doc__
        """ setStyleName(self, styleName: Optional[str]) """
        pass

    def setStyleStrategy(self, s): # real signature unknown; restored from __doc__
        """ setStyleStrategy(self, s: QFont.StyleStrategy) """
        pass

    def setUnderline(self, a0): # real signature unknown; restored from __doc__
        """ setUnderline(self, a0: bool) """
        pass

    def setWeight(self, a0): # real signature unknown; restored from __doc__
        """ setWeight(self, a0: int) """
        pass

    def setWordSpacing(self, spacing): # real signature unknown; restored from __doc__
        """ setWordSpacing(self, spacing: float) """
        pass

    def stretch(self): # real signature unknown; restored from __doc__
        """ stretch(self) -> int """
        return 0

    def strikeOut(self): # real signature unknown; restored from __doc__
        """ strikeOut(self) -> bool """
        return False

    def style(self): # real signature unknown; restored from __doc__
        """ style(self) -> QFont.Style """
        pass

    def styleHint(self): # real signature unknown; restored from __doc__
        """ styleHint(self) -> QFont.StyleHint """
        pass

    def styleName(self): # real signature unknown; restored from __doc__
        """ styleName(self) -> str """
        return ""

    def styleStrategy(self): # real signature unknown; restored from __doc__
        """ styleStrategy(self) -> QFont.StyleStrategy """
        pass

    def substitute(self, a0, p_str=None): # real signature unknown; restored from __doc__
        """ substitute(a0: Optional[str]) -> str """
        return ""

    def substitutes(self, a0, p_str=None): # real signature unknown; restored from __doc__
        """ substitutes(a0: Optional[str]) -> List[str] """
        return []

    def substitutions(self): # real signature unknown; restored from __doc__
        """ substitutions() -> List[str] """
        return []

    def swap(self, other): # real signature unknown; restored from __doc__
        """ swap(self, other: QFont) """
        pass

    def toString(self): # real signature unknown; restored from __doc__
        """ toString(self) -> str """
        return ""

    def underline(self): # real signature unknown; restored from __doc__
        """ underline(self) -> bool """
        return False

    def weight(self): # real signature unknown; restored from __doc__
        """ weight(self) -> int """
        return 0

    def wordSpacing(self): # real signature unknown; restored from __doc__
        """ wordSpacing(self) -> float """
        return 0.0

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

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    AbsoluteSpacing = 1
    AllLowercase = 2
    AllUppercase = 1
    AnyStretch = 0
    AnyStyle = 5
    Black = 87
    Bold = 75
    Capitalize = 4
    Condensed = 75
    Courier = 2
    Cursive = 6
    Decorative = 3
    DemiBold = 63
    Expanded = 125
    ExtraBold = 81
    ExtraCondensed = 62
    ExtraExpanded = 150
    ExtraLight = 12
    Fantasy = 8
    ForceIntegerMetrics = 1024
    ForceOutline = 16
    Helvetica = 0
    Light = 25
    Medium = 57
    MixedCase = 0
    Monospace = 7
    NoAntialias = 256
    NoFontMerging = 32768
    Normal = 50
    NoSubpixelAntialias = 2048
    OldEnglish = 3
    OpenGLCompatible = 512
    PercentageSpacing = 0
    PreferAntialias = 128
    PreferBitmap = 2
    PreferDefault = 1
    PreferDefaultHinting = 0
    PreferDevice = 4
    PreferFullHinting = 3
    PreferMatch = 32
    PreferNoHinting = 1
    PreferNoShaping = 4096
    PreferOutline = 8
    PreferQuality = 64
    PreferVerticalHinting = 2
    SansSerif = 0
    SemiCondensed = 87
    SemiExpanded = 112
    Serif = 1
    SmallCaps = 3
    StyleItalic = 1
    StyleNormal = 0
    StyleOblique = 2
    System = 4
    Thin = 0
    Times = 1
    TypeWriter = 2
    UltraCondensed = 50
    UltraExpanded = 200
    Unstretched = 100


