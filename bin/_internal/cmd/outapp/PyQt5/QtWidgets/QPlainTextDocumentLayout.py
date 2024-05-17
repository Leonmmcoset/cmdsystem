# encoding: utf-8
# module PyQt5.QtWidgets
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtWidgets.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import PyQt5.QtGui as __PyQt5_QtGui
import sip as __sip


class QPlainTextDocumentLayout(__PyQt5_QtGui.QAbstractTextDocumentLayout):
    """ QPlainTextDocumentLayout(document: Optional[QTextDocument]) """
    def blockBoundingRect(self, block): # real signature unknown; restored from __doc__
        """ blockBoundingRect(self, block: QTextBlock) -> QRectF """
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def cursorWidth(self): # real signature unknown; restored from __doc__
        """ cursorWidth(self) -> int """
        return 0

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def documentChanged(self, from_, a1, charsAdded): # real signature unknown; restored from __doc__
        """ documentChanged(self, from_: int, a1: int, charsAdded: int) """
        pass

    def documentSize(self): # real signature unknown; restored from __doc__
        """ documentSize(self) -> QSizeF """
        pass

    def draw(self, a0, QPainter=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ draw(self, a0: Optional[QPainter], a1: QAbstractTextDocumentLayout.PaintContext) """
        pass

    def drawInlineObject(self, *args, **kwargs): # real signature unknown
        pass

    def ensureBlockLayout(self, block): # real signature unknown; restored from __doc__
        """ ensureBlockLayout(self, block: QTextBlock) """
        pass

    def format(self, *args, **kwargs): # real signature unknown
        pass

    def frameBoundingRect(self, a0, QTextFrame=None): # real signature unknown; restored from __doc__
        """ frameBoundingRect(self, a0: Optional[QTextFrame]) -> QRectF """
        pass

    def hitTest(self, a0, QPointF=None, QPoint=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ hitTest(self, a0: Union[QPointF, QPoint], a1: Qt.HitTestAccuracy) -> int """
        pass

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def pageCount(self): # real signature unknown; restored from __doc__
        """ pageCount(self) -> int """
        return 0

    def positionInlineObject(self, *args, **kwargs): # real signature unknown
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def requestUpdate(self): # real signature unknown; restored from __doc__
        """ requestUpdate(self) """
        pass

    def resizeInlineObject(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setCursorWidth(self, width): # real signature unknown; restored from __doc__
        """ setCursorWidth(self, width: int) """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, document, QTextDocument=None): # real signature unknown; restored from __doc__
        pass


