# encoding: utf-8
# module PyQt5.QAxContainer
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QAxContainer.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import PyQt5.QtWidgets as __PyQt5_QtWidgets
import sip as __sip


# no functions
# classes

class QAxBase(__sip.simplewrapper):
    # no doc
    def asVariant(self): # real signature unknown; restored from __doc__
        """ asVariant(self) -> Any """
        pass

    def classContext(self): # real signature unknown; restored from __doc__
        """ classContext(self) -> int """
        return 0

    def clear(self): # real signature unknown; restored from __doc__
        """ clear(self) """
        pass

    def control(self): # real signature unknown; restored from __doc__
        """ control(self) -> str """
        return ""

    def disableClassInfo(self): # real signature unknown; restored from __doc__
        """ disableClassInfo(self) """
        pass

    def disableEventSink(self): # real signature unknown; restored from __doc__
        """ disableEventSink(self) """
        pass

    def disableMetaObject(self): # real signature unknown; restored from __doc__
        """ disableMetaObject(self) """
        pass

    def dynamicCall(self, a0, p_str=None, *args, **kwargs): # real signature unknown; restored from __doc__ with multiple overloads
        """
        dynamicCall(self, a0: Optional[str], a1: Iterable[Any]) -> Any
        dynamicCall(self, a0: Optional[str], value1: Any = None, value2: Any = None, value3: Any = None, value4: Any = None, value5: Any = None, value6: Any = None, value7: Any = None, value8: Any = None) -> Any
        """
        pass

    def generateDocumentation(self): # real signature unknown; restored from __doc__
        """ generateDocumentation(self) -> str """
        return ""

    def isNull(self): # real signature unknown; restored from __doc__
        """ isNull(self) -> bool """
        return False

    def propertyBag(self): # real signature unknown; restored from __doc__
        """ propertyBag(self) -> Dict[str, Any] """
        return {}

    def propertyWritable(self, a0, p_str=None): # real signature unknown; restored from __doc__
        """ propertyWritable(self, a0: Optional[str]) -> bool """
        return False

    def querySubObject(self, a0, p_str=None, *args, **kwargs): # real signature unknown; restored from __doc__ with multiple overloads
        """
        querySubObject(self, a0: Optional[str], a1: Iterable[Any]) -> Optional[QAxObject]
        querySubObject(self, a0: Optional[str], value1: Any = None, value2: Any = None, value3: Any = None, value4: Any = None, value5: Any = None, value6: Any = None, value7: Any = None, value8: Any = None) -> Optional[QAxObject]
        """
        pass

    def setClassContext(self, classContext): # real signature unknown; restored from __doc__
        """ setClassContext(self, classContext: int) """
        pass

    def setControl(self, a0, p_str=None): # real signature unknown; restored from __doc__
        """ setControl(self, a0: Optional[str]) -> bool """
        return False

    def setPropertyBag(self, a0, p_str=None, Any=None): # real signature unknown; restored from __doc__
        """ setPropertyBag(self, a0: Dict[str, Any]) """
        pass

    def setPropertyWritable(self, a0, p_str=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ setPropertyWritable(self, a0: Optional[str], a1: bool) """
        pass

    def verbs(self): # real signature unknown; restored from __doc__
        """ verbs(self) -> List[str] """
        return []

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class QAxObject(__PyQt5_QtCore.QObject, QAxBase):
    """
    QAxObject(parent: Optional[QObject] = None)
    QAxObject(a0: Optional[str], parent: Optional[QObject] = None)
    """
    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, a0): # real signature unknown; restored from __doc__
        """ connectNotify(self, a0: QMetaMethod) """
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def doVerb(self, a0, p_str=None): # real signature unknown; restored from __doc__
        """ doVerb(self, a0: Optional[str]) -> bool """
        return False

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

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass


class QAxWidget(__PyQt5_QtWidgets.QWidget, QAxBase):
    """
    QAxWidget(parent: Optional[QWidget] = None, flags: Union[Qt.WindowFlags, Qt.WindowType] = 0)
    QAxWidget(a0: Optional[str], parent: Optional[QWidget] = None, flags: Union[Qt.WindowFlags, Qt.WindowType] = 0)
    """
    def actionEvent(self, *args, **kwargs): # real signature unknown
        pass

    def changeEvent(self, a0, QEvent=None): # real signature unknown; restored from __doc__
        """ changeEvent(self, a0: Optional[QEvent]) """
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def clear(self): # real signature unknown; restored from __doc__
        """ clear(self) """
        pass

    def closeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, a0): # real signature unknown; restored from __doc__
        """ connectNotify(self, a0: QMetaMethod) """
        pass

    def contextMenuEvent(self, *args, **kwargs): # real signature unknown
        pass

    def create(self, *args, **kwargs): # real signature unknown
        pass

    def createHostWindow(self, a0): # real signature unknown; restored from __doc__
        """ createHostWindow(self, a0: bool) -> bool """
        return False

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def destroy(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def doVerb(self, a0, p_str=None): # real signature unknown; restored from __doc__
        """ doVerb(self, a0: Optional[str]) -> bool """
        return False

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

    def minimumSizeHint(self): # real signature unknown; restored from __doc__
        """ minimumSizeHint(self) -> QSize """
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

    def resizeEvent(self, a0, QResizeEvent=None): # real signature unknown; restored from __doc__
        """ resizeEvent(self, a0: Optional[QResizeEvent]) """
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def sharedPainter(self, *args, **kwargs): # real signature unknown
        pass

    def showEvent(self, *args, **kwargs): # real signature unknown
        pass

    def sizeHint(self): # real signature unknown; restored from __doc__
        """ sizeHint(self) -> QSize """
        pass

    def tabletEvent(self, *args, **kwargs): # real signature unknown
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def translateKeyEvent(self, a0, a1): # real signature unknown; restored from __doc__
        """ translateKeyEvent(self, a0: int, a1: int) -> bool """
        return False

    def updateMicroFocus(self, *args, **kwargs): # real signature unknown
        pass

    def wheelEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass


# variables with complex values



