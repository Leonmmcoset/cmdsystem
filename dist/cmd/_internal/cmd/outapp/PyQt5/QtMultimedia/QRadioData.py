# encoding: utf-8
# module PyQt5.QtMultimedia
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtMultimedia.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


from .QMediaBindableInterface import QMediaBindableInterface

class QRadioData(__PyQt5_QtCore.QObject, QMediaBindableInterface):
    """ QRadioData(mediaObject: Optional[QMediaObject], parent: Optional[QObject] = None) """
    def alternativeFrequenciesEnabledChanged(self, *args, **kwargs): # real signature unknown
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

    def availability(self): # real signature unknown; restored from __doc__
        """ availability(self) -> QMultimedia.AvailabilityStatus """
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def error(self, *args, **kwargs): # real signature unknown
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

    def errorString(self): # real signature unknown; restored from __doc__
        """ errorString(self) -> str """
        return ""

    def isAlternativeFrequenciesEnabled(self): # real signature unknown; restored from __doc__
        """ isAlternativeFrequenciesEnabled(self) -> bool """
        return False

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def mediaObject(self): # real signature unknown; restored from __doc__
        """ mediaObject(self) -> Optional[QMediaObject] """
        pass

    def programType(self): # real signature unknown; restored from __doc__
        """ programType(self) -> QRadioData.ProgramType """
        pass

    def programTypeChanged(self, *args, **kwargs): # real signature unknown
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

    def programTypeName(self): # real signature unknown; restored from __doc__
        """ programTypeName(self) -> str """
        return ""

    def programTypeNameChanged(self, *args, **kwargs): # real signature unknown
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

    def radioText(self): # real signature unknown; restored from __doc__
        """ radioText(self) -> str """
        return ""

    def radioTextChanged(self, *args, **kwargs): # real signature unknown
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

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setAlternativeFrequenciesEnabled(self, enabled): # real signature unknown; restored from __doc__
        """ setAlternativeFrequenciesEnabled(self, enabled: bool) """
        pass

    def setMediaObject(self, a0, QMediaObject=None): # real signature unknown; restored from __doc__
        """ setMediaObject(self, a0: Optional[QMediaObject]) -> bool """
        return False

    def stationId(self): # real signature unknown; restored from __doc__
        """ stationId(self) -> str """
        return ""

    def stationIdChanged(self, *args, **kwargs): # real signature unknown
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

    def stationName(self): # real signature unknown; restored from __doc__
        """ stationName(self) -> str """
        return ""

    def stationNameChanged(self, *args, **kwargs): # real signature unknown
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

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, mediaObject, QMediaObject=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    AdultHits = 34
    Alarm = 31
    AlarmTest = 30
    ChildrensProgrammes = 18
    Classical = 39
    ClassicRock = 33
    College = 47
    CountryMusic = 25
    Culture = 7
    CurrentAffairs = 2
    Documentary = 29
    Drama = 6
    EasyListening = 12
    Education = 5
    Finance = 17
    FolkMusic = 28
    Information = 3
    JazzMusic = 24
    Language = 42
    Leisure = 23
    LightClassical = 13
    NationalMusic = 26
    News = 1
    NoError = 0
    Nostalgia = 38
    OldiesMusic = 27
    OpenError = 2
    OtherMusic = 15
    OutOfRangeError = 3
    Personality = 45
    PhoneIn = 21
    PopMusic = 10
    Public = 46
    Religion = 20
    ReligiousMusic = 43
    ReligiousTalk = 44
    ResourceError = 1
    RhythmAndBlues = 40
    RockMusic = 11
    Science = 8
    SeriousClassical = 14
    SocialAffairs = 19
    Soft = 37
    SoftRhythmAndBlues = 41
    SoftRock = 35
    Sport = 4
    Talk = 32
    Top40 = 36
    Travel = 22
    Undefined = 0
    Varied = 9
    Weather = 16


