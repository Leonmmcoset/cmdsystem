# encoding: utf-8
# module PyQt5.QtHelp
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtHelp.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import PyQt5.QtWidgets as __PyQt5_QtWidgets
import sip as __sip


# no functions
# classes

class QCompressedHelpInfo(__sip.simplewrapper):
    """
    QCompressedHelpInfo()
    QCompressedHelpInfo(other: QCompressedHelpInfo)
    """
    def component(self): # real signature unknown; restored from __doc__
        """ component(self) -> str """
        return ""

    def fromCompressedHelpFile(self, documentationFileName, p_str=None): # real signature unknown; restored from __doc__
        """ fromCompressedHelpFile(documentationFileName: Optional[str]) -> QCompressedHelpInfo """
        return QCompressedHelpInfo

    def isNull(self): # real signature unknown; restored from __doc__
        """ isNull(self) -> bool """
        return False

    def namespaceName(self): # real signature unknown; restored from __doc__
        """ namespaceName(self) -> str """
        return ""

    def swap(self, other): # real signature unknown; restored from __doc__
        """ swap(self, other: QCompressedHelpInfo) """
        pass

    def version(self): # real signature unknown; restored from __doc__
        """ version(self) -> QVersionNumber """
        pass

    def __init__(self, other=None): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class QHelpContentItem(__sip.simplewrapper):
    # no doc
    def child(self, row): # real signature unknown; restored from __doc__
        """ child(self, row: int) -> Optional[QHelpContentItem] """
        pass

    def childCount(self): # real signature unknown; restored from __doc__
        """ childCount(self) -> int """
        return 0

    def childPosition(self, child, QHelpContentItem=None): # real signature unknown; restored from __doc__
        """ childPosition(self, child: Optional[QHelpContentItem]) -> int """
        return 0

    def parent(self): # real signature unknown; restored from __doc__
        """ parent(self) -> Optional[QHelpContentItem] """
        pass

    def row(self): # real signature unknown; restored from __doc__
        """ row(self) -> int """
        return 0

    def title(self): # real signature unknown; restored from __doc__
        """ title(self) -> str """
        return ""

    def url(self): # real signature unknown; restored from __doc__
        """ url(self) -> QUrl """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class QHelpContentModel(__PyQt5_QtCore.QAbstractItemModel):
    # no doc
    def columnCount(self, parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ columnCount(self, parent: QModelIndex = QModelIndex()) -> int """
        pass

    def contentItemAt(self, index): # real signature unknown; restored from __doc__
        """ contentItemAt(self, index: QModelIndex) -> Optional[QHelpContentItem] """
        pass

    def contentsCreated(self, *args, **kwargs): # real signature unknown
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

    def contentsCreationStarted(self, *args, **kwargs): # real signature unknown
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

    def createContents(self, customFilterName, p_str=None): # real signature unknown; restored from __doc__
        """ createContents(self, customFilterName: Optional[str]) """
        pass

    def data(self, index, role): # real signature unknown; restored from __doc__
        """ data(self, index: QModelIndex, role: int) -> Any """
        pass

    def index(self, row, column, parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ index(self, row: int, column: int, parent: QModelIndex = QModelIndex()) -> QModelIndex """
        pass

    def isCreatingContents(self): # real signature unknown; restored from __doc__
        """ isCreatingContents(self) -> bool """
        return False

    def parent(self, index): # real signature unknown; restored from __doc__
        """ parent(self, index: QModelIndex) -> QModelIndex """
        pass

    def rowCount(self, parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ rowCount(self, parent: QModelIndex = QModelIndex()) -> int """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class QHelpContentWidget(__PyQt5_QtWidgets.QTreeView):
    # no doc
    def indexOf(self, link): # real signature unknown; restored from __doc__
        """ indexOf(self, link: QUrl) -> QModelIndex """
        pass

    def linkActivated(self, *args, **kwargs): # real signature unknown
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

    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class QHelpEngineCore(__PyQt5_QtCore.QObject):
    """ QHelpEngineCore(collectionFile: Optional[str], parent: Optional[QObject] = None) """
    def addCustomFilter(self, filterName, p_str=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ addCustomFilter(self, filterName: Optional[str], attributes: Iterable[Optional[str]]) -> bool """
        pass

    def autoSaveFilter(self): # real signature unknown; restored from __doc__
        """ autoSaveFilter(self) -> bool """
        return False

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def collectionFile(self): # real signature unknown; restored from __doc__
        """ collectionFile(self) -> str """
        return ""

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def copyCollectionFile(self, fileName, p_str=None): # real signature unknown; restored from __doc__
        """ copyCollectionFile(self, fileName: Optional[str]) -> bool """
        return False

    def currentFilter(self): # real signature unknown; restored from __doc__
        """ currentFilter(self) -> str """
        return ""

    def currentFilterChanged(self, *args, **kwargs): # real signature unknown
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

    def customFilters(self): # real signature unknown; restored from __doc__
        """ customFilters(self) -> List[str] """
        return []

    def customValue(self, key, p_str=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ customValue(self, key: Optional[str], defaultValue: Any = None) -> Any """
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def documentationFileName(self, namespaceName, p_str=None): # real signature unknown; restored from __doc__
        """ documentationFileName(self, namespaceName: Optional[str]) -> str """
        return ""

    def documentsForIdentifier(self, id, p_str=None, *args=None, **kwargs=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        documentsForIdentifier(self, id: Optional[str]) -> List[QHelpLink]
        documentsForIdentifier(self, id: Optional[str], filterName: Optional[str]) -> List[QHelpLink]
        """
        return []

    def documentsForKeyword(self, keyword, p_str=None, *args=None, **kwargs=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        documentsForKeyword(self, keyword: Optional[str]) -> List[QHelpLink]
        documentsForKeyword(self, keyword: Optional[str], filterName: Optional[str]) -> List[QHelpLink]
        """
        return []

    def error(self): # real signature unknown; restored from __doc__
        """ error(self) -> str """
        return ""

    def fileData(self, url): # real signature unknown; restored from __doc__
        """ fileData(self, url: QUrl) -> QByteArray """
        pass

    def files(self, namespaceName, p_str=None, *args, **kwargs): # real signature unknown; restored from __doc__ with multiple overloads
        """
        files(self, namespaceName: Optional[str], filterAttributes: Iterable[Optional[str]], extensionFilter: Optional[str] = '') -> List[QUrl]
        files(self, namespaceName: Optional[str], filterName: Optional[str], extensionFilter: Optional[str] = '') -> List[QUrl]
        """
        pass

    def filterAttributes(self, filterName=None, p_str=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        filterAttributes(self) -> List[str]
        filterAttributes(self, filterName: Optional[str]) -> List[str]
        """
        return []

    def filterAttributeSets(self, namespaceName, p_str=None): # real signature unknown; restored from __doc__
        """ filterAttributeSets(self, namespaceName: Optional[str]) -> List[List[str]] """
        return []

    def filterEngine(self): # real signature unknown; restored from __doc__
        """ filterEngine(self) -> Optional[QHelpFilterEngine] """
        pass

    def findFile(self, url): # real signature unknown; restored from __doc__
        """ findFile(self, url: QUrl) -> QUrl """
        pass

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def linksForIdentifier(self, id, p_str=None): # real signature unknown; restored from __doc__
        """ linksForIdentifier(self, id: Optional[str]) -> Dict[str, QUrl] """
        return {}

    def linksForKeyword(self, keyword, p_str=None): # real signature unknown; restored from __doc__
        """ linksForKeyword(self, keyword: Optional[str]) -> Dict[str, QUrl] """
        return {}

    def metaData(self, documentationFileName, p_str=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ metaData(documentationFileName: Optional[str], name: Optional[str]) -> Any """
        pass

    def namespaceName(self, documentationFileName, p_str=None): # real signature unknown; restored from __doc__
        """ namespaceName(documentationFileName: Optional[str]) -> str """
        return ""

    def readersAboutToBeInvalidated(self, *args, **kwargs): # real signature unknown
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

    def registerDocumentation(self, documentationFileName, p_str=None): # real signature unknown; restored from __doc__
        """ registerDocumentation(self, documentationFileName: Optional[str]) -> bool """
        return False

    def registeredDocumentations(self): # real signature unknown; restored from __doc__
        """ registeredDocumentations(self) -> List[str] """
        return []

    def removeCustomFilter(self, filterName, p_str=None): # real signature unknown; restored from __doc__
        """ removeCustomFilter(self, filterName: Optional[str]) -> bool """
        return False

    def removeCustomValue(self, key, p_str=None): # real signature unknown; restored from __doc__
        """ removeCustomValue(self, key: Optional[str]) -> bool """
        return False

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setAutoSaveFilter(self, save): # real signature unknown; restored from __doc__
        """ setAutoSaveFilter(self, save: bool) """
        pass

    def setCollectionFile(self, fileName, p_str=None): # real signature unknown; restored from __doc__
        """ setCollectionFile(self, fileName: Optional[str]) """
        pass

    def setCurrentFilter(self, filterName, p_str=None): # real signature unknown; restored from __doc__
        """ setCurrentFilter(self, filterName: Optional[str]) """
        pass

    def setCustomValue(self, key, p_str=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ setCustomValue(self, key: Optional[str], value: Any) -> bool """
        pass

    def setupData(self): # real signature unknown; restored from __doc__
        """ setupData(self) -> bool """
        return False

    def setupFinished(self, *args, **kwargs): # real signature unknown
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

    def setupStarted(self, *args, **kwargs): # real signature unknown
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

    def setUsesFilterEngine(self, uses): # real signature unknown; restored from __doc__
        """ setUsesFilterEngine(self, uses: bool) """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def unregisterDocumentation(self, namespaceName, p_str=None): # real signature unknown; restored from __doc__
        """ unregisterDocumentation(self, namespaceName: Optional[str]) -> bool """
        return False

    def usesFilterEngine(self): # real signature unknown; restored from __doc__
        """ usesFilterEngine(self) -> bool """
        return False

    def warning(self, *args, **kwargs): # real signature unknown
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

    def __init__(self, collectionFile, p_str=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass


class QHelpEngine(QHelpEngineCore):
    """ QHelpEngine(collectionFile: Optional[str], parent: Optional[QObject] = None) """
    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def contentModel(self): # real signature unknown; restored from __doc__
        """ contentModel(self) -> Optional[QHelpContentModel] """
        pass

    def contentWidget(self): # real signature unknown; restored from __doc__
        """ contentWidget(self) -> Optional[QHelpContentWidget] """
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def indexModel(self): # real signature unknown; restored from __doc__
        """ indexModel(self) -> Optional[QHelpIndexModel] """
        pass

    def indexWidget(self): # real signature unknown; restored from __doc__
        """ indexWidget(self) -> Optional[QHelpIndexWidget] """
        pass

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def searchEngine(self): # real signature unknown; restored from __doc__
        """ searchEngine(self) -> Optional[QHelpSearchEngine] """
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, collectionFile, p_str=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass


class QHelpFilterData(__sip.simplewrapper):
    """
    QHelpFilterData()
    QHelpFilterData(other: QHelpFilterData)
    """
    def components(self): # real signature unknown; restored from __doc__
        """ components(self) -> List[str] """
        return []

    def setComponents(self, components, Optional=None, p_str=None): # real signature unknown; restored from __doc__
        """ setComponents(self, components: Iterable[Optional[str]]) """
        pass

    def setVersions(self, versions, QVersionNumber=None): # real signature unknown; restored from __doc__
        """ setVersions(self, versions: Iterable[QVersionNumber]) """
        pass

    def swap(self, other): # real signature unknown; restored from __doc__
        """ swap(self, other: QHelpFilterData) """
        pass

    def versions(self): # real signature unknown; restored from __doc__
        """ versions(self) -> List[QVersionNumber] """
        return []

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __init__(self, other=None): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __hash__ = None


class QHelpFilterEngine(__PyQt5_QtCore.QObject):
    # no doc
    def activeFilter(self): # real signature unknown; restored from __doc__
        """ activeFilter(self) -> str """
        return ""

    def availableComponents(self): # real signature unknown; restored from __doc__
        """ availableComponents(self) -> List[str] """
        return []

    def availableVersions(self): # real signature unknown; restored from __doc__
        """ availableVersions(self) -> List[QVersionNumber] """
        return []

    def filterActivated(self, *args, **kwargs): # real signature unknown
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

    def filterData(self, filterName, p_str=None): # real signature unknown; restored from __doc__
        """ filterData(self, filterName: Optional[str]) -> QHelpFilterData """
        return QHelpFilterData

    def filters(self): # real signature unknown; restored from __doc__
        """ filters(self) -> List[str] """
        return []

    def indices(self, filterName=None, p_str=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        indices(self) -> List[str]
        indices(self, filterName: Optional[str]) -> List[str]
        """
        return []

    def namespacesForFilter(self, filterName, p_str=None): # real signature unknown; restored from __doc__
        """ namespacesForFilter(self, filterName: Optional[str]) -> List[str] """
        return []

    def namespaceToComponent(self): # real signature unknown; restored from __doc__
        """ namespaceToComponent(self) -> Dict[str, str] """
        return {}

    def namespaceToVersion(self): # real signature unknown; restored from __doc__
        """ namespaceToVersion(self) -> Dict[str, QVersionNumber] """
        return {}

    def removeFilter(self, filterName, p_str=None): # real signature unknown; restored from __doc__
        """ removeFilter(self, filterName: Optional[str]) -> bool """
        return False

    def setActiveFilter(self, filterName, p_str=None): # real signature unknown; restored from __doc__
        """ setActiveFilter(self, filterName: Optional[str]) -> bool """
        return False

    def setFilterData(self, filterName, p_str=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ setFilterData(self, filterName: Optional[str], filterData: QHelpFilterData) -> bool """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class QHelpFilterSettingsWidget(__PyQt5_QtWidgets.QWidget):
    """ QHelpFilterSettingsWidget(parent: Optional[QWidget] = None) """
    def actionEvent(self, *args, **kwargs): # real signature unknown
        pass

    def applySettings(self, filterEngine, QHelpFilterEngine=None): # real signature unknown; restored from __doc__
        """ applySettings(self, filterEngine: Optional[QHelpFilterEngine]) -> bool """
        return False

    def changeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def closeEvent(self, *args, **kwargs): # real signature unknown
        pass

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

    def hideEvent(self, *args, **kwargs): # real signature unknown
        pass

    def initPainter(self, *args, **kwargs): # real signature unknown
        pass

    def inputMethodEvent(self, *args, **kwargs): # real signature unknown
        pass

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def keyPressEvent(self, *args, **kwargs): # real signature unknown
        pass

    def keyReleaseEvent(self, *args, **kwargs): # real signature unknown
        pass

    def leaveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def metric(self, *args, **kwargs): # real signature unknown
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

    def paintEvent(self, *args, **kwargs): # real signature unknown
        pass

    def readSettings(self, filterEngine, QHelpFilterEngine=None): # real signature unknown; restored from __doc__
        """ readSettings(self, filterEngine: Optional[QHelpFilterEngine]) """
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def resizeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setAvailableComponents(self, components, Optional=None, p_str=None): # real signature unknown; restored from __doc__
        """ setAvailableComponents(self, components: Iterable[Optional[str]]) """
        pass

    def setAvailableVersions(self, versions, QVersionNumber=None): # real signature unknown; restored from __doc__
        """ setAvailableVersions(self, versions: Iterable[QVersionNumber]) """
        pass

    def sharedPainter(self, *args, **kwargs): # real signature unknown
        pass

    def showEvent(self, *args, **kwargs): # real signature unknown
        pass

    def tabletEvent(self, *args, **kwargs): # real signature unknown
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def updateMicroFocus(self, *args, **kwargs): # real signature unknown
        pass

    def wheelEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, parent, QWidget=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass


class QHelpIndexModel(__PyQt5_QtCore.QStringListModel):
    # no doc
    def createIndex(self, customFilterName, p_str=None): # real signature unknown; restored from __doc__
        """ createIndex(self, customFilterName: Optional[str]) """
        pass

    def filter(self, filter, p_str=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ filter(self, filter: Optional[str], wildcard: Optional[str] = '') -> QModelIndex """
        pass

    def helpEngine(self): # real signature unknown; restored from __doc__
        """ helpEngine(self) -> Optional[QHelpEngineCore] """
        pass

    def indexCreated(self, *args, **kwargs): # real signature unknown
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

    def indexCreationStarted(self, *args, **kwargs): # real signature unknown
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

    def isCreatingIndex(self): # real signature unknown; restored from __doc__
        """ isCreatingIndex(self) -> bool """
        return False

    def linksForKeyword(self, keyword, p_str=None): # real signature unknown; restored from __doc__
        """ linksForKeyword(self, keyword: Optional[str]) -> Dict[str, QUrl] """
        return {}

    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class QHelpIndexWidget(__PyQt5_QtWidgets.QListView):
    # no doc
    def activateCurrentItem(self): # real signature unknown; restored from __doc__
        """ activateCurrentItem(self) """
        pass

    def documentActivated(self, *args, **kwargs): # real signature unknown
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

    def documentsActivated(self, *args, **kwargs): # real signature unknown
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

    def filterIndices(self, filter, p_str=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ filterIndices(self, filter: Optional[str], wildcard: Optional[str] = '') """
        pass

    def linkActivated(self, *args, **kwargs): # real signature unknown
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

    def linksActivated(self, *args, **kwargs): # real signature unknown
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

    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class QHelpLink(__sip.simplewrapper):
    """
    QHelpLink()
    QHelpLink(a0: QHelpLink)
    """
    def __init__(self, a0=None): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""




class QHelpSearchEngine(__PyQt5_QtCore.QObject):
    """ QHelpSearchEngine(helpEngine: Optional[QHelpEngineCore], parent: Optional[QObject] = None) """
    def cancelIndexing(self): # real signature unknown; restored from __doc__
        """ cancelIndexing(self) """
        pass

    def cancelSearching(self): # real signature unknown; restored from __doc__
        """ cancelSearching(self) """
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def hitCount(self): # real signature unknown; restored from __doc__
        """ hitCount(self) -> int """
        return 0

    def hits(self, start, end): # real signature unknown; restored from __doc__
        """ hits(self, start: int, end: int) -> List[Tuple[str, str]] """
        return []

    def indexingFinished(self, *args, **kwargs): # real signature unknown
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

    def indexingStarted(self, *args, **kwargs): # real signature unknown
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

    def query(self): # real signature unknown; restored from __doc__
        """ query(self) -> List[QHelpSearchQuery] """
        return []

    def queryWidget(self): # real signature unknown; restored from __doc__
        """ queryWidget(self) -> Optional[QHelpSearchQueryWidget] """
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def reindexDocumentation(self): # real signature unknown; restored from __doc__
        """ reindexDocumentation(self) """
        pass

    def resultWidget(self): # real signature unknown; restored from __doc__
        """ resultWidget(self) -> Optional[QHelpSearchResultWidget] """
        pass

    def search(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        search(self, queryList: Iterable[QHelpSearchQuery])
        search(self, searchInput: Optional[str])
        """
        pass

    def searchingFinished(self, *args, **kwargs): # real signature unknown
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

    def searchingStarted(self, *args, **kwargs): # real signature unknown
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

    def searchInput(self): # real signature unknown; restored from __doc__
        """ searchInput(self) -> str """
        return ""

    def searchResultCount(self): # real signature unknown; restored from __doc__
        """ searchResultCount(self) -> int """
        return 0

    def searchResults(self, start, end): # real signature unknown; restored from __doc__
        """ searchResults(self, start: int, end: int) -> List[QHelpSearchResult] """
        return []

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, helpEngine, QHelpEngineCore=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass


class QHelpSearchQuery(__sip.simplewrapper):
    """
    QHelpSearchQuery()
    QHelpSearchQuery(field: QHelpSearchQuery.FieldName, wordList: Iterable[Optional[str]])
    QHelpSearchQuery(a0: QHelpSearchQuery)
    """
    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    ALL = 4
    ATLEAST = 5
    DEFAULT = 0
    FUZZY = 1
    PHRASE = 3
    WITHOUT = 2


class QHelpSearchQueryWidget(__PyQt5_QtWidgets.QWidget):
    """ QHelpSearchQueryWidget(parent: Optional[QWidget] = None) """
    def actionEvent(self, *args, **kwargs): # real signature unknown
        pass

    def changeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def closeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def collapseExtendedSearch(self): # real signature unknown; restored from __doc__
        """ collapseExtendedSearch(self) """
        pass

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

    def expandExtendedSearch(self): # real signature unknown; restored from __doc__
        """ expandExtendedSearch(self) """
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

    def hideEvent(self, *args, **kwargs): # real signature unknown
        pass

    def initPainter(self, *args, **kwargs): # real signature unknown
        pass

    def inputMethodEvent(self, *args, **kwargs): # real signature unknown
        pass

    def isCompactMode(self): # real signature unknown; restored from __doc__
        """ isCompactMode(self) -> bool """
        return False

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def keyPressEvent(self, *args, **kwargs): # real signature unknown
        pass

    def keyReleaseEvent(self, *args, **kwargs): # real signature unknown
        pass

    def leaveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def metric(self, *args, **kwargs): # real signature unknown
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

    def paintEvent(self, *args, **kwargs): # real signature unknown
        pass

    def query(self): # real signature unknown; restored from __doc__
        """ query(self) -> List[QHelpSearchQuery] """
        return []

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def resizeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def search(self, *args, **kwargs): # real signature unknown
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

    def searchInput(self): # real signature unknown; restored from __doc__
        """ searchInput(self) -> str """
        return ""

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setCompactMode(self, on): # real signature unknown; restored from __doc__
        """ setCompactMode(self, on: bool) """
        pass

    def setQuery(self, queryList, QHelpSearchQuery=None): # real signature unknown; restored from __doc__
        """ setQuery(self, queryList: Iterable[QHelpSearchQuery]) """
        pass

    def setSearchInput(self, searchInput, p_str=None): # real signature unknown; restored from __doc__
        """ setSearchInput(self, searchInput: Optional[str]) """
        pass

    def sharedPainter(self, *args, **kwargs): # real signature unknown
        pass

    def showEvent(self, *args, **kwargs): # real signature unknown
        pass

    def tabletEvent(self, *args, **kwargs): # real signature unknown
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def updateMicroFocus(self, *args, **kwargs): # real signature unknown
        pass

    def wheelEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, parent, QWidget=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass


class QHelpSearchResult(__sip.simplewrapper):
    """
    QHelpSearchResult()
    QHelpSearchResult(other: QHelpSearchResult)
    QHelpSearchResult(url: QUrl, title: Optional[str], snippet: Optional[str])
    """
    def snippet(self): # real signature unknown; restored from __doc__
        """ snippet(self) -> str """
        return ""

    def title(self): # real signature unknown; restored from __doc__
        """ title(self) -> str """
        return ""

    def url(self): # real signature unknown; restored from __doc__
        """ url(self) -> QUrl """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class QHelpSearchResultWidget(__PyQt5_QtWidgets.QWidget):
    # no doc
    def linkAt(self, point): # real signature unknown; restored from __doc__
        """ linkAt(self, point: QPoint) -> QUrl """
        pass

    def requestShowLink(self, *args, **kwargs): # real signature unknown
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

    def __init__(self, *args, **kwargs): # real signature unknown
        pass


# variables with complex values



