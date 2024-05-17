# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .GeomEnums import GeomEnums

class GeomVertexAnimationSpec(GeomEnums):
    """
    /**
     * This object describes how the vertex animation, if any, represented in a
     * GeomVertexData is encoded.
     *
     * Vertex animation includes soft-skinned skeleton animation and morphs (blend
     * shapes), and might be performed on the CPU by Panda, or passed down to the
     * graphics backed to be performed on the hardware (depending on the
     * hardware's advertised capabilities).
     *
     * Changing this setting doesn't by itself change the way the animation is
     * actually performed; this just specifies how the vertices are set up to be
     * animated.
     */
    """
    def assign(self, const_GeomVertexAnimationSpec_self, const_GeomVertexAnimationSpec_other): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        assign(const GeomVertexAnimationSpec self, const GeomVertexAnimationSpec other)
        """
        pass

    def getAnimationType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_animation_type(GeomVertexAnimationSpec self)
        
        /**
         * Returns the type of animation represented by this spec.
         */
        """
        pass

    def getIndexedTransforms(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_indexed_transforms(GeomVertexAnimationSpec self)
        
        /**
         * This is only meaningful for animation_type AT_hardware.  If true, it
         * indicates that the format uses indexed animation tables.  It is false if
         * each vertex will reference the first _num_transforms table entries only.
         */
        """
        pass

    def getNumTransforms(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_transforms(GeomVertexAnimationSpec self)
        
        /**
         * This is only meaningful for animation_type AT_hardware.  It specifies the
         * maximum number of transforms that might be simultaneously applied to any
         * one vertex by the data in this format.
         */
        """
        pass

    def get_animation_type(self, GeomVertexAnimationSpec_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_animation_type(GeomVertexAnimationSpec self)
        
        /**
         * Returns the type of animation represented by this spec.
         */
        """
        pass

    def get_indexed_transforms(self, GeomVertexAnimationSpec_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_indexed_transforms(GeomVertexAnimationSpec self)
        
        /**
         * This is only meaningful for animation_type AT_hardware.  If true, it
         * indicates that the format uses indexed animation tables.  It is false if
         * each vertex will reference the first _num_transforms table entries only.
         */
        """
        pass

    def get_num_transforms(self, GeomVertexAnimationSpec_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_transforms(GeomVertexAnimationSpec self)
        
        /**
         * This is only meaningful for animation_type AT_hardware.  It specifies the
         * maximum number of transforms that might be simultaneously applied to any
         * one vertex by the data in this format.
         */
        """
        pass

    def output(self, GeomVertexAnimationSpec_self, ostream_out): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        output(GeomVertexAnimationSpec self, ostream out)
        
        /**
         *
         */
        """
        pass

    def setHardware(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_hardware(const GeomVertexAnimationSpec self, int num_transforms, bool indexed_transforms)
        
        /**
         * Specifies that vertex animation is to be performed by the graphics hardware
         * (or at least by the graphics backend API, which is actually still free to
         * animate the vertices on the CPU).
         *
         * This is only legal if the graphics hardware can support the specified
         * limits on number of transforms and/or indexed transforms.  Also, no current
         * graphics API's support morphing.
         */
        """
        pass

    def setNone(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_none(const GeomVertexAnimationSpec self)
        
        /**
         * Specifies that no vertex animation is represented by this spec.
         */
        """
        pass

    def setPanda(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_panda(const GeomVertexAnimationSpec self)
        
        /**
         * Specifies that vertex animation is to be performed by Panda.  This is the
         * most general setting and can handle any kind of vertex animation
         * represented.
         */
        """
        pass

    def set_hardware(self, const_GeomVertexAnimationSpec_self, int_num_transforms, bool_indexed_transforms): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_hardware(const GeomVertexAnimationSpec self, int num_transforms, bool indexed_transforms)
        
        /**
         * Specifies that vertex animation is to be performed by the graphics hardware
         * (or at least by the graphics backend API, which is actually still free to
         * animate the vertices on the CPU).
         *
         * This is only legal if the graphics hardware can support the specified
         * limits on number of transforms and/or indexed transforms.  Also, no current
         * graphics API's support morphing.
         */
        """
        pass

    def set_none(self, const_GeomVertexAnimationSpec_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_none(const GeomVertexAnimationSpec self)
        
        /**
         * Specifies that no vertex animation is represented by this spec.
         */
        """
        pass

    def set_panda(self, const_GeomVertexAnimationSpec_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_panda(const GeomVertexAnimationSpec self)
        
        /**
         * Specifies that vertex animation is to be performed by Panda.  This is the
         * most general setting and can handle any kind of vertex animation
         * represented.
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

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    animation_type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    indexed_transforms = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    num_transforms = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.core.GeomVertexAnimationSpec' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.core.GeomVertexAnimationSpec' objects>"
        '__doc__': "/**\n * This object describes how the vertex animation, if any, represented in a\n * GeomVertexData is encoded.\n *\n * Vertex animation includes soft-skinned skeleton animation and morphs (blend\n * shapes), and might be performed on the CPU by Panda, or passed down to the\n * graphics backed to be performed on the hardware (depending on the\n * hardware's advertised capabilities).\n *\n * Changing this setting doesn't by itself change the way the animation is\n * actually performed; this just specifies how the vertices are set up to be\n * animated.\n */",
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.GeomVertexAnimationSpec' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE2F9BB0>'
        '__repr__': None, # (!) real value is "<slot wrapper '__repr__' of 'panda3d.core.GeomVertexAnimationSpec' objects>"
        '__str__': None, # (!) real value is "<slot wrapper '__str__' of 'panda3d.core.GeomVertexAnimationSpec' objects>"
        'animation_type': None, # (!) real value is "<attribute 'animation_type' of 'panda3d.core.GeomVertexAnimationSpec' objects>"
        'assign': None, # (!) real value is "<method 'assign' of 'panda3d.core.GeomVertexAnimationSpec' objects>"
        'getAnimationType': None, # (!) real value is "<method 'getAnimationType' of 'panda3d.core.GeomVertexAnimationSpec' objects>"
        'getIndexedTransforms': None, # (!) real value is "<method 'getIndexedTransforms' of 'panda3d.core.GeomVertexAnimationSpec' objects>"
        'getNumTransforms': None, # (!) real value is "<method 'getNumTransforms' of 'panda3d.core.GeomVertexAnimationSpec' objects>"
        'get_animation_type': None, # (!) real value is "<method 'get_animation_type' of 'panda3d.core.GeomVertexAnimationSpec' objects>"
        'get_indexed_transforms': None, # (!) real value is "<method 'get_indexed_transforms' of 'panda3d.core.GeomVertexAnimationSpec' objects>"
        'get_num_transforms': None, # (!) real value is "<method 'get_num_transforms' of 'panda3d.core.GeomVertexAnimationSpec' objects>"
        'indexed_transforms': None, # (!) real value is "<attribute 'indexed_transforms' of 'panda3d.core.GeomVertexAnimationSpec' objects>"
        'num_transforms': None, # (!) real value is "<attribute 'num_transforms' of 'panda3d.core.GeomVertexAnimationSpec' objects>"
        'output': None, # (!) real value is "<method 'output' of 'panda3d.core.GeomVertexAnimationSpec' objects>"
        'setHardware': None, # (!) real value is "<method 'setHardware' of 'panda3d.core.GeomVertexAnimationSpec' objects>"
        'setNone': None, # (!) real value is "<method 'setNone' of 'panda3d.core.GeomVertexAnimationSpec' objects>"
        'setPanda': None, # (!) real value is "<method 'setPanda' of 'panda3d.core.GeomVertexAnimationSpec' objects>"
        'set_hardware': None, # (!) real value is "<method 'set_hardware' of 'panda3d.core.GeomVertexAnimationSpec' objects>"
        'set_none': None, # (!) real value is "<method 'set_none' of 'panda3d.core.GeomVertexAnimationSpec' objects>"
        'set_panda': None, # (!) real value is "<method 'set_panda' of 'panda3d.core.GeomVertexAnimationSpec' objects>"
    }


