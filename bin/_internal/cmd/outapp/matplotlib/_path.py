# encoding: utf-8
# module matplotlib._path
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\matplotlib\_path.cp311-win_amd64.pyd
# by generator 1.147
# no doc
# no imports

# functions

def affine_transform(*args, **kwargs): # real signature unknown
    pass

def cleanup_path(*args, **kwargs): # real signature unknown
    pass

def clip_path_to_rect(*args, **kwargs): # real signature unknown
    pass

def convert_path_to_polygons(*args, **kwargs): # real signature unknown
    pass

def convert_to_string(*args, **kwargs): # real signature unknown
    """
    Convert *path* to a bytestring.
    
    The first five parameters (up to *sketch*) are interpreted as in
    `.cleanup_path`.  The following ones are detailed below.
    
    Parameters
    ----------
    path : Path
    trans : Transform or None
    clip_rect : sequence of 4 floats, or None
    simplify : bool
    sketch : tuple of 3 floats, or None
    precision : int
        The precision used to "%.*f"-format the values.  Trailing zeros
        and decimal points are always removed.  (precision=-1 is a special
        case used to implement ttconv-back-compatible conversion.)
    codes : sequence of 5 bytestrings
        The bytes representation of each opcode (MOVETO, LINETO, CURVE3,
        CURVE4, CLOSEPOLY), in that order.  If the bytes for CURVE3 is
        empty, quad segments are automatically converted to cubic ones
        (this is used by backends such as pdf and ps, which do not support
        quads).
    postfix : bool
        Whether the opcode comes after the values (True) or before (False).
    """
    pass

def count_bboxes_overlapping_bbox(*args, **kwargs): # real signature unknown
    pass

def get_path_collection_extents(*args, **kwargs): # real signature unknown
    pass

def is_sorted_and_has_non_nan(*args, **kwargs): # real signature unknown
    """
    Return whether the 1D *array* is monotonically increasing, ignoring NaNs,
    and has at least one non-nan value.
    """
    pass

def path_intersects_path(*args, **kwargs): # real signature unknown
    pass

def path_intersects_rectangle(*args, **kwargs): # real signature unknown
    pass

def path_in_path(*args, **kwargs): # real signature unknown
    pass

def points_in_path(*args, **kwargs): # real signature unknown
    pass

def point_in_path(*args, **kwargs): # real signature unknown
    pass

def point_in_path_collection(*args, **kwargs): # real signature unknown
    pass

def update_path_extents(*args, **kwargs): # real signature unknown
    pass

# no classes
# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x000001CCDFB4A290>'

__spec__ = None # (!) real value is "ModuleSpec(name='matplotlib._path', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x000001CCDFB4A290>, origin='C:\\\\Users\\\\leonm\\\\PycharmProjects\\\\leonsystem\\\\venv\\\\Lib\\\\site-packages\\\\matplotlib\\\\_path.cp311-win_amd64.pyd')"

