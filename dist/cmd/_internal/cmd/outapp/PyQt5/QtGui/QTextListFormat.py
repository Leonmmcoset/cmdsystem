# encoding: utf-8
# module PyQt5.QtGui
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtGui.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


from .QTextFormat import QTextFormat

class QTextListFormat(QTextFormat):
    """
    QTextListFormat()
    QTextListFormat(a0: QTextListFormat)
    """
    def indent(self): # real signature unknown; restored from __doc__
        """ indent(self) -> int """
        return 0

    def isValid(self): # real signature unknown; restored from __doc__
        """ isValid(self) -> bool """
        return False

    def numberPrefix(self): # real signature unknown; restored from __doc__
        """ numberPrefix(self) -> str """
        return ""

    def numberSuffix(self): # real signature unknown; restored from __doc__
        """ numberSuffix(self) -> str """
        return ""

    def setIndent(self, aindent): # real signature unknown; restored from __doc__
        """ setIndent(self, aindent: int) """
        pass

    def setNumberPrefix(self, np, p_str=None): # real signature unknown; restored from __doc__
        """ setNumberPrefix(self, np: Optional[str]) """
        pass

    def setNumberSuffix(self, ns, p_str=None): # real signature unknown; restored from __doc__
        """ setNumberSuffix(self, ns: Optional[str]) """
        pass

    def setStyle(self, astyle): # real signature unknown; restored from __doc__
        """ setStyle(self, astyle: QTextListFormat.Style) """
        pass

    def style(self): # real signature unknown; restored from __doc__
        """ style(self) -> QTextListFormat.Style """
        pass

    def __init__(self, a0=None): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    ListCircle = -2
    ListDecimal = -4
    ListDisc = -1
    ListLowerAlpha = -5
    ListLowerRoman = -7
    ListSquare = -3
    ListUpperAlpha = -6
    ListUpperRoman = -8


