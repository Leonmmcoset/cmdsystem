# encoding: utf-8
# module PyQt5.QtWidgets
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtWidgets.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import PyQt5.QtGui as __PyQt5_QtGui
import sip as __sip


from .QGraphicsLayout import QGraphicsLayout

class QGraphicsGridLayout(QGraphicsLayout):
    """ QGraphicsGridLayout(parent: Optional[QGraphicsLayoutItem] = None) """
    def addChildLayoutItem(self, *args, **kwargs): # real signature unknown
        pass

    def addItem(self, item, QGraphicsLayoutItem=None, *args, **kwargs): # real signature unknown; restored from __doc__ with multiple overloads
        """
        addItem(self, item: Optional[QGraphicsLayoutItem], row: int, column: int, rowSpan: int, columnSpan: int, alignment: Union[Qt.Alignment, Qt.AlignmentFlag] = Qt.Alignment())
        addItem(self, item: Optional[QGraphicsLayoutItem], row: int, column: int, alignment: Union[Qt.Alignment, Qt.AlignmentFlag] = Qt.Alignment())
        """
        pass

    def alignment(self, item, QGraphicsLayoutItem=None): # real signature unknown; restored from __doc__
        """ alignment(self, item: Optional[QGraphicsLayoutItem]) -> Qt.Alignment """
        pass

    def columnAlignment(self, column): # real signature unknown; restored from __doc__
        """ columnAlignment(self, column: int) -> Qt.Alignment """
        pass

    def columnCount(self): # real signature unknown; restored from __doc__
        """ columnCount(self) -> int """
        return 0

    def columnMaximumWidth(self, column): # real signature unknown; restored from __doc__
        """ columnMaximumWidth(self, column: int) -> float """
        return 0.0

    def columnMinimumWidth(self, column): # real signature unknown; restored from __doc__
        """ columnMinimumWidth(self, column: int) -> float """
        return 0.0

    def columnPreferredWidth(self, column): # real signature unknown; restored from __doc__
        """ columnPreferredWidth(self, column: int) -> float """
        return 0.0

    def columnSpacing(self, column): # real signature unknown; restored from __doc__
        """ columnSpacing(self, column: int) -> float """
        return 0.0

    def columnStretchFactor(self, column): # real signature unknown; restored from __doc__
        """ columnStretchFactor(self, column: int) -> int """
        return 0

    def count(self): # real signature unknown; restored from __doc__
        """ count(self) -> int """
        return 0

    def horizontalSpacing(self): # real signature unknown; restored from __doc__
        """ horizontalSpacing(self) -> float """
        return 0.0

    def invalidate(self): # real signature unknown; restored from __doc__
        """ invalidate(self) """
        pass

    def itemAt(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        itemAt(self, row: int, column: int) -> Optional[QGraphicsLayoutItem]
        itemAt(self, index: int) -> Optional[QGraphicsLayoutItem]
        """
        pass

    def removeAt(self, index): # real signature unknown; restored from __doc__
        """ removeAt(self, index: int) """
        pass

    def removeItem(self, item, QGraphicsLayoutItem=None): # real signature unknown; restored from __doc__
        """ removeItem(self, item: Optional[QGraphicsLayoutItem]) """
        pass

    def rowAlignment(self, row): # real signature unknown; restored from __doc__
        """ rowAlignment(self, row: int) -> Qt.Alignment """
        pass

    def rowCount(self): # real signature unknown; restored from __doc__
        """ rowCount(self) -> int """
        return 0

    def rowMaximumHeight(self, row): # real signature unknown; restored from __doc__
        """ rowMaximumHeight(self, row: int) -> float """
        return 0.0

    def rowMinimumHeight(self, row): # real signature unknown; restored from __doc__
        """ rowMinimumHeight(self, row: int) -> float """
        return 0.0

    def rowPreferredHeight(self, row): # real signature unknown; restored from __doc__
        """ rowPreferredHeight(self, row: int) -> float """
        return 0.0

    def rowSpacing(self, row): # real signature unknown; restored from __doc__
        """ rowSpacing(self, row: int) -> float """
        return 0.0

    def rowStretchFactor(self, row): # real signature unknown; restored from __doc__
        """ rowStretchFactor(self, row: int) -> int """
        return 0

    def setAlignment(self, item, QGraphicsLayoutItem=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ setAlignment(self, item: Optional[QGraphicsLayoutItem], alignment: Union[Qt.Alignment, Qt.AlignmentFlag]) """
        pass

    def setColumnAlignment(self, column, alignment, Qt_Alignment=None, Qt_AlignmentFlag=None): # real signature unknown; restored from __doc__
        """ setColumnAlignment(self, column: int, alignment: Union[Qt.Alignment, Qt.AlignmentFlag]) """
        pass

    def setColumnFixedWidth(self, column, width): # real signature unknown; restored from __doc__
        """ setColumnFixedWidth(self, column: int, width: float) """
        pass

    def setColumnMaximumWidth(self, column, width): # real signature unknown; restored from __doc__
        """ setColumnMaximumWidth(self, column: int, width: float) """
        pass

    def setColumnMinimumWidth(self, column, width): # real signature unknown; restored from __doc__
        """ setColumnMinimumWidth(self, column: int, width: float) """
        pass

    def setColumnPreferredWidth(self, column, width): # real signature unknown; restored from __doc__
        """ setColumnPreferredWidth(self, column: int, width: float) """
        pass

    def setColumnSpacing(self, column, spacing): # real signature unknown; restored from __doc__
        """ setColumnSpacing(self, column: int, spacing: float) """
        pass

    def setColumnStretchFactor(self, column, stretch): # real signature unknown; restored from __doc__
        """ setColumnStretchFactor(self, column: int, stretch: int) """
        pass

    def setGeometry(self, rect): # real signature unknown; restored from __doc__
        """ setGeometry(self, rect: QRectF) """
        pass

    def setGraphicsItem(self, *args, **kwargs): # real signature unknown
        pass

    def setHorizontalSpacing(self, spacing): # real signature unknown; restored from __doc__
        """ setHorizontalSpacing(self, spacing: float) """
        pass

    def setOwnedByLayout(self, *args, **kwargs): # real signature unknown
        pass

    def setRowAlignment(self, row, alignment, Qt_Alignment=None, Qt_AlignmentFlag=None): # real signature unknown; restored from __doc__
        """ setRowAlignment(self, row: int, alignment: Union[Qt.Alignment, Qt.AlignmentFlag]) """
        pass

    def setRowFixedHeight(self, row, height): # real signature unknown; restored from __doc__
        """ setRowFixedHeight(self, row: int, height: float) """
        pass

    def setRowMaximumHeight(self, row, height): # real signature unknown; restored from __doc__
        """ setRowMaximumHeight(self, row: int, height: float) """
        pass

    def setRowMinimumHeight(self, row, height): # real signature unknown; restored from __doc__
        """ setRowMinimumHeight(self, row: int, height: float) """
        pass

    def setRowPreferredHeight(self, row, height): # real signature unknown; restored from __doc__
        """ setRowPreferredHeight(self, row: int, height: float) """
        pass

    def setRowSpacing(self, row, spacing): # real signature unknown; restored from __doc__
        """ setRowSpacing(self, row: int, spacing: float) """
        pass

    def setRowStretchFactor(self, row, stretch): # real signature unknown; restored from __doc__
        """ setRowStretchFactor(self, row: int, stretch: int) """
        pass

    def setSpacing(self, spacing): # real signature unknown; restored from __doc__
        """ setSpacing(self, spacing: float) """
        pass

    def setVerticalSpacing(self, spacing): # real signature unknown; restored from __doc__
        """ setVerticalSpacing(self, spacing: float) """
        pass

    def sizeHint(self, which, constraint=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ sizeHint(self, which: Qt.SizeHint, constraint: QSizeF = QSizeF()) -> QSizeF """
        pass

    def verticalSpacing(self): # real signature unknown; restored from __doc__
        """ verticalSpacing(self) -> float """
        return 0.0

    def __init__(self, parent, QGraphicsLayoutItem=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass


