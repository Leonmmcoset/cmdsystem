# encoding: utf-8
# module PyQt5.QtCore
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtCore.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum
import sip as __sip


from .QAbstractProxyModel import QAbstractProxyModel

class QIdentityProxyModel(QAbstractProxyModel):
    """ QIdentityProxyModel(parent: Optional[QObject] = None) """
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

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

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

    def match(self, start, role, value, hits=1, flags, Qt_MatchFlags=None, Qt_MatchFlag=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ match(self, start: QModelIndex, role: int, value: Any, hits: int = 1, flags: Union[Qt.MatchFlags, Qt.MatchFlag] = Qt.MatchStartsWith|Qt.MatchWrap) -> List[QModelIndex] """
        pass

    def moveColumns(self, sourceParent, sourceColumn, count, destinationParent, destinationChild): # real signature unknown; restored from __doc__
        """ moveColumns(self, sourceParent: QModelIndex, sourceColumn: int, count: int, destinationParent: QModelIndex, destinationChild: int) -> bool """
        return False

    def moveRows(self, sourceParent, sourceRow, count, destinationParent, destinationChild): # real signature unknown; restored from __doc__
        """ moveRows(self, sourceParent: QModelIndex, sourceRow: int, count: int, destinationParent: QModelIndex, destinationChild: int) -> bool """
        return False

    def parent(self, child): # real signature unknown; restored from __doc__
        """ parent(self, child: QModelIndex) -> QModelIndex """
        return QModelIndex

    def persistentIndexList(self, *args, **kwargs): # real signature unknown
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
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

    def setSourceModel(self, sourceModel, QAbstractItemModel=None): # real signature unknown; restored from __doc__
        """ setSourceModel(self, sourceModel: Optional[QAbstractItemModel]) """
        pass

    def sibling(self, row, column, idx): # real signature unknown; restored from __doc__
        """ sibling(self, row: int, column: int, idx: QModelIndex) -> QModelIndex """
        return QModelIndex

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, parent, QObject=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass


