# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .LVecBase4d import LVecBase4d

class PlaneD(LVecBase4d):
    """
    /**
     * An abstract mathematical description of a plane.  A plane is defined by the
     * equation Ax + By + Cz + D = 0.
     */
    """
    def distToPlane(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        dist_to_plane(LPlaned self, const LPoint3d point)
        
        /**
         * Returns the straight-line shortest distance from the point to the plane.
         * The returned value is positive if the point is in front of the plane (on
         * the side with the normal), or negative in the point is behind the plane (on
         * the opposite side from the normal). It's zero if the point is exactly in
         * the plane.
         */
        """
        pass

    def dist_to_plane(self, LPlaned_self, const_LPoint3d_point): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        dist_to_plane(LPlaned self, const LPoint3d point)
        
        /**
         * Returns the straight-line shortest distance from the point to the plane.
         * The returned value is positive if the point is in front of the plane (on
         * the side with the normal), or negative in the point is behind the plane (on
         * the opposite side from the normal). It's zero if the point is exactly in
         * the plane.
         */
        """
        pass

    def flip(self, const_LPlaned_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        flip(const LPlaned self)
        
        /**
         * Convenience method that flips the plane in-place.  This is done by simply
         * flipping the normal vector.
         */
        """
        pass

    def getNormal(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_normal(LPlaned self)
        
        /**
         * Returns the surface normal of the plane.
         */
        """
        pass

    def getPoint(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_point(LPlaned self)
        
        /**
         * Returns an arbitrary point in the plane.  This can be used along with the
         * normal returned by get_normal() to reconstruct the plane.
         */
        """
        pass

    def getReflectionMat(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_reflection_mat(LPlaned self)
        
        /**
         * This computes a transform matrix that reflects the universe to the other
         * side of the plane, as in a mirror.
         */
        """
        pass

    def get_normal(self, LPlaned_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_normal(LPlaned self)
        
        /**
         * Returns the surface normal of the plane.
         */
        """
        pass

    def get_point(self, LPlaned_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_point(LPlaned self)
        
        /**
         * Returns an arbitrary point in the plane.  This can be used along with the
         * normal returned by get_normal() to reconstruct the plane.
         */
        """
        pass

    def get_reflection_mat(self, LPlaned_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_reflection_mat(LPlaned self)
        
        /**
         * This computes a transform matrix that reflects the universe to the other
         * side of the plane, as in a mirror.
         */
        """
        pass

    def intersectsLine(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        intersects_line(LPlaned self, LPoint3d intersection_point, const LPoint3d p1, const LPoint3d p2)
        
        /**
         * Returns true if the plane intersects the infinite line passing through
         * points p1 and p2, false if the line is parallel.  The points p1 and p2 are
         * used only to define the Euclidean line; they have no other bearing on the
         * intersection test.  If true, sets intersection_point to the point of
         * intersection.
         */
        
        /**
         * This flavor of intersects_line() returns a bit more information about the
         * nature of the intersecting point.  The line is defined via the parametric
         * equation from + t * delta for all real values of t.
         *
         * If there is no intersection with the plane, the function returns false and
         * leaves t undefined.  If there is an intersection with the plane, the
         * function returns true and sets t to the parametric value that defines the
         * point of intersection.  That is, t == 0.0f implies that the intersection
         * occurred exactly at point from, and t == 1.0f implies at point from +
         * delta, with other values of t accordingly.
         */
        """
        pass

    def intersectsPlane(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        intersects_plane(LPlaned self, LPoint3d from, LVector3d delta, const LPlaned other)
        
        /**
         * Returns true if the two planes intersect, false if they do not.  If they do
         * intersect, then from and delta are filled in with the parametric
         * representation of the line of intersection: that is, from is a point on
         * that line, and delta is a vector showing the direction of the line.
         */
        """
        pass

    def intersects_line(self, LPlaned_self, LPoint3d_intersection_point, const_LPoint3d_p1, const_LPoint3d_p2): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        intersects_line(LPlaned self, LPoint3d intersection_point, const LPoint3d p1, const LPoint3d p2)
        
        /**
         * Returns true if the plane intersects the infinite line passing through
         * points p1 and p2, false if the line is parallel.  The points p1 and p2 are
         * used only to define the Euclidean line; they have no other bearing on the
         * intersection test.  If true, sets intersection_point to the point of
         * intersection.
         */
        
        /**
         * This flavor of intersects_line() returns a bit more information about the
         * nature of the intersecting point.  The line is defined via the parametric
         * equation from + t * delta for all real values of t.
         *
         * If there is no intersection with the plane, the function returns false and
         * leaves t undefined.  If there is an intersection with the plane, the
         * function returns true and sets t to the parametric value that defines the
         * point of intersection.  That is, t == 0.0f implies that the intersection
         * occurred exactly at point from, and t == 1.0f implies at point from +
         * delta, with other values of t accordingly.
         */
        """
        pass

    def intersects_plane(self, LPlaned_self, LPoint3d_from, LVector3d_delta, const_LPlaned_other): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        intersects_plane(LPlaned self, LPoint3d from, LVector3d delta, const LPlaned other)
        
        /**
         * Returns true if the two planes intersect, false if they do not.  If they do
         * intersect, then from and delta are filled in with the parametric
         * representation of the line of intersection: that is, from is a point on
         * that line, and delta is a vector showing the direction of the line.
         */
        """
        pass

    def normalize(self, const_LPlaned_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        normalize(const LPlaned self)
        
        /**
         * Normalizes the plane in place.  Returns true if the plane was normalized,
         * false if the plane had a zero-length normal vector.
         */
        """
        pass

    def normalized(self, LPlaned_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        normalized(LPlaned self)
        
        /**
         * Normalizes the plane and returns the normalized plane as a copy.  If the
         * plane's normal was a zero-length vector, the same plane is returned.
         */
        """
        pass

    def output(self, LPlaned_self, ostream_out): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        output(LPlaned self, ostream out)
        
        /**
         *
         */
        """
        pass

    def project(self, LPlaned_self, const_LPoint3d_point): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        project(LPlaned self, const LPoint3d point)
        
        /**
         * Returns the point within the plane nearest to the indicated point in space.
         */
        """
        pass

    def write(self, LPlaned_self, ostream_out, int_indent_level): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        write(LPlaned self, ostream out, int indent_level)
        
        /**
         *
         */
        """
        pass

    def xform(self, const_LPlaned_self, const_LMatrix4d_mat): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        xform(const LPlaned self, const LMatrix4d mat)
        
        /**
         * Transforms the plane by the indicated matrix.
         */
        """
        pass

    def __copy__(self, *args, **kwargs): # real signature unknown
        pass

    def __deepcopy__(self, *args, **kwargs): # real signature unknown
        pass

    def __imul__(self, *args, **kwargs): # real signature unknown
        """ Return self*=value. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __mul__(self, *args, **kwargs): # real signature unknown
        """ Return self*value. """
        pass

    def __neg__(self, *args, **kwargs): # real signature unknown
        """ -self """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __rmul__(self, *args, **kwargs): # real signature unknown
        """ Return value*self. """
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.core.LPlaned' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.core.LPlaned' objects>"
        '__doc__': '/**\n * An abstract mathematical description of a plane.  A plane is defined by the\n * equation Ax + By + Cz + D = 0.\n */',
        '__imul__': None, # (!) real value is "<slot wrapper '__imul__' of 'panda3d.core.LPlaned' objects>"
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.LPlaned' objects>"
        '__mul__': None, # (!) real value is "<slot wrapper '__mul__' of 'panda3d.core.LPlaned' objects>"
        '__neg__': None, # (!) real value is "<slot wrapper '__neg__' of 'panda3d.core.LPlaned' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE341510>'
        '__repr__': None, # (!) real value is "<slot wrapper '__repr__' of 'panda3d.core.LPlaned' objects>"
        '__rmul__': None, # (!) real value is "<slot wrapper '__rmul__' of 'panda3d.core.LPlaned' objects>"
        '__str__': None, # (!) real value is "<slot wrapper '__str__' of 'panda3d.core.LPlaned' objects>"
        'distToPlane': None, # (!) real value is "<method 'distToPlane' of 'panda3d.core.LPlaned' objects>"
        'dist_to_plane': None, # (!) real value is "<method 'dist_to_plane' of 'panda3d.core.LPlaned' objects>"
        'flip': None, # (!) real value is "<method 'flip' of 'panda3d.core.LPlaned' objects>"
        'getNormal': None, # (!) real value is "<method 'getNormal' of 'panda3d.core.LPlaned' objects>"
        'getPoint': None, # (!) real value is "<method 'getPoint' of 'panda3d.core.LPlaned' objects>"
        'getReflectionMat': None, # (!) real value is "<method 'getReflectionMat' of 'panda3d.core.LPlaned' objects>"
        'get_normal': None, # (!) real value is "<method 'get_normal' of 'panda3d.core.LPlaned' objects>"
        'get_point': None, # (!) real value is "<method 'get_point' of 'panda3d.core.LPlaned' objects>"
        'get_reflection_mat': None, # (!) real value is "<method 'get_reflection_mat' of 'panda3d.core.LPlaned' objects>"
        'intersectsLine': None, # (!) real value is "<method 'intersectsLine' of 'panda3d.core.LPlaned' objects>"
        'intersectsPlane': None, # (!) real value is "<method 'intersectsPlane' of 'panda3d.core.LPlaned' objects>"
        'intersects_line': None, # (!) real value is "<method 'intersects_line' of 'panda3d.core.LPlaned' objects>"
        'intersects_plane': None, # (!) real value is "<method 'intersects_plane' of 'panda3d.core.LPlaned' objects>"
        'normalize': None, # (!) real value is "<method 'normalize' of 'panda3d.core.LPlaned' objects>"
        'normalized': None, # (!) real value is "<method 'normalized' of 'panda3d.core.LPlaned' objects>"
        'output': None, # (!) real value is "<method 'output' of 'panda3d.core.LPlaned' objects>"
        'project': None, # (!) real value is "<method 'project' of 'panda3d.core.LPlaned' objects>"
        'write': None, # (!) real value is "<method 'write' of 'panda3d.core.LPlaned' objects>"
        'xform': None, # (!) real value is "<method 'xform' of 'panda3d.core.LPlaned' objects>"
    }


