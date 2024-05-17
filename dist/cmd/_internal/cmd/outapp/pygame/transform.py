# encoding: utf-8
# module pygame.transform
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\pygame\transform.cp311-win_amd64.pyd
# by generator 1.147
""" pygame module to transform surfaces """
# no imports

# functions

def average_color(surface, rect=None, consider_alpha=False): # real signature unknown; restored from __doc__
    """
    average_color(surface, rect=None, consider_alpha=False) -> Color
    finds the average color of a surface
    """
    pass

def average_surfaces(surfaces, dest_surface=None, palette_colors=1): # real signature unknown; restored from __doc__
    """
    average_surfaces(surfaces, dest_surface=None, palette_colors=1) -> Surface
    find the average surface from many surfaces.
    """
    pass

def chop(surface, rect): # real signature unknown; restored from __doc__
    """
    chop(surface, rect) -> Surface
    gets a copy of an image with an interior area removed
    """
    pass

def flip(surface, flip_x, flip_y): # real signature unknown; restored from __doc__
    """
    flip(surface, flip_x, flip_y) -> Surface
    flip vertically and horizontally
    """
    pass

def get_smoothscale_backend(): # real signature unknown; restored from __doc__
    """
    get_smoothscale_backend() -> string
    return smoothscale filter version in use: 'GENERIC', 'MMX', or 'SSE'
    """
    return ""

def grayscale(surface, dest_surface=None): # real signature unknown; restored from __doc__
    """
    grayscale(surface, dest_surface=None) -> Surface
    grayscale a surface
    """
    pass

def laplacian(*args, **kwargs): # real signature unknown
    """
    threshold(dest_surface, surface, search_color, threshold=(0,0,0,0), set_color=(0,0,0,0), set_behavior=1, search_surf=None, inverse_set=False) -> num_threshold_pixels
    finds which, and how many pixels in a surface are within a threshold of a 'search_color' or a 'search_surf'.
    """
    pass

def rotate(surface, angle): # real signature unknown; restored from __doc__
    """
    rotate(surface, angle) -> Surface
    rotate an image
    """
    pass

def rotozoom(surface, angle, scale): # real signature unknown; restored from __doc__
    """
    rotozoom(surface, angle, scale) -> Surface
    filtered scale and rotation
    """
    pass

def scale(surface, size, dest_surface=None): # real signature unknown; restored from __doc__
    """
    scale(surface, size, dest_surface=None) -> Surface
    resize to new resolution
    """
    pass

def scale2x(surface, dest_surface=None): # real signature unknown; restored from __doc__
    """
    scale2x(surface, dest_surface=None) -> Surface
    specialized image doubler
    """
    pass

def scale_by(surface, factor, dest_surface=None): # real signature unknown; restored from __doc__
    """
    scale_by(surface, factor, dest_surface=None) -> Surface
    resize to new resolution, using scalar(s)
    """
    pass

def set_smoothscale_backend(backend): # real signature unknown; restored from __doc__
    """
    set_smoothscale_backend(backend) -> None
    set smoothscale filter version to one of: 'GENERIC', 'MMX', or 'SSE'
    """
    pass

def smoothscale(surface, size, dest_surface=None): # real signature unknown; restored from __doc__
    """
    smoothscale(surface, size, dest_surface=None) -> Surface
    scale a surface to an arbitrary size smoothly
    """
    pass

def smoothscale_by(surface, factor, dest_surface=None): # real signature unknown; restored from __doc__
    """
    smoothscale_by(surface, factor, dest_surface=None) -> Surface
    resize to new resolution, using scalar(s)
    """
    pass

def threshold(dest_surface, surface, search_color, threshold=(0,0,0,0), set_color=(0,0,0,0), set_behavior=1, search_surf=None, inverse_set=False): # real signature unknown; restored from __doc__
    """
    threshold(dest_surface, surface, search_color, threshold=(0,0,0,0), set_color=(0,0,0,0), set_behavior=1, search_surf=None, inverse_set=False) -> num_threshold_pixels
    finds which, and how many pixels in a surface are within a threshold of a 'search_color' or a 'search_surf'.
    """
    pass

# no classes
# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x0000020170BB6450>'

__spec__ = None # (!) real value is "ModuleSpec(name='pygame.transform', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x0000020170BB6450>, origin='C:\\\\Users\\\\leonm\\\\PycharmProjects\\\\leonsystem\\\\venv\\\\Lib\\\\site-packages\\\\pygame\\\\transform.cp311-win_amd64.pyd')"

