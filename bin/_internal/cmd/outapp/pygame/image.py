# encoding: utf-8
# module pygame.image
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\pygame\image.cp311-win_amd64.pyd
# by generator 1.147
""" pygame module for image transfer """
# no imports

# functions

def frombuffer(buffer, size, format): # real signature unknown; restored from __doc__
    """
    frombuffer(buffer, size, format) -> Surface
    create a new Surface that shares data inside a bytes buffer
    """
    pass

def frombytes(bytes, size, format, flipped=False): # real signature unknown; restored from __doc__
    """
    frombytes(bytes, size, format, flipped=False) -> Surface
    create new Surface from a byte buffer
    """
    pass

def fromstring(bytes, size, format, flipped=False): # real signature unknown; restored from __doc__
    """
    fromstring(bytes, size, format, flipped=False) -> Surface
    create new Surface from a byte buffer
    """
    pass

def get_extended(): # real signature unknown; restored from __doc__
    """
    get_extended() -> bool
    test if extended image formats can be loaded
    """
    return False

def get_sdl_image_version(linked=True): # real signature unknown; restored from __doc__
    """
    get_sdl_image_version(linked=True) -> None
    get_sdl_image_version(linked=True) -> (major, minor, patch)
    get version number of the SDL_Image library being used
    """
    pass

def load(filename): # real signature unknown; restored from __doc__
    """
    load(filename) -> Surface
    load(fileobj, namehint=) -> Surface
    load new image from a file (or file-like object)
    """
    pass

def load_basic(file): # real signature unknown; restored from __doc__
    """
    load_basic(file) -> Surface
    load new BMP image from a file (or file-like object)
    """
    pass

def load_extended(filename): # real signature unknown; restored from __doc__
    """
    load_extended(filename) -> Surface
    load_extended(fileobj, namehint=) -> Surface
    load an image from a file (or file-like object)
    """
    pass

def save(Surface, filename): # real signature unknown; restored from __doc__
    """
    save(Surface, filename) -> None
    save(Surface, fileobj, namehint=) -> None
    save an image to file (or file-like object)
    """
    pass

def save_extended(Surface, filename): # real signature unknown; restored from __doc__
    """
    save_extended(Surface, filename) -> None
    save_extended(Surface, fileobj, namehint=) -> None
    save a png/jpg image to file (or file-like object)
    """
    pass

def tobytes(Surface, format, flipped=False): # real signature unknown; restored from __doc__
    """
    tobytes(Surface, format, flipped=False) -> bytes
    transfer image to byte buffer
    """
    return b""

def tostring(Surface, format, flipped=False): # real signature unknown; restored from __doc__
    """
    tostring(Surface, format, flipped=False) -> bytes
    transfer image to byte buffer
    """
    return b""

# no classes
# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x000002534455BA10>'

__spec__ = None # (!) real value is "ModuleSpec(name='pygame.image', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x000002534455BA10>, origin='C:\\\\Users\\\\leonm\\\\PycharmProjects\\\\leonsystem\\\\venv\\\\Lib\\\\site-packages\\\\pygame\\\\image.cp311-win_amd64.pyd')"

