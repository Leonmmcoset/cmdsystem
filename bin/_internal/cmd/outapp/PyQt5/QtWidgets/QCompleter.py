# encoding: utf-8
# module PyQt5.QtWidgets
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtWidgets.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import PyQt5.QtGui as __PyQt5_QtGui
import sip as __sip


class QCompleter(__PyQt5_QtCore.QObject):
    """
    QCompleter(model: Optional[QAbstractItemModel], parent: Optional[QObject] = None)
    QCompleter(list: Iterable[Optional[str]], parent: Optional[QObject] = None)
    QCompleter(parent: Optional[QObject] = None)
    """
    def activated(self, *args, **kwargs): # real signature unknown
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

    def caseSensitivity(self): # real signature unknown; restored from __doc__
        """ caseSensitivity(self) -> Qt.CaseSensitivity """
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def complete(self, rect=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ complete(self, rect: QRect = QRect()) """
        pass

    def completionColumn(self): # real signature unknown; restored from __doc__
        """ completionColumn(self) -> int """
        return 0

    def completionCount(self): # real signature unknown; restored from __doc__
        """ completionCount(self) -> int """
        return 0

    def completionMode(self): # real signature unknown; restored from __doc__
        """ completionMode(self) -> QCompleter.CompletionMode """
        pass

    def completionModel(self): # real signature unknown; restored from __doc__
        """ completionModel(self) -> Optional[QAbstractItemModel] """
        pass

    def completionPrefix(self): # real signature unknown; restored from __doc__
        """ completionPrefix(self) -> str """
        return ""

    def completionRole(self): # real signature unknown; restored from __doc__
        """ completionRole(self) -> int """
        return 0

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def currentCompletion(self): # real signature unknown; restored from __doc__
        """ currentCompletion(self) -> str """
        return ""

    def currentIndex(self): # real signature unknown; restored from __doc__
        """ currentIndex(self) -> QModelIndex """
        pass

    def currentRow(self): # real signature unknown; restored from __doc__
        """ currentRow(self) -> int """
        return 0

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def event(self, a0, QEvent=None): # real signature unknown; restored from __doc__
        """ event(self, a0: Optional[QEvent]) -> bool """
        return False

    def eventFilter(self, o, QObject=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ eventFilter(self, o: Optional[QObject], e: Optional[QEvent]) -> bool """
        pass

    def filterMode(self): # real signature unknown; restored from __doc__
        """ filterMode(self) -> Qt.MatchFlags """
        pass

    def highlighted(self, *args, **kwargs): # real signature unknown
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

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def maxVisibleItems(self): # real signature unknown; restored from __doc__
        """ maxVisibleItems(self) -> int """
        return 0

    def model(self): # real signature unknown; restored from __doc__
        """ model(self) -> Optional[QAbstractItemModel] """
        pass

    def modelSorting(self): # real signature unknown; restored from __doc__
        """ modelSorting(self) -> QCompleter.ModelSorting """
        pass

    def pathFromIndex(self, index): # real signature unknown; restored from __doc__
        """ pathFromIndex(self, index: QModelIndex) -> str """
        return ""

    def popup(self): # real signature unknown; restored from __doc__
        """ popup(self) -> Optional[QAbstractItemView] """
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setCaseSensitivity(self, caseSensitivity): # real signature unknown; restored from __doc__
        """ setCaseSensitivity(self, caseSensitivity: Qt.CaseSensitivity) """
        pass

    def setCompletionColumn(self, column): # real signature unknown; restored from __doc__
        """ setCompletionColumn(self, column: int) """
        pass

    def setCompletionMode(self, mode): # real signature unknown; restored from __doc__
        """ setCompletionMode(self, mode: QCompleter.CompletionMode) """
        pass

    def setCompletionPrefix(self, prefix, p_str=None): # real signature unknown; restored from __doc__
        """ setCompletionPrefix(self, prefix: Optional[str]) """
        pass

    def setCompletionRole(self, role): # real signature unknown; restored from __doc__
        """ setCompletionRole(self, role: int) """
        pass

    def setCurrentRow(self, row): # real signature unknown; restored from __doc__
        """ setCurrentRow(self, row: int) -> bool """
        return False

    def setFilterMode(self, filterMode, Qt_MatchFlags=None, Qt_MatchFlag=None): # real signature unknown; restored from __doc__
        """ setFilterMode(self, filterMode: Union[Qt.MatchFlags, Qt.MatchFlag]) """
        pass

    def setMaxVisibleItems(self, maxItems): # real signature unknown; restored from __doc__
        """ setMaxVisibleItems(self, maxItems: int) """
        pass

    def setModel(self, c, QAbstractItemModel=None): # real signature unknown; restored from __doc__
        """ setModel(self, c: Optional[QAbstractItemModel]) """
        pass

    def setModelSorting(self, sorting): # real signature unknown; restored from __doc__
        """ setModelSorting(self, sorting: QCompleter.ModelSorting) """
        pass

    def setPopup(self, popup, QAbstractItemView=None): # real signature unknown; restored from __doc__
        """ setPopup(self, popup: Optional[QAbstractItemView]) """
        pass

    def setWidget(self, widget, QWidget=None): # real signature unknown; restored from __doc__
        """ setWidget(self, widget: Optional[QWidget]) """
        pass

    def setWrapAround(self, wrap): # real signature unknown; restored from __doc__
        """ setWrapAround(self, wrap: bool) """
        pass

    def splitPath(self, path, p_str=None): # real signature unknown; restored from __doc__
        """ splitPath(self, path: Optional[str]) -> List[str] """
        return []

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def widget(self): # real signature unknown; restored from __doc__
        """ widget(self) -> Optional[QWidget] """
        pass

    def wrapAround(self): # real signature unknown; restored from __doc__
        """ wrapAround(self) -> bool """
        return False

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    CaseInsensitivelySortedModel = 2
    CaseSensitivelySortedModel = 1
    InlineCompletion = 2
    PopupCompletion = 0
    UnfilteredPopupCompletion = 1
    UnsortedModel = 0


