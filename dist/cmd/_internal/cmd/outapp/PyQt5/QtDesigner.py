# encoding: utf-8
# module PyQt5.QtDesigner
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtDesigner.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import PyQt5.QtWidgets as __PyQt5_QtWidgets
import sip as __sip


# no functions
# classes

class QAbstractExtensionFactory(__sip.simplewrapper):
    """
    QAbstractExtensionFactory()
    QAbstractExtensionFactory(a0: QAbstractExtensionFactory)
    """
    def extension(self, p_object, QObject=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ extension(self, object: Optional[QObject], iid: Optional[str]) -> Optional[QObject] """
        pass

    def __init__(self, a0=None): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class QAbstractExtensionManager(__sip.simplewrapper):
    """
    QAbstractExtensionManager()
    QAbstractExtensionManager(a0: QAbstractExtensionManager)
    """
    def extension(self, p_object, QObject=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ extension(self, object: Optional[QObject], iid: Optional[str]) -> Optional[QObject] """
        pass

    def registerExtensions(self, factory, QAbstractExtensionFactory=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ registerExtensions(self, factory: Optional[QAbstractExtensionFactory], iid: Optional[str]) """
        pass

    def unregisterExtensions(self, factory, QAbstractExtensionFactory=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ unregisterExtensions(self, factory: Optional[QAbstractExtensionFactory], iid: Optional[str]) """
        pass

    def __init__(self, a0=None): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class QAbstractFormBuilder(__sip.simplewrapper):
    """ QAbstractFormBuilder() """
    def errorString(self): # real signature unknown; restored from __doc__
        """ errorString(self) -> str """
        return ""

    def load(self, device, QIODevice=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ load(self, device: Optional[QIODevice], parent: Optional[QWidget] = None) -> Optional[QWidget] """
        pass

    def save(self, dev, QIODevice=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ save(self, dev: Optional[QIODevice], widget: Optional[QWidget]) """
        pass

    def setWorkingDirectory(self, directory): # real signature unknown; restored from __doc__
        """ setWorkingDirectory(self, directory: QDir) """
        pass

    def workingDirectory(self): # real signature unknown; restored from __doc__
        """ workingDirectory(self) -> QDir """
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class QDesignerActionEditorInterface(__PyQt5_QtWidgets.QWidget):
    """ QDesignerActionEditorInterface(parent: Optional[QWidget], flags: Union[Qt.WindowFlags, Qt.WindowType] = 0) """
    def actionEvent(self, *args, **kwargs): # real signature unknown
        pass

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

    def core(self): # real signature unknown; restored from __doc__
        """ core(self) -> Optional[QDesignerFormEditorInterface] """
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

    def manageAction(self, action, QAction=None): # real signature unknown; restored from __doc__
        """ manageAction(self, action: Optional[QAction]) """
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

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def resizeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setFormWindow(self, formWindow, QDesignerFormWindowInterface=None): # real signature unknown; restored from __doc__
        """ setFormWindow(self, formWindow: Optional[QDesignerFormWindowInterface]) """
        pass

    def sharedPainter(self, *args, **kwargs): # real signature unknown
        pass

    def showEvent(self, *args, **kwargs): # real signature unknown
        pass

    def tabletEvent(self, *args, **kwargs): # real signature unknown
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def unmanageAction(self, action, QAction=None): # real signature unknown; restored from __doc__
        """ unmanageAction(self, action: Optional[QAction]) """
        pass

    def updateMicroFocus(self, *args, **kwargs): # real signature unknown
        pass

    def wheelEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, parent, QWidget=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass


class QDesignerContainerExtension(__sip.simplewrapper):
    """
    QDesignerContainerExtension()
    QDesignerContainerExtension(a0: QDesignerContainerExtension)
    """
    def addWidget(self, widget, QWidget=None): # real signature unknown; restored from __doc__
        """ addWidget(self, widget: Optional[QWidget]) """
        pass

    def canAddWidget(self): # real signature unknown; restored from __doc__
        """ canAddWidget(self) -> bool """
        return False

    def canRemove(self, index): # real signature unknown; restored from __doc__
        """ canRemove(self, index: int) -> bool """
        return False

    def count(self): # real signature unknown; restored from __doc__
        """ count(self) -> int """
        return 0

    def currentIndex(self): # real signature unknown; restored from __doc__
        """ currentIndex(self) -> int """
        return 0

    def insertWidget(self, index, widget, QWidget=None): # real signature unknown; restored from __doc__
        """ insertWidget(self, index: int, widget: Optional[QWidget]) """
        pass

    def remove(self, index): # real signature unknown; restored from __doc__
        """ remove(self, index: int) """
        pass

    def setCurrentIndex(self, index): # real signature unknown; restored from __doc__
        """ setCurrentIndex(self, index: int) """
        pass

    def widget(self, index): # real signature unknown; restored from __doc__
        """ widget(self, index: int) -> Optional[QWidget] """
        pass

    def __init__(self, a0=None): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    def __len__(self, *args, **kwargs): # real signature unknown
        """ Return len(self). """
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class QDesignerCustomWidgetCollectionInterface(__sip.simplewrapper):
    """
    QDesignerCustomWidgetCollectionInterface()
    QDesignerCustomWidgetCollectionInterface(a0: QDesignerCustomWidgetCollectionInterface)
    """
    def customWidgets(self): # real signature unknown; restored from __doc__
        """ customWidgets(self) -> List[QDesignerCustomWidgetInterface] """
        return []

    def __init__(self, a0=None): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class QDesignerCustomWidgetInterface(__sip.simplewrapper):
    """
    QDesignerCustomWidgetInterface()
    QDesignerCustomWidgetInterface(a0: QDesignerCustomWidgetInterface)
    """
    def codeTemplate(self): # real signature unknown; restored from __doc__
        """ codeTemplate(self) -> str """
        return ""

    def createWidget(self, parent, QWidget=None): # real signature unknown; restored from __doc__
        """ createWidget(self, parent: Optional[QWidget]) -> Optional[QWidget] """
        pass

    def domXml(self): # real signature unknown; restored from __doc__
        """ domXml(self) -> str """
        return ""

    def group(self): # real signature unknown; restored from __doc__
        """ group(self) -> str """
        return ""

    def icon(self): # real signature unknown; restored from __doc__
        """ icon(self) -> QIcon """
        pass

    def includeFile(self): # real signature unknown; restored from __doc__
        """ includeFile(self) -> str """
        return ""

    def initialize(self, core, QDesignerFormEditorInterface=None): # real signature unknown; restored from __doc__
        """ initialize(self, core: Optional[QDesignerFormEditorInterface]) """
        pass

    def isContainer(self): # real signature unknown; restored from __doc__
        """ isContainer(self) -> bool """
        return False

    def isInitialized(self): # real signature unknown; restored from __doc__
        """ isInitialized(self) -> bool """
        return False

    def name(self): # real signature unknown; restored from __doc__
        """ name(self) -> str """
        return ""

    def toolTip(self): # real signature unknown; restored from __doc__
        """ toolTip(self) -> str """
        return ""

    def whatsThis(self): # real signature unknown; restored from __doc__
        """ whatsThis(self) -> str """
        return ""

    def __init__(self, a0=None): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class QDesignerFormEditorInterface(__PyQt5_QtCore.QObject):
    """ QDesignerFormEditorInterface(parent: Optional[QObject] = None) """
    def actionEditor(self): # real signature unknown; restored from __doc__
        """ actionEditor(self) -> Optional[QDesignerActionEditorInterface] """
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def extensionManager(self): # real signature unknown; restored from __doc__
        """ extensionManager(self) -> Optional[QExtensionManager] """
        pass

    def formWindowManager(self): # real signature unknown; restored from __doc__
        """ formWindowManager(self) -> Optional[QDesignerFormWindowManagerInterface] """
        pass

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def objectInspector(self): # real signature unknown; restored from __doc__
        """ objectInspector(self) -> Optional[QDesignerObjectInspectorInterface] """
        pass

    def propertyEditor(self): # real signature unknown; restored from __doc__
        """ propertyEditor(self) -> Optional[QDesignerPropertyEditorInterface] """
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setActionEditor(self, actionEditor, QDesignerActionEditorInterface=None): # real signature unknown; restored from __doc__
        """ setActionEditor(self, actionEditor: Optional[QDesignerActionEditorInterface]) """
        pass

    def setObjectInspector(self, objectInspector, QDesignerObjectInspectorInterface=None): # real signature unknown; restored from __doc__
        """ setObjectInspector(self, objectInspector: Optional[QDesignerObjectInspectorInterface]) """
        pass

    def setPropertyEditor(self, propertyEditor, QDesignerPropertyEditorInterface=None): # real signature unknown; restored from __doc__
        """ setPropertyEditor(self, propertyEditor: Optional[QDesignerPropertyEditorInterface]) """
        pass

    def setWidgetBox(self, widgetBox, QDesignerWidgetBoxInterface=None): # real signature unknown; restored from __doc__
        """ setWidgetBox(self, widgetBox: Optional[QDesignerWidgetBoxInterface]) """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def topLevel(self): # real signature unknown; restored from __doc__
        """ topLevel(self) -> Optional[QWidget] """
        pass

    def widgetBox(self): # real signature unknown; restored from __doc__
        """ widgetBox(self) -> Optional[QDesignerWidgetBoxInterface] """
        pass

    def __init__(self, parent, QObject=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass


class QDesignerFormWindowCursorInterface(__sip.simplewrapper):
    """
    QDesignerFormWindowCursorInterface()
    QDesignerFormWindowCursorInterface(a0: QDesignerFormWindowCursorInterface)
    """
    def current(self): # real signature unknown; restored from __doc__
        """ current(self) -> Optional[QWidget] """
        pass

    def formWindow(self): # real signature unknown; restored from __doc__
        """ formWindow(self) -> Optional[QDesignerFormWindowInterface] """
        pass

    def hasSelection(self): # real signature unknown; restored from __doc__
        """ hasSelection(self) -> bool """
        return False

    def isWidgetSelected(self, widget, QWidget=None): # real signature unknown; restored from __doc__
        """ isWidgetSelected(self, widget: Optional[QWidget]) -> bool """
        return False

    def movePosition(self, op, mode=None): # real signature unknown; restored from __doc__
        """ movePosition(self, op: QDesignerFormWindowCursorInterface.MoveOperation, mode: QDesignerFormWindowCursorInterface.MoveMode = QDesignerFormWindowCursorInterface.MoveAnchor) -> bool """
        return False

    def position(self): # real signature unknown; restored from __doc__
        """ position(self) -> int """
        return 0

    def resetWidgetProperty(self, widget, QWidget=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ resetWidgetProperty(self, widget: Optional[QWidget], name: Optional[str]) """
        pass

    def selectedWidget(self, index): # real signature unknown; restored from __doc__
        """ selectedWidget(self, index: int) -> Optional[QWidget] """
        pass

    def selectedWidgetCount(self): # real signature unknown; restored from __doc__
        """ selectedWidgetCount(self) -> int """
        return 0

    def setPosition(self, pos, mode=None): # real signature unknown; restored from __doc__
        """ setPosition(self, pos: int, mode: QDesignerFormWindowCursorInterface.MoveMode = QDesignerFormWindowCursorInterface.MoveAnchor) """
        pass

    def setProperty(self, name, p_str=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ setProperty(self, name: Optional[str], value: Any) """
        pass

    def setWidgetProperty(self, widget, QWidget=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ setWidgetProperty(self, widget: Optional[QWidget], name: Optional[str], value: Any) """
        pass

    def widget(self, index): # real signature unknown; restored from __doc__
        """ widget(self, index: int) -> Optional[QWidget] """
        pass

    def widgetCount(self): # real signature unknown; restored from __doc__
        """ widgetCount(self) -> int """
        return 0

    def __init__(self, a0=None): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    Down = 8
    End = 2
    KeepAnchor = 1
    Left = 5
    MoveAnchor = 0
    Next = 3
    NoMove = 0
    Prev = 4
    Right = 6
    Start = 1
    Up = 7


class QDesignerFormWindowInterface(__PyQt5_QtWidgets.QWidget):
    # no doc
    def aboutToUnmanageWidget(self, *args, **kwargs): # real signature unknown
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

    def absoluteDir(self): # real signature unknown; restored from __doc__
        """ absoluteDir(self) -> QDir """
        pass

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

    def activateResourceFilePaths(self, paths, Optional=None, p_str=None): # real signature unknown; restored from __doc__
        """ activateResourceFilePaths(self, paths: Iterable[Optional[str]]) -> (Optional[int], Optional[str]) """
        pass

    def activeResourceFilePaths(self): # real signature unknown; restored from __doc__
        """ activeResourceFilePaths(self) -> List[str] """
        return []

    def addResourceFile(self, path, p_str=None): # real signature unknown; restored from __doc__
        """ addResourceFile(self, path: Optional[str]) """
        pass

    def author(self): # real signature unknown; restored from __doc__
        """ author(self) -> str """
        return ""

    def changed(self, *args, **kwargs): # real signature unknown
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

    def checkContents(self): # real signature unknown; restored from __doc__
        """ checkContents(self) -> List[str] """
        return []

    def clearSelection(self, update=True): # real signature unknown; restored from __doc__
        """ clearSelection(self, update: bool = True) """
        pass

    def comment(self): # real signature unknown; restored from __doc__
        """ comment(self) -> str """
        return ""

    def contents(self): # real signature unknown; restored from __doc__
        """ contents(self) -> str """
        return ""

    def core(self): # real signature unknown; restored from __doc__
        """ core(self) -> Optional[QDesignerFormEditorInterface] """
        pass

    def cursor(self): # real signature unknown; restored from __doc__
        """ cursor(self) -> Optional[QDesignerFormWindowCursorInterface] """
        pass

    def emitSelectionChanged(self): # real signature unknown; restored from __doc__
        """ emitSelectionChanged(self) """
        pass

    def exportMacro(self): # real signature unknown; restored from __doc__
        """ exportMacro(self) -> str """
        return ""

    def featureChanged(self, *args, **kwargs): # real signature unknown
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

    def features(self): # real signature unknown; restored from __doc__
        """ features(self) -> QDesignerFormWindowInterface.Feature """
        pass

    def fileName(self): # real signature unknown; restored from __doc__
        """ fileName(self) -> str """
        return ""

    def fileNameChanged(self, *args, **kwargs): # real signature unknown
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

    def findFormWindow(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        findFormWindow(w: Optional[QWidget]) -> Optional[QDesignerFormWindowInterface]
        findFormWindow(obj: Optional[QObject]) -> Optional[QDesignerFormWindowInterface]
        """
        pass

    def formContainer(self): # real signature unknown; restored from __doc__
        """ formContainer(self) -> Optional[QWidget] """
        pass

    def geometryChanged(self, *args, **kwargs): # real signature unknown
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

    def grid(self): # real signature unknown; restored from __doc__
        """ grid(self) -> QPoint """
        pass

    def hasFeature(self, f, QDesignerFormWindowInterface_Feature=None, QDesignerFormWindowInterface_FeatureFlag=None): # real signature unknown; restored from __doc__
        """ hasFeature(self, f: Union[QDesignerFormWindowInterface.Feature, QDesignerFormWindowInterface.FeatureFlag]) -> bool """
        return False

    def includeHints(self): # real signature unknown; restored from __doc__
        """ includeHints(self) -> List[str] """
        return []

    def isDirty(self): # real signature unknown; restored from __doc__
        """ isDirty(self) -> bool """
        return False

    def isManaged(self, widget, QWidget=None): # real signature unknown; restored from __doc__
        """ isManaged(self, widget: Optional[QWidget]) -> bool """
        return False

    def layoutDefault(self): # real signature unknown; restored from __doc__
        """ layoutDefault(self) -> (Optional[int], Optional[int]) """
        pass

    def layoutFunction(self): # real signature unknown; restored from __doc__
        """ layoutFunction(self) -> (Optional[str], Optional[str]) """
        pass

    def mainContainer(self): # real signature unknown; restored from __doc__
        """ mainContainer(self) -> Optional[QWidget] """
        pass

    def mainContainerChanged(self, *args, **kwargs): # real signature unknown
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

    def manageWidget(self, widget, QWidget=None): # real signature unknown; restored from __doc__
        """ manageWidget(self, widget: Optional[QWidget]) """
        pass

    def objectRemoved(self, *args, **kwargs): # real signature unknown
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

    def pixmapFunction(self): # real signature unknown; restored from __doc__
        """ pixmapFunction(self) -> str """
        return ""

    def removeResourceFile(self, path, p_str=None): # real signature unknown; restored from __doc__
        """ removeResourceFile(self, path: Optional[str]) """
        pass

    def resourceFiles(self): # real signature unknown; restored from __doc__
        """ resourceFiles(self) -> List[str] """
        return []

    def resourceFilesChanged(self, *args, **kwargs): # real signature unknown
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

    def selectWidget(self, widget, QWidget=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ selectWidget(self, widget: Optional[QWidget], select: bool = True) """
        pass

    def setAuthor(self, author, p_str=None): # real signature unknown; restored from __doc__
        """ setAuthor(self, author: Optional[str]) """
        pass

    def setComment(self, comment, p_str=None): # real signature unknown; restored from __doc__
        """ setComment(self, comment: Optional[str]) """
        pass

    def setContents(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setContents(self, dev: Optional[QIODevice], errorMessage: Optional[Optional[str]] = '') -> bool
        setContents(self, contents: Optional[str]) -> bool
        """
        return False

    def setDirty(self, dirty): # real signature unknown; restored from __doc__
        """ setDirty(self, dirty: bool) """
        pass

    def setExportMacro(self, exportMacro, p_str=None): # real signature unknown; restored from __doc__
        """ setExportMacro(self, exportMacro: Optional[str]) """
        pass

    def setFeatures(self, f, QDesignerFormWindowInterface_Feature=None, QDesignerFormWindowInterface_FeatureFlag=None): # real signature unknown; restored from __doc__
        """ setFeatures(self, f: Union[QDesignerFormWindowInterface.Feature, QDesignerFormWindowInterface.FeatureFlag]) """
        pass

    def setFileName(self, fileName, p_str=None): # real signature unknown; restored from __doc__
        """ setFileName(self, fileName: Optional[str]) """
        pass

    def setGrid(self, grid): # real signature unknown; restored from __doc__
        """ setGrid(self, grid: QPoint) """
        pass

    def setIncludeHints(self, includeHints, Optional=None, p_str=None): # real signature unknown; restored from __doc__
        """ setIncludeHints(self, includeHints: Iterable[Optional[str]]) """
        pass

    def setLayoutDefault(self, margin, spacing): # real signature unknown; restored from __doc__
        """ setLayoutDefault(self, margin: int, spacing: int) """
        pass

    def setLayoutFunction(self, margin, p_str=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ setLayoutFunction(self, margin: Optional[str], spacing: Optional[str]) """
        pass

    def setMainContainer(self, mainContainer, QWidget=None): # real signature unknown; restored from __doc__
        """ setMainContainer(self, mainContainer: Optional[QWidget]) """
        pass

    def setPixmapFunction(self, pixmapFunction, p_str=None): # real signature unknown; restored from __doc__
        """ setPixmapFunction(self, pixmapFunction: Optional[str]) """
        pass

    def unmanageWidget(self, widget, QWidget=None): # real signature unknown; restored from __doc__
        """ unmanageWidget(self, widget: Optional[QWidget]) """
        pass

    def widgetManaged(self, *args, **kwargs): # real signature unknown
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

    def widgetRemoved(self, *args, **kwargs): # real signature unknown
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

    def widgetUnmanaged(self, *args, **kwargs): # real signature unknown
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

    DefaultFeature = 3
    EditFeature = 1
    GridFeature = 2
    TabOrderFeature = 4


class QDesignerFormWindowManagerInterface(__PyQt5_QtCore.QObject):
    # no doc
    def action(self, action): # real signature unknown; restored from __doc__
        """ action(self, action: QDesignerFormWindowManagerInterface.Action) -> Optional[QAction] """
        pass

    def actionFormLayout(self): # real signature unknown; restored from __doc__
        """ actionFormLayout(self) -> Optional[QAction] """
        pass

    def actionGroup(self, actionGroup): # real signature unknown; restored from __doc__
        """ actionGroup(self, actionGroup: QDesignerFormWindowManagerInterface.ActionGroup) -> Optional[QActionGroup] """
        pass

    def actionSimplifyLayout(self): # real signature unknown; restored from __doc__
        """ actionSimplifyLayout(self) -> Optional[QAction] """
        pass

    def activeFormWindow(self): # real signature unknown; restored from __doc__
        """ activeFormWindow(self) -> Optional[QDesignerFormWindowInterface] """
        pass

    def activeFormWindowChanged(self, *args, **kwargs): # real signature unknown
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

    def addFormWindow(self, formWindow, QDesignerFormWindowInterface=None): # real signature unknown; restored from __doc__
        """ addFormWindow(self, formWindow: Optional[QDesignerFormWindowInterface]) """
        pass

    def closeAllPreviews(self): # real signature unknown; restored from __doc__
        """ closeAllPreviews(self) """
        pass

    def core(self): # real signature unknown; restored from __doc__
        """ core(self) -> Optional[QDesignerFormEditorInterface] """
        pass

    def createFormWindow(self, parent, QWidget=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ createFormWindow(self, parent: Optional[QWidget] = None, flags: Union[Qt.WindowFlags, Qt.WindowType] = 0) -> Optional[QDesignerFormWindowInterface] """
        pass

    def formWindow(self, index): # real signature unknown; restored from __doc__
        """ formWindow(self, index: int) -> Optional[QDesignerFormWindowInterface] """
        pass

    def formWindowAdded(self, *args, **kwargs): # real signature unknown
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

    def formWindowCount(self): # real signature unknown; restored from __doc__
        """ formWindowCount(self) -> int """
        return 0

    def formWindowRemoved(self, *args, **kwargs): # real signature unknown
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

    def formWindowSettingsChanged(self, *args, **kwargs): # real signature unknown
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

    def removeFormWindow(self, formWindow, QDesignerFormWindowInterface=None): # real signature unknown; restored from __doc__
        """ removeFormWindow(self, formWindow: Optional[QDesignerFormWindowInterface]) """
        pass

    def setActiveFormWindow(self, formWindow, QDesignerFormWindowInterface=None): # real signature unknown; restored from __doc__
        """ setActiveFormWindow(self, formWindow: Optional[QDesignerFormWindowInterface]) """
        pass

    def showPluginDialog(self): # real signature unknown; restored from __doc__
        """ showPluginDialog(self) """
        pass

    def showPreview(self): # real signature unknown; restored from __doc__
        """ showPreview(self) """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    AdjustSizeAction = 407
    BreakLayoutAction = 406
    CopyAction = 101
    CutAction = 100
    DefaultPreviewAction = 500
    DeleteAction = 103
    FormLayoutAction = 405
    FormWindowSettingsDialogAction = 600
    GridLayoutAction = 404
    HorizontalLayoutAction = 400
    LowerAction = 200
    PasteAction = 102
    RaiseAction = 201
    RedoAction = 301
    SelectAllAction = 104
    SimplifyLayoutAction = 408
    SplitHorizontalAction = 402
    SplitVerticalAction = 403
    StyledPreviewActionGroup = 100
    UndoAction = 300
    VerticalLayoutAction = 401


class QDesignerMemberSheetExtension(__sip.simplewrapper):
    """
    QDesignerMemberSheetExtension()
    QDesignerMemberSheetExtension(a0: QDesignerMemberSheetExtension)
    """
    def count(self): # real signature unknown; restored from __doc__
        """ count(self) -> int """
        return 0

    def declaredInClass(self, index): # real signature unknown; restored from __doc__
        """ declaredInClass(self, index: int) -> str """
        return ""

    def indexOf(self, name, p_str=None): # real signature unknown; restored from __doc__
        """ indexOf(self, name: Optional[str]) -> int """
        return 0

    def inheritedFromWidget(self, index): # real signature unknown; restored from __doc__
        """ inheritedFromWidget(self, index: int) -> bool """
        return False

    def isSignal(self, index): # real signature unknown; restored from __doc__
        """ isSignal(self, index: int) -> bool """
        return False

    def isSlot(self, index): # real signature unknown; restored from __doc__
        """ isSlot(self, index: int) -> bool """
        return False

    def isVisible(self, index): # real signature unknown; restored from __doc__
        """ isVisible(self, index: int) -> bool """
        return False

    def memberGroup(self, index): # real signature unknown; restored from __doc__
        """ memberGroup(self, index: int) -> str """
        return ""

    def memberName(self, index): # real signature unknown; restored from __doc__
        """ memberName(self, index: int) -> str """
        return ""

    def parameterNames(self, index): # real signature unknown; restored from __doc__
        """ parameterNames(self, index: int) -> List[QByteArray] """
        return []

    def parameterTypes(self, index): # real signature unknown; restored from __doc__
        """ parameterTypes(self, index: int) -> List[QByteArray] """
        return []

    def setMemberGroup(self, index, group, p_str=None): # real signature unknown; restored from __doc__
        """ setMemberGroup(self, index: int, group: Optional[str]) """
        pass

    def setVisible(self, index, b): # real signature unknown; restored from __doc__
        """ setVisible(self, index: int, b: bool) """
        pass

    def signature(self, index): # real signature unknown; restored from __doc__
        """ signature(self, index: int) -> str """
        return ""

    def __init__(self, a0=None): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    def __len__(self, *args, **kwargs): # real signature unknown
        """ Return len(self). """
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class QDesignerObjectInspectorInterface(__PyQt5_QtWidgets.QWidget):
    """ QDesignerObjectInspectorInterface(parent: Optional[QWidget], flags: Union[Qt.WindowFlags, Qt.WindowType] = 0) """
    def actionEvent(self, *args, **kwargs): # real signature unknown
        pass

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

    def core(self): # real signature unknown; restored from __doc__
        """ core(self) -> Optional[QDesignerFormEditorInterface] """
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

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def resizeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setFormWindow(self, formWindow, QDesignerFormWindowInterface=None): # real signature unknown; restored from __doc__
        """ setFormWindow(self, formWindow: Optional[QDesignerFormWindowInterface]) """
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


class QDesignerPropertyEditorInterface(__PyQt5_QtWidgets.QWidget):
    """ QDesignerPropertyEditorInterface(parent: Optional[QWidget], flags: Union[Qt.WindowFlags, Qt.WindowType] = 0) """
    def actionEvent(self, *args, **kwargs): # real signature unknown
        pass

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

    def core(self): # real signature unknown; restored from __doc__
        """ core(self) -> Optional[QDesignerFormEditorInterface] """
        pass

    def create(self, *args, **kwargs): # real signature unknown
        pass

    def currentPropertyName(self): # real signature unknown; restored from __doc__
        """ currentPropertyName(self) -> str """
        return ""

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

    def isReadOnly(self): # real signature unknown; restored from __doc__
        """ isReadOnly(self) -> bool """
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

    def object(self): # real signature unknown; restored from __doc__
        """ object(self) -> Optional[QObject] """
        pass

    def paintEvent(self, *args, **kwargs): # real signature unknown
        pass

    def propertyChanged(self, *args, **kwargs): # real signature unknown
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

    def resizeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setObject(self, p_object, QObject=None): # real signature unknown; restored from __doc__
        """ setObject(self, object: Optional[QObject]) """
        pass

    def setPropertyValue(self, name, p_str=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ setPropertyValue(self, name: Optional[str], value: Any, changed: bool = True) """
        pass

    def setReadOnly(self, readOnly): # real signature unknown; restored from __doc__
        """ setReadOnly(self, readOnly: bool) """
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


class QDesignerPropertySheetExtension(__sip.simplewrapper):
    """
    QDesignerPropertySheetExtension()
    QDesignerPropertySheetExtension(a0: QDesignerPropertySheetExtension)
    """
    def count(self): # real signature unknown; restored from __doc__
        """ count(self) -> int """
        return 0

    def hasReset(self, index): # real signature unknown; restored from __doc__
        """ hasReset(self, index: int) -> bool """
        return False

    def indexOf(self, name, p_str=None): # real signature unknown; restored from __doc__
        """ indexOf(self, name: Optional[str]) -> int """
        return 0

    def isAttribute(self, index): # real signature unknown; restored from __doc__
        """ isAttribute(self, index: int) -> bool """
        return False

    def isChanged(self, index): # real signature unknown; restored from __doc__
        """ isChanged(self, index: int) -> bool """
        return False

    def isEnabled(self, index): # real signature unknown; restored from __doc__
        """ isEnabled(self, index: int) -> bool """
        return False

    def isVisible(self, index): # real signature unknown; restored from __doc__
        """ isVisible(self, index: int) -> bool """
        return False

    def property(self, index): # real signature unknown; restored from __doc__
        """ property(self, index: int) -> Any """
        pass

    def propertyGroup(self, index): # real signature unknown; restored from __doc__
        """ propertyGroup(self, index: int) -> str """
        return ""

    def propertyName(self, index): # real signature unknown; restored from __doc__
        """ propertyName(self, index: int) -> str """
        return ""

    def reset(self, index): # real signature unknown; restored from __doc__
        """ reset(self, index: int) -> bool """
        return False

    def setAttribute(self, index, b): # real signature unknown; restored from __doc__
        """ setAttribute(self, index: int, b: bool) """
        pass

    def setChanged(self, index, changed): # real signature unknown; restored from __doc__
        """ setChanged(self, index: int, changed: bool) """
        pass

    def setProperty(self, index, value): # real signature unknown; restored from __doc__
        """ setProperty(self, index: int, value: Any) """
        pass

    def setPropertyGroup(self, index, group, p_str=None): # real signature unknown; restored from __doc__
        """ setPropertyGroup(self, index: int, group: Optional[str]) """
        pass

    def setVisible(self, index, b): # real signature unknown; restored from __doc__
        """ setVisible(self, index: int, b: bool) """
        pass

    def __init__(self, a0=None): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    def __len__(self, *args, **kwargs): # real signature unknown
        """ Return len(self). """
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class QDesignerTaskMenuExtension(__sip.simplewrapper):
    """
    QDesignerTaskMenuExtension()
    QDesignerTaskMenuExtension(a0: QDesignerTaskMenuExtension)
    """
    def preferredEditAction(self): # real signature unknown; restored from __doc__
        """ preferredEditAction(self) -> Optional[QAction] """
        pass

    def taskActions(self): # real signature unknown; restored from __doc__
        """ taskActions(self) -> List[QAction] """
        return []

    def __init__(self, a0=None): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class QDesignerWidgetBoxInterface(__PyQt5_QtWidgets.QWidget):
    # no doc
    def fileName(self): # real signature unknown; restored from __doc__
        """ fileName(self) -> str """
        return ""

    def load(self): # real signature unknown; restored from __doc__
        """ load(self) -> bool """
        return False

    def save(self): # real signature unknown; restored from __doc__
        """ save(self) -> bool """
        return False

    def setFileName(self, file_name, p_str=None): # real signature unknown; restored from __doc__
        """ setFileName(self, file_name: Optional[str]) """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class QExtensionFactory(__PyQt5_QtCore.QObject, QAbstractExtensionFactory):
    """ QExtensionFactory(parent: Optional[QExtensionManager] = None) """
    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def createExtension(self, p_object, QObject=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ createExtension(self, object: Optional[QObject], iid: Optional[str], parent: Optional[QObject]) -> Optional[QObject] """
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def extension(self, p_object, QObject=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ extension(self, object: Optional[QObject], iid: Optional[str]) -> Optional[QObject] """
        pass

    def extensionManager(self): # real signature unknown; restored from __doc__
        """ extensionManager(self) -> Optional[QExtensionManager] """
        pass

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, parent, QExtensionManager=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass


class QExtensionManager(__PyQt5_QtCore.QObject, QAbstractExtensionManager):
    """ QExtensionManager(parent: Optional[QObject] = None) """
    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def extension(self, p_object, QObject=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ extension(self, object: Optional[QObject], iid: Optional[str]) -> Optional[QObject] """
        pass

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def registerExtensions(self, factory, QAbstractExtensionFactory=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ registerExtensions(self, factory: Optional[QAbstractExtensionFactory], iid: Optional[str] = '') """
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def unregisterExtensions(self, factory, QAbstractExtensionFactory=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ unregisterExtensions(self, factory: Optional[QAbstractExtensionFactory], iid: Optional[str] = '') """
        pass

    def __init__(self, parent, QObject=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass


class QFormBuilder(QAbstractFormBuilder):
    """ QFormBuilder() """
    def addPluginPath(self, pluginPath, p_str=None): # real signature unknown; restored from __doc__
        """ addPluginPath(self, pluginPath: Optional[str]) """
        pass

    def clearPluginPaths(self): # real signature unknown; restored from __doc__
        """ clearPluginPaths(self) """
        pass

    def customWidgets(self): # real signature unknown; restored from __doc__
        """ customWidgets(self) -> List[QDesignerCustomWidgetInterface] """
        return []

    def pluginPaths(self): # real signature unknown; restored from __doc__
        """ pluginPaths(self) -> List[str] """
        return []

    def setPluginPath(self, pluginPaths, Optional=None, p_str=None): # real signature unknown; restored from __doc__
        """ setPluginPath(self, pluginPaths: Iterable[Optional[str]]) """
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        pass


class QPyDesignerContainerExtension(__PyQt5_QtCore.QObject, QDesignerContainerExtension):
    """ QPyDesignerContainerExtension(parent: Optional[QObject]) """
    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, parent, QObject=None): # real signature unknown; restored from __doc__
        pass


class QPyDesignerCustomWidgetCollectionPlugin(__PyQt5_QtCore.QObject, QDesignerCustomWidgetCollectionInterface):
    """ QPyDesignerCustomWidgetCollectionPlugin(parent: Optional[QObject] = None) """
    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, parent, QObject=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass


class QPyDesignerCustomWidgetPlugin(__PyQt5_QtCore.QObject, QDesignerCustomWidgetInterface):
    """ QPyDesignerCustomWidgetPlugin(parent: Optional[QObject] = None) """
    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, parent, QObject=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass


class QPyDesignerMemberSheetExtension(__PyQt5_QtCore.QObject, QDesignerMemberSheetExtension):
    """ QPyDesignerMemberSheetExtension(parent: Optional[QObject]) """
    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, parent, QObject=None): # real signature unknown; restored from __doc__
        pass


class QPyDesignerPropertySheetExtension(__PyQt5_QtCore.QObject, QDesignerPropertySheetExtension):
    """ QPyDesignerPropertySheetExtension(parent: Optional[QObject]) """
    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, parent, QObject=None): # real signature unknown; restored from __doc__
        pass


class QPyDesignerTaskMenuExtension(__PyQt5_QtCore.QObject, QDesignerTaskMenuExtension):
    """ QPyDesignerTaskMenuExtension(parent: Optional[QObject]) """
    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, parent, QObject=None): # real signature unknown; restored from __doc__
        pass


# variables with complex values



