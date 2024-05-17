# encoding: utf-8
# module PyQt5.QtGui
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtGui.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


class QScrollEvent(__PyQt5_QtCore.QEvent):
    """
    QScrollEvent(contentPos: Union[QPointF, QPoint], overshoot: Union[QPointF, QPoint], scrollState: QScrollEvent.ScrollState)
    QScrollEvent(a0: QScrollEvent)
    """
    def contentPos(self): # real signature unknown; restored from __doc__
        """ contentPos(self) -> QPointF """
        pass

    def overshootDistance(self): # real signature unknown; restored from __doc__
        """ overshootDistance(self) -> QPointF """
        pass

    def scrollState(self): # real signature unknown; restored from __doc__
        """ scrollState(self) -> QScrollEvent.ScrollState """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    ScrollFinished = 2
    ScrollStarted = 0
    ScrollUpdated = 1


