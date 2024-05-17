# encoding: utf-8
# module PyQt5.QtWidgets
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtWidgets.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import PyQt5.QtGui as __PyQt5_QtGui
import sip as __sip


from .QAction import QAction

class QWidgetAction(QAction):
    """ QWidgetAction(parent: Optional[QObject]) """
    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def createdWidgets(self): # real signature unknown; restored from __doc__
        """ createdWidgets(self) -> List[QWidget] """
        return []

    def createWidget(self, parent, QWidget=None): # real signature unknown; restored from __doc__
        """ createWidget(self, parent: Optional[QWidget]) -> Optional[QWidget] """
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def defaultWidget(self): # real signature unknown; restored from __doc__
        """ defaultWidget(self) -> Optional[QWidget] """
        pass

    def deleteWidget(self, widget, QWidget=None): # real signature unknown; restored from __doc__
        """ deleteWidget(self, widget: Optional[QWidget]) """
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def event(self, a0, QEvent=None): # real signature unknown; restored from __doc__
        """ event(self, a0: Optional[QEvent]) -> bool """
        return False

    def eventFilter(self, a0, QObject=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ eventFilter(self, a0: Optional[QObject], a1: Optional[QEvent]) -> bool """
        pass

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def releaseWidget(self, widget, QWidget=None): # real signature unknown; restored from __doc__
        """ releaseWidget(self, widget: Optional[QWidget]) """
        pass

    def requestWidget(self, parent, QWidget=None): # real signature unknown; restored from __doc__
        """ requestWidget(self, parent: Optional[QWidget]) -> Optional[QWidget] """
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setDefaultWidget(self, w, QWidget=None): # real signature unknown; restored from __doc__
        """ setDefaultWidget(self, w: Optional[QWidget]) """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, parent, QObject=None): # real signature unknown; restored from __doc__
        pass


