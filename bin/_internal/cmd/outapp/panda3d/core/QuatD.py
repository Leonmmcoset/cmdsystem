# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .LVecBase4d import LVecBase4d

class QuatD(LVecBase4d):
    """
    /**
     * This is the base quaternion class
     */
    """
    def almostEqual(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        almost_equal(LQuaterniond self, const LQuaterniond other)
        almost_equal(LQuaterniond self, const LQuaterniond other, double threshold)
        
        /**
         * Returns true if two quaternions are memberwise equal within a default
         * tolerance based on the numeric type.
         */
        
        /**
         * Returns true if two quaternions are memberwise equal within a specified
         * tolerance.
         */
        """
        pass

    def almostSameDirection(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        almost_same_direction(LQuaterniond self, const LQuaterniond other, double threshold)
        
        /**
         * Returns true if two quaternions represent the same rotation within a
         * specified tolerance.
         */
        """
        pass

    def almost_equal(self, LQuaterniond_self, const_LQuaterniond_other): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        almost_equal(LQuaterniond self, const LQuaterniond other)
        almost_equal(LQuaterniond self, const LQuaterniond other, double threshold)
        
        /**
         * Returns true if two quaternions are memberwise equal within a default
         * tolerance based on the numeric type.
         */
        
        /**
         * Returns true if two quaternions are memberwise equal within a specified
         * tolerance.
         */
        """
        pass

    def almost_same_direction(self, LQuaterniond_self, const_LQuaterniond_other, double_threshold): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        almost_same_direction(LQuaterniond self, const LQuaterniond other, double threshold)
        
        /**
         * Returns true if two quaternions represent the same rotation within a
         * specified tolerance.
         */
        """
        pass

    def angleDeg(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        angle_deg(LQuaterniond self, const LQuaterniond other)
        
        /**
         * Returns the angle between the orientation represented by this quaternion
         * and the other one, expressed in degrees.
         */
        """
        pass

    def angleRad(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        angle_rad(LQuaterniond self, const LQuaterniond other)
        
        /**
         * Returns the angle between the orientation represented by this quaternion
         * and the other one, expressed in radians.
         */
        """
        pass

    def angle_deg(self, LQuaterniond_self, const_LQuaterniond_other): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        angle_deg(LQuaterniond self, const LQuaterniond other)
        
        /**
         * Returns the angle between the orientation represented by this quaternion
         * and the other one, expressed in degrees.
         */
        """
        pass

    def angle_rad(self, LQuaterniond_self, const_LQuaterniond_other): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        angle_rad(LQuaterniond self, const LQuaterniond other)
        
        /**
         * Returns the angle between the orientation represented by this quaternion
         * and the other one, expressed in radians.
         */
        """
        pass

    def conjugate(self, LQuaterniond_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        conjugate(LQuaterniond self)
        
        /**
         * Returns the complex conjugate of this quat.
         */
        """
        pass

    def conjugateFrom(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        conjugate_from(const LQuaterniond self, const LQuaterniond other)
        
        /**
         * Computes the conjugate of the other quat, and stores the result in this
         * quat.  This is a fully general operation and makes no assumptions about the
         * type of transform represented by the quat.
         *
         * The other quat must be a different object than this quat.  However, if you
         * need to get a conjugate of a quat in place, see conjugate_in_place.
         *
         * The return value is true if the quat was successfully inverted, false if
         * there was a singularity.
         */
        """
        pass

    def conjugateInPlace(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        conjugate_in_place(const LQuaterniond self)
        
        /**
         * Sets this to be the conjugate of the current quat.  Returns true if the
         * successful, false if the quat was singular.
         */
        """
        pass

    def conjugate_from(self, const_LQuaterniond_self, const_LQuaterniond_other): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        conjugate_from(const LQuaterniond self, const LQuaterniond other)
        
        /**
         * Computes the conjugate of the other quat, and stores the result in this
         * quat.  This is a fully general operation and makes no assumptions about the
         * type of transform represented by the quat.
         *
         * The other quat must be a different object than this quat.  However, if you
         * need to get a conjugate of a quat in place, see conjugate_in_place.
         *
         * The return value is true if the quat was successfully inverted, false if
         * there was a singularity.
         */
        """
        pass

    def conjugate_in_place(self, const_LQuaterniond_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        conjugate_in_place(const LQuaterniond self)
        
        /**
         * Sets this to be the conjugate of the current quat.  Returns true if the
         * successful, false if the quat was singular.
         */
        """
        pass

    def extractToMatrix(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        extract_to_matrix(LQuaterniond self, LMatrix4d m)
        extract_to_matrix(LQuaterniond self, LMatrix3d m)
        
        /**
         * Based on the quat lib from VRPN.
         */
        
        /**
         * Based on the quat lib from VRPN.
         */
        """
        pass

    def extract_to_matrix(self, LQuaterniond_self, LMatrix4d_m): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        extract_to_matrix(LQuaterniond self, LMatrix4d m)
        extract_to_matrix(LQuaterniond self, LMatrix3d m)
        
        /**
         * Based on the quat lib from VRPN.
         */
        
        /**
         * Based on the quat lib from VRPN.
         */
        """
        pass

    def getAngle(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_angle(LQuaterniond self)
        
        /**
         * This, along with get_axis(), returns the rotation represented by the
         * quaternion as an angle about an arbitrary axis.  This returns the angle, in
         * degrees counterclockwise about the axis.
         *
         * It is necessary to ensure the quaternion has been normalized (for instance,
         * with a call to normalize()) before calling this method.
         */
        """
        pass

    def getAngleRad(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_angle_rad(LQuaterniond self)
        
        /**
         * This, along with get_axis(), returns the rotation represented by the
         * quaternion as an angle about an arbitrary axis.  This returns the angle, in
         * radians counterclockwise about the axis.
         *
         * It is necessary to ensure the quaternion has been normalized (for instance,
         * with a call to normalize()) before calling this method.
         */
        """
        pass

    def getAxis(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_axis(LQuaterniond self)
        
        /**
         * This, along with get_angle(), returns the rotation represented by the
         * quaternion as an angle about an arbitrary axis.  This returns the axis; it
         * is not normalized.
         */
        """
        pass

    def getAxisNormalized(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_axis_normalized(LQuaterniond self)
        
        /**
         * This, along with get_angle(), returns the rotation represented by the
         * quaternion as an angle about an arbitrary axis.  This returns the
         * normalized axis.
         */
        """
        pass

    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getForward(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_forward(LQuaterniond self, int cs)
        
        /**
         * Returns the orientation represented by this quaternion, expressed as a
         * forward vector.
         */
        """
        pass

    def getHpr(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_hpr(LQuaterniond self, int cs)
        
        /**
         * Extracts the equivalent Euler angles from the unit quaternion.
         */
        """
        pass

    def getI(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_i(LQuaterniond self)
        
        /**
         *
         */
        """
        pass

    def getJ(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_j(LQuaterniond self)
        
        /**
         *
         */
        """
        pass

    def getK(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_k(LQuaterniond self)
        
        /**
         *
         */
        """
        pass

    def getR(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_r(LQuaterniond self)
        
        /**
         *
         */
        """
        pass

    def getRight(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_right(LQuaterniond self, int cs)
        
        /**
         * Returns the orientation represented by this quaternion, expressed as a
         * right vector.
         */
        """
        pass

    def getUp(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_up(LQuaterniond self, int cs)
        
        /**
         * Returns the orientation represented by this quaternion, expressed as an up
         * vector.
         */
        """
        pass

    def get_angle(self, LQuaterniond_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_angle(LQuaterniond self)
        
        /**
         * This, along with get_axis(), returns the rotation represented by the
         * quaternion as an angle about an arbitrary axis.  This returns the angle, in
         * degrees counterclockwise about the axis.
         *
         * It is necessary to ensure the quaternion has been normalized (for instance,
         * with a call to normalize()) before calling this method.
         */
        """
        pass

    def get_angle_rad(self, LQuaterniond_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_angle_rad(LQuaterniond self)
        
        /**
         * This, along with get_axis(), returns the rotation represented by the
         * quaternion as an angle about an arbitrary axis.  This returns the angle, in
         * radians counterclockwise about the axis.
         *
         * It is necessary to ensure the quaternion has been normalized (for instance,
         * with a call to normalize()) before calling this method.
         */
        """
        pass

    def get_axis(self, LQuaterniond_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_axis(LQuaterniond self)
        
        /**
         * This, along with get_angle(), returns the rotation represented by the
         * quaternion as an angle about an arbitrary axis.  This returns the axis; it
         * is not normalized.
         */
        """
        pass

    def get_axis_normalized(self, LQuaterniond_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_axis_normalized(LQuaterniond self)
        
        /**
         * This, along with get_angle(), returns the rotation represented by the
         * quaternion as an angle about an arbitrary axis.  This returns the
         * normalized axis.
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_forward(self, LQuaterniond_self, int_cs): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_forward(LQuaterniond self, int cs)
        
        /**
         * Returns the orientation represented by this quaternion, expressed as a
         * forward vector.
         */
        """
        pass

    def get_hpr(self, LQuaterniond_self, int_cs): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_hpr(LQuaterniond self, int cs)
        
        /**
         * Extracts the equivalent Euler angles from the unit quaternion.
         */
        """
        pass

    def get_i(self, LQuaterniond_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_i(LQuaterniond self)
        
        /**
         *
         */
        """
        pass

    def get_j(self, LQuaterniond_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_j(LQuaterniond self)
        
        /**
         *
         */
        """
        pass

    def get_k(self, LQuaterniond_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_k(LQuaterniond self)
        
        /**
         *
         */
        """
        pass

    def get_r(self, LQuaterniond_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_r(LQuaterniond self)
        
        /**
         *
         */
        """
        pass

    def get_right(self, LQuaterniond_self, int_cs): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_right(LQuaterniond self, int cs)
        
        /**
         * Returns the orientation represented by this quaternion, expressed as a
         * right vector.
         */
        """
        pass

    def get_up(self, LQuaterniond_self, int_cs): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_up(LQuaterniond self, int cs)
        
        /**
         * Returns the orientation represented by this quaternion, expressed as an up
         * vector.
         */
        """
        pass

    def identQuat(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        ident_quat()
        
        /**
         * Returns an identity quaternion.
         */
        """
        pass

    def ident_quat(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        ident_quat()
        
        /**
         * Returns an identity quaternion.
         */
        """
        pass

    def invertFrom(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        invert_from(const LQuaterniond self, const LQuaterniond other)
        
        /**
         * Computes the inverse of the other quat, and stores the result in this quat.
         * This is a fully general operation and makes no assumptions about the type
         * of transform represented by the quat.
         *
         * The other quat must be a different object than this quat.  However, if you
         * need to invert a quat in place, see invert_in_place.
         *
         * The return value is true if the quat was successfully inverted, false if
         * there was a singularity.
         */
        """
        pass

    def invertInPlace(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        invert_in_place(const LQuaterniond self)
        
        /**
         * Inverts the current quat.  Returns true if the inverse is successful, false
         * if the quat was singular.
         */
        """
        pass

    def invert_from(self, const_LQuaterniond_self, const_LQuaterniond_other): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        invert_from(const LQuaterniond self, const LQuaterniond other)
        
        /**
         * Computes the inverse of the other quat, and stores the result in this quat.
         * This is a fully general operation and makes no assumptions about the type
         * of transform represented by the quat.
         *
         * The other quat must be a different object than this quat.  However, if you
         * need to invert a quat in place, see invert_in_place.
         *
         * The return value is true if the quat was successfully inverted, false if
         * there was a singularity.
         */
        """
        pass

    def invert_in_place(self, const_LQuaterniond_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        invert_in_place(const LQuaterniond self)
        
        /**
         * Inverts the current quat.  Returns true if the inverse is successful, false
         * if the quat was singular.
         */
        """
        pass

    def isAlmostIdentity(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_almost_identity(LQuaterniond self, double tolerance)
        
        /**
         * Returns true if this quaternion represents the identity transformation
         * within a given tolerance.
         */
        """
        pass

    def isIdentity(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_identity(LQuaterniond self)
        
        /**
         * Returns true if this quaternion represents the identity transformation: no
         * rotation.
         */
        """
        pass

    def isSameDirection(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_same_direction(LQuaterniond self, const LQuaterniond other)
        
        /**
         * Returns true if two quaternions represent the same rotation within a
         * default tolerance based on the numeric type.
         */
        """
        pass

    def is_almost_identity(self, LQuaterniond_self, double_tolerance): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_almost_identity(LQuaterniond self, double tolerance)
        
        /**
         * Returns true if this quaternion represents the identity transformation
         * within a given tolerance.
         */
        """
        pass

    def is_identity(self, LQuaterniond_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_identity(LQuaterniond self)
        
        /**
         * Returns true if this quaternion represents the identity transformation: no
         * rotation.
         */
        """
        pass

    def is_same_direction(self, LQuaterniond_self, const_LQuaterniond_other): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_same_direction(LQuaterniond self, const LQuaterniond other)
        
        /**
         * Returns true if two quaternions represent the same rotation within a
         * default tolerance based on the numeric type.
         */
        """
        pass

    def multiply(self, LQuaterniond_self, const_LQuaterniond_rhs): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        multiply(LQuaterniond self, const LQuaterniond rhs)
        
        /**
         * actual multiply call (non virtual)
         */
        """
        pass

    def normalize(self, const_LQuaterniond_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        normalize(const LQuaterniond self)
        
        /**
         *
         */
        """
        pass

    def output(self, LQuaterniond_self, ostream_param0): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        output(LQuaterniond self, ostream param0)
        
        /**
         *
         */
        """
        pass

    def pureImaginary(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        pure_imaginary(const LVector3d v)
        
        /**
         *
         */
        """
        pass

    def pure_imaginary(self, const_LVector3d_v): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        pure_imaginary(const LVector3d v)
        
        /**
         *
         */
        """
        pass

    def setFromAxisAngle(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_from_axis_angle(const LQuaterniond self, double angle_deg, const LVector3d axis)
        
        /**
         * angle_deg is the angle about the axis in degrees.  axis must be normalized.
         */
        """
        pass

    def setFromAxisAngleRad(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_from_axis_angle_rad(const LQuaterniond self, double angle_rad, const LVector3d axis)
        
        /**
         * angle_rad is the angle about the axis in radians.  axis must be normalized.
         */
        """
        pass

    def setFromMatrix(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_from_matrix(const LQuaterniond self, const LMatrix4d m)
        set_from_matrix(const LQuaterniond self, const LMatrix3d m)
        
        /**
         *
         */
        
        /**
         * Sets the quaternion according to the rotation represented by the matrix.
         * Originally we tried an algorithm presented by Do-While Jones, but that
         * turned out to be broken.  This is based on the quat lib from UNC.
         */
        """
        pass

    def setHpr(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_hpr(const LQuaterniond self, const LVecBase3d hpr, int cs)
        
        /**
         * Sets the quaternion as the unit quaternion that is equivalent to these
         * Euler angles.  (from Real-time Rendering, p.49)
         */
        """
        pass

    def setI(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_i(const LQuaterniond self, double i)
        
        /**
         *
         */
        """
        pass

    def setJ(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_j(const LQuaterniond self, double j)
        
        /**
         *
         */
        """
        pass

    def setK(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_k(const LQuaterniond self, double k)
        
        /**
         *
         */
        """
        pass

    def setR(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_r(const LQuaterniond self, double r)
        
        /**
         *
         */
        """
        pass

    def set_from_axis_angle(self, const_LQuaterniond_self, double_angle_deg, const_LVector3d_axis): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_from_axis_angle(const LQuaterniond self, double angle_deg, const LVector3d axis)
        
        /**
         * angle_deg is the angle about the axis in degrees.  axis must be normalized.
         */
        """
        pass

    def set_from_axis_angle_rad(self, const_LQuaterniond_self, double_angle_rad, const_LVector3d_axis): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_from_axis_angle_rad(const LQuaterniond self, double angle_rad, const LVector3d axis)
        
        /**
         * angle_rad is the angle about the axis in radians.  axis must be normalized.
         */
        """
        pass

    def set_from_matrix(self, const_LQuaterniond_self, const_LMatrix4d_m): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_from_matrix(const LQuaterniond self, const LMatrix4d m)
        set_from_matrix(const LQuaterniond self, const LMatrix3d m)
        
        /**
         *
         */
        
        /**
         * Sets the quaternion according to the rotation represented by the matrix.
         * Originally we tried an algorithm presented by Do-While Jones, but that
         * turned out to be broken.  This is based on the quat lib from UNC.
         */
        """
        pass

    def set_hpr(self, const_LQuaterniond_self, const_LVecBase3d_hpr, int_cs): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_hpr(const LQuaterniond self, const LVecBase3d hpr, int cs)
        
        /**
         * Sets the quaternion as the unit quaternion that is equivalent to these
         * Euler angles.  (from Real-time Rendering, p.49)
         */
        """
        pass

    def set_i(self, const_LQuaterniond_self, double_i): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_i(const LQuaterniond self, double i)
        
        /**
         *
         */
        """
        pass

    def set_j(self, const_LQuaterniond_self, double_j): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_j(const LQuaterniond self, double j)
        
        /**
         *
         */
        """
        pass

    def set_k(self, const_LQuaterniond_self, double_k): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_k(const LQuaterniond self, double k)
        
        /**
         *
         */
        """
        pass

    def set_r(self, const_LQuaterniond_self, double_r): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_r(const LQuaterniond self, double r)
        
        /**
         *
         */
        """
        pass

    def xform(self, LQuaterniond_self, const_LVecBase4d_v): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        xform(LQuaterniond self, const LVecBase4d v)
        xform(LQuaterniond self, const LVecBase3d v)
        
        /**
         * Transforms a 3-d vector by the indicated rotation
         */
        
        /**
         * Transforms a 4-d vector by the indicated rotation
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

    def __pow__(self, *args, **kwargs): # real signature unknown
        """ Return pow(self, value, mod). """
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

    def __rpow__(self, *args, **kwargs): # real signature unknown
        """ Return pow(value, self, mod). """
        pass

    def __rsub__(self, *args, **kwargs): # real signature unknown
        """ Return value-self. """
        pass

    def __rtruediv__(self, *args, **kwargs): # real signature unknown
        """ Return value/self. """
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    def __sub__(self, *args, **kwargs): # real signature unknown
        """ Return self-value. """
        pass

    def __truediv__(self, *args, **kwargs): # real signature unknown
        """ Return self/value. """
        pass

    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__add__': None, # (!) real value is "<slot wrapper '__add__' of 'panda3d.core.LQuaterniond' objects>"
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.core.LQuaterniond' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.core.LQuaterniond' objects>"
        '__doc__': '/**\n * This is the base quaternion class\n */',
        '__imul__': None, # (!) real value is "<slot wrapper '__imul__' of 'panda3d.core.LQuaterniond' objects>"
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.LQuaterniond' objects>"
        '__mul__': None, # (!) real value is "<slot wrapper '__mul__' of 'panda3d.core.LQuaterniond' objects>"
        '__neg__': None, # (!) real value is "<slot wrapper '__neg__' of 'panda3d.core.LQuaterniond' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE325860>'
        '__pow__': None, # (!) real value is "<slot wrapper '__pow__' of 'panda3d.core.LQuaterniond' objects>"
        '__radd__': None, # (!) real value is "<slot wrapper '__radd__' of 'panda3d.core.LQuaterniond' objects>"
        '__repr__': None, # (!) real value is "<slot wrapper '__repr__' of 'panda3d.core.LQuaterniond' objects>"
        '__rmul__': None, # (!) real value is "<slot wrapper '__rmul__' of 'panda3d.core.LQuaterniond' objects>"
        '__rpow__': None, # (!) real value is "<slot wrapper '__rpow__' of 'panda3d.core.LQuaterniond' objects>"
        '__rsub__': None, # (!) real value is "<slot wrapper '__rsub__' of 'panda3d.core.LQuaterniond' objects>"
        '__rtruediv__': None, # (!) real value is "<slot wrapper '__rtruediv__' of 'panda3d.core.LQuaterniond' objects>"
        '__str__': None, # (!) real value is "<slot wrapper '__str__' of 'panda3d.core.LQuaterniond' objects>"
        '__sub__': None, # (!) real value is "<slot wrapper '__sub__' of 'panda3d.core.LQuaterniond' objects>"
        '__truediv__': None, # (!) real value is "<slot wrapper '__truediv__' of 'panda3d.core.LQuaterniond' objects>"
        'almostEqual': None, # (!) real value is "<method 'almostEqual' of 'panda3d.core.LQuaterniond' objects>"
        'almostSameDirection': None, # (!) real value is "<method 'almostSameDirection' of 'panda3d.core.LQuaterniond' objects>"
        'almost_equal': None, # (!) real value is "<method 'almost_equal' of 'panda3d.core.LQuaterniond' objects>"
        'almost_same_direction': None, # (!) real value is "<method 'almost_same_direction' of 'panda3d.core.LQuaterniond' objects>"
        'angleDeg': None, # (!) real value is "<method 'angleDeg' of 'panda3d.core.LQuaterniond' objects>"
        'angleRad': None, # (!) real value is "<method 'angleRad' of 'panda3d.core.LQuaterniond' objects>"
        'angle_deg': None, # (!) real value is "<method 'angle_deg' of 'panda3d.core.LQuaterniond' objects>"
        'angle_rad': None, # (!) real value is "<method 'angle_rad' of 'panda3d.core.LQuaterniond' objects>"
        'conjugate': None, # (!) real value is "<method 'conjugate' of 'panda3d.core.LQuaterniond' objects>"
        'conjugateFrom': None, # (!) real value is "<method 'conjugateFrom' of 'panda3d.core.LQuaterniond' objects>"
        'conjugateInPlace': None, # (!) real value is "<method 'conjugateInPlace' of 'panda3d.core.LQuaterniond' objects>"
        'conjugate_from': None, # (!) real value is "<method 'conjugate_from' of 'panda3d.core.LQuaterniond' objects>"
        'conjugate_in_place': None, # (!) real value is "<method 'conjugate_in_place' of 'panda3d.core.LQuaterniond' objects>"
        'extractToMatrix': None, # (!) real value is "<method 'extractToMatrix' of 'panda3d.core.LQuaterniond' objects>"
        'extract_to_matrix': None, # (!) real value is "<method 'extract_to_matrix' of 'panda3d.core.LQuaterniond' objects>"
        'getAngle': None, # (!) real value is "<method 'getAngle' of 'panda3d.core.LQuaterniond' objects>"
        'getAngleRad': None, # (!) real value is "<method 'getAngleRad' of 'panda3d.core.LQuaterniond' objects>"
        'getAxis': None, # (!) real value is "<method 'getAxis' of 'panda3d.core.LQuaterniond' objects>"
        'getAxisNormalized': None, # (!) real value is "<method 'getAxisNormalized' of 'panda3d.core.LQuaterniond' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE325860>)>'
        'getForward': None, # (!) real value is "<method 'getForward' of 'panda3d.core.LQuaterniond' objects>"
        'getHpr': None, # (!) real value is "<method 'getHpr' of 'panda3d.core.LQuaterniond' objects>"
        'getI': None, # (!) real value is "<method 'getI' of 'panda3d.core.LQuaterniond' objects>"
        'getJ': None, # (!) real value is "<method 'getJ' of 'panda3d.core.LQuaterniond' objects>"
        'getK': None, # (!) real value is "<method 'getK' of 'panda3d.core.LQuaterniond' objects>"
        'getR': None, # (!) real value is "<method 'getR' of 'panda3d.core.LQuaterniond' objects>"
        'getRight': None, # (!) real value is "<method 'getRight' of 'panda3d.core.LQuaterniond' objects>"
        'getUp': None, # (!) real value is "<method 'getUp' of 'panda3d.core.LQuaterniond' objects>"
        'get_angle': None, # (!) real value is "<method 'get_angle' of 'panda3d.core.LQuaterniond' objects>"
        'get_angle_rad': None, # (!) real value is "<method 'get_angle_rad' of 'panda3d.core.LQuaterniond' objects>"
        'get_axis': None, # (!) real value is "<method 'get_axis' of 'panda3d.core.LQuaterniond' objects>"
        'get_axis_normalized': None, # (!) real value is "<method 'get_axis_normalized' of 'panda3d.core.LQuaterniond' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE325860>)>'
        'get_forward': None, # (!) real value is "<method 'get_forward' of 'panda3d.core.LQuaterniond' objects>"
        'get_hpr': None, # (!) real value is "<method 'get_hpr' of 'panda3d.core.LQuaterniond' objects>"
        'get_i': None, # (!) real value is "<method 'get_i' of 'panda3d.core.LQuaterniond' objects>"
        'get_j': None, # (!) real value is "<method 'get_j' of 'panda3d.core.LQuaterniond' objects>"
        'get_k': None, # (!) real value is "<method 'get_k' of 'panda3d.core.LQuaterniond' objects>"
        'get_r': None, # (!) real value is "<method 'get_r' of 'panda3d.core.LQuaterniond' objects>"
        'get_right': None, # (!) real value is "<method 'get_right' of 'panda3d.core.LQuaterniond' objects>"
        'get_up': None, # (!) real value is "<method 'get_up' of 'panda3d.core.LQuaterniond' objects>"
        'identQuat': None, # (!) real value is '<staticmethod(<built-in method identQuat of type object at 0x00007FFCFE325860>)>'
        'ident_quat': None, # (!) real value is '<staticmethod(<built-in method ident_quat of type object at 0x00007FFCFE325860>)>'
        'invertFrom': None, # (!) real value is "<method 'invertFrom' of 'panda3d.core.LQuaterniond' objects>"
        'invertInPlace': None, # (!) real value is "<method 'invertInPlace' of 'panda3d.core.LQuaterniond' objects>"
        'invert_from': None, # (!) real value is "<method 'invert_from' of 'panda3d.core.LQuaterniond' objects>"
        'invert_in_place': None, # (!) real value is "<method 'invert_in_place' of 'panda3d.core.LQuaterniond' objects>"
        'isAlmostIdentity': None, # (!) real value is "<method 'isAlmostIdentity' of 'panda3d.core.LQuaterniond' objects>"
        'isIdentity': None, # (!) real value is "<method 'isIdentity' of 'panda3d.core.LQuaterniond' objects>"
        'isSameDirection': None, # (!) real value is "<method 'isSameDirection' of 'panda3d.core.LQuaterniond' objects>"
        'is_almost_identity': None, # (!) real value is "<method 'is_almost_identity' of 'panda3d.core.LQuaterniond' objects>"
        'is_identity': None, # (!) real value is "<method 'is_identity' of 'panda3d.core.LQuaterniond' objects>"
        'is_same_direction': None, # (!) real value is "<method 'is_same_direction' of 'panda3d.core.LQuaterniond' objects>"
        'multiply': None, # (!) real value is "<method 'multiply' of 'panda3d.core.LQuaterniond' objects>"
        'normalize': None, # (!) real value is "<method 'normalize' of 'panda3d.core.LQuaterniond' objects>"
        'output': None, # (!) real value is "<method 'output' of 'panda3d.core.LQuaterniond' objects>"
        'pureImaginary': None, # (!) real value is '<staticmethod(<built-in method pureImaginary of type object at 0x00007FFCFE325860>)>'
        'pure_imaginary': None, # (!) real value is '<staticmethod(<built-in method pure_imaginary of type object at 0x00007FFCFE325860>)>'
        'setFromAxisAngle': None, # (!) real value is "<method 'setFromAxisAngle' of 'panda3d.core.LQuaterniond' objects>"
        'setFromAxisAngleRad': None, # (!) real value is "<method 'setFromAxisAngleRad' of 'panda3d.core.LQuaterniond' objects>"
        'setFromMatrix': None, # (!) real value is "<method 'setFromMatrix' of 'panda3d.core.LQuaterniond' objects>"
        'setHpr': None, # (!) real value is "<method 'setHpr' of 'panda3d.core.LQuaterniond' objects>"
        'setI': None, # (!) real value is "<method 'setI' of 'panda3d.core.LQuaterniond' objects>"
        'setJ': None, # (!) real value is "<method 'setJ' of 'panda3d.core.LQuaterniond' objects>"
        'setK': None, # (!) real value is "<method 'setK' of 'panda3d.core.LQuaterniond' objects>"
        'setR': None, # (!) real value is "<method 'setR' of 'panda3d.core.LQuaterniond' objects>"
        'set_from_axis_angle': None, # (!) real value is "<method 'set_from_axis_angle' of 'panda3d.core.LQuaterniond' objects>"
        'set_from_axis_angle_rad': None, # (!) real value is "<method 'set_from_axis_angle_rad' of 'panda3d.core.LQuaterniond' objects>"
        'set_from_matrix': None, # (!) real value is "<method 'set_from_matrix' of 'panda3d.core.LQuaterniond' objects>"
        'set_hpr': None, # (!) real value is "<method 'set_hpr' of 'panda3d.core.LQuaterniond' objects>"
        'set_i': None, # (!) real value is "<method 'set_i' of 'panda3d.core.LQuaterniond' objects>"
        'set_j': None, # (!) real value is "<method 'set_j' of 'panda3d.core.LQuaterniond' objects>"
        'set_k': None, # (!) real value is "<method 'set_k' of 'panda3d.core.LQuaterniond' objects>"
        'set_r': None, # (!) real value is "<method 'set_r' of 'panda3d.core.LQuaterniond' objects>"
        'xform': None, # (!) real value is "<method 'xform' of 'panda3d.core.LQuaterniond' objects>"
    }


