# encoding: utf-8
# module PyQt5.QtGui
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtGui.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


class QFontDatabase(__sip.simplewrapper):
    """
    QFontDatabase()
    QFontDatabase(a0: QFontDatabase)
    """
    def addApplicationFont(self, fileName, p_str=None): # real signature unknown; restored from __doc__
        """ addApplicationFont(fileName: Optional[str]) -> int """
        return 0

    def addApplicationFontFromData(self, fontData, QByteArray=None, bytes=None, bytearray=None): # real signature unknown; restored from __doc__
        """ addApplicationFontFromData(fontData: Union[QByteArray, bytes, bytearray]) -> int """
        return 0

    def applicationFontFamilies(self, id): # real signature unknown; restored from __doc__
        """ applicationFontFamilies(id: int) -> List[str] """
        return []

    def bold(self, family, p_str=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ bold(self, family: Optional[str], style: Optional[str]) -> bool """
        pass

    def families(self, writingSystem=None): # real signature unknown; restored from __doc__
        """ families(self, writingSystem: QFontDatabase.WritingSystem = QFontDatabase.Any) -> List[str] """
        return []

    def font(self, family, p_str=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ font(self, family: Optional[str], style: Optional[str], pointSize: int) -> QFont """
        pass

    def isBitmapScalable(self, family, p_str=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ isBitmapScalable(self, family: Optional[str], style: Optional[str] = '') -> bool """
        pass

    def isFixedPitch(self, family, p_str=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ isFixedPitch(self, family: Optional[str], style: Optional[str] = '') -> bool """
        pass

    def isPrivateFamily(self, family, p_str=None): # real signature unknown; restored from __doc__
        """ isPrivateFamily(self, family: Optional[str]) -> bool """
        return False

    def isScalable(self, family, p_str=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ isScalable(self, family: Optional[str], style: Optional[str] = '') -> bool """
        pass

    def isSmoothlyScalable(self, family, p_str=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ isSmoothlyScalable(self, family: Optional[str], style: Optional[str] = '') -> bool """
        pass

    def italic(self, family, p_str=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ italic(self, family: Optional[str], style: Optional[str]) -> bool """
        pass

    def pointSizes(self, family, p_str=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ pointSizes(self, family: Optional[str], style: Optional[str] = '') -> List[int] """
        pass

    def removeAllApplicationFonts(self): # real signature unknown; restored from __doc__
        """ removeAllApplicationFonts() -> bool """
        return False

    def removeApplicationFont(self, id): # real signature unknown; restored from __doc__
        """ removeApplicationFont(id: int) -> bool """
        return False

    def smoothSizes(self, family, p_str=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ smoothSizes(self, family: Optional[str], style: Optional[str]) -> List[int] """
        pass

    def standardSizes(self): # real signature unknown; restored from __doc__
        """ standardSizes() -> List[int] """
        return []

    def styles(self, family, p_str=None): # real signature unknown; restored from __doc__
        """ styles(self, family: Optional[str]) -> List[str] """
        return []

    def styleString(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        styleString(self, font: QFont) -> str
        styleString(self, fontInfo: QFontInfo) -> str
        """
        return ""

    def supportsThreadedFontRendering(self): # real signature unknown; restored from __doc__
        """ supportsThreadedFontRendering() -> bool """
        return False

    def systemFont(self, type): # real signature unknown; restored from __doc__
        """ systemFont(type: QFontDatabase.SystemFont) -> QFont """
        return QFont

    def weight(self, family, p_str=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ weight(self, family: Optional[str], style: Optional[str]) -> int """
        pass

    def writingSystemName(self, writingSystem): # real signature unknown; restored from __doc__
        """ writingSystemName(writingSystem: QFontDatabase.WritingSystem) -> str """
        return ""

    def writingSystems(self, family=None, p_str=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        writingSystems(self) -> List[QFontDatabase.WritingSystem]
        writingSystems(self, family: Optional[str]) -> List[QFontDatabase.WritingSystem]
        """
        return []

    def writingSystemSample(self, writingSystem): # real signature unknown; restored from __doc__
        """ writingSystemSample(writingSystem: QFontDatabase.WritingSystem) -> str """
        return ""

    def __init__(self, a0=None): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    Any = 0
    Arabic = 6
    Armenian = 4
    Bengali = 10
    Cyrillic = 3
    Devanagari = 9
    FixedFont = 1
    GeneralFont = 0
    Georgian = 23
    Greek = 2
    Gujarati = 12
    Gurmukhi = 11
    Hebrew = 5
    Japanese = 27
    Kannada = 16
    Khmer = 24
    Korean = 28
    Lao = 20
    Latin = 1
    Malayalam = 17
    Myanmar = 22
    Nko = 33
    Ogham = 31
    Oriya = 13
    Other = 30
    Runic = 32
    SimplifiedChinese = 25
    Sinhala = 18
    SmallestReadableFont = 3
    Symbol = 30
    Syriac = 7
    Tamil = 14
    Telugu = 15
    Thaana = 8
    Thai = 19
    Tibetan = 21
    TitleFont = 2
    TraditionalChinese = 26
    Vietnamese = 29


