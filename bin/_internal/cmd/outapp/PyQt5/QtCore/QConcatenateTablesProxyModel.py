# encoding: utf-8
# module PyQt5.QtCore
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtCore.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum
import sip as __sip


from .QAbstractItemModel import QAbstractItemModel

class QConcatenateTablesProxyModel(QAbstractItemModel):
    """ QConcatenateTablesProxyModel(parent: Optional[QObject] = None) """
    def addSourceModel(self, sourceModel, QAbstractItemModel=None): # real signature unknown; restored from __doc__
        """ addSourceModel(self, sourceModel: Optional[QAbstractItemModel]) """
        pass

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

    def canDropMimeData(self, data, QMimeData=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ canDropMimeData(self, data: Optional[QMimeData], action: Qt.DropAction, row: int, column: int, parent: QModelIndex) -> bool """
        pass

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
        """ data(self, index: QModelIndex, role: int = Qt.ItemDataRole.DisplayRole) -> Any """
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

    def flags(self, index): # real signature unknown; restored from __doc__
        """ flags(self, index: QModelIndex) -> Qt.ItemFlags """
        pass

    def headerData(self, section, orientation, role=None): # real signature unknown; restored from __doc__
        """ headerData(self, section: int, orientation: Qt.Orientation, role: int = Qt.ItemDataRole.DisplayRole) -> Any """
        pass

    def index(self, row, column, parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ index(self, row: int, column: int, parent: QModelIndex = QModelIndex()) -> QModelIndex """
        pass

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def itemData(self, proxyIndex): # real signature unknown; restored from __doc__
        """ itemData(self, proxyIndex: QModelIndex) -> Dict[int, Any] """
        return {}

    def mapFromSource(self, sourceIndex): # real signature unknown; restored from __doc__
        """ mapFromSource(self, sourceIndex: QModelIndex) -> QModelIndex """
        return QModelIndex

    def mapToSource(self, proxyIndex): # real signature unknown; restored from __doc__
        """ mapToSource(self, proxyIndex: QModelIndex) -> QModelIndex """
        return QModelIndex

    def mimeData(self, indexes, QModelIndex=None): # real signature unknown; restored from __doc__
        """ mimeData(self, indexes: Iterable[QModelIndex]) -> Optional[QMimeData] """
        pass

    def mimeTypes(self): # real signature unknown; restored from __doc__
        """ mimeTypes(self) -> List[str] """
        return []

    def parent(self, index): # real signature unknown; restored from __doc__
        """ parent(self, index: QModelIndex) -> QModelIndex """
        return QModelIndex

    def persistentIndexList(self, *args, **kwargs): # real signature unknown
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def removeSourceModel(self, sourceModel, QAbstractItemModel=None): # real signature unknown; restored from __doc__
        """ removeSourceModel(self, sourceModel: Optional[QAbstractItemModel]) """
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
        """ setData(self, index: QModelIndex, value: Any, role: int = Qt.ItemDataRole.EditRole) -> bool """
        return False

    def setItemData(self, index, roles, p_int=None, Any=None): # real signature unknown; restored from __doc__
        """ setItemData(self, index: QModelIndex, roles: Dict[int, Any]) -> bool """
        return False

    def sourceModels(self): # real signature unknown; restored from __doc__
        """ sourceModels(self) -> List[QAbstractItemModel] """
        return []

    def span(self, index): # real signature unknown; restored from __doc__
        """ span(self, index: QModelIndex) -> QSize """
        return QSize

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, parent, QObject=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass


