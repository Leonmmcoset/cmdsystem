# encoding: utf-8
# module fontTools.varLib.iup
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\fontTools\varLib\iup.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import numbers as __numbers


# Variables with simple values

COMPILED = True

MAX_LOOKBACK = 8

# functions

def iup_contour(deltas, coords): # real signature unknown; restored from __doc__
    """
    iup_contour(deltas: _DeltaOrNoneSegment, coords: _PointSegment) -> _DeltaSegment
    For the contour given in `coords`, interpolate any missing
        delta values in delta vector `deltas`.
    
        Returns fully filled-out delta vector.
    """
    pass

def iup_contour_optimize(deltas, coords, tolerance=0.0): # real signature unknown; restored from __doc__
    """
    iup_contour_optimize(deltas: _DeltaSegment, coords: _PointSegment, tolerance: Real = 0.0) -> _DeltaOrNoneSegment
    For contour with coordinates `coords`, optimize a set of delta
        values `deltas` within error `tolerance`.
    
        Returns delta vector that has most number of None items instead of
        the input delta.
    """
    pass

def iup_delta(deltas, coords, ends): # real signature unknown; restored from __doc__
    """
    iup_delta(deltas: _DeltaOrNoneSegment, coords: _PointSegment, ends: _Endpoints) -> _DeltaSegment
    For the outline given in `coords`, with contour endpoints given
        in sorted increasing order in `ends`, interpolate any missing
        delta values in delta vector `deltas`.
    
        Returns fully filled-out delta vector.
    """
    pass

def iup_delta_optimize(deltas, coords, ends, tolerance=0.0): # real signature unknown; restored from __doc__
    """
    iup_delta_optimize(deltas: _DeltaSegment, coords: _PointSegment, ends: _Endpoints, tolerance: Real = 0.0) -> _DeltaOrNoneSegment
    For the outline given in `coords`, with contour endpoints given
        in sorted increasing order in `ends`, optimize a set of delta
        values `deltas` within error `tolerance`.
    
        Returns delta vector that has most number of None items instead of
        the input delta.
    """
    pass

def Sequence(*args, **kwargs): # real signature unknown
    """ A generic version of collections.abc.Sequence. """
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

def _Delta(*args, **kwargs): # real signature unknown
    pass

def _DeltaOrNone(*args, **kwargs): # real signature unknown
    pass

def _DeltaOrNoneSegment(*args, **kwargs): # real signature unknown
    pass

def _DeltaSegment(*args, **kwargs): # real signature unknown
    pass

def _Endpoints(*args, **kwargs): # real signature unknown
    pass

def _iup_contour_bound_forced_set(deltas, coords, tolerance=0): # real signature unknown; restored from __doc__
    """
    _iup_contour_bound_forced_set(deltas: _DeltaSegment, coords: _PointSegment, tolerance: Real = 0) -> set
    The forced set is a conservative set of points on the contour that must be encoded
        explicitly (ie. cannot be interpolated).  Calculating this set allows for significantly
        speeding up the dynamic-programming, as well as resolve circularity in DP.
    
        The set is precise; that is, if an index is in the returned set, then there is no way
        that IUP can generate delta for that point, given `coords` and `deltas`.
    """
    return set(*(), **{})

def _iup_contour_optimize_dp(deltas, coords, set_forced=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    _iup_contour_optimize_dp(deltas: _DeltaSegment, coords: _PointSegment, set forced=set(), double tolerance: Real = 0, lookback: Integral = None)
    Straightforward Dynamic-Programming.  For each index i, find least-costly encoding of
        points 0 to i where i is explicitly encoded.  We find this by considering all previous
        explicit points j and check whether interpolation can fill points between j and i.
    
        Note that solution always encodes last point explicitly.  Higher-level is responsible
        for removing that restriction.
    
        As major speedup, we stop looking further whenever we see a "forced" point.
    """
    pass

def _Point(*args, **kwargs): # real signature unknown
    pass

def _PointSegment(*args, **kwargs): # real signature unknown
    pass

def _rot_list(list_l, int_k): # real signature unknown; restored from __doc__
    """
    _rot_list(list l: list, int k: int)
    Rotate list by k items forward.  Ie. item at position 0 will be
        at position k in returned list.  Negative k is allowed.
    """
    pass

def _rot_set(set_s, int_k, int_n): # real signature unknown; restored from __doc__
    """ _rot_set(set s: set, int k: int, int n: int) """
    pass

# classes

class Real(__numbers.Complex):
    """
    To Complex, Real adds the operations that work on real numbers.
    
        In short, those are: a conversion to float, trunc(), divmod,
        %, <, <=, >, and >=.
    
        Real also provides defaults for the derived operations.
    """
    def conjugate(self): # reliably restored by inspect
        """ Conjugate is a no-op for Reals. """
        pass

    def __ceil__(self): # reliably restored by inspect
        """ Finds the least Integral >= self. """
        pass

    def __complex__(self): # reliably restored by inspect
        """ complex(self) == complex(float(self), 0) """
        pass

    def __divmod__(self, other): # reliably restored by inspect
        """
        divmod(self, other): The pair (self // other, self % other).
        
                Sometimes this can be computed faster than the pair of
                operations.
        """
        pass

    def __float__(self): # reliably restored by inspect
        """
        Any Real can be converted to a native float object.
        
                Called for float(self).
        """
        pass

    def __floordiv__(self, other): # reliably restored by inspect
        """ self // other: The floor() of self/other. """
        pass

    def __floor__(self): # reliably restored by inspect
        """ Finds the greatest Integral <= self. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __le__(self, other): # reliably restored by inspect
        """ self <= other """
        pass

    def __lt__(self, other): # reliably restored by inspect
        """
        self < other
        
                < on Reals defines a total ordering, except perhaps for NaN.
        """
        pass

    def __mod__(self, other): # reliably restored by inspect
        """ self % other """
        pass

    def __rdivmod__(self, other): # reliably restored by inspect
        """
        divmod(other, self): The pair (self // other, self % other).
        
                Sometimes this can be computed faster than the pair of
                operations.
        """
        pass

    def __rfloordiv__(self, other): # reliably restored by inspect
        """ other // self: The floor() of other/self. """
        pass

    def __rmod__(self, other): # reliably restored by inspect
        """ other % self """
        pass

    def __round__(self, ndigits=None): # reliably restored by inspect
        """
        Rounds self to ndigits decimal places, defaulting to 0.
        
                If ndigits is omitted or None, returns an Integral, otherwise
                returns a Real. Rounds half toward even.
        """
        pass

    def __trunc__(self): # reliably restored by inspect
        """
        trunc(self): Truncates self to an Integral.
        
                Returns an Integral i such that:
                  * i>0 iff self>0;
                  * abs(i) <= abs(self);
                  * for any Integral j satisfying the first two conditions,
                    abs(i) >= abs(j) [i.e. i has "maximal" abs among those].
                i.e. "truncate towards 0".
        """
        pass

    imag = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Real numbers have no imaginary component."""

    real = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Real numbers are their real component."""


    _abc_impl = None # (!) real value is '<_abc._abc_data object at 0x000001BBD361BA40>'
    __abstractmethods__ = frozenset({'__float__', '__rmul__', '__eq__', '__le__', '__abs__', '__radd__', '__round__', '__lt__', '__rmod__', '__truediv__', '__pow__', '__rtruediv__', '__mul__', '__add__', '__mod__', '__floordiv__', '__rfloordiv__', '__neg__', '__rpow__', '__trunc__', '__ceil__', '__pos__', '__floor__'})
    __slots__ = ()


class Integral(__numbers.Rational):
    """
    Integral adds methods that work on integral numbers.
    
        In short, these are conversion to int, pow with modulus, and the
        bit-string operations.
    """
    def __and__(self, other): # reliably restored by inspect
        """ self & other """
        pass

    def __float__(self): # reliably restored by inspect
        """ float(self) == float(int(self)) """
        pass

    def __index__(self): # reliably restored by inspect
        """ Called whenever an index is needed, such as in slicing """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __int__(self): # reliably restored by inspect
        """ int(self) """
        pass

    def __invert__(self): # reliably restored by inspect
        """ ~self """
        pass

    def __lshift__(self, other): # reliably restored by inspect
        """ self << other """
        pass

    def __or__(self, other): # reliably restored by inspect
        """ self | other """
        pass

    def __pow__(self, exponent, modulus=None): # reliably restored by inspect
        """
        self ** exponent % modulus, but maybe faster.
        
                Accept the modulus argument if you want to support the
                3-argument version of pow(). Raise a TypeError if exponent < 0
                or any argument isn't Integral. Otherwise, just implement the
                2-argument version described in Complex.
        """
        pass

    def __rand__(self, other): # reliably restored by inspect
        """ other & self """
        pass

    def __rlshift__(self, other): # reliably restored by inspect
        """ other << self """
        pass

    def __ror__(self, other): # reliably restored by inspect
        """ other | self """
        pass

    def __rrshift__(self, other): # reliably restored by inspect
        """ other >> self """
        pass

    def __rshift__(self, other): # reliably restored by inspect
        """ self >> other """
        pass

    def __rxor__(self, other): # reliably restored by inspect
        """ other ^ self """
        pass

    def __xor__(self, other): # reliably restored by inspect
        """ self ^ other """
        pass

    denominator = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Integers have a denominator of 1."""

    numerator = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Integers are their own numerators."""


    _abc_impl = None # (!) real value is '<_abc._abc_data object at 0x000001BBD35F4400>'
    __abstractmethods__ = frozenset({'__rxor__', '__rmul__', '__eq__', '__le__', '__xor__', '__abs__', '__radd__', '__round__', '__invert__', '__lt__', '__rmod__', '__pow__', '__truediv__', '__rshift__', '__rrshift__', '__rtruediv__', '__mul__', '__add__', '__rlshift__', '__mod__', '__ror__', '__and__', '__rand__', '__floordiv__', '__rfloordiv__', '__neg__', '__rpow__', '__lshift__', '__int__', '__trunc__', '__or__', '__ceil__', '__pos__', '__floor__'})
    __slots__ = ()


# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x000001BBD3989910>'

__spec__ = None # (!) real value is "ModuleSpec(name='fontTools.varLib.iup', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x000001BBD3989910>, origin='C:\\\\Users\\\\leonm\\\\PycharmProjects\\\\leonsystem\\\\venv\\\\Lib\\\\site-packages\\\\fontTools\\\\varLib\\\\iup.cp311-win_amd64.pyd')"

__test__ = {}

