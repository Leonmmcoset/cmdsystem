# encoding: utf-8
# module PyQt5.QtGui
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtGui.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


class QColor(__sip.simplewrapper):
    """
    QColor(color: Qt.GlobalColor)
    QColor(rgb: int)
    QColor(rgba64: QRgba64)
    QColor(variant: Any)
    QColor()
    QColor(r: int, g: int, b: int, alpha: int = 255)
    QColor(aname: Optional[str])
    QColor(acolor: Union[QColor, Qt.GlobalColor])
    """
    def alpha(self): # real signature unknown; restored from __doc__
        """ alpha(self) -> int """
        return 0

    def alphaF(self): # real signature unknown; restored from __doc__
        """ alphaF(self) -> float """
        return 0.0

    def black(self): # real signature unknown; restored from __doc__
        """ black(self) -> int """
        return 0

    def blackF(self): # real signature unknown; restored from __doc__
        """ blackF(self) -> float """
        return 0.0

    def blue(self): # real signature unknown; restored from __doc__
        """ blue(self) -> int """
        return 0

    def blueF(self): # real signature unknown; restored from __doc__
        """ blueF(self) -> float """
        return 0.0

    def colorNames(self): # real signature unknown; restored from __doc__
        """ colorNames() -> List[str] """
        return []

    def convertTo(self, colorSpec): # real signature unknown; restored from __doc__
        """ convertTo(self, colorSpec: QColor.Spec) -> QColor """
        return QColor

    def cyan(self): # real signature unknown; restored from __doc__
        """ cyan(self) -> int """
        return 0

    def cyanF(self): # real signature unknown; restored from __doc__
        """ cyanF(self) -> float """
        return 0.0

    def darker(self, factor=200): # real signature unknown; restored from __doc__
        """ darker(self, factor: int = 200) -> QColor """
        return QColor

    def fromCmyk(self, c, m, y, k, alpha=255): # real signature unknown; restored from __doc__
        """ fromCmyk(c: int, m: int, y: int, k: int, alpha: int = 255) -> QColor """
        return QColor

    def fromCmykF(self, c, m, y, k, alpha=1): # real signature unknown; restored from __doc__
        """ fromCmykF(c: float, m: float, y: float, k: float, alpha: float = 1) -> QColor """
        return QColor

    def fromHsl(self, h, s, l, alpha=255): # real signature unknown; restored from __doc__
        """ fromHsl(h: int, s: int, l: int, alpha: int = 255) -> QColor """
        return QColor

    def fromHslF(self, h, s, l, alpha=1): # real signature unknown; restored from __doc__
        """ fromHslF(h: float, s: float, l: float, alpha: float = 1) -> QColor """
        return QColor

    def fromHsv(self, h, s, v, alpha=255): # real signature unknown; restored from __doc__
        """ fromHsv(h: int, s: int, v: int, alpha: int = 255) -> QColor """
        return QColor

    def fromHsvF(self, h, s, v, alpha=1): # real signature unknown; restored from __doc__
        """ fromHsvF(h: float, s: float, v: float, alpha: float = 1) -> QColor """
        return QColor

    def fromRgb(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        fromRgb(rgb: int) -> QColor
        fromRgb(r: int, g: int, b: int, alpha: int = 255) -> QColor
        """
        return QColor

    def fromRgba(self, rgba): # real signature unknown; restored from __doc__
        """ fromRgba(rgba: int) -> QColor """
        return QColor

    def fromRgba64(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        fromRgba64(r: int, g: int, b: int, alpha: int = 65535) -> QColor
        fromRgba64(rgba: QRgba64) -> QColor
        """
        return QColor

    def fromRgbF(self, r, g, b, alpha=1): # real signature unknown; restored from __doc__
        """ fromRgbF(r: float, g: float, b: float, alpha: float = 1) -> QColor """
        return QColor

    def getCmyk(self): # real signature unknown; restored from __doc__
        """ getCmyk(self) -> (Optional[int], Optional[int], Optional[int], Optional[int], Optional[int]) """
        pass

    def getCmykF(self): # real signature unknown; restored from __doc__
        """ getCmykF(self) -> (Optional[float], Optional[float], Optional[float], Optional[float], Optional[float]) """
        pass

    def getHsl(self): # real signature unknown; restored from __doc__
        """ getHsl(self) -> (Optional[int], Optional[int], Optional[int], Optional[int]) """
        pass

    def getHslF(self): # real signature unknown; restored from __doc__
        """ getHslF(self) -> (Optional[float], Optional[float], Optional[float], Optional[float]) """
        pass

    def getHsv(self): # real signature unknown; restored from __doc__
        """ getHsv(self) -> (Optional[int], Optional[int], Optional[int], Optional[int]) """
        pass

    def getHsvF(self): # real signature unknown; restored from __doc__
        """ getHsvF(self) -> (Optional[float], Optional[float], Optional[float], Optional[float]) """
        pass

    def getRgb(self): # real signature unknown; restored from __doc__
        """ getRgb(self) -> (Optional[int], Optional[int], Optional[int], Optional[int]) """
        pass

    def getRgbF(self): # real signature unknown; restored from __doc__
        """ getRgbF(self) -> (Optional[float], Optional[float], Optional[float], Optional[float]) """
        pass

    def green(self): # real signature unknown; restored from __doc__
        """ green(self) -> int """
        return 0

    def greenF(self): # real signature unknown; restored from __doc__
        """ greenF(self) -> float """
        return 0.0

    def hslHue(self): # real signature unknown; restored from __doc__
        """ hslHue(self) -> int """
        return 0

    def hslHueF(self): # real signature unknown; restored from __doc__
        """ hslHueF(self) -> float """
        return 0.0

    def hslSaturation(self): # real signature unknown; restored from __doc__
        """ hslSaturation(self) -> int """
        return 0

    def hslSaturationF(self): # real signature unknown; restored from __doc__
        """ hslSaturationF(self) -> float """
        return 0.0

    def hsvHue(self): # real signature unknown; restored from __doc__
        """ hsvHue(self) -> int """
        return 0

    def hsvHueF(self): # real signature unknown; restored from __doc__
        """ hsvHueF(self) -> float """
        return 0.0

    def hsvSaturation(self): # real signature unknown; restored from __doc__
        """ hsvSaturation(self) -> int """
        return 0

    def hsvSaturationF(self): # real signature unknown; restored from __doc__
        """ hsvSaturationF(self) -> float """
        return 0.0

    def hue(self): # real signature unknown; restored from __doc__
        """ hue(self) -> int """
        return 0

    def hueF(self): # real signature unknown; restored from __doc__
        """ hueF(self) -> float """
        return 0.0

    def isValid(self): # real signature unknown; restored from __doc__
        """ isValid(self) -> bool """
        return False

    def isValidColor(self, name, p_str=None): # real signature unknown; restored from __doc__
        """ isValidColor(name: Optional[str]) -> bool """
        return False

    def lighter(self, factor=150): # real signature unknown; restored from __doc__
        """ lighter(self, factor: int = 150) -> QColor """
        return QColor

    def lightness(self): # real signature unknown; restored from __doc__
        """ lightness(self) -> int """
        return 0

    def lightnessF(self): # real signature unknown; restored from __doc__
        """ lightnessF(self) -> float """
        return 0.0

    def magenta(self): # real signature unknown; restored from __doc__
        """ magenta(self) -> int """
        return 0

    def magentaF(self): # real signature unknown; restored from __doc__
        """ magentaF(self) -> float """
        return 0.0

    def name(self, format=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        name(self) -> str
        name(self, format: QColor.NameFormat) -> str
        """
        return ""

    def red(self): # real signature unknown; restored from __doc__
        """ red(self) -> int """
        return 0

    def redF(self): # real signature unknown; restored from __doc__
        """ redF(self) -> float """
        return 0.0

    def rgb(self): # real signature unknown; restored from __doc__
        """ rgb(self) -> int """
        return 0

    def rgba(self): # real signature unknown; restored from __doc__
        """ rgba(self) -> int """
        return 0

    def rgba64(self): # real signature unknown; restored from __doc__
        """ rgba64(self) -> QRgba64 """
        return QRgba64

    def saturation(self): # real signature unknown; restored from __doc__
        """ saturation(self) -> int """
        return 0

    def saturationF(self): # real signature unknown; restored from __doc__
        """ saturationF(self) -> float """
        return 0.0

    def setAlpha(self, alpha): # real signature unknown; restored from __doc__
        """ setAlpha(self, alpha: int) """
        pass

    def setAlphaF(self, alpha): # real signature unknown; restored from __doc__
        """ setAlphaF(self, alpha: float) """
        pass

    def setBlue(self, blue): # real signature unknown; restored from __doc__
        """ setBlue(self, blue: int) """
        pass

    def setBlueF(self, blue): # real signature unknown; restored from __doc__
        """ setBlueF(self, blue: float) """
        pass

    def setCmyk(self, c, m, y, k, alpha=255): # real signature unknown; restored from __doc__
        """ setCmyk(self, c: int, m: int, y: int, k: int, alpha: int = 255) """
        pass

    def setCmykF(self, c, m, y, k, alpha=1): # real signature unknown; restored from __doc__
        """ setCmykF(self, c: float, m: float, y: float, k: float, alpha: float = 1) """
        pass

    def setGreen(self, green): # real signature unknown; restored from __doc__
        """ setGreen(self, green: int) """
        pass

    def setGreenF(self, green): # real signature unknown; restored from __doc__
        """ setGreenF(self, green: float) """
        pass

    def setHsl(self, h, s, l, alpha=255): # real signature unknown; restored from __doc__
        """ setHsl(self, h: int, s: int, l: int, alpha: int = 255) """
        pass

    def setHslF(self, h, s, l, alpha=1): # real signature unknown; restored from __doc__
        """ setHslF(self, h: float, s: float, l: float, alpha: float = 1) """
        pass

    def setHsv(self, h, s, v, alpha=255): # real signature unknown; restored from __doc__
        """ setHsv(self, h: int, s: int, v: int, alpha: int = 255) """
        pass

    def setHsvF(self, h, s, v, alpha=1): # real signature unknown; restored from __doc__
        """ setHsvF(self, h: float, s: float, v: float, alpha: float = 1) """
        pass

    def setNamedColor(self, name, p_str=None): # real signature unknown; restored from __doc__
        """ setNamedColor(self, name: Optional[str]) """
        pass

    def setRed(self, red): # real signature unknown; restored from __doc__
        """ setRed(self, red: int) """
        pass

    def setRedF(self, red): # real signature unknown; restored from __doc__
        """ setRedF(self, red: float) """
        pass

    def setRgb(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setRgb(self, r: int, g: int, b: int, alpha: int = 255)
        setRgb(self, rgb: int)
        """
        pass

    def setRgba(self, rgba): # real signature unknown; restored from __doc__
        """ setRgba(self, rgba: int) """
        pass

    def setRgba64(self, rgba): # real signature unknown; restored from __doc__
        """ setRgba64(self, rgba: QRgba64) """
        pass

    def setRgbF(self, r, g, b, alpha=1): # real signature unknown; restored from __doc__
        """ setRgbF(self, r: float, g: float, b: float, alpha: float = 1) """
        pass

    def spec(self): # real signature unknown; restored from __doc__
        """ spec(self) -> QColor.Spec """
        pass

    def toCmyk(self): # real signature unknown; restored from __doc__
        """ toCmyk(self) -> QColor """
        return QColor

    def toExtendedRgb(self): # real signature unknown; restored from __doc__
        """ toExtendedRgb(self) -> QColor """
        return QColor

    def toHsl(self): # real signature unknown; restored from __doc__
        """ toHsl(self) -> QColor """
        return QColor

    def toHsv(self): # real signature unknown; restored from __doc__
        """ toHsv(self) -> QColor """
        return QColor

    def toRgb(self): # real signature unknown; restored from __doc__
        """ toRgb(self) -> QColor """
        return QColor

    def value(self): # real signature unknown; restored from __doc__
        """ value(self) -> int """
        return 0

    def valueF(self): # real signature unknown; restored from __doc__
        """ valueF(self) -> float """
        return 0.0

    def yellow(self): # real signature unknown; restored from __doc__
        """ yellow(self) -> int """
        return 0

    def yellowF(self): # real signature unknown; restored from __doc__
        """ yellowF(self) -> float """
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

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    Cmyk = 3
    ExtendedRgb = 5
    HexArgb = 1
    HexRgb = 0
    Hsl = 4
    Hsv = 2
    Invalid = 0
    Rgb = 1
    __hash__ = None


