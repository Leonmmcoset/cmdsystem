# encoding: utf-8
# module PyQt5.QtWidgets
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtWidgets.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import PyQt5.QtGui as __PyQt5_QtGui
import sip as __sip


from .QLayoutItem import QLayoutItem

class QSpacerItem(QLayoutItem):
    """
    QSpacerItem(w: int, h: int, hPolicy: QSizePolicy.Policy = QSizePolicy.Minimum, vPolicy: QSizePolicy.Policy = QSizePolicy.Minimum)
    QSpacerItem(a0: QSpacerItem)
    """
    def changeSize(self, w, h, hPolicy=None, vPolicy=None): # real signature unknown; restored from __doc__
        """ changeSize(self, w: int, h: int, hPolicy: QSizePolicy.Policy = QSizePolicy.Minimum, vPolicy: QSizePolicy.Policy = QSizePolicy.Minimum) """
        pass

    def expandingDirections(self): # real signature unknown; restored from __doc__
        """ expandingDirections(self) -> Qt.Orientations """
        pass

    def geometry(self): # real signature unknown; restored from __doc__
        """ geometry(self) -> QRect """
        pass

    def isEmpty(self): # real signature unknown; restored from __doc__
        """ isEmpty(self) -> bool """
        return False

    def maximumSize(self): # real signature unknown; restored from __doc__
        """ maximumSize(self) -> QSize """
        pass

    def minimumSize(self): # real signature unknown; restored from __doc__
        """ minimumSize(self) -> QSize """
        pass

    def setGeometry(self, a0): # real signature unknown; restored from __doc__
        """ setGeometry(self, a0: QRect) """
        pass

    def sizeHint(self): # real signature unknown; restored from __doc__
        """ sizeHint(self) -> QSize """
        pass

    def sizePolicy(self): # real signature unknown; restored from __doc__
        """ sizePolicy(self) -> QSizePolicy """
        return QSizePolicy

    def spacerItem(self): # real signature unknown; restored from __doc__
        """ spacerItem(self) -> Optional[QSpacerItem] """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass


