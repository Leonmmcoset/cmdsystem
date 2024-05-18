# encoding: utf-8
# module contourpy._contourpy
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\contourpy\_contourpy.cp311-win_amd64.pyd
# by generator 1.147
"""
C++11 extension module wrapped using `pybind11`_.

It should not be necessary to access classes and functions in this extension module directly. Instead, :func:`contourpy.contour_generator` should be used to create :class:`~contourpy.ContourGenerator` objects, and the enums (:class:`~contourpy.FillType`, :class:`~contourpy.LineType` and :class:`~contourpy.ZInterp`) and :func:`contourpy.max_threads` function are all available in the :mod:`contourpy` module.
"""

# imports
import pybind11_builtins as __pybind11_builtins


# Variables with simple values

NDEBUG = 1

__version__ = '1.2.1'

# functions

def max_threads(): # real signature unknown; restored from __doc__
    """
    max_threads() -> int
    
    Return the maximum number of threads, obtained from ``std::thread::hardware_concurrency()``.
    
    This is the number of threads used by a multithreaded ContourGenerator if the kwarg ``threads=0`` is passed to :func:`~contourpy.contour_generator`.
    """
    return 0

# classes

class ContourGenerator(__pybind11_builtins.pybind11_object):
    """ Abstract base class for contour generator classes, defining the interface that they all implement. """
    def create_contour(self, level): # real signature unknown; restored from __doc__
        """
        create_contour(self: object, level: float) -> tuple
        
        Synonym for :func:`~contourpy.ContourGenerator.lines` to provide backward compatibility with Matplotlib.
        """
        return ()

    def create_filled_contour(self, lower_level, upper_level): # real signature unknown; restored from __doc__
        """
        create_filled_contour(self: object, lower_level: float, upper_level: float) -> tuple
        
        Synonym for :func:`~contourpy.ContourGenerator.filled` to provide backward compatibility with Matplotlib.
        """
        return ()

    def filled(self, lower_level, upper_level): # real signature unknown; restored from __doc__
        """
        filled(self: object, lower_level: float, upper_level: float) -> tuple
        
        Calculate and return filled contours between two levels.
        
        Args:
            lower_level (float): Lower z-level of the filled contours.
            upper_level (float): Upper z-level of the filled contours.
        Return:
            Filled contour polygons as one or more sequences of numpy arrays. The exact format is determined by the ``fill_type`` used by the ``ContourGenerator``.
        
        Raises a ``ValueError`` if ``lower_level >= upper_level``.
        
        To return filled contours below a ``level`` use ``filled(-np.inf, level)``.
        To return filled contours above a ``level`` use ``filled(level, np.inf)``
        """
        return ()

    def lines(self, level): # real signature unknown; restored from __doc__
        """
        lines(self: object, level: float) -> tuple
        
        Calculate and return contour lines at a particular level.
        
        Args:
            level (float): z-level to calculate contours at.
        
        Return:
            Contour lines (open line strips and closed line loops) as one or more sequences of numpy arrays. The exact format is determined by the ``line_type`` used by the ``ContourGenerator``.
        """
        return ()

    def supports_corner_mask(self): # real signature unknown; restored from __doc__
        """
        supports_corner_mask() -> bool
        
        Return whether this algorithm supports ``corner_mask``.
        """
        return False

    def supports_fill_type(self, fill_type): # real signature unknown; restored from __doc__
        """
        supports_fill_type(fill_type: contourpy._contourpy.FillType) -> bool
        
        Return whether this algorithm supports a particular ``FillType``.
        """
        return False

    def supports_line_type(self, line_type): # real signature unknown; restored from __doc__
        """
        supports_line_type(line_type: contourpy._contourpy.LineType) -> bool
        
        Return whether this algorithm supports a particular ``LineType``.
        """
        return False

    def supports_quad_as_tri(self): # real signature unknown; restored from __doc__
        """
        supports_quad_as_tri() -> bool
        
        Return whether this algorithm supports ``quad_as_tri``.
        """
        return False

    def supports_threads(self): # real signature unknown; restored from __doc__
        """
        supports_threads() -> bool
        
        Return whether this algorithm supports the use of threads.
        """
        return False

    def supports_z_interp(self): # real signature unknown; restored from __doc__
        """
        supports_z_interp() -> bool
        
        Return whether this algorithm supports ``z_interp`` values other than ``ZInterp.Linear`` which all support.
        """
        return False

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    chunk_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Return tuple of (y, x) chunk counts."""

    chunk_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Return tuple of (y, x) chunk sizes."""

    corner_mask = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Return whether ``corner_mask`` is set or not."""

    fill_type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Return the ``FillType``."""

    line_type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Return the ``LineType``."""

    quad_as_tri = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Return whether ``quad_as_tri`` is set or not."""

    thread_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Return the number of threads used."""

    z_interp = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Return the ``ZInterp``."""


    default_fill_type = None # (!) real value is '<FillType.OuterOffset: 202>'
    default_line_type = None # (!) real value is '<LineType.Separate: 101>'


class FillType(__pybind11_builtins.pybind11_object):
    """
    Enum used for ``fill_type`` keyword argument in :func:`~contourpy.contour_generator`.
    
    This controls the format of filled contour data returned from :meth:`~contourpy.ContourGenerator.filled`.
    
    Members:
    
      OuterCode
    
      OuterOffset
    
      ChunkCombinedCode
    
      ChunkCombinedOffset
    
      ChunkCombinedCodeOffset
    
      ChunkCombinedOffsetOffset
    """
    def __eq__(self, other): # real signature unknown; restored from __doc__
        """ __eq__(self: object, other: object) -> bool """
        return False

    def __getstate__(self): # real signature unknown; restored from __doc__
        """ __getstate__(self: object) -> int """
        return 0

    def __hash__(self): # real signature unknown; restored from __doc__
        """ __hash__(self: object) -> int """
        return 0

    def __index__(self): # real signature unknown; restored from __doc__
        """ __index__(self: contourpy._contourpy.FillType) -> int """
        return 0

    def __init__(self, value): # real signature unknown; restored from __doc__
        """ __init__(self: contourpy._contourpy.FillType, value: int) -> None """
        pass

    def __int__(self): # real signature unknown; restored from __doc__
        """ __int__(self: contourpy._contourpy.FillType) -> int """
        return 0

    def __ne__(self, other): # real signature unknown; restored from __doc__
        """ __ne__(self: object, other: object) -> bool """
        return False

    def __repr__(self): # real signature unknown; restored from __doc__
        """ __repr__(self: object) -> str """
        return ""

    def __setstate__(self, state): # real signature unknown; restored from __doc__
        """ __setstate__(self: contourpy._contourpy.FillType, state: int) -> None """
        pass

    def __str__(self): # real signature unknown; restored from __doc__
        """ __str__(self: object) -> str """
        return ""

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """name(self: object) -> str
"""

    value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    ChunkCombinedCode = None # (!) real value is '<FillType.ChunkCombinedCode: 203>'
    ChunkCombinedCodeOffset = None # (!) forward: ChunkCombinedCodeOffset, real value is '<FillType.ChunkCombinedCodeOffset: 205>'
    ChunkCombinedOffset = None # (!) real value is '<FillType.ChunkCombinedOffset: 204>'
    ChunkCombinedOffsetOffset = None # (!) forward: ChunkCombinedOffsetOffset, real value is '<FillType.ChunkCombinedOffsetOffset: 206>'
    OuterCode = None # (!) forward: OuterCode, real value is '<FillType.OuterCode: 201>'
    OuterOffset = None # (!) forward: OuterOffset, real value is '<FillType.OuterOffset: 202>'
    __entries = {
        'ChunkCombinedCode': (
            None, # (!) real value is '<FillType.ChunkCombinedCode: 203>'
            None,
        ),
        'ChunkCombinedCodeOffset': (
            None, # (!) forward: ChunkCombinedCodeOffset, real value is '<FillType.ChunkCombinedCodeOffset: 205>'
            None,
        ),
        'ChunkCombinedOffset': (
            None, # (!) real value is '<FillType.ChunkCombinedOffset: 204>'
            None,
        ),
        'ChunkCombinedOffsetOffset': (
            None, # (!) forward: ChunkCombinedOffsetOffset, real value is '<FillType.ChunkCombinedOffsetOffset: 206>'
            None,
        ),
        'OuterCode': (
            None, # (!) forward: OuterCode, real value is '<FillType.OuterCode: 201>'
            None,
        ),
        'OuterOffset': (
            None, # (!) forward: OuterOffset, real value is '<FillType.OuterOffset: 202>'
            None,
        ),
    }
    __members__ = {
        'ChunkCombinedCode': None, # (!) real value is '<FillType.ChunkCombinedCode: 203>'
        'ChunkCombinedCodeOffset': None, # (!) forward: ChunkCombinedCodeOffset, real value is '<FillType.ChunkCombinedCodeOffset: 205>'
        'ChunkCombinedOffset': None, # (!) real value is '<FillType.ChunkCombinedOffset: 204>'
        'ChunkCombinedOffsetOffset': None, # (!) forward: ChunkCombinedOffsetOffset, real value is '<FillType.ChunkCombinedOffsetOffset: 206>'
        'OuterCode': None, # (!) forward: OuterCode, real value is '<FillType.OuterCode: 201>'
        'OuterOffset': None, # (!) forward: OuterOffset, real value is '<FillType.OuterOffset: 202>'
    }


class LineType(__pybind11_builtins.pybind11_object):
    """
    Enum used for ``line_type`` keyword argument in :func:`~contourpy.contour_generator`.
    
    This controls the format of contour line data returned from :meth:`~contourpy.ContourGenerator.lines`.
    
    ``LineType.ChunkCombinedNan`` added in version 1.2.0
    
    Members:
    
      Separate
    
      SeparateCode
    
      ChunkCombinedCode
    
      ChunkCombinedOffset
    
      ChunkCombinedNan
    """
    def __eq__(self, other): # real signature unknown; restored from __doc__
        """ __eq__(self: object, other: object) -> bool """
        return False

    def __getstate__(self): # real signature unknown; restored from __doc__
        """ __getstate__(self: object) -> int """
        return 0

    def __hash__(self): # real signature unknown; restored from __doc__
        """ __hash__(self: object) -> int """
        return 0

    def __index__(self): # real signature unknown; restored from __doc__
        """ __index__(self: contourpy._contourpy.LineType) -> int """
        return 0

    def __init__(self, value): # real signature unknown; restored from __doc__
        """ __init__(self: contourpy._contourpy.LineType, value: int) -> None """
        pass

    def __int__(self): # real signature unknown; restored from __doc__
        """ __int__(self: contourpy._contourpy.LineType) -> int """
        return 0

    def __ne__(self, other): # real signature unknown; restored from __doc__
        """ __ne__(self: object, other: object) -> bool """
        return False

    def __repr__(self): # real signature unknown; restored from __doc__
        """ __repr__(self: object) -> str """
        return ""

    def __setstate__(self, state): # real signature unknown; restored from __doc__
        """ __setstate__(self: contourpy._contourpy.LineType, state: int) -> None """
        pass

    def __str__(self): # real signature unknown; restored from __doc__
        """ __str__(self: object) -> str """
        return ""

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """name(self: object) -> str
"""

    value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    ChunkCombinedCode = None # (!) forward: ChunkCombinedCode, real value is '<LineType.ChunkCombinedCode: 103>'
    ChunkCombinedNan = None # (!) forward: ChunkCombinedNan, real value is '<LineType.ChunkCombinedNan: 105>'
    ChunkCombinedOffset = None # (!) forward: ChunkCombinedOffset, real value is '<LineType.ChunkCombinedOffset: 104>'
    Separate = None # (!) forward: Separate, real value is '<LineType.Separate: 101>'
    SeparateCode = None # (!) forward: SeparateCode, real value is '<LineType.SeparateCode: 102>'
    __entries = {
        'ChunkCombinedCode': (
            None, # (!) forward: ChunkCombinedCode, real value is '<LineType.ChunkCombinedCode: 103>'
            None,
        ),
        'ChunkCombinedNan': (
            None, # (!) forward: ChunkCombinedNan, real value is '<LineType.ChunkCombinedNan: 105>'
            None,
        ),
        'ChunkCombinedOffset': (
            None, # (!) forward: ChunkCombinedOffset, real value is '<LineType.ChunkCombinedOffset: 104>'
            None,
        ),
        'Separate': (
            None, # (!) forward: Separate, real value is '<LineType.Separate: 101>'
            None,
        ),
        'SeparateCode': (
            None, # (!) forward: SeparateCode, real value is '<LineType.SeparateCode: 102>'
            None,
        ),
    }
    __members__ = {
        'ChunkCombinedCode': None, # (!) forward: ChunkCombinedCode, real value is '<LineType.ChunkCombinedCode: 103>'
        'ChunkCombinedNan': None, # (!) forward: ChunkCombinedNan, real value is '<LineType.ChunkCombinedNan: 105>'
        'ChunkCombinedOffset': None, # (!) forward: ChunkCombinedOffset, real value is '<LineType.ChunkCombinedOffset: 104>'
        'Separate': None, # (!) forward: Separate, real value is '<LineType.Separate: 101>'
        'SeparateCode': None, # (!) forward: SeparateCode, real value is '<LineType.SeparateCode: 102>'
    }


class Mpl2005ContourGenerator(ContourGenerator):
    """
    ContourGenerator corresponding to ``name="mpl2005"``.
    
    This is the original 2005 Matplotlib algorithm. Does not support any of ``corner_mask``, ``quad_as_tri``, ``threads`` or ``z_interp``. Only supports ``line_type=LineType.SeparateCode`` and ``fill_type=FillType.OuterCode``. Only supports chunking for filled contours, not contour lines.
    
    .. warning::
       This algorithm is in ``contourpy`` for historic comparison. No new features or bug fixes will be added to it, except for security-related bug fixes.
    """
    def create_contour(self, arg0): # real signature unknown; restored from __doc__
        """
        create_contour(self: contourpy._contourpy.Mpl2005ContourGenerator, arg0: float) -> tuple
        
        Synonym for :func:`~contourpy.ContourGenerator.lines` to provide backward compatibility with Matplotlib.
        """
        return ()

    def create_filled_contour(self, arg0, arg1): # real signature unknown; restored from __doc__
        """
        create_filled_contour(self: contourpy._contourpy.Mpl2005ContourGenerator, arg0: float, arg1: float) -> tuple
        
        Synonym for :func:`~contourpy.ContourGenerator.filled` to provide backward compatibility with Matplotlib.
        """
        return ()

    def filled(self, arg0, arg1): # real signature unknown; restored from __doc__
        """
        filled(self: contourpy._contourpy.Mpl2005ContourGenerator, arg0: float, arg1: float) -> tuple
        
        Calculate and return filled contours between two levels.
        
        Args:
            lower_level (float): Lower z-level of the filled contours.
            upper_level (float): Upper z-level of the filled contours.
        Return:
            Filled contour polygons as one or more sequences of numpy arrays. The exact format is determined by the ``fill_type`` used by the ``ContourGenerator``.
        
        Raises a ``ValueError`` if ``lower_level >= upper_level``.
        
        To return filled contours below a ``level`` use ``filled(-np.inf, level)``.
        To return filled contours above a ``level`` use ``filled(level, np.inf)``
        """
        return ()

    def lines(self, arg0): # real signature unknown; restored from __doc__
        """
        lines(self: contourpy._contourpy.Mpl2005ContourGenerator, arg0: float) -> tuple
        
        Calculate and return contour lines at a particular level.
        
        Args:
            level (float): z-level to calculate contours at.
        
        Return:
            Contour lines (open line strips and closed line loops) as one or more sequences of numpy arrays. The exact format is determined by the ``line_type`` used by the ``ContourGenerator``.
        """
        return ()

    def supports_fill_type(self, arg0): # real signature unknown; restored from __doc__
        """
        supports_fill_type(arg0: contourpy._contourpy.FillType) -> bool
        
        Return whether this algorithm supports a particular ``FillType``.
        """
        return False

    def supports_line_type(self, arg0): # real signature unknown; restored from __doc__
        """
        supports_line_type(arg0: contourpy._contourpy.LineType) -> bool
        
        Return whether this algorithm supports a particular ``LineType``.
        """
        return False

    def __init__(self, x, numpy_float64=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ __init__(self: contourpy._contourpy.Mpl2005ContourGenerator, x: numpy.ndarray[numpy.float64], y: numpy.ndarray[numpy.float64], z: numpy.ndarray[numpy.float64], mask: numpy.ndarray[bool], *, x_chunk_size: int = 0, y_chunk_size: int = 0) -> None """
        pass

    chunk_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Return tuple of (y, x) chunk counts."""

    chunk_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Return tuple of (y, x) chunk sizes."""

    fill_type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Return the ``FillType``."""

    line_type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Return the ``LineType``."""


    default_fill_type = None # (!) real value is '<FillType.OuterCode: 201>'
    default_line_type = None # (!) real value is '<LineType.SeparateCode: 102>'


class Mpl2014ContourGenerator(ContourGenerator):
    """
    ContourGenerator corresponding to ``name="mpl2014"``.
    
    This is the 2014 Matplotlib algorithm, a replacement of the original 2005 algorithm that added ``corner_mask`` and made the code more maintainable. Only supports ``corner_mask``, does not support ``quad_as_tri``, ``threads`` or ``z_interp``. 
    Only supports ``line_type=LineType.SeparateCode`` and ``fill_type=FillType.OuterCode``.
    
    .. warning::
       This algorithm is in ``contourpy`` for historic comparison. No new features or bug fixes will be added to it, except for security-related bug fixes.
    """
    def create_contour(self, arg0): # real signature unknown; restored from __doc__
        """
        create_contour(self: contourpy._contourpy.Mpl2014ContourGenerator, arg0: float) -> tuple
        
        Synonym for :func:`~contourpy.ContourGenerator.lines` to provide backward compatibility with Matplotlib.
        """
        return ()

    def create_filled_contour(self, arg0, arg1): # real signature unknown; restored from __doc__
        """
        create_filled_contour(self: contourpy._contourpy.Mpl2014ContourGenerator, arg0: float, arg1: float) -> tuple
        
        Synonym for :func:`~contourpy.ContourGenerator.filled` to provide backward compatibility with Matplotlib.
        """
        return ()

    def filled(self, arg0, arg1): # real signature unknown; restored from __doc__
        """
        filled(self: contourpy._contourpy.Mpl2014ContourGenerator, arg0: float, arg1: float) -> tuple
        
        Calculate and return filled contours between two levels.
        
        Args:
            lower_level (float): Lower z-level of the filled contours.
            upper_level (float): Upper z-level of the filled contours.
        Return:
            Filled contour polygons as one or more sequences of numpy arrays. The exact format is determined by the ``fill_type`` used by the ``ContourGenerator``.
        
        Raises a ``ValueError`` if ``lower_level >= upper_level``.
        
        To return filled contours below a ``level`` use ``filled(-np.inf, level)``.
        To return filled contours above a ``level`` use ``filled(level, np.inf)``
        """
        return ()

    def lines(self, arg0): # real signature unknown; restored from __doc__
        """
        lines(self: contourpy._contourpy.Mpl2014ContourGenerator, arg0: float) -> tuple
        
        Calculate and return contour lines at a particular level.
        
        Args:
            level (float): z-level to calculate contours at.
        
        Return:
            Contour lines (open line strips and closed line loops) as one or more sequences of numpy arrays. The exact format is determined by the ``line_type`` used by the ``ContourGenerator``.
        """
        return ()

    def supports_corner_mask(self): # real signature unknown; restored from __doc__
        """
        supports_corner_mask() -> bool
        
        Return whether this algorithm supports ``corner_mask``.
        """
        return False

    def supports_fill_type(self, arg0): # real signature unknown; restored from __doc__
        """
        supports_fill_type(arg0: contourpy._contourpy.FillType) -> bool
        
        Return whether this algorithm supports a particular ``FillType``.
        """
        return False

    def supports_line_type(self, arg0): # real signature unknown; restored from __doc__
        """
        supports_line_type(arg0: contourpy._contourpy.LineType) -> bool
        
        Return whether this algorithm supports a particular ``LineType``.
        """
        return False

    def __init__(self, x, numpy_float64=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ __init__(self: contourpy._contourpy.Mpl2014ContourGenerator, x: numpy.ndarray[numpy.float64], y: numpy.ndarray[numpy.float64], z: numpy.ndarray[numpy.float64], mask: numpy.ndarray[bool], *, corner_mask: bool, x_chunk_size: int = 0, y_chunk_size: int = 0) -> None """
        pass

    chunk_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Return tuple of (y, x) chunk counts."""

    chunk_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Return tuple of (y, x) chunk sizes."""

    corner_mask = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Return whether ``corner_mask`` is set or not."""

    fill_type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Return the ``FillType``."""

    line_type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Return the ``LineType``."""


    default_fill_type = None # (!) real value is '<FillType.OuterCode: 201>'
    default_line_type = None # (!) real value is '<LineType.SeparateCode: 102>'


class SerialContourGenerator(ContourGenerator):
    """
    ContourGenerator corresponding to ``name="serial"``, the default algorithm for ``contourpy``.
    
    Supports ``corner_mask``, ``quad_as_tri`` and ``z_interp`` but not ``threads``. Supports all options for ``line_type`` and ``fill_type``.
    """
    def create_contour(self, arg0): # real signature unknown; restored from __doc__
        """
        create_contour(self: contourpy._contourpy.SerialContourGenerator, arg0: float) -> Sequence
        
        Synonym for :func:`~contourpy.ContourGenerator.lines` to provide backward compatibility with Matplotlib.
        """
        return ()

    def create_filled_contour(self, arg0, arg1): # real signature unknown; restored from __doc__
        """
        create_filled_contour(self: contourpy._contourpy.SerialContourGenerator, arg0: float, arg1: float) -> Sequence
        
        Synonym for :func:`~contourpy.ContourGenerator.filled` to provide backward compatibility with Matplotlib.
        """
        return ()

    def filled(self, arg0, arg1): # real signature unknown; restored from __doc__
        """
        filled(self: contourpy._contourpy.SerialContourGenerator, arg0: float, arg1: float) -> Sequence
        
        Calculate and return filled contours between two levels.
        
        Args:
            lower_level (float): Lower z-level of the filled contours.
            upper_level (float): Upper z-level of the filled contours.
        Return:
            Filled contour polygons as one or more sequences of numpy arrays. The exact format is determined by the ``fill_type`` used by the ``ContourGenerator``.
        
        Raises a ``ValueError`` if ``lower_level >= upper_level``.
        
        To return filled contours below a ``level`` use ``filled(-np.inf, level)``.
        To return filled contours above a ``level`` use ``filled(level, np.inf)``
        """
        return ()

    def lines(self, arg0): # real signature unknown; restored from __doc__
        """
        lines(self: contourpy._contourpy.SerialContourGenerator, arg0: float) -> Sequence
        
        Calculate and return contour lines at a particular level.
        
        Args:
            level (float): z-level to calculate contours at.
        
        Return:
            Contour lines (open line strips and closed line loops) as one or more sequences of numpy arrays. The exact format is determined by the ``line_type`` used by the ``ContourGenerator``.
        """
        return ()

    def supports_corner_mask(self): # real signature unknown; restored from __doc__
        """
        supports_corner_mask() -> bool
        
        Return whether this algorithm supports ``corner_mask``.
        """
        return False

    def supports_fill_type(self, arg0): # real signature unknown; restored from __doc__
        """
        supports_fill_type(arg0: contourpy._contourpy.FillType) -> bool
        
        Return whether this algorithm supports a particular ``FillType``.
        """
        return False

    def supports_line_type(self, arg0): # real signature unknown; restored from __doc__
        """
        supports_line_type(arg0: contourpy._contourpy.LineType) -> bool
        
        Return whether this algorithm supports a particular ``LineType``.
        """
        return False

    def supports_quad_as_tri(self): # real signature unknown; restored from __doc__
        """
        supports_quad_as_tri() -> bool
        
        Return whether this algorithm supports ``quad_as_tri``.
        """
        return False

    def supports_z_interp(self): # real signature unknown; restored from __doc__
        """
        supports_z_interp() -> bool
        
        Return whether this algorithm supports ``z_interp`` values other than ``ZInterp.Linear`` which all support.
        """
        return False

    def _write_cache(self): # real signature unknown; restored from __doc__
        """ _write_cache(self: contourpy._contourpy.SerialContourGenerator) -> None """
        pass

    def __init__(self, x, numpy_float64=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ __init__(self: contourpy._contourpy.SerialContourGenerator, x: numpy.ndarray[numpy.float64], y: numpy.ndarray[numpy.float64], z: numpy.ndarray[numpy.float64], mask: numpy.ndarray[bool], *, corner_mask: bool, line_type: contourpy._contourpy.LineType, fill_type: contourpy._contourpy.FillType, quad_as_tri: bool, z_interp: contourpy._contourpy.ZInterp, x_chunk_size: int = 0, y_chunk_size: int = 0) -> None """
        pass

    chunk_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Return tuple of (y, x) chunk counts."""

    chunk_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Return tuple of (y, x) chunk sizes."""

    corner_mask = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Return whether ``corner_mask`` is set or not."""

    fill_type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Return the ``FillType``."""

    line_type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Return the ``LineType``."""

    quad_as_tri = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Return whether ``quad_as_tri`` is set or not."""

    z_interp = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Return the ``ZInterp``."""


    default_fill_type = None # (!) real value is '<FillType.OuterOffset: 202>'
    default_line_type = None # (!) real value is '<LineType.Separate: 101>'


class ThreadedContourGenerator(ContourGenerator):
    """
    ContourGenerator corresponding to ``name="threaded"``, the multithreaded version of :class:`~contourpy._contourpy.SerialContourGenerator`.
    
    Supports ``corner_mask``, ``quad_as_tri`` and ``z_interp`` and ``threads``. Supports all options for ``line_type`` and ``fill_type``.
    """
    def create_contour(self, arg0): # real signature unknown; restored from __doc__
        """
        create_contour(self: contourpy._contourpy.ThreadedContourGenerator, arg0: float) -> Sequence
        
        Synonym for :func:`~contourpy.ContourGenerator.lines` to provide backward compatibility with Matplotlib.
        """
        return ()

    def create_filled_contour(self, arg0, arg1): # real signature unknown; restored from __doc__
        """
        create_filled_contour(self: contourpy._contourpy.ThreadedContourGenerator, arg0: float, arg1: float) -> Sequence
        
        Synonym for :func:`~contourpy.ContourGenerator.filled` to provide backward compatibility with Matplotlib.
        """
        return ()

    def filled(self, arg0, arg1): # real signature unknown; restored from __doc__
        """
        filled(self: contourpy._contourpy.ThreadedContourGenerator, arg0: float, arg1: float) -> Sequence
        
        Calculate and return filled contours between two levels.
        
        Args:
            lower_level (float): Lower z-level of the filled contours.
            upper_level (float): Upper z-level of the filled contours.
        Return:
            Filled contour polygons as one or more sequences of numpy arrays. The exact format is determined by the ``fill_type`` used by the ``ContourGenerator``.
        
        Raises a ``ValueError`` if ``lower_level >= upper_level``.
        
        To return filled contours below a ``level`` use ``filled(-np.inf, level)``.
        To return filled contours above a ``level`` use ``filled(level, np.inf)``
        """
        return ()

    def lines(self, arg0): # real signature unknown; restored from __doc__
        """
        lines(self: contourpy._contourpy.ThreadedContourGenerator, arg0: float) -> Sequence
        
        Calculate and return contour lines at a particular level.
        
        Args:
            level (float): z-level to calculate contours at.
        
        Return:
            Contour lines (open line strips and closed line loops) as one or more sequences of numpy arrays. The exact format is determined by the ``line_type`` used by the ``ContourGenerator``.
        """
        return ()

    def supports_corner_mask(self): # real signature unknown; restored from __doc__
        """
        supports_corner_mask() -> bool
        
        Return whether this algorithm supports ``corner_mask``.
        """
        return False

    def supports_fill_type(self, arg0): # real signature unknown; restored from __doc__
        """
        supports_fill_type(arg0: contourpy._contourpy.FillType) -> bool
        
        Return whether this algorithm supports a particular ``FillType``.
        """
        return False

    def supports_line_type(self, arg0): # real signature unknown; restored from __doc__
        """
        supports_line_type(arg0: contourpy._contourpy.LineType) -> bool
        
        Return whether this algorithm supports a particular ``LineType``.
        """
        return False

    def supports_quad_as_tri(self): # real signature unknown; restored from __doc__
        """
        supports_quad_as_tri() -> bool
        
        Return whether this algorithm supports ``quad_as_tri``.
        """
        return False

    def supports_threads(self): # real signature unknown; restored from __doc__
        """
        supports_threads() -> bool
        
        Return whether this algorithm supports the use of threads.
        """
        return False

    def supports_z_interp(self): # real signature unknown; restored from __doc__
        """
        supports_z_interp() -> bool
        
        Return whether this algorithm supports ``z_interp`` values other than ``ZInterp.Linear`` which all support.
        """
        return False

    def _write_cache(self): # real signature unknown; restored from __doc__
        """ _write_cache(self: contourpy._contourpy.ThreadedContourGenerator) -> None """
        pass

    def __init__(self, x, numpy_float64=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ __init__(self: contourpy._contourpy.ThreadedContourGenerator, x: numpy.ndarray[numpy.float64], y: numpy.ndarray[numpy.float64], z: numpy.ndarray[numpy.float64], mask: numpy.ndarray[bool], *, corner_mask: bool, line_type: contourpy._contourpy.LineType, fill_type: contourpy._contourpy.FillType, quad_as_tri: bool, z_interp: contourpy._contourpy.ZInterp, x_chunk_size: int = 0, y_chunk_size: int = 0, thread_count: int = 0) -> None """
        pass

    chunk_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Return tuple of (y, x) chunk counts."""

    chunk_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Return tuple of (y, x) chunk sizes."""

    corner_mask = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Return whether ``corner_mask`` is set or not."""

    fill_type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Return the ``FillType``."""

    line_type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Return the ``LineType``."""

    quad_as_tri = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Return whether ``quad_as_tri`` is set or not."""

    thread_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Return the number of threads used."""

    z_interp = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Return the ``ZInterp``."""


    default_fill_type = None # (!) real value is '<FillType.OuterOffset: 202>'
    default_line_type = None # (!) real value is '<LineType.Separate: 101>'


class ZInterp(__pybind11_builtins.pybind11_object):
    """
    Enum used for ``z_interp`` keyword argument in :func:`~contourpy.contour_generator`
    
    This controls the interpolation used on ``z`` values to determine where contour lines intersect the edges of grid quads, and ``z`` values at quad centres.
    
    Members:
    
      Linear
    
      Log
    """
    def __eq__(self, other): # real signature unknown; restored from __doc__
        """ __eq__(self: object, other: object) -> bool """
        return False

    def __getstate__(self): # real signature unknown; restored from __doc__
        """ __getstate__(self: object) -> int """
        return 0

    def __hash__(self): # real signature unknown; restored from __doc__
        """ __hash__(self: object) -> int """
        return 0

    def __index__(self): # real signature unknown; restored from __doc__
        """ __index__(self: contourpy._contourpy.ZInterp) -> int """
        return 0

    def __init__(self, value): # real signature unknown; restored from __doc__
        """ __init__(self: contourpy._contourpy.ZInterp, value: int) -> None """
        pass

    def __int__(self): # real signature unknown; restored from __doc__
        """ __int__(self: contourpy._contourpy.ZInterp) -> int """
        return 0

    def __ne__(self, other): # real signature unknown; restored from __doc__
        """ __ne__(self: object, other: object) -> bool """
        return False

    def __repr__(self): # real signature unknown; restored from __doc__
        """ __repr__(self: object) -> str """
        return ""

    def __setstate__(self, state): # real signature unknown; restored from __doc__
        """ __setstate__(self: contourpy._contourpy.ZInterp, state: int) -> None """
        pass

    def __str__(self): # real signature unknown; restored from __doc__
        """ __str__(self: object) -> str """
        return ""

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """name(self: object) -> str
"""

    value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    Linear = None # (!) forward: Linear, real value is '<ZInterp.Linear: 1>'
    Log = None # (!) forward: Log, real value is '<ZInterp.Log: 2>'
    __entries = {
        'Linear': (
            None, # (!) forward: Linear, real value is '<ZInterp.Linear: 1>'
            None,
        ),
        'Log': (
            None, # (!) forward: Log, real value is '<ZInterp.Log: 2>'
            None,
        ),
    }
    __members__ = {
        'Linear': None, # (!) forward: Linear, real value is '<ZInterp.Linear: 1>'
        'Log': None, # (!) forward: Log, real value is '<ZInterp.Log: 2>'
    }


# variables with complex values

ChunkCombinedCode = None # (!) real value is '<LineType.ChunkCombinedCode: 103>'

ChunkCombinedCodeOffset = None # (!) real value is '<FillType.ChunkCombinedCodeOffset: 205>'

ChunkCombinedNan = None # (!) real value is '<LineType.ChunkCombinedNan: 105>'

ChunkCombinedOffset = None # (!) real value is '<LineType.ChunkCombinedOffset: 104>'

ChunkCombinedOffsetOffset = None # (!) real value is '<FillType.ChunkCombinedOffsetOffset: 206>'

Linear = None # (!) real value is '<ZInterp.Linear: 1>'

Log = None # (!) real value is '<ZInterp.Log: 2>'

OuterCode = None # (!) real value is '<FillType.OuterCode: 201>'

OuterOffset = None # (!) real value is '<FillType.OuterOffset: 202>'

Separate = None # (!) real value is '<LineType.Separate: 101>'

SeparateCode = None # (!) real value is '<LineType.SeparateCode: 102>'

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x00000175252EF690>'

__spec__ = None # (!) real value is "ModuleSpec(name='contourpy._contourpy', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x00000175252EF690>, origin='C:\\\\Users\\\\leonm\\\\PycharmProjects\\\\leonsystem\\\\venv\\\\Lib\\\\site-packages\\\\contourpy\\\\_contourpy.cp311-win_amd64.pyd')"

