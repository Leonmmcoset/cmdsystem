# encoding: utf-8
# module fontTools.qu2cu.qu2cu
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\fontTools\qu2cu\qu2cu.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import math as math # <module 'math' (built-in)>
from fontTools.misc.bezierTools import splitCubicAtTC


# Variables with simple values

COMPILED = True

# functions

def add_implicit_on_curves(p): # real signature unknown; restored from __doc__
    """ add_implicit_on_curves(p) """
    pass

def elevate_quadratic(double_complex_p0, double_complex_p1, double_complex_p2): # real signature unknown; restored from __doc__
    """
    elevate_quadratic(double complex p0, double complex p1, double complex p2)
    Given a quadratic bezier curve, return its degree-elevated cubic.
    """
    pass

def List(*args, **kwargs): # real signature unknown
    """ A generic version of list. """
    pass

def main(): # real signature unknown; restored from __doc__
    """ main() """
    pass

def namedtuple(typename, field_names, *, rename=False, defaults=None, module=None): # reliably restored by inspect
    """
    Returns a new subclass of tuple with named fields.
    
        >>> Point = namedtuple('Point', ['x', 'y'])
        >>> Point.__doc__                   # docstring for the new class
        'Point(x, y)'
        >>> p = Point(11, y=22)             # instantiate with positional args or keywords
        >>> p[0] + p[1]                     # indexable like a plain tuple
        33
        >>> x, y = p                        # unpack like a regular tuple
        >>> x, y
        (11, 22)
        >>> p.x + p.y                       # fields also accessible by name
        33
        >>> d = p._asdict()                 # convert to a dictionary
        >>> d['x']
        11
        >>> Point(**d)                      # convert from a dictionary
        Point(x=11, y=22)
        >>> p._replace(x=100)               # _replace() is like str.replace() but targets named fields
        Point(x=100, y=22)
    """
    pass

def Point(*args, **kwargs): # real signature unknown
    pass

def quadratic_to_curves(list_quads, List=None, Point=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    quadratic_to_curves(list quads: List[List[Point]], double max_err: float = 0.5, all_cubic: bool = False) -> List[Tuple[Point, ...]]
    Converts a connecting list of quadratic splines to a list of quadratic
        and cubic curves.
    
        A quadratic spline is specified as a list of points.  Either each point is
        a 2-tuple of X,Y coordinates, or each point is a complex number with
        real/imaginary components representing X,Y coordinates.
    
        The first and last points are on-curve points and the rest are off-curve
        points, with an implied on-curve point in the middle between every two
        consequtive off-curve points.
    
        Returns:
            The output is a list of tuples of points. Points are represented
            in the same format as the input, either as 2-tuples or complex numbers.
    
            Each tuple is either of length three, for a quadratic curve, or four,
            for a cubic curve.  Each curve's last point is the same as the next
            curve's first point.
    
        Args:
            quads: quadratic splines
    
            max_err: absolute error tolerance; defaults to 0.5
    
            all_cubic: if True, only cubic curves are generated; defaults to False
    """
    pass

def spline_to_curves(q, costs, double_tolerance=0.5, int_all_cubic=False): # real signature unknown; restored from __doc__
    """
    spline_to_curves(q, costs, double tolerance=0.5, int all_cubic=False)
    
        q: quadratic spline with alternating on-curve / off-curve points.
    
        costs: cumulative list of encoding cost of q in terms of number of
          points that need to be encoded.  Implied on-curve points do not
          contribute to the cost. If all points need to be encoded, then
          costs will be range(1, len(q)+1).
    """
    pass

def Tuple(*args, **kwargs): # real signature unknown
    """
    Deprecated alias to builtins.tuple.
    
        Tuple[X, Y] is the cross-product type of X and Y.
    
        Example: Tuple[T1, T2] is a tuple of two elements corresponding
        to type variables T1 and T2.  Tuple[int, float, str] is a tuple
        of an int, a float and a string.
    
        To specify a variable-length tuple of homogeneous type, use Tuple[T, ...].
    """
    pass

def Union(*args, **kwargs): # real signature unknown
    """
    Union type; Union[X, Y] means either X or Y.
    
        On Python 3.10 and higher, the | operator
        can also be used to denote unions;
        X | Y means the same thing to the type checker as Union[X, Y].
    
        To define a union, use e.g. Union[int, str]. Details:
        - The arguments must be types and there must be at least one.
        - None as an argument is a special case and is replaced by
          type(None).
        - Unions of unions are flattened, e.g.::
    
            assert Union[Union[int, str], float] == Union[int, str, float]
    
        - Unions of a single argument vanish, e.g.::
    
            assert Union[int] == int  # The constructor actually returns int
    
        - Redundant arguments are skipped, e.g.::
    
            assert Union[int, str, int] == Union[int, str]
    
        - When comparing unions, the argument order is ignored, e.g.::
    
            assert Union[int, str] == Union[str, int]
    
        - You cannot subclass or instantiate a union.
        - You can use Optional[X] as a shorthand for Union[X, None].
    """
    pass

# classes

class Solution(tuple):
    """ Solution(num_points, error, start_index, is_cubic) """
    def _asdict(self): # reliably restored by inspect
        """ Return a new dict which maps field names to their values. """
        pass

    @classmethod
    def _make(cls, *args, **kwargs): # real signature unknown
        """ Make a new Solution object from a sequence or iterable """
        pass

    def _replace(self, **kwds): # reliably restored by inspect
        """ Return a new Solution object replacing specified fields with new values """
        pass

    def __getnewargs__(self): # reliably restored by inspect
        """ Return self as a plain tuple.  Used by copy and pickle. """
        pass

    def __init__(self, num_points, error, start_index, is_cubic): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(_cls, num_points, error, start_index, is_cubic): # reliably restored by inspect
        """ Create new instance of Solution(num_points, error, start_index, is_cubic) """
        pass

    def __repr__(self): # reliably restored by inspect
        """ Return a nicely formatted representation string """
        pass

    error = _tuplegetter(1, 'Alias for field number 1')
    is_cubic = _tuplegetter(3, 'Alias for field number 3')
    num_points = _tuplegetter(0, 'Alias for field number 0')
    start_index = _tuplegetter(2, 'Alias for field number 2')
    _fields = (
        'num_points',
        'error',
        'start_index',
        'is_cubic',
    )
    _field_defaults = {}
    __match_args__ = (
        'num_points',
        'error',
        'start_index',
        'is_cubic',
    )
    __slots__ = ()


# variables with complex values

__all__ = [
    'quadratic_to_curves',
]

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x000002D184D6E910>'

__spec__ = None # (!) real value is "ModuleSpec(name='fontTools.qu2cu.qu2cu', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x000002D184D6E910>, origin='C:\\\\Users\\\\leonm\\\\PycharmProjects\\\\leonsystem\\\\venv\\\\Lib\\\\site-packages\\\\fontTools\\\\qu2cu\\\\qu2cu.cp311-win_amd64.pyd')"

__test__ = {}

