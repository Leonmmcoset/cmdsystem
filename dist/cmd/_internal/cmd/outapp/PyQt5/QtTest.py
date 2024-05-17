# encoding: utf-8
# module PyQt5.QtTest
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtTest.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


# no functions
# classes

class QAbstractItemModelTester(__PyQt5_QtCore.QObject):
    """
    QAbstractItemModelTester(model: Optional[QAbstractItemModel], parent: Optional[QObject] = None)
    QAbstractItemModelTester(model: Optional[QAbstractItemModel], mode: QAbstractItemModelTester.FailureReportingMode, parent: Optional[QObject] = None)
    """
    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def failureReportingMode(self): # real signature unknown; restored from __doc__
        """ failureReportingMode(self) -> QAbstractItemModelTester.FailureReportingMode """
        pass

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def model(self): # real signature unknown; restored from __doc__
        """ model(self) -> Optional[QAbstractItemModel] """
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, model, QAbstractItemModel=None, *args, **kwargs): # real signature unknown; restored from __doc__ with multiple overloads
        pass



class QSignalSpy(__PyQt5_QtCore.QObject):
    """
    QSignalSpy(signal: pyqtBoundSignal)
    QSignalSpy(obj: Optional[QObject], signal: QMetaMethod)
    """
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

    def isValid(self): # real signature unknown; restored from __doc__
        """ isValid(self) -> bool """
        return False

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def signal(self): # real signature unknown; restored from __doc__
        """ signal(self) -> QByteArray """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def wait(self, timeout=5000): # real signature unknown; restored from __doc__
        """ wait(self, timeout: int = 5000) -> bool """
        return False

    def __delitem__(self, *args, **kwargs): # real signature unknown
        """ Delete self[key]. """
        pass

    def __getitem__(self, *args, **kwargs): # real signature unknown
        """ Return self[key]. """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    def __len__(self, *args, **kwargs): # real signature unknown
        """ Return len(self). """
        pass

    def __setitem__(self, *args, **kwargs): # real signature unknown
        """ Set self[key] to value. """
        pass


class QTest(__sip.simplewrapper):
    # no doc
    def keyClick(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        keyClick(widget: Optional[QWidget], key: Qt.Key, modifier: Union[Qt.KeyboardModifiers, Qt.KeyboardModifier] = Qt.NoModifier, delay: int = -1)
        keyClick(widget: Optional[QWidget], key: str, modifier: Union[Qt.KeyboardModifiers, Qt.KeyboardModifier] = Qt.NoModifier, delay: int = -1)
        keyClick(window: Optional[QWindow], key: Qt.Key, modifier: Union[Qt.KeyboardModifiers, Qt.KeyboardModifier] = Qt.NoModifier, delay: int = -1)
        keyClick(window: Optional[QWindow], key: str, modifier: Union[Qt.KeyboardModifiers, Qt.KeyboardModifier] = Qt.NoModifier, delay: int = -1)
        """
        pass

    def keyClicks(self, widget, QWidget=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ keyClicks(widget: Optional[QWidget], sequence: Optional[str], modifier: Union[Qt.KeyboardModifiers, Qt.KeyboardModifier] = Qt.NoModifier, delay: int = -1) """
        pass

    def keyEvent(self, action, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        keyEvent(action: QTest.KeyAction, widget: Optional[QWidget], key: Qt.Key, modifier: Union[Qt.KeyboardModifiers, Qt.KeyboardModifier] = Qt.NoModifier, delay: int = -1)
        keyEvent(action: QTest.KeyAction, widget: Optional[QWidget], ascii: str, modifier: Union[Qt.KeyboardModifiers, Qt.KeyboardModifier] = Qt.NoModifier, delay: int = -1)
        keyEvent(action: QTest.KeyAction, window: Optional[QWindow], key: Qt.Key, modifier: Union[Qt.KeyboardModifiers, Qt.KeyboardModifier] = Qt.NoModifier, delay: int = -1)
        keyEvent(action: QTest.KeyAction, window: Optional[QWindow], ascii: str, modifier: Union[Qt.KeyboardModifiers, Qt.KeyboardModifier] = Qt.NoModifier, delay: int = -1)
        """
        pass

    def keyPress(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        keyPress(widget: Optional[QWidget], key: Qt.Key, modifier: Union[Qt.KeyboardModifiers, Qt.KeyboardModifier] = Qt.NoModifier, delay: int = -1)
        keyPress(widget: Optional[QWidget], key: str, modifier: Union[Qt.KeyboardModifiers, Qt.KeyboardModifier] = Qt.NoModifier, delay: int = -1)
        keyPress(window: Optional[QWindow], key: Qt.Key, modifier: Union[Qt.KeyboardModifiers, Qt.KeyboardModifier] = Qt.NoModifier, delay: int = -1)
        keyPress(window: Optional[QWindow], key: str, modifier: Union[Qt.KeyboardModifiers, Qt.KeyboardModifier] = Qt.NoModifier, delay: int = -1)
        """
        pass

    def keyRelease(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        keyRelease(widget: Optional[QWidget], key: Qt.Key, modifier: Union[Qt.KeyboardModifiers, Qt.KeyboardModifier] = Qt.NoModifier, delay: int = -1)
        keyRelease(widget: Optional[QWidget], key: str, modifier: Union[Qt.KeyboardModifiers, Qt.KeyboardModifier] = Qt.NoModifier, delay: int = -1)
        keyRelease(window: Optional[QWindow], key: Qt.Key, modifier: Union[Qt.KeyboardModifiers, Qt.KeyboardModifier] = Qt.NoModifier, delay: int = -1)
        keyRelease(window: Optional[QWindow], key: str, modifier: Union[Qt.KeyboardModifiers, Qt.KeyboardModifier] = Qt.NoModifier, delay: int = -1)
        """
        pass

    def keySequence(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        keySequence(widget: Optional[QWidget], keySequence: Union[QKeySequence, QKeySequence.StandardKey, Optional[str], int])
        keySequence(window: Optional[QWindow], keySequence: Union[QKeySequence, QKeySequence.StandardKey, Optional[str], int])
        """
        pass

    def mouseClick(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        mouseClick(widget: Optional[QWidget], button: Qt.MouseButton, modifier: Union[Qt.KeyboardModifiers, Qt.KeyboardModifier] = Qt.KeyboardModifiers(), pos: QPoint = QPoint(), delay: int = -1)
        mouseClick(window: Optional[QWindow], button: Qt.MouseButton, modifier: Union[Qt.KeyboardModifiers, Qt.KeyboardModifier] = Qt.KeyboardModifiers(), pos: QPoint = QPoint(), delay: int = -1)
        """
        pass

    def mouseDClick(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        mouseDClick(widget: Optional[QWidget], button: Qt.MouseButton, modifier: Union[Qt.KeyboardModifiers, Qt.KeyboardModifier] = Qt.KeyboardModifiers(), pos: QPoint = QPoint(), delay: int = -1)
        mouseDClick(window: Optional[QWindow], button: Qt.MouseButton, modifier: Union[Qt.KeyboardModifiers, Qt.KeyboardModifier] = Qt.KeyboardModifiers(), pos: QPoint = QPoint(), delay: int = -1)
        """
        pass

    def mouseMove(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        mouseMove(widget: Optional[QWidget], pos: QPoint = QPoint(), delay: int = -1)
        mouseMove(window: Optional[QWindow], pos: QPoint = QPoint(), delay: int = -1)
        """
        pass

    def mousePress(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        mousePress(widget: Optional[QWidget], button: Qt.MouseButton, modifier: Union[Qt.KeyboardModifiers, Qt.KeyboardModifier] = Qt.KeyboardModifiers(), pos: QPoint = QPoint(), delay: int = -1)
        mousePress(window: Optional[QWindow], button: Qt.MouseButton, modifier: Union[Qt.KeyboardModifiers, Qt.KeyboardModifier] = Qt.KeyboardModifiers(), pos: QPoint = QPoint(), delay: int = -1)
        """
        pass

    def mouseRelease(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        mouseRelease(widget: Optional[QWidget], button: Qt.MouseButton, modifier: Union[Qt.KeyboardModifiers, Qt.KeyboardModifier] = Qt.KeyboardModifiers(), pos: QPoint = QPoint(), delay: int = -1)
        mouseRelease(window: Optional[QWindow], button: Qt.MouseButton, modifier: Union[Qt.KeyboardModifiers, Qt.KeyboardModifier] = Qt.KeyboardModifiers(), pos: QPoint = QPoint(), delay: int = -1)
        """
        pass

    def qSleep(self, ms): # real signature unknown; restored from __doc__
        """ qSleep(ms: int) """
        pass

    def qWait(self, ms): # real signature unknown; restored from __doc__
        """ qWait(ms: int) """
        pass

    def qWaitForWindowActive(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        qWaitForWindowActive(window: Optional[QWindow], timeout: int = 5000) -> bool
        qWaitForWindowActive(widget: Optional[QWidget], timeout: int = 5000) -> bool
        """
        pass

    def qWaitForWindowExposed(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        qWaitForWindowExposed(window: Optional[QWindow], timeout: int = 5000) -> bool
        qWaitForWindowExposed(widget: Optional[QWidget], timeout: int = 5000) -> bool
        """
        pass

    def touchEvent(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        touchEvent(widget: Optional[QWidget], device: Optional[QTouchDevice]) -> QTest.QTouchEventSequence
        touchEvent(window: Optional[QWindow], device: Optional[QTouchDevice]) -> QTest.QTouchEventSequence
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    Click = 2
    Press = 0
    Release = 1
    Shortcut = 3


# variables with complex values



