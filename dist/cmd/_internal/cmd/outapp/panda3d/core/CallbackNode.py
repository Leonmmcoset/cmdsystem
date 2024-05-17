# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .PandaNode import PandaNode

class CallbackNode(PandaNode):
    """
    /**
     * A special node that can issue arbitrary callbacks to user code, either
     * during the cull or draw traversals.
     */
    """
    def clearCullCallback(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_cull_callback(const CallbackNode self)
        
        /**
         * Removes the callback set by an earlier call to set_cull_callback().
         */
        """
        pass

    def clearDrawCallback(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_draw_callback(const CallbackNode self)
        
        /**
         * Removes the callback set by an earlier call to set_draw_callback().
         */
        """
        pass

    def clear_cull_callback(self, const_CallbackNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_cull_callback(const CallbackNode self)
        
        /**
         * Removes the callback set by an earlier call to set_cull_callback().
         */
        """
        pass

    def clear_draw_callback(self, const_CallbackNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_draw_callback(const CallbackNode self)
        
        /**
         * Removes the callback set by an earlier call to set_draw_callback().
         */
        """
        pass

    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getCullCallback(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_cull_callback(CallbackNode self)
        
        /**
         * Returns the CallbackObject set by set_cull_callback().
         */
        """
        pass

    def getDrawCallback(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_draw_callback(CallbackNode self)
        
        /**
         * Returns the CallbackObject set by set_draw_callback().
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_cull_callback(self, CallbackNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_cull_callback(CallbackNode self)
        
        /**
         * Returns the CallbackObject set by set_cull_callback().
         */
        """
        pass

    def get_draw_callback(self, CallbackNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_draw_callback(CallbackNode self)
        
        /**
         * Returns the CallbackObject set by set_draw_callback().
         */
        """
        pass

    def setCullCallback(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_cull_callback(const CallbackNode self, CallbackObject object)
        
        /**
         * Sets the CallbackObject that will be notified when this node is visited
         * during the cull traversal.  This callback will be made during the cull
         * thread.
         *
         * The cull traversal is responsible for determining which nodes are visible
         * and within the view frustum, and for accumulating state and transform, and
         * generally building up the list of CullableObjects that are to be eventually
         * passed to the draw traversal for rendering.
         *
         * At the time the cull traversal callback is made, the node has been
         * determined to be visible and it has passed the bounding-volume test, so it
         * lies within the view frustum.
         *
         * The callback is passed an instance of a NodeCullCallbackData, which
         * contains pointers to the CullTraverser and CullTraverserData--enough data
         * to examine the current node and its place within the scene graph.  The
         * callback *replaces* the normal cull behavior, so if your callback does
         * nothing, the cull traversal will not continue below this node.  If you wish
         * the cull traversal to continue to visit this node and below, you must call
         * cbdata->upcall() from your callback.
         */
        """
        pass

    def setDrawCallback(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_draw_callback(const CallbackNode self, CallbackObject object)
        
        /**
         * Sets the CallbackObject that will be notified when this node is visited
         * during the draw traversal.  This callback will be made during the draw
         * thread.
         *
         * The draw traversal is responsible for actually issuing the commands to the
         * graphics engine to draw primitives.  Its job is to walk through the list of
         * CullableObjects build up by the cull traversal, as quickly as possible,
         * issuing the appropriate commands to draw each one.
         *
         * At the time the draw traversal callback is made, the graphics state has
         * been loaded with the correct modelview transform and render state, and the
         * primitives (if any) in this node are ready to be drawn.
         *
         * The callback is passed an instance of a GeomDrawCallbackData, which
         * contains pointers to the current state and transform, as well as the
         * current GSG.  There is a Geom pointer as well, but it will always be NULL
         * to this callback, since the CallbackNode does not itself contain any Geoms.
         */
        """
        pass

    def set_cull_callback(self, const_CallbackNode_self, CallbackObject_object): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_cull_callback(const CallbackNode self, CallbackObject object)
        
        /**
         * Sets the CallbackObject that will be notified when this node is visited
         * during the cull traversal.  This callback will be made during the cull
         * thread.
         *
         * The cull traversal is responsible for determining which nodes are visible
         * and within the view frustum, and for accumulating state and transform, and
         * generally building up the list of CullableObjects that are to be eventually
         * passed to the draw traversal for rendering.
         *
         * At the time the cull traversal callback is made, the node has been
         * determined to be visible and it has passed the bounding-volume test, so it
         * lies within the view frustum.
         *
         * The callback is passed an instance of a NodeCullCallbackData, which
         * contains pointers to the CullTraverser and CullTraverserData--enough data
         * to examine the current node and its place within the scene graph.  The
         * callback *replaces* the normal cull behavior, so if your callback does
         * nothing, the cull traversal will not continue below this node.  If you wish
         * the cull traversal to continue to visit this node and below, you must call
         * cbdata->upcall() from your callback.
         */
        """
        pass

    def set_draw_callback(self, const_CallbackNode_self, CallbackObject_object): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_draw_callback(const CallbackNode self, CallbackObject object)
        
        /**
         * Sets the CallbackObject that will be notified when this node is visited
         * during the draw traversal.  This callback will be made during the draw
         * thread.
         *
         * The draw traversal is responsible for actually issuing the commands to the
         * graphics engine to draw primitives.  Its job is to walk through the list of
         * CullableObjects build up by the cull traversal, as quickly as possible,
         * issuing the appropriate commands to draw each one.
         *
         * At the time the draw traversal callback is made, the graphics state has
         * been loaded with the correct modelview transform and render state, and the
         * primitives (if any) in this node are ready to be drawn.
         *
         * The callback is passed an instance of a GeomDrawCallbackData, which
         * contains pointers to the current state and transform, as well as the
         * current GSG.  There is a Geom pointer as well, but it will always be NULL
         * to this callback, since the CallbackNode does not itself contain any Geoms.
         */
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    cull_callback = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    draw_callback = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__doc__': '/**\n * A special node that can issue arbitrary callbacks to user code, either\n * during the cull or draw traversals.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.CallbackNode' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE287190>'
        'clearCullCallback': None, # (!) real value is "<method 'clearCullCallback' of 'panda3d.core.CallbackNode' objects>"
        'clearDrawCallback': None, # (!) real value is "<method 'clearDrawCallback' of 'panda3d.core.CallbackNode' objects>"
        'clear_cull_callback': None, # (!) real value is "<method 'clear_cull_callback' of 'panda3d.core.CallbackNode' objects>"
        'clear_draw_callback': None, # (!) real value is "<method 'clear_draw_callback' of 'panda3d.core.CallbackNode' objects>"
        'cull_callback': None, # (!) real value is "<attribute 'cull_callback' of 'panda3d.core.CallbackNode' objects>"
        'draw_callback': None, # (!) real value is "<attribute 'draw_callback' of 'panda3d.core.CallbackNode' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE287190>)>'
        'getCullCallback': None, # (!) real value is "<method 'getCullCallback' of 'panda3d.core.CallbackNode' objects>"
        'getDrawCallback': None, # (!) real value is "<method 'getDrawCallback' of 'panda3d.core.CallbackNode' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE287190>)>'
        'get_cull_callback': None, # (!) real value is "<method 'get_cull_callback' of 'panda3d.core.CallbackNode' objects>"
        'get_draw_callback': None, # (!) real value is "<method 'get_draw_callback' of 'panda3d.core.CallbackNode' objects>"
        'setCullCallback': None, # (!) real value is "<method 'setCullCallback' of 'panda3d.core.CallbackNode' objects>"
        'setDrawCallback': None, # (!) real value is "<method 'setDrawCallback' of 'panda3d.core.CallbackNode' objects>"
        'set_cull_callback': None, # (!) real value is "<method 'set_cull_callback' of 'panda3d.core.CallbackNode' objects>"
        'set_draw_callback': None, # (!) real value is "<method 'set_draw_callback' of 'panda3d.core.CallbackNode' objects>"
    }


