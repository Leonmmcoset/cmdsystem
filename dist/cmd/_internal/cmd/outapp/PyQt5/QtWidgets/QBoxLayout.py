# encoding: utf-8
# module PyQt5.QtWidgets
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtWidgets.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import PyQt5.QtGui as __PyQt5_QtGui
import sip as __sip


from .QLayout import QLayout

class QBoxLayout(QLayout):
    """ QBoxLayout(direction: QBoxLayout.Direction, parent: Optional[QWidget] = None) """
    def addChildLayout(self, *args, **kwargs): # real signature unknown
        pass

    def addChildWidget(self, *args, **kwargs): # real signature unknown
        pass

    def addItem(self, a0, QLayoutItem=None): # real signature unknown; restored from __doc__
        """ addItem(self, a0: Optional[QLayoutItem]) """
        pass

    def addLayout(self, layout, QLayout=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ addLayout(self, layout: Optional[QLayout], stretch: int = 0) """
        pass

    def addSpacerItem(self, spacerItem, QSpacerItem=None): # real signature unknown; restored from __doc__
        """ addSpacerItem(self, spacerItem: Optional[QSpacerItem]) """
        pass

    def addSpacing(self, size): # real signature unknown; restored from __doc__
        """ addSpacing(self, size: int) """
        pass

    def addStretch(self, stretch=0): # real signature unknown; restored from __doc__
        """ addStretch(self, stretch: int = 0) """
        pass

    def addStrut(self, a0): # real signature unknown; restored from __doc__
        """ addStrut(self, a0: int) """
        pass

    def addWidget(self, a0, QWidget=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ addWidget(self, a0: Optional[QWidget], stretch: int = 0, alignment: Union[Qt.Alignment, Qt.AlignmentFlag] = Qt.Alignment()) """
        pass

    def alignmentRect(self, *args, **kwargs): # real signature unknown
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def count(self): # real signature unknown; restored from __doc__
        """ count(self) -> int """
        return 0

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def direction(self): # real signature unknown; restored from __doc__
        """ direction(self) -> QBoxLayout.Direction """
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def expandingDirections(self): # real signature unknown; restored from __doc__
        """ expandingDirections(self) -> Qt.Orientations """
        pass

    def hasHeightForWidth(self): # real signature unknown; restored from __doc__
        """ hasHeightForWidth(self) -> bool """
        return False

    def heightForWidth(self, a0): # real signature unknown; restored from __doc__
        """ heightForWidth(self, a0: int) -> int """
        return 0

    def insertItem(self, index, a1, QLayoutItem=None): # real signature unknown; restored from __doc__
        """ insertItem(self, index: int, a1: Optional[QLayoutItem]) """
        pass

    def insertLayout(self, index, layout, QLayout=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ insertLayout(self, index: int, layout: Optional[QLayout], stretch: int = 0) """
        pass

    def insertSpacerItem(self, index, spacerItem, QSpacerItem=None): # real signature unknown; restored from __doc__
        """ insertSpacerItem(self, index: int, spacerItem: Optional[QSpacerItem]) """
        pass

    def insertSpacing(self, index, size): # real signature unknown; restored from __doc__
        """ insertSpacing(self, index: int, size: int) """
        pass

    def insertStretch(self, index, stretch=0): # real signature unknown; restored from __doc__
        """ insertStretch(self, index: int, stretch: int = 0) """
        pass

    def insertWidget(self, index, widget, QWidget=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ insertWidget(self, index: int, widget: Optional[QWidget], stretch: int = 0, alignment: Union[Qt.Alignment, Qt.AlignmentFlag] = Qt.Alignment()) """
        pass

    def invalidate(self): # real signature unknown; restored from __doc__
        """ invalidate(self) """
        pass

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def itemAt(self, a0): # real signature unknown; restored from __doc__
        """ itemAt(self, a0: int) -> Optional[QLayoutItem] """
        pass

    def maximumSize(self): # real signature unknown; restored from __doc__
        """ maximumSize(self) -> QSize """
        pass

    def minimumHeightForWidth(self, a0): # real signature unknown; restored from __doc__
        """ minimumHeightForWidth(self, a0: int) -> int """
        return 0

    def minimumSize(self): # real signature unknown; restored from __doc__
        """ minimumSize(self) -> QSize """
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setDirection(self, a0): # real signature unknown; restored from __doc__
        """ setDirection(self, a0: QBoxLayout.Direction) """
        pass

    def setGeometry(self, a0): # real signature unknown; restored from __doc__
        """ setGeometry(self, a0: QRect) """
        pass

    def setSpacing(self, spacing): # real signature unknown; restored from __doc__
        """ setSpacing(self, spacing: int) """
        pass

    def setStretch(self, index, stretch): # real signature unknown; restored from __doc__
        """ setStretch(self, index: int, stretch: int) """
        pass

    def setStretchFactor(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setStretchFactor(self, w: Optional[QWidget], stretch: int) -> bool
        setStretchFactor(self, l: Optional[QLayout], stretch: int) -> bool
        """
        pass

    def sizeHint(self): # real signature unknown; restored from __doc__
        """ sizeHint(self) -> QSize """
        pass

    def spacing(self): # real signature unknown; restored from __doc__
        """ spacing(self) -> int """
        return 0

    def stretch(self, index): # real signature unknown; restored from __doc__
        """ stretch(self, index: int) -> int """
        return 0

    def takeAt(self, a0): # real signature unknown; restored from __doc__
        """ takeAt(self, a0: int) -> Optional[QLayoutItem] """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def widgetEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, direction, parent, QWidget=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    BottomToTop = 3
    Down = 2
    LeftToRight = 0
    RightToLeft = 1
    TopToBottom = 2
    Up = 3


