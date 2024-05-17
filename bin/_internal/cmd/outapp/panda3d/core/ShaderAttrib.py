# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .RenderAttrib import RenderAttrib

class ShaderAttrib(RenderAttrib):
    """
    /**
     *
     */
    """
    def autoGlossOn(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        auto_gloss_on(ShaderAttrib self)
        
        /**
         *
         */
        """
        pass

    def autoGlowOn(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        auto_glow_on(ShaderAttrib self)
        
        /**
         *
         */
        """
        pass

    def autoNormalOn(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        auto_normal_on(ShaderAttrib self)
        """
        pass

    def autoRampOn(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        auto_ramp_on(ShaderAttrib self)
        
        /**
         *
         */
        """
        pass

    def autoShader(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        auto_shader(ShaderAttrib self)
        
        /**
         * If true, then this ShaderAttrib does not contain an explicit shader -
         * instead, it requests the automatic generation of a shader.
         */
        """
        pass

    def autoShadowOn(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        auto_shadow_on(ShaderAttrib self)
        
        /**
         *
         */
        """
        pass

    def auto_gloss_on(self, ShaderAttrib_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        auto_gloss_on(ShaderAttrib self)
        
        /**
         *
         */
        """
        pass

    def auto_glow_on(self, ShaderAttrib_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        auto_glow_on(ShaderAttrib self)
        
        /**
         *
         */
        """
        pass

    def auto_normal_on(self, ShaderAttrib_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        auto_normal_on(ShaderAttrib self)
        """
        pass

    def auto_ramp_on(self, ShaderAttrib_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        auto_ramp_on(ShaderAttrib self)
        
        /**
         *
         */
        """
        pass

    def auto_shader(self, ShaderAttrib_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        auto_shader(ShaderAttrib self)
        
        /**
         * If true, then this ShaderAttrib does not contain an explicit shader -
         * instead, it requests the automatic generation of a shader.
         */
        """
        pass

    def auto_shadow_on(self, ShaderAttrib_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        auto_shadow_on(ShaderAttrib self)
        
        /**
         *
         */
        """
        pass

    def clearAllShaderInputs(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_all_shader_inputs(ShaderAttrib self)
        
        /**
         * Clears all the shader inputs on the attrib.
         */
        """
        pass

    def clearFlag(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_flag(ShaderAttrib self, int flag)
        
        /**
         *
         */
        """
        pass

    def clearShader(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_shader(ShaderAttrib self)
        
        /**
         *
         */
        """
        pass

    def clearShaderInput(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_shader_input(ShaderAttrib self, const InternalName id)
        clear_shader_input(ShaderAttrib self, str id)
        
        /**
         *
         */
        
        /**
         *
         */
        """
        pass

    def clear_all_shader_inputs(self, ShaderAttrib_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_all_shader_inputs(ShaderAttrib self)
        
        /**
         * Clears all the shader inputs on the attrib.
         */
        """
        pass

    def clear_flag(self, ShaderAttrib_self, int_flag): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_flag(ShaderAttrib self, int flag)
        
        /**
         *
         */
        """
        pass

    def clear_shader(self, ShaderAttrib_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_shader(ShaderAttrib self)
        
        /**
         *
         */
        """
        pass

    def clear_shader_input(self, ShaderAttrib_self, const_InternalName_id): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_shader_input(ShaderAttrib self, const InternalName id)
        clear_shader_input(ShaderAttrib self, str id)
        
        /**
         *
         */
        
        /**
         *
         */
        """
        pass

    def getClassSlot(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_slot()
        """
        pass

    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getFlag(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_flag(ShaderAttrib self, int flag)
        
        /**
         *
         */
        """
        pass

    def getInstanceCount(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_instance_count(ShaderAttrib self)
        
        /**
         * Returns the number of geometry instances.  A value of 0 means not to use
         * instancing at all.
         */
        """
        pass

    def getShader(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_shader(ShaderAttrib self)
        
        /**
         * Returns the shader object associated with the node.  If get_override
         * returns true, but get_shader returns NULL, that means that this attribute
         * should disable the shader.
         */
        """
        pass

    def getShaderInput(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_shader_input(ShaderAttrib self, const InternalName id)
        get_shader_input(ShaderAttrib self, str id)
        
        /**
         * Returns the ShaderInput of the given name.  If no such name is found, this
         * function does not return NULL --- it returns the "blank" ShaderInput.
         */
        
        /**
         * Returns the ShaderInput of the given name.  If no such name is found, this
         * function does not return NULL --- it returns the "blank" ShaderInput.
         */
        """
        pass

    def getShaderInputBuffer(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_shader_input_buffer(ShaderAttrib self, const InternalName id)
        
        /**
         * Returns the ShaderInput as a ShaderBuffer.  Assertion fails if there is
         * none, or if it is not a ShaderBuffer.
         */
        """
        pass

    def getShaderInputMatrix(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_shader_input_matrix(ShaderAttrib self, const InternalName id, LMatrix4f matrix)
        
        /**
         * Returns the ShaderInput as a matrix.  Assertion fails if there is none, or
         * if it is not a matrix or NodePath.
         */
        """
        pass

    def getShaderInputNodepath(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_shader_input_nodepath(ShaderAttrib self, const InternalName id)
        
        /**
         * Returns the ShaderInput as a nodepath.  Assertion fails if there is none,
         * or if it is not a nodepath.
         */
        """
        pass

    def getShaderInputTexture(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_shader_input_texture(ShaderAttrib self, const InternalName id, SamplerState sampler)
        
        /**
         * Returns the ShaderInput as a texture.  Assertion fails if there is none, or
         * if it is not a texture.
         *
         * If sampler is not NULL, the sampler state to use for this texture is
         * assigned to it.
         */
        """
        pass

    def getShaderInputVector(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_shader_input_vector(ShaderAttrib self, InternalName id)
        
        /**
         * Returns the ShaderInput as a vector.  Assertion fails if there is none, or
         * if it is not a vector.
         */
        """
        pass

    def getShaderPriority(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_shader_priority(ShaderAttrib self)
        
        /**
         *
         */
        """
        pass

    def get_class_slot(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_slot()
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_flag(self, ShaderAttrib_self, int_flag): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_flag(ShaderAttrib self, int flag)
        
        /**
         *
         */
        """
        pass

    def get_instance_count(self, ShaderAttrib_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_instance_count(ShaderAttrib self)
        
        /**
         * Returns the number of geometry instances.  A value of 0 means not to use
         * instancing at all.
         */
        """
        pass

    def get_shader(self, ShaderAttrib_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_shader(ShaderAttrib self)
        
        /**
         * Returns the shader object associated with the node.  If get_override
         * returns true, but get_shader returns NULL, that means that this attribute
         * should disable the shader.
         */
        """
        pass

    def get_shader_input(self, ShaderAttrib_self, const_InternalName_id): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_shader_input(ShaderAttrib self, const InternalName id)
        get_shader_input(ShaderAttrib self, str id)
        
        /**
         * Returns the ShaderInput of the given name.  If no such name is found, this
         * function does not return NULL --- it returns the "blank" ShaderInput.
         */
        
        /**
         * Returns the ShaderInput of the given name.  If no such name is found, this
         * function does not return NULL --- it returns the "blank" ShaderInput.
         */
        """
        pass

    def get_shader_input_buffer(self, ShaderAttrib_self, const_InternalName_id): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_shader_input_buffer(ShaderAttrib self, const InternalName id)
        
        /**
         * Returns the ShaderInput as a ShaderBuffer.  Assertion fails if there is
         * none, or if it is not a ShaderBuffer.
         */
        """
        pass

    def get_shader_input_matrix(self, ShaderAttrib_self, const_InternalName_id, LMatrix4f_matrix): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_shader_input_matrix(ShaderAttrib self, const InternalName id, LMatrix4f matrix)
        
        /**
         * Returns the ShaderInput as a matrix.  Assertion fails if there is none, or
         * if it is not a matrix or NodePath.
         */
        """
        pass

    def get_shader_input_nodepath(self, ShaderAttrib_self, const_InternalName_id): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_shader_input_nodepath(ShaderAttrib self, const InternalName id)
        
        /**
         * Returns the ShaderInput as a nodepath.  Assertion fails if there is none,
         * or if it is not a nodepath.
         */
        """
        pass

    def get_shader_input_texture(self, ShaderAttrib_self, const_InternalName_id, SamplerState_sampler): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_shader_input_texture(ShaderAttrib self, const InternalName id, SamplerState sampler)
        
        /**
         * Returns the ShaderInput as a texture.  Assertion fails if there is none, or
         * if it is not a texture.
         *
         * If sampler is not NULL, the sampler state to use for this texture is
         * assigned to it.
         */
        """
        pass

    def get_shader_input_vector(self, ShaderAttrib_self, InternalName_id): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_shader_input_vector(ShaderAttrib self, InternalName id)
        
        /**
         * Returns the ShaderInput as a vector.  Assertion fails if there is none, or
         * if it is not a vector.
         */
        """
        pass

    def get_shader_priority(self, ShaderAttrib_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_shader_priority(ShaderAttrib self)
        
        /**
         *
         */
        """
        pass

    def hasShader(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_shader(ShaderAttrib self)
        
        /**
         * If true, the shader field of this attribute overrides the shader field of
         * the parent attribute.
         */
        """
        pass

    def hasShaderInput(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_shader_input(ShaderAttrib self, const InternalName id)
        
        /**
         * Returns true if there is a ShaderInput of the given name.
         */
        """
        pass

    def has_shader(self, ShaderAttrib_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_shader(ShaderAttrib self)
        
        /**
         * If true, the shader field of this attribute overrides the shader field of
         * the parent attribute.
         */
        """
        pass

    def has_shader_input(self, ShaderAttrib_self, const_InternalName_id): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_shader_input(ShaderAttrib self, const InternalName id)
        
        /**
         * Returns true if there is a ShaderInput of the given name.
         */
        """
        pass

    def make(self, const_Shader_shader, int_priority): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        make(const Shader shader, int priority)
        
        /**
         * Constructs a new ShaderAttrib object with nothing set.
         */
        """
        pass

    def makeDefault(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        make_default()
        
        /**
         * Returns a RenderAttrib that corresponds to whatever the standard default
         * properties for render attributes of this type ought to be.
         */
        """
        pass

    def makeOff(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        make_off()
        
        /**
         * Constructs a new ShaderAttrib object that disables the use of shaders (it
         * does not clear out all shader data, however.)
         */
        """
        pass

    def make_default(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        make_default()
        
        /**
         * Returns a RenderAttrib that corresponds to whatever the standard default
         * properties for render attributes of this type ought to be.
         */
        """
        pass

    def make_off(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        make_off()
        
        /**
         * Constructs a new ShaderAttrib object that disables the use of shaders (it
         * does not clear out all shader data, however.)
         */
        """
        pass

    def registerWithReadFactory(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        register_with_read_factory()
        
        /**
         * Factory method to generate a Shader object
         */
        """
        pass

    def register_with_read_factory(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        register_with_read_factory()
        
        /**
         * Factory method to generate a Shader object
         */
        """
        pass

    def setFlag(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_flag(ShaderAttrib self, int flag, bool value)
        
        /**
         *
         */
        """
        pass

    def setInstanceCount(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_instance_count(ShaderAttrib self, int instance_count)
        
        /**
         * Sets the geometry instance count.  Do not confuse this with instanceTo,
         * which is used for animation instancing, and has nothing to do with this.  A
         * value of 0 means not to use instancing at all.
         */
        """
        pass

    def setShader(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_shader(ShaderAttrib self, const Shader s, int priority)
        
        /**
         *
         */
        """
        pass

    def setShaderAuto(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_shader_auto(ShaderAttrib self)
        set_shader_auto(ShaderAttrib self, BitMask shader_switch, int priority)
        set_shader_auto(ShaderAttrib self, int priority)
        
        /**
         *
         */
        
        /**
         * Set auto shader with bitmask to customize use, e.g., to keep normal, glow,
         * etc., on or off
         */
        """
        pass

    def setShaderInput(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_shader_input(ShaderAttrib self, const ShaderInput input)
        set_shader_input(ShaderAttrib self, const InternalName param0, object param1, int priority)
        
        // Shader Inputs
        
        /**
         *
         */
        
        /**
         *
         */
        
        /**
         *
         */
        
        /**
         *
         */
        
        /**
         *
         */
        
        /**
         *
         */
        
        /**
         *
         */
        
        /**
         *
         */
        
        /**
         *
         */
        
        /**
         *
         */
        
        /**
         *
         */
        
        /**
         *
         */
        
        /**
         *
         */
        
        /**
         *
         */
        
        /**
         *
         */
        
        /**
         *
         */
        
        /**
         *
         */
        """
        pass

    def setShaderInputs(self, *args, **kwargs): # real signature unknown
        pass

    def setShaderOff(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_shader_off(ShaderAttrib self, int priority)
        
        /**
         *
         */
        """
        pass

    def set_flag(self, ShaderAttrib_self, int_flag, bool_value): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_flag(ShaderAttrib self, int flag, bool value)
        
        /**
         *
         */
        """
        pass

    def set_instance_count(self, ShaderAttrib_self, int_instance_count): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_instance_count(ShaderAttrib self, int instance_count)
        
        /**
         * Sets the geometry instance count.  Do not confuse this with instanceTo,
         * which is used for animation instancing, and has nothing to do with this.  A
         * value of 0 means not to use instancing at all.
         */
        """
        pass

    def set_shader(self, ShaderAttrib_self, const_Shader_s, int_priority): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_shader(ShaderAttrib self, const Shader s, int priority)
        
        /**
         *
         */
        """
        pass

    def set_shader_auto(self, ShaderAttrib_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_shader_auto(ShaderAttrib self)
        set_shader_auto(ShaderAttrib self, BitMask shader_switch, int priority)
        set_shader_auto(ShaderAttrib self, int priority)
        
        /**
         *
         */
        
        /**
         * Set auto shader with bitmask to customize use, e.g., to keep normal, glow,
         * etc., on or off
         */
        """
        pass

    def set_shader_input(self, ShaderAttrib_self, const_ShaderInput_input): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_shader_input(ShaderAttrib self, const ShaderInput input)
        set_shader_input(ShaderAttrib self, const InternalName param0, object param1, int priority)
        
        // Shader Inputs
        
        /**
         *
         */
        
        /**
         *
         */
        
        /**
         *
         */
        
        /**
         *
         */
        
        /**
         *
         */
        
        /**
         *
         */
        
        /**
         *
         */
        
        /**
         *
         */
        
        /**
         *
         */
        
        /**
         *
         */
        
        /**
         *
         */
        
        /**
         *
         */
        
        /**
         *
         */
        
        /**
         *
         */
        
        /**
         *
         */
        
        /**
         *
         */
        
        /**
         *
         */
        """
        pass

    def set_shader_inputs(self, *args, **kwargs): # real signature unknown
        pass

    def set_shader_off(self, ShaderAttrib_self, int_priority): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_shader_off(ShaderAttrib self, int priority)
        
        /**
         *
         */
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    instance_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    shader = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    class_slot = 24
    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        'F_disable_alpha_write': 0,
        'F_hardware_skinning': 2,
        'F_shader_point_size': 3,
        'F_subsume_alpha_test': 1,
        '__doc__': '/**\n *\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.ShaderAttrib' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE29A1C0>'
        'autoGlossOn': None, # (!) real value is "<method 'autoGlossOn' of 'panda3d.core.ShaderAttrib' objects>"
        'autoGlowOn': None, # (!) real value is "<method 'autoGlowOn' of 'panda3d.core.ShaderAttrib' objects>"
        'autoNormalOn': None, # (!) real value is "<method 'autoNormalOn' of 'panda3d.core.ShaderAttrib' objects>"
        'autoRampOn': None, # (!) real value is "<method 'autoRampOn' of 'panda3d.core.ShaderAttrib' objects>"
        'autoShader': None, # (!) real value is "<method 'autoShader' of 'panda3d.core.ShaderAttrib' objects>"
        'autoShadowOn': None, # (!) real value is "<method 'autoShadowOn' of 'panda3d.core.ShaderAttrib' objects>"
        'auto_gloss_on': None, # (!) real value is "<method 'auto_gloss_on' of 'panda3d.core.ShaderAttrib' objects>"
        'auto_glow_on': None, # (!) real value is "<method 'auto_glow_on' of 'panda3d.core.ShaderAttrib' objects>"
        'auto_normal_on': None, # (!) real value is "<method 'auto_normal_on' of 'panda3d.core.ShaderAttrib' objects>"
        'auto_ramp_on': None, # (!) real value is "<method 'auto_ramp_on' of 'panda3d.core.ShaderAttrib' objects>"
        'auto_shader': None, # (!) real value is "<method 'auto_shader' of 'panda3d.core.ShaderAttrib' objects>"
        'auto_shadow_on': None, # (!) real value is "<method 'auto_shadow_on' of 'panda3d.core.ShaderAttrib' objects>"
        'class_slot': None, # (!) real value is "<attribute 'class_slot' of 'panda3d.core.ShaderAttrib'>"
        'clearAllShaderInputs': None, # (!) real value is "<method 'clearAllShaderInputs' of 'panda3d.core.ShaderAttrib' objects>"
        'clearFlag': None, # (!) real value is "<method 'clearFlag' of 'panda3d.core.ShaderAttrib' objects>"
        'clearShader': None, # (!) real value is "<method 'clearShader' of 'panda3d.core.ShaderAttrib' objects>"
        'clearShaderInput': None, # (!) real value is "<method 'clearShaderInput' of 'panda3d.core.ShaderAttrib' objects>"
        'clear_all_shader_inputs': None, # (!) real value is "<method 'clear_all_shader_inputs' of 'panda3d.core.ShaderAttrib' objects>"
        'clear_flag': None, # (!) real value is "<method 'clear_flag' of 'panda3d.core.ShaderAttrib' objects>"
        'clear_shader': None, # (!) real value is "<method 'clear_shader' of 'panda3d.core.ShaderAttrib' objects>"
        'clear_shader_input': None, # (!) real value is "<method 'clear_shader_input' of 'panda3d.core.ShaderAttrib' objects>"
        'getClassSlot': None, # (!) real value is '<staticmethod(<built-in method getClassSlot of type object at 0x00007FFCFE29A1C0>)>'
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE29A1C0>)>'
        'getFlag': None, # (!) real value is "<method 'getFlag' of 'panda3d.core.ShaderAttrib' objects>"
        'getInstanceCount': None, # (!) real value is "<method 'getInstanceCount' of 'panda3d.core.ShaderAttrib' objects>"
        'getShader': None, # (!) real value is "<method 'getShader' of 'panda3d.core.ShaderAttrib' objects>"
        'getShaderInput': None, # (!) real value is "<method 'getShaderInput' of 'panda3d.core.ShaderAttrib' objects>"
        'getShaderInputBuffer': None, # (!) real value is "<method 'getShaderInputBuffer' of 'panda3d.core.ShaderAttrib' objects>"
        'getShaderInputMatrix': None, # (!) real value is "<method 'getShaderInputMatrix' of 'panda3d.core.ShaderAttrib' objects>"
        'getShaderInputNodepath': None, # (!) real value is "<method 'getShaderInputNodepath' of 'panda3d.core.ShaderAttrib' objects>"
        'getShaderInputTexture': None, # (!) real value is "<method 'getShaderInputTexture' of 'panda3d.core.ShaderAttrib' objects>"
        'getShaderInputVector': None, # (!) real value is "<method 'getShaderInputVector' of 'panda3d.core.ShaderAttrib' objects>"
        'getShaderPriority': None, # (!) real value is "<method 'getShaderPriority' of 'panda3d.core.ShaderAttrib' objects>"
        'get_class_slot': None, # (!) real value is '<staticmethod(<built-in method get_class_slot of type object at 0x00007FFCFE29A1C0>)>'
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE29A1C0>)>'
        'get_flag': None, # (!) real value is "<method 'get_flag' of 'panda3d.core.ShaderAttrib' objects>"
        'get_instance_count': None, # (!) real value is "<method 'get_instance_count' of 'panda3d.core.ShaderAttrib' objects>"
        'get_shader': None, # (!) real value is "<method 'get_shader' of 'panda3d.core.ShaderAttrib' objects>"
        'get_shader_input': None, # (!) real value is "<method 'get_shader_input' of 'panda3d.core.ShaderAttrib' objects>"
        'get_shader_input_buffer': None, # (!) real value is "<method 'get_shader_input_buffer' of 'panda3d.core.ShaderAttrib' objects>"
        'get_shader_input_matrix': None, # (!) real value is "<method 'get_shader_input_matrix' of 'panda3d.core.ShaderAttrib' objects>"
        'get_shader_input_nodepath': None, # (!) real value is "<method 'get_shader_input_nodepath' of 'panda3d.core.ShaderAttrib' objects>"
        'get_shader_input_texture': None, # (!) real value is "<method 'get_shader_input_texture' of 'panda3d.core.ShaderAttrib' objects>"
        'get_shader_input_vector': None, # (!) real value is "<method 'get_shader_input_vector' of 'panda3d.core.ShaderAttrib' objects>"
        'get_shader_priority': None, # (!) real value is "<method 'get_shader_priority' of 'panda3d.core.ShaderAttrib' objects>"
        'hasShader': None, # (!) real value is "<method 'hasShader' of 'panda3d.core.ShaderAttrib' objects>"
        'hasShaderInput': None, # (!) real value is "<method 'hasShaderInput' of 'panda3d.core.ShaderAttrib' objects>"
        'has_shader': None, # (!) real value is "<method 'has_shader' of 'panda3d.core.ShaderAttrib' objects>"
        'has_shader_input': None, # (!) real value is "<method 'has_shader_input' of 'panda3d.core.ShaderAttrib' objects>"
        'instance_count': None, # (!) real value is "<attribute 'instance_count' of 'panda3d.core.ShaderAttrib' objects>"
        'make': None, # (!) real value is '<staticmethod(<built-in method make of type object at 0x00007FFCFE29A1C0>)>'
        'makeDefault': None, # (!) real value is '<staticmethod(<built-in method makeDefault of type object at 0x00007FFCFE29A1C0>)>'
        'makeOff': None, # (!) real value is '<staticmethod(<built-in method makeOff of type object at 0x00007FFCFE29A1C0>)>'
        'make_default': None, # (!) real value is '<staticmethod(<built-in method make_default of type object at 0x00007FFCFE29A1C0>)>'
        'make_off': None, # (!) real value is '<staticmethod(<built-in method make_off of type object at 0x00007FFCFE29A1C0>)>'
        'registerWithReadFactory': None, # (!) real value is '<staticmethod(<built-in method registerWithReadFactory of type object at 0x00007FFCFE29A1C0>)>'
        'register_with_read_factory': None, # (!) real value is '<staticmethod(<built-in method register_with_read_factory of type object at 0x00007FFCFE29A1C0>)>'
        'setFlag': None, # (!) real value is "<method 'setFlag' of 'panda3d.core.ShaderAttrib' objects>"
        'setInstanceCount': None, # (!) real value is "<method 'setInstanceCount' of 'panda3d.core.ShaderAttrib' objects>"
        'setShader': None, # (!) real value is "<method 'setShader' of 'panda3d.core.ShaderAttrib' objects>"
        'setShaderAuto': None, # (!) real value is "<method 'setShaderAuto' of 'panda3d.core.ShaderAttrib' objects>"
        'setShaderInput': None, # (!) real value is "<method 'setShaderInput' of 'panda3d.core.ShaderAttrib' objects>"
        'setShaderInputs': None, # (!) real value is "<method 'setShaderInputs' of 'panda3d.core.ShaderAttrib' objects>"
        'setShaderOff': None, # (!) real value is "<method 'setShaderOff' of 'panda3d.core.ShaderAttrib' objects>"
        'set_flag': None, # (!) real value is "<method 'set_flag' of 'panda3d.core.ShaderAttrib' objects>"
        'set_instance_count': None, # (!) real value is "<method 'set_instance_count' of 'panda3d.core.ShaderAttrib' objects>"
        'set_shader': None, # (!) real value is "<method 'set_shader' of 'panda3d.core.ShaderAttrib' objects>"
        'set_shader_auto': None, # (!) real value is "<method 'set_shader_auto' of 'panda3d.core.ShaderAttrib' objects>"
        'set_shader_input': None, # (!) real value is "<method 'set_shader_input' of 'panda3d.core.ShaderAttrib' objects>"
        'set_shader_inputs': None, # (!) real value is "<method 'set_shader_inputs' of 'panda3d.core.ShaderAttrib' objects>"
        'set_shader_off': None, # (!) real value is "<method 'set_shader_off' of 'panda3d.core.ShaderAttrib' objects>"
        'shader': None, # (!) real value is "<attribute 'shader' of 'panda3d.core.ShaderAttrib' objects>"
    }
    F_disable_alpha_write = 0
    F_hardware_skinning = 2
    F_shader_point_size = 3
    F_subsume_alpha_test = 1


