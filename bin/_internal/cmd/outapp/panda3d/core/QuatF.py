# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .LVecBase4f import LVecBase4f

class QuatF(LVecBase4f):
    """
    /**
     * This is the base quaternion class
     */
    """
    def almostEqual(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        almost_equal(LQuaternionf self, const LQuaternionf other)
        almost_equal(LQuaternionf self, const LQuaternionf other, float threshold)
        
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
        almost_same_direction(LQuaternionf self, const LQuaternionf other, float threshold)
        
        /**
         * Returns true if two quaternions represent the same rotation within a
         * specified tolerance.
         */
        """
        pass

    def almost_equal(self, LQuaternionf_self, const_LQuaternionf_other): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        almost_equal(LQuaternionf self, const LQuaternionf other)
        almost_equal(LQuaternionf self, const LQuaternionf other, float threshold)
        
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

    def almost_same_direction(self, LQuaternionf_self, const_LQuaternionf_other, float_threshold): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        almost_same_direction(LQuaternionf self, const LQuaternionf other, float threshold)
        
        /**
         * Returns true if two quaternions represent the same rotation within a
         * specified tolerance.
         */
        """
        pass

    def angleDeg(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        angle_deg(LQuaternionf self, const LQuaternionf other)
        
        /**
         * Returns the angle between the orientation represented by this quaternion
         * and the other one, expressed in degrees.
         */
        """
        pass

    def angleRad(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        angle_rad(LQuaternionf self, const LQuaternionf other)
        
        /**
         * Returns the angle between the orientation represented by this quaternion
         * and the other one, expressed in radians.
         */
        """
        pass

    def angle_deg(self, LQuaternionf_self, const_LQuaternionf_other): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        angle_deg(LQuaternionf self, const LQuaternionf other)
        
        /**
         * Returns the angle between the orientation represented by this quaternion
         * and the other one, expressed in degrees.
         */
        """
        pass

    def angle_rad(self, LQuaternionf_self, const_LQuaternionf_other): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        angle_rad(LQuaternionf self, const LQuaternionf other)
        
        /**
         * Returns the angle between the orientation represented by this quaternion
         * and the other one, expressed in radians.
         */
        """
        pass

    def conjugate(self, LQuaternionf_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        conjugate(LQuaternionf self)
        
        /**
         * Returns the complex conjugate of this quat.
         */
        """
        pass

    def conjugateFrom(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        conjugate_from(const LQuaternionf self, const LQuaternionf other)
        
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
        conjugate_in_place(const LQuaternionf self)
        
        /**
         * Sets this to be the conjugate of the current quat.  Returns true if the
         * successful, false if the quat was singular.
         */
        """
        pass

    def conjugate_from(self, const_LQuaternionf_self, const_LQuaternionf_other): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        conjugate_from(const LQuaternionf self, const LQuaternionf other)
        
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

    def conjugate_in_place(self, const_LQuaternionf_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        conjugate_in_place(const LQuaternionf self)
        
        /**
         * Sets this to be the conjugate of the current quat.  Returns true if the
         * successful, false if the quat was singular.
         */
        """
        pass

    def extractToMatrix(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        extract_to_matrix(LQuaternionf self, LMatrix3f m)
        extract_to_matrix(LQuaternionf self, LMatrix4f m)
        
        /**
         * Based on the quat lib from VRPN.
         */
        
        /**
         * Based on the quat lib from VRPN.
         */
        """
        pass

    def extract_to_matrix(self, LQuaternionf_self, LMatrix3f_m): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        extract_to_matrix(LQuaternionf self, LMatrix3f m)
        extract_to_matrix(LQuaternionf self, LMatrix4f m)
        
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
        get_angle(LQuaternionf self)
        
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
        get_angle_rad(LQuaternionf self)
        
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
        get_axis(LQuaternionf self)
        
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
        get_axis_normalized(LQuaternionf self)
        
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
        get_forward(LQuaternionf self, int cs)
        
        /**
         * Returns the orientation represented by this quaternion, expressed as a
         * forward vector.
         */
        """
        pass

    def getHpr(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_hpr(LQuaternionf self, int cs)
        
        /**
         * Extracts the equivalent Euler angles from the unit quaternion.
         */
        """
        pass

    def getI(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_i(LQuaternionf self)
        
        /**
         *
         */
        """
        pass

    def getJ(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_j(LQuaternionf self)
        
        /**
         *
         */
        """
        pass

    def getK(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_k(LQuaternionf self)
        
        /**
         *
         */
        """
        pass

    def getR(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_r(LQuaternionf self)
        
        /**
         *
         */
        """
        pass

    def getRight(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_right(LQuaternionf self, int cs)
        
        /**
         * Returns the orientation represented by this quaternion, expressed as a
         * right vector.
         */
        """
        pass

    def getUp(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_up(LQuaternionf self, int cs)
        
        /**
         * Returns the orientation represented by this quaternion, expressed as an up
         * vector.
         */
        """
        pass

    def get_angle(self, LQuaternionf_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_angle(LQuaternionf self)
        
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

    def get_angle_rad(self, LQuaternionf_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_angle_rad(LQuaternionf self)
        
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

    def get_axis(self, LQuaternionf_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_axis(LQuaternionf self)
        
        /**
         * This, along with get_angle(), returns the rotation represented by the
         * quaternion as an angle about an arbitrary axis.  This returns the axis; it
         * is not normalized.
         */
        """
        pass

    def get_axis_normalized(self, LQuaternionf_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_axis_normalized(LQuaternionf self)
        
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

    def get_forward(self, LQuaternionf_self, int_cs): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_forward(LQuaternionf self, int cs)
        
        /**
         * Returns the orientation represented by this quaternion, expressed as a
         * forward vector.
         */
        """
        pass

    def get_hpr(self, LQuaternionf_self, int_cs): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_hpr(LQuaternionf self, int cs)
        
        /**
         * Extracts the equivalent Euler angles from the unit quaternion.
         */
        """
        pass

    def get_i(self, LQuaternionf_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_i(LQuaternionf self)
        
        /**
         *
         */
        """
        pass

    def get_j(self, LQuaternionf_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_j(LQuaternionf self)
        
        /**
         *
         */
        """
        pass

    def get_k(self, LQuaternionf_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_k(LQuaternionf self)
        
        /**
         *
         */
        """
        pass

    def get_r(self, LQuaternionf_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_r(LQuaternionf self)
        
        /**
         *
         */
        """
        pass

    def get_right(self, LQuaternionf_self, int_cs): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_right(LQuaternionf self, int cs)
        
        /**
         * Returns the orientation represented by this quaternion, expressed as a
         * right vector.
         */
        """
        pass

    def get_up(self, LQuaternionf_self, int_cs): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_up(LQuaternionf self, int cs)
        
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
        invert_from(const LQuaternionf self, const LQuaternionf other)
        
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
        invert_in_place(const LQuaternionf self)
        
        /**
         * Inverts the current quat.  Returns true if the inverse is successful, false
         * if the quat was singular.
         */
        """
        pass

    def invert_from(self, const_LQuaternionf_self, const_LQuaternionf_other): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        invert_from(const LQuaternionf self, const LQuaternionf other)
        
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

    def invert_in_place(self, const_LQuaternionf_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        invert_in_place(const LQuaternionf self)
        
        /**
         * Inverts the current quat.  Returns true if the inverse is successful, false
         * if the quat was singular.
         */
        """
        pass

    def isAlmostIdentity(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_almost_identity(LQuaternionf self, float tolerance)
        
        /**
         * Returns true if this quaternion represents the identity transformation
         * within a given tolerance.
         */
        """
        pass

    def isIdentity(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_identity(LQuaternionf self)
        
        /**
         * Returns true if this quaternion represents the identity transformation: no
         * rotation.
         */
        """
        pass

    def isSameDirection(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_same_direction(LQuaternionf self, const LQuaternionf other)
        
        /**
         * Returns true if two quaternions represent the same rotation within a
         * default tolerance based on the numeric type.
         */
        """
        pass

    def is_almost_identity(self, LQuaternionf_self, float_tolerance): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_almost_identity(LQuaternionf self, float tolerance)
        
        /**
         * Returns true if this quaternion represents the identity transformation
         * within a given tolerance.
         */
        """
        pass

    def is_identity(self, LQuaternionf_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_identity(LQuaternionf self)
        
        /**
         * Returns true if this quaternion represents the identity transformation: no
         * rotation.
         */
        """
        pass

    def is_same_direction(self, LQuaternionf_self, const_LQuaternionf_other): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_same_direction(LQuaternionf self, const LQuaternionf other)
        
        /**
         * Returns true if two quaternions represent the same rotation within a
         * default tolerance based on the numeric type.
         */
        """
        pass

    def multiply(self, LQuaternionf_self, const_LQuaternionf_rhs): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        multiply(LQuaternionf self, const LQuaternionf rhs)
        
        /**
         * actual multiply call (non virtual)
         */
        """
        pass

    def normalize(self, const_LQuaternionf_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        normalize(const LQuaternionf self)
        
        /**
         *
         */
        """
        pass

    def output(self, LQuaternionf_self, ostream_param0): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        output(LQuaternionf self, ostream param0)
        
        /**
         *
         */
        """
        pass

    def pureImaginary(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        pure_imaginary(const LVector3f v)
        
        /**
         *
         */
        """
        pass

    def pure_imaginary(self, const_LVector3f_v): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        pure_imaginary(const LVector3f v)
        
        /**
         *
         */
        """
        pass

    def setFromAxisAngle(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_from_axis_angle(const LQuaternionf self, float angle_deg, const LVector3f axis)
        
        /**
         * angle_deg is the angle about the axis in degrees.  axis must be normalized.
         */
        """
        pass

    def setFromAxisAngleRad(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_from_axis_angle_rad(const LQuaternionf self, float angle_rad, const LVector3f axis)
        
        /**
         * angle_rad is the angle about the axis in radians.  axis must be normalized.
         */
        """
        pass

    def setFromMatrix(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_from_matrix(const LQuaternionf self, const LMatrix4f m)
        set_from_matrix(const LQuaternionf self, const LMatrix3f m)
        
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
        set_hpr(const LQuaternionf self, const LVecBase3f hpr, int cs)
        
        /**
         * Sets the quaternion as the unit quaternion that is equivalent to these
         * Euler angles.  (from Real-time Rendering, p.49)
         */
        """
        pass

    def setI(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_i(const LQuaternionf self, float i)
        
        /**
         *
         */
        """
        pass

    def setJ(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_j(const LQuaternionf self, float j)
        
        /**
         *
         */
        """
        pass

    def setK(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_k(const LQuaternionf self, float k)
        
        /**
         *
         */
        """
        pass

    def setR(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_r(const LQuaternionf self, float r)
        
        /**
         *
         */
        """
        pass

    def set_from_axis_angle(self, const_LQuaternionf_self, float_angle_deg, const_LVector3f_axis): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_from_axis_angle(const LQuaternionf self, float angle_deg, const LVector3f axis)
        
        /**
         * angle_deg is the angle about the axis in degrees.  axis must be normalized.
         */
        """
        pass

    def set_from_axis_angle_rad(self, const_LQuaternionf_self, float_angle_rad, const_LVector3f_axis): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_from_axis_angle_rad(const LQuaternionf self, float angle_rad, const LVector3f axis)
        
        /**
         * angle_rad is the angle about the axis in radians.  axis must be normalized.
         */
        """
        pass

    def set_from_matrix(self, const_LQuaternionf_self, const_LMatrix4f_m): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_from_matrix(const LQuaternionf self, const LMatrix4f m)
        set_from_matrix(const LQuaternionf self, const LMatrix3f m)
        
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

    def set_hpr(self, const_LQuaternionf_self, const_LVecBase3f_hpr, int_cs): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_hpr(const LQuaternionf self, const LVecBase3f hpr, int cs)
        
        /**
         * Sets the quaternion as the unit quaternion that is equivalent to these
         * Euler angles.  (from Real-time Rendering, p.49)
         */
        """
        pass

    def set_i(self, const_LQuaternionf_self, float_i): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_i(const LQuaternionf self, float i)
        
        /**
         *
         */
        """
        pass

    def set_j(self, const_LQuaternionf_self, float_j): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_j(const LQuaternionf self, float j)
        
        /**
         *
         */
        """
        pass

    def set_k(self, const_LQuaternionf_self, float_k): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_k(const LQuaternionf self, float k)
        
        /**
         *
         */
        """
        pass

    def set_r(self, const_LQuaternionf_self, float_r): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_r(const LQuaternionf self, float r)
        
        /**
         *
         */
        """
        pass

    def xform(self, LQuaternionf_self, const_LVecBase3f_v): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        xform(LQuaternionf self, const LVecBase3f v)
        xform(LQuaternionf self, const LVecBase4f v)
        
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
        '__add__': None, # (!) real value is "<slot wrapper '__add__' of 'panda3d.core.LQuaternionf' objects>"
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.core.LQuaternionf' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.core.LQuaternionf' objects>"
        '__doc__': '/**\n * This is the base quaternion class\n */',
        '__imul__': None, # (!) real value is "<slot wrapper '__imul__' of 'panda3d.core.LQuaternionf' objects>"
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.LQuaternionf' objects>"
        '__mul__': None, # (!) real value is "<slot wrapper '__mul__' of 'panda3d.core.LQuaternionf' objects>"
        '__neg__': None, # (!) real value is "<slot wrapper '__neg__' of 'panda3d.core.LQuaternionf' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE325690>'
        '__pow__': None, # (!) real value is "<slot wrapper '__pow__' of 'panda3d.core.LQuaternionf' objects>"
        '__radd__': None, # (!) real value is "<slot wrapper '__radd__' of 'panda3d.core.LQuaternionf' objects>"
        '__repr__': None, # (!) real value is "<slot wrapper '__repr__' of 'panda3d.core.LQuaternionf' objects>"
        '__rmul__': None, # (!) real value is "<slot wrapper '__rmul__' of 'panda3d.core.LQuaternionf' objects>"
        '__rpow__': None, # (!) real value is "<slot wrapper '__rpow__' of 'panda3d.core.LQuaternionf' objects>"
        '__rsub__': None, # (!) real value is "<slot wrapper '__rsub__' of 'panda3d.core.LQuaternionf' objects>"
        '__rtruediv__': None, # (!) real value is "<slot wrapper '__rtruediv__' of 'panda3d.core.LQuaternionf' objects>"
        '__str__': None, # (!) real value is "<slot wrapper '__str__' of 'panda3d.core.LQuaternionf' objects>"
        '__sub__': None, # (!) real value is "<slot wrapper '__sub__' of 'panda3d.core.LQuaternionf' objects>"
        '__truediv__': None, # (!) real value is "<slot wrapper '__truediv__' of 'panda3d.core.LQuaternionf' objects>"
        'almostEqual': None, # (!) real value is "<method 'almostEqual' of 'panda3d.core.LQuaternionf' objects>"
        'almostSameDirection': None, # (!) real value is "<method 'almostSameDirection' of 'panda3d.core.LQuaternionf' objects>"
        'almost_equal': None, # (!) real value is "<method 'almost_equal' of 'panda3d.core.LQuaternionf' objects>"
        'almost_same_direction': None, # (!) real value is "<method 'almost_same_direction' of 'panda3d.core.LQuaternionf' objects>"
        'angleDeg': None, # (!) real value is "<method 'angleDeg' of 'panda3d.core.LQuaternionf' objects>"
        'angleRad': None, # (!) real value is "<method 'angleRad' of 'panda3d.core.LQuaternionf' objects>"
        'angle_deg': None, # (!) real value is "<method 'angle_deg' of 'panda3d.core.LQuaternionf' objects>"
        'angle_rad': None, # (!) real value is "<method 'angle_rad' of 'panda3d.core.LQuaternionf' objects>"
        'conjugate': None, # (!) real value is "<method 'conjugate' of 'panda3d.core.LQuaternionf' objects>"
        'conjugateFrom': None, # (!) real value is "<method 'conjugateFrom' of 'panda3d.core.LQuaternionf' objects>"
        'conjugateInPlace': None, # (!) real value is "<method 'conjugateInPlace' of 'panda3d.core.LQuaternionf' objects>"
        'conjugate_from': None, # (!) real value is "<method 'conjugate_from' of 'panda3d.core.LQuaternionf' objects>"
        'conjugate_in_place': None, # (!) real value is "<method 'conjugate_in_place' of 'panda3d.core.LQuaternionf' objects>"
        'extractToMatrix': None, # (!) real value is "<method 'extractToMatrix' of 'panda3d.core.LQuaternionf' objects>"
        'extract_to_matrix': None, # (!) real value is "<method 'extract_to_matrix' of 'panda3d.core.LQuaternionf' objects>"
        'getAngle': None, # (!) real value is "<method 'getAngle' of 'panda3d.core.LQuaternionf' objects>"
        'getAngleRad': None, # (!) real value is "<method 'getAngleRad' of 'panda3d.core.LQuaternionf' objects>"
        'getAxis': None, # (!) real value is "<method 'getAxis' of 'panda3d.core.LQuaternionf' objects>"
        'getAxisNormalized': None, # (!) real value is "<method 'getAxisNormalized' of 'panda3d.core.LQuaternionf' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE325690>)>'
        'getForward': None, # (!) real value is "<method 'getForward' of 'panda3d.core.LQuaternionf' objects>"
        'getHpr': None, # (!) real value is "<method 'getHpr' of 'panda3d.core.LQuaternionf' objects>"
        'getI': None, # (!) real value is "<method 'getI' of 'panda3d.core.LQuaternionf' objects>"
        'getJ': None, # (!) real value is "<method 'getJ' of 'panda3d.core.LQuaternionf' objects>"
        'getK': None, # (!) real value is "<method 'getK' of 'panda3d.core.LQuaternionf' objects>"
        'getR': None, # (!) real value is "<method 'getR' of 'panda3d.core.LQuaternionf' objects>"
        'getRight': None, # (!) real value is "<method 'getRight' of 'panda3d.core.LQuaternionf' objects>"
        'getUp': None, # (!) real value is "<method 'getUp' of 'panda3d.core.LQuaternionf' objects>"
        'get_angle': None, # (!) real value is "<method 'get_angle' of 'panda3d.core.LQuaternionf' objects>"
        'get_angle_rad': None, # (!) real value is "<method 'get_angle_rad' of 'panda3d.core.LQuaternionf' objects>"
        'get_axis': None, # (!) real value is "<method 'get_axis' of 'panda3d.core.LQuaternionf' objects>"
        'get_axis_normalized': None, # (!) real value is "<method 'get_axis_normalized' of 'panda3d.core.LQuaternionf' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE325690>)>'
        'get_forward': None, # (!) real value is "<method 'get_forward' of 'panda3d.core.LQuaternionf' objects>"
        'get_hpr': None, # (!) real value is "<method 'get_hpr' of 'panda3d.core.LQuaternionf' objects>"
        'get_i': None, # (!) real value is "<method 'get_i' of 'panda3d.core.LQuaternionf' objects>"
        'get_j': None, # (!) real value is "<method 'get_j' of 'panda3d.core.LQuaternionf' objects>"
        'get_k': None, # (!) real value is "<method 'get_k' of 'panda3d.core.LQuaternionf' objects>"
        'get_r': None, # (!) real value is "<method 'get_r' of 'panda3d.core.LQuaternionf' objects>"
        'get_right': None, # (!) real value is "<method 'get_right' of 'panda3d.core.LQuaternionf' objects>"
        'get_up': None, # (!) real value is "<method 'get_up' of 'panda3d.core.LQuaternionf' objects>"
        'identQuat': None, # (!) real value is '<staticmethod(<built-in method identQuat of type object at 0x00007FFCFE325690>)>'
        'ident_quat': None, # (!) real value is '<staticmethod(<built-in method ident_quat of type object at 0x00007FFCFE325690>)>'
        'invertFrom': None, # (!) real value is "<method 'invertFrom' of 'panda3d.core.LQuaternionf' objects>"
        'invertInPlace': None, # (!) real value is "<method 'invertInPlace' of 'panda3d.core.LQuaternionf' objects>"
        'invert_from': None, # (!) real value is "<method 'invert_from' of 'panda3d.core.LQuaternionf' objects>"
        'invert_in_place': None, # (!) real value is "<method 'invert_in_place' of 'panda3d.core.LQuaternionf' objects>"
        'isAlmostIdentity': None, # (!) real value is "<method 'isAlmostIdentity' of 'panda3d.core.LQuaternionf' objects>"
        'isIdentity': None, # (!) real value is "<method 'isIdentity' of 'panda3d.core.LQuaternionf' objects>"
        'isSameDirection': None, # (!) real value is "<method 'isSameDirection' of 'panda3d.core.LQuaternionf' objects>"
        'is_almost_identity': None, # (!) real value is "<method 'is_almost_identity' of 'panda3d.core.LQuaternionf' objects>"
        'is_identity': None, # (!) real value is "<method 'is_identity' of 'panda3d.core.LQuaternionf' objects>"
        'is_same_direction': None, # (!) real value is "<method 'is_same_direction' of 'panda3d.core.LQuaternionf' objects>"
        'multiply': None, # (!) real value is "<method 'multiply' of 'panda3d.core.LQuaternionf' objects>"
        'normalize': None, # (!) real value is "<method 'normalize' of 'panda3d.core.LQuaternionf' objects>"
        'output': None, # (!) real value is "<method 'output' of 'panda3d.core.LQuaternionf' objects>"
        'pureImaginary': None, # (!) real value is '<staticmethod(<built-in method pureImaginary of type object at 0x00007FFCFE325690>)>'
        'pure_imaginary': None, # (!) real value is '<staticmethod(<built-in method pure_imaginary of type object at 0x00007FFCFE325690>)>'
        'setFromAxisAngle': None, # (!) real value is "<method 'setFromAxisAngle' of 'panda3d.core.LQuaternionf' objects>"
        'setFromAxisAngleRad': None, # (!) real value is "<method 'setFromAxisAngleRad' of 'panda3d.core.LQuaternionf' objects>"
        'setFromMatrix': None, # (!) real value is "<method 'setFromMatrix' of 'panda3d.core.LQuaternionf' objects>"
        'setHpr': None, # (!) real value is "<method 'setHpr' of 'panda3d.core.LQuaternionf' objects>"
        'setI': None, # (!) real value is "<method 'setI' of 'panda3d.core.LQuaternionf' objects>"
        'setJ': None, # (!) real value is "<method 'setJ' of 'panda3d.core.LQuaternionf' objects>"
        'setK': None, # (!) real value is "<method 'setK' of 'panda3d.core.LQuaternionf' objects>"
        'setR': None, # (!) real value is "<method 'setR' of 'panda3d.core.LQuaternionf' objects>"
        'set_from_axis_angle': None, # (!) real value is "<method 'set_from_axis_angle' of 'panda3d.core.LQuaternionf' objects>"
        'set_from_axis_angle_rad': None, # (!) real value is "<method 'set_from_axis_angle_rad' of 'panda3d.core.LQuaternionf' objects>"
        'set_from_matrix': None, # (!) real value is "<method 'set_from_matrix' of 'panda3d.core.LQuaternionf' objects>"
        'set_hpr': None, # (!) real value is "<method 'set_hpr' of 'panda3d.core.LQuaternionf' objects>"
        'set_i': None, # (!) real value is "<method 'set_i' of 'panda3d.core.LQuaternionf' objects>"
        'set_j': None, # (!) real value is "<method 'set_j' of 'panda3d.core.LQuaternionf' objects>"
        'set_k': None, # (!) real value is "<method 'set_k' of 'panda3d.core.LQuaternionf' objects>"
        'set_r': None, # (!) real value is "<method 'set_r' of 'panda3d.core.LQuaternionf' objects>"
        'xform': None, # (!) real value is "<method 'xform' of 'panda3d.core.LQuaternionf' objects>"
    }


