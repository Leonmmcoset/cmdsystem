# encoding: utf-8
# module pygame.pixelarray
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\pygame\pixelarray.cp311-win_amd64.pyd
# by generator 1.147
# no doc
# no imports

# no functions
# classes

class PixelArray(object):
    """
    PixelArray(Surface) -> PixelArray
    pygame object for direct pixel access of surfaces
    """
    def close(self): # real signature unknown; restored from __doc__
        """
        close() -> PixelArray
        Closes the PixelArray, and releases Surface lock.
        """
        return PixelArray

    def compare(self, array, distance=0, weights=0.2990): # real signature unknown; restored from __doc__
        """
        compare(array, distance=0, weights=(0.299, 0.587, 0.114)) -> PixelArray
        Compares the PixelArray with another one.
        """
        return PixelArray

    def extract(self, color, distance=0, weights=0.2990): # real signature unknown; restored from __doc__
        """
        extract(color, distance=0, weights=(0.299, 0.587, 0.114)) -> PixelArray
        Extracts the passed color from the PixelArray.
        """
        return PixelArray

    def make_surface(self): # real signature unknown; restored from __doc__
        """
        make_surface() -> Surface
        Creates a new Surface from the current PixelArray.
        """
        pass

    def replace(self, color, repcolor, distance=0, weights=0.2990): # real signature unknown; restored from __doc__
        """
        replace(color, repcolor, distance=0, weights=(0.299, 0.587, 0.114)) -> None
        Replaces the passed color in the PixelArray with another one.
        """
        pass

    def transpose(self): # real signature unknown; restored from __doc__
        """
        transpose() -> PixelArray
        Exchanges the x and y axis.
        """
        return PixelArray

    def __contains__(self, *args, **kwargs): # real signature unknown
        """ Return key in self. """
        pass

    def __delitem__(self, *args, **kwargs): # real signature unknown
        """ Delete self[key]. """
        pass

    def __enter__(self, *args, **kwargs): # real signature unknown
        """
        close() -> PixelArray
        Closes the PixelArray, and releases Surface lock.
        """
        pass

    def __exit__(self, *args, **kwargs): # real signature unknown
        """
        extract(color, distance=0, weights=(0.299, 0.587, 0.114)) -> PixelArray
        Extracts the passed color from the PixelArray.
        """
        pass

    def __getitem__(self, *args, **kwargs): # real signature unknown
        """ Return self[key]. """
        pass

    def __init__(self, Surface): # real signature unknown; restored from __doc__
        pass

    def __iter__(self, *args, **kwargs): # real signature unknown
        """ Implement iter(self). """
        pass

    def __len__(self, *args, **kwargs): # real signature unknown
        """ Return len(self). """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __setitem__(self, *args, **kwargs): # real signature unknown
        """ Set self[key] to value. """
        pass

    itemsize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """itemsize -> int
Returns the byte size of a pixel array item"""

    ndim = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """ndim -> int
Returns the number of dimensions."""

    shape = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """shape -> tuple of int's
Returns the array size."""

    strides = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """strides -> tuple of int's
Returns byte offsets for each array dimension."""

    surface = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """surface -> Surface
Gets the Surface the PixelArray uses."""

    _pixels_address = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """pixel buffer address (readonly)"""

    __array_interface__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Version 3"""

    __array_struct__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Version 3"""


    __dict__ = None # (!) real value is "mappingproxy({'__new__': <built-in method __new__ of type object at 0x00007FFFC960C280>, '__repr__': <slot wrapper '__repr__' of 'pygame.pixelarray.PixelArray' objects>, '__iter__': <slot wrapper '__iter__' of 'pygame.pixelarray.PixelArray' objects>, '__len__': <slot wrapper '__len__' of 'pygame.pixelarray.PixelArray' objects>, '__getitem__': <slot wrapper '__getitem__' of 'pygame.pixelarray.PixelArray' objects>, '__setitem__': <slot wrapper '__setitem__' of 'pygame.pixelarray.PixelArray' objects>, '__delitem__': <slot wrapper '__delitem__' of 'pygame.pixelarray.PixelArray' objects>, '__contains__': <slot wrapper '__contains__' of 'pygame.pixelarray.PixelArray' objects>, 'compare': <method 'compare' of 'pygame.pixelarray.PixelArray' objects>, 'extract': <method 'extract' of 'pygame.pixelarray.PixelArray' objects>, 'make_surface': <method 'make_surface' of 'pygame.pixelarray.PixelArray' objects>, 'close': <method 'close' of 'pygame.pixelarray.PixelArray' objects>, '__enter__': <method '__enter__' of 'pygame.pixelarray.PixelArray' objects>, '__exit__': <method '__exit__' of 'pygame.pixelarray.PixelArray' objects>, 'replace': <method 'replace' of 'pygame.pixelarray.PixelArray' objects>, 'transpose': <method 'transpose' of 'pygame.pixelarray.PixelArray' objects>, '__dict__': <attribute '__dict__' of 'pygame.pixelarray.PixelArray' objects>, 'surface': <attribute 'surface' of 'pygame.pixelarray.PixelArray' objects>, 'itemsize': <attribute 'itemsize' of 'pygame.pixelarray.PixelArray' objects>, 'shape': <attribute 'shape' of 'pygame.pixelarray.PixelArray' objects>, 'strides': <attribute 'strides' of 'pygame.pixelarray.PixelArray' objects>, 'ndim': <attribute 'ndim' of 'pygame.pixelarray.PixelArray' objects>, '__array_struct__': <attribute '__array_struct__' of 'pygame.pixelarray.PixelArray' objects>, '__array_interface__': <attribute '__array_interface__' of 'pygame.pixelarray.PixelArray' objects>, '_pixels_address': <attribute '_pixels_address' of 'pygame.pixelarray.PixelArray' objects>, '__doc__': 'PixelArray(Surface) -> PixelArray\\npygame object for direct pixel access of surfaces'})"


# variables with complex values

_PYGAME_C_API = None # (!) real value is '<capsule object "pygame.pixelarray._PYGAME_C_API" at 0x000002A1F2F98240>'

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x000002A1F2F4BE50>'

__spec__ = None # (!) real value is "ModuleSpec(name='pygame.pixelarray', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x000002A1F2F4BE50>, origin='C:\\\\Users\\\\leonm\\\\PycharmProjects\\\\leonsystem\\\\venv\\\\Lib\\\\site-packages\\\\pygame\\\\pixelarray.cp311-win_amd64.pyd')"

