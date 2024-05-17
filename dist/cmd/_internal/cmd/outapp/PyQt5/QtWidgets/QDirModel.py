# encoding: utf-8
# module PyQt5.QtWidgets
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtWidgets.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import PyQt5.QtGui as __PyQt5_QtGui
import sip as __sip


class QDirModel(__PyQt5_QtCore.QAbstractItemModel):
    """
    QDirModel(nameFilters: Iterable[Optional[str]], filters: Union[QDir.Filters, QDir.Filter], sort: Union[QDir.SortFlags, QDir.SortFlag], parent: Optional[QObject] = None)
    QDirModel(parent: Optional[QObject] = None)
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

    def fileIcon(self, index): # real signature unknown; restored from __doc__
        """ fileIcon(self, index: QModelIndex) -> QIcon """
        pass

    def fileInfo(self, index): # real signature unknown; restored from __doc__
        """ fileInfo(self, index: QModelIndex) -> QFileInfo """
        pass

    def fileName(self, index): # real signature unknown; restored from __doc__
        """ fileName(self, index: QModelIndex) -> str """
        return ""

    def filePath(self, index): # real signature unknown; restored from __doc__
        """ filePath(self, index: QModelIndex) -> str """
        return ""

    def filter(self): # real signature unknown; restored from __doc__
        """ filter(self) -> QDir.Filters """
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

    def iconProvider(self): # real signature unknown; restored from __doc__
        """ iconProvider(self) -> Optional[QFileIconProvider] """
        pass

    def index(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        index(self, row: int, column: int, parent: QModelIndex = QModelIndex()) -> QModelIndex
        index(self, path: Optional[str], column: int = 0) -> QModelIndex
        """
        pass

    def isDir(self, index): # real signature unknown; restored from __doc__
        """ isDir(self, index: QModelIndex) -> bool """
        return False

    def isReadOnly(self): # real signature unknown; restored from __doc__
        """ isReadOnly(self) -> bool """
        return False

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def lazyChildCount(self): # real signature unknown; restored from __doc__
        """ lazyChildCount(self) -> bool """
        return False

    def mimeData(self, indexes, QModelIndex=None): # real signature unknown; restored from __doc__
        """ mimeData(self, indexes: Iterable[QModelIndex]) -> Optional[QMimeData] """
        pass

    def mimeTypes(self): # real signature unknown; restored from __doc__
        """ mimeTypes(self) -> List[str] """
        return []

    def mkdir(self, parent, name, p_str=None): # real signature unknown; restored from __doc__
        """ mkdir(self, parent: QModelIndex, name: Optional[str]) -> QModelIndex """
        pass

    def nameFilters(self): # real signature unknown; restored from __doc__
        """ nameFilters(self) -> List[str] """
        return []

    def parent(self, child=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        parent(self, child: QModelIndex) -> QModelIndex
        parent(self) -> Optional[QObject]
        """
        pass

    def persistentIndexList(self, *args, **kwargs): # real signature unknown
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def refresh(self, parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ refresh(self, parent: QModelIndex = QModelIndex()) """
        pass

    def remove(self, index): # real signature unknown; restored from __doc__
        """ remove(self, index: QModelIndex) -> bool """
        return False

    def resetInternalData(self, *args, **kwargs): # real signature unknown
        pass

    def resolveSymlinks(self): # real signature unknown; restored from __doc__
        """ resolveSymlinks(self) -> bool """
        return False

    def rmdir(self, index): # real signature unknown; restored from __doc__
        """ rmdir(self, index: QModelIndex) -> bool """
        return False

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

    def setFilter(self, filters, QDir_Filters=None, QDir_Filter=None): # real signature unknown; restored from __doc__
        """ setFilter(self, filters: Union[QDir.Filters, QDir.Filter]) """
        pass

    def setIconProvider(self, provider, QFileIconProvider=None): # real signature unknown; restored from __doc__
        """ setIconProvider(self, provider: Optional[QFileIconProvider]) """
        pass

    def setLazyChildCount(self, enable): # real signature unknown; restored from __doc__
        """ setLazyChildCount(self, enable: bool) """
        pass

    def setNameFilters(self, filters, Optional=None, p_str=None): # real signature unknown; restored from __doc__
        """ setNameFilters(self, filters: Iterable[Optional[str]]) """
        pass

    def setReadOnly(self, enable): # real signature unknown; restored from __doc__
        """ setReadOnly(self, enable: bool) """
        pass

    def setResolveSymlinks(self, enable): # real signature unknown; restored from __doc__
        """ setResolveSymlinks(self, enable: bool) """
        pass

    def setSorting(self, sort, QDir_SortFlags=None, QDir_SortFlag=None): # real signature unknown; restored from __doc__
        """ setSorting(self, sort: Union[QDir.SortFlags, QDir.SortFlag]) """
        pass

    def sort(self, column, order=None): # real signature unknown; restored from __doc__
        """ sort(self, column: int, order: Qt.SortOrder = Qt.AscendingOrder) """
        pass

    def sorting(self): # real signature unknown; restored from __doc__
        """ sorting(self) -> QDir.SortFlags """
        pass

    def supportedDropActions(self): # real signature unknown; restored from __doc__
        """ supportedDropActions(self) -> Qt.DropActions """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    FileIconRole = 1
    FileNameRole = 258
    FilePathRole = 257


