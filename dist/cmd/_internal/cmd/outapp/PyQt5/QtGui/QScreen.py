# encoding: utf-8
# module PyQt5.QtGui
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtGui.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


class QScreen(__PyQt5_QtCore.QObject):
    # no doc
    def angleBetween(self, a, b): # real signature unknown; restored from __doc__
        """ angleBetween(self, a: Qt.ScreenOrientation, b: Qt.ScreenOrientation) -> int """
        return 0

    def availableGeometry(self): # real signature unknown; restored from __doc__
        """ availableGeometry(self) -> QRect """
        pass

    def availableGeometryChanged(self, *args, **kwargs): # real signature unknown
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

    def availableSize(self): # real signature unknown; restored from __doc__
        """ availableSize(self) -> QSize """
        pass

    def availableVirtualGeometry(self): # real signature unknown; restored from __doc__
        """ availableVirtualGeometry(self) -> QRect """
        pass

    def availableVirtualSize(self): # real signature unknown; restored from __doc__
        """ availableVirtualSize(self) -> QSize """
        pass

    def depth(self): # real signature unknown; restored from __doc__
        """ depth(self) -> int """
        return 0

    def devicePixelRatio(self): # real signature unknown; restored from __doc__
        """ devicePixelRatio(self) -> float """
        return 0.0

    def geometry(self): # real signature unknown; restored from __doc__
        """ geometry(self) -> QRect """
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

    def grabWindow(self, window, x=0, y=0, width=-1, height=-1): # real signature unknown; restored from __doc__
        """ grabWindow(self, window: PyQt5.sip.voidptr, x: int = 0, y: int = 0, width: int = -1, height: int = -1) -> QPixmap """
        return QPixmap

    def isLandscape(self, orientation): # real signature unknown; restored from __doc__
        """ isLandscape(self, orientation: Qt.ScreenOrientation) -> bool """
        return False

    def isPortrait(self, orientation): # real signature unknown; restored from __doc__
        """ isPortrait(self, orientation: Qt.ScreenOrientation) -> bool """
        return False

    def logicalDotsPerInch(self): # real signature unknown; restored from __doc__
        """ logicalDotsPerInch(self) -> float """
        return 0.0

    def logicalDotsPerInchChanged(self, *args, **kwargs): # real signature unknown
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

    def logicalDotsPerInchX(self): # real signature unknown; restored from __doc__
        """ logicalDotsPerInchX(self) -> float """
        return 0.0

    def logicalDotsPerInchY(self): # real signature unknown; restored from __doc__
        """ logicalDotsPerInchY(self) -> float """
        return 0.0

    def manufacturer(self): # real signature unknown; restored from __doc__
        """ manufacturer(self) -> str """
        return ""

    def mapBetween(self, a, b, rect): # real signature unknown; restored from __doc__
        """ mapBetween(self, a: Qt.ScreenOrientation, b: Qt.ScreenOrientation, rect: QRect) -> QRect """
        pass

    def model(self): # real signature unknown; restored from __doc__
        """ model(self) -> str """
        return ""

    def name(self): # real signature unknown; restored from __doc__
        """ name(self) -> str """
        return ""

    def nativeOrientation(self): # real signature unknown; restored from __doc__
        """ nativeOrientation(self) -> Qt.ScreenOrientation """
        pass

    def orientation(self): # real signature unknown; restored from __doc__
        """ orientation(self) -> Qt.ScreenOrientation """
        pass

    def orientationChanged(self, *args, **kwargs): # real signature unknown
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

    def orientationUpdateMask(self): # real signature unknown; restored from __doc__
        """ orientationUpdateMask(self) -> Qt.ScreenOrientations """
        pass

    def physicalDotsPerInch(self): # real signature unknown; restored from __doc__
        """ physicalDotsPerInch(self) -> float """
        return 0.0

    def physicalDotsPerInchChanged(self, *args, **kwargs): # real signature unknown
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

    def physicalDotsPerInchX(self): # real signature unknown; restored from __doc__
        """ physicalDotsPerInchX(self) -> float """
        return 0.0

    def physicalDotsPerInchY(self): # real signature unknown; restored from __doc__
        """ physicalDotsPerInchY(self) -> float """
        return 0.0

    def physicalSize(self): # real signature unknown; restored from __doc__
        """ physicalSize(self) -> QSizeF """
        pass

    def physicalSizeChanged(self, *args, **kwargs): # real signature unknown
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

    def primaryOrientation(self): # real signature unknown; restored from __doc__
        """ primaryOrientation(self) -> Qt.ScreenOrientation """
        pass

    def primaryOrientationChanged(self, *args, **kwargs): # real signature unknown
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

    def refreshRate(self): # real signature unknown; restored from __doc__
        """ refreshRate(self) -> float """
        return 0.0

    def refreshRateChanged(self, *args, **kwargs): # real signature unknown
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

    def serialNumber(self): # real signature unknown; restored from __doc__
        """ serialNumber(self) -> str """
        return ""

    def setOrientationUpdateMask(self, mask, Qt_ScreenOrientations=None, Qt_ScreenOrientation=None): # real signature unknown; restored from __doc__
        """ setOrientationUpdateMask(self, mask: Union[Qt.ScreenOrientations, Qt.ScreenOrientation]) """
        pass

    def size(self): # real signature unknown; restored from __doc__
        """ size(self) -> QSize """
        pass

    def transformBetween(self, a, b, target): # real signature unknown; restored from __doc__
        """ transformBetween(self, a: Qt.ScreenOrientation, b: Qt.ScreenOrientation, target: QRect) -> QTransform """
        return QTransform

    def virtualGeometry(self): # real signature unknown; restored from __doc__
        """ virtualGeometry(self) -> QRect """
        pass

    def virtualGeometryChanged(self, *args, **kwargs): # real signature unknown
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

    def virtualSiblingAt(self, point): # real signature unknown; restored from __doc__
        """ virtualSiblingAt(self, point: QPoint) -> Optional[QScreen] """
        pass

    def virtualSiblings(self): # real signature unknown; restored from __doc__
        """ virtualSiblings(self) -> List[QScreen] """
        return []

    def virtualSize(self): # real signature unknown; restored from __doc__
        """ virtualSize(self) -> QSize """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass


