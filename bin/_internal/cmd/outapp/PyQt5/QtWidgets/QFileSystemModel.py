# encoding: utf-8
# module PyQt5.QtWidgets
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtWidgets.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import PyQt5.QtGui as __PyQt5_QtGui
import sip as __sip


class QFileSystemModel(__PyQt5_QtCore.QAbstractItemModel):
    """ QFileSystemModel(parent: Optional[QObject] = None) """
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
        """ data(self, index: QModelIndex, role: int = Qt.ItemDataRole.DisplayRole) -> Any """
        pass

    def decodeData(self, *args, **kwargs): # real signature unknown
        pass

    def directoryLoaded(self, *args, **kwargs): # real signature unknown
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

    def event(self, event, QEvent=None): # real signature unknown; restored from __doc__
        """ event(self, event: Optional[QEvent]) -> bool """
        return False

    def fetchMore(self, parent): # real signature unknown; restored from __doc__
        """ fetchMore(self, parent: QModelIndex) """
        pass

    def fileIcon(self, aindex): # real signature unknown; restored from __doc__
        """ fileIcon(self, aindex: QModelIndex) -> QIcon """
        pass

    def fileInfo(self, aindex): # real signature unknown; restored from __doc__
        """ fileInfo(self, aindex: QModelIndex) -> QFileInfo """
        pass

    def fileName(self, aindex): # real signature unknown; restored from __doc__
        """ fileName(self, aindex: QModelIndex) -> str """
        return ""

    def filePath(self, index): # real signature unknown; restored from __doc__
        """ filePath(self, index: QModelIndex) -> str """
        return ""

    def fileRenamed(self, *args, **kwargs): # real signature unknown
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
        """ headerData(self, section: int, orientation: Qt.Orientation, role: int = Qt.ItemDataRole.DisplayRole) -> Any """
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

    def lastModified(self, index): # real signature unknown; restored from __doc__
        """ lastModified(self, index: QModelIndex) -> QDateTime """
        pass

    def mimeData(self, indexes, QModelIndex=None): # real signature unknown; restored from __doc__
        """ mimeData(self, indexes: Iterable[QModelIndex]) -> Optional[QMimeData] """
        pass

    def mimeTypes(self): # real signature unknown; restored from __doc__
        """ mimeTypes(self) -> List[str] """
        return []

    def mkdir(self, parent, name, p_str=None): # real signature unknown; restored from __doc__
        """ mkdir(self, parent: QModelIndex, name: Optional[str]) -> QModelIndex """
        pass

    def myComputer(self, role=None): # real signature unknown; restored from __doc__
        """ myComputer(self, role: int = Qt.ItemDataRole.DisplayRole) -> Any """
        pass

    def nameFilterDisables(self): # real signature unknown; restored from __doc__
        """ nameFilterDisables(self) -> bool """
        return False

    def nameFilters(self): # real signature unknown; restored from __doc__
        """ nameFilters(self) -> List[str] """
        return []

    def options(self): # real signature unknown; restored from __doc__
        """ options(self) -> QFileSystemModel.Options """
        pass

    def parent(self, child): # real signature unknown; restored from __doc__
        """ parent(self, child: QModelIndex) -> QModelIndex """
        pass

    def permissions(self, index): # real signature unknown; restored from __doc__
        """ permissions(self, index: QModelIndex) -> QFileDevice.Permissions """
        pass

    def persistentIndexList(self, *args, **kwargs): # real signature unknown
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
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

    def rootDirectory(self): # real signature unknown; restored from __doc__
        """ rootDirectory(self) -> QDir """
        pass

    def rootPath(self): # real signature unknown; restored from __doc__
        """ rootPath(self) -> str """
        return ""

    def rootPathChanged(self, *args, **kwargs): # real signature unknown
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

    def setFilter(self, filters, QDir_Filters=None, QDir_Filter=None): # real signature unknown; restored from __doc__
        """ setFilter(self, filters: Union[QDir.Filters, QDir.Filter]) """
        pass

    def setIconProvider(self, provider, QFileIconProvider=None): # real signature unknown; restored from __doc__
        """ setIconProvider(self, provider: Optional[QFileIconProvider]) """
        pass

    def setNameFilterDisables(self, enable): # real signature unknown; restored from __doc__
        """ setNameFilterDisables(self, enable: bool) """
        pass

    def setNameFilters(self, filters, Optional=None, p_str=None): # real signature unknown; restored from __doc__
        """ setNameFilters(self, filters: Iterable[Optional[str]]) """
        pass

    def setOption(self, option, on=True): # real signature unknown; restored from __doc__
        """ setOption(self, option: QFileSystemModel.Option, on: bool = True) """
        pass

    def setOptions(self, options, QFileSystemModel_Options=None, QFileSystemModel_Option=None): # real signature unknown; restored from __doc__
        """ setOptions(self, options: Union[QFileSystemModel.Options, QFileSystemModel.Option]) """
        pass

    def setReadOnly(self, enable): # real signature unknown; restored from __doc__
        """ setReadOnly(self, enable: bool) """
        pass

    def setResolveSymlinks(self, enable): # real signature unknown; restored from __doc__
        """ setResolveSymlinks(self, enable: bool) """
        pass

    def setRootPath(self, path, p_str=None): # real signature unknown; restored from __doc__
        """ setRootPath(self, path: Optional[str]) -> QModelIndex """
        pass

    def sibling(self, row, column, idx): # real signature unknown; restored from __doc__
        """ sibling(self, row: int, column: int, idx: QModelIndex) -> QModelIndex """
        pass

    def size(self, index): # real signature unknown; restored from __doc__
        """ size(self, index: QModelIndex) -> int """
        return 0

    def sort(self, column, order=None): # real signature unknown; restored from __doc__
        """ sort(self, column: int, order: Qt.SortOrder = Qt.AscendingOrder) """
        pass

    def supportedDropActions(self): # real signature unknown; restored from __doc__
        """ supportedDropActions(self) -> Qt.DropActions """
        pass

    def testOption(self, option): # real signature unknown; restored from __doc__
        """ testOption(self, option: QFileSystemModel.Option) -> bool """
        return False

    def timerEvent(self, event, QTimerEvent=None): # real signature unknown; restored from __doc__
        """ timerEvent(self, event: Optional[QTimerEvent]) """
        pass

    def type(self, index): # real signature unknown; restored from __doc__
        """ type(self, index: QModelIndex) -> str """
        return ""

    def __init__(self, parent, QObject=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    DontResolveSymlinks = 2
    DontUseCustomDirectoryIcons = 4
    DontWatchForChanges = 1
    FileIconRole = 1
    FileNameRole = 258
    FilePathRole = 257
    FilePermissions = 259


