# encoding: utf-8
# module PyQt5.QtCore
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtCore.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum
import sip as __sip


from .QObject import QObject

class QItemSelectionModel(QObject):
    """
    QItemSelectionModel(model: Optional[QAbstractItemModel] = None)
    QItemSelectionModel(model: Optional[QAbstractItemModel], parent: Optional[QObject])
    """
    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def clear(self): # real signature unknown; restored from __doc__
        """ clear(self) """
        pass

    def clearCurrentIndex(self): # real signature unknown; restored from __doc__
        """ clearCurrentIndex(self) """
        pass

    def clearSelection(self): # real signature unknown; restored from __doc__
        """ clearSelection(self) """
        pass

    def columnIntersectsSelection(self, column, parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ columnIntersectsSelection(self, column: int, parent: QModelIndex = QModelIndex()) -> bool """
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def currentChanged(self, *args, **kwargs): # real signature unknown
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

    def currentColumnChanged(self, *args, **kwargs): # real signature unknown
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

    def currentIndex(self): # real signature unknown; restored from __doc__
        """ currentIndex(self) -> QModelIndex """
        return QModelIndex

    def currentRowChanged(self, *args, **kwargs): # real signature unknown
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

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def emitSelectionChanged(self, newSelection, oldSelection): # real signature unknown; restored from __doc__
        """ emitSelectionChanged(self, newSelection: QItemSelection, oldSelection: QItemSelection) """
        pass

    def hasSelection(self): # real signature unknown; restored from __doc__
        """ hasSelection(self) -> bool """
        return False

    def isColumnSelected(self, column, parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ isColumnSelected(self, column: int, parent: QModelIndex = QModelIndex()) -> bool """
        pass

    def isRowSelected(self, row, parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ isRowSelected(self, row: int, parent: QModelIndex = QModelIndex()) -> bool """
        pass

    def isSelected(self, index): # real signature unknown; restored from __doc__
        """ isSelected(self, index: QModelIndex) -> bool """
        return False

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def model(self): # real signature unknown; restored from __doc__
        """ model(self) -> Optional[QAbstractItemModel] """
        pass

    def modelChanged(self, *args, **kwargs): # real signature unknown
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

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def reset(self): # real signature unknown; restored from __doc__
        """ reset(self) """
        pass

    def rowIntersectsSelection(self, row, parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ rowIntersectsSelection(self, row: int, parent: QModelIndex = QModelIndex()) -> bool """
        pass

    def select(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        select(self, index: QModelIndex, command: Union[QItemSelectionModel.SelectionFlags, QItemSelectionModel.SelectionFlag])
        select(self, selection: QItemSelection, command: Union[QItemSelectionModel.SelectionFlags, QItemSelectionModel.SelectionFlag])
        """
        pass

    def selectedColumns(self, row=0): # real signature unknown; restored from __doc__
        """ selectedColumns(self, row: int = 0) -> List[QModelIndex] """
        return []

    def selectedIndexes(self): # real signature unknown; restored from __doc__
        """ selectedIndexes(self) -> List[QModelIndex] """
        return []

    def selectedRows(self, column=0): # real signature unknown; restored from __doc__
        """ selectedRows(self, column: int = 0) -> List[QModelIndex] """
        return []

    def selection(self): # real signature unknown; restored from __doc__
        """ selection(self) -> QItemSelection """
        return QItemSelection

    def selectionChanged(self, *args, **kwargs): # real signature unknown
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

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setCurrentIndex(self, index, command, QItemSelectionModel_SelectionFlags=None, QItemSelectionModel_SelectionFlag=None): # real signature unknown; restored from __doc__
        """ setCurrentIndex(self, index: QModelIndex, command: Union[QItemSelectionModel.SelectionFlags, QItemSelectionModel.SelectionFlag]) """
        pass

    def setModel(self, model, QAbstractItemModel=None): # real signature unknown; restored from __doc__
        """ setModel(self, model: Optional[QAbstractItemModel]) """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, model, QAbstractItemModel=None, *args, **kwargs): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    Clear = 1
    ClearAndSelect = 3
    Columns = 64
    Current = 16
    Deselect = 4
    NoUpdate = 0
    Rows = 32
    Select = 2
    SelectCurrent = 18
    Toggle = 8
    ToggleCurrent = 24


