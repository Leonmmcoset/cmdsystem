# encoding: utf-8
# module PyQt5.QtGui
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtGui.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


class QPageLayout(__sip.simplewrapper):
    """
    QPageLayout()
    QPageLayout(pageSize: QPageSize, orientation: QPageLayout.Orientation, margins: QMarginsF, units: QPageLayout.Unit = QPageLayout.Point, minMargins: QMarginsF = QMarginsF(0, 0, 0, 0))
    QPageLayout(other: QPageLayout)
    """
    def fullRect(self, units=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        fullRect(self) -> QRectF
        fullRect(self, units: QPageLayout.Unit) -> QRectF
        """
        pass

    def fullRectPixels(self, resolution): # real signature unknown; restored from __doc__
        """ fullRectPixels(self, resolution: int) -> QRect """
        pass

    def fullRectPoints(self): # real signature unknown; restored from __doc__
        """ fullRectPoints(self) -> QRect """
        pass

    def isEquivalentTo(self, other): # real signature unknown; restored from __doc__
        """ isEquivalentTo(self, other: QPageLayout) -> bool """
        return False

    def isValid(self): # real signature unknown; restored from __doc__
        """ isValid(self) -> bool """
        return False

    def margins(self, units=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        margins(self) -> QMarginsF
        margins(self, units: QPageLayout.Unit) -> QMarginsF
        """
        pass

    def marginsPixels(self, resolution): # real signature unknown; restored from __doc__
        """ marginsPixels(self, resolution: int) -> QMargins """
        pass

    def marginsPoints(self): # real signature unknown; restored from __doc__
        """ marginsPoints(self) -> QMargins """
        pass

    def maximumMargins(self): # real signature unknown; restored from __doc__
        """ maximumMargins(self) -> QMarginsF """
        pass

    def minimumMargins(self): # real signature unknown; restored from __doc__
        """ minimumMargins(self) -> QMarginsF """
        pass

    def mode(self): # real signature unknown; restored from __doc__
        """ mode(self) -> QPageLayout.Mode """
        pass

    def orientation(self): # real signature unknown; restored from __doc__
        """ orientation(self) -> QPageLayout.Orientation """
        pass

    def pageSize(self): # real signature unknown; restored from __doc__
        """ pageSize(self) -> QPageSize """
        return QPageSize

    def paintRect(self, units=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        paintRect(self) -> QRectF
        paintRect(self, units: QPageLayout.Unit) -> QRectF
        """
        pass

    def paintRectPixels(self, resolution): # real signature unknown; restored from __doc__
        """ paintRectPixels(self, resolution: int) -> QRect """
        pass

    def paintRectPoints(self): # real signature unknown; restored from __doc__
        """ paintRectPoints(self) -> QRect """
        pass

    def setBottomMargin(self, bottomMargin): # real signature unknown; restored from __doc__
        """ setBottomMargin(self, bottomMargin: float) -> bool """
        return False

    def setLeftMargin(self, leftMargin): # real signature unknown; restored from __doc__
        """ setLeftMargin(self, leftMargin: float) -> bool """
        return False

    def setMargins(self, margins): # real signature unknown; restored from __doc__
        """ setMargins(self, margins: QMarginsF) -> bool """
        return False

    def setMinimumMargins(self, minMargins): # real signature unknown; restored from __doc__
        """ setMinimumMargins(self, minMargins: QMarginsF) """
        pass

    def setMode(self, mode): # real signature unknown; restored from __doc__
        """ setMode(self, mode: QPageLayout.Mode) """
        pass

    def setOrientation(self, orientation): # real signature unknown; restored from __doc__
        """ setOrientation(self, orientation: QPageLayout.Orientation) """
        pass

    def setPageSize(self, pageSize, minMargins=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ setPageSize(self, pageSize: QPageSize, minMargins: QMarginsF = QMarginsF(0, 0, 0, 0)) """
        pass

    def setRightMargin(self, rightMargin): # real signature unknown; restored from __doc__
        """ setRightMargin(self, rightMargin: float) -> bool """
        return False

    def setTopMargin(self, topMargin): # real signature unknown; restored from __doc__
        """ setTopMargin(self, topMargin: float) -> bool """
        return False

    def setUnits(self, units): # real signature unknown; restored from __doc__
        """ setUnits(self, units: QPageLayout.Unit) """
        pass

    def swap(self, other): # real signature unknown; restored from __doc__
        """ swap(self, other: QPageLayout) """
        pass

    def units(self): # real signature unknown; restored from __doc__
        """ units(self) -> QPageLayout.Unit """
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


    Cicero = 5
    Didot = 4
    FullPageMode = 1
    Inch = 2
    Landscape = 1
    Millimeter = 0
    Pica = 3
    Point = 1
    Portrait = 0
    StandardMode = 0
    __hash__ = None


