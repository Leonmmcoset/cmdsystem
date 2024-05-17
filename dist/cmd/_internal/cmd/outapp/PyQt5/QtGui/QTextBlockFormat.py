# encoding: utf-8
# module PyQt5.QtGui
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtGui.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


from .QTextFormat import QTextFormat

class QTextBlockFormat(QTextFormat):
    """
    QTextBlockFormat()
    QTextBlockFormat(a0: QTextBlockFormat)
    """
    def alignment(self): # real signature unknown; restored from __doc__
        """ alignment(self) -> Qt.Alignment """
        pass

    def bottomMargin(self): # real signature unknown; restored from __doc__
        """ bottomMargin(self) -> float """
        return 0.0

    def headingLevel(self): # real signature unknown; restored from __doc__
        """ headingLevel(self) -> int """
        return 0

    def indent(self): # real signature unknown; restored from __doc__
        """ indent(self) -> int """
        return 0

    def isValid(self): # real signature unknown; restored from __doc__
        """ isValid(self) -> bool """
        return False

    def leftMargin(self): # real signature unknown; restored from __doc__
        """ leftMargin(self) -> float """
        return 0.0

    def lineHeight(self, scriptLineHeight=None, scaling=1): # real signature unknown; restored from __doc__ with multiple overloads
        """
        lineHeight(self) -> float
        lineHeight(self, scriptLineHeight: float, scaling: float = 1) -> float
        """
        return 0.0

    def lineHeightType(self): # real signature unknown; restored from __doc__
        """ lineHeightType(self) -> int """
        return 0

    def marker(self): # real signature unknown; restored from __doc__
        """ marker(self) -> QTextBlockFormat.MarkerType """
        pass

    def nonBreakableLines(self): # real signature unknown; restored from __doc__
        """ nonBreakableLines(self) -> bool """
        return False

    def pageBreakPolicy(self): # real signature unknown; restored from __doc__
        """ pageBreakPolicy(self) -> QTextFormat.PageBreakFlags """
        pass

    def rightMargin(self): # real signature unknown; restored from __doc__
        """ rightMargin(self) -> float """
        return 0.0

    def setAlignment(self, aalignment, Qt_Alignment=None, Qt_AlignmentFlag=None): # real signature unknown; restored from __doc__
        """ setAlignment(self, aalignment: Union[Qt.Alignment, Qt.AlignmentFlag]) """
        pass

    def setBottomMargin(self, margin): # real signature unknown; restored from __doc__
        """ setBottomMargin(self, margin: float) """
        pass

    def setHeadingLevel(self, alevel): # real signature unknown; restored from __doc__
        """ setHeadingLevel(self, alevel: int) """
        pass

    def setIndent(self, aindent): # real signature unknown; restored from __doc__
        """ setIndent(self, aindent: int) """
        pass

    def setLeftMargin(self, margin): # real signature unknown; restored from __doc__
        """ setLeftMargin(self, margin: float) """
        pass

    def setLineHeight(self, height, heightType): # real signature unknown; restored from __doc__
        """ setLineHeight(self, height: float, heightType: int) """
        pass

    def setMarker(self, marker): # real signature unknown; restored from __doc__
        """ setMarker(self, marker: QTextBlockFormat.MarkerType) """
        pass

    def setNonBreakableLines(self, b): # real signature unknown; restored from __doc__
        """ setNonBreakableLines(self, b: bool) """
        pass

    def setPageBreakPolicy(self, flags, QTextFormat_PageBreakFlags=None, QTextFormat_PageBreakFlag=None): # real signature unknown; restored from __doc__
        """ setPageBreakPolicy(self, flags: Union[QTextFormat.PageBreakFlags, QTextFormat.PageBreakFlag]) """
        pass

    def setRightMargin(self, margin): # real signature unknown; restored from __doc__
        """ setRightMargin(self, margin: float) """
        pass

    def setTabPositions(self, tabs, QTextOption_Tab=None): # real signature unknown; restored from __doc__
        """ setTabPositions(self, tabs: Iterable[QTextOption.Tab]) """
        pass

    def setTextIndent(self, margin): # real signature unknown; restored from __doc__
        """ setTextIndent(self, margin: float) """
        pass

    def setTopMargin(self, margin): # real signature unknown; restored from __doc__
        """ setTopMargin(self, margin: float) """
        pass

    def tabPositions(self): # real signature unknown; restored from __doc__
        """ tabPositions(self) -> List[QTextOption.Tab] """
        return []

    def textIndent(self): # real signature unknown; restored from __doc__
        """ textIndent(self) -> float """
        return 0.0

    def topMargin(self): # real signature unknown; restored from __doc__
        """ topMargin(self) -> float """
        return 0.0

    def __init__(self, a0=None): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    FixedHeight = 2
    LineDistanceHeight = 4
    MinimumHeight = 3
    ProportionalHeight = 1
    SingleHeight = 0


