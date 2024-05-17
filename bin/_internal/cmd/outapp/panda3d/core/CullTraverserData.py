# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


class CullTraverserData(__dtoolconfig.DTOOL_SUPER_BASE):
    """
    /**
     * This collects together the pieces of data that are accumulated for each
     * node while walking the scene graph during the cull traversal.
     *
     * Having this as a separate object simplifies the parameter list to
     * CullTraverser::r_traverse(), as well as to other functions like
     * PandaNode::cull_callback().  It also makes it easier to add cull
     * parameters, and provides a place to abstract out some of the cull behavior
     * (like view-frustum culling).
     */
    """
    def applyTransform(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        apply_transform(const CullTraverserData self, const TransformState node_transform)
        
        /**
         * Applies the indicated transform changes onto the current data.
         */
        """
        pass

    def applyTransformAndState(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        apply_transform_and_state(const CullTraverserData self, CullTraverser trav)
        
        /**
         * Applies the transform and state from the current node onto the current
         * data.  This also evaluates billboards, etc.
         */
        """
        pass

    def apply_transform(self, const_CullTraverserData_self, const_TransformState_node_transform): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        apply_transform(const CullTraverserData self, const TransformState node_transform)
        
        /**
         * Applies the indicated transform changes onto the current data.
         */
        """
        pass

    def apply_transform_and_state(self, const_CullTraverserData_self, CullTraverser_trav): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        apply_transform_and_state(const CullTraverserData self, CullTraverser trav)
        
        /**
         * Applies the transform and state from the current node onto the current
         * data.  This also evaluates billboards, etc.
         */
        """
        pass

    def getInternalTransform(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_internal_transform(CullTraverserData self, const CullTraverser trav)
        
        /**
         * Returns the internal transform: the modelview transform in the GSG's
         * internal coordinate system.
         */
        """
        pass

    def getModelviewTransform(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_modelview_transform(CullTraverserData self, const CullTraverser trav)
        
        /**
         * Returns the modelview transform: the relative transform from the camera to
         * the model.
         */
        """
        pass

    def getNetTransform(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_net_transform(CullTraverserData self, const CullTraverser trav)
        
        /**
         * Returns the net transform: the relative transform from root of the scene
         * graph to the current node.
         */
        """
        pass

    def get_internal_transform(self, CullTraverserData_self, const_CullTraverser_trav): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_internal_transform(CullTraverserData self, const CullTraverser trav)
        
        /**
         * Returns the internal transform: the modelview transform in the GSG's
         * internal coordinate system.
         */
        """
        pass

    def get_modelview_transform(self, CullTraverserData_self, const_CullTraverser_trav): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_modelview_transform(CullTraverserData self, const CullTraverser trav)
        
        /**
         * Returns the modelview transform: the relative transform from the camera to
         * the model.
         */
        """
        pass

    def get_net_transform(self, CullTraverserData_self, const_CullTraverser_trav): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_net_transform(CullTraverserData self, const CullTraverser trav)
        
        /**
         * Returns the net transform: the relative transform from root of the scene
         * graph to the current node.
         */
        """
        pass

    def isInView(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_in_view(const CullTraverserData self, const BitMask camera_mask)
        
        /**
         * Returns true if the current node is within the view frustum, false
         * otherwise.  If the node's bounding volume falls completely within the view
         * frustum, this will also reset the view frustum pointer, saving some work
         * for future nodes.
         */
        """
        pass

    def isThisNodeHidden(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_this_node_hidden(CullTraverserData self, const BitMask camera_mask)
        
        /**
         * Returns true if this particular node is hidden, even though we might be
         * traversing past this node to find a child node that has had show_through()
         * called for it.  If this returns true, the node should not be rendered.
         */
        """
        pass

    def is_in_view(self, const_CullTraverserData_self, const_BitMask_camera_mask): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_in_view(const CullTraverserData self, const BitMask camera_mask)
        
        /**
         * Returns true if the current node is within the view frustum, false
         * otherwise.  If the node's bounding volume falls completely within the view
         * frustum, this will also reset the view frustum pointer, saving some work
         * for future nodes.
         */
        """
        pass

    def is_this_node_hidden(self, CullTraverserData_self, const_BitMask_camera_mask): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_this_node_hidden(CullTraverserData self, const BitMask camera_mask)
        
        /**
         * Returns true if this particular node is hidden, even though we might be
         * traversing past this node to find a child node that has had show_through()
         * called for it.  If this returns true, the node should not be rendered.
         */
        """
        pass

    def node(self, CullTraverserData_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        node(CullTraverserData self)
        
        /**
         * Returns the node traversed to so far.
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

    node_path = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.core.CullTraverserData' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.core.CullTraverserData' objects>"
        '__doc__': '/**\n * This collects together the pieces of data that are accumulated for each\n * node while walking the scene graph during the cull traversal.\n *\n * Having this as a separate object simplifies the parameter list to\n * CullTraverser::r_traverse(), as well as to other functions like\n * PandaNode::cull_callback().  It also makes it easier to add cull\n * parameters, and provides a place to abstract out some of the cull behavior\n * (like view-frustum culling).\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.CullTraverserData' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE2965F0>'
        'applyTransform': None, # (!) real value is "<method 'applyTransform' of 'panda3d.core.CullTraverserData' objects>"
        'applyTransformAndState': None, # (!) real value is "<method 'applyTransformAndState' of 'panda3d.core.CullTraverserData' objects>"
        'apply_transform': None, # (!) real value is "<method 'apply_transform' of 'panda3d.core.CullTraverserData' objects>"
        'apply_transform_and_state': None, # (!) real value is "<method 'apply_transform_and_state' of 'panda3d.core.CullTraverserData' objects>"
        'getInternalTransform': None, # (!) real value is "<method 'getInternalTransform' of 'panda3d.core.CullTraverserData' objects>"
        'getModelviewTransform': None, # (!) real value is "<method 'getModelviewTransform' of 'panda3d.core.CullTraverserData' objects>"
        'getNetTransform': None, # (!) real value is "<method 'getNetTransform' of 'panda3d.core.CullTraverserData' objects>"
        'get_internal_transform': None, # (!) real value is "<method 'get_internal_transform' of 'panda3d.core.CullTraverserData' objects>"
        'get_modelview_transform': None, # (!) real value is "<method 'get_modelview_transform' of 'panda3d.core.CullTraverserData' objects>"
        'get_net_transform': None, # (!) real value is "<method 'get_net_transform' of 'panda3d.core.CullTraverserData' objects>"
        'isInView': None, # (!) real value is "<method 'isInView' of 'panda3d.core.CullTraverserData' objects>"
        'isThisNodeHidden': None, # (!) real value is "<method 'isThisNodeHidden' of 'panda3d.core.CullTraverserData' objects>"
        'is_in_view': None, # (!) real value is "<method 'is_in_view' of 'panda3d.core.CullTraverserData' objects>"
        'is_this_node_hidden': None, # (!) real value is "<method 'is_this_node_hidden' of 'panda3d.core.CullTraverserData' objects>"
        'node': None, # (!) real value is "<method 'node' of 'panda3d.core.CullTraverserData' objects>"
        'node_path': None, # (!) real value is "<attribute 'node_path' of 'panda3d.core.CullTraverserData' objects>"
    }


