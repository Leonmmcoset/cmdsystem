# encoding: utf-8
# module PyQt5.QtWidgets
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtWidgets.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import PyQt5.QtGui as __PyQt5_QtGui
import sip as __sip


class QFileIconProvider(__sip.simplewrapper):
    """ QFileIconProvider() """
    def icon(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        icon(self, type: QFileIconProvider.IconType) -> QIcon
        icon(self, info: QFileInfo) -> QIcon
        """
        pass

    def options(self): # real signature unknown; restored from __doc__
        """ options(self) -> QFileIconProvider.Options """
        pass

    def setOptions(self, options, QFileIconProvider_Options=None, QFileIconProvider_Option=None): # real signature unknown; restored from __doc__
        """ setOptions(self, options: Union[QFileIconProvider.Options, QFileIconProvider.Option]) """
        pass

    def type(self, info): # real signature unknown; restored from __doc__
        """ type(self, info: QFileInfo) -> str """
        return ""

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    Computer = 0
    Desktop = 1
    DontUseCustomDirectoryIcons = 1
    Drive = 4
    File = 6
    Folder = 5
    Network = 3
    Trashcan = 2


