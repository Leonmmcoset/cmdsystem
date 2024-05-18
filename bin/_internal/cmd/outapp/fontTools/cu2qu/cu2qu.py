# encoding: utf-8
# module fontTools.cu2qu.cu2qu
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\fontTools\cu2qu\cu2qu.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import math as math # <module 'math' (built-in)>
import fontTools.cu2qu.errors as __fontTools_cu2qu_errors


# Variables with simple values

COMPILED = True

MAX_N = 100

NAN = nan

# functions

def curves_to_quadratic(curves, max_errors, int_all_quadratic=True): # real signature unknown; restored from __doc__
    """
    curves_to_quadratic(curves, max_errors, int all_quadratic=True)
    Return quadratic Bezier splines approximating the input cubic Beziers.
    
        Args:
            curves: A sequence of *n* curves, each curve being a sequence of four
                2D tuples.
            max_errors: A sequence of *n* floats representing the maximum permissible
                deviation from each of the cubic Bezier curves.
            all_quadratic (bool): If True (default) returned values are a
                quadratic spline. If False, they are either a single quadratic
                curve or a single cubic curve.
    
        Example::
    
            >>> curves_to_quadratic( [
            ...   [ (50,50), (100,100), (150,100), (200,50) ],
            ...   [ (75,50), (120,100), (150,75),  (200,60) ]
            ... ], [1,1] )
            [[(50.0, 50.0), (75.0, 75.0), (125.0, 91.66666666666666), (175.0, 75.0), (200.0, 50.0)], [(75.0, 50.0), (97.5, 75.0), (135.41666666666666, 82.08333333333333), (175.0, 67.5), (200.0, 60.0)]]
    
        The returned splines have "implied oncurve points" suitable for use in
        TrueType ``glif`` outlines - i.e. in the first spline returned above,
        the first quadratic segment runs from (50,50) to
        ( (75 + 125)/2 , (120 + 91.666..)/2 ) = (100, 83.333...).
    
        Returns:
            If all_quadratic is True, a list of splines, each spline being a list
            of 2D tuples.
    
            If all_quadratic is False, a list of curves, each curve being a quadratic
            (length 3), or cubic (length 4).
    
        Raises:
            fontTools.cu2qu.Errors.ApproxNotFoundError: if no suitable approximation
            can be found for all curves with the given parameters.
    """
    pass

def curve_to_quadratic(curve, double_max_err, int_all_quadratic=True): # real signature unknown; restored from __doc__
    """
    curve_to_quadratic(curve, double max_err, int all_quadratic=True)
    Approximate a cubic Bezier curve with a spline of n quadratics.
    
        Args:
            cubic (sequence): Four 2D tuples representing control points of
                the cubic Bezier curve.
            max_err (double): Permitted deviation from the original curve.
            all_quadratic (bool): If True (default) returned value is a
                quadratic spline. If False, it's either a single quadratic
                curve or a single cubic curve.
    
        Returns:
            If all_quadratic is True: A list of 2D tuples, representing
            control points of the quadratic spline if it fits within the
            given tolerance, or ``None`` if no suitable spline could be
            calculated.
    
            If all_quadratic is False: Either a quadratic curve (if length
            of output is 3), or a cubic curve (if length of output is 4).
    """
    pass

def _split_cubic_into_n_gen(double_complex_p0, double_complex_p1, double_complex_p2, double_complex_p3, int_n): # real signature unknown; restored from __doc__
    """ _split_cubic_into_n_gen(double complex p0, double complex p1, double complex p2, double complex p3, int n) """
    pass

# classes

class Cu2QuError(Exception):
    """ Base Cu2Qu exception class for all other errors. """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class ApproxNotFoundError(__fontTools_cu2qu_errors.Error):
    # no doc
    def __init__(self, curve): # reliably restored by inspect
        # no doc
        pass


# variables with complex values

__all__ = [
    'curve_to_quadratic',
    'curves_to_quadratic',
]

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x000001848292E910>'

__spec__ = None # (!) real value is "ModuleSpec(name='fontTools.cu2qu.cu2qu', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x000001848292E910>, origin='C:\\\\Users\\\\leonm\\\\PycharmProjects\\\\leonsystem\\\\venv\\\\Lib\\\\site-packages\\\\fontTools\\\\cu2qu\\\\cu2qu.cp311-win_amd64.pyd')"

__test__ = {
    'curves_to_quadratic (line 474)': 'Return quadratic Bezier splines approximating the input cubic Beziers.\n\n    Args:\n        curves: A sequence of *n* curves, each curve being a sequence of four\n            2D tuples.\n        max_errors: A sequence of *n* floats representing the maximum permissible\n            deviation from each of the cubic Bezier curves.\n        all_quadratic (bool): If True (default) returned values are a\n            quadratic spline. If False, they are either a single quadratic\n            curve or a single cubic curve.\n\n    Example::\n\n        >>> curves_to_quadratic( [\n        ...   [ (50,50), (100,100), (150,100), (200,50) ],\n        ...   [ (75,50), (120,100), (150,75),  (200,60) ]\n        ... ], [1,1] )\n        [[(50.0, 50.0), (75.0, 75.0), (125.0, 91.66666666666666), (175.0, 75.0), (200.0, 50.0)], [(75.0, 50.0), (97.5, 75.0), (135.41666666666666, 82.08333333333333), (175.0, 67.5), (200.0, 60.0)]]\n\n    The returned splines have "implied oncurve points" suitable for use in\n    TrueType ``glif`` outlines - i.e. in the first spline returned above,\n    the first quadratic segment runs from (50,50) to\n    ( (75 + 125)/2 , (120 + 91.666..)/2 ) = (100, 83.333...).\n\n    Returns:\n        If all_quadratic is True, a list of splines, each spline being a list\n        of 2D tuples.\n\n        If all_quadratic is False, a list of curves, each curve being a quadratic\n        (length 3), or cubic (length 4).\n\n    Raises:\n        fontTools.cu2qu.Errors.ApproxNotFoundError: if no suitable approximation\n        can be found for all curves with the given parameters.\n    ',
}

