# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .PandaNode import PandaNode

class RigidBodyCombiner(PandaNode):
    """
    /**
     * This is a special node that combines multiple independently-moving rigid
     * nodes into one Geom internally (or as few Geoms as possible), for the
     * purposes of improving rendering performance.
     *
     * To use it, parent a number of moving objects to this node and call
     * collect().  A child node is identified as "moving" if (a) it has a non-
     * identity transform initially, or (b) it is a ModelNode with the
     * preserve_transform flag set.  Any other nodes will be considered static,
     * and later transforms applied to them will not be identified.
     *
     * You should call collect() only at startup or if you change the set of
     * children; it is a relatively expensive call.
     *
     * Once you call collect(), you may change the transforms on the child nodes
     * freely without having to call collect() again.
     *
     * RenderEffects such as Billboards are not supported below this node.
     */
    """
    def collect(self, const_RigidBodyCombiner_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        collect(const RigidBodyCombiner self)
        
        /**
         * Walks through the entire subgraph of nodes rooted at this node, accumulates
         * all of the RenderAttribs and Geoms below this node, flattening them into
         * just one Geom (or as few as possible, if there are multiple different
         * states).
         *
         * Nodes that have transforms on them at the time of collect(), or any
         * ModelNodes with the preserve_transform flag, will be identified as "moving"
         * nodes, and their transforms will be monitored as they change in future
         * frames and each new transform directly applied to the vertices.
         *
         * This call must be made after adding any nodes to or removing any nodes from
         * the subgraph rooted at this node.  It should not be made too often, as it
         * is a relatively expensive call.  If you need to hide children of this node,
         * consider scaling them to zero (or very near zero), or moving them behind
         * the camera, instead.
         */
        """
        pass

    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getInternalScene(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_internal_scene(const RigidBodyCombiner self)
        
        /**
         * Returns a special NodePath that represents the internal node of this
         * object.  This is the node that is actually sent to the graphics card for
         * rendering; it contains the collection of the children of this node into as
         * few Geoms as possible.
         *
         * This node is filled up by the last call to collect().
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_internal_scene(self, const_RigidBodyCombiner_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_internal_scene(const RigidBodyCombiner self)
        
        /**
         * Returns a special NodePath that represents the internal node of this
         * object.  This is the node that is actually sent to the graphics card for
         * rendering; it contains the collection of the children of this node into as
         * few Geoms as possible.
         *
         * This node is filled up by the last call to collect().
         */
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    internal_scene = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__doc__': '/**\n * This is a special node that combines multiple independently-moving rigid\n * nodes into one Geom internally (or as few Geoms as possible), for the\n * purposes of improving rendering performance.\n *\n * To use it, parent a number of moving objects to this node and call\n * collect().  A child node is identified as "moving" if (a) it has a non-\n * identity transform initially, or (b) it is a ModelNode with the\n * preserve_transform flag set.  Any other nodes will be considered static,\n * and later transforms applied to them will not be identified.\n *\n * You should call collect() only at startup or if you change the set of\n * children; it is a relatively expensive call.\n *\n * Once you call collect(), you may change the transforms on the child nodes\n * freely without having to call collect() again.\n *\n * RenderEffects such as Billboards are not supported below this node.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.RigidBodyCombiner' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE2BD780>'
        'collect': None, # (!) real value is "<method 'collect' of 'panda3d.core.RigidBodyCombiner' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE2BD780>)>'
        'getInternalScene': None, # (!) real value is "<method 'getInternalScene' of 'panda3d.core.RigidBodyCombiner' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE2BD780>)>'
        'get_internal_scene': None, # (!) real value is "<method 'get_internal_scene' of 'panda3d.core.RigidBodyCombiner' objects>"
        'internal_scene': None, # (!) real value is "<attribute 'internal_scene' of 'panda3d.core.RigidBodyCombiner' objects>"
    }


