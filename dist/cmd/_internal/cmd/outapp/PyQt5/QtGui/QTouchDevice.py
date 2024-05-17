# encoding: utf-8
# module PyQt5.QtGui
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtGui.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


class QTouchDevice(__sip.simplewrapper):
    """
    QTouchDevice()
    QTouchDevice(a0: QTouchDevice)
    """
    def capabilities(self): # real signature unknown; restored from __doc__
        """ capabilities(self) -> QTouchDevice.Capabilities """
        pass

    def devices(self): # real signature unknown; restored from __doc__
        """ devices() -> List[QTouchDevice] """
        return []

    def maximumTouchPoints(self): # real signature unknown; restored from __doc__
        """ maximumTouchPoints(self) -> int """
        return 0

    def name(self): # real signature unknown; restored from __doc__
        """ name(self) -> str """
        return ""

    def setCapabilities(self, caps, QTouchDevice_Capabilities=None, QTouchDevice_CapabilityFlag=None): # real signature unknown; restored from __doc__
        """ setCapabilities(self, caps: Union[QTouchDevice.Capabilities, QTouchDevice.CapabilityFlag]) """
        pass

    def setMaximumTouchPoints(self, max): # real signature unknown; restored from __doc__
        """ setMaximumTouchPoints(self, max: int) """
        pass

    def setName(self, name, p_str=None): # real signature unknown; restored from __doc__
        """ setName(self, name: Optional[str]) """
        pass

    def setType(self, devType): # real signature unknown; restored from __doc__
        """ setType(self, devType: QTouchDevice.DeviceType) """
        pass

    def type(self): # real signature unknown; restored from __doc__
        """ type(self) -> QTouchDevice.DeviceType """
        pass

    def __init__(self, a0=None): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    Area = 2
    MouseEmulation = 64
    NormalizedPosition = 32
    Position = 1
    Pressure = 4
    RawPositions = 16
    TouchPad = 1
    TouchScreen = 0
    Velocity = 8


