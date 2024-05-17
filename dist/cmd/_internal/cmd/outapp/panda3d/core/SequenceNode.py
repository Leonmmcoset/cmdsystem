# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .SelectiveChildNode import SelectiveChildNode

from .AnimInterface import AnimInterface

class SequenceNode(SelectiveChildNode, AnimInterface):
    """
    /**
     * A node that automatically cycles through rendering each one of its children
     * according to its frame rate.
     */
    """
    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getNumFrames(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_frames(SequenceNode self)
        
        /**
         * Returns the number of frames in the animation.  This is a property of the
         * animation and may not be directly adjusted by the user (although it may
         * change without warning with certain kinds of animations, since this is a
         * virtual method that may be overridden).
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_num_frames(self, SequenceNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_frames(SequenceNode self)
        
        /**
         * Returns the number of frames in the animation.  This is a property of the
         * animation and may not be directly adjusted by the user (although it may
         * change without warning with certain kinds of animations, since this is a
         * virtual method that may be overridden).
         */
        """
        pass

    def setFrameRate(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_frame_rate(const SequenceNode self, double frame_rate)
        
        /**
         * Changes the advertised frame rate of the SequenceNode.  This can be used in
         * conjunction with get_play_rate() to change the effective frame rate of the
         * node.
         */
        """
        pass

    def set_frame_rate(self, const_SequenceNode_self, double_frame_rate): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_frame_rate(const SequenceNode self, double frame_rate)
        
        /**
         * Changes the advertised frame rate of the SequenceNode.  This can be used in
         * conjunction with get_play_rate() to change the effective frame rate of the
         * node.
         */
        """
        pass

    def upcastToAnimInterface(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        upcast_to_AnimInterface(const SequenceNode self)
        
        upcast from SequenceNode to AnimInterface
        """
        pass

    def upcastToSelectiveChildNode(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        upcast_to_SelectiveChildNode(const SequenceNode self)
        
        upcast from SequenceNode to SelectiveChildNode
        """
        pass

    def upcast_to_AnimInterface(self, const_SequenceNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        upcast_to_AnimInterface(const SequenceNode self)
        
        upcast from SequenceNode to AnimInterface
        """
        pass

    def upcast_to_SelectiveChildNode(self, const_SequenceNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        upcast_to_SelectiveChildNode(const SequenceNode self)
        
        upcast from SequenceNode to SelectiveChildNode
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    frame_rate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__doc__': '/**\n * A node that automatically cycles through rendering each one of its children\n * according to its frame rate.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.SequenceNode' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE2883B0>'
        'frame_rate': None, # (!) real value is "<attribute 'frame_rate' of 'panda3d.core.SequenceNode' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE2883B0>)>'
        'getNumFrames': None, # (!) real value is "<method 'getNumFrames' of 'panda3d.core.SequenceNode' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE2883B0>)>'
        'get_num_frames': None, # (!) real value is "<method 'get_num_frames' of 'panda3d.core.SequenceNode' objects>"
        'setFrameRate': None, # (!) real value is "<method 'setFrameRate' of 'panda3d.core.SequenceNode' objects>"
        'set_frame_rate': None, # (!) real value is "<method 'set_frame_rate' of 'panda3d.core.SequenceNode' objects>"
        'upcastToAnimInterface': None, # (!) real value is "<method 'upcastToAnimInterface' of 'panda3d.core.SequenceNode' objects>"
        'upcastToSelectiveChildNode': None, # (!) real value is "<method 'upcastToSelectiveChildNode' of 'panda3d.core.SequenceNode' objects>"
        'upcast_to_AnimInterface': None, # (!) real value is "<method 'upcast_to_AnimInterface' of 'panda3d.core.SequenceNode' objects>"
        'upcast_to_SelectiveChildNode': None, # (!) real value is "<method 'upcast_to_SelectiveChildNode' of 'panda3d.core.SequenceNode' objects>"
    }


