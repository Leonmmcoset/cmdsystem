# encoding: utf-8
# module fontTools.misc.bezierTools
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\fontTools\misc\bezierTools.cp311-win_amd64.pyd
# by generator 1.147
""" fontTools.misc.bezierTools.py -- tools for working with Bezier path segments. """

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import math as math # <module 'math' (built-in)>
from math import acos, cos, sqrt


# Variables with simple values

COMPILED = True

epsilon = 1e-10
epsilonDigits = 6

pi = 3.141592653589793

# functions

def approximateCubicArcLength(pt1, pt2, pt3, pt4): # real signature unknown; restored from __doc__
    """
    approximateCubicArcLength(pt1, pt2, pt3, pt4)
    Approximates the arc length for a cubic Bezier segment.
    
        Uses Gauss-Lobatto quadrature with n=5 points to approximate arc length.
        See :func:`calcCubicArcLength` for a slower but more accurate result.
    
        Args:
            pt1,pt2,pt3,pt4: Control points of the Bezier as 2D tuples.
    
        Returns:
            Arc length value.
    
        Example::
    
            >>> approximateCubicArcLength((0, 0), (25, 100), (75, 100), (100, 0))
            190.04332968932817
            >>> approximateCubicArcLength((0, 0), (50, 0), (100, 50), (100, 100))
            154.8852074945903
            >>> approximateCubicArcLength((0, 0), (50, 0), (100, 0), (150, 0)) # line; exact result should be 150.
            149.99999999999991
            >>> approximateCubicArcLength((0, 0), (50, 0), (100, 0), (-50, 0)) # cusp; exact result should be 150.
            136.9267662156362
            >>> approximateCubicArcLength((0, 0), (50, 0), (100, -50), (-50, 0)) # cusp
            154.80848416537057
    """
    pass

def approximateCubicArcLengthC(double_complex_pt1, double_complex_pt2, double_complex_pt3, double_complex_pt4): # real signature unknown; restored from __doc__
    """
    approximateCubicArcLengthC(double complex pt1, double complex pt2, double complex pt3, double complex pt4)
    Approximates the arc length for a cubic Bezier segment.
    
        Args:
            pt1,pt2,pt3,pt4: Control points of the Bezier as complex numbers.
    
        Returns:
            Arc length value.
    """
    pass

def approximateQuadraticArcLength(pt1, pt2, pt3): # real signature unknown; restored from __doc__
    """
    approximateQuadraticArcLength(pt1, pt2, pt3)
    Calculates the arc length for a quadratic Bezier segment.
    
        Uses Gauss-Legendre quadrature for a branch-free approximation.
        See :func:`calcQuadraticArcLength` for a slower but more accurate result.
    
        Args:
            pt1: Start point of the Bezier as 2D tuple.
            pt2: Handle point of the Bezier as 2D tuple.
            pt3: End point of the Bezier as 2D tuple.
    
        Returns:
            Approximate arc length value.
    """
    pass

def approximateQuadraticArcLengthC(double_complex_pt1, double_complex_pt2, double_complex_pt3): # real signature unknown; restored from __doc__
    """
    approximateQuadraticArcLengthC(double complex pt1, double complex pt2, double complex pt3)
    Calculates the arc length for a quadratic Bezier segment.
    
        Uses Gauss-Legendre quadrature for a branch-free approximation.
        See :func:`calcQuadraticArcLength` for a slower but more accurate result.
    
        Args:
            pt1: Start point of the Bezier as a complex number.
            pt2: Handle point of the Bezier as a complex number.
            pt3: End point of the Bezier as a complex number.
    
        Returns:
            Approximate arc length value.
    """
    pass

def calcBounds(array): # reliably restored by inspect
    """
    Calculate the bounding rectangle of a 2D points array.
    
        Args:
            array: A sequence of 2D tuples.
    
        Returns:
            A four-item tuple representing the bounding rectangle ``(xMin, yMin, xMax, yMax)``.
    """
    pass

def calcCubicArcLength(pt1, pt2, pt3, pt4, tolerance=0.005): # real signature unknown; restored from __doc__
    """
    calcCubicArcLength(pt1, pt2, pt3, pt4, tolerance=0.005)
    Calculates the arc length for a cubic Bezier segment.
    
        Whereas :func:`approximateCubicArcLength` approximates the length, this
        function calculates it by "measuring", recursively dividing the curve
        until the divided segments are shorter than ``tolerance``.
    
        Args:
            pt1,pt2,pt3,pt4: Control points of the Bezier as 2D tuples.
            tolerance: Controls the precision of the calcuation.
    
        Returns:
            Arc length value.
    """
    pass

def calcCubicArcLengthC(double_complex_pt1, double_complex_pt2, double_complex_pt3, double_complex_pt4, double_tolerance=0.005): # real signature unknown; restored from __doc__
    """
    calcCubicArcLengthC(double complex pt1, double complex pt2, double complex pt3, double complex pt4, double tolerance=0.005)
    Calculates the arc length for a cubic Bezier segment.
    
        Args:
            pt1,pt2,pt3,pt4: Control points of the Bezier as complex numbers.
            tolerance: Controls the precision of the calcuation.
    
        Returns:
            Arc length value.
    """
    pass

def calcCubicBounds(pt1, pt2, pt3, pt4): # real signature unknown; restored from __doc__
    """
    calcCubicBounds(pt1, pt2, pt3, pt4)
    Calculates the bounding rectangle for a quadratic Bezier segment.
    
        Args:
            pt1,pt2,pt3,pt4: Control points of the Bezier as 2D tuples.
    
        Returns:
            A four-item tuple representing the bounding rectangle ``(xMin, yMin, xMax, yMax)``.
    
        Example::
    
            >>> calcCubicBounds((0, 0), (25, 100), (75, 100), (100, 0))
            (0, 0, 100, 75.0)
            >>> calcCubicBounds((0, 0), (50, 0), (100, 50), (100, 100))
            (0.0, 0.0, 100, 100)
            >>> print("%f %f %f %f" % calcCubicBounds((50, 0), (0, 100), (100, 100), (50, 0)))
            35.566243 0.000000 64.433757 75.000000
    """
    pass

def calcCubicParameters(pt1, pt2, pt3, pt4): # real signature unknown; restored from __doc__
    """ calcCubicParameters(pt1, pt2, pt3, pt4) """
    pass

def calcCubicPoints(a, b, c, d): # real signature unknown; restored from __doc__
    """ calcCubicPoints(a, b, c, d) """
    pass

def calcQuadraticArcLength(pt1, pt2, pt3): # real signature unknown; restored from __doc__
    """
    calcQuadraticArcLength(pt1, pt2, pt3)
    Calculates the arc length for a quadratic Bezier segment.
    
        Args:
            pt1: Start point of the Bezier as 2D tuple.
            pt2: Handle point of the Bezier as 2D tuple.
            pt3: End point of the Bezier as 2D tuple.
    
        Returns:
            Arc length value.
    
        Example::
    
            >>> calcQuadraticArcLength((0, 0), (0, 0), (0, 0)) # empty segment
            0.0
            >>> calcQuadraticArcLength((0, 0), (50, 0), (80, 0)) # collinear points
            80.0
            >>> calcQuadraticArcLength((0, 0), (0, 50), (0, 80)) # collinear points vertical
            80.0
            >>> calcQuadraticArcLength((0, 0), (50, 20), (100, 40)) # collinear points
            107.70329614269008
            >>> calcQuadraticArcLength((0, 0), (0, 100), (100, 0))
            154.02976155645263
            >>> calcQuadraticArcLength((0, 0), (0, 50), (100, 0))
            120.21581243984076
            >>> calcQuadraticArcLength((0, 0), (50, -10), (80, 50))
            102.53273816445825
            >>> calcQuadraticArcLength((0, 0), (40, 0), (-40, 0)) # collinear points, control point outside
            66.66666666666667
            >>> calcQuadraticArcLength((0, 0), (40, 0), (0, 0)) # collinear points, looping back
            40.0
    """
    pass

def calcQuadraticArcLengthC(double_complex_pt1, double_complex_pt2, double_complex_pt3): # real signature unknown; restored from __doc__
    """
    calcQuadraticArcLengthC(double complex pt1, double complex pt2, double complex pt3)
    Calculates the arc length for a quadratic Bezier segment.
    
        Args:
            pt1: Start point of the Bezier as a complex number.
            pt2: Handle point of the Bezier as a complex number.
            pt3: End point of the Bezier as a complex number.
    
        Returns:
            Arc length value.
    """
    pass

def calcQuadraticBounds(pt1, pt2, pt3): # real signature unknown; restored from __doc__
    """
    calcQuadraticBounds(pt1, pt2, pt3)
    Calculates the bounding rectangle for a quadratic Bezier segment.
    
        Args:
            pt1: Start point of the Bezier as a 2D tuple.
            pt2: Handle point of the Bezier as a 2D tuple.
            pt3: End point of the Bezier as a 2D tuple.
    
        Returns:
            A four-item tuple representing the bounding rectangle ``(xMin, yMin, xMax, yMax)``.
    
        Example::
    
            >>> calcQuadraticBounds((0, 0), (50, 100), (100, 0))
            (0, 0, 100, 50.0)
            >>> calcQuadraticBounds((0, 0), (100, 0), (100, 100))
            (0.0, 0.0, 100, 100)
    """
    pass

def calcQuadraticParameters(pt1, pt2, pt3): # real signature unknown; restored from __doc__
    """ calcQuadraticParameters(pt1, pt2, pt3) """
    pass

def calcQuadraticPoints(a, b, c): # real signature unknown; restored from __doc__
    """ calcQuadraticPoints(a, b, c) """
    pass

def cubicPointAtT(pt1, pt2, pt3, pt4, t): # real signature unknown; restored from __doc__
    """
    cubicPointAtT(pt1, pt2, pt3, pt4, t)
    Finds the point at time `t` on a cubic curve.
    
        Args:
            pt1, pt2, pt3, pt4: Coordinates of the curve as 2D tuples.
            t: The time along the curve.
    
        Returns:
            A 2D tuple with the coordinates of the point.
    """
    pass

def cubicPointAtTC(double_complex_pt1, double_complex_pt2, double_complex_pt3, double_complex_pt4, double_t): # real signature unknown; restored from __doc__
    """
    cubicPointAtTC(double complex pt1, double complex pt2, double complex pt3, double complex pt4, double t)
    Finds the point at time `t` on a cubic curve.
    
        Args:
            pt1, pt2, pt3, pt4: Coordinates of the curve as complex numbers.
            t: The time along the curve.
    
        Returns:
            A complex number with the coordinates of the point.
    """
    pass

def curveCurveIntersections(curve1, curve2): # real signature unknown; restored from __doc__
    """
    curveCurveIntersections(curve1, curve2)
    Finds intersections between a curve and a curve.
    
        Args:
            curve1: List of coordinates of the first curve segment as 2D tuples.
            curve2: List of coordinates of the second curve segment as 2D tuples.
    
        Returns:
            A list of ``Intersection`` objects, each object having ``pt``, ``t1``
            and ``t2`` attributes containing the intersection point, time on first
            segment and time on second segment respectively.
    
        Examples::
            >>> curve1 = [ (10,100), (90,30), (40,140), (220,220) ]
            >>> curve2 = [ (5,150), (180,20), (80,250), (210,190) ]
            >>> intersections = curveCurveIntersections(curve1, curve2)
            >>> len(intersections)
            3
            >>> intersections[0].pt
            (81.7831487395506, 109.88904552375288)
    """
    pass

def curveLineIntersections(curve, line): # real signature unknown; restored from __doc__
    """
    curveLineIntersections(curve, line)
    Finds intersections between a curve and a line.
    
        Args:
            curve: List of coordinates of the curve segment as 2D tuples.
            line: List of coordinates of the line segment as 2D tuples.
    
        Returns:
            A list of ``Intersection`` objects, each object having ``pt``, ``t1``
            and ``t2`` attributes containing the intersection point, time on first
            segment and time on second segment respectively.
    
        Examples::
            >>> curve = [ (100, 240), (30, 60), (210, 230), (160, 30) ]
            >>> line  = [ (25, 260), (230, 20) ]
            >>> intersections = curveLineIntersections(curve, line)
            >>> len(intersections)
            3
            >>> intersections[0].pt
            (84.9000930760723, 189.87306176459828)
    """
    pass

def lineLineIntersections(s1, e1, s2, e2): # real signature unknown; restored from __doc__
    """
    lineLineIntersections(s1, e1, s2, e2)
    Finds intersections between two line segments.
    
        Args:
            s1, e1: Coordinates of the first line as 2D tuples.
            s2, e2: Coordinates of the second line as 2D tuples.
    
        Returns:
            A list of ``Intersection`` objects, each object having ``pt``, ``t1``
            and ``t2`` attributes containing the intersection point, time on first
            segment and time on second segment respectively.
    
        Examples::
    
            >>> a = lineLineIntersections( (310,389), (453, 222), (289, 251), (447, 367))
            >>> len(a)
            1
            >>> intersection = a[0]
            >>> intersection.pt
            (374.44882952482897, 313.73458370177315)
            >>> (intersection.t1, intersection.t2)
            (0.45069111555824465, 0.5408153767394238)
    """
    pass

def linePointAtT(pt1, pt2, t): # real signature unknown; restored from __doc__
    """
    linePointAtT(pt1, pt2, t)
    Finds the point at time `t` on a line.
    
        Args:
            pt1, pt2: Coordinates of the line as 2D tuples.
            t: The time along the line.
    
        Returns:
            A 2D tuple with the coordinates of the point.
    """
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

def printSegments(segments): # real signature unknown; restored from __doc__
    """
    printSegments(segments)
    Helper for the doctests, displaying each segment in a list of
        segments on a single line as a tuple.
    """
    pass

def quadraticPointAtT(pt1, pt2, pt3, t): # real signature unknown; restored from __doc__
    """
    quadraticPointAtT(pt1, pt2, pt3, t)
    Finds the point at time `t` on a quadratic curve.
    
        Args:
            pt1, pt2, pt3: Coordinates of the curve as 2D tuples.
            t: The time along the curve.
    
        Returns:
            A 2D tuple with the coordinates of the point.
    """
    pass

def rectArea(rect): # reliably restored by inspect
    """
    Determine rectangle area.
    
        Args:
            rect: Bounding rectangle, expressed as tuples
                ``(xMin, yMin, xMax, yMax)``.
    
        Returns:
            The area of the rectangle.
    """
    pass

def sectRect(rect1, rect2): # reliably restored by inspect
    """
    Test for rectangle-rectangle intersection.
    
        Args:
            rect1: First bounding rectangle, expressed as tuples
                ``(xMin, yMin, xMax, yMax)``.
            rect2: Second bounding rectangle.
    
        Returns:
            A boolean and a rectangle.
            If the input rectangles intersect, returns ``True`` and the intersecting
            rectangle. Returns ``False`` and ``(0, 0, 0, 0)`` if the input
            rectangles don't intersect.
    """
    pass

def segmentPointAtT(seg, t): # real signature unknown; restored from __doc__
    """ segmentPointAtT(seg, t) """
    pass

def segmentSegmentIntersections(seg1, seg2): # real signature unknown; restored from __doc__
    """
    segmentSegmentIntersections(seg1, seg2)
    Finds intersections between two segments.
    
        Args:
            seg1: List of coordinates of the first segment as 2D tuples.
            seg2: List of coordinates of the second segment as 2D tuples.
    
        Returns:
            A list of ``Intersection`` objects, each object having ``pt``, ``t1``
            and ``t2`` attributes containing the intersection point, time on first
            segment and time on second segment respectively.
    
        Examples::
            >>> curve1 = [ (10,100), (90,30), (40,140), (220,220) ]
            >>> curve2 = [ (5,150), (180,20), (80,250), (210,190) ]
            >>> intersections = segmentSegmentIntersections(curve1, curve2)
            >>> len(intersections)
            3
            >>> intersections[0].pt
            (81.7831487395506, 109.88904552375288)
            >>> curve3 = [ (100, 240), (30, 60), (210, 230), (160, 30) ]
            >>> line  = [ (25, 260), (230, 20) ]
            >>> intersections = segmentSegmentIntersections(curve3, line)
            >>> len(intersections)
            3
            >>> intersections[0].pt
            (84.9000930760723, 189.87306176459828)
    """
    pass

def solveCubic(a, b, c, d): # real signature unknown; restored from __doc__
    """
    solveCubic(a, b, c, d)
    Solve a cubic equation.
    
        Solves *a*x*x*x + b*x*x + c*x + d = 0* where a, b, c and d are real.
    
        Args:
            a: coefficient of *x³*
            b: coefficient of *x²*
            c: coefficient of *x*
            d: constant term
    
        Returns:
            A list of roots. Note that the returned list is neither guaranteed to
            be sorted nor to contain unique values!
    
        Examples::
    
            >>> solveCubic(1, 1, -6, 0)
            [-3.0, -0.0, 2.0]
            >>> solveCubic(-10.0, -9.0, 48.0, -29.0)
            [-2.9, 1.0, 1.0]
            >>> solveCubic(-9.875, -9.0, 47.625, -28.75)
            [-2.911392, 1.0, 1.0]
            >>> solveCubic(1.0, -4.5, 6.75, -3.375)
            [1.5, 1.5, 1.5]
            >>> solveCubic(-12.0, 18.0, -9.0, 1.50023651123)
            [0.5, 0.5, 0.5]
            >>> solveCubic(
            ...     9.0, 0.0, 0.0, -7.62939453125e-05
            ... ) == [-0.0, -0.0, -0.0]
            True
    """
    pass

def solveQuadratic(a, b, c, sqrt=None): # real signature unknown; restored from __doc__
    """
    solveQuadratic(a, b, c, sqrt=sqrt)
    Solve a quadratic equation.
    
        Solves *a*x*x + b*x + c = 0* where a, b and c are real.
    
        Args:
            a: coefficient of *x²*
            b: coefficient of *x*
            c: constant term
    
        Returns:
            A list of roots. Note that the returned list is neither guaranteed to
            be sorted nor to contain unique values!
    """
    pass

def splitCubic(pt1, pt2, pt3, pt4, where, isHorizontal): # real signature unknown; restored from __doc__
    """
    splitCubic(pt1, pt2, pt3, pt4, where, isHorizontal)
    Split a cubic Bezier curve at a given coordinate.
    
        Args:
            pt1,pt2,pt3,pt4: Control points of the Bezier as 2D tuples.
            where: Position at which to split the curve.
            isHorizontal: Direction of the ray splitting the curve. If true,
                ``where`` is interpreted as a Y coordinate; if false, then
                ``where`` is interpreted as an X coordinate.
    
        Returns:
            A list of two curve segments (each curve segment being four 2D tuples)
            if the curve was successfully split, or a list containing the original
            curve.
    
        Example::
    
            >>> printSegments(splitCubic((0, 0), (25, 100), (75, 100), (100, 0), 150, False))
            ((0, 0), (25, 100), (75, 100), (100, 0))
            >>> printSegments(splitCubic((0, 0), (25, 100), (75, 100), (100, 0), 50, False))
            ((0, 0), (12.5, 50), (31.25, 75), (50, 75))
            ((50, 75), (68.75, 75), (87.5, 50), (100, 0))
            >>> printSegments(splitCubic((0, 0), (25, 100), (75, 100), (100, 0), 25, True))
            ((0, 0), (2.29379, 9.17517), (4.79804, 17.5085), (7.47414, 25))
            ((7.47414, 25), (31.2886, 91.6667), (68.7114, 91.6667), (92.5259, 25))
            ((92.5259, 25), (95.202, 17.5085), (97.7062, 9.17517), (100, 1.77636e-15))
    """
    pass

def splitCubicAtT(pt1, pt2, pt3, pt4, *ts): # real signature unknown; restored from __doc__
    """
    splitCubicAtT(pt1, pt2, pt3, pt4, *ts)
    Split a cubic Bezier curve at one or more values of t.
    
        Args:
            pt1,pt2,pt3,pt4: Control points of the Bezier as 2D tuples.
            *ts: Positions at which to split the curve.
    
        Returns:
            A list of curve segments (each curve segment being four 2D tuples).
    
        Examples::
    
            >>> printSegments(splitCubicAtT((0, 0), (25, 100), (75, 100), (100, 0), 0.5))
            ((0, 0), (12.5, 50), (31.25, 75), (50, 75))
            ((50, 75), (68.75, 75), (87.5, 50), (100, 0))
            >>> printSegments(splitCubicAtT((0, 0), (25, 100), (75, 100), (100, 0), 0.5, 0.75))
            ((0, 0), (12.5, 50), (31.25, 75), (50, 75))
            ((50, 75), (59.375, 75), (68.75, 68.75), (77.3438, 56.25))
            ((77.3438, 56.25), (85.9375, 43.75), (93.75, 25), (100, 0))
    """
    pass

def splitCubicAtTC(double_complex_pt1, double_complex_pt2, double_complex_pt3, double_complex_pt4, *ts): # real signature unknown; restored from __doc__
    """
    splitCubicAtTC(double complex pt1, double complex pt2, double complex pt3, double complex pt4, *ts)
    Split a cubic Bezier curve at one or more values of t.
    
        Args:
            pt1,pt2,pt3,pt4: Control points of the Bezier as complex numbers..
            *ts: Positions at which to split the curve.
    
        Yields:
            Curve segments (each curve segment being four complex numbers).
    """
    pass

def splitCubicIntoTwoAtTC(double_complex_pt1, double_complex_pt2, double_complex_pt3, double_complex_pt4, double_t): # real signature unknown; restored from __doc__
    """
    splitCubicIntoTwoAtTC(double complex pt1, double complex pt2, double complex pt3, double complex pt4, double t)
    Split a cubic Bezier curve at t.
    
        Args:
            pt1,pt2,pt3,pt4: Control points of the Bezier as complex numbers.
            t: Position at which to split the curve.
    
        Returns:
            A tuple of two curve segments (each curve segment being four complex numbers).
    """
    pass

def splitLine(pt1, pt2, where, isHorizontal): # real signature unknown; restored from __doc__
    """
    splitLine(pt1, pt2, where, isHorizontal)
    Split a line at a given coordinate.
    
        Args:
            pt1: Start point of line as 2D tuple.
            pt2: End point of line as 2D tuple.
            where: Position at which to split the line.
            isHorizontal: Direction of the ray splitting the line. If true,
                ``where`` is interpreted as a Y coordinate; if false, then
                ``where`` is interpreted as an X coordinate.
    
        Returns:
            A list of two line segments (each line segment being two 2D tuples)
            if the line was successfully split, or a list containing the original
            line.
    
        Example::
    
            >>> printSegments(splitLine((0, 0), (100, 100), 50, True))
            ((0, 0), (50, 50))
            ((50, 50), (100, 100))
            >>> printSegments(splitLine((0, 0), (100, 100), 100, True))
            ((0, 0), (100, 100))
            >>> printSegments(splitLine((0, 0), (100, 100), 0, True))
            ((0, 0), (0, 0))
            ((0, 0), (100, 100))
            >>> printSegments(splitLine((0, 0), (100, 100), 0, False))
            ((0, 0), (0, 0))
            ((0, 0), (100, 100))
            >>> printSegments(splitLine((100, 0), (0, 0), 50, False))
            ((100, 0), (50, 0))
            ((50, 0), (0, 0))
            >>> printSegments(splitLine((0, 100), (0, 0), 50, True))
            ((0, 100), (0, 50))
            ((0, 50), (0, 0))
    """
    pass

def splitQuadratic(pt1, pt2, pt3, where, isHorizontal): # real signature unknown; restored from __doc__
    """
    splitQuadratic(pt1, pt2, pt3, where, isHorizontal)
    Split a quadratic Bezier curve at a given coordinate.
    
        Args:
            pt1,pt2,pt3: Control points of the Bezier as 2D tuples.
            where: Position at which to split the curve.
            isHorizontal: Direction of the ray splitting the curve. If true,
                ``where`` is interpreted as a Y coordinate; if false, then
                ``where`` is interpreted as an X coordinate.
    
        Returns:
            A list of two curve segments (each curve segment being three 2D tuples)
            if the curve was successfully split, or a list containing the original
            curve.
    
        Example::
    
            >>> printSegments(splitQuadratic((0, 0), (50, 100), (100, 0), 150, False))
            ((0, 0), (50, 100), (100, 0))
            >>> printSegments(splitQuadratic((0, 0), (50, 100), (100, 0), 50, False))
            ((0, 0), (25, 50), (50, 50))
            ((50, 50), (75, 50), (100, 0))
            >>> printSegments(splitQuadratic((0, 0), (50, 100), (100, 0), 25, False))
            ((0, 0), (12.5, 25), (25, 37.5))
            ((25, 37.5), (62.5, 75), (100, 0))
            >>> printSegments(splitQuadratic((0, 0), (50, 100), (100, 0), 25, True))
            ((0, 0), (7.32233, 14.6447), (14.6447, 25))
            ((14.6447, 25), (50, 75), (85.3553, 25))
            ((85.3553, 25), (92.6777, 14.6447), (100, -7.10543e-15))
            >>> # XXX I'm not at all sure if the following behavior is desirable:
            >>> printSegments(splitQuadratic((0, 0), (50, 100), (100, 0), 50, True))
            ((0, 0), (25, 50), (50, 50))
            ((50, 50), (50, 50), (50, 50))
            ((50, 50), (75, 50), (100, 0))
    """
    pass

def splitQuadraticAtT(pt1, pt2, pt3, *ts): # real signature unknown; restored from __doc__
    """
    splitQuadraticAtT(pt1, pt2, pt3, *ts)
    Split a quadratic Bezier curve at one or more values of t.
    
        Args:
            pt1,pt2,pt3: Control points of the Bezier as 2D tuples.
            *ts: Positions at which to split the curve.
    
        Returns:
            A list of curve segments (each curve segment being three 2D tuples).
    
        Examples::
    
            >>> printSegments(splitQuadraticAtT((0, 0), (50, 100), (100, 0), 0.5))
            ((0, 0), (25, 50), (50, 50))
            ((50, 50), (75, 50), (100, 0))
            >>> printSegments(splitQuadraticAtT((0, 0), (50, 100), (100, 0), 0.5, 0.75))
            ((0, 0), (25, 50), (50, 50))
            ((50, 50), (62.5, 50), (75, 37.5))
            ((75, 37.5), (87.5, 25), (100, 0))
    """
    pass

def _alignment_transformation(segment): # real signature unknown; restored from __doc__
    """ _alignment_transformation(segment) """
    pass

def _both_points_are_on_same_side_of_origin(a, b, origin): # real signature unknown; restored from __doc__
    """ _both_points_are_on_same_side_of_origin(a, b, origin) """
    pass

def _calcCubicArcLengthCRecurse(double_mult, double_complex_p0, double_complex_p1, double_complex_p2, double_complex_p3): # real signature unknown; restored from __doc__
    """ _calcCubicArcLengthCRecurse(double mult, double complex p0, double complex p1, double complex p2, double complex p3) """
    pass

def _curve_bounds(c): # real signature unknown; restored from __doc__
    """ _curve_bounds(c) """
    pass

def _curve_curve_intersections_t(curve1, curve2, precision=1, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """ _curve_curve_intersections_t(curve1, curve2, precision=1e-3, range1=None, range2=None) """
    pass

def _curve_line_intersections_t(curve, line): # real signature unknown; restored from __doc__
    """ _curve_line_intersections_t(curve, line) """
    pass

def _is_linelike(segment): # real signature unknown; restored from __doc__
    """ _is_linelike(segment) """
    pass

def _line_t_of_pt(s, e, pt): # real signature unknown; restored from __doc__
    """ _line_t_of_pt(s, e, pt) """
    pass

def _segmentrepr(obj): # real signature unknown; restored from __doc__
    """
    _segmentrepr(obj)
    
        >>> _segmentrepr([1, [2, 3], [], [[2, [3, 4], [0.1, 2.2]]]])
        '(1, (2, 3), (), ((2, (3, 4), (0.1, 2.2))))'
    """
    pass

def _splitCubicAtT(a, b, c, d, *ts): # real signature unknown; restored from __doc__
    """ _splitCubicAtT(a, b, c, d, *ts) """
    pass

def _splitCubicAtTC(double_complex_a, double_complex_b, double_complex_c, double_complex_d, *ts): # real signature unknown; restored from __doc__
    """ _splitCubicAtTC(double complex a, double complex b, double complex c, double complex d, *ts) """
    pass

def _splitQuadraticAtT(a, b, c, *ts): # real signature unknown; restored from __doc__
    """ _splitQuadraticAtT(a, b, c, *ts) """
    pass

def _split_cubic_into_two(p0, p1, p2, p3): # real signature unknown; restored from __doc__
    """ _split_cubic_into_two(p0, p1, p2, p3) """
    pass

def _split_segment_at_t(c, t): # real signature unknown; restored from __doc__
    """ _split_segment_at_t(c, t) """
    pass

# classes

class Intersection(tuple):
    """ Intersection(pt, t1, t2) """
    def _asdict(self): # reliably restored by inspect
        """ Return a new dict which maps field names to their values. """
        pass

    @classmethod
    def _make(cls, *args, **kwargs): # real signature unknown
        """ Make a new Intersection object from a sequence or iterable """
        pass

    def _replace(self, **kwds): # reliably restored by inspect
        """ Return a new Intersection object replacing specified fields with new values """
        pass

    def __getnewargs__(self): # reliably restored by inspect
        """ Return self as a plain tuple.  Used by copy and pickle. """
        pass

    def __init__(self, pt, t1, t2): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(_cls, pt, t1, t2): # reliably restored by inspect
        """ Create new instance of Intersection(pt, t1, t2) """
        pass

    def __repr__(self): # reliably restored by inspect
        """ Return a nicely formatted representation string """
        pass

    pt = _tuplegetter(0, 'Alias for field number 0')
    t1 = _tuplegetter(1, 'Alias for field number 1')
    t2 = _tuplegetter(2, 'Alias for field number 2')
    _fields = (
        'pt',
        't1',
        't2',
    )
    _field_defaults = {}
    __match_args__ = (
        'pt',
        't1',
        't2',
    )
    __slots__ = ()


# variables with complex values

Identity = (
    1,
    0,
    0,
    1,
    0,
    0,
)

__all__ = [
    'approximateCubicArcLength',
    'approximateCubicArcLengthC',
    'approximateQuadraticArcLength',
    'approximateQuadraticArcLengthC',
    'calcCubicArcLength',
    'calcCubicArcLengthC',
    'calcQuadraticArcLength',
    'calcQuadraticArcLengthC',
    'calcCubicBounds',
    'calcQuadraticBounds',
    'splitLine',
    'splitQuadratic',
    'splitCubic',
    'splitQuadraticAtT',
    'splitCubicAtT',
    'splitCubicAtTC',
    'splitCubicIntoTwoAtTC',
    'solveQuadratic',
    'solveCubic',
    'quadraticPointAtT',
    'cubicPointAtT',
    'cubicPointAtTC',
    'linePointAtT',
    'segmentPointAtT',
    'lineLineIntersections',
    'curveLineIntersections',
    'curveCurveIntersections',
    'segmentSegmentIntersections',
]

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x00000158B3E6E210>'

__spec__ = None # (!) real value is "ModuleSpec(name='fontTools.misc.bezierTools', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x00000158B3E6E210>, origin='C:\\\\Users\\\\leonm\\\\PycharmProjects\\\\leonsystem\\\\venv\\\\Lib\\\\site-packages\\\\fontTools\\\\misc\\\\bezierTools.cp311-win_amd64.pyd')"

__test__ = {
    '_segmentrepr (line 1465)': "\n    >>> _segmentrepr([1, [2, 3], [], [[2, [3, 4], [0.1, 2.2]]]])\n    '(1, (2, 3), (), ((2, (3, 4), (0.1, 2.2))))'\n    ",
    'approximateCubicArcLength (line 332)': 'Approximates the arc length for a cubic Bezier segment.\n\n    Uses Gauss-Lobatto quadrature with n=5 points to approximate arc length.\n    See :func:`calcCubicArcLength` for a slower but more accurate result.\n\n    Args:\n        pt1,pt2,pt3,pt4: Control points of the Bezier as 2D tuples.\n\n    Returns:\n        Arc length value.\n\n    Example::\n\n        >>> approximateCubicArcLength((0, 0), (25, 100), (75, 100), (100, 0))\n        190.04332968932817\n        >>> approximateCubicArcLength((0, 0), (50, 0), (100, 50), (100, 100))\n        154.8852074945903\n        >>> approximateCubicArcLength((0, 0), (50, 0), (100, 0), (150, 0)) # line; exact result should be 150.\n        149.99999999999991\n        >>> approximateCubicArcLength((0, 0), (50, 0), (100, 0), (-50, 0)) # cusp; exact result should be 150.\n        136.9267662156362\n        >>> approximateCubicArcLength((0, 0), (50, 0), (100, -50), (-50, 0)) # cusp\n        154.80848416537057\n    ',
    'calcCubicBounds (line 412)': 'Calculates the bounding rectangle for a quadratic Bezier segment.\n\n    Args:\n        pt1,pt2,pt3,pt4: Control points of the Bezier as 2D tuples.\n\n    Returns:\n        A four-item tuple representing the bounding rectangle ``(xMin, yMin, xMax, yMax)``.\n\n    Example::\n\n        >>> calcCubicBounds((0, 0), (25, 100), (75, 100), (100, 0))\n        (0, 0, 100, 75.0)\n        >>> calcCubicBounds((0, 0), (50, 0), (100, 50), (100, 100))\n        (0.0, 0.0, 100, 100)\n        >>> print("%f %f %f %f" % calcCubicBounds((50, 0), (0, 100), (100, 100), (50, 0)))\n        35.566243 0.000000 64.433757 75.000000\n    ',
    'calcQuadraticArcLength (line 151)': 'Calculates the arc length for a quadratic Bezier segment.\n\n    Args:\n        pt1: Start point of the Bezier as 2D tuple.\n        pt2: Handle point of the Bezier as 2D tuple.\n        pt3: End point of the Bezier as 2D tuple.\n\n    Returns:\n        Arc length value.\n\n    Example::\n\n        >>> calcQuadraticArcLength((0, 0), (0, 0), (0, 0)) # empty segment\n        0.0\n        >>> calcQuadraticArcLength((0, 0), (50, 0), (80, 0)) # collinear points\n        80.0\n        >>> calcQuadraticArcLength((0, 0), (0, 50), (0, 80)) # collinear points vertical\n        80.0\n        >>> calcQuadraticArcLength((0, 0), (50, 20), (100, 40)) # collinear points\n        107.70329614269008\n        >>> calcQuadraticArcLength((0, 0), (0, 100), (100, 0))\n        154.02976155645263\n        >>> calcQuadraticArcLength((0, 0), (0, 50), (100, 0))\n        120.21581243984076\n        >>> calcQuadraticArcLength((0, 0), (50, -10), (80, 50))\n        102.53273816445825\n        >>> calcQuadraticArcLength((0, 0), (40, 0), (-40, 0)) # collinear points, control point outside\n        66.66666666666667\n        >>> calcQuadraticArcLength((0, 0), (40, 0), (0, 0)) # collinear points, looping back\n        40.0\n    ',
    'calcQuadraticBounds (line 298)': 'Calculates the bounding rectangle for a quadratic Bezier segment.\n\n    Args:\n        pt1: Start point of the Bezier as a 2D tuple.\n        pt2: Handle point of the Bezier as a 2D tuple.\n        pt3: End point of the Bezier as a 2D tuple.\n\n    Returns:\n        A four-item tuple representing the bounding rectangle ``(xMin, yMin, xMax, yMax)``.\n\n    Example::\n\n        >>> calcQuadraticBounds((0, 0), (50, 100), (100, 0))\n        (0, 0, 100, 50.0)\n        >>> calcQuadraticBounds((0, 0), (100, 0), (100, 100))\n        (0.0, 0.0, 100, 100)\n    ',
    'curveCurveIntersections (line 1378)': 'Finds intersections between a curve and a curve.\n\n    Args:\n        curve1: List of coordinates of the first curve segment as 2D tuples.\n        curve2: List of coordinates of the second curve segment as 2D tuples.\n\n    Returns:\n        A list of ``Intersection`` objects, each object having ``pt``, ``t1``\n        and ``t2`` attributes containing the intersection point, time on first\n        segment and time on second segment respectively.\n\n    Examples::\n        >>> curve1 = [ (10,100), (90,30), (40,140), (220,220) ]\n        >>> curve2 = [ (5,150), (180,20), (80,250), (210,190) ]\n        >>> intersections = curveCurveIntersections(curve1, curve2)\n        >>> len(intersections)\n        3\n        >>> intersections[0].pt\n        (81.7831487395506, 109.88904552375288)\n    ',
    'curveLineIntersections (line 1248)': 'Finds intersections between a curve and a line.\n\n    Args:\n        curve: List of coordinates of the curve segment as 2D tuples.\n        line: List of coordinates of the line segment as 2D tuples.\n\n    Returns:\n        A list of ``Intersection`` objects, each object having ``pt``, ``t1``\n        and ``t2`` attributes containing the intersection point, time on first\n        segment and time on second segment respectively.\n\n    Examples::\n        >>> curve = [ (100, 240), (30, 60), (210, 230), (160, 30) ]\n        >>> line  = [ (25, 260), (230, 20) ]\n        >>> intersections = curveLineIntersections(curve, line)\n        >>> len(intersections)\n        3\n        >>> intersections[0].pt\n        (84.9000930760723, 189.87306176459828)\n    ',
    'lineLineIntersections (line 1147)': 'Finds intersections between two line segments.\n\n    Args:\n        s1, e1: Coordinates of the first line as 2D tuples.\n        s2, e2: Coordinates of the second line as 2D tuples.\n\n    Returns:\n        A list of ``Intersection`` objects, each object having ``pt``, ``t1``\n        and ``t2`` attributes containing the intersection point, time on first\n        segment and time on second segment respectively.\n\n    Examples::\n\n        >>> a = lineLineIntersections( (310,389), (453, 222), (289, 251), (447, 367))\n        >>> len(a)\n        1\n        >>> intersection = a[0]\n        >>> intersection.pt\n        (374.44882952482897, 313.73458370177315)\n        >>> (intersection.t1, intersection.t2)\n        (0.45069111555824465, 0.5408153767394238)\n    ',
    'segmentSegmentIntersections (line 1417)': 'Finds intersections between two segments.\n\n    Args:\n        seg1: List of coordinates of the first segment as 2D tuples.\n        seg2: List of coordinates of the second segment as 2D tuples.\n\n    Returns:\n        A list of ``Intersection`` objects, each object having ``pt``, ``t1``\n        and ``t2`` attributes containing the intersection point, time on first\n        segment and time on second segment respectively.\n\n    Examples::\n        >>> curve1 = [ (10,100), (90,30), (40,140), (220,220) ]\n        >>> curve2 = [ (5,150), (180,20), (80,250), (210,190) ]\n        >>> intersections = segmentSegmentIntersections(curve1, curve2)\n        >>> len(intersections)\n        3\n        >>> intersections[0].pt\n        (81.7831487395506, 109.88904552375288)\n        >>> curve3 = [ (100, 240), (30, 60), (210, 230), (160, 30) ]\n        >>> line  = [ (25, 260), (230, 20) ]\n        >>> intersections = segmentSegmentIntersections(curve3, line)\n        >>> len(intersections)\n        3\n        >>> intersections[0].pt\n        (84.9000930760723, 189.87306176459828)\n\n    ',
    'solveCubic (line 841)': 'Solve a cubic equation.\n\n    Solves *a*x*x*x + b*x*x + c*x + d = 0* where a, b, c and d are real.\n\n    Args:\n        a: coefficient of *x³*\n        b: coefficient of *x²*\n        c: coefficient of *x*\n        d: constant term\n\n    Returns:\n        A list of roots. Note that the returned list is neither guaranteed to\n        be sorted nor to contain unique values!\n\n    Examples::\n\n        >>> solveCubic(1, 1, -6, 0)\n        [-3.0, -0.0, 2.0]\n        >>> solveCubic(-10.0, -9.0, 48.0, -29.0)\n        [-2.9, 1.0, 1.0]\n        >>> solveCubic(-9.875, -9.0, 47.625, -28.75)\n        [-2.911392, 1.0, 1.0]\n        >>> solveCubic(1.0, -4.5, 6.75, -3.375)\n        [1.5, 1.5, 1.5]\n        >>> solveCubic(-12.0, 18.0, -9.0, 1.50023651123)\n        [0.5, 0.5, 0.5]\n        >>> solveCubic(\n        ...     9.0, 0.0, 0.0, -7.62939453125e-05\n        ... ) == [-0.0, -0.0, -0.0]\n        True\n    ',
    'splitCubic (line 552)': 'Split a cubic Bezier curve at a given coordinate.\n\n    Args:\n        pt1,pt2,pt3,pt4: Control points of the Bezier as 2D tuples.\n        where: Position at which to split the curve.\n        isHorizontal: Direction of the ray splitting the curve. If true,\n            ``where`` is interpreted as a Y coordinate; if false, then\n            ``where`` is interpreted as an X coordinate.\n\n    Returns:\n        A list of two curve segments (each curve segment being four 2D tuples)\n        if the curve was successfully split, or a list containing the original\n        curve.\n\n    Example::\n\n        >>> printSegments(splitCubic((0, 0), (25, 100), (75, 100), (100, 0), 150, False))\n        ((0, 0), (25, 100), (75, 100), (100, 0))\n        >>> printSegments(splitCubic((0, 0), (25, 100), (75, 100), (100, 0), 50, False))\n        ((0, 0), (12.5, 50), (31.25, 75), (50, 75))\n        ((50, 75), (68.75, 75), (87.5, 50), (100, 0))\n        >>> printSegments(splitCubic((0, 0), (25, 100), (75, 100), (100, 0), 25, True))\n        ((0, 0), (2.29379, 9.17517), (4.79804, 17.5085), (7.47414, 25))\n        ((7.47414, 25), (31.2886, 91.6667), (68.7114, 91.6667), (92.5259, 25))\n        ((92.5259, 25), (95.202, 17.5085), (97.7062, 9.17517), (100, 1.77636e-15))\n    ',
    'splitCubicAtT (line 613)': 'Split a cubic Bezier curve at one or more values of t.\n\n    Args:\n        pt1,pt2,pt3,pt4: Control points of the Bezier as 2D tuples.\n        *ts: Positions at which to split the curve.\n\n    Returns:\n        A list of curve segments (each curve segment being four 2D tuples).\n\n    Examples::\n\n        >>> printSegments(splitCubicAtT((0, 0), (25, 100), (75, 100), (100, 0), 0.5))\n        ((0, 0), (12.5, 50), (31.25, 75), (50, 75))\n        ((50, 75), (68.75, 75), (87.5, 50), (100, 0))\n        >>> printSegments(splitCubicAtT((0, 0), (25, 100), (75, 100), (100, 0), 0.5, 0.75))\n        ((0, 0), (12.5, 50), (31.25, 75), (50, 75))\n        ((50, 75), (59.375, 75), (68.75, 68.75), (77.3438, 56.25))\n        ((77.3438, 56.25), (85.9375, 43.75), (93.75, 25), (100, 0))\n    ',
    'splitLine (line 450)': 'Split a line at a given coordinate.\n\n    Args:\n        pt1: Start point of line as 2D tuple.\n        pt2: End point of line as 2D tuple.\n        where: Position at which to split the line.\n        isHorizontal: Direction of the ray splitting the line. If true,\n            ``where`` is interpreted as a Y coordinate; if false, then\n            ``where`` is interpreted as an X coordinate.\n\n    Returns:\n        A list of two line segments (each line segment being two 2D tuples)\n        if the line was successfully split, or a list containing the original\n        line.\n\n    Example::\n\n        >>> printSegments(splitLine((0, 0), (100, 100), 50, True))\n        ((0, 0), (50, 50))\n        ((50, 50), (100, 100))\n        >>> printSegments(splitLine((0, 0), (100, 100), 100, True))\n        ((0, 0), (100, 100))\n        >>> printSegments(splitLine((0, 0), (100, 100), 0, True))\n        ((0, 0), (0, 0))\n        ((0, 0), (100, 100))\n        >>> printSegments(splitLine((0, 0), (100, 100), 0, False))\n        ((0, 0), (0, 0))\n        ((0, 0), (100, 100))\n        >>> printSegments(splitLine((100, 0), (0, 0), 50, False))\n        ((100, 0), (50, 0))\n        ((50, 0), (0, 0))\n        >>> printSegments(splitLine((0, 100), (0, 0), 50, True))\n        ((0, 100), (0, 50))\n        ((0, 50), (0, 0))\n    ',
    'splitQuadratic (line 507)': "Split a quadratic Bezier curve at a given coordinate.\n\n    Args:\n        pt1,pt2,pt3: Control points of the Bezier as 2D tuples.\n        where: Position at which to split the curve.\n        isHorizontal: Direction of the ray splitting the curve. If true,\n            ``where`` is interpreted as a Y coordinate; if false, then\n            ``where`` is interpreted as an X coordinate.\n\n    Returns:\n        A list of two curve segments (each curve segment being three 2D tuples)\n        if the curve was successfully split, or a list containing the original\n        curve.\n\n    Example::\n\n        >>> printSegments(splitQuadratic((0, 0), (50, 100), (100, 0), 150, False))\n        ((0, 0), (50, 100), (100, 0))\n        >>> printSegments(splitQuadratic((0, 0), (50, 100), (100, 0), 50, False))\n        ((0, 0), (25, 50), (50, 50))\n        ((50, 50), (75, 50), (100, 0))\n        >>> printSegments(splitQuadratic((0, 0), (50, 100), (100, 0), 25, False))\n        ((0, 0), (12.5, 25), (25, 37.5))\n        ((25, 37.5), (62.5, 75), (100, 0))\n        >>> printSegments(splitQuadratic((0, 0), (50, 100), (100, 0), 25, True))\n        ((0, 0), (7.32233, 14.6447), (14.6447, 25))\n        ((14.6447, 25), (50, 75), (85.3553, 25))\n        ((85.3553, 25), (92.6777, 14.6447), (100, -7.10543e-15))\n        >>> # XXX I'm not at all sure if the following behavior is desirable:\n        >>> printSegments(splitQuadratic((0, 0), (50, 100), (100, 0), 50, True))\n        ((0, 0), (25, 50), (50, 50))\n        ((50, 50), (50, 50), (50, 50))\n        ((50, 50), (75, 50), (100, 0))\n    ",
    'splitQuadraticAtT (line 589)': 'Split a quadratic Bezier curve at one or more values of t.\n\n    Args:\n        pt1,pt2,pt3: Control points of the Bezier as 2D tuples.\n        *ts: Positions at which to split the curve.\n\n    Returns:\n        A list of curve segments (each curve segment being three 2D tuples).\n\n    Examples::\n\n        >>> printSegments(splitQuadraticAtT((0, 0), (50, 100), (100, 0), 0.5))\n        ((0, 0), (25, 50), (50, 50))\n        ((50, 50), (75, 50), (100, 0))\n        >>> printSegments(splitQuadraticAtT((0, 0), (50, 100), (100, 0), 0.5, 0.75))\n        ((0, 0), (25, 50), (50, 50))\n        ((50, 50), (62.5, 50), (75, 37.5))\n        ((75, 37.5), (87.5, 25), (100, 0))\n    ',
}

