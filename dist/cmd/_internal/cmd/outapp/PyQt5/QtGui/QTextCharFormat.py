# encoding: utf-8
# module PyQt5.QtGui
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtGui.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


from .QTextFormat import QTextFormat

class QTextCharFormat(QTextFormat):
    """
    QTextCharFormat()
    QTextCharFormat(a0: QTextCharFormat)
    """
    def anchorHref(self): # real signature unknown; restored from __doc__
        """ anchorHref(self) -> str """
        return ""

    def anchorNames(self): # real signature unknown; restored from __doc__
        """ anchorNames(self) -> List[str] """
        return []

    def font(self): # real signature unknown; restored from __doc__
        """ font(self) -> QFont """
        return QFont

    def fontCapitalization(self): # real signature unknown; restored from __doc__
        """ fontCapitalization(self) -> QFont.Capitalization """
        pass

    def fontFamilies(self): # real signature unknown; restored from __doc__
        """ fontFamilies(self) -> Any """
        pass

    def fontFamily(self): # real signature unknown; restored from __doc__
        """ fontFamily(self) -> str """
        return ""

    def fontFixedPitch(self): # real signature unknown; restored from __doc__
        """ fontFixedPitch(self) -> bool """
        return False

    def fontHintingPreference(self): # real signature unknown; restored from __doc__
        """ fontHintingPreference(self) -> QFont.HintingPreference """
        pass

    def fontItalic(self): # real signature unknown; restored from __doc__
        """ fontItalic(self) -> bool """
        return False

    def fontKerning(self): # real signature unknown; restored from __doc__
        """ fontKerning(self) -> bool """
        return False

    def fontLetterSpacing(self): # real signature unknown; restored from __doc__
        """ fontLetterSpacing(self) -> float """
        return 0.0

    def fontLetterSpacingType(self): # real signature unknown; restored from __doc__
        """ fontLetterSpacingType(self) -> QFont.SpacingType """
        pass

    def fontOverline(self): # real signature unknown; restored from __doc__
        """ fontOverline(self) -> bool """
        return False

    def fontPointSize(self): # real signature unknown; restored from __doc__
        """ fontPointSize(self) -> float """
        return 0.0

    def fontStretch(self): # real signature unknown; restored from __doc__
        """ fontStretch(self) -> int """
        return 0

    def fontStrikeOut(self): # real signature unknown; restored from __doc__
        """ fontStrikeOut(self) -> bool """
        return False

    def fontStyleHint(self): # real signature unknown; restored from __doc__
        """ fontStyleHint(self) -> QFont.StyleHint """
        pass

    def fontStyleName(self): # real signature unknown; restored from __doc__
        """ fontStyleName(self) -> Any """
        pass

    def fontStyleStrategy(self): # real signature unknown; restored from __doc__
        """ fontStyleStrategy(self) -> QFont.StyleStrategy """
        pass

    def fontUnderline(self): # real signature unknown; restored from __doc__
        """ fontUnderline(self) -> bool """
        return False

    def fontWeight(self): # real signature unknown; restored from __doc__
        """ fontWeight(self) -> int """
        return 0

    def fontWordSpacing(self): # real signature unknown; restored from __doc__
        """ fontWordSpacing(self) -> float """
        return 0.0

    def isAnchor(self): # real signature unknown; restored from __doc__
        """ isAnchor(self) -> bool """
        return False

    def isValid(self): # real signature unknown; restored from __doc__
        """ isValid(self) -> bool """
        return False

    def setAnchor(self, anchor): # real signature unknown; restored from __doc__
        """ setAnchor(self, anchor: bool) """
        pass

    def setAnchorHref(self, value, p_str=None): # real signature unknown; restored from __doc__
        """ setAnchorHref(self, value: Optional[str]) """
        pass

    def setAnchorNames(self, names, Optional=None, p_str=None): # real signature unknown; restored from __doc__
        """ setAnchorNames(self, names: Iterable[Optional[str]]) """
        pass

    def setFont(self, font, behavior=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setFont(self, font: QFont)
        setFont(self, font: QFont, behavior: QTextCharFormat.FontPropertiesInheritanceBehavior)
        """
        pass

    def setFontCapitalization(self, capitalization): # real signature unknown; restored from __doc__
        """ setFontCapitalization(self, capitalization: QFont.Capitalization) """
        pass

    def setFontFamilies(self, families, Optional=None, p_str=None): # real signature unknown; restored from __doc__
        """ setFontFamilies(self, families: Iterable[Optional[str]]) """
        pass

    def setFontFamily(self, family, p_str=None): # real signature unknown; restored from __doc__
        """ setFontFamily(self, family: Optional[str]) """
        pass

    def setFontFixedPitch(self, fixedPitch): # real signature unknown; restored from __doc__
        """ setFontFixedPitch(self, fixedPitch: bool) """
        pass

    def setFontHintingPreference(self, hintingPreference): # real signature unknown; restored from __doc__
        """ setFontHintingPreference(self, hintingPreference: QFont.HintingPreference) """
        pass

    def setFontItalic(self, italic): # real signature unknown; restored from __doc__
        """ setFontItalic(self, italic: bool) """
        pass

    def setFontKerning(self, enable): # real signature unknown; restored from __doc__
        """ setFontKerning(self, enable: bool) """
        pass

    def setFontLetterSpacing(self, spacing): # real signature unknown; restored from __doc__
        """ setFontLetterSpacing(self, spacing: float) """
        pass

    def setFontLetterSpacingType(self, letterSpacingType): # real signature unknown; restored from __doc__
        """ setFontLetterSpacingType(self, letterSpacingType: QFont.SpacingType) """
        pass

    def setFontOverline(self, overline): # real signature unknown; restored from __doc__
        """ setFontOverline(self, overline: bool) """
        pass

    def setFontPointSize(self, size): # real signature unknown; restored from __doc__
        """ setFontPointSize(self, size: float) """
        pass

    def setFontStretch(self, factor): # real signature unknown; restored from __doc__
        """ setFontStretch(self, factor: int) """
        pass

    def setFontStrikeOut(self, strikeOut): # real signature unknown; restored from __doc__
        """ setFontStrikeOut(self, strikeOut: bool) """
        pass

    def setFontStyleHint(self, hint, strategy=None): # real signature unknown; restored from __doc__
        """ setFontStyleHint(self, hint: QFont.StyleHint, strategy: QFont.StyleStrategy = QFont.PreferDefault) """
        pass

    def setFontStyleName(self, styleName, p_str=None): # real signature unknown; restored from __doc__
        """ setFontStyleName(self, styleName: Optional[str]) """
        pass

    def setFontStyleStrategy(self, strategy): # real signature unknown; restored from __doc__
        """ setFontStyleStrategy(self, strategy: QFont.StyleStrategy) """
        pass

    def setFontUnderline(self, underline): # real signature unknown; restored from __doc__
        """ setFontUnderline(self, underline: bool) """
        pass

    def setFontWeight(self, weight): # real signature unknown; restored from __doc__
        """ setFontWeight(self, weight: int) """
        pass

    def setFontWordSpacing(self, spacing): # real signature unknown; restored from __doc__
        """ setFontWordSpacing(self, spacing: float) """
        pass

    def setTableCellColumnSpan(self, atableCellColumnSpan): # real signature unknown; restored from __doc__
        """ setTableCellColumnSpan(self, atableCellColumnSpan: int) """
        pass

    def setTableCellRowSpan(self, atableCellRowSpan): # real signature unknown; restored from __doc__
        """ setTableCellRowSpan(self, atableCellRowSpan: int) """
        pass

    def setTextOutline(self, pen, QPen=None, Union=None, QColor=None, Qt_GlobalColor=None): # real signature unknown; restored from __doc__
        """ setTextOutline(self, pen: Union[QPen, Union[QColor, Qt.GlobalColor]]) """
        pass

    def setToolTip(self, tip, p_str=None): # real signature unknown; restored from __doc__
        """ setToolTip(self, tip: Optional[str]) """
        pass

    def setUnderlineColor(self, color, QColor=None, Qt_GlobalColor=None): # real signature unknown; restored from __doc__
        """ setUnderlineColor(self, color: Union[QColor, Qt.GlobalColor]) """
        pass

    def setUnderlineStyle(self, style): # real signature unknown; restored from __doc__
        """ setUnderlineStyle(self, style: QTextCharFormat.UnderlineStyle) """
        pass

    def setVerticalAlignment(self, alignment): # real signature unknown; restored from __doc__
        """ setVerticalAlignment(self, alignment: QTextCharFormat.VerticalAlignment) """
        pass

    def tableCellColumnSpan(self): # real signature unknown; restored from __doc__
        """ tableCellColumnSpan(self) -> int """
        return 0

    def tableCellRowSpan(self): # real signature unknown; restored from __doc__
        """ tableCellRowSpan(self) -> int """
        return 0

    def textOutline(self): # real signature unknown; restored from __doc__
        """ textOutline(self) -> QPen """
        return QPen

    def toolTip(self): # real signature unknown; restored from __doc__
        """ toolTip(self) -> str """
        return ""

    def underlineColor(self): # real signature unknown; restored from __doc__
        """ underlineColor(self) -> QColor """
        return QColor

    def underlineStyle(self): # real signature unknown; restored from __doc__
        """ underlineStyle(self) -> QTextCharFormat.UnderlineStyle """
        pass

    def verticalAlignment(self): # real signature unknown; restored from __doc__
        """ verticalAlignment(self) -> QTextCharFormat.VerticalAlignment """
        pass

    def __init__(self, a0=None): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    AlignBaseline = 6
    AlignBottom = 5
    AlignMiddle = 3
    AlignNormal = 0
    AlignSubScript = 2
    AlignSuperScript = 1
    AlignTop = 4
    DashDotDotLine = 5
    DashDotLine = 4
    DashUnderline = 2
    DotLine = 3
    FontPropertiesAll = 1
    FontPropertiesSpecifiedOnly = 0
    NoUnderline = 0
    SingleUnderline = 1
    SpellCheckUnderline = 7
    WaveUnderline = 6


