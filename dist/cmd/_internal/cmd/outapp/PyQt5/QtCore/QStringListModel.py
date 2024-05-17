# encoding: utf-8
# module PyQt5.QtCore
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtCore.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum
import sip as __sip


from .QAbstractListModel import QAbstractListModel

class QStringListModel(QAbstractListModel):
    """
    QStringListModel(parent: Optional[QObject] = None)
    QStringListModel(strings: Iterable[Optional[str]], parent: Optional[QObject] = None)
    """
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

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def createIndex(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def data(self, index, role): # real signature unknown; restored from __doc__
        """ data(self, index: QModelIndex, role: int) -> Any """
        pass

    def decodeData(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
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

    def insertRows(self, row, count, parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ insertRows(self, row: int, count: int, parent: QModelIndex = QModelIndex()) -> bool """
        pass

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def itemData(self, index): # real signature unknown; restored from __doc__
        """ itemData(self, index: QModelIndex) -> Dict[int, Any] """
        return {}

    def moveRows(self, sourceParent, sourceRow, count, destinationParent, destinationChild): # real signature unknown; restored from __doc__
        """ moveRows(self, sourceParent: QModelIndex, sourceRow: int, count: int, destinationParent: QModelIndex, destinationChild: int) -> bool """
        return False

    def persistentIndexList(self, *args, **kwargs): # real signature unknown
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
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

    def setItemData(self, index, roles, p_int=None, Any=None): # real signature unknown; restored from __doc__
        """ setItemData(self, index: QModelIndex, roles: Dict[int, Any]) -> bool """
        return False

    def setStringList(self, strings, Optional=None, p_str=None): # real signature unknown; restored from __doc__
        """ setStringList(self, strings: Iterable[Optional[str]]) """
        pass

    def sibling(self, row, column, idx): # real signature unknown; restored from __doc__
        """ sibling(self, row: int, column: int, idx: QModelIndex) -> QModelIndex """
        return QModelIndex

    def sort(self, column, order=None): # real signature unknown; restored from __doc__
        """ sort(self, column: int, order: Qt.SortOrder = Qt.AscendingOrder) """
        pass

    def stringList(self): # real signature unknown; restored from __doc__
        """ stringList(self) -> List[str] """
        return []

    def supportedDropActions(self): # real signature unknown; restored from __doc__
        """ supportedDropActions(self) -> Qt.DropActions """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass


