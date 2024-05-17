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

class QGridLayout(QLayout):
    """
    QGridLayout(parent: Optional[QWidget])
    QGridLayout()
    """
    def addChildLayout(self, *args, **kwargs): # real signature unknown
        pass

    def addChildWidget(self, *args, **kwargs): # real signature unknown
        pass

    def addItem(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        addItem(self, item: Optional[QLayoutItem], row: int, column: int, rowSpan: int = 1, columnSpan: int = 1, alignment: Union[Qt.Alignment, Qt.AlignmentFlag] = Qt.Alignment())
        addItem(self, a0: Optional[QLayoutItem])
        """
        pass

    def addLayout(self, a0, QLayout=None, *args, **kwargs): # real signature unknown; restored from __doc__ with multiple overloads
        """
        addLayout(self, a0: Optional[QLayout], row: int, column: int, alignment: Union[Qt.Alignment, Qt.AlignmentFlag] = Qt.Alignment())
        addLayout(self, a0: Optional[QLayout], row: int, column: int, rowSpan: int, columnSpan: int, alignment: Union[Qt.Alignment, Qt.AlignmentFlag] = Qt.Alignment())
        """
        pass

    def addWidget(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        addWidget(self, w: Optional[QWidget])
        addWidget(self, a0: Optional[QWidget], row: int, column: int, alignment: Union[Qt.Alignment, Qt.AlignmentFlag] = Qt.Alignment())
        addWidget(self, a0: Optional[QWidget], row: int, column: int, rowSpan: int, columnSpan: int, alignment: Union[Qt.Alignment, Qt.AlignmentFlag] = Qt.Alignment())
        """
        pass

    def alignmentRect(self, *args, **kwargs): # real signature unknown
        pass

    def cellRect(self, row, column): # real signature unknown; restored from __doc__
        """ cellRect(self, row: int, column: int) -> QRect """
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def columnCount(self): # real signature unknown; restored from __doc__
        """ columnCount(self) -> int """
        return 0

    def columnMinimumWidth(self, column): # real signature unknown; restored from __doc__
        """ columnMinimumWidth(self, column: int) -> int """
        return 0

    def columnStretch(self, column): # real signature unknown; restored from __doc__
        """ columnStretch(self, column: int) -> int """
        return 0

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def count(self): # real signature unknown; restored from __doc__
        """ count(self) -> int """
        return 0

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def expandingDirections(self): # real signature unknown; restored from __doc__
        """ expandingDirections(self) -> Qt.Orientations """
        pass

    def getItemPosition(self, idx): # real signature unknown; restored from __doc__
        """ getItemPosition(self, idx: int) -> (Optional[int], Optional[int], Optional[int], Optional[int]) """
        pass

    def hasHeightForWidth(self): # real signature unknown; restored from __doc__
        """ hasHeightForWidth(self) -> bool """
        return False

    def heightForWidth(self, a0): # real signature unknown; restored from __doc__
        """ heightForWidth(self, a0: int) -> int """
        return 0

    def horizontalSpacing(self): # real signature unknown; restored from __doc__
        """ horizontalSpacing(self) -> int """
        return 0

    def invalidate(self): # real signature unknown; restored from __doc__
        """ invalidate(self) """
        pass

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def itemAt(self, a0): # real signature unknown; restored from __doc__
        """ itemAt(self, a0: int) -> Optional[QLayoutItem] """
        pass

    def itemAtPosition(self, row, column): # real signature unknown; restored from __doc__
        """ itemAtPosition(self, row: int, column: int) -> Optional[QLayoutItem] """
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

    def originCorner(self): # real signature unknown; restored from __doc__
        """ originCorner(self) -> Qt.Corner """
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def rowCount(self): # real signature unknown; restored from __doc__
        """ rowCount(self) -> int """
        return 0

    def rowMinimumHeight(self, row): # real signature unknown; restored from __doc__
        """ rowMinimumHeight(self, row: int) -> int """
        return 0

    def rowStretch(self, row): # real signature unknown; restored from __doc__
        """ rowStretch(self, row: int) -> int """
        return 0

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setColumnMinimumWidth(self, column, minSize): # real signature unknown; restored from __doc__
        """ setColumnMinimumWidth(self, column: int, minSize: int) """
        pass

    def setColumnStretch(self, column, stretch): # real signature unknown; restored from __doc__
        """ setColumnStretch(self, column: int, stretch: int) """
        pass

    def setDefaultPositioning(self, n, orient): # real signature unknown; restored from __doc__
        """ setDefaultPositioning(self, n: int, orient: Qt.Orientation) """
        pass

    def setGeometry(self, a0): # real signature unknown; restored from __doc__
        """ setGeometry(self, a0: QRect) """
        pass

    def setHorizontalSpacing(self, spacing): # real signature unknown; restored from __doc__
        """ setHorizontalSpacing(self, spacing: int) """
        pass

    def setOriginCorner(self, a0): # real signature unknown; restored from __doc__
        """ setOriginCorner(self, a0: Qt.Corner) """
        pass

    def setRowMinimumHeight(self, row, minSize): # real signature unknown; restored from __doc__
        """ setRowMinimumHeight(self, row: int, minSize: int) """
        pass

    def setRowStretch(self, row, stretch): # real signature unknown; restored from __doc__
        """ setRowStretch(self, row: int, stretch: int) """
        pass

    def setSpacing(self, spacing): # real signature unknown; restored from __doc__
        """ setSpacing(self, spacing: int) """
        pass

    def setVerticalSpacing(self, spacing): # real signature unknown; restored from __doc__
        """ setVerticalSpacing(self, spacing: int) """
        pass

    def sizeHint(self): # real signature unknown; restored from __doc__
        """ sizeHint(self) -> QSize """
        pass

    def spacing(self): # real signature unknown; restored from __doc__
        """ spacing(self) -> int """
        return 0

    def takeAt(self, a0): # real signature unknown; restored from __doc__
        """ takeAt(self, a0: int) -> Optional[QLayoutItem] """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def verticalSpacing(self): # real signature unknown; restored from __doc__
        """ verticalSpacing(self) -> int """
        return 0

    def widgetEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, parent=None, QWidget=None): # real signature unknown; restored from __doc__ with multiple overloads
        pass


