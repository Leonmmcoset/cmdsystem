# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .TypedWritableReferenceCount import TypedWritableReferenceCount

class GraphicsStateGuardianBase(TypedWritableReferenceCount):
    """
    /**
     * This is a base class for the GraphicsStateGuardian class, which is itself a
     * base class for the various GSG's for different platforms.  This class
     * contains all the function prototypes to support the double-dispatch of GSG
     * to geoms, transitions, etc.  It lives in a separate class in its own
     * package so we can avoid circular build dependency problems.
     *
     * GraphicsStateGuardians are not actually writable to bam files, of course,
     * but they may be passed as event parameters, so they inherit from
     * TypedWritableReferenceCount instead of TypedReferenceCount for that
     * convenience.
     */
    """
    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getDefaultGsg(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_default_gsg()
        
        /**
         * Returns a pointer to the "default" GSG.  This is typically the first GSG
         * created in an application; in a single-window application, it will be the
         * only GSG. This GSG is used to determine default optimization choices for
         * loaded geometry.
         *
         * The return value may be NULL if a GSG has not been created.
         */
        """
        pass

    def getEffectiveIncompleteRender(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_effective_incomplete_render(GraphicsStateGuardianBase self)
        """
        pass

    def getGsg(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_gsg(int n)
        
        /**
         * Returns the nth GSG in the universe.  GSG's automatically add themselves
         * and remove themselves from this list as they are created and destroyed.
         */
        """
        pass

    def getGsgs(self, *args, **kwargs): # real signature unknown
        pass

    def getIncompleteRender(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_incomplete_render(GraphicsStateGuardianBase self)
        """
        pass

    def getMaxTextureDimension(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_max_texture_dimension(GraphicsStateGuardianBase self)
        """
        pass

    def getMaxVerticesPerArray(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_max_vertices_per_array(GraphicsStateGuardianBase self)
        """
        pass

    def getMaxVerticesPerPrimitive(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_max_vertices_per_primitive(GraphicsStateGuardianBase self)
        """
        pass

    def getNumGsgs(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_gsgs()
        
        /**
         * Returns the total number of GSG's in the universe.
         */
        """
        pass

    def getSupportedGeomRendering(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_supported_geom_rendering(GraphicsStateGuardianBase self)
        """
        pass

    def getSupportsCompressedTextureFormat(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_supports_compressed_texture_format(GraphicsStateGuardianBase self, int compression_mode)
        """
        pass

    def getSupportsHlsl(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_supports_hlsl(GraphicsStateGuardianBase self)
        """
        pass

    def getSupportsMultisample(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_supports_multisample(GraphicsStateGuardianBase self)
        """
        pass

    def getSupportsShadowFilter(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_supports_shadow_filter(GraphicsStateGuardianBase self)
        """
        pass

    def getSupportsTextureSrgb(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_supports_texture_srgb(GraphicsStateGuardianBase self)
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_default_gsg(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_default_gsg()
        
        /**
         * Returns a pointer to the "default" GSG.  This is typically the first GSG
         * created in an application; in a single-window application, it will be the
         * only GSG. This GSG is used to determine default optimization choices for
         * loaded geometry.
         *
         * The return value may be NULL if a GSG has not been created.
         */
        """
        pass

    def get_effective_incomplete_render(self, GraphicsStateGuardianBase_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_effective_incomplete_render(GraphicsStateGuardianBase self)
        """
        pass

    def get_gsg(self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_gsg(int n)
        
        /**
         * Returns the nth GSG in the universe.  GSG's automatically add themselves
         * and remove themselves from this list as they are created and destroyed.
         */
        """
        pass

    def get_gsgs(self, *args, **kwargs): # real signature unknown
        pass

    def get_incomplete_render(self, GraphicsStateGuardianBase_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_incomplete_render(GraphicsStateGuardianBase self)
        """
        pass

    def get_max_texture_dimension(self, GraphicsStateGuardianBase_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_max_texture_dimension(GraphicsStateGuardianBase self)
        """
        pass

    def get_max_vertices_per_array(self, GraphicsStateGuardianBase_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_max_vertices_per_array(GraphicsStateGuardianBase self)
        """
        pass

    def get_max_vertices_per_primitive(self, GraphicsStateGuardianBase_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_max_vertices_per_primitive(GraphicsStateGuardianBase self)
        """
        pass

    def get_num_gsgs(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_gsgs()
        
        /**
         * Returns the total number of GSG's in the universe.
         */
        """
        pass

    def get_supported_geom_rendering(self, GraphicsStateGuardianBase_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_supported_geom_rendering(GraphicsStateGuardianBase self)
        """
        pass

    def get_supports_compressed_texture_format(self, GraphicsStateGuardianBase_self, int_compression_mode): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_supports_compressed_texture_format(GraphicsStateGuardianBase self, int compression_mode)
        """
        pass

    def get_supports_hlsl(self, GraphicsStateGuardianBase_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_supports_hlsl(GraphicsStateGuardianBase self)
        """
        pass

    def get_supports_multisample(self, GraphicsStateGuardianBase_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_supports_multisample(GraphicsStateGuardianBase self)
        """
        pass

    def get_supports_shadow_filter(self, GraphicsStateGuardianBase_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_supports_shadow_filter(GraphicsStateGuardianBase self)
        """
        pass

    def get_supports_texture_srgb(self, GraphicsStateGuardianBase_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_supports_texture_srgb(GraphicsStateGuardianBase self)
        """
        pass

    def prefersTriangleStrips(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        prefers_triangle_strips(GraphicsStateGuardianBase self)
        """
        pass

    def prefers_triangle_strips(self, GraphicsStateGuardianBase_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        prefers_triangle_strips(GraphicsStateGuardianBase self)
        """
        pass

    def setDefaultGsg(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_default_gsg(GraphicsStateGuardianBase default_gsg)
        
        /**
         * Specifies a particular GSG to use as the "default" GSG.  See
         * get_default_gsg().
         */
        """
        pass

    def set_default_gsg(self, GraphicsStateGuardianBase_default_gsg): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_default_gsg(GraphicsStateGuardianBase default_gsg)
        
        /**
         * Specifies a particular GSG to use as the "default" GSG.  See
         * get_default_gsg().
         */
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__doc__': "/**\n * This is a base class for the GraphicsStateGuardian class, which is itself a\n * base class for the various GSG's for different platforms.  This class\n * contains all the function prototypes to support the double-dispatch of GSG\n * to geoms, transitions, etc.  It lives in a separate class in its own\n * package so we can avoid circular build dependency problems.\n *\n * GraphicsStateGuardians are not actually writable to bam files, of course,\n * but they may be passed as event parameters, so they inherit from\n * TypedWritableReferenceCount instead of TypedReferenceCount for that\n * convenience.\n */",
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.GraphicsStateGuardianBase' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE319D10>'
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE319D10>)>'
        'getDefaultGsg': None, # (!) real value is '<staticmethod(<built-in method getDefaultGsg of type object at 0x00007FFCFE319D10>)>'
        'getEffectiveIncompleteRender': None, # (!) real value is "<method 'getEffectiveIncompleteRender' of 'panda3d.core.GraphicsStateGuardianBase' objects>"
        'getGsg': None, # (!) real value is '<staticmethod(<built-in method getGsg of type object at 0x00007FFCFE319D10>)>'
        'getGsgs': None, # (!) real value is '<staticmethod(<built-in method getGsgs of type object at 0x00007FFCFE319D10>)>'
        'getIncompleteRender': None, # (!) real value is "<method 'getIncompleteRender' of 'panda3d.core.GraphicsStateGuardianBase' objects>"
        'getMaxTextureDimension': None, # (!) real value is "<method 'getMaxTextureDimension' of 'panda3d.core.GraphicsStateGuardianBase' objects>"
        'getMaxVerticesPerArray': None, # (!) real value is "<method 'getMaxVerticesPerArray' of 'panda3d.core.GraphicsStateGuardianBase' objects>"
        'getMaxVerticesPerPrimitive': None, # (!) real value is "<method 'getMaxVerticesPerPrimitive' of 'panda3d.core.GraphicsStateGuardianBase' objects>"
        'getNumGsgs': None, # (!) real value is '<staticmethod(<built-in method getNumGsgs of type object at 0x00007FFCFE319D10>)>'
        'getSupportedGeomRendering': None, # (!) real value is "<method 'getSupportedGeomRendering' of 'panda3d.core.GraphicsStateGuardianBase' objects>"
        'getSupportsCompressedTextureFormat': None, # (!) real value is "<method 'getSupportsCompressedTextureFormat' of 'panda3d.core.GraphicsStateGuardianBase' objects>"
        'getSupportsHlsl': None, # (!) real value is "<method 'getSupportsHlsl' of 'panda3d.core.GraphicsStateGuardianBase' objects>"
        'getSupportsMultisample': None, # (!) real value is "<method 'getSupportsMultisample' of 'panda3d.core.GraphicsStateGuardianBase' objects>"
        'getSupportsShadowFilter': None, # (!) real value is "<method 'getSupportsShadowFilter' of 'panda3d.core.GraphicsStateGuardianBase' objects>"
        'getSupportsTextureSrgb': None, # (!) real value is "<method 'getSupportsTextureSrgb' of 'panda3d.core.GraphicsStateGuardianBase' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE319D10>)>'
        'get_default_gsg': None, # (!) real value is '<staticmethod(<built-in method get_default_gsg of type object at 0x00007FFCFE319D10>)>'
        'get_effective_incomplete_render': None, # (!) real value is "<method 'get_effective_incomplete_render' of 'panda3d.core.GraphicsStateGuardianBase' objects>"
        'get_gsg': None, # (!) real value is '<staticmethod(<built-in method get_gsg of type object at 0x00007FFCFE319D10>)>'
        'get_gsgs': None, # (!) real value is '<staticmethod(<built-in method get_gsgs of type object at 0x00007FFCFE319D10>)>'
        'get_incomplete_render': None, # (!) real value is "<method 'get_incomplete_render' of 'panda3d.core.GraphicsStateGuardianBase' objects>"
        'get_max_texture_dimension': None, # (!) real value is "<method 'get_max_texture_dimension' of 'panda3d.core.GraphicsStateGuardianBase' objects>"
        'get_max_vertices_per_array': None, # (!) real value is "<method 'get_max_vertices_per_array' of 'panda3d.core.GraphicsStateGuardianBase' objects>"
        'get_max_vertices_per_primitive': None, # (!) real value is "<method 'get_max_vertices_per_primitive' of 'panda3d.core.GraphicsStateGuardianBase' objects>"
        'get_num_gsgs': None, # (!) real value is '<staticmethod(<built-in method get_num_gsgs of type object at 0x00007FFCFE319D10>)>'
        'get_supported_geom_rendering': None, # (!) real value is "<method 'get_supported_geom_rendering' of 'panda3d.core.GraphicsStateGuardianBase' objects>"
        'get_supports_compressed_texture_format': None, # (!) real value is "<method 'get_supports_compressed_texture_format' of 'panda3d.core.GraphicsStateGuardianBase' objects>"
        'get_supports_hlsl': None, # (!) real value is "<method 'get_supports_hlsl' of 'panda3d.core.GraphicsStateGuardianBase' objects>"
        'get_supports_multisample': None, # (!) real value is "<method 'get_supports_multisample' of 'panda3d.core.GraphicsStateGuardianBase' objects>"
        'get_supports_shadow_filter': None, # (!) real value is "<method 'get_supports_shadow_filter' of 'panda3d.core.GraphicsStateGuardianBase' objects>"
        'get_supports_texture_srgb': None, # (!) real value is "<method 'get_supports_texture_srgb' of 'panda3d.core.GraphicsStateGuardianBase' objects>"
        'prefersTriangleStrips': None, # (!) real value is "<method 'prefersTriangleStrips' of 'panda3d.core.GraphicsStateGuardianBase' objects>"
        'prefers_triangle_strips': None, # (!) real value is "<method 'prefers_triangle_strips' of 'panda3d.core.GraphicsStateGuardianBase' objects>"
        'setDefaultGsg': None, # (!) real value is '<staticmethod(<built-in method setDefaultGsg of type object at 0x00007FFCFE319D10>)>'
        'set_default_gsg': None, # (!) real value is '<staticmethod(<built-in method set_default_gsg of type object at 0x00007FFCFE319D10>)>'
    }


