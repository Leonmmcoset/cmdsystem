# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .RenderAttrib import RenderAttrib

class TextureAttrib(RenderAttrib):
    """
    /**
     * Indicates the set of TextureStages and their associated Textures that
     * should be applied to (or removed from) a node.
     */
    """
    def addOffStage(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_off_stage(TextureAttrib self, TextureStage stage, int override)
        
        /**
         * Returns a new TextureAttrib, just like this one, but with the indicated
         * stage added to the list of stages turned off by this attrib.
         */
        """
        pass

    def addOnStage(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_on_stage(TextureAttrib self, TextureStage stage, Texture tex)
        add_on_stage(TextureAttrib self, TextureStage stage, Texture tex, const SamplerState sampler, int override)
        add_on_stage(TextureAttrib self, TextureStage stage, Texture tex, int override)
        
        /**
         * Returns a new TextureAttrib, just like this one, but with the indicated
         * stage added to the list of stages turned on by this attrib.
         */
        
        /**
         * Returns a new TextureAttrib, just like this one, but with the indicated
         * stage added to the list of stages turned on by this attrib.
         */
        """
        pass

    def add_off_stage(self, TextureAttrib_self, TextureStage_stage, int_override): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_off_stage(TextureAttrib self, TextureStage stage, int override)
        
        /**
         * Returns a new TextureAttrib, just like this one, but with the indicated
         * stage added to the list of stages turned off by this attrib.
         */
        """
        pass

    def add_on_stage(self, TextureAttrib_self, TextureStage_stage, Texture_tex): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_on_stage(TextureAttrib self, TextureStage stage, Texture tex)
        add_on_stage(TextureAttrib self, TextureStage stage, Texture tex, const SamplerState sampler, int override)
        add_on_stage(TextureAttrib self, TextureStage stage, Texture tex, int override)
        
        /**
         * Returns a new TextureAttrib, just like this one, but with the indicated
         * stage added to the list of stages turned on by this attrib.
         */
        
        /**
         * Returns a new TextureAttrib, just like this one, but with the indicated
         * stage added to the list of stages turned on by this attrib.
         */
        """
        pass

    def findOnStage(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        find_on_stage(TextureAttrib self, const TextureStage stage)
        
        /**
         * Returns the index number of the indicated TextureStage within the list of
         * on_stages, or -1 if the indicated stage is not listed.
         */
        """
        pass

    def find_on_stage(self, TextureAttrib_self, const_TextureStage_stage): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        find_on_stage(TextureAttrib self, const TextureStage stage)
        
        /**
         * Returns the index number of the indicated TextureStage within the list of
         * on_stages, or -1 if the indicated stage is not listed.
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

    def getFfTcIndex(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_ff_tc_index(TextureAttrib self, int n)
        
        /**
         * For each TextureStage listed in get_on_ff_stage(), this returns a unique
         * index number for the texture coordinate name used by that TextureStage.  It
         * is guaranteed to remain the same index number for each texcoord name (for a
         * given set of TextureStages), even if the texture render order changes.
         */
        """
        pass

    def getNumOffStages(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_off_stages(TextureAttrib self)
        
        /**
         * Returns the number of stages that are turned off by the attribute.
         */
        """
        pass

    def getNumOnFfStages(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_on_ff_stages(TextureAttrib self)
        
        /**
         * Returns the number of on-stages that are relevant to the classic fixed
         * function pipeline.  This excludes texture stages such as normal maps.
         */
        """
        pass

    def getNumOnStages(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_on_stages(TextureAttrib self)
        
        /**
         * Returns the number of stages that are turned on by the attribute.
         */
        """
        pass

    def getOffStage(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_off_stage(TextureAttrib self, int n)
        
        /**
         * Returns the nth stage turned off by the attribute, sorted in arbitrary
         * (pointer) order.
         */
        """
        pass

    def getOffStages(self, *args, **kwargs): # real signature unknown
        pass

    def getOnFfStage(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_on_ff_stage(TextureAttrib self, int n)
        
        /**
         * Returns the nth stage turned on by the attribute, sorted in render order,
         * including only those relevant to the classic fixed function pipeline.  This
         * excludes texture stages such as normal maps.
         */
        """
        pass

    def getOnFfStages(self, *args, **kwargs): # real signature unknown
        pass

    def getOnSampler(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_on_sampler(TextureAttrib self, TextureStage stage)
        
        /**
         * Returns the sampler associated with the indicated stage, or the one
         * associated with its texture if no custom stage has been specified.  It is
         * an error to call this if the stage does not exist.
         */
        """
        pass

    def getOnStage(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_on_stage(TextureAttrib self, int n)
        
        /**
         * Returns the nth stage turned on by the attribute, sorted in render order.
         */
        """
        pass

    def getOnStageOverride(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_on_stage_override(TextureAttrib self, TextureStage stage)
        
        /**
         * Returns the override value associated with the indicated stage.
         */
        """
        pass

    def getOnStages(self, *args, **kwargs): # real signature unknown
        pass

    def getOnTexture(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_on_texture(TextureAttrib self, TextureStage stage)
        
        /**
         * Returns the texture associated with the indicated stage, or NULL if no
         * texture is associated.
         */
        """
        pass

    def getTexture(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_texture(TextureAttrib self)
        
        /**
         * If the TextureAttrib is not an 'off' TextureAttrib, returns the base-level
         * texture that is associated.  Otherwise, return NULL.
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

    def get_ff_tc_index(self, TextureAttrib_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_ff_tc_index(TextureAttrib self, int n)
        
        /**
         * For each TextureStage listed in get_on_ff_stage(), this returns a unique
         * index number for the texture coordinate name used by that TextureStage.  It
         * is guaranteed to remain the same index number for each texcoord name (for a
         * given set of TextureStages), even if the texture render order changes.
         */
        """
        pass

    def get_num_off_stages(self, TextureAttrib_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_off_stages(TextureAttrib self)
        
        /**
         * Returns the number of stages that are turned off by the attribute.
         */
        """
        pass

    def get_num_on_ff_stages(self, TextureAttrib_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_on_ff_stages(TextureAttrib self)
        
        /**
         * Returns the number of on-stages that are relevant to the classic fixed
         * function pipeline.  This excludes texture stages such as normal maps.
         */
        """
        pass

    def get_num_on_stages(self, TextureAttrib_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_on_stages(TextureAttrib self)
        
        /**
         * Returns the number of stages that are turned on by the attribute.
         */
        """
        pass

    def get_off_stage(self, TextureAttrib_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_off_stage(TextureAttrib self, int n)
        
        /**
         * Returns the nth stage turned off by the attribute, sorted in arbitrary
         * (pointer) order.
         */
        """
        pass

    def get_off_stages(self, *args, **kwargs): # real signature unknown
        pass

    def get_on_ff_stage(self, TextureAttrib_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_on_ff_stage(TextureAttrib self, int n)
        
        /**
         * Returns the nth stage turned on by the attribute, sorted in render order,
         * including only those relevant to the classic fixed function pipeline.  This
         * excludes texture stages such as normal maps.
         */
        """
        pass

    def get_on_ff_stages(self, *args, **kwargs): # real signature unknown
        pass

    def get_on_sampler(self, TextureAttrib_self, TextureStage_stage): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_on_sampler(TextureAttrib self, TextureStage stage)
        
        /**
         * Returns the sampler associated with the indicated stage, or the one
         * associated with its texture if no custom stage has been specified.  It is
         * an error to call this if the stage does not exist.
         */
        """
        pass

    def get_on_stage(self, TextureAttrib_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_on_stage(TextureAttrib self, int n)
        
        /**
         * Returns the nth stage turned on by the attribute, sorted in render order.
         */
        """
        pass

    def get_on_stages(self, *args, **kwargs): # real signature unknown
        pass

    def get_on_stage_override(self, TextureAttrib_self, TextureStage_stage): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_on_stage_override(TextureAttrib self, TextureStage stage)
        
        /**
         * Returns the override value associated with the indicated stage.
         */
        """
        pass

    def get_on_texture(self, TextureAttrib_self, TextureStage_stage): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_on_texture(TextureAttrib self, TextureStage stage)
        
        /**
         * Returns the texture associated with the indicated stage, or NULL if no
         * texture is associated.
         */
        """
        pass

    def get_texture(self, TextureAttrib_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_texture(TextureAttrib self)
        
        /**
         * If the TextureAttrib is not an 'off' TextureAttrib, returns the base-level
         * texture that is associated.  Otherwise, return NULL.
         */
        """
        pass

    def hasAllOff(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_all_off(TextureAttrib self)
        
        /**
         * Returns true if this attrib turns off all stages (although it may also turn
         * some on).
         */
        """
        pass

    def hasOffStage(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_off_stage(TextureAttrib self, TextureStage stage)
        
        /**
         * Returns true if the indicated stage is turned off by the attrib, false
         * otherwise.
         */
        """
        pass

    def hasOnStage(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_on_stage(TextureAttrib self, TextureStage stage)
        
        /**
         * Returns true if the indicated stage is turned on by the attrib, false
         * otherwise.
         */
        """
        pass

    def has_all_off(self, TextureAttrib_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_all_off(TextureAttrib self)
        
        /**
         * Returns true if this attrib turns off all stages (although it may also turn
         * some on).
         */
        """
        pass

    def has_off_stage(self, TextureAttrib_self, TextureStage_stage): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_off_stage(TextureAttrib self, TextureStage stage)
        
        /**
         * Returns true if the indicated stage is turned off by the attrib, false
         * otherwise.
         */
        """
        pass

    def has_on_stage(self, TextureAttrib_self, TextureStage_stage): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_on_stage(TextureAttrib self, TextureStage stage)
        
        /**
         * Returns true if the indicated stage is turned on by the attrib, false
         * otherwise.
         */
        """
        pass

    def isIdentity(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_identity(TextureAttrib self)
        
        /**
         * Returns true if this is an identity attrib: it does not change the set of
         * stages in use.
         */
        """
        pass

    def isOff(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_off(TextureAttrib self)
        
        /**
         * Returns true if the TextureAttrib is an 'off' TextureAttrib, indicating
         * that it should disable texturing.
         *
         * If multitexture is in effect, a TextureAttrib may not be strictly "on" or
         * "off"; therefore, to get a more precise answer to this question, you should
         * consider using has_all_off() or get_num_off_stages() or has_off_stage()
         * instead.
         */
        """
        pass

    def is_identity(self, TextureAttrib_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_identity(TextureAttrib self)
        
        /**
         * Returns true if this is an identity attrib: it does not change the set of
         * stages in use.
         */
        """
        pass

    def is_off(self, TextureAttrib_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_off(TextureAttrib self)
        
        /**
         * Returns true if the TextureAttrib is an 'off' TextureAttrib, indicating
         * that it should disable texturing.
         *
         * If multitexture is in effect, a TextureAttrib may not be strictly "on" or
         * "off"; therefore, to get a more precise answer to this question, you should
         * consider using has_all_off() or get_num_off_stages() or has_off_stage()
         * instead.
         */
        """
        pass

    def make(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        make()
        make(Texture tex)
        
        // These methods are used to create a simple, single-textured layer.  For
        // multitexture, use the multitexture interfaces, further below.
        
        // The following methods define the new multitexture mode for TextureAttrib.
        // Each TextureAttrib can add or remove individual texture stages from the
        // complete set of textures that are to be applied; this is similar to the
        // mechanism of LightAttrib.
        
        /**
         * Constructs a new TextureAttrib object suitable for rendering the indicated
         * texture onto geometry, using the default TextureStage.
         */
        
        /**
         * Constructs a new TextureAttrib object that does nothing.
         */
        """
        pass

    def makeAllOff(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        make_all_off()
        
        /**
         * Constructs a new TextureAttrib object that turns off all stages (and hence
         * disables texturing).
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
         * Constructs a new TextureAttrib object suitable for rendering untextured
         * geometry.
         */
        """
        pass

    def make_all_off(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        make_all_off()
        
        /**
         * Constructs a new TextureAttrib object that turns off all stages (and hence
         * disables texturing).
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
         * Constructs a new TextureAttrib object suitable for rendering untextured
         * geometry.
         */
        """
        pass

    def removeOffStage(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        remove_off_stage(TextureAttrib self, TextureStage stage)
        
        /**
         * Returns a new TextureAttrib, just like this one, but with the indicated
         * stage removed from the list of stages turned off by this attrib.
         */
        """
        pass

    def removeOnStage(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        remove_on_stage(TextureAttrib self, TextureStage stage)
        
        /**
         * Returns a new TextureAttrib, just like this one, but with the indicated
         * stage removed from the list of stages turned on by this attrib.
         */
        """
        pass

    def remove_off_stage(self, TextureAttrib_self, TextureStage_stage): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        remove_off_stage(TextureAttrib self, TextureStage stage)
        
        /**
         * Returns a new TextureAttrib, just like this one, but with the indicated
         * stage removed from the list of stages turned off by this attrib.
         */
        """
        pass

    def remove_on_stage(self, TextureAttrib_self, TextureStage_stage): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        remove_on_stage(TextureAttrib self, TextureStage stage)
        
        /**
         * Returns a new TextureAttrib, just like this one, but with the indicated
         * stage removed from the list of stages turned on by this attrib.
         */
        """
        pass

    def replaceTexture(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        replace_texture(TextureAttrib self, Texture tex, Texture new_tex)
        replace_texture(TextureAttrib self, Texture tex, NoneType new_tex)
        
        // Let interrogate know this also accepts None
        
        /**
         * Returns a new TextureAttrib, just like this one, but with all references to
         * the given texture replaced with the new texture.
         *
         * As of Panda3D 1.10.13, new_tex may be null to remove the texture.
         *
         * @since 1.10.4
         */
        """
        pass

    def replace_texture(self, TextureAttrib_self, Texture_tex, Texture_new_tex): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        replace_texture(TextureAttrib self, Texture tex, Texture new_tex)
        replace_texture(TextureAttrib self, Texture tex, NoneType new_tex)
        
        // Let interrogate know this also accepts None
        
        /**
         * Returns a new TextureAttrib, just like this one, but with all references to
         * the given texture replaced with the new texture.
         *
         * As of Panda3D 1.10.13, new_tex may be null to remove the texture.
         *
         * @since 1.10.4
         */
        """
        pass

    def unifyTextureStages(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        unify_texture_stages(TextureAttrib self, TextureStage stage)
        
        /**
         * Returns a new TextureAttrib, just like this one, but with any included
         * TextureAttribs that happen to have the same name as the given object
         * replaced with the object.
         */
        """
        pass

    def unify_texture_stages(self, TextureAttrib_self, TextureStage_stage): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        unify_texture_stages(TextureAttrib self, TextureStage stage)
        
        /**
         * Returns a new TextureAttrib, just like this one, but with any included
         * TextureAttribs that happen to have the same name as the given object
         * replaced with the object.
         */
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    off_stages = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    on_stages = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    samplers = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    textures = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    class_slot = 27
    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__doc__': '/**\n * Indicates the set of TextureStages and their associated Textures that\n * should be applied to (or removed from) a node.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.TextureAttrib' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE2996E0>'
        'addOffStage': None, # (!) real value is "<method 'addOffStage' of 'panda3d.core.TextureAttrib' objects>"
        'addOnStage': None, # (!) real value is "<method 'addOnStage' of 'panda3d.core.TextureAttrib' objects>"
        'add_off_stage': None, # (!) real value is "<method 'add_off_stage' of 'panda3d.core.TextureAttrib' objects>"
        'add_on_stage': None, # (!) real value is "<method 'add_on_stage' of 'panda3d.core.TextureAttrib' objects>"
        'class_slot': None, # (!) real value is "<attribute 'class_slot' of 'panda3d.core.TextureAttrib'>"
        'findOnStage': None, # (!) real value is "<method 'findOnStage' of 'panda3d.core.TextureAttrib' objects>"
        'find_on_stage': None, # (!) real value is "<method 'find_on_stage' of 'panda3d.core.TextureAttrib' objects>"
        'getClassSlot': None, # (!) real value is '<staticmethod(<built-in method getClassSlot of type object at 0x00007FFCFE2996E0>)>'
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE2996E0>)>'
        'getFfTcIndex': None, # (!) real value is "<method 'getFfTcIndex' of 'panda3d.core.TextureAttrib' objects>"
        'getNumOffStages': None, # (!) real value is "<method 'getNumOffStages' of 'panda3d.core.TextureAttrib' objects>"
        'getNumOnFfStages': None, # (!) real value is "<method 'getNumOnFfStages' of 'panda3d.core.TextureAttrib' objects>"
        'getNumOnStages': None, # (!) real value is "<method 'getNumOnStages' of 'panda3d.core.TextureAttrib' objects>"
        'getOffStage': None, # (!) real value is "<method 'getOffStage' of 'panda3d.core.TextureAttrib' objects>"
        'getOffStages': None, # (!) real value is "<method 'getOffStages' of 'panda3d.core.TextureAttrib' objects>"
        'getOnFfStage': None, # (!) real value is "<method 'getOnFfStage' of 'panda3d.core.TextureAttrib' objects>"
        'getOnFfStages': None, # (!) real value is "<method 'getOnFfStages' of 'panda3d.core.TextureAttrib' objects>"
        'getOnSampler': None, # (!) real value is "<method 'getOnSampler' of 'panda3d.core.TextureAttrib' objects>"
        'getOnStage': None, # (!) real value is "<method 'getOnStage' of 'panda3d.core.TextureAttrib' objects>"
        'getOnStageOverride': None, # (!) real value is "<method 'getOnStageOverride' of 'panda3d.core.TextureAttrib' objects>"
        'getOnStages': None, # (!) real value is "<method 'getOnStages' of 'panda3d.core.TextureAttrib' objects>"
        'getOnTexture': None, # (!) real value is "<method 'getOnTexture' of 'panda3d.core.TextureAttrib' objects>"
        'getTexture': None, # (!) real value is "<method 'getTexture' of 'panda3d.core.TextureAttrib' objects>"
        'get_class_slot': None, # (!) real value is '<staticmethod(<built-in method get_class_slot of type object at 0x00007FFCFE2996E0>)>'
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE2996E0>)>'
        'get_ff_tc_index': None, # (!) real value is "<method 'get_ff_tc_index' of 'panda3d.core.TextureAttrib' objects>"
        'get_num_off_stages': None, # (!) real value is "<method 'get_num_off_stages' of 'panda3d.core.TextureAttrib' objects>"
        'get_num_on_ff_stages': None, # (!) real value is "<method 'get_num_on_ff_stages' of 'panda3d.core.TextureAttrib' objects>"
        'get_num_on_stages': None, # (!) real value is "<method 'get_num_on_stages' of 'panda3d.core.TextureAttrib' objects>"
        'get_off_stage': None, # (!) real value is "<method 'get_off_stage' of 'panda3d.core.TextureAttrib' objects>"
        'get_off_stages': None, # (!) real value is "<method 'get_off_stages' of 'panda3d.core.TextureAttrib' objects>"
        'get_on_ff_stage': None, # (!) real value is "<method 'get_on_ff_stage' of 'panda3d.core.TextureAttrib' objects>"
        'get_on_ff_stages': None, # (!) real value is "<method 'get_on_ff_stages' of 'panda3d.core.TextureAttrib' objects>"
        'get_on_sampler': None, # (!) real value is "<method 'get_on_sampler' of 'panda3d.core.TextureAttrib' objects>"
        'get_on_stage': None, # (!) real value is "<method 'get_on_stage' of 'panda3d.core.TextureAttrib' objects>"
        'get_on_stage_override': None, # (!) real value is "<method 'get_on_stage_override' of 'panda3d.core.TextureAttrib' objects>"
        'get_on_stages': None, # (!) real value is "<method 'get_on_stages' of 'panda3d.core.TextureAttrib' objects>"
        'get_on_texture': None, # (!) real value is "<method 'get_on_texture' of 'panda3d.core.TextureAttrib' objects>"
        'get_texture': None, # (!) real value is "<method 'get_texture' of 'panda3d.core.TextureAttrib' objects>"
        'hasAllOff': None, # (!) real value is "<method 'hasAllOff' of 'panda3d.core.TextureAttrib' objects>"
        'hasOffStage': None, # (!) real value is "<method 'hasOffStage' of 'panda3d.core.TextureAttrib' objects>"
        'hasOnStage': None, # (!) real value is "<method 'hasOnStage' of 'panda3d.core.TextureAttrib' objects>"
        'has_all_off': None, # (!) real value is "<method 'has_all_off' of 'panda3d.core.TextureAttrib' objects>"
        'has_off_stage': None, # (!) real value is "<method 'has_off_stage' of 'panda3d.core.TextureAttrib' objects>"
        'has_on_stage': None, # (!) real value is "<method 'has_on_stage' of 'panda3d.core.TextureAttrib' objects>"
        'isIdentity': None, # (!) real value is "<method 'isIdentity' of 'panda3d.core.TextureAttrib' objects>"
        'isOff': None, # (!) real value is "<method 'isOff' of 'panda3d.core.TextureAttrib' objects>"
        'is_identity': None, # (!) real value is "<method 'is_identity' of 'panda3d.core.TextureAttrib' objects>"
        'is_off': None, # (!) real value is "<method 'is_off' of 'panda3d.core.TextureAttrib' objects>"
        'make': None, # (!) real value is '<staticmethod(<built-in method make of type object at 0x00007FFCFE2996E0>)>'
        'makeAllOff': None, # (!) real value is '<staticmethod(<built-in method makeAllOff of type object at 0x00007FFCFE2996E0>)>'
        'makeDefault': None, # (!) real value is '<staticmethod(<built-in method makeDefault of type object at 0x00007FFCFE2996E0>)>'
        'makeOff': None, # (!) real value is '<staticmethod(<built-in method makeOff of type object at 0x00007FFCFE2996E0>)>'
        'make_all_off': None, # (!) real value is '<staticmethod(<built-in method make_all_off of type object at 0x00007FFCFE2996E0>)>'
        'make_default': None, # (!) real value is '<staticmethod(<built-in method make_default of type object at 0x00007FFCFE2996E0>)>'
        'make_off': None, # (!) real value is '<staticmethod(<built-in method make_off of type object at 0x00007FFCFE2996E0>)>'
        'off_stages': None, # (!) real value is "<attribute 'off_stages' of 'panda3d.core.TextureAttrib' objects>"
        'on_stages': None, # (!) real value is "<attribute 'on_stages' of 'panda3d.core.TextureAttrib' objects>"
        'removeOffStage': None, # (!) real value is "<method 'removeOffStage' of 'panda3d.core.TextureAttrib' objects>"
        'removeOnStage': None, # (!) real value is "<method 'removeOnStage' of 'panda3d.core.TextureAttrib' objects>"
        'remove_off_stage': None, # (!) real value is "<method 'remove_off_stage' of 'panda3d.core.TextureAttrib' objects>"
        'remove_on_stage': None, # (!) real value is "<method 'remove_on_stage' of 'panda3d.core.TextureAttrib' objects>"
        'replaceTexture': None, # (!) real value is "<method 'replaceTexture' of 'panda3d.core.TextureAttrib' objects>"
        'replace_texture': None, # (!) real value is "<method 'replace_texture' of 'panda3d.core.TextureAttrib' objects>"
        'samplers': None, # (!) real value is "<attribute 'samplers' of 'panda3d.core.TextureAttrib' objects>"
        'textures': None, # (!) real value is "<attribute 'textures' of 'panda3d.core.TextureAttrib' objects>"
        'unifyTextureStages': None, # (!) real value is "<method 'unifyTextureStages' of 'panda3d.core.TextureAttrib' objects>"
        'unify_texture_stages': None, # (!) real value is "<method 'unify_texture_stages' of 'panda3d.core.TextureAttrib' objects>"
    }


