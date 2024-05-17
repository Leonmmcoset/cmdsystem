# encoding: utf-8
# module pygame._camera
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\pygame\_camera.cp311-win_amd64.pyd
# by generator 1.147
""" pygame module for camera use """
# no imports

# functions

def colorspace(Surface, format, DestSurface=None): # real signature unknown; restored from __doc__
    """
    colorspace(Surface, format, DestSurface = None) -> Surface
    Surface colorspace conversion
    """
    pass

def list_cameras(): # real signature unknown; restored from __doc__
    """
    list_cameras() -> [cameras]
    returns a list of available cameras
    """
    pass

# classes

class CameraType(object):
    """
    Camera(device, (width, height), format) -> Camera
    load a camera
    """
    def get_controls(self): # real signature unknown; restored from __doc__
        """
        get_controls() -> (hflip = bool, vflip = bool, brightness)
        gets current values of user controls
        """
        pass

    def get_image(self, Surface=None): # real signature unknown; restored from __doc__
        """
        get_image(Surface = None) -> Surface
        captures an image as a Surface
        """
        pass

    def get_raw(self): # real signature unknown; restored from __doc__
        """
        get_raw() -> bytes
        returns an unmodified image as bytes
        """
        return b""

    def get_size(self): # real signature unknown; restored from __doc__
        """
        get_size() -> (width, height)
        returns the dimensions of the images being recorded
        """
        pass

    def query_image(self): # real signature unknown; restored from __doc__
        """
        query_image() -> bool
        checks if a frame is ready
        """
        return False

    def set_controls(self, hflip=None, vflip=None, brightness): # real signature unknown; restored from __doc__
        """
        set_controls(hflip = bool, vflip = bool, brightness) -> (hflip = bool, vflip = bool, brightness)
        changes camera settings if supported by the camera
        """
        pass

    def start(self): # real signature unknown; restored from __doc__
        """
        start() -> None
        opens, initializes, and starts capturing
        """
        pass

    def stop(self): # real signature unknown; restored from __doc__
        """
        stop() -> None
        stops, uninitializes, and closes the camera
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass


Camera = CameraType


# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x000002A891978BD0>'

__spec__ = None # (!) real value is "ModuleSpec(name='pygame._camera', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x000002A891978BD0>, origin='C:\\\\Users\\\\leonm\\\\PycharmProjects\\\\leonsystem\\\\venv\\\\Lib\\\\site-packages\\\\pygame\\\\_camera.cp311-win_amd64.pyd')"

