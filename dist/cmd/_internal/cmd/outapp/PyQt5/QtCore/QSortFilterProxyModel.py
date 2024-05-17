# encoding: utf-8
# module PyQt5.QtCore
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtCore.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum
import sip as __sip


from .QAbstractProxyModel import QAbstractProxyModel

class QSortFilterProxyModel(QAbstractProxyModel):
    """ QSortFilterProxyModel(parent: Optional[QObject] = None) """
    def beginInsertColumns(self, *args, **kwargs): # real signature unknown
        pass

    def beginInsertRows(self, *args, **kwargs): # real signature unknown
        pass

    def beginMoveColumns(self, *args, **kwargs): # real signature unknown
        pass

    def beginMoveRows(self, *args, **kwargs): # real signature unknown
        pass

    def beginRemoveColumns(self, *args, **kwargs): # real signature unknown
        pass

    def beginRemoveRows(self, *args, **kwargs): # real signature unknown
        pass

    def beginResetModel(self, *args, **kwargs): # real signature unknown
        pass

    def buddy(self, index): # real signature unknown; restored from __doc__
        """ buddy(self, index: QModelIndex) -> QModelIndex """
        return QModelIndex

    def canFetchMore(self, parent): # real signature unknown; restored from __doc__
        """ canFetchMore(self, parent: QModelIndex) -> bool """
        return False

    def changePersistentIndex(self, *args, **kwargs): # real signature unknown
        pass

    def changePersistentIndexList(self, *args, **kwargs): # real signature unknown
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def columnCount(self, parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ columnCount(self, parent: QModelIndex = QModelIndex()) -> int """
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def createIndex(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def data(self, index, role=None): # real signature unknown; restored from __doc__
        """ data(self, index: QModelIndex, role: int = Qt.DisplayRole) -> Any """
        pass

    def decodeData(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def dropMimeData(self, data, QMimeData=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ dropMimeData(self, data: Optional[QMimeData], action: Qt.DropAction, row: int, column: int, parent: QModelIndex) -> bool """
        pass

    def dynamicSortFilter(self): # real signature unknown; restored from __doc__
        """ dynamicSortFilter(self) -> bool """
        return False

    def dynamicSortFilterChanged(self, *args, **kwargs): # real signature unknown
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

    def encodeData(self, *args, **kwargs): # real signature unknown
        pass

    def endInsertColumns(self, *args, **kwargs): # real signature unknown
        pass

    def endInsertRows(self, *args, **kwargs): # real signature unknown
        pass

    def endMoveColumns(self, *args, **kwargs): # real signature unknown
        pass

    def endMoveRows(self, *args, **kwargs): # real signature unknown
        pass

    def endRemoveColumns(self, *args, **kwargs): # real signature unknown
        pass

    def endRemoveRows(self, *args, **kwargs): # real signature unknown
        pass

    def endResetModel(self, *args, **kwargs): # real signature unknown
        pass

    def fetchMore(self, parent): # real signature unknown; restored from __doc__
        """ fetchMore(self, parent: QModelIndex) """
        pass

    def filterAcceptsColumn(self, source_column, source_parent): # real signature unknown; restored from __doc__
        """ filterAcceptsColumn(self, source_column: int, source_parent: QModelIndex) -> bool """
        return False

    def filterAcceptsRow(self, source_row, source_parent): # real signature unknown; restored from __doc__
        """ filterAcceptsRow(self, source_row: int, source_parent: QModelIndex) -> bool """
        return False

    def filterCaseSensitivity(self): # real signature unknown; restored from __doc__
        """ filterCaseSensitivity(self) -> Qt.CaseSensitivity """
        pass

    def filterCaseSensitivityChanged(self, *args, **kwargs): # real signature unknown
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

    def filterKeyColumn(self): # real signature unknown; restored from __doc__
        """ filterKeyColumn(self) -> int """
        return 0

    def filterRegExp(self): # real signature unknown; restored from __doc__
        """ filterRegExp(self) -> QRegExp """
        return QRegExp

    def filterRegularExpression(self): # real signature unknown; restored from __doc__
        """ filterRegularExpression(self) -> QRegularExpression """
        return QRegularExpression

    def filterRole(self): # real signature unknown; restored from __doc__
        """ filterRole(self) -> int """
        return 0

    def filterRoleChanged(self, *args, **kwargs): # real signature unknown
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

    def flags(self, index): # real signature unknown; restored from __doc__
        """ flags(self, index: QModelIndex) -> Qt.ItemFlags """
        pass

    def hasChildren(self, parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ hasChildren(self, parent: QModelIndex = QModelIndex()) -> bool """
        pass

    def headerData(self, section, orientation, role=None): # real signature unknown; restored from __doc__
        """ headerData(self, section: int, orientation: Qt.Orientation, role: int = Qt.DisplayRole) -> Any """
        pass

    def index(self, row, column, parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ index(self, row: int, column: int, parent: QModelIndex = QModelIndex()) -> QModelIndex """
        pass

    def insertColumns(self, column, count, parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ insertColumns(self, column: int, count: int, parent: QModelIndex = QModelIndex()) -> bool """
        pass

    def insertRows(self, row, count, parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ insertRows(self, row: int, count: int, parent: QModelIndex = QModelIndex()) -> bool """
        pass

    def invalidate(self): # real signature unknown; restored from __doc__
        """ invalidate(self) """
        pass

    def invalidateFilter(self): # real signature unknown; restored from __doc__
        """ invalidateFilter(self) """
        pass

    def isRecursiveFilteringEnabled(self): # real signature unknown; restored from __doc__
        """ isRecursiveFilteringEnabled(self) -> bool """
        return False

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def isSortLocaleAware(self): # real signature unknown; restored from __doc__
        """ isSortLocaleAware(self) -> bool """
        return False

    def lessThan(self, left, right): # real signature unknown; restored from __doc__
        """ lessThan(self, left: QModelIndex, right: QModelIndex) -> bool """
        return False

    def mapFromSource(self, sourceIndex): # real signature unknown; restored from __doc__
        """ mapFromSource(self, sourceIndex: QModelIndex) -> QModelIndex """
        return QModelIndex

    def mapSelectionFromSource(self, sourceSelection): # real signature unknown; restored from __doc__
        """ mapSelectionFromSource(self, sourceSelection: QItemSelection) -> QItemSelection """
        return QItemSelection

    def mapSelectionToSource(self, proxySelection): # real signature unknown; restored from __doc__
        """ mapSelectionToSource(self, proxySelection: QItemSelection) -> QItemSelection """
        return QItemSelection

    def mapToSource(self, proxyIndex): # real signature unknown; restored from __doc__
        """ mapToSource(self, proxyIndex: QModelIndex) -> QModelIndex """
        return QModelIndex

    def match(self, start, role, value, hits=1, flags, Qt_MatchFlags=None, Qt_MatchFlag=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ match(self, start: QModelIndex, role: int, value: Any, hits: int = 1, flags: Union[Qt.MatchFlags, Qt.MatchFlag] = Qt.MatchStartsWith|Qt.MatchWrap) -> List[QModelIndex] """
        pass

    def mimeData(self, indexes, QModelIndex=None): # real signature unknown; restored from __doc__
        """ mimeData(self, indexes: Iterable[QModelIndex]) -> Optional[QMimeData] """
        pass

    def mimeTypes(self): # real signature unknown; restored from __doc__
        """ mimeTypes(self) -> List[str] """
        return []

    def parent(self, child=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        parent(self, child: QModelIndex) -> QModelIndex
        parent(self) -> Optional[QObject]
        """
        return QModelIndex

    def persistentIndexList(self, *args, **kwargs): # real signature unknown
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def recursiveFilteringEnabledChanged(self, *args, **kwargs): # real signature unknown
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

    def removeColumns(self, column, count, parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ removeColumns(self, column: int, count: int, parent: QModelIndex = QModelIndex()) -> bool """
        pass

    def removeRows(self, row, count, parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ removeRows(self, row: int, count: int, parent: QModelIndex = QModelIndex()) -> bool """
        pass

    def resetInternalData(self, *args, **kwargs): # real signature unknown
        pass

    def rowCount(self, parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ rowCount(self, parent: QModelIndex = QModelIndex()) -> int """
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setData(self, index, value, role=None): # real signature unknown; restored from __doc__
        """ setData(self, index: QModelIndex, value: Any, role: int = Qt.EditRole) -> bool """
        return False

    def setDynamicSortFilter(self, enable): # real signature unknown; restored from __doc__
        """ setDynamicSortFilter(self, enable: bool) """
        pass

    def setFilterCaseSensitivity(self, cs): # real signature unknown; restored from __doc__
        """ setFilterCaseSensitivity(self, cs: Qt.CaseSensitivity) """
        pass

    def setFilterFixedString(self, pattern, p_str=None): # real signature unknown; restored from __doc__
        """ setFilterFixedString(self, pattern: Optional[str]) """
        pass

    def setFilterKeyColumn(self, column): # real signature unknown; restored from __doc__
        """ setFilterKeyColumn(self, column: int) """
        pass

    def setFilterRegExp(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setFilterRegExp(self, regExp: QRegExp)
        setFilterRegExp(self, pattern: Optional[str])
        """
        pass

    def setFilterRegularExpression(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setFilterRegularExpression(self, regularExpression: QRegularExpression)
        setFilterRegularExpression(self, pattern: Optional[str])
        """
        pass

    def setFilterRole(self, role): # real signature unknown; restored from __doc__
        """ setFilterRole(self, role: int) """
        pass

    def setFilterWildcard(self, pattern, p_str=None): # real signature unknown; restored from __doc__
        """ setFilterWildcard(self, pattern: Optional[str]) """
        pass

    def setHeaderData(self, section, orientation, value, role=None): # real signature unknown; restored from __doc__
        """ setHeaderData(self, section: int, orientation: Qt.Orientation, value: Any, role: int = Qt.EditRole) -> bool """
        return False

    def setRecursiveFilteringEnabled(self, recursive): # real signature unknown; restored from __doc__
        """ setRecursiveFilteringEnabled(self, recursive: bool) """
        pass

    def setSortCaseSensitivity(self, cs): # real signature unknown; restored from __doc__
        """ setSortCaseSensitivity(self, cs: Qt.CaseSensitivity) """
        pass

    def setSortLocaleAware(self, on): # real signature unknown; restored from __doc__
        """ setSortLocaleAware(self, on: bool) """
        pass

    def setSortRole(self, role): # real signature unknown; restored from __doc__
        """ setSortRole(self, role: int) """
        pass

    def setSourceModel(self, sourceModel, QAbstractItemModel=None): # real signature unknown; restored from __doc__
        """ setSourceModel(self, sourceModel: Optional[QAbstractItemModel]) """
        pass

    def sibling(self, row, column, idx): # real signature unknown; restored from __doc__
        """ sibling(self, row: int, column: int, idx: QModelIndex) -> QModelIndex """
        return QModelIndex

    def sort(self, column, order=None): # real signature unknown; restored from __doc__
        """ sort(self, column: int, order: Qt.SortOrder = Qt.AscendingOrder) """
        pass

    def sortCaseSensitivity(self): # real signature unknown; restored from __doc__
        """ sortCaseSensitivity(self) -> Qt.CaseSensitivity """
        pass

    def sortCaseSensitivityChanged(self, *args, **kwargs): # real signature unknown
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

    def sortColumn(self): # real signature unknown; restored from __doc__
        """ sortColumn(self) -> int """
        return 0

    def sortLocaleAwareChanged(self, *args, **kwargs): # real signature unknown
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

    def sortOrder(self): # real signature unknown; restored from __doc__
        """ sortOrder(self) -> Qt.SortOrder """
        pass

    def sortRole(self): # real signature unknown; restored from __doc__
        """ sortRole(self) -> int """
        return 0

    def sortRoleChanged(self, *args, **kwargs): # real signature unknown
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

    def span(self, index): # real signature unknown; restored from __doc__
        """ span(self, index: QModelIndex) -> QSize """
        return QSize

    def supportedDropActions(self): # real signature unknown; restored from __doc__
        """ supportedDropActions(self) -> Qt.DropActions """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, parent, QObject=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass


