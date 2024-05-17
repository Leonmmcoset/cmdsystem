# encoding: utf-8
# module PyQt5.QtMultimedia
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtMultimedia.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


class QCameraImageProcessing(__PyQt5_QtCore.QObject):
    # no doc
    def brightness(self): # real signature unknown; restored from __doc__
        """ brightness(self) -> float """
        return 0.0

    def colorFilter(self): # real signature unknown; restored from __doc__
        """ colorFilter(self) -> QCameraImageProcessing.ColorFilter """
        pass

    def contrast(self): # real signature unknown; restored from __doc__
        """ contrast(self) -> float """
        return 0.0

    def denoisingLevel(self): # real signature unknown; restored from __doc__
        """ denoisingLevel(self) -> float """
        return 0.0

    def isAvailable(self): # real signature unknown; restored from __doc__
        """ isAvailable(self) -> bool """
        return False

    def isColorFilterSupported(self, filter): # real signature unknown; restored from __doc__
        """ isColorFilterSupported(self, filter: QCameraImageProcessing.ColorFilter) -> bool """
        return False

    def isWhiteBalanceModeSupported(self, mode): # real signature unknown; restored from __doc__
        """ isWhiteBalanceModeSupported(self, mode: QCameraImageProcessing.WhiteBalanceMode) -> bool """
        return False

    def manualWhiteBalance(self): # real signature unknown; restored from __doc__
        """ manualWhiteBalance(self) -> float """
        return 0.0

    def saturation(self): # real signature unknown; restored from __doc__
        """ saturation(self) -> float """
        return 0.0

    def setBrightness(self, value): # real signature unknown; restored from __doc__
        """ setBrightness(self, value: float) """
        pass

    def setColorFilter(self, filter): # real signature unknown; restored from __doc__
        """ setColorFilter(self, filter: QCameraImageProcessing.ColorFilter) """
        pass

    def setContrast(self, value): # real signature unknown; restored from __doc__
        """ setContrast(self, value: float) """
        pass

    def setDenoisingLevel(self, value): # real signature unknown; restored from __doc__
        """ setDenoisingLevel(self, value: float) """
        pass

    def setManualWhiteBalance(self, colorTemperature): # real signature unknown; restored from __doc__
        """ setManualWhiteBalance(self, colorTemperature: float) """
        pass

    def setSaturation(self, value): # real signature unknown; restored from __doc__
        """ setSaturation(self, value: float) """
        pass

    def setSharpeningLevel(self, value): # real signature unknown; restored from __doc__
        """ setSharpeningLevel(self, value: float) """
        pass

    def setWhiteBalanceMode(self, mode): # real signature unknown; restored from __doc__
        """ setWhiteBalanceMode(self, mode: QCameraImageProcessing.WhiteBalanceMode) """
        pass

    def sharpeningLevel(self): # real signature unknown; restored from __doc__
        """ sharpeningLevel(self) -> float """
        return 0.0

    def whiteBalanceMode(self): # real signature unknown; restored from __doc__
        """ whiteBalanceMode(self) -> QCameraImageProcessing.WhiteBalanceMode """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    ColorFilterAqua = 8
    ColorFilterBlackboard = 7
    ColorFilterGrayscale = 1
    ColorFilterNegative = 2
    ColorFilterNone = 0
    ColorFilterPosterize = 5
    ColorFilterSepia = 4
    ColorFilterSolarize = 3
    ColorFilterVendor = 1000
    ColorFilterWhiteboard = 6
    WhiteBalanceAuto = 0
    WhiteBalanceCloudy = 3
    WhiteBalanceFlash = 7
    WhiteBalanceFluorescent = 6
    WhiteBalanceManual = 1
    WhiteBalanceShade = 4
    WhiteBalanceSunlight = 2
    WhiteBalanceSunset = 8
    WhiteBalanceTungsten = 5
    WhiteBalanceVendor = 1000


