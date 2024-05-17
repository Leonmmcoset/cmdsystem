# encoding: utf-8
# module PyQt5.QtSensors
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtSensors.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


from .QSensorReading import QSensorReading

class QLidReading(QSensorReading):
    # no doc
    def backLidChanged(self, *args, **kwargs): # real signature unknown
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

    def backLidClosed(self): # real signature unknown; restored from __doc__
        """ backLidClosed(self) -> bool """
        return False

    def frontLidChanged(self, *args, **kwargs): # real signature unknown
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

    def frontLidClosed(self): # real signature unknown; restored from __doc__
        """ frontLidClosed(self) -> bool """
        return False

    def setBackLidClosed(self, closed): # real signature unknown; restored from __doc__
        """ setBackLidClosed(self, closed: bool) """
        pass

    def setFrontLidClosed(self, closed): # real signature unknown; restored from __doc__
        """ setFrontLidClosed(self, closed: bool) """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass


