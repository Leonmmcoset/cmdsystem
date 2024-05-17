# encoding: utf-8
# module PyQt5.QtGui
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtGui.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


class QColorSpace(__sip.simplewrapper):
    """
    QColorSpace()
    QColorSpace(namedColorSpace: QColorSpace.NamedColorSpace)
    QColorSpace(primaries: QColorSpace.Primaries, fun: QColorSpace.TransferFunction, gamma: float = 0)
    QColorSpace(primaries: QColorSpace.Primaries, gamma: float)
    QColorSpace(whitePoint: Union[QPointF, QPoint], redPoint: Union[QPointF, QPoint], greenPoint: Union[QPointF, QPoint], bluePoint: Union[QPointF, QPoint], fun: QColorSpace.TransferFunction, gamma: float = 0)
    QColorSpace(colorSpace: QColorSpace)
    """
    def fromIccProfile(self, iccProfile, QByteArray=None, bytes=None, bytearray=None): # real signature unknown; restored from __doc__
        """ fromIccProfile(iccProfile: Union[QByteArray, bytes, bytearray]) -> QColorSpace """
        return QColorSpace

    def gamma(self): # real signature unknown; restored from __doc__
        """ gamma(self) -> float """
        return 0.0

    def iccProfile(self): # real signature unknown; restored from __doc__
        """ iccProfile(self) -> QByteArray """
        pass

    def isValid(self): # real signature unknown; restored from __doc__
        """ isValid(self) -> bool """
        return False

    def primaries(self): # real signature unknown; restored from __doc__
        """ primaries(self) -> QColorSpace.Primaries """
        pass

    def setPrimaries(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setPrimaries(self, primariesId: QColorSpace.Primaries)
        setPrimaries(self, whitePoint: Union[QPointF, QPoint], redPoint: Union[QPointF, QPoint], greenPoint: Union[QPointF, QPoint], bluePoint: Union[QPointF, QPoint])
        """
        pass

    def setTransferFunction(self, transferFunction, gamma=0): # real signature unknown; restored from __doc__
        """ setTransferFunction(self, transferFunction: QColorSpace.TransferFunction, gamma: float = 0) """
        pass

    def swap(self, colorSpace): # real signature unknown; restored from __doc__
        """ swap(self, colorSpace: QColorSpace) """
        pass

    def transferFunction(self): # real signature unknown; restored from __doc__
        """ transferFunction(self) -> QColorSpace.TransferFunction """
        pass

    def transformationToColorSpace(self, colorspace): # real signature unknown; restored from __doc__
        """ transformationToColorSpace(self, colorspace: QColorSpace) -> QColorTransform """
        return QColorTransform

    def withTransferFunction(self, transferFunction, gamma=0): # real signature unknown; restored from __doc__
        """ withTransferFunction(self, transferFunction: QColorSpace.TransferFunction, gamma: float = 0) -> QColorSpace """
        return QColorSpace

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
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


    AdobeRgb = 3
    DisplayP3 = 4
    ProPhotoRgb = 5
    SRgb = 1
    SRgbLinear = 2
    __hash__ = None


