# encoding: utf-8
# module PyQt5.QtGui
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtGui.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


class QAbstractTextDocumentLayout(__PyQt5_QtCore.QObject):
    """ QAbstractTextDocumentLayout(doc: Optional[QTextDocument]) """
    def anchorAt(self, pos, QPointF=None, QPoint=None): # real signature unknown; restored from __doc__
        """ anchorAt(self, pos: Union[QPointF, QPoint]) -> str """
        return ""

    def blockBoundingRect(self, block): # real signature unknown; restored from __doc__
        """ blockBoundingRect(self, block: QTextBlock) -> QRectF """
        pass

    def blockWithMarkerAt(self, pos, QPointF=None, QPoint=None): # real signature unknown; restored from __doc__
        """ blockWithMarkerAt(self, pos: Union[QPointF, QPoint]) -> QTextBlock """
        return QTextBlock

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def document(self): # real signature unknown; restored from __doc__
        """ document(self) -> Optional[QTextDocument] """
        pass

    def documentChanged(self, from_, charsRemoved, charsAdded): # real signature unknown; restored from __doc__
        """ documentChanged(self, from_: int, charsRemoved: int, charsAdded: int) """
        pass

    def documentSize(self): # real signature unknown; restored from __doc__
        """ documentSize(self) -> QSizeF """
        pass

    def documentSizeChanged(self, *args, **kwargs): # real signature unknown
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

    def draw(self, painter, QPainter=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ draw(self, painter: Optional[QPainter], context: QAbstractTextDocumentLayout.PaintContext) """
        pass

    def drawInlineObject(self, painter, QPainter=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ drawInlineObject(self, painter: Optional[QPainter], rect: QRectF, object: QTextInlineObject, posInDocument: int, format: QTextFormat) """
        pass

    def format(self, pos): # real signature unknown; restored from __doc__
        """ format(self, pos: int) -> QTextCharFormat """
        return QTextCharFormat

    def formatAt(self, pos, QPointF=None, QPoint=None): # real signature unknown; restored from __doc__
        """ formatAt(self, pos: Union[QPointF, QPoint]) -> QTextFormat """
        return QTextFormat

    def frameBoundingRect(self, frame, QTextFrame=None): # real signature unknown; restored from __doc__
        """ frameBoundingRect(self, frame: Optional[QTextFrame]) -> QRectF """
        pass

    def handlerForObject(self, objectType): # real signature unknown; restored from __doc__
        """ handlerForObject(self, objectType: int) -> Optional[QTextObjectInterface] """
        pass

    def hitTest(self, point, QPointF=None, QPoint=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ hitTest(self, point: Union[QPointF, QPoint], accuracy: Qt.HitTestAccuracy) -> int """
        pass

    def imageAt(self, pos, QPointF=None, QPoint=None): # real signature unknown; restored from __doc__
        """ imageAt(self, pos: Union[QPointF, QPoint]) -> str """
        return ""

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def pageCount(self): # real signature unknown; restored from __doc__
        """ pageCount(self) -> int """
        return 0

    def pageCountChanged(self, *args, **kwargs): # real signature unknown
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

    def paintDevice(self): # real signature unknown; restored from __doc__
        """ paintDevice(self) -> Optional[QPaintDevice] """
        pass

    def positionInlineObject(self, item, posInDocument, format): # real signature unknown; restored from __doc__
        """ positionInlineObject(self, item: QTextInlineObject, posInDocument: int, format: QTextFormat) """
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def registerHandler(self, objectType, component, QObject=None): # real signature unknown; restored from __doc__
        """ registerHandler(self, objectType: int, component: Optional[QObject]) """
        pass

    def resizeInlineObject(self, item, posInDocument, format): # real signature unknown; restored from __doc__
        """ resizeInlineObject(self, item: QTextInlineObject, posInDocument: int, format: QTextFormat) """
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setPaintDevice(self, device, QPaintDevice=None): # real signature unknown; restored from __doc__
        """ setPaintDevice(self, device: Optional[QPaintDevice]) """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def unregisterHandler(self, objectType, component, QObject=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ unregisterHandler(self, objectType: int, component: Optional[QObject] = None) """
        pass

    def update(self, *args, **kwargs): # real signature unknown
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

    def updateBlock(self, *args, **kwargs): # real signature unknown
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

    def __init__(self, doc, QTextDocument=None): # real signature unknown; restored from __doc__
        pass



