# encoding: utf-8
# module PyQt5.QtGui
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtGui.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


class QDesktopServices(__sip.simplewrapper):
    """
    QDesktopServices()
    QDesktopServices(a0: QDesktopServices)
    """
    def openUrl(self, url): # real signature unknown; restored from __doc__
        """ openUrl(url: QUrl) -> bool """
        return False

    def setUrlHandler(self, scheme, p_str=None, *args, **kwargs): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setUrlHandler(scheme: Optional[str], receiver: Optional[QObject], method: Optional[str])
        setUrlHandler(scheme: Optional[str], method: Callable[[QUrl], None])
        """
        pass

    def unsetUrlHandler(self, scheme, p_str=None): # real signature unknown; restored from __doc__
        """ unsetUrlHandler(scheme: Optional[str]) """
        pass

    def __init__(self, a0=None): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



