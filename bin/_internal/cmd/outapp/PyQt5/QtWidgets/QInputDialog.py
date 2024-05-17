# encoding: utf-8
# module PyQt5.QtWidgets
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtWidgets.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import PyQt5.QtGui as __PyQt5_QtGui
import sip as __sip


from .QDialog import QDialog

class QInputDialog(QDialog):
    """ QInputDialog(parent: Optional[QWidget] = None, flags: Union[Qt.WindowFlags, Qt.WindowType] = Qt.WindowFlags()) """
    def actionEvent(self, *args, **kwargs): # real signature unknown
        pass

    def cancelButtonText(self): # real signature unknown; restored from __doc__
        """ cancelButtonText(self) -> str """
        return ""

    def changeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def closeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def comboBoxItems(self): # real signature unknown; restored from __doc__
        """ comboBoxItems(self) -> List[str] """
        return []

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def contextMenuEvent(self, *args, **kwargs): # real signature unknown
        pass

    def create(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def destroy(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def done(self, result): # real signature unknown; restored from __doc__
        """ done(self, result: int) """
        pass

    def doubleDecimals(self): # real signature unknown; restored from __doc__
        """ doubleDecimals(self) -> int """
        return 0

    def doubleMaximum(self): # real signature unknown; restored from __doc__
        """ doubleMaximum(self) -> float """
        return 0.0

    def doubleMinimum(self): # real signature unknown; restored from __doc__
        """ doubleMinimum(self) -> float """
        return 0.0

    def doubleStep(self): # real signature unknown; restored from __doc__
        """ doubleStep(self) -> float """
        return 0.0

    def doubleValue(self): # real signature unknown; restored from __doc__
        """ doubleValue(self) -> float """
        return 0.0

    def doubleValueChanged(self, *args, **kwargs): # real signature unknown
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
        pass

    def doubleValueSelected(self, *args, **kwargs): # real signature unknown
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
        pass

    def dragEnterEvent(self, *args, **kwargs): # real signature unknown
        pass

    def dragLeaveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def dragMoveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def dropEvent(self, *args, **kwargs): # real signature unknown
        pass

    def enterEvent(self, *args, **kwargs): # real signature unknown
        pass

    def event(self, *args, **kwargs): # real signature unknown
        pass

    def eventFilter(self, *args, **kwargs): # real signature unknown
        pass

    def focusInEvent(self, *args, **kwargs): # real signature unknown
        pass

    def focusNextChild(self, *args, **kwargs): # real signature unknown
        pass

    def focusNextPrevChild(self, *args, **kwargs): # real signature unknown
        pass

    def focusOutEvent(self, *args, **kwargs): # real signature unknown
        pass

    def focusPreviousChild(self, *args, **kwargs): # real signature unknown
        pass

    def getDouble(self, parent, QWidget=None, *args, **kwargs): # real signature unknown; restored from __doc__ with multiple overloads
        """
        getDouble(parent: Optional[QWidget], title: Optional[str], label: Optional[str], value: float = 0, min: float = -2147483647, max: float = 2147483647, decimals: int = 1, flags: Union[Qt.WindowFlags, Qt.WindowType] = Qt.WindowFlags()) -> (float, Optional[bool])
        getDouble(parent: Optional[QWidget], title: Optional[str], label: Optional[str], value: float, minValue: float, maxValue: float, decimals: int, flags: Union[Qt.WindowFlags, Qt.WindowType], step: float) -> (float, Optional[bool])
        """
        pass

    def getInt(self, parent, QWidget=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ getInt(parent: Optional[QWidget], title: Optional[str], label: Optional[str], value: int = 0, min: int = -2147483647, max: int = 2147483647, step: int = 1, flags: Union[Qt.WindowFlags, Qt.WindowType] = Qt.WindowFlags()) -> (int, Optional[bool]) """
        pass

    def getItem(self, parent, QWidget=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ getItem(parent: Optional[QWidget], title: Optional[str], label: Optional[str], items: Iterable[Optional[str]], current: int = 0, editable: bool = True, flags: Union[Qt.WindowFlags, Qt.WindowType] = Qt.WindowFlags(), inputMethodHints: Union[Qt.InputMethodHints, Qt.InputMethodHint] = Qt.ImhNone) -> (str, Optional[bool]) """
        pass

    def getMultiLineText(self, parent, QWidget=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ getMultiLineText(parent: Optional[QWidget], title: Optional[str], label: Optional[str], text: Optional[str] = '', flags: Union[Qt.WindowFlags, Qt.WindowType] = Qt.WindowFlags(), inputMethodHints: Union[Qt.InputMethodHints, Qt.InputMethodHint] = Qt.ImhNone) -> (str, Optional[bool]) """
        pass

    def getText(self, parent, QWidget=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ getText(parent: Optional[QWidget], title: Optional[str], label: Optional[str], echo: QLineEdit.EchoMode = QLineEdit.Normal, text: Optional[str] = '', flags: Union[Qt.WindowFlags, Qt.WindowType] = Qt.WindowFlags(), inputMethodHints: Union[Qt.InputMethodHints, Qt.InputMethodHint] = Qt.ImhNone) -> (str, Optional[bool]) """
        pass

    def hideEvent(self, *args, **kwargs): # real signature unknown
        pass

    def initPainter(self, *args, **kwargs): # real signature unknown
        pass

    def inputMethodEvent(self, *args, **kwargs): # real signature unknown
        pass

    def inputMode(self): # real signature unknown; restored from __doc__
        """ inputMode(self) -> QInputDialog.InputMode """
        pass

    def intMaximum(self): # real signature unknown; restored from __doc__
        """ intMaximum(self) -> int """
        return 0

    def intMinimum(self): # real signature unknown; restored from __doc__
        """ intMinimum(self) -> int """
        return 0

    def intStep(self): # real signature unknown; restored from __doc__
        """ intStep(self) -> int """
        return 0

    def intValue(self): # real signature unknown; restored from __doc__
        """ intValue(self) -> int """
        return 0

    def intValueChanged(self, *args, **kwargs): # real signature unknown
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
        pass

    def intValueSelected(self, *args, **kwargs): # real signature unknown
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
        pass

    def isComboBoxEditable(self): # real signature unknown; restored from __doc__
        """ isComboBoxEditable(self) -> bool """
        return False

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def keyPressEvent(self, *args, **kwargs): # real signature unknown
        pass

    def keyReleaseEvent(self, *args, **kwargs): # real signature unknown
        pass

    def labelText(self): # real signature unknown; restored from __doc__
        """ labelText(self) -> str """
        return ""

    def leaveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def metric(self, *args, **kwargs): # real signature unknown
        pass

    def minimumSizeHint(self): # real signature unknown; restored from __doc__
        """ minimumSizeHint(self) -> QSize """
        pass

    def mouseDoubleClickEvent(self, *args, **kwargs): # real signature unknown
        pass

    def mouseMoveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def mousePressEvent(self, *args, **kwargs): # real signature unknown
        pass

    def mouseReleaseEvent(self, *args, **kwargs): # real signature unknown
        pass

    def moveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def nativeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def okButtonText(self): # real signature unknown; restored from __doc__
        """ okButtonText(self) -> str """
        return ""

    def open(self, slot=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        open(self)
        open(self, slot: PYQT_SLOT)
        """
        pass

    def options(self): # real signature unknown; restored from __doc__
        """ options(self) -> QInputDialog.InputDialogOptions """
        pass

    def paintEvent(self, *args, **kwargs): # real signature unknown
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def resizeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setCancelButtonText(self, text, p_str=None): # real signature unknown; restored from __doc__
        """ setCancelButtonText(self, text: Optional[str]) """
        pass

    def setComboBoxEditable(self, editable): # real signature unknown; restored from __doc__
        """ setComboBoxEditable(self, editable: bool) """
        pass

    def setComboBoxItems(self, items, Optional=None, p_str=None): # real signature unknown; restored from __doc__
        """ setComboBoxItems(self, items: Iterable[Optional[str]]) """
        pass

    def setDoubleDecimals(self, decimals): # real signature unknown; restored from __doc__
        """ setDoubleDecimals(self, decimals: int) """
        pass

    def setDoubleMaximum(self, max): # real signature unknown; restored from __doc__
        """ setDoubleMaximum(self, max: float) """
        pass

    def setDoubleMinimum(self, min): # real signature unknown; restored from __doc__
        """ setDoubleMinimum(self, min: float) """
        pass

    def setDoubleRange(self, min, max): # real signature unknown; restored from __doc__
        """ setDoubleRange(self, min: float, max: float) """
        pass

    def setDoubleStep(self, step): # real signature unknown; restored from __doc__
        """ setDoubleStep(self, step: float) """
        pass

    def setDoubleValue(self, value): # real signature unknown; restored from __doc__
        """ setDoubleValue(self, value: float) """
        pass

    def setInputMode(self, mode): # real signature unknown; restored from __doc__
        """ setInputMode(self, mode: QInputDialog.InputMode) """
        pass

    def setIntMaximum(self, max): # real signature unknown; restored from __doc__
        """ setIntMaximum(self, max: int) """
        pass

    def setIntMinimum(self, min): # real signature unknown; restored from __doc__
        """ setIntMinimum(self, min: int) """
        pass

    def setIntRange(self, min, max): # real signature unknown; restored from __doc__
        """ setIntRange(self, min: int, max: int) """
        pass

    def setIntStep(self, step): # real signature unknown; restored from __doc__
        """ setIntStep(self, step: int) """
        pass

    def setIntValue(self, value): # real signature unknown; restored from __doc__
        """ setIntValue(self, value: int) """
        pass

    def setLabelText(self, text, p_str=None): # real signature unknown; restored from __doc__
        """ setLabelText(self, text: Optional[str]) """
        pass

    def setOkButtonText(self, text, p_str=None): # real signature unknown; restored from __doc__
        """ setOkButtonText(self, text: Optional[str]) """
        pass

    def setOption(self, option, on=True): # real signature unknown; restored from __doc__
        """ setOption(self, option: QInputDialog.InputDialogOption, on: bool = True) """
        pass

    def setOptions(self, options, QInputDialog_InputDialogOptions=None, QInputDialog_InputDialogOption=None): # real signature unknown; restored from __doc__
        """ setOptions(self, options: Union[QInputDialog.InputDialogOptions, QInputDialog.InputDialogOption]) """
        pass

    def setTextEchoMode(self, mode): # real signature unknown; restored from __doc__
        """ setTextEchoMode(self, mode: QLineEdit.EchoMode) """
        pass

    def setTextValue(self, text, p_str=None): # real signature unknown; restored from __doc__
        """ setTextValue(self, text: Optional[str]) """
        pass

    def setVisible(self, visible): # real signature unknown; restored from __doc__
        """ setVisible(self, visible: bool) """
        pass

    def sharedPainter(self, *args, **kwargs): # real signature unknown
        pass

    def showEvent(self, *args, **kwargs): # real signature unknown
        pass

    def sizeHint(self): # real signature unknown; restored from __doc__
        """ sizeHint(self) -> QSize """
        pass

    def tabletEvent(self, *args, **kwargs): # real signature unknown
        pass

    def testOption(self, option): # real signature unknown; restored from __doc__
        """ testOption(self, option: QInputDialog.InputDialogOption) -> bool """
        return False

    def textEchoMode(self): # real signature unknown; restored from __doc__
        """ textEchoMode(self) -> QLineEdit.EchoMode """
        pass

    def textValue(self): # real signature unknown; restored from __doc__
        """ textValue(self) -> str """
        return ""

    def textValueChanged(self, *args, **kwargs): # real signature unknown
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
        pass

    def textValueSelected(self, *args, **kwargs): # real signature unknown
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def updateMicroFocus(self, *args, **kwargs): # real signature unknown
        pass

    def wheelEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, parent, QWidget=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    DoubleInput = 2
    IntInput = 1
    NoButtons = 1
    TextInput = 0
    UseListViewForComboBoxItems = 2
    UsePlainTextEditForTextInput = 4


