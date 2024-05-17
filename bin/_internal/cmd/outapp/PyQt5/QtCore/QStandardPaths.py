# encoding: utf-8
# module PyQt5.QtCore
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtCore.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum
import sip as __sip


class QStandardPaths(__sip.simplewrapper):
    """ QStandardPaths(a0: QStandardPaths) """
    def displayName(self, type): # real signature unknown; restored from __doc__
        """ displayName(type: QStandardPaths.StandardLocation) -> str """
        return ""

    def enableTestMode(self, testMode): # real signature unknown; restored from __doc__
        """ enableTestMode(testMode: bool) """
        pass

    def findExecutable(self, executableName, p_str=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ findExecutable(executableName: Optional[str], paths: Iterable[Optional[str]] = []) -> str """
        pass

    def locate(self, type, fileName, p_str=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ locate(type: QStandardPaths.StandardLocation, fileName: Optional[str], options: QStandardPaths.LocateOptions = QStandardPaths.LocateFile) -> str """
        pass

    def locateAll(self, type, fileName, p_str=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ locateAll(type: QStandardPaths.StandardLocation, fileName: Optional[str], options: QStandardPaths.LocateOptions = QStandardPaths.LocateFile) -> List[str] """
        pass

    def setTestModeEnabled(self, testMode): # real signature unknown; restored from __doc__
        """ setTestModeEnabled(testMode: bool) """
        pass

    def standardLocations(self, type): # real signature unknown; restored from __doc__
        """ standardLocations(type: QStandardPaths.StandardLocation) -> List[str] """
        return []

    def writableLocation(self, type): # real signature unknown; restored from __doc__
        """ writableLocation(type: QStandardPaths.StandardLocation) -> str """
        return ""

    def __init__(self, a0): # real signature unknown; restored from __doc__
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    AppConfigLocation = 18
    AppDataLocation = 17
    ApplicationsLocation = 3
    AppLocalDataLocation = 9
    CacheLocation = 10
    ConfigLocation = 13
    DataLocation = 9
    DesktopLocation = 0
    DocumentsLocation = 1
    DownloadLocation = 14
    FontsLocation = 2
    GenericCacheLocation = 15
    GenericConfigLocation = 16
    GenericDataLocation = 11
    HomeLocation = 8
    LocateDirectory = 1
    LocateFile = 0
    MoviesLocation = 5
    MusicLocation = 4
    PicturesLocation = 6
    RuntimeLocation = 12
    TempLocation = 7


