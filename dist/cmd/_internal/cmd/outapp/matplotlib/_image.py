# encoding: utf-8
# module matplotlib._image
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\matplotlib\_image.cp311-win_amd64.pyd
# by generator 1.147
# no doc
# no imports

# Variables with simple values

BESSEL = 12

BICUBIC = 2
BILINEAR = 1

BLACKMAN = 16

CATROM = 10

GAUSSIAN = 11

HAMMING = 6
HANNING = 5

HERMITE = 7

KAISER = 8

LANCZOS = 15

MITCHELL = 13

NEAREST = 0

QUADRIC = 9

SINC = 14

SPLINE16 = 3
SPLINE36 = 4

_n_interpolation = 17

# functions

def resample(*args, **kwargs): # real signature unknown
    """
    Resample input_array, blending it in-place into output_array, using an
    affine transformation.
    
    Parameters
    ----------
    input_array : 2-d or 3-d NumPy array of float, double or `numpy.uint8`
        If 2-d, the image is grayscale.  If 3-d, the image must be of size
        4 in the last dimension and represents RGBA data.
    
    output_array : 2-d or 3-d NumPy array of float, double or `numpy.uint8`
        The dtype and number of dimensions must match `input_array`.
    
    transform : matplotlib.transforms.Transform instance
        The transformation from the input array to the output array.
    
    interpolation : int, default: NEAREST
        The interpolation method.  Must be one of the following constants
        defined in this module:
    
          NEAREST, BILINEAR, BICUBIC, SPLINE16, SPLINE36,
          HANNING, HAMMING, HERMITE, KAISER, QUADRIC, CATROM, GAUSSIAN,
          BESSEL, MITCHELL, SINC, LANCZOS, BLACKMAN
    
    resample : bool, optional
        When `True`, use a full resampling method.  When `False`, only
        resample when the output image is larger than the input image.
    
    alpha : float, default: 1
        The transparency level, from 0 (transparent) to 1 (opaque).
    
    norm : bool, default: False
        Whether to norm the interpolation function.
    
    radius: float, default: 1
        The radius of the kernel, if method is SINC, LANCZOS or BLACKMAN.
    """
    pass

# no classes
# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x000001CF418BF790>'

__spec__ = None # (!) real value is "ModuleSpec(name='matplotlib._image', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x000001CF418BF790>, origin='C:\\\\Users\\\\leonm\\\\PycharmProjects\\\\leonsystem\\\\venv\\\\Lib\\\\site-packages\\\\matplotlib\\\\_image.cp311-win_amd64.pyd')"

