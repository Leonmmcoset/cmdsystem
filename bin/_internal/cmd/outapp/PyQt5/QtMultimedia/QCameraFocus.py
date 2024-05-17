# encoding: utf-8
# module PyQt5.QtMultimedia
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtMultimedia.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


class QCameraFocus(__PyQt5_QtCore.QObject):
    # no doc
    def customFocusPoint(self): # real signature unknown; restored from __doc__
        """ customFocusPoint(self) -> QPointF """
        pass

    def digitalZoom(self): # real signature unknown; restored from __doc__
        """ digitalZoom(self) -> float """
        return 0.0

    def digitalZoomChanged(self, *args, **kwargs): # real signature unknown
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

    def focusMode(self): # real signature unknown; restored from __doc__
        """ focusMode(self) -> QCameraFocus.FocusModes """
        pass

    def focusPointMode(self): # real signature unknown; restored from __doc__
        """ focusPointMode(self) -> QCameraFocus.FocusPointMode """
        pass

    def focusZones(self): # real signature unknown; restored from __doc__
        """ focusZones(self) -> List[QCameraFocusZone] """
        return []

    def focusZonesChanged(self, *args, **kwargs): # real signature unknown
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

    def isAvailable(self): # real signature unknown; restored from __doc__
        """ isAvailable(self) -> bool """
        return False

    def isFocusModeSupported(self, mode, QCameraFocus_FocusModes=None, QCameraFocus_FocusMode=None): # real signature unknown; restored from __doc__
        """ isFocusModeSupported(self, mode: Union[QCameraFocus.FocusModes, QCameraFocus.FocusMode]) -> bool """
        return False

    def isFocusPointModeSupported(self, a0): # real signature unknown; restored from __doc__
        """ isFocusPointModeSupported(self, a0: QCameraFocus.FocusPointMode) -> bool """
        return False

    def maximumDigitalZoom(self): # real signature unknown; restored from __doc__
        """ maximumDigitalZoom(self) -> float """
        return 0.0

    def maximumDigitalZoomChanged(self, *args, **kwargs): # real signature unknown
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

    def maximumOpticalZoom(self): # real signature unknown; restored from __doc__
        """ maximumOpticalZoom(self) -> float """
        return 0.0

    def maximumOpticalZoomChanged(self, *args, **kwargs): # real signature unknown
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

    def opticalZoom(self): # real signature unknown; restored from __doc__
        """ opticalZoom(self) -> float """
        return 0.0

    def opticalZoomChanged(self, *args, **kwargs): # real signature unknown
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

    def setCustomFocusPoint(self, point, QPointF=None, QPoint=None): # real signature unknown; restored from __doc__
        """ setCustomFocusPoint(self, point: Union[QPointF, QPoint]) """
        pass

    def setFocusMode(self, mode, QCameraFocus_FocusModes=None, QCameraFocus_FocusMode=None): # real signature unknown; restored from __doc__
        """ setFocusMode(self, mode: Union[QCameraFocus.FocusModes, QCameraFocus.FocusMode]) """
        pass

    def setFocusPointMode(self, mode): # real signature unknown; restored from __doc__
        """ setFocusPointMode(self, mode: QCameraFocus.FocusPointMode) """
        pass

    def zoomTo(self, opticalZoom, digitalZoom): # real signature unknown; restored from __doc__
        """ zoomTo(self, opticalZoom: float, digitalZoom: float) """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    AutoFocus = 8
    ContinuousFocus = 16
    FocusPointAuto = 0
    FocusPointCenter = 1
    FocusPointCustom = 3
    FocusPointFaceDetection = 2
    HyperfocalFocus = 2
    InfinityFocus = 4
    MacroFocus = 32
    ManualFocus = 1


