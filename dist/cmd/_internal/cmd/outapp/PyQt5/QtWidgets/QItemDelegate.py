# encoding: utf-8
# module PyQt5.QtWidgets
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtWidgets.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import PyQt5.QtGui as __PyQt5_QtGui
import sip as __sip


from .QAbstractItemDelegate import QAbstractItemDelegate

class QItemDelegate(QAbstractItemDelegate):
    """ QItemDelegate(parent: Optional[QObject] = None) """
    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def createEditor(self, parent, QWidget=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ createEditor(self, parent: Optional[QWidget], option: QStyleOptionViewItem, index: QModelIndex) -> Optional[QWidget] """
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def drawBackground(self, painter, QPainter=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ drawBackground(self, painter: Optional[QPainter], option: QStyleOptionViewItem, index: QModelIndex) """
        pass

    def drawCheck(self, painter, QPainter=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ drawCheck(self, painter: Optional[QPainter], option: QStyleOptionViewItem, rect: QRect, state: Qt.CheckState) """
        pass

    def drawDecoration(self, painter, QPainter=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ drawDecoration(self, painter: Optional[QPainter], option: QStyleOptionViewItem, rect: QRect, pixmap: QPixmap) """
        pass

    def drawDisplay(self, painter, QPainter=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ drawDisplay(self, painter: Optional[QPainter], option: QStyleOptionViewItem, rect: QRect, text: Optional[str]) """
        pass

    def drawFocus(self, painter, QPainter=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ drawFocus(self, painter: Optional[QPainter], option: QStyleOptionViewItem, rect: QRect) """
        pass

    def editorEvent(self, event, QEvent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ editorEvent(self, event: Optional[QEvent], model: Optional[QAbstractItemModel], option: QStyleOptionViewItem, index: QModelIndex) -> bool """
        pass

    def eventFilter(self, p_object, QObject=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ eventFilter(self, object: Optional[QObject], event: Optional[QEvent]) -> bool """
        pass

    def hasClipping(self): # real signature unknown; restored from __doc__
        """ hasClipping(self) -> bool """
        return False

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def itemEditorFactory(self): # real signature unknown; restored from __doc__
        """ itemEditorFactory(self) -> Optional[QItemEditorFactory] """
        pass

    def paint(self, painter, QPainter=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ paint(self, painter: Optional[QPainter], option: QStyleOptionViewItem, index: QModelIndex) """
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setClipping(self, clip): # real signature unknown; restored from __doc__
        """ setClipping(self, clip: bool) """
        pass

    def setEditorData(self, editor, QWidget=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ setEditorData(self, editor: Optional[QWidget], index: QModelIndex) """
        pass

    def setItemEditorFactory(self, factory, QItemEditorFactory=None): # real signature unknown; restored from __doc__
        """ setItemEditorFactory(self, factory: Optional[QItemEditorFactory]) """
        pass

    def setModelData(self, editor, QWidget=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ setModelData(self, editor: Optional[QWidget], model: Optional[QAbstractItemModel], index: QModelIndex) """
        pass

    def sizeHint(self, option, index): # real signature unknown; restored from __doc__
        """ sizeHint(self, option: QStyleOptionViewItem, index: QModelIndex) -> QSize """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def updateEditorGeometry(self, editor, QWidget=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ updateEditorGeometry(self, editor: Optional[QWidget], option: QStyleOptionViewItem, index: QModelIndex) """
        pass

    def __init__(self, parent, QObject=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass


