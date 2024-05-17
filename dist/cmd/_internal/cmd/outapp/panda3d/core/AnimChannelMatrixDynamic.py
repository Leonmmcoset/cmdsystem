# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .AnimChannel_ACMatrixSwitchType import AnimChannel_ACMatrixSwitchType

class AnimChannelMatrixDynamic(AnimChannel_ACMatrixSwitchType):
    """
    /**
     * An animation channel that accepts a matrix each frame from some dynamic
     * input provided by code.
     *
     * This object operates in two modes: in explicit mode, the programmer should
     * call set_value() each frame to indicate the new value; in implicit mode,
     * the programmer should call set_value_node() to indicate the node whose
     * transform will be copied to the joint each frame.
     */
    """
    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getValueNode(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_value_node(AnimChannelMatrixDynamic self)
        
        /**
         * Returns the node that was set via set_value_node(), if any.
         */
        """
        pass

    def getValueTransform(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_value_transform(AnimChannelMatrixDynamic self)
        
        /**
         * Returns the explicit TransformState value that was set via set_value(), if
         * any.
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_value_node(self, AnimChannelMatrixDynamic_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_value_node(AnimChannelMatrixDynamic self)
        
        /**
         * Returns the node that was set via set_value_node(), if any.
         */
        """
        pass

    def get_value_transform(self, AnimChannelMatrixDynamic_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_value_transform(AnimChannelMatrixDynamic self)
        
        /**
         * Returns the explicit TransformState value that was set via set_value(), if
         * any.
         */
        """
        pass

    def setValue(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_value(const AnimChannelMatrixDynamic self, const TransformState value)
        
        /**
         * Explicitly sets the matrix value.
         */
        
        /**
         * Explicitly sets the matrix value, using the indicated TransformState object
         * as a convenience.
         */
        """
        pass

    def setValueNode(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_value_node(const AnimChannelMatrixDynamic self, PandaNode node)
        
        /**
         * Specifies a node whose transform will be queried each frame to implicitly
         * specify the transform of this joint.
         */
        """
        pass

    def set_value(self, const_AnimChannelMatrixDynamic_self, const_TransformState_value): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_value(const AnimChannelMatrixDynamic self, const TransformState value)
        
        /**
         * Explicitly sets the matrix value.
         */
        
        /**
         * Explicitly sets the matrix value, using the indicated TransformState object
         * as a convenience.
         */
        """
        pass

    def set_value_node(self, const_AnimChannelMatrixDynamic_self, PandaNode_node): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_value_node(const AnimChannelMatrixDynamic self, PandaNode node)
        
        /**
         * Specifies a node whose transform will be queried each frame to implicitly
         * specify the transform of this joint.
         */
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    value_node = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__doc__': '/**\n * An animation channel that accepts a matrix each frame from some dynamic\n * input provided by code.\n *\n * This object operates in two modes: in explicit mode, the programmer should\n * call set_value() each frame to indicate the new value; in implicit mode,\n * the programmer should call set_value_node() to indicate the node whose\n * transform will be copied to the joint each frame.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.AnimChannelMatrixDynamic' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE2C38F0>'
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE2C38F0>)>'
        'getValueNode': None, # (!) real value is "<method 'getValueNode' of 'panda3d.core.AnimChannelMatrixDynamic' objects>"
        'getValueTransform': None, # (!) real value is "<method 'getValueTransform' of 'panda3d.core.AnimChannelMatrixDynamic' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE2C38F0>)>'
        'get_value_node': None, # (!) real value is "<method 'get_value_node' of 'panda3d.core.AnimChannelMatrixDynamic' objects>"
        'get_value_transform': None, # (!) real value is "<method 'get_value_transform' of 'panda3d.core.AnimChannelMatrixDynamic' objects>"
        'setValue': None, # (!) real value is "<method 'setValue' of 'panda3d.core.AnimChannelMatrixDynamic' objects>"
        'setValueNode': None, # (!) real value is "<method 'setValueNode' of 'panda3d.core.AnimChannelMatrixDynamic' objects>"
        'set_value': None, # (!) real value is "<method 'set_value' of 'panda3d.core.AnimChannelMatrixDynamic' objects>"
        'set_value_node': None, # (!) real value is "<method 'set_value_node' of 'panda3d.core.AnimChannelMatrixDynamic' objects>"
        'value_node': None, # (!) real value is "<attribute 'value_node' of 'panda3d.core.AnimChannelMatrixDynamic' objects>"
    }


