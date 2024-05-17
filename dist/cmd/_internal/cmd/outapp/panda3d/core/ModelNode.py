# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .PandaNode import PandaNode

class ModelNode(PandaNode):
    """
    /**
     * This node is placed at key points within the scene graph to indicate the
     * roots of "models": subtrees that are conceptually to be treated as a single
     * unit, like a car or a room, for instance.  It doesn't affect rendering or
     * any other operations; it's primarily useful as a high-level model
     * indication.
     *
     * ModelNodes are created in response to a <Model> { 1 } flag within an egg
     * file.
     */
    """
    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getPreserveAttributes(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_preserve_attributes(ModelNode self)
        
        /**
         * Returns the current setting of the preserve_attributes flag.  See
         * set_preserve_attributes().
         */
        """
        pass

    def getPreserveTransform(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_preserve_transform(ModelNode self)
        
        /**
         * Returns the current setting of the preserve_transform flag.  See
         * set_preserve_transform().
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_preserve_attributes(self, ModelNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_preserve_attributes(ModelNode self)
        
        /**
         * Returns the current setting of the preserve_attributes flag.  See
         * set_preserve_attributes().
         */
        """
        pass

    def get_preserve_transform(self, ModelNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_preserve_transform(ModelNode self)
        
        /**
         * Returns the current setting of the preserve_transform flag.  See
         * set_preserve_transform().
         */
        """
        pass

    def setPreserveAttributes(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_preserve_attributes(const ModelNode self, int attrib_mask)
        
        /**
         * Sets the preserve_attributes flag.  This restricts the ability of a flatten
         * operation to affect the render attributes stored on this node.
         *
         * The value should be the union of bits from SceneGraphReducer::AttribTypes
         * that represent the attributes that should *not* be changed.
         */
        """
        pass

    def setPreserveTransform(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_preserve_transform(const ModelNode self, int preserve_transform)
        
        /**
         * Sets the preserve_transform flag.  This restricts the ability of a flatten
         * operation to affect the transform stored on this node, and/or the node
         * itself.  In the order from weakest to strongest restrictions, the possible
         * flags are:
         *
         * PT_drop_node - This node should be removed at the next flatten call.
         *
         * PT_none - The transform may be adjusted at will.  The node itself will not
         * be removed.  This is the default.
         *
         * PT_net - Preserve the net transform from the root, but it's acceptable to
         * modify the local transform stored on this particular node if necessary, so
         * long as the net transform is not changed.  This eliminates the need to drop
         * an extra transform on the node above.
         *
         * PT_local - The local (and net) transform should not be changed in any way.
         * If necessary, an extra transform will be left on the node above to
         * guarantee this.  This is a stronger restriction than PT_net.
         *
         * PT_no_touch - The local transform will not be changed, the node will not be
         * removed, and furthermore any flatten operation will not continue below this
         * node--this node and all descendents are protected from the effects of
         * flatten.
         */
        """
        pass

    def setTransformLimit(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_transform_limit(const ModelNode self, float limit)
        """
        pass

    def set_preserve_attributes(self, const_ModelNode_self, int_attrib_mask): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_preserve_attributes(const ModelNode self, int attrib_mask)
        
        /**
         * Sets the preserve_attributes flag.  This restricts the ability of a flatten
         * operation to affect the render attributes stored on this node.
         *
         * The value should be the union of bits from SceneGraphReducer::AttribTypes
         * that represent the attributes that should *not* be changed.
         */
        """
        pass

    def set_preserve_transform(self, const_ModelNode_self, int_preserve_transform): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_preserve_transform(const ModelNode self, int preserve_transform)
        
        /**
         * Sets the preserve_transform flag.  This restricts the ability of a flatten
         * operation to affect the transform stored on this node, and/or the node
         * itself.  In the order from weakest to strongest restrictions, the possible
         * flags are:
         *
         * PT_drop_node - This node should be removed at the next flatten call.
         *
         * PT_none - The transform may be adjusted at will.  The node itself will not
         * be removed.  This is the default.
         *
         * PT_net - Preserve the net transform from the root, but it's acceptable to
         * modify the local transform stored on this particular node if necessary, so
         * long as the net transform is not changed.  This eliminates the need to drop
         * an extra transform on the node above.
         *
         * PT_local - The local (and net) transform should not be changed in any way.
         * If necessary, an extra transform will be left on the node above to
         * guarantee this.  This is a stronger restriction than PT_net.
         *
         * PT_no_touch - The local transform will not be changed, the node will not be
         * removed, and furthermore any flatten operation will not continue below this
         * node--this node and all descendents are protected from the effects of
         * flatten.
         */
        """
        pass

    def set_transform_limit(self, const_ModelNode_self, float_limit): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_transform_limit(const ModelNode self, float limit)
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
        'PTDropNode': 3,
        'PTLocal': 1,
        'PTNet': 2,
        'PTNoTouch': 4,
        'PTNone': 0,
        'PT_drop_node': 3,
        'PT_local': 1,
        'PT_net': 2,
        'PT_no_touch': 4,
        'PT_none': 0,
        '__doc__': '/**\n * This node is placed at key points within the scene graph to indicate the\n * roots of "models": subtrees that are conceptually to be treated as a single\n * unit, like a car or a room, for instance.  It doesn\'t affect rendering or\n * any other operations; it\'s primarily useful as a high-level model\n * indication.\n *\n * ModelNodes are created in response to a <Model> { 1 } flag within an egg\n * file.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.ModelNode' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE298DD0>'
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE298DD0>)>'
        'getPreserveAttributes': None, # (!) real value is "<method 'getPreserveAttributes' of 'panda3d.core.ModelNode' objects>"
        'getPreserveTransform': None, # (!) real value is "<method 'getPreserveTransform' of 'panda3d.core.ModelNode' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE298DD0>)>'
        'get_preserve_attributes': None, # (!) real value is "<method 'get_preserve_attributes' of 'panda3d.core.ModelNode' objects>"
        'get_preserve_transform': None, # (!) real value is "<method 'get_preserve_transform' of 'panda3d.core.ModelNode' objects>"
        'setPreserveAttributes': None, # (!) real value is "<method 'setPreserveAttributes' of 'panda3d.core.ModelNode' objects>"
        'setPreserveTransform': None, # (!) real value is "<method 'setPreserveTransform' of 'panda3d.core.ModelNode' objects>"
        'setTransformLimit': None, # (!) real value is "<method 'setTransformLimit' of 'panda3d.core.ModelNode' objects>"
        'set_preserve_attributes': None, # (!) real value is "<method 'set_preserve_attributes' of 'panda3d.core.ModelNode' objects>"
        'set_preserve_transform': None, # (!) real value is "<method 'set_preserve_transform' of 'panda3d.core.ModelNode' objects>"
        'set_transform_limit': None, # (!) real value is "<method 'set_transform_limit' of 'panda3d.core.ModelNode' objects>"
    }
    PTDropNode = 3
    PTLocal = 1
    PTNet = 2
    PTNone = 0
    PTNoTouch = 4
    PT_drop_node = 3
    PT_local = 1
    PT_net = 2
    PT_none = 0
    PT_no_touch = 4


