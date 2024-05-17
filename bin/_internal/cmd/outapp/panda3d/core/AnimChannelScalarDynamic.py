# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .AnimChannel_ACScalarSwitchType import AnimChannel_ACScalarSwitchType

class AnimChannelScalarDynamic(AnimChannel_ACScalarSwitchType):
    """
    /**
     * An animation channel that accepts a scalar each frame from some dynamic
     * input provided by code.
     *
     * This object operates in two modes: in explicit mode, the programmer should
     * call set_value() each frame to indicate the new value; in implicit mode,
     * the programmer should call set_value_node() to indicate the node whose X
     * component will be copied to the scalar each frame.
     */
    """
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

    def setValue(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_value(const AnimChannelScalarDynamic self, float value)
        
        /**
         * Explicitly sets the value.  This will remove any node assigned via
         * set_value_node().
         */
        """
        pass

    def setValueNode(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_value_node(const AnimChannelScalarDynamic self, PandaNode node)
        
        /**
         * Specifies a node whose transform will be queried each frame to implicitly
         * specify the transform of this joint.  This will override the values set by
         * set_value().
         */
        """
        pass

    def set_value(self, const_AnimChannelScalarDynamic_self, float_value): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_value(const AnimChannelScalarDynamic self, float value)
        
        /**
         * Explicitly sets the value.  This will remove any node assigned via
         * set_value_node().
         */
        """
        pass

    def set_value_node(self, const_AnimChannelScalarDynamic_self, PandaNode_node): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_value_node(const AnimChannelScalarDynamic self, PandaNode node)
        
        /**
         * Specifies a node whose transform will be queried each frame to implicitly
         * specify the transform of this joint.  This will override the values set by
         * set_value().
         */
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    value_node = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__doc__': '/**\n * An animation channel that accepts a scalar each frame from some dynamic\n * input provided by code.\n *\n * This object operates in two modes: in explicit mode, the programmer should\n * call set_value() each frame to indicate the new value; in implicit mode,\n * the programmer should call set_value_node() to indicate the node whose X\n * component will be copied to the scalar each frame.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.AnimChannelScalarDynamic' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE2C3C90>'
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE2C3C90>)>'
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE2C3C90>)>'
        'setValue': None, # (!) real value is "<method 'setValue' of 'panda3d.core.AnimChannelScalarDynamic' objects>"
        'setValueNode': None, # (!) real value is "<method 'setValueNode' of 'panda3d.core.AnimChannelScalarDynamic' objects>"
        'set_value': None, # (!) real value is "<method 'set_value' of 'panda3d.core.AnimChannelScalarDynamic' objects>"
        'set_value_node': None, # (!) real value is "<method 'set_value_node' of 'panda3d.core.AnimChannelScalarDynamic' objects>"
        'value': None, # (!) real value is "<attribute 'value' of 'panda3d.core.AnimChannelScalarDynamic' objects>"
        'value_node': None, # (!) real value is "<attribute 'value_node' of 'panda3d.core.AnimChannelScalarDynamic' objects>"
    }


