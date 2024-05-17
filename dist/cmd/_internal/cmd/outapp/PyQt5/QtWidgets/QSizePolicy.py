# encoding: utf-8
# module PyQt5.QtWidgets
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtWidgets.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import PyQt5.QtGui as __PyQt5_QtGui
import sip as __sip


class QSizePolicy(__sip.simplewrapper):
    """
    QSizePolicy()
    QSizePolicy(horizontal: QSizePolicy.Policy, vertical: QSizePolicy.Policy, type: QSizePolicy.ControlType = QSizePolicy.DefaultType)
    QSizePolicy(variant: Any)
    QSizePolicy(a0: QSizePolicy)
    """
    def controlType(self): # real signature unknown; restored from __doc__
        """ controlType(self) -> QSizePolicy.ControlType """
        pass

    def expandingDirections(self): # real signature unknown; restored from __doc__
        """ expandingDirections(self) -> Qt.Orientations """
        pass

    def hasHeightForWidth(self): # real signature unknown; restored from __doc__
        """ hasHeightForWidth(self) -> bool """
        return False

    def hasWidthForHeight(self): # real signature unknown; restored from __doc__
        """ hasWidthForHeight(self) -> bool """
        return False

    def horizontalPolicy(self): # real signature unknown; restored from __doc__
        """ horizontalPolicy(self) -> QSizePolicy.Policy """
        pass

    def horizontalStretch(self): # real signature unknown; restored from __doc__
        """ horizontalStretch(self) -> int """
        return 0

    def retainSizeWhenHidden(self): # real signature unknown; restored from __doc__
        """ retainSizeWhenHidden(self) -> bool """
        return False

    def setControlType(self, type): # real signature unknown; restored from __doc__
        """ setControlType(self, type: QSizePolicy.ControlType) """
        pass

    def setHeightForWidth(self, b): # real signature unknown; restored from __doc__
        """ setHeightForWidth(self, b: bool) """
        pass

    def setHorizontalPolicy(self, d): # real signature unknown; restored from __doc__
        """ setHorizontalPolicy(self, d: QSizePolicy.Policy) """
        pass

    def setHorizontalStretch(self, stretchFactor): # real signature unknown; restored from __doc__
        """ setHorizontalStretch(self, stretchFactor: int) """
        pass

    def setRetainSizeWhenHidden(self, retainSize): # real signature unknown; restored from __doc__
        """ setRetainSizeWhenHidden(self, retainSize: bool) """
        pass

    def setVerticalPolicy(self, d): # real signature unknown; restored from __doc__
        """ setVerticalPolicy(self, d: QSizePolicy.Policy) """
        pass

    def setVerticalStretch(self, stretchFactor): # real signature unknown; restored from __doc__
        """ setVerticalStretch(self, stretchFactor: int) """
        pass

    def setWidthForHeight(self, b): # real signature unknown; restored from __doc__
        """ setWidthForHeight(self, b: bool) """
        pass

    def transpose(self): # real signature unknown; restored from __doc__
        """ transpose(self) """
        pass

    def transposed(self): # real signature unknown; restored from __doc__
        """ transposed(self) -> QSizePolicy """
        return QSizePolicy

    def verticalPolicy(self): # real signature unknown; restored from __doc__
        """ verticalPolicy(self) -> QSizePolicy.Policy """
        pass

    def verticalStretch(self): # real signature unknown; restored from __doc__
        """ verticalStretch(self) -> int """
        return 0

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __hash__(self, *args, **kwargs): # real signature unknown
        """ Return hash(self). """
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


    ButtonBox = 2
    CheckBox = 4
    ComboBox = 8
    DefaultType = 1
    ExpandFlag = 2
    Expanding = 7
    Fixed = 0
    Frame = 16
    GroupBox = 32
    GrowFlag = 1
    Ignored = 13
    IgnoreFlag = 8
    Label = 64
    Line = 128
    LineEdit = 256
    Maximum = 4
    Minimum = 1
    MinimumExpanding = 3
    Preferred = 5
    PushButton = 512
    RadioButton = 1024
    ShrinkFlag = 4
    Slider = 2048
    SpinBox = 4096
    TabWidget = 8192
    ToolButton = 16384


