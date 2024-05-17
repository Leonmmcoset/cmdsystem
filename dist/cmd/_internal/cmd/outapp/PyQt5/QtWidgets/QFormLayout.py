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

class QFormLayout(QLayout):
    """ QFormLayout(parent: Optional[QWidget] = None) """
    def addChildLayout(self, *args, **kwargs): # real signature unknown
        pass

    def addChildWidget(self, *args, **kwargs): # real signature unknown
        pass

    def addItem(self, item, QLayoutItem=None): # real signature unknown; restored from __doc__
        """ addItem(self, item: Optional[QLayoutItem]) """
        pass

    def addRow(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        addRow(self, label: Optional[QWidget], field: Optional[QWidget])
        addRow(self, label: Optional[QWidget], field: Optional[QLayout])
        addRow(self, labelText: Optional[str], field: Optional[QWidget])
        addRow(self, labelText: Optional[str], field: Optional[QLayout])
        addRow(self, widget: Optional[QWidget])
        addRow(self, layout: Optional[QLayout])
        """
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

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def expandingDirections(self): # real signature unknown; restored from __doc__
        """ expandingDirections(self) -> Qt.Orientations """
        pass

    def fieldGrowthPolicy(self): # real signature unknown; restored from __doc__
        """ fieldGrowthPolicy(self) -> QFormLayout.FieldGrowthPolicy """
        pass

    def formAlignment(self): # real signature unknown; restored from __doc__
        """ formAlignment(self) -> Qt.Alignment """
        pass

    def getItemPosition(self, index): # real signature unknown; restored from __doc__
        """ getItemPosition(self, index: int) -> (Optional[int], Optional[QFormLayout.ItemRole]) """
        pass

    def getLayoutPosition(self, layout, QLayout=None): # real signature unknown; restored from __doc__
        """ getLayoutPosition(self, layout: Optional[QLayout]) -> (Optional[int], Optional[QFormLayout.ItemRole]) """
        pass

    def getWidgetPosition(self, widget, QWidget=None): # real signature unknown; restored from __doc__
        """ getWidgetPosition(self, widget: Optional[QWidget]) -> (Optional[int], Optional[QFormLayout.ItemRole]) """
        pass

    def hasHeightForWidth(self): # real signature unknown; restored from __doc__
        """ hasHeightForWidth(self) -> bool """
        return False

    def heightForWidth(self, width): # real signature unknown; restored from __doc__
        """ heightForWidth(self, width: int) -> int """
        return 0

    def horizontalSpacing(self): # real signature unknown; restored from __doc__
        """ horizontalSpacing(self) -> int """
        return 0

    def insertRow(self, row, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        insertRow(self, row: int, label: Optional[QWidget], field: Optional[QWidget])
        insertRow(self, row: int, label: Optional[QWidget], field: Optional[QLayout])
        insertRow(self, row: int, labelText: Optional[str], field: Optional[QWidget])
        insertRow(self, row: int, labelText: Optional[str], field: Optional[QLayout])
        insertRow(self, row: int, widget: Optional[QWidget])
        insertRow(self, row: int, layout: Optional[QLayout])
        """
        pass

    def invalidate(self): # real signature unknown; restored from __doc__
        """ invalidate(self) """
        pass

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def itemAt(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        itemAt(self, row: int, role: QFormLayout.ItemRole) -> Optional[QLayoutItem]
        itemAt(self, index: int) -> Optional[QLayoutItem]
        """
        pass

    def labelAlignment(self): # real signature unknown; restored from __doc__
        """ labelAlignment(self) -> Qt.Alignment """
        pass

    def labelForField(self, field, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        labelForField(self, field: Optional[QWidget]) -> Optional[QWidget]
        labelForField(self, field: Optional[QLayout]) -> Optional[QWidget]
        """
        pass

    def minimumSize(self): # real signature unknown; restored from __doc__
        """ minimumSize(self) -> QSize """
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def removeRow(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        removeRow(self, row: int)
        removeRow(self, widget: Optional[QWidget])
        removeRow(self, layout: Optional[QLayout])
        """
        pass

    def rowCount(self): # real signature unknown; restored from __doc__
        """ rowCount(self) -> int """
        return 0

    def rowWrapPolicy(self): # real signature unknown; restored from __doc__
        """ rowWrapPolicy(self) -> QFormLayout.RowWrapPolicy """
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setFieldGrowthPolicy(self, policy): # real signature unknown; restored from __doc__
        """ setFieldGrowthPolicy(self, policy: QFormLayout.FieldGrowthPolicy) """
        pass

    def setFormAlignment(self, alignment, Qt_Alignment=None, Qt_AlignmentFlag=None): # real signature unknown; restored from __doc__
        """ setFormAlignment(self, alignment: Union[Qt.Alignment, Qt.AlignmentFlag]) """
        pass

    def setGeometry(self, rect): # real signature unknown; restored from __doc__
        """ setGeometry(self, rect: QRect) """
        pass

    def setHorizontalSpacing(self, spacing): # real signature unknown; restored from __doc__
        """ setHorizontalSpacing(self, spacing: int) """
        pass

    def setItem(self, row, role, item, QLayoutItem=None): # real signature unknown; restored from __doc__
        """ setItem(self, row: int, role: QFormLayout.ItemRole, item: Optional[QLayoutItem]) """
        pass

    def setLabelAlignment(self, alignment, Qt_Alignment=None, Qt_AlignmentFlag=None): # real signature unknown; restored from __doc__
        """ setLabelAlignment(self, alignment: Union[Qt.Alignment, Qt.AlignmentFlag]) """
        pass

    def setLayout(self, row, role, layout, QLayout=None): # real signature unknown; restored from __doc__
        """ setLayout(self, row: int, role: QFormLayout.ItemRole, layout: Optional[QLayout]) """
        pass

    def setRowWrapPolicy(self, policy): # real signature unknown; restored from __doc__
        """ setRowWrapPolicy(self, policy: QFormLayout.RowWrapPolicy) """
        pass

    def setSpacing(self, a0): # real signature unknown; restored from __doc__
        """ setSpacing(self, a0: int) """
        pass

    def setVerticalSpacing(self, spacing): # real signature unknown; restored from __doc__
        """ setVerticalSpacing(self, spacing: int) """
        pass

    def setWidget(self, row, role, widget, QWidget=None): # real signature unknown; restored from __doc__
        """ setWidget(self, row: int, role: QFormLayout.ItemRole, widget: Optional[QWidget]) """
        pass

    def sizeHint(self): # real signature unknown; restored from __doc__
        """ sizeHint(self) -> QSize """
        pass

    def spacing(self): # real signature unknown; restored from __doc__
        """ spacing(self) -> int """
        return 0

    def takeAt(self, index): # real signature unknown; restored from __doc__
        """ takeAt(self, index: int) -> Optional[QLayoutItem] """
        pass

    def takeRow(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        takeRow(self, row: int) -> QFormLayout.TakeRowResult
        takeRow(self, widget: Optional[QWidget]) -> QFormLayout.TakeRowResult
        takeRow(self, layout: Optional[QLayout]) -> QFormLayout.TakeRowResult
        """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def verticalSpacing(self): # real signature unknown; restored from __doc__
        """ verticalSpacing(self) -> int """
        return 0

    def widgetEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, parent, QWidget=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    AllNonFixedFieldsGrow = 2
    DontWrapRows = 0
    ExpandingFieldsGrow = 1
    FieldRole = 1
    FieldsStayAtSizeHint = 0
    LabelRole = 0
    SpanningRole = 2
    WrapAllRows = 2
    WrapLongRows = 1


