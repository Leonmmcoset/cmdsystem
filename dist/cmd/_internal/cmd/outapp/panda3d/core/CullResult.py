# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .ReferenceCount import ReferenceCount

class CullResult(ReferenceCount):
    """
    /**
     * This stores the result of a BinCullHandler traversal: an ordered collection
     * of CullBins, each of which holds a number of Geoms and RenderStates to be
     * rendered in some defined order.
     *
     * This is also used to keep the results of last frame's cull traversal around
     * to make next frame's traversal of the same scene a little easier.
     */
    """
    def draw(self, const_CullResult_self, Thread_current_thread): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        draw(const CullResult self, Thread current_thread)
        
        /**
         * Asks all the bins to draw themselves in the correct order.
         */
        """
        pass

    def finishCull(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        finish_cull(const CullResult self, SceneSetup scene_setup, Thread current_thread)
        
        /**
         * Called after all the geoms have been added, this indicates that the cull
         * process is finished for this frame and gives the bins a chance to do any
         * post-processing (like sorting) before moving on to draw.
         */
        """
        pass

    def finish_cull(self, const_CullResult_self, SceneSetup_scene_setup, Thread_current_thread): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        finish_cull(const CullResult self, SceneSetup scene_setup, Thread current_thread)
        
        /**
         * Called after all the geoms have been added, this indicates that the cull
         * process is finished for this frame and gives the bins a chance to do any
         * post-processing (like sorting) before moving on to draw.
         */
        """
        pass

    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def makeNext(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        make_next(CullResult self)
        
        /**
         * Returns a newly-allocated CullResult object that contains a copy of just
         * the subset of the data from this CullResult object that is worth keeping
         * around for next frame.
         */
        """
        pass

    def makeResultGraph(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        make_result_graph(const CullResult self)
        
        /**
         * Returns a special scene graph constructed to represent the results of the
         * cull.  This will be a hierarchy of nodes, one node for each bin, each of
         * which will in term be a parent of a number of GeomNodes, representing the
         * geometry drawn in each bin.
         *
         * This is useful mainly for high-level debugging and abstraction tools; it
         * should not be mistaken for the low-level cull result itself.  For the low-
         * level cull result, use draw() to efficiently draw the culled scene.
         */
        """
        pass

    def make_next(self, CullResult_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        make_next(CullResult self)
        
        /**
         * Returns a newly-allocated CullResult object that contains a copy of just
         * the subset of the data from this CullResult object that is worth keeping
         * around for next frame.
         */
        """
        pass

    def make_result_graph(self, const_CullResult_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        make_result_graph(const CullResult self)
        
        /**
         * Returns a special scene graph constructed to represent the results of the
         * cull.  This will be a hierarchy of nodes, one node for each bin, each of
         * which will in term be a parent of a number of GeomNodes, representing the
         * geometry drawn in each bin.
         *
         * This is useful mainly for high-level debugging and abstraction tools; it
         * should not be mistaken for the low-level cull result itself.  For the low-
         * level cull result, use draw() to efficiently draw the culled scene.
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

    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.core.CullResult' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.core.CullResult' objects>"
        '__doc__': "/**\n * This stores the result of a BinCullHandler traversal: an ordered collection\n * of CullBins, each of which holds a number of Geoms and RenderStates to be\n * rendered in some defined order.\n *\n * This is also used to keep the results of last frame's cull traversal around\n * to make next frame's traversal of the same scene a little easier.\n */",
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.CullResult' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE2972A0>'
        'draw': None, # (!) real value is "<method 'draw' of 'panda3d.core.CullResult' objects>"
        'finishCull': None, # (!) real value is "<method 'finishCull' of 'panda3d.core.CullResult' objects>"
        'finish_cull': None, # (!) real value is "<method 'finish_cull' of 'panda3d.core.CullResult' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE2972A0>)>'
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE2972A0>)>'
        'makeNext': None, # (!) real value is "<method 'makeNext' of 'panda3d.core.CullResult' objects>"
        'makeResultGraph': None, # (!) real value is "<method 'makeResultGraph' of 'panda3d.core.CullResult' objects>"
        'make_next': None, # (!) real value is "<method 'make_next' of 'panda3d.core.CullResult' objects>"
        'make_result_graph': None, # (!) real value is "<method 'make_result_graph' of 'panda3d.core.CullResult' objects>"
    }


