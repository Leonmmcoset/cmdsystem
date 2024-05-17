# encoding: utf-8
# module PyQt5.QtGui
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtGui.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


class QPictureIO(__sip.simplewrapper):
    """
    QPictureIO()
    QPictureIO(ioDevice: Optional[QIODevice], format: Optional[str])
    QPictureIO(fileName: Optional[str], format: Optional[str])
    """
    def defineIOHandler(self, format, p_str=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ defineIOHandler(format: Optional[str], header: Optional[str], flags: Optional[str], read_picture: Optional[Callable[[QPictureIO], None]], write_picture: Optional[Callable[[QPictureIO], None]]) """
        pass

    def description(self): # real signature unknown; restored from __doc__
        """ description(self) -> str """
        return ""

    def fileName(self): # real signature unknown; restored from __doc__
        """ fileName(self) -> str """
        return ""

    def format(self): # real signature unknown; restored from __doc__
        """ format(self) -> Optional[str] """
        pass

    def gamma(self): # real signature unknown; restored from __doc__
        """ gamma(self) -> float """
        return 0.0

    def inputFormats(self): # real signature unknown; restored from __doc__
        """ inputFormats() -> List[QByteArray] """
        return []

    def ioDevice(self): # real signature unknown; restored from __doc__
        """ ioDevice(self) -> Optional[QIODevice] """
        pass

    def outputFormats(self): # real signature unknown; restored from __doc__
        """ outputFormats() -> List[QByteArray] """
        return []

    def parameters(self): # real signature unknown; restored from __doc__
        """ parameters(self) -> Optional[str] """
        pass

    def picture(self): # real signature unknown; restored from __doc__
        """ picture(self) -> QPicture """
        return QPicture

    def pictureFormat(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        pictureFormat(fileName: Optional[str]) -> QByteArray
        pictureFormat(a0: Optional[QIODevice]) -> QByteArray
        """
        pass

    def quality(self): # real signature unknown; restored from __doc__
        """ quality(self) -> int """
        return 0

    def read(self): # real signature unknown; restored from __doc__
        """ read(self) -> bool """
        return False

    def setDescription(self, a0, p_str=None): # real signature unknown; restored from __doc__
        """ setDescription(self, a0: Optional[str]) """
        pass

    def setFileName(self, a0, p_str=None): # real signature unknown; restored from __doc__
        """ setFileName(self, a0: Optional[str]) """
        pass

    def setFormat(self, a0, p_str=None): # real signature unknown; restored from __doc__
        """ setFormat(self, a0: Optional[str]) """
        pass

    def setGamma(self, a0): # real signature unknown; restored from __doc__
        """ setGamma(self, a0: float) """
        pass

    def setIODevice(self, a0, QIODevice=None): # real signature unknown; restored from __doc__
        """ setIODevice(self, a0: Optional[QIODevice]) """
        pass

    def setParameters(self, a0, p_str=None): # real signature unknown; restored from __doc__
        """ setParameters(self, a0: Optional[str]) """
        pass

    def setPicture(self, a0): # real signature unknown; restored from __doc__
        """ setPicture(self, a0: QPicture) """
        pass

    def setQuality(self, a0): # real signature unknown; restored from __doc__
        """ setQuality(self, a0: int) """
        pass

    def setStatus(self, a0): # real signature unknown; restored from __doc__
        """ setStatus(self, a0: int) """
        pass

    def status(self): # real signature unknown; restored from __doc__
        """ status(self) -> int """
        return 0

    def write(self): # real signature unknown; restored from __doc__
        """ write(self) -> bool """
        return False

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



