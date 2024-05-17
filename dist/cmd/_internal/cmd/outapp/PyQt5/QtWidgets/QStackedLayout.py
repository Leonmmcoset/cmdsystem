# encoding: utf-8
# module PyQt5.QtWidgets
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtWidgets.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import PyQt5.QtGui as __PyQt5_QtGui
import sip as __sip


from .QLayout import QLayout

class QStackedLayout(QLayout):
    """
    QStackedLayout()
    QStackedLayout(parent: Optional[QWidget])
    QStackedLayout(parentLayout: Optional[QLayout])
    """
    def addChildLayout(self, *args, **kwargs): # real signature unknown
        pass

    def addChildWidget(self, *args, **kwargs): # real signature unknown
        pass

    def addItem(self, item, QLayoutItem=None): # real signature unknown; restored from __doc__
        """ addItem(self, item: Optional[QLayoutItem]) """
        pass

    def addWidget(self, w, QWidget=None): # real signature unknown; restored from __doc__
        """ addWidget(self, w: Optional[QWidget]) -> int """
        return 0

    def alignmentRect(self, *args, **kwargs): # real signature unknown
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def count(self): # real signature unknown; restored from __doc__
        """ count(self) -> int """
        return 0

    def currentChanged(self, *args, **kwargs): # real signature unknown
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

    def currentIndex(self): # real signature unknown; restored from __doc__
        """ currentIndex(self) -> int """
        return 0

    def currentWidget(self): # real signature unknown; restored from __doc__
        """ currentWidget(self) -> Optional[QWidget] """
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def hasHeightForWidth(self): # real signature unknown; restored from __doc__
        """ hasHeightForWidth(self) -> bool """
        return False

    def heightForWidth(self, width): # real signature unknown; restored from __doc__
        """ heightForWidth(self, width: int) -> int """
        return 0

    def insertWidget(self, index, w, QWidget=None): # real signature unknown; restored from __doc__
        """ insertWidget(self, index: int, w: Optional[QWidget]) -> int """
        return 0

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def itemAt(self, a0): # real signature unknown; restored from __doc__
        """ itemAt(self, a0: int) -> Optional[QLayoutItem] """
        pass

    def minimumSize(self): # real signature unknown; restored from __doc__
        """ minimumSize(self) -> QSize """
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setCurrentIndex(self, index): # real signature unknown; restored from __doc__
        """ setCurrentIndex(self, index: int) """
        pass

    def setCurrentWidget(self, w, QWidget=None): # real signature unknown; restored from __doc__
        """ setCurrentWidget(self, w: Optional[QWidget]) """
        pass

    def setGeometry(self, rect): # real signature unknown; restored from __doc__
        """ setGeometry(self, rect: QRect) """
        pass

    def setStackingMode(self, stackingMode): # real signature unknown; restored from __doc__
        """ setStackingMode(self, stackingMode: QStackedLayout.StackingMode) """
        pass

    def sizeHint(self): # real signature unknown; restored from __doc__
        """ sizeHint(self) -> QSize """
        pass

    def stackingMode(self): # real signature unknown; restored from __doc__
        """ stackingMode(self) -> QStackedLayout.StackingMode """
        pass

    def takeAt(self, a0): # real signature unknown; restored from __doc__
        """ takeAt(self, a0: int) -> Optional[QLayoutItem] """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def widget(self, a0=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        widget(self, a0: int) -> Optional[QWidget]
        widget(self) -> Optional[QWidget]
        """
        pass

    def widgetEvent(self, *args, **kwargs): # real signature unknown
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

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    StackAll = 1
    StackOne = 0


