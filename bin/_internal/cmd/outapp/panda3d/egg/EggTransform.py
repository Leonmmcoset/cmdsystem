# encoding: utf-8
# module panda3d.egg
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\egg.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import panda3d.core as __panda3d_core


class EggTransform(__dtoolconfig.DTOOL_SUPER_BASE):
    """
    /**
     * This represents the <Transform> entry of a group or texture node: a list of
     * component transform operations, applied in order, that describe a net
     * transform matrix.
     *
     * This may be either a 3-d transform, and therefore described by a 4x4
     * matrix, or a 2-d transform, described by a 3x3 matrix.
     */
    """
    def addMatrix3(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_matrix3(const EggTransform self, const LMatrix3d mat)
        
        /**
         * Appends an arbitrary 3x3 matrix to the current transform.
         */
        """
        pass

    def addMatrix4(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_matrix4(const EggTransform self, const LMatrix4d mat)
        
        /**
         * Appends an arbitrary 4x4 matrix to the current transform.
         */
        """
        pass

    def addRotate2d(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_rotate2d(const EggTransform self, double angle)
        
        /**
         * Appends a 2-d rotation to the current transform.  The rotation angle is
         * specified in degrees counterclockwise about the origin.
         */
        """
        pass

    def addRotate3d(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_rotate3d(const EggTransform self, const LQuaterniond quat)
        add_rotate3d(const EggTransform self, double angle, const LVector3d axis)
        
        /**
         * Appends a 3-d rotation about an arbitrary axis to the current transform.
         * The rotation angle is specified in degrees counterclockwise about the axis.
         */
        
        /**
         * Appends an arbitrary 3-d rotation to the current transform, expressed as a
         * quaternion.  This is converted to axis-angle notation for the egg file.
         */
        """
        pass

    def addRotx(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_rotx(const EggTransform self, double angle)
        
        /**
         * Appends a rotation about the X axis to the current transform.  The rotation
         * angle is specified in degrees counterclockwise about the axis.
         */
        """
        pass

    def addRoty(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_roty(const EggTransform self, double angle)
        
        /**
         * Appends a rotation about the Y axis to the current transform.  The rotation
         * angle is specified in degrees counterclockwise about the axis.
         */
        """
        pass

    def addRotz(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_rotz(const EggTransform self, double angle)
        
        /**
         * Appends a rotation about the Z axis to the current transform.  The rotation
         * angle is specified in degrees counterclockwise about the axis.
         */
        """
        pass

    def addScale2d(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_scale2d(const EggTransform self, const LVecBase2d scale)
        
        /**
         * Appends a possibly non-uniform scale to the current transform.
         */
        """
        pass

    def addScale3d(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_scale3d(const EggTransform self, const LVecBase3d scale)
        
        /**
         * Appends a possibly non-uniform scale to the current transform.
         */
        """
        pass

    def addTranslate2d(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_translate2d(const EggTransform self, const LVector2d translate)
        
        /**
         * Appends a 2-d translation operation to the current transform.
         */
        """
        pass

    def addTranslate3d(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_translate3d(const EggTransform self, const LVector3d translate)
        
        /**
         * Appends a 3-d translation operation to the current transform.
         */
        """
        pass

    def addUniformScale(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_uniform_scale(const EggTransform self, double scale)
        
        /**
         * Appends a uniform scale to the current transform.
         */
        """
        pass

    def add_matrix3(self, const_EggTransform_self, const_LMatrix3d_mat): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_matrix3(const EggTransform self, const LMatrix3d mat)
        
        /**
         * Appends an arbitrary 3x3 matrix to the current transform.
         */
        """
        pass

    def add_matrix4(self, const_EggTransform_self, const_LMatrix4d_mat): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_matrix4(const EggTransform self, const LMatrix4d mat)
        
        /**
         * Appends an arbitrary 4x4 matrix to the current transform.
         */
        """
        pass

    def add_rotate2d(self, const_EggTransform_self, double_angle): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_rotate2d(const EggTransform self, double angle)
        
        /**
         * Appends a 2-d rotation to the current transform.  The rotation angle is
         * specified in degrees counterclockwise about the origin.
         */
        """
        pass

    def add_rotate3d(self, const_EggTransform_self, const_LQuaterniond_quat): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_rotate3d(const EggTransform self, const LQuaterniond quat)
        add_rotate3d(const EggTransform self, double angle, const LVector3d axis)
        
        /**
         * Appends a 3-d rotation about an arbitrary axis to the current transform.
         * The rotation angle is specified in degrees counterclockwise about the axis.
         */
        
        /**
         * Appends an arbitrary 3-d rotation to the current transform, expressed as a
         * quaternion.  This is converted to axis-angle notation for the egg file.
         */
        """
        pass

    def add_rotx(self, const_EggTransform_self, double_angle): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_rotx(const EggTransform self, double angle)
        
        /**
         * Appends a rotation about the X axis to the current transform.  The rotation
         * angle is specified in degrees counterclockwise about the axis.
         */
        """
        pass

    def add_roty(self, const_EggTransform_self, double_angle): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_roty(const EggTransform self, double angle)
        
        /**
         * Appends a rotation about the Y axis to the current transform.  The rotation
         * angle is specified in degrees counterclockwise about the axis.
         */
        """
        pass

    def add_rotz(self, const_EggTransform_self, double_angle): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_rotz(const EggTransform self, double angle)
        
        /**
         * Appends a rotation about the Z axis to the current transform.  The rotation
         * angle is specified in degrees counterclockwise about the axis.
         */
        """
        pass

    def add_scale2d(self, const_EggTransform_self, const_LVecBase2d_scale): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_scale2d(const EggTransform self, const LVecBase2d scale)
        
        /**
         * Appends a possibly non-uniform scale to the current transform.
         */
        """
        pass

    def add_scale3d(self, const_EggTransform_self, const_LVecBase3d_scale): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_scale3d(const EggTransform self, const LVecBase3d scale)
        
        /**
         * Appends a possibly non-uniform scale to the current transform.
         */
        """
        pass

    def add_translate2d(self, const_EggTransform_self, const_LVector2d_translate): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_translate2d(const EggTransform self, const LVector2d translate)
        
        /**
         * Appends a 2-d translation operation to the current transform.
         */
        """
        pass

    def add_translate3d(self, const_EggTransform_self, const_LVector3d_translate): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_translate3d(const EggTransform self, const LVector3d translate)
        
        /**
         * Appends a 3-d translation operation to the current transform.
         */
        """
        pass

    def add_uniform_scale(self, const_EggTransform_self, double_scale): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_uniform_scale(const EggTransform self, double scale)
        
        /**
         * Appends a uniform scale to the current transform.
         */
        """
        pass

    def assign(self, const_EggTransform_self, const_EggTransform_copy): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        assign(const EggTransform self, const EggTransform copy)
        
        /**
         *
         */
        """
        pass

    def clearTransform(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_transform(const EggTransform self)
        
        /**
         * Resets the transform to empty, identity.
         */
        """
        pass

    def clear_transform(self, const_EggTransform_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_transform(const EggTransform self)
        
        /**
         * Resets the transform to empty, identity.
         */
        """
        pass

    def getComponentMat3(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_component_mat3(EggTransform self, int n)
        
        /**
         * Returns the 3x3 matrix associated with the nth component.  It is an error
         * to call this if the component type is not CT_matrix3.
         */
        """
        pass

    def getComponentMat4(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_component_mat4(EggTransform self, int n)
        
        /**
         * Returns the 4x4 matrix associated with the nth component.  It is an error
         * to call this if the component type is not CT_matrix4.
         */
        """
        pass

    def getComponentNumber(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_component_number(EggTransform self, int n)
        
        /**
         * Returns the solitary number associated with the nth component.  In the case
         * of a rotation, this is the angle in degrees to rotate; in the case of
         * uniform scale, this is the amount of the scale.  Other types do not use
         * this property.
         */
        """
        pass

    def getComponentType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_component_type(EggTransform self, int n)
        
        /**
         * Returns the type of the nth component.
         */
        """
        pass

    def getComponentVec2(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_component_vec2(EggTransform self, int n)
        
        /**
         * Returns the 2-component vector associated with the nth component.  This may
         * be the translate vector, rotate axis, or non-uniform scale.  It is an error
         * to call this if the component type does not use a 2-d vector property.
         */
        """
        pass

    def getComponentVec3(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_component_vec3(EggTransform self, int n)
        
        /**
         * Returns the 3-component vector associated with the nth component.  This may
         * be the translate vector, rotate axis, or non-uniform scale.  It is an error
         * to call this if the component type does not use a 3-d vector property.
         */
        """
        pass

    def getNumComponents(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_components(EggTransform self)
        
        /**
         * Returns the number of components that make up the transform.
         */
        """
        pass

    def getTransform2d(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_transform2d(EggTransform self)
        
        /**
         * Returns the overall transform as a 3x3 matrix.  It is an error to call this
         * if has_transform3d() is true.
         */
        """
        pass

    def getTransform3d(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_transform3d(EggTransform self)
        
        /**
         * Returns the overall transform as a 4x4 matrix.  It is valid to call this
         * even if has_transform2d() is true; in this case, the 3x3 transform will be
         * expanded to a 4x4 matrix.
         */
        """
        pass

    def get_component_mat3(self, EggTransform_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_component_mat3(EggTransform self, int n)
        
        /**
         * Returns the 3x3 matrix associated with the nth component.  It is an error
         * to call this if the component type is not CT_matrix3.
         */
        """
        pass

    def get_component_mat4(self, EggTransform_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_component_mat4(EggTransform self, int n)
        
        /**
         * Returns the 4x4 matrix associated with the nth component.  It is an error
         * to call this if the component type is not CT_matrix4.
         */
        """
        pass

    def get_component_number(self, EggTransform_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_component_number(EggTransform self, int n)
        
        /**
         * Returns the solitary number associated with the nth component.  In the case
         * of a rotation, this is the angle in degrees to rotate; in the case of
         * uniform scale, this is the amount of the scale.  Other types do not use
         * this property.
         */
        """
        pass

    def get_component_type(self, EggTransform_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_component_type(EggTransform self, int n)
        
        /**
         * Returns the type of the nth component.
         */
        """
        pass

    def get_component_vec2(self, EggTransform_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_component_vec2(EggTransform self, int n)
        
        /**
         * Returns the 2-component vector associated with the nth component.  This may
         * be the translate vector, rotate axis, or non-uniform scale.  It is an error
         * to call this if the component type does not use a 2-d vector property.
         */
        """
        pass

    def get_component_vec3(self, EggTransform_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_component_vec3(EggTransform self, int n)
        
        /**
         * Returns the 3-component vector associated with the nth component.  This may
         * be the translate vector, rotate axis, or non-uniform scale.  It is an error
         * to call this if the component type does not use a 3-d vector property.
         */
        """
        pass

    def get_num_components(self, EggTransform_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_components(EggTransform self)
        
        /**
         * Returns the number of components that make up the transform.
         */
        """
        pass

    def get_transform2d(self, EggTransform_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_transform2d(EggTransform self)
        
        /**
         * Returns the overall transform as a 3x3 matrix.  It is an error to call this
         * if has_transform3d() is true.
         */
        """
        pass

    def get_transform3d(self, EggTransform_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_transform3d(EggTransform self)
        
        /**
         * Returns the overall transform as a 4x4 matrix.  It is valid to call this
         * even if has_transform2d() is true; in this case, the 3x3 transform will be
         * expanded to a 4x4 matrix.
         */
        """
        pass

    def hasTransform(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_transform(EggTransform self)
        
        /**
         * Returns true if the transform is nonempty, false if it is empty (no
         * transform components have been added).  This is true for either a 2-d or a
         * 3-d transform.
         */
        """
        pass

    def hasTransform2d(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_transform2d(EggTransform self)
        
        /**
         * Returns true if the transform is specified as a 2-d transform, e.g.  with a
         * 3x3 matrix, or false if it is specified as a 3-d transform (with a 4x4
         * matrix), or not specified at all.
         *
         * Normally, EggTextures have a 2-d matrix (but occasionally they use a 3-d
         * matrix), and EggGroups always have a 3-d matrix.
         */
        """
        pass

    def hasTransform3d(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_transform3d(EggTransform self)
        
        /**
         * Returns true if the transform is specified as a 3-d transform, e.g.  with a
         * 4x4 matrix, or false if it is specified as a 2-d transform (with a 2x2
         * matrix), or not specified at all.
         *
         * Normally, EggTextures have a 3-d matrix (but occasionally they use a 3-d
         * matrix), and EggGroups always have a 3-d matrix.
         */
        """
        pass

    def has_transform(self, EggTransform_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_transform(EggTransform self)
        
        /**
         * Returns true if the transform is nonempty, false if it is empty (no
         * transform components have been added).  This is true for either a 2-d or a
         * 3-d transform.
         */
        """
        pass

    def has_transform2d(self, EggTransform_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_transform2d(EggTransform self)
        
        /**
         * Returns true if the transform is specified as a 2-d transform, e.g.  with a
         * 3x3 matrix, or false if it is specified as a 3-d transform (with a 4x4
         * matrix), or not specified at all.
         *
         * Normally, EggTextures have a 2-d matrix (but occasionally they use a 3-d
         * matrix), and EggGroups always have a 3-d matrix.
         */
        """
        pass

    def has_transform3d(self, EggTransform_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_transform3d(EggTransform self)
        
        /**
         * Returns true if the transform is specified as a 3-d transform, e.g.  with a
         * 4x4 matrix, or false if it is specified as a 2-d transform (with a 2x2
         * matrix), or not specified at all.
         *
         * Normally, EggTextures have a 3-d matrix (but occasionally they use a 3-d
         * matrix), and EggGroups always have a 3-d matrix.
         */
        """
        pass

    def setTransform2d(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_transform2d(const EggTransform self, const LMatrix3d mat)
        
        /**
         * Sets the overall transform as a 3x3 matrix.  This completely replaces
         * whatever componentwise transform may have been defined.
         */
        """
        pass

    def setTransform3d(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_transform3d(const EggTransform self, const LMatrix4d mat)
        
        /**
         * Sets the overall transform as a 4x4 matrix.  This completely replaces
         * whatever componentwise transform may have been defined.
         */
        """
        pass

    def set_transform2d(self, const_EggTransform_self, const_LMatrix3d_mat): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_transform2d(const EggTransform self, const LMatrix3d mat)
        
        /**
         * Sets the overall transform as a 3x3 matrix.  This completely replaces
         * whatever componentwise transform may have been defined.
         */
        """
        pass

    def set_transform3d(self, const_EggTransform_self, const_LMatrix4d_mat): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_transform3d(const EggTransform self, const LMatrix4d mat)
        
        /**
         * Sets the overall transform as a 4x4 matrix.  This completely replaces
         * whatever componentwise transform may have been defined.
         */
        """
        pass

    def transformIsIdentity(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        transform_is_identity(EggTransform self)
        
        /**
         * Returns true if the described transform is identity, false otherwise.
         */
        """
        pass

    def transform_is_identity(self, EggTransform_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        transform_is_identity(EggTransform self)
        
        /**
         * Returns true if the described transform is identity, false otherwise.
         */
        """
        pass

    def write(self, EggTransform_self, ostream_out, int_indent_level, str_label): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        write(EggTransform self, ostream out, int indent_level, str label)
        
        /**
         * Writes the transform to the indicated stream in Egg format.
         */
        """
        pass

    def __copy__(self, *args, **kwargs): # real signature unknown
        pass

    def __deepcopy__(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    CTInvalid = 0
    CTMatrix3 = 11
    CTMatrix4 = 12
    CTRotate2d = 3
    CTRotate3d = 7
    CTRotx = 4
    CTRoty = 5
    CTRotz = 6
    CTScale2d = 8
    CTScale3d = 9
    CTTranslate2d = 1
    CTTranslate3d = 2
    CTUniformScale = 10
    CT_invalid = 0
    CT_matrix3 = 11
    CT_matrix4 = 12
    CT_rotate2d = 3
    CT_rotate3d = 7
    CT_rotx = 4
    CT_roty = 5
    CT_rotz = 6
    CT_scale2d = 8
    CT_scale3d = 9
    CT_translate2d = 1
    CT_translate3d = 2
    CT_uniform_scale = 10
    DtoolClassDict = {
        'CTInvalid': 0,
        'CTMatrix3': 11,
        'CTMatrix4': 12,
        'CTRotate2d': 3,
        'CTRotate3d': 7,
        'CTRotx': 4,
        'CTRoty': 5,
        'CTRotz': 6,
        'CTScale2d': 8,
        'CTScale3d': 9,
        'CTTranslate2d': 1,
        'CTTranslate3d': 2,
        'CTUniformScale': 10,
        'CT_invalid': 0,
        'CT_matrix3': 11,
        'CT_matrix4': 12,
        'CT_rotate2d': 3,
        'CT_rotate3d': 7,
        'CT_rotx': 4,
        'CT_roty': 5,
        'CT_rotz': 6,
        'CT_scale2d': 8,
        'CT_scale3d': 9,
        'CT_translate2d': 1,
        'CT_translate3d': 2,
        'CT_uniform_scale': 10,
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.egg.EggTransform' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.egg.EggTransform' objects>"
        '__doc__': '/**\n * This represents the <Transform> entry of a group or texture node: a list of\n * component transform operations, applied in order, that describe a net\n * transform matrix.\n *\n * This may be either a 3-d transform, and therefore described by a 4x4\n * matrix, or a 2-d transform, described by a 3x3 matrix.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.egg.EggTransform' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFDC68CDD40>'
        'addMatrix3': None, # (!) real value is "<method 'addMatrix3' of 'panda3d.egg.EggTransform' objects>"
        'addMatrix4': None, # (!) real value is "<method 'addMatrix4' of 'panda3d.egg.EggTransform' objects>"
        'addRotate2d': None, # (!) real value is "<method 'addRotate2d' of 'panda3d.egg.EggTransform' objects>"
        'addRotate3d': None, # (!) real value is "<method 'addRotate3d' of 'panda3d.egg.EggTransform' objects>"
        'addRotx': None, # (!) real value is "<method 'addRotx' of 'panda3d.egg.EggTransform' objects>"
        'addRoty': None, # (!) real value is "<method 'addRoty' of 'panda3d.egg.EggTransform' objects>"
        'addRotz': None, # (!) real value is "<method 'addRotz' of 'panda3d.egg.EggTransform' objects>"
        'addScale2d': None, # (!) real value is "<method 'addScale2d' of 'panda3d.egg.EggTransform' objects>"
        'addScale3d': None, # (!) real value is "<method 'addScale3d' of 'panda3d.egg.EggTransform' objects>"
        'addTranslate2d': None, # (!) real value is "<method 'addTranslate2d' of 'panda3d.egg.EggTransform' objects>"
        'addTranslate3d': None, # (!) real value is "<method 'addTranslate3d' of 'panda3d.egg.EggTransform' objects>"
        'addUniformScale': None, # (!) real value is "<method 'addUniformScale' of 'panda3d.egg.EggTransform' objects>"
        'add_matrix3': None, # (!) real value is "<method 'add_matrix3' of 'panda3d.egg.EggTransform' objects>"
        'add_matrix4': None, # (!) real value is "<method 'add_matrix4' of 'panda3d.egg.EggTransform' objects>"
        'add_rotate2d': None, # (!) real value is "<method 'add_rotate2d' of 'panda3d.egg.EggTransform' objects>"
        'add_rotate3d': None, # (!) real value is "<method 'add_rotate3d' of 'panda3d.egg.EggTransform' objects>"
        'add_rotx': None, # (!) real value is "<method 'add_rotx' of 'panda3d.egg.EggTransform' objects>"
        'add_roty': None, # (!) real value is "<method 'add_roty' of 'panda3d.egg.EggTransform' objects>"
        'add_rotz': None, # (!) real value is "<method 'add_rotz' of 'panda3d.egg.EggTransform' objects>"
        'add_scale2d': None, # (!) real value is "<method 'add_scale2d' of 'panda3d.egg.EggTransform' objects>"
        'add_scale3d': None, # (!) real value is "<method 'add_scale3d' of 'panda3d.egg.EggTransform' objects>"
        'add_translate2d': None, # (!) real value is "<method 'add_translate2d' of 'panda3d.egg.EggTransform' objects>"
        'add_translate3d': None, # (!) real value is "<method 'add_translate3d' of 'panda3d.egg.EggTransform' objects>"
        'add_uniform_scale': None, # (!) real value is "<method 'add_uniform_scale' of 'panda3d.egg.EggTransform' objects>"
        'assign': None, # (!) real value is "<method 'assign' of 'panda3d.egg.EggTransform' objects>"
        'clearTransform': None, # (!) real value is "<method 'clearTransform' of 'panda3d.egg.EggTransform' objects>"
        'clear_transform': None, # (!) real value is "<method 'clear_transform' of 'panda3d.egg.EggTransform' objects>"
        'getComponentMat3': None, # (!) real value is "<method 'getComponentMat3' of 'panda3d.egg.EggTransform' objects>"
        'getComponentMat4': None, # (!) real value is "<method 'getComponentMat4' of 'panda3d.egg.EggTransform' objects>"
        'getComponentNumber': None, # (!) real value is "<method 'getComponentNumber' of 'panda3d.egg.EggTransform' objects>"
        'getComponentType': None, # (!) real value is "<method 'getComponentType' of 'panda3d.egg.EggTransform' objects>"
        'getComponentVec2': None, # (!) real value is "<method 'getComponentVec2' of 'panda3d.egg.EggTransform' objects>"
        'getComponentVec3': None, # (!) real value is "<method 'getComponentVec3' of 'panda3d.egg.EggTransform' objects>"
        'getNumComponents': None, # (!) real value is "<method 'getNumComponents' of 'panda3d.egg.EggTransform' objects>"
        'getTransform2d': None, # (!) real value is "<method 'getTransform2d' of 'panda3d.egg.EggTransform' objects>"
        'getTransform3d': None, # (!) real value is "<method 'getTransform3d' of 'panda3d.egg.EggTransform' objects>"
        'get_component_mat3': None, # (!) real value is "<method 'get_component_mat3' of 'panda3d.egg.EggTransform' objects>"
        'get_component_mat4': None, # (!) real value is "<method 'get_component_mat4' of 'panda3d.egg.EggTransform' objects>"
        'get_component_number': None, # (!) real value is "<method 'get_component_number' of 'panda3d.egg.EggTransform' objects>"
        'get_component_type': None, # (!) real value is "<method 'get_component_type' of 'panda3d.egg.EggTransform' objects>"
        'get_component_vec2': None, # (!) real value is "<method 'get_component_vec2' of 'panda3d.egg.EggTransform' objects>"
        'get_component_vec3': None, # (!) real value is "<method 'get_component_vec3' of 'panda3d.egg.EggTransform' objects>"
        'get_num_components': None, # (!) real value is "<method 'get_num_components' of 'panda3d.egg.EggTransform' objects>"
        'get_transform2d': None, # (!) real value is "<method 'get_transform2d' of 'panda3d.egg.EggTransform' objects>"
        'get_transform3d': None, # (!) real value is "<method 'get_transform3d' of 'panda3d.egg.EggTransform' objects>"
        'hasTransform': None, # (!) real value is "<method 'hasTransform' of 'panda3d.egg.EggTransform' objects>"
        'hasTransform2d': None, # (!) real value is "<method 'hasTransform2d' of 'panda3d.egg.EggTransform' objects>"
        'hasTransform3d': None, # (!) real value is "<method 'hasTransform3d' of 'panda3d.egg.EggTransform' objects>"
        'has_transform': None, # (!) real value is "<method 'has_transform' of 'panda3d.egg.EggTransform' objects>"
        'has_transform2d': None, # (!) real value is "<method 'has_transform2d' of 'panda3d.egg.EggTransform' objects>"
        'has_transform3d': None, # (!) real value is "<method 'has_transform3d' of 'panda3d.egg.EggTransform' objects>"
        'setTransform2d': None, # (!) real value is "<method 'setTransform2d' of 'panda3d.egg.EggTransform' objects>"
        'setTransform3d': None, # (!) real value is "<method 'setTransform3d' of 'panda3d.egg.EggTransform' objects>"
        'set_transform2d': None, # (!) real value is "<method 'set_transform2d' of 'panda3d.egg.EggTransform' objects>"
        'set_transform3d': None, # (!) real value is "<method 'set_transform3d' of 'panda3d.egg.EggTransform' objects>"
        'transformIsIdentity': None, # (!) real value is "<method 'transformIsIdentity' of 'panda3d.egg.EggTransform' objects>"
        'transform_is_identity': None, # (!) real value is "<method 'transform_is_identity' of 'panda3d.egg.EggTransform' objects>"
        'write': None, # (!) real value is "<method 'write' of 'panda3d.egg.EggTransform' objects>"
    }


