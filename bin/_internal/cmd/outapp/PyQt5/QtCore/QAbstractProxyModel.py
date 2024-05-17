# encoding: utf-8
# module PyQt5.QtCore
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtCore.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum
import sip as __sip


from .QAbstractItemModel import QAbstractItemModel

class QAbstractProxyModel(QAbstractItemModel):
    """ QAbstractProxyModel(parent: Optional[QObject] = None) """
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

    def canDropMimeData(self, data, QMimeData=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ canDropMimeData(self, data: Optional[QMimeData], action: Qt.DropAction, row: int, column: int, parent: QModelIndex) -> bool """
        pass

    def canFetchMore(self, parent): # real signature unknown; restored from __doc__
        """ canFetchMore(self, parent: QModelIndex) -> bool """
        return False

    def changePersistentIndex(self, *args, **kwargs): # real signature unknown
        pass

    def changePersistentIndexList(self, *args, **kwargs): # real signature unknown
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def createIndex(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def data(self, proxyIndex, role=None): # real signature unknown; restored from __doc__
        """ data(self, proxyIndex: QModelIndex, role: int = Qt.DisplayRole) -> Any """
        pass

    def decodeData(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def dropMimeData(self, data, QMimeData=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ dropMimeData(self, data: Optional[QMimeData], action: Qt.DropAction, row: int, column: int, parent: QModelIndex) -> bool """
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

    def flags(self, index): # real signature unknown; restored from __doc__
        """ flags(self, index: QModelIndex) -> Qt.ItemFlags """
        pass

    def hasChildren(self, parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ hasChildren(self, parent: QModelIndex = QModelIndex()) -> bool """
        pass

    def headerData(self, section, orientation, role=None): # real signature unknown; restored from __doc__
        """ headerData(self, section: int, orientation: Qt.Orientation, role: int = Qt.DisplayRole) -> Any """
        pass

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def itemData(self, index): # real signature unknown; restored from __doc__
        """ itemData(self, index: QModelIndex) -> Dict[int, Any] """
        return {}

    def mapFromSource(self, sourceIndex): # real signature unknown; restored from __doc__
        """ mapFromSource(self, sourceIndex: QModelIndex) -> QModelIndex """
        return QModelIndex

    def mapSelectionFromSource(self, selection): # real signature unknown; restored from __doc__
        """ mapSelectionFromSource(self, selection: QItemSelection) -> QItemSelection """
        return QItemSelection

    def mapSelectionToSource(self, selection): # real signature unknown; restored from __doc__
        """ mapSelectionToSource(self, selection: QItemSelection) -> QItemSelection """
        return QItemSelection

    def mapToSource(self, proxyIndex): # real signature unknown; restored from __doc__
        """ mapToSource(self, proxyIndex: QModelIndex) -> QModelIndex """
        return QModelIndex

    def mimeData(self, indexes, QModelIndex=None): # real signature unknown; restored from __doc__
        """ mimeData(self, indexes: Iterable[QModelIndex]) -> Optional[QMimeData] """
        pass

    def mimeTypes(self): # real signature unknown; restored from __doc__
        """ mimeTypes(self) -> List[str] """
        return []

    def persistentIndexList(self, *args, **kwargs): # real signature unknown
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def resetInternalData(self): # real signature unknown; restored from __doc__
        """ resetInternalData(self) """
        pass

    def revert(self): # real signature unknown; restored from __doc__
        """ revert(self) """
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setData(self, index, value, role=None): # real signature unknown; restored from __doc__
        """ setData(self, index: QModelIndex, value: Any, role: int = Qt.EditRole) -> bool """
        return False

    def setHeaderData(self, section, orientation, value, role=None): # real signature unknown; restored from __doc__
        """ setHeaderData(self, section: int, orientation: Qt.Orientation, value: Any, role: int = Qt.EditRole) -> bool """
        return False

    def setItemData(self, index, roles, p_int=None, Any=None): # real signature unknown; restored from __doc__
        """ setItemData(self, index: QModelIndex, roles: Dict[int, Any]) -> bool """
        return False

    def setSourceModel(self, sourceModel, QAbstractItemModel=None): # real signature unknown; restored from __doc__
        """ setSourceModel(self, sourceModel: Optional[QAbstractItemModel]) """
        pass

    def sibling(self, row, column, idx): # real signature unknown; restored from __doc__
        """ sibling(self, row: int, column: int, idx: QModelIndex) -> QModelIndex """
        return QModelIndex

    def sort(self, column, order=None): # real signature unknown; restored from __doc__
        """ sort(self, column: int, order: Qt.SortOrder = Qt.AscendingOrder) """
        pass

    def sourceModel(self): # real signature unknown; restored from __doc__
        """ sourceModel(self) -> Optional[QAbstractItemModel] """
        pass

    def sourceModelChanged(self, *args, **kwargs): # real signature unknown
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

    def submit(self): # real signature unknown; restored from __doc__
        """ submit(self) -> bool """
        return False

    def supportedDragActions(self): # real signature unknown; restored from __doc__
        """ supportedDragActions(self) -> Qt.DropActions """
        pass

    def supportedDropActions(self): # real signature unknown; restored from __doc__
        """ supportedDropActions(self) -> Qt.DropActions """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, parent, QObject=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass


