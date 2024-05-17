# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .RenderAttrib import RenderAttrib

class TexGenAttrib(RenderAttrib):
    """
    /**
     * Computes texture coordinates for geometry automatically based on vertex
     * position and/or normal.  This can be used to implement reflection and/or
     * refraction maps, for instance to make shiny surfaces, as well as other
     * special effects such as projective texturing.
     */
    """
    def addStage(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_stage(TexGenAttrib self, TextureStage stage, int mode)
        add_stage(TexGenAttrib self, TextureStage stage, int mode, const LPoint3f constant_value)
        
        /**
         * Returns a new TexGenAttrib just like this one, with the indicated
         * generation mode for the given stage.  If this stage already exists, its
         * mode is replaced.
         */
        
        /**
         * Returns a new TexGenAttrib just like this one, with the indicated
         * generation mode for the given stage.  If this stage already exists, its
         * mode is replaced.
         *
         * This variant also accepts constant_value, which is only meaningful if mode
         * is M_constant.
         */
        """
        pass

    def add_stage(self, TexGenAttrib_self, TextureStage_stage, int_mode): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_stage(TexGenAttrib self, TextureStage stage, int mode)
        add_stage(TexGenAttrib self, TextureStage stage, int mode, const LPoint3f constant_value)
        
        /**
         * Returns a new TexGenAttrib just like this one, with the indicated
         * generation mode for the given stage.  If this stage already exists, its
         * mode is replaced.
         */
        
        /**
         * Returns a new TexGenAttrib just like this one, with the indicated
         * generation mode for the given stage.  If this stage already exists, its
         * mode is replaced.
         *
         * This variant also accepts constant_value, which is only meaningful if mode
         * is M_constant.
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

    def getConstantValue(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_constant_value(TexGenAttrib self, TextureStage stage)
        
        /**
         * Returns the constant value associated with the named texture stage.  This
         * is only meaningful if the mode is M_constant.
         */
        """
        pass

    def getGeomRendering(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_geom_rendering(TexGenAttrib self, int geom_rendering)
        
        /**
         * Returns the union of the Geom::GeomRendering bits that will be required
         * once this TexGenAttrib is applied to a geom which includes the indicated
         * geom_rendering bits.
         */
        """
        pass

    def getMode(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_mode(TexGenAttrib self, TextureStage stage)
        
        /**
         * Returns the generation mode associated with the named texture stage, or
         * M_off if nothing is associated with the indicated stage.
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

    def get_constant_value(self, TexGenAttrib_self, TextureStage_stage): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_constant_value(TexGenAttrib self, TextureStage stage)
        
        /**
         * Returns the constant value associated with the named texture stage.  This
         * is only meaningful if the mode is M_constant.
         */
        """
        pass

    def get_geom_rendering(self, TexGenAttrib_self, int_geom_rendering): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_geom_rendering(TexGenAttrib self, int geom_rendering)
        
        /**
         * Returns the union of the Geom::GeomRendering bits that will be required
         * once this TexGenAttrib is applied to a geom which includes the indicated
         * geom_rendering bits.
         */
        """
        pass

    def get_mode(self, TexGenAttrib_self, TextureStage_stage): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_mode(TexGenAttrib self, TextureStage stage)
        
        /**
         * Returns the generation mode associated with the named texture stage, or
         * M_off if nothing is associated with the indicated stage.
         */
        """
        pass

    def hasGenTexcoordStage(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_gen_texcoord_stage(TexGenAttrib self, TextureStage stage)
        
        /**
         * Returns true if the indicated TextureStage will have texture coordinates
         * generated for it automatically (and thus there is no need to upload the
         * texture coordinates encoded in the vertices).
         */
        """
        pass

    def hasStage(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_stage(TexGenAttrib self, TextureStage stage)
        
        /**
         * Returns true if there is a mode associated with the indicated stage, or
         * false otherwise (in which case get_transform(stage) will return M_off).
         */
        """
        pass

    def has_gen_texcoord_stage(self, TexGenAttrib_self, TextureStage_stage): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_gen_texcoord_stage(TexGenAttrib self, TextureStage stage)
        
        /**
         * Returns true if the indicated TextureStage will have texture coordinates
         * generated for it automatically (and thus there is no need to upload the
         * texture coordinates encoded in the vertices).
         */
        """
        pass

    def has_stage(self, TexGenAttrib_self, TextureStage_stage): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_stage(TexGenAttrib self, TextureStage stage)
        
        /**
         * Returns true if there is a mode associated with the indicated stage, or
         * false otherwise (in which case get_transform(stage) will return M_off).
         */
        """
        pass

    def isEmpty(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_empty(TexGenAttrib self)
        
        /**
         * Returns true if no stages are defined in the TexGenAttrib, false if at
         * least one is.
         */
        """
        pass

    def is_empty(self, TexGenAttrib_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_empty(TexGenAttrib self)
        
        /**
         * Returns true if no stages are defined in the TexGenAttrib, false if at
         * least one is.
         */
        """
        pass

    def make(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        make()
        make(TextureStage stage, int mode)
        
        /**
         * Constructs a TexGenAttrib that generates no stages at all.
         */
        
        /**
         * Constructs a TexGenAttrib that generates just the indicated stage.
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

    def removeStage(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        remove_stage(TexGenAttrib self, TextureStage stage)
        
        /**
         * Returns a new TexGenAttrib just like this one, with the indicated stage
         * removed.
         */
        """
        pass

    def remove_stage(self, TexGenAttrib_self, TextureStage_stage): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        remove_stage(TexGenAttrib self, TextureStage stage)
        
        /**
         * Returns a new TexGenAttrib just like this one, with the indicated stage
         * removed.
         */
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    class_slot = 28
    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__doc__': '/**\n * Computes texture coordinates for geometry automatically based on vertex\n * position and/or normal.  This can be used to implement reflection and/or\n * refraction maps, for instance to make shiny surfaces, as well as other\n * special effects such as projective texturing.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.TexGenAttrib' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE2998B0>'
        'addStage': None, # (!) real value is "<method 'addStage' of 'panda3d.core.TexGenAttrib' objects>"
        'add_stage': None, # (!) real value is "<method 'add_stage' of 'panda3d.core.TexGenAttrib' objects>"
        'class_slot': None, # (!) real value is "<attribute 'class_slot' of 'panda3d.core.TexGenAttrib'>"
        'getClassSlot': None, # (!) real value is '<staticmethod(<built-in method getClassSlot of type object at 0x00007FFCFE2998B0>)>'
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE2998B0>)>'
        'getConstantValue': None, # (!) real value is "<method 'getConstantValue' of 'panda3d.core.TexGenAttrib' objects>"
        'getGeomRendering': None, # (!) real value is "<method 'getGeomRendering' of 'panda3d.core.TexGenAttrib' objects>"
        'getMode': None, # (!) real value is "<method 'getMode' of 'panda3d.core.TexGenAttrib' objects>"
        'get_class_slot': None, # (!) real value is '<staticmethod(<built-in method get_class_slot of type object at 0x00007FFCFE2998B0>)>'
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE2998B0>)>'
        'get_constant_value': None, # (!) real value is "<method 'get_constant_value' of 'panda3d.core.TexGenAttrib' objects>"
        'get_geom_rendering': None, # (!) real value is "<method 'get_geom_rendering' of 'panda3d.core.TexGenAttrib' objects>"
        'get_mode': None, # (!) real value is "<method 'get_mode' of 'panda3d.core.TexGenAttrib' objects>"
        'hasGenTexcoordStage': None, # (!) real value is "<method 'hasGenTexcoordStage' of 'panda3d.core.TexGenAttrib' objects>"
        'hasStage': None, # (!) real value is "<method 'hasStage' of 'panda3d.core.TexGenAttrib' objects>"
        'has_gen_texcoord_stage': None, # (!) real value is "<method 'has_gen_texcoord_stage' of 'panda3d.core.TexGenAttrib' objects>"
        'has_stage': None, # (!) real value is "<method 'has_stage' of 'panda3d.core.TexGenAttrib' objects>"
        'isEmpty': None, # (!) real value is "<method 'isEmpty' of 'panda3d.core.TexGenAttrib' objects>"
        'is_empty': None, # (!) real value is "<method 'is_empty' of 'panda3d.core.TexGenAttrib' objects>"
        'make': None, # (!) real value is '<staticmethod(<built-in method make of type object at 0x00007FFCFE2998B0>)>'
        'makeDefault': None, # (!) real value is '<staticmethod(<built-in method makeDefault of type object at 0x00007FFCFE2998B0>)>'
        'make_default': None, # (!) real value is '<staticmethod(<built-in method make_default of type object at 0x00007FFCFE2998B0>)>'
        'removeStage': None, # (!) real value is "<method 'removeStage' of 'panda3d.core.TexGenAttrib' objects>"
        'remove_stage': None, # (!) real value is "<method 'remove_stage' of 'panda3d.core.TexGenAttrib' objects>"
    }


