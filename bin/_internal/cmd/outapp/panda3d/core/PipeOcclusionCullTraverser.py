# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .CullTraverser import CullTraverser

class PipeOcclusionCullTraverser(CullTraverser):
    """
    /**
     * This specialization of CullTraverser uses the graphics pipe itself to
     * perform occlusion culling.  As such, it's likely to be inefficient (since
     * it interferes with the pipe's normal mode of rendering), and is mainly
     * useful to test other, CPU-based occlusion algorithms.
     *
     * This cannot be used in a multithreaded pipeline environment where cull and
     * draw are operating simultaneously.
     *
     * It can't be defined in the cull subdirectory, because it needs access to
     * GraphicsPipe and DisplayRegion and other classes in display.  So we put it
     * in grutil instead, for lack of any better ideas.
     */
    """
    def endTraverse(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        end_traverse(const PipeOcclusionCullTraverser self)
        
        /**
         * Should be called when the traverser has finished traversing its scene, this
         * gives it a chance to do any necessary finalization.
         */
        """
        pass

    def end_traverse(self, const_PipeOcclusionCullTraverser_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        end_traverse(const PipeOcclusionCullTraverser self)
        
        /**
         * Should be called when the traverser has finished traversing its scene, this
         * gives it a chance to do any necessary finalization.
         */
        """
        pass

    def getBuffer(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_buffer(PipeOcclusionCullTraverser self)
        
        /**
         *
         */
        """
        pass

    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getOcclusionMask(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_occlusion_mask(PipeOcclusionCullTraverser self)
        
        /**
         * Returns the DrawMask for occlusion polygons.  See set_occlusion_mask().
         */
        """
        pass

    def getTexture(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_texture(const PipeOcclusionCullTraverser self)
        
        /**
         * Returns a Texture that can be used to visualize the efforts of the
         * occlusion cull.
         */
        """
        pass

    def get_buffer(self, PipeOcclusionCullTraverser_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_buffer(PipeOcclusionCullTraverser self)
        
        /**
         *
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_occlusion_mask(self, PipeOcclusionCullTraverser_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_occlusion_mask(PipeOcclusionCullTraverser self)
        
        /**
         * Returns the DrawMask for occlusion polygons.  See set_occlusion_mask().
         */
        """
        pass

    def get_texture(self, const_PipeOcclusionCullTraverser_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_texture(const PipeOcclusionCullTraverser self)
        
        /**
         * Returns a Texture that can be used to visualize the efforts of the
         * occlusion cull.
         */
        """
        pass

    def setOcclusionMask(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_occlusion_mask(const PipeOcclusionCullTraverser self, const BitMask occlusion_mask)
        
        /**
         * Specifies the DrawMask that should be set on occlusion polygons for this
         * scene.  This identifies the polygons that are to be treated as occluders.
         * Polygons that do not have this draw mask set will not be considered
         * occluders.
         */
        """
        pass

    def setScene(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_scene(const PipeOcclusionCullTraverser self, SceneSetup scene_setup, GraphicsStateGuardianBase gsg, bool dr_incomplete_render)
        
        /**
         *
         */
        """
        pass

    def set_occlusion_mask(self, const_PipeOcclusionCullTraverser_self, const_BitMask_occlusion_mask): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_occlusion_mask(const PipeOcclusionCullTraverser self, const BitMask occlusion_mask)
        
        /**
         * Specifies the DrawMask that should be set on occlusion polygons for this
         * scene.  This identifies the polygons that are to be treated as occluders.
         * Polygons that do not have this draw mask set will not be considered
         * occluders.
         */
        """
        pass

    def set_scene(self, const_PipeOcclusionCullTraverser_self, SceneSetup_scene_setup, GraphicsStateGuardianBase_gsg, bool_dr_incomplete_render): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_scene(const PipeOcclusionCullTraverser self, SceneSetup scene_setup, GraphicsStateGuardianBase gsg, bool dr_incomplete_render)
        
        /**
         *
         */
        """
        pass

    def upcastToCullTraverser(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        upcast_to_CullTraverser(const PipeOcclusionCullTraverser self)
        
        upcast from PipeOcclusionCullTraverser to CullTraverser
        """
        pass

    def upcast_to_CullTraverser(self, const_PipeOcclusionCullTraverser_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        upcast_to_CullTraverser(const PipeOcclusionCullTraverser self)
        
        upcast from PipeOcclusionCullTraverser to CullTraverser
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
        '__doc__': "/**\n * This specialization of CullTraverser uses the graphics pipe itself to\n * perform occlusion culling.  As such, it's likely to be inefficient (since\n * it interferes with the pipe's normal mode of rendering), and is mainly\n * useful to test other, CPU-based occlusion algorithms.\n *\n * This cannot be used in a multithreaded pipeline environment where cull and\n * draw are operating simultaneously.\n *\n * It can't be defined in the cull subdirectory, because it needs access to\n * GraphicsPipe and DisplayRegion and other classes in display.  So we put it\n * in grutil instead, for lack of any better ideas.\n */",
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.PipeOcclusionCullTraverser' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE2BD950>'
        'endTraverse': None, # (!) real value is "<method 'endTraverse' of 'panda3d.core.PipeOcclusionCullTraverser' objects>"
        'end_traverse': None, # (!) real value is "<method 'end_traverse' of 'panda3d.core.PipeOcclusionCullTraverser' objects>"
        'getBuffer': None, # (!) real value is "<method 'getBuffer' of 'panda3d.core.PipeOcclusionCullTraverser' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE2BD950>)>'
        'getOcclusionMask': None, # (!) real value is "<method 'getOcclusionMask' of 'panda3d.core.PipeOcclusionCullTraverser' objects>"
        'getTexture': None, # (!) real value is "<method 'getTexture' of 'panda3d.core.PipeOcclusionCullTraverser' objects>"
        'get_buffer': None, # (!) real value is "<method 'get_buffer' of 'panda3d.core.PipeOcclusionCullTraverser' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE2BD950>)>'
        'get_occlusion_mask': None, # (!) real value is "<method 'get_occlusion_mask' of 'panda3d.core.PipeOcclusionCullTraverser' objects>"
        'get_texture': None, # (!) real value is "<method 'get_texture' of 'panda3d.core.PipeOcclusionCullTraverser' objects>"
        'setOcclusionMask': None, # (!) real value is "<method 'setOcclusionMask' of 'panda3d.core.PipeOcclusionCullTraverser' objects>"
        'setScene': None, # (!) real value is "<method 'setScene' of 'panda3d.core.PipeOcclusionCullTraverser' objects>"
        'set_occlusion_mask': None, # (!) real value is "<method 'set_occlusion_mask' of 'panda3d.core.PipeOcclusionCullTraverser' objects>"
        'set_scene': None, # (!) real value is "<method 'set_scene' of 'panda3d.core.PipeOcclusionCullTraverser' objects>"
        'upcastToCullTraverser': None, # (!) real value is "<method 'upcastToCullTraverser' of 'panda3d.core.PipeOcclusionCullTraverser' objects>"
        'upcast_to_CullTraverser': None, # (!) real value is "<method 'upcast_to_CullTraverser' of 'panda3d.core.PipeOcclusionCullTraverser' objects>"
    }


