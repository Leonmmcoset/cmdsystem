# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .TypedReferenceCount import TypedReferenceCount

from .AnimInterface import AnimInterface

from .Namable import Namable

class AnimControl(TypedReferenceCount, AnimInterface, Namable):
    """
    /**
     * Controls the timing of a character animation.  An AnimControl object is
     * created for each character/bundle binding and manages the state of the
     * animation: whether started, stopped, or looping, and the current frame
     * number and play rate.
     */
    """
    def getAnim(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_anim(AnimControl self)
        
        /**
         * Returns the AnimBundle bound in with this AnimControl.
         */
        """
        pass

    def getAnimModel(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_anim_model(AnimControl self)
        
        /**
         * Retrieves the pointer set via set_anim_model().  See set_anim_model().
         */
        """
        pass

    def getBoundJoints(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_bound_joints(AnimControl self)
        
        /**
         * Returns the subset of joints controlled by this AnimControl.  Most of the
         * time, this will be BitArray::all_on(), for a normal full-body animation.
         * For a subset animation, however, this will be just a subset of those bits,
         * corresponding to the set of joints and sliders actually bound (as
         * enumerated by bind_hierarchy() in depth-first LIFO order).
         */
        """
        pass

    def getChannelIndex(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_channel_index(AnimControl self)
        
        /**
         * Returns the particular channel index associated with this AnimControl.
         * This channel index is the slot on which each AnimGroup is bound to its
         * associated PartGroup, for each joint in the animation.
         *
         * It will be true that
         * get_part()->find_child("n")->get_bound(get_channel_index()) ==
         * get_anim()->find_child("n"), for each joint "n".
         */
        """
        pass

    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getPart(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_part(AnimControl self)
        
        /**
         * Returns the PartBundle bound in with this AnimControl.
         */
        """
        pass

    def getPendingDoneEvent(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_pending_done_event(AnimControl self)
        
        /**
         * Returns the event name that will be thrown when the AnimControl is finished
         * binding asynchronously.
         */
        """
        pass

    def get_anim(self, AnimControl_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_anim(AnimControl self)
        
        /**
         * Returns the AnimBundle bound in with this AnimControl.
         */
        """
        pass

    def get_anim_model(self, AnimControl_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_anim_model(AnimControl self)
        
        /**
         * Retrieves the pointer set via set_anim_model().  See set_anim_model().
         */
        """
        pass

    def get_bound_joints(self, AnimControl_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_bound_joints(AnimControl self)
        
        /**
         * Returns the subset of joints controlled by this AnimControl.  Most of the
         * time, this will be BitArray::all_on(), for a normal full-body animation.
         * For a subset animation, however, this will be just a subset of those bits,
         * corresponding to the set of joints and sliders actually bound (as
         * enumerated by bind_hierarchy() in depth-first LIFO order).
         */
        """
        pass

    def get_channel_index(self, AnimControl_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_channel_index(AnimControl self)
        
        /**
         * Returns the particular channel index associated with this AnimControl.
         * This channel index is the slot on which each AnimGroup is bound to its
         * associated PartGroup, for each joint in the animation.
         *
         * It will be true that
         * get_part()->find_child("n")->get_bound(get_channel_index()) ==
         * get_anim()->find_child("n"), for each joint "n".
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_part(self, AnimControl_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_part(AnimControl self)
        
        /**
         * Returns the PartBundle bound in with this AnimControl.
         */
        """
        pass

    def get_pending_done_event(self, AnimControl_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_pending_done_event(AnimControl self)
        
        /**
         * Returns the event name that will be thrown when the AnimControl is finished
         * binding asynchronously.
         */
        """
        pass

    def hasAnim(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_anim(AnimControl self)
        
        /**
         * Returns true if the AnimControl was successfully loaded, or false if there
         * was a problem.  This may return false while is_pending() is true.
         */
        """
        pass

    def has_anim(self, AnimControl_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_anim(AnimControl self)
        
        /**
         * Returns true if the AnimControl was successfully loaded, or false if there
         * was a problem.  This may return false while is_pending() is true.
         */
        """
        pass

    def isPending(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_pending(AnimControl self)
        
        /**
         * Returns true if the AnimControl is being bound asynchronously, and has not
         * yet finished.  If this is true, the AnimControl's interface is still
         * available and will be perfectly useful (though get_anim() might return
         * NULL), but nothing visible will happen immediately.
         */
        """
        pass

    def is_pending(self, AnimControl_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_pending(AnimControl self)
        
        /**
         * Returns true if the AnimControl is being bound asynchronously, and has not
         * yet finished.  If this is true, the AnimControl's interface is still
         * available and will be perfectly useful (though get_anim() might return
         * NULL), but nothing visible will happen immediately.
         */
        """
        pass

    def output(self, AnimControl_self, ostream_out): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        output(AnimControl self, ostream out)
        
        /**
         *
         */
        """
        pass

    def setAnimModel(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_anim_model(const AnimControl self, PandaNode model)
        
        /**
         * Associates the indicated PandaNode with the AnimControl.  By convention,
         * this node represents the root node of the model file that corresponds to
         * this AnimControl's animation file, though nothing in this code makes this
         * assumption or indeed does anything with this node.
         *
         * The purpose of this is simply to allow the AnimControl to keep a reference
         * count on the ModelRoot node that generated it, so that the model will not
         * disappear from the model pool until it is no longer referenced.
         */
        """
        pass

    def setPendingDoneEvent(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_pending_done_event(const AnimControl self, str done_event)
        
        /**
         * Specifies an event name that will be thrown when the AnimControl is
         * finished binding asynchronously.  If the AnimControl has already finished
         * binding, the event will be thrown immediately.
         */
        """
        pass

    def set_anim_model(self, const_AnimControl_self, PandaNode_model): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_anim_model(const AnimControl self, PandaNode model)
        
        /**
         * Associates the indicated PandaNode with the AnimControl.  By convention,
         * this node represents the root node of the model file that corresponds to
         * this AnimControl's animation file, though nothing in this code makes this
         * assumption or indeed does anything with this node.
         *
         * The purpose of this is simply to allow the AnimControl to keep a reference
         * count on the ModelRoot node that generated it, so that the model will not
         * disappear from the model pool until it is no longer referenced.
         */
        """
        pass

    def set_pending_done_event(self, const_AnimControl_self, str_done_event): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_pending_done_event(const AnimControl self, str done_event)
        
        /**
         * Specifies an event name that will be thrown when the AnimControl is
         * finished binding asynchronously.  If the AnimControl has already finished
         * binding, the event will be thrown immediately.
         */
        """
        pass

    def upcastToAnimInterface(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        upcast_to_AnimInterface(const AnimControl self)
        
        upcast from AnimControl to AnimInterface
        """
        pass

    def upcastToNamable(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        upcast_to_Namable(const AnimControl self)
        
        upcast from AnimControl to Namable
        """
        pass

    def upcastToTypedReferenceCount(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        upcast_to_TypedReferenceCount(const AnimControl self)
        
        upcast from AnimControl to TypedReferenceCount
        """
        pass

    def upcast_to_AnimInterface(self, const_AnimControl_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        upcast_to_AnimInterface(const AnimControl self)
        
        upcast from AnimControl to AnimInterface
        """
        pass

    def upcast_to_Namable(self, const_AnimControl_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        upcast_to_Namable(const AnimControl self)
        
        upcast from AnimControl to Namable
        """
        pass

    def upcast_to_TypedReferenceCount(self, const_AnimControl_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        upcast_to_TypedReferenceCount(const AnimControl self)
        
        upcast from AnimControl to TypedReferenceCount
        """
        pass

    def waitPending(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        wait_pending(const AnimControl self)
        
        /**
         * Blocks the current thread until the AnimControl has finished loading and is
         * fully bound.
         */
        """
        pass

    def wait_pending(self, const_AnimControl_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        wait_pending(const AnimControl self)
        
        /**
         * Blocks the current thread until the AnimControl has finished loading and is
         * fully bound.
         */
        """
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

    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__doc__': '/**\n * Controls the timing of a character animation.  An AnimControl object is\n * created for each character/bundle binding and manages the state of the\n * animation: whether started, stopped, or looping, and the current frame\n * number and play rate.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.AnimControl' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE2C31B0>'
        '__repr__': None, # (!) real value is "<slot wrapper '__repr__' of 'panda3d.core.AnimControl' objects>"
        '__str__': None, # (!) real value is "<slot wrapper '__str__' of 'panda3d.core.AnimControl' objects>"
        'getAnim': None, # (!) real value is "<method 'getAnim' of 'panda3d.core.AnimControl' objects>"
        'getAnimModel': None, # (!) real value is "<method 'getAnimModel' of 'panda3d.core.AnimControl' objects>"
        'getBoundJoints': None, # (!) real value is "<method 'getBoundJoints' of 'panda3d.core.AnimControl' objects>"
        'getChannelIndex': None, # (!) real value is "<method 'getChannelIndex' of 'panda3d.core.AnimControl' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE2C31B0>)>'
        'getPart': None, # (!) real value is "<method 'getPart' of 'panda3d.core.AnimControl' objects>"
        'getPendingDoneEvent': None, # (!) real value is "<method 'getPendingDoneEvent' of 'panda3d.core.AnimControl' objects>"
        'get_anim': None, # (!) real value is "<method 'get_anim' of 'panda3d.core.AnimControl' objects>"
        'get_anim_model': None, # (!) real value is "<method 'get_anim_model' of 'panda3d.core.AnimControl' objects>"
        'get_bound_joints': None, # (!) real value is "<method 'get_bound_joints' of 'panda3d.core.AnimControl' objects>"
        'get_channel_index': None, # (!) real value is "<method 'get_channel_index' of 'panda3d.core.AnimControl' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE2C31B0>)>'
        'get_part': None, # (!) real value is "<method 'get_part' of 'panda3d.core.AnimControl' objects>"
        'get_pending_done_event': None, # (!) real value is "<method 'get_pending_done_event' of 'panda3d.core.AnimControl' objects>"
        'hasAnim': None, # (!) real value is "<method 'hasAnim' of 'panda3d.core.AnimControl' objects>"
        'has_anim': None, # (!) real value is "<method 'has_anim' of 'panda3d.core.AnimControl' objects>"
        'isPending': None, # (!) real value is "<method 'isPending' of 'panda3d.core.AnimControl' objects>"
        'is_pending': None, # (!) real value is "<method 'is_pending' of 'panda3d.core.AnimControl' objects>"
        'output': None, # (!) real value is "<method 'output' of 'panda3d.core.AnimControl' objects>"
        'setAnimModel': None, # (!) real value is "<method 'setAnimModel' of 'panda3d.core.AnimControl' objects>"
        'setPendingDoneEvent': None, # (!) real value is "<method 'setPendingDoneEvent' of 'panda3d.core.AnimControl' objects>"
        'set_anim_model': None, # (!) real value is "<method 'set_anim_model' of 'panda3d.core.AnimControl' objects>"
        'set_pending_done_event': None, # (!) real value is "<method 'set_pending_done_event' of 'panda3d.core.AnimControl' objects>"
        'upcastToAnimInterface': None, # (!) real value is "<method 'upcastToAnimInterface' of 'panda3d.core.AnimControl' objects>"
        'upcastToNamable': None, # (!) real value is "<method 'upcastToNamable' of 'panda3d.core.AnimControl' objects>"
        'upcastToTypedReferenceCount': None, # (!) real value is "<method 'upcastToTypedReferenceCount' of 'panda3d.core.AnimControl' objects>"
        'upcast_to_AnimInterface': None, # (!) real value is "<method 'upcast_to_AnimInterface' of 'panda3d.core.AnimControl' objects>"
        'upcast_to_Namable': None, # (!) real value is "<method 'upcast_to_Namable' of 'panda3d.core.AnimControl' objects>"
        'upcast_to_TypedReferenceCount': None, # (!) real value is "<method 'upcast_to_TypedReferenceCount' of 'panda3d.core.AnimControl' objects>"
        'waitPending': None, # (!) real value is "<method 'waitPending' of 'panda3d.core.AnimControl' objects>"
        'wait_pending': None, # (!) real value is "<method 'wait_pending' of 'panda3d.core.AnimControl' objects>"
    }


