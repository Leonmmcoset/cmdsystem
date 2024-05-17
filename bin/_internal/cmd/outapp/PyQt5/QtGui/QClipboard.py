# encoding: utf-8
# module PyQt5.QtGui
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtGui.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


class QClipboard(__PyQt5_QtCore.QObject):
    # no doc
    def changed(self, *args, **kwargs): # real signature unknown
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

    def clear(self, mode=None): # real signature unknown; restored from __doc__
        """ clear(self, mode: QClipboard.Mode = QClipboard.Clipboard) """
        pass

    def dataChanged(self, *args, **kwargs): # real signature unknown
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

    def findBufferChanged(self, *args, **kwargs): # real signature unknown
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

    def image(self, mode=None): # real signature unknown; restored from __doc__
        """ image(self, mode: QClipboard.Mode = QClipboard.Clipboard) -> QImage """
        return QImage

    def mimeData(self, mode=None): # real signature unknown; restored from __doc__
        """ mimeData(self, mode: QClipboard.Mode = QClipboard.Clipboard) -> Optional[QMimeData] """
        pass

    def ownsClipboard(self): # real signature unknown; restored from __doc__
        """ ownsClipboard(self) -> bool """
        return False

    def ownsFindBuffer(self): # real signature unknown; restored from __doc__
        """ ownsFindBuffer(self) -> bool """
        return False

    def ownsSelection(self): # real signature unknown; restored from __doc__
        """ ownsSelection(self) -> bool """
        return False

    def pixmap(self, mode=None): # real signature unknown; restored from __doc__
        """ pixmap(self, mode: QClipboard.Mode = QClipboard.Clipboard) -> QPixmap """
        return QPixmap

    def selectionChanged(self, *args, **kwargs): # real signature unknown
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

    def setImage(self, a0, mode=None): # real signature unknown; restored from __doc__
        """ setImage(self, a0: QImage, mode: QClipboard.Mode = QClipboard.Clipboard) """
        pass

    def setMimeData(self, data, QMimeData=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ setMimeData(self, data: Optional[QMimeData], mode: QClipboard.Mode = QClipboard.Clipboard) """
        pass

    def setPixmap(self, a0, mode=None): # real signature unknown; restored from __doc__
        """ setPixmap(self, a0: QPixmap, mode: QClipboard.Mode = QClipboard.Clipboard) """
        pass

    def setText(self, a0, p_str=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ setText(self, a0: Optional[str], mode: QClipboard.Mode = QClipboard.Clipboard) """
        pass

    def supportsFindBuffer(self): # real signature unknown; restored from __doc__
        """ supportsFindBuffer(self) -> bool """
        return False

    def supportsSelection(self): # real signature unknown; restored from __doc__
        """ supportsSelection(self) -> bool """
        return False

    def text(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        text(self, mode: QClipboard.Mode = QClipboard.Clipboard) -> str
        text(self, subtype: Optional[str], mode: QClipboard.Mode = QClipboard.Clipboard) -> Tuple[str, str]
        """
        return ""

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    Clipboard = 0
    FindBuffer = 2
    Selection = 1


