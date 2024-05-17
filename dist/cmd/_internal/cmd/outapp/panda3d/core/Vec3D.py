# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .LVecBase3d import LVecBase3d

class Vec3D(LVecBase3d):
    """
    /**
     * This is a three-component vector distance (as opposed to a three-component
     * point, which represents a particular point in space).  Some of the methods
     * are slightly different between LPoint3 and LVector3; in particular,
     * subtraction of two points yields a vector, while addition of a vector and a
     * point yields a point.
     */
    """
    def angleDeg(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        angle_deg(LVector3d self, const LVector3d other)
        
        /**
         * Returns the angle between this vector and the other one, expressed in
         * degrees.  Both vectors should be initially normalized.
         */
        """
        pass

    def angleRad(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        angle_rad(LVector3d self, const LVector3d other)
        
        /**
         * Returns the unsigned angle between this vector and the other one, expressed
         * in radians.  Both vectors should be initially normalized.
         */
        """
        pass

    def angle_deg(self, LVector3d_self, const_LVector3d_other): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        angle_deg(LVector3d self, const LVector3d other)
        
        /**
         * Returns the angle between this vector and the other one, expressed in
         * degrees.  Both vectors should be initially normalized.
         */
        """
        pass

    def angle_rad(self, LVector3d_self, const_LVector3d_other): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        angle_rad(LVector3d self, const LVector3d other)
        
        /**
         * Returns the unsigned angle between this vector and the other one, expressed
         * in radians.  Both vectors should be initially normalized.
         */
        """
        pass

    def back(self, int_cs): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        back(int cs)
        
        /**
         * Returns the back vector for the given coordinate system.
         */
        """
        pass

    def cross(self, LVector3d_self, const_LVecBase3d_other): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        cross(LVector3d self, const LVecBase3d other)
        
        /**
         *
         */
        """
        pass

    def down(self, int_cs): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        down(int cs)
        
        /**
         * Returns the down vector for the given coordinate system.
         */
        """
        pass

    def forward(self, int_cs): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        forward(int cs)
        
        /**
         * Returns the forward vector for the given coordinate system.
         */
        """
        pass

    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getXy(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_xy(LVector3d self)
        
        /**
         * Returns a 2-component vector that shares just the first two components of
         * this vector.
         */
        """
        pass

    def getXz(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_xz(LVector3d self)
        
        /**
         * Returns a 2-component vector that shares just the first and last components
         * of this vector.
         */
        """
        pass

    def getYz(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_yz(LVector3d self)
        
        /**
         * Returns a 2-component vector that shares just the last two components of
         * this vector.
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_xy(self, LVector3d_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_xy(LVector3d self)
        
        /**
         * Returns a 2-component vector that shares just the first two components of
         * this vector.
         */
        """
        pass

    def get_xz(self, LVector3d_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_xz(LVector3d self)
        
        /**
         * Returns a 2-component vector that shares just the first and last components
         * of this vector.
         */
        """
        pass

    def get_yz(self, LVector3d_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_yz(LVector3d self)
        
        /**
         * Returns a 2-component vector that shares just the last two components of
         * this vector.
         */
        """
        pass

    def left(self, int_cs): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        left(int cs)
        
        /**
         * Returns the left vector for the given coordinate system.
         */
        """
        pass

    def normalized(self, LVector3d_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        normalized(LVector3d self)
        
        /**
         * Normalizes the vector and returns the normalized vector as a copy.  If the
         * vector was a zero-length vector, a zero length vector will be returned.
         */
        """
        pass

    def project(self, LVector3d_self, const_LVecBase3d_onto): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        project(LVector3d self, const LVecBase3d onto)
        
        /**
         * Returns a new vector representing the projection of this vector onto
         * another one.  The resulting vector will be a scalar multiple of onto.
         */
        """
        pass

    def relativeAngleDeg(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        relative_angle_deg(LVector3d self, const LVector3d other)
        
        /**
         * @deprecated Do not use.
         */
        """
        pass

    def relativeAngleRad(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        relative_angle_rad(LVector3d self, const LVector3d other)
        
        /**
         * @deprecated Do not use.
         */
        """
        pass

    def relative_angle_deg(self, LVector3d_self, const_LVector3d_other): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        relative_angle_deg(LVector3d self, const LVector3d other)
        
        /**
         * @deprecated Do not use.
         */
        """
        pass

    def relative_angle_rad(self, LVector3d_self, const_LVector3d_other): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        relative_angle_rad(LVector3d self, const LVector3d other)
        
        /**
         * @deprecated Do not use.
         */
        """
        pass

    def rfu(self, double_right, double_fwd, double_up, int_cs): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        rfu(double right, double fwd, double up, int cs)
        
        // INLINE_LINMATH static FLOATNAME(LVector3) & rfu(FLOATTYPE right,
        
        /**
         * Returns a vector that is described by its right, forward, and up
         * components, in whatever way the coordinate system represents that vector.
         */
        """
        pass

    def right(self, int_cs): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        right(int cs)
        
        /**
         * Returns the right vector for the given coordinate system.
         */
        """
        pass

    def signedAngleDeg(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        signed_angle_deg(LVector3d self, const LVector3d other, const LVector3d ref)
        
        /**
         * Returns the signed angle between two vectors.  The angle is positive if the
         * rotation from this vector to other is clockwise when looking in the
         * direction of the ref vector.
         *
         * Vectors (except the ref vector) should be initially normalized.
         */
        """
        pass

    def signedAngleRad(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        signed_angle_rad(LVector3d self, const LVector3d other, const LVector3d ref)
        
        /**
         * returns the signed angle between two vectors.  The angle is positive if the
         * rotation from this vector to other is clockwise when looking in the
         * direction of the ref vector.
         *
         * Vectors (except the ref vector) should be initially normalized.
         */
        """
        pass

    def signed_angle_deg(self, LVector3d_self, const_LVector3d_other, const_LVector3d_ref): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        signed_angle_deg(LVector3d self, const LVector3d other, const LVector3d ref)
        
        /**
         * Returns the signed angle between two vectors.  The angle is positive if the
         * rotation from this vector to other is clockwise when looking in the
         * direction of the ref vector.
         *
         * Vectors (except the ref vector) should be initially normalized.
         */
        """
        pass

    def signed_angle_rad(self, LVector3d_self, const_LVector3d_other, const_LVector3d_ref): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        signed_angle_rad(LVector3d self, const LVector3d other, const LVector3d ref)
        
        /**
         * returns the signed angle between two vectors.  The angle is positive if the
         * rotation from this vector to other is clockwise when looking in the
         * direction of the ref vector.
         *
         * Vectors (except the ref vector) should be initially normalized.
         */
        """
        pass

    def unitX(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        unit_x()
        
        /**
         * Returns a unit X vector.
         */
        """
        pass

    def unitY(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        unit_y()
        
        /**
         * Returns a unit Y vector.
         */
        """
        pass

    def unitZ(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        unit_z()
        
        /**
         * Returns a unit Z vector.
         */
        """
        pass

    def unit_x(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        unit_x()
        
        /**
         * Returns a unit X vector.
         */
        """
        pass

    def unit_y(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        unit_y()
        
        /**
         * Returns a unit Y vector.
         */
        """
        pass

    def unit_z(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        unit_z()
        
        /**
         * Returns a unit Z vector.
         */
        """
        pass

    def up(self, int_cs): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        up(int cs)
        
        /**
         * Returns the up vector for the given coordinate system.
         */
        """
        pass

    def zero(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        zero()
        
        /**
         * Returns a zero-length vector.
         */
        """
        pass

    def __add__(self, *args, **kwargs): # real signature unknown
        """ Return self+value. """
        pass

    def __copy__(self, *args, **kwargs): # real signature unknown
        pass

    def __deepcopy__(self, *args, **kwargs): # real signature unknown
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
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

    def __radd__(self, *args, **kwargs): # real signature unknown
        """ Return value+self. """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __rmul__(self, *args, **kwargs): # real signature unknown
        """ Return value*self. """
        pass

    def __rsub__(self, *args, **kwargs): # real signature unknown
        """ Return value-self. """
        pass

    def __rtruediv__(self, *args, **kwargs): # real signature unknown
        """ Return value/self. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    def __sub__(self, *args, **kwargs): # real signature unknown
        """ Return self-value. """
        pass

    def __truediv__(self, *args, **kwargs): # real signature unknown
        """ Return self/value. """
        pass

    xy = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    xz = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    yz = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__add__': None, # (!) real value is "<slot wrapper '__add__' of 'panda3d.core.LVector3d' objects>"
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.core.LVector3d' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.core.LVector3d' objects>"
        '__delattr__': None, # (!) real value is "<slot wrapper '__delattr__' of 'panda3d.core.LVector3d' objects>"
        '__doc__': '/**\n * This is a three-component vector distance (as opposed to a three-component\n * point, which represents a particular point in space).  Some of the methods\n * are slightly different between LPoint3 and LVector3; in particular,\n * subtraction of two points yields a vector, while addition of a vector and a\n * point yields a point.\n */',
        '__getattribute__': None, # (!) real value is "<slot wrapper '__getattribute__' of 'panda3d.core.LVector3d' objects>"
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.LVector3d' objects>"
        '__mul__': None, # (!) real value is "<slot wrapper '__mul__' of 'panda3d.core.LVector3d' objects>"
        '__neg__': None, # (!) real value is "<slot wrapper '__neg__' of 'panda3d.core.LVector3d' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE321E60>'
        '__radd__': None, # (!) real value is "<slot wrapper '__radd__' of 'panda3d.core.LVector3d' objects>"
        '__repr__': None, # (!) real value is "<slot wrapper '__repr__' of 'panda3d.core.LVector3d' objects>"
        '__rmul__': None, # (!) real value is "<slot wrapper '__rmul__' of 'panda3d.core.LVector3d' objects>"
        '__rsub__': None, # (!) real value is "<slot wrapper '__rsub__' of 'panda3d.core.LVector3d' objects>"
        '__rtruediv__': None, # (!) real value is "<slot wrapper '__rtruediv__' of 'panda3d.core.LVector3d' objects>"
        '__setattr__': None, # (!) real value is "<slot wrapper '__setattr__' of 'panda3d.core.LVector3d' objects>"
        '__sub__': None, # (!) real value is "<slot wrapper '__sub__' of 'panda3d.core.LVector3d' objects>"
        '__truediv__': None, # (!) real value is "<slot wrapper '__truediv__' of 'panda3d.core.LVector3d' objects>"
        'angleDeg': None, # (!) real value is "<method 'angleDeg' of 'panda3d.core.LVector3d' objects>"
        'angleRad': None, # (!) real value is "<method 'angleRad' of 'panda3d.core.LVector3d' objects>"
        'angle_deg': None, # (!) real value is "<method 'angle_deg' of 'panda3d.core.LVector3d' objects>"
        'angle_rad': None, # (!) real value is "<method 'angle_rad' of 'panda3d.core.LVector3d' objects>"
        'back': None, # (!) real value is '<staticmethod(<built-in method back of type object at 0x00007FFCFE321E60>)>'
        'cross': None, # (!) real value is "<method 'cross' of 'panda3d.core.LVector3d' objects>"
        'down': None, # (!) real value is '<staticmethod(<built-in method down of type object at 0x00007FFCFE321E60>)>'
        'forward': None, # (!) real value is '<staticmethod(<built-in method forward of type object at 0x00007FFCFE321E60>)>'
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE321E60>)>'
        'getXy': None, # (!) real value is "<method 'getXy' of 'panda3d.core.LVector3d' objects>"
        'getXz': None, # (!) real value is "<method 'getXz' of 'panda3d.core.LVector3d' objects>"
        'getYz': None, # (!) real value is "<method 'getYz' of 'panda3d.core.LVector3d' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE321E60>)>'
        'get_xy': None, # (!) real value is "<method 'get_xy' of 'panda3d.core.LVector3d' objects>"
        'get_xz': None, # (!) real value is "<method 'get_xz' of 'panda3d.core.LVector3d' objects>"
        'get_yz': None, # (!) real value is "<method 'get_yz' of 'panda3d.core.LVector3d' objects>"
        'left': None, # (!) real value is '<staticmethod(<built-in method left of type object at 0x00007FFCFE321E60>)>'
        'normalized': None, # (!) real value is "<method 'normalized' of 'panda3d.core.LVector3d' objects>"
        'project': None, # (!) real value is "<method 'project' of 'panda3d.core.LVector3d' objects>"
        'relativeAngleDeg': None, # (!) real value is "<method 'relativeAngleDeg' of 'panda3d.core.LVector3d' objects>"
        'relativeAngleRad': None, # (!) real value is "<method 'relativeAngleRad' of 'panda3d.core.LVector3d' objects>"
        'relative_angle_deg': None, # (!) real value is "<method 'relative_angle_deg' of 'panda3d.core.LVector3d' objects>"
        'relative_angle_rad': None, # (!) real value is "<method 'relative_angle_rad' of 'panda3d.core.LVector3d' objects>"
        'rfu': None, # (!) real value is '<staticmethod(<built-in method rfu of type object at 0x00007FFCFE321E60>)>'
        'right': None, # (!) real value is '<staticmethod(<built-in method right of type object at 0x00007FFCFE321E60>)>'
        'signedAngleDeg': None, # (!) real value is "<method 'signedAngleDeg' of 'panda3d.core.LVector3d' objects>"
        'signedAngleRad': None, # (!) real value is "<method 'signedAngleRad' of 'panda3d.core.LVector3d' objects>"
        'signed_angle_deg': None, # (!) real value is "<method 'signed_angle_deg' of 'panda3d.core.LVector3d' objects>"
        'signed_angle_rad': None, # (!) real value is "<method 'signed_angle_rad' of 'panda3d.core.LVector3d' objects>"
        'unitX': None, # (!) real value is '<staticmethod(<built-in method unitX of type object at 0x00007FFCFE321E60>)>'
        'unitY': None, # (!) real value is '<staticmethod(<built-in method unitY of type object at 0x00007FFCFE321E60>)>'
        'unitZ': None, # (!) real value is '<staticmethod(<built-in method unitZ of type object at 0x00007FFCFE321E60>)>'
        'unit_x': None, # (!) real value is '<staticmethod(<built-in method unit_x of type object at 0x00007FFCFE321E60>)>'
        'unit_y': None, # (!) real value is '<staticmethod(<built-in method unit_y of type object at 0x00007FFCFE321E60>)>'
        'unit_z': None, # (!) real value is '<staticmethod(<built-in method unit_z of type object at 0x00007FFCFE321E60>)>'
        'up': None, # (!) real value is '<staticmethod(<built-in method up of type object at 0x00007FFCFE321E60>)>'
        'xy': None, # (!) real value is "<attribute 'xy' of 'panda3d.core.LVector3d' objects>"
        'xz': None, # (!) real value is "<attribute 'xz' of 'panda3d.core.LVector3d' objects>"
        'yz': None, # (!) real value is "<attribute 'yz' of 'panda3d.core.LVector3d' objects>"
        'zero': None, # (!) real value is '<staticmethod(<built-in method zero of type object at 0x00007FFCFE321E60>)>'
    }

