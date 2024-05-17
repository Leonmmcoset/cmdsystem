# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


class AnimControlCollection(__dtoolconfig.DTOOL_SUPER_BASE):
    """
    /**
     * This is a named collection of AnimControl pointers.  An AnimControl may be
     * added to the collection by name.  While an AnimControl is associated, its
     * reference count is maintained; associating a new AnimControl with the same
     * name will decrement the previous control's reference count (and possibly
     * delete it, unbinding its animation).
     */
    """
    def clearAnims(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_anims(const AnimControlCollection self)
        
        /**
         * Disassociates all anims from this collection.
         */
        """
        pass

    def clear_anims(self, const_AnimControlCollection_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_anims(const AnimControlCollection self)
        
        /**
         * Disassociates all anims from this collection.
         */
        """
        pass

    def findAnim(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        find_anim(AnimControlCollection self, str name)
        
        /**
         * Returns the AnimControl associated with the given name, or NULL if no such
         * control has been associated.
         */
        """
        pass

    def find_anim(self, AnimControlCollection_self, str_name): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        find_anim(AnimControlCollection self, str name)
        
        /**
         * Returns the AnimControl associated with the given name, or NULL if no such
         * control has been associated.
         */
        """
        pass

    def getAnim(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_anim(AnimControlCollection self, int n)
        
        /**
         * Returns the nth AnimControl associated with this collection.
         */
        """
        pass

    def getAnimName(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_anim_name(AnimControlCollection self, int n)
        
        /**
         * Returns the name of the nth AnimControl associated with this collection.
         */
        """
        pass

    def getAnimNames(self, *args, **kwargs): # real signature unknown
        pass

    def getAnims(self, *args, **kwargs): # real signature unknown
        pass

    def getFrame(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_frame(AnimControlCollection self)
        get_frame(AnimControlCollection self, str anim_name)
        
        /**
         * Returns the current frame in the named animation, or 0 if the animation is
         * not found.
         */
        
        /**
         * Returns the current frame in the last-started animation.
         */
        """
        pass

    def getNumAnims(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_anims(AnimControlCollection self)
        
        /**
         * Returns the number of AnimControls associated with this collection.
         */
        """
        pass

    def getNumFrames(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_frames(AnimControlCollection self)
        get_num_frames(AnimControlCollection self, str anim_name)
        
        /**
         * Returns the total number of frames in the named animation, or 0 if the
         * animation is not found.
         */
        
        /**
         * Returns the total number of frames in the last-started animation.
         */
        """
        pass

    def get_anim(self, AnimControlCollection_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_anim(AnimControlCollection self, int n)
        
        /**
         * Returns the nth AnimControl associated with this collection.
         */
        """
        pass

    def get_anims(self, *args, **kwargs): # real signature unknown
        pass

    def get_anim_name(self, AnimControlCollection_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_anim_name(AnimControlCollection self, int n)
        
        /**
         * Returns the name of the nth AnimControl associated with this collection.
         */
        """
        pass

    def get_anim_names(self, *args, **kwargs): # real signature unknown
        pass

    def get_frame(self, AnimControlCollection_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_frame(AnimControlCollection self)
        get_frame(AnimControlCollection self, str anim_name)
        
        /**
         * Returns the current frame in the named animation, or 0 if the animation is
         * not found.
         */
        
        /**
         * Returns the current frame in the last-started animation.
         */
        """
        pass

    def get_num_anims(self, AnimControlCollection_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_anims(AnimControlCollection self)
        
        /**
         * Returns the number of AnimControls associated with this collection.
         */
        """
        pass

    def get_num_frames(self, AnimControlCollection_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_frames(AnimControlCollection self)
        get_num_frames(AnimControlCollection self, str anim_name)
        
        /**
         * Returns the total number of frames in the named animation, or 0 if the
         * animation is not found.
         */
        
        /**
         * Returns the total number of frames in the last-started animation.
         */
        """
        pass

    def isPlaying(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_playing(AnimControlCollection self)
        is_playing(AnimControlCollection self, str anim_name)
        
        /**
         * Returns true if the named animation is currently playing, false otherwise.
         */
        
        /**
         * Returns true if the last-started animation is currently playing, false
         * otherwise.
         */
        """
        pass

    def is_playing(self, AnimControlCollection_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_playing(AnimControlCollection self)
        is_playing(AnimControlCollection self, str anim_name)
        
        /**
         * Returns true if the named animation is currently playing, false otherwise.
         */
        
        /**
         * Returns true if the last-started animation is currently playing, false
         * otherwise.
         */
        """
        pass

    def loop(self, const_AnimControlCollection_self, str_anim_name, bool_restart): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        loop(const AnimControlCollection self, str anim_name, bool restart)
        loop(const AnimControlCollection self, str anim_name, bool restart, double from, double to)
        
        /**
         * Starts the named animation looping.
         */
        
        /**
         * Starts the named animation looping.
         */
        """
        pass

    def loopAll(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        loop_all(const AnimControlCollection self, bool restart)
        loop_all(const AnimControlCollection self, bool restart, double from, double to)
        
        /**
         * Starts all animations looping.
         */
        
        /**
         * Starts all animations looping.
         */
        """
        pass

    def loop_all(self, const_AnimControlCollection_self, bool_restart): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        loop_all(const AnimControlCollection self, bool restart)
        loop_all(const AnimControlCollection self, bool restart, double from, double to)
        
        /**
         * Starts all animations looping.
         */
        
        /**
         * Starts all animations looping.
         */
        """
        pass

    def output(self, AnimControlCollection_self, ostream_out): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        output(AnimControlCollection self, ostream out)
        
        /**
         *
         */
        """
        pass

    def play(self, const_AnimControlCollection_self, str_anim_name): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        play(const AnimControlCollection self, str anim_name)
        play(const AnimControlCollection self, str anim_name, double from, double to)
        
        /**
         * Starts the named animation playing.
         */
        
        /**
         * Starts the named animation playing.
         */
        """
        pass

    def playAll(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        play_all(const AnimControlCollection self)
        play_all(const AnimControlCollection self, double from, double to)
        
        // These functions operate on all anims at once.
        
        /**
         * Starts all animations playing.
         */
        
        /**
         * Starts all animations playing.
         */
        """
        pass

    def play_all(self, const_AnimControlCollection_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        play_all(const AnimControlCollection self)
        play_all(const AnimControlCollection self, double from, double to)
        
        // These functions operate on all anims at once.
        
        /**
         * Starts all animations playing.
         */
        
        /**
         * Starts all animations playing.
         */
        """
        pass

    def pose(self, const_AnimControlCollection_self, str_anim_name, double_frame): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        pose(const AnimControlCollection self, str anim_name, double frame)
        
        /**
         * Sets to a particular frame in the named animation.
         */
        """
        pass

    def poseAll(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        pose_all(const AnimControlCollection self, double frame)
        
        /**
         * Sets all animations to the indicated frame.
         */
        """
        pass

    def pose_all(self, const_AnimControlCollection_self, double_frame): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        pose_all(const AnimControlCollection self, double frame)
        
        /**
         * Sets all animations to the indicated frame.
         */
        """
        pass

    def stop(self, const_AnimControlCollection_self, str_anim_name): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        stop(const AnimControlCollection self, str anim_name)
        
        /**
         * Stops the named animation.
         */
        """
        pass

    def stopAll(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        stop_all(const AnimControlCollection self)
        
        /**
         * Stops all currently playing animations.  Returns true if any animations
         * were stopped, false if none were playing.
         */
        """
        pass

    def stop_all(self, const_AnimControlCollection_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        stop_all(const AnimControlCollection self)
        
        /**
         * Stops all currently playing animations.  Returns true if any animations
         * were stopped, false if none were playing.
         */
        """
        pass

    def storeAnim(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        store_anim(const AnimControlCollection self, AnimControl control, str name)
        
        /**
         * Associates the given AnimControl with this collection under the given name.
         * The AnimControl will remain associated until a new AnimControl is
         * associated with the same name later, or until unbind_anim() is called with
         * this name.
         */
        """
        pass

    def store_anim(self, const_AnimControlCollection_self, AnimControl_control, str_name): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        store_anim(const AnimControlCollection self, AnimControl control, str name)
        
        /**
         * Associates the given AnimControl with this collection under the given name.
         * The AnimControl will remain associated until a new AnimControl is
         * associated with the same name later, or until unbind_anim() is called with
         * this name.
         */
        """
        pass

    def unbindAnim(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        unbind_anim(const AnimControlCollection self, str name)
        
        /**
         * Removes the AnimControl associated with the given name, if any.  Returns
         * true if an AnimControl was removed, false if there was no AnimControl with
         * the indicated name.
         */
        """
        pass

    def unbind_anim(self, const_AnimControlCollection_self, str_name): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        unbind_anim(const AnimControlCollection self, str name)
        
        /**
         * Removes the AnimControl associated with the given name, if any.  Returns
         * true if an AnimControl was removed, false if there was no AnimControl with
         * the indicated name.
         */
        """
        pass

    def whichAnimPlaying(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        which_anim_playing(AnimControlCollection self)
        
        /**
         * Returns the name of the bound AnimControl currently playing, if any.  If
         * more than one AnimControl is currently playing, returns all of the names
         * separated by spaces.
         */
        """
        pass

    def which_anim_playing(self, AnimControlCollection_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        which_anim_playing(AnimControlCollection self)
        
        /**
         * Returns the name of the bound AnimControl currently playing, if any.  If
         * more than one AnimControl is currently playing, returns all of the names
         * separated by spaces.
         */
        """
        pass

    def write(self, AnimControlCollection_self, ostream_out): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        write(AnimControlCollection self, ostream out)
        
        /**
         *
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

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.core.AnimControlCollection' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.core.AnimControlCollection' objects>"
        '__doc__': "/**\n * This is a named collection of AnimControl pointers.  An AnimControl may be\n * added to the collection by name.  While an AnimControl is associated, its\n * reference count is maintained; associating a new AnimControl with the same\n * name will decrement the previous control's reference count (and possibly\n * delete it, unbinding its animation).\n */",
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.AnimControlCollection' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE2C4030>'
        '__repr__': None, # (!) real value is "<slot wrapper '__repr__' of 'panda3d.core.AnimControlCollection' objects>"
        '__str__': None, # (!) real value is "<slot wrapper '__str__' of 'panda3d.core.AnimControlCollection' objects>"
        'clearAnims': None, # (!) real value is "<method 'clearAnims' of 'panda3d.core.AnimControlCollection' objects>"
        'clear_anims': None, # (!) real value is "<method 'clear_anims' of 'panda3d.core.AnimControlCollection' objects>"
        'findAnim': None, # (!) real value is "<method 'findAnim' of 'panda3d.core.AnimControlCollection' objects>"
        'find_anim': None, # (!) real value is "<method 'find_anim' of 'panda3d.core.AnimControlCollection' objects>"
        'getAnim': None, # (!) real value is "<method 'getAnim' of 'panda3d.core.AnimControlCollection' objects>"
        'getAnimName': None, # (!) real value is "<method 'getAnimName' of 'panda3d.core.AnimControlCollection' objects>"
        'getAnimNames': None, # (!) real value is "<method 'getAnimNames' of 'panda3d.core.AnimControlCollection' objects>"
        'getAnims': None, # (!) real value is "<method 'getAnims' of 'panda3d.core.AnimControlCollection' objects>"
        'getFrame': None, # (!) real value is "<method 'getFrame' of 'panda3d.core.AnimControlCollection' objects>"
        'getNumAnims': None, # (!) real value is "<method 'getNumAnims' of 'panda3d.core.AnimControlCollection' objects>"
        'getNumFrames': None, # (!) real value is "<method 'getNumFrames' of 'panda3d.core.AnimControlCollection' objects>"
        'get_anim': None, # (!) real value is "<method 'get_anim' of 'panda3d.core.AnimControlCollection' objects>"
        'get_anim_name': None, # (!) real value is "<method 'get_anim_name' of 'panda3d.core.AnimControlCollection' objects>"
        'get_anim_names': None, # (!) real value is "<method 'get_anim_names' of 'panda3d.core.AnimControlCollection' objects>"
        'get_anims': None, # (!) real value is "<method 'get_anims' of 'panda3d.core.AnimControlCollection' objects>"
        'get_frame': None, # (!) real value is "<method 'get_frame' of 'panda3d.core.AnimControlCollection' objects>"
        'get_num_anims': None, # (!) real value is "<method 'get_num_anims' of 'panda3d.core.AnimControlCollection' objects>"
        'get_num_frames': None, # (!) real value is "<method 'get_num_frames' of 'panda3d.core.AnimControlCollection' objects>"
        'isPlaying': None, # (!) real value is "<method 'isPlaying' of 'panda3d.core.AnimControlCollection' objects>"
        'is_playing': None, # (!) real value is "<method 'is_playing' of 'panda3d.core.AnimControlCollection' objects>"
        'loop': None, # (!) real value is "<method 'loop' of 'panda3d.core.AnimControlCollection' objects>"
        'loopAll': None, # (!) real value is "<method 'loopAll' of 'panda3d.core.AnimControlCollection' objects>"
        'loop_all': None, # (!) real value is "<method 'loop_all' of 'panda3d.core.AnimControlCollection' objects>"
        'output': None, # (!) real value is "<method 'output' of 'panda3d.core.AnimControlCollection' objects>"
        'play': None, # (!) real value is "<method 'play' of 'panda3d.core.AnimControlCollection' objects>"
        'playAll': None, # (!) real value is "<method 'playAll' of 'panda3d.core.AnimControlCollection' objects>"
        'play_all': None, # (!) real value is "<method 'play_all' of 'panda3d.core.AnimControlCollection' objects>"
        'pose': None, # (!) real value is "<method 'pose' of 'panda3d.core.AnimControlCollection' objects>"
        'poseAll': None, # (!) real value is "<method 'poseAll' of 'panda3d.core.AnimControlCollection' objects>"
        'pose_all': None, # (!) real value is "<method 'pose_all' of 'panda3d.core.AnimControlCollection' objects>"
        'stop': None, # (!) real value is "<method 'stop' of 'panda3d.core.AnimControlCollection' objects>"
        'stopAll': None, # (!) real value is "<method 'stopAll' of 'panda3d.core.AnimControlCollection' objects>"
        'stop_all': None, # (!) real value is "<method 'stop_all' of 'panda3d.core.AnimControlCollection' objects>"
        'storeAnim': None, # (!) real value is "<method 'storeAnim' of 'panda3d.core.AnimControlCollection' objects>"
        'store_anim': None, # (!) real value is "<method 'store_anim' of 'panda3d.core.AnimControlCollection' objects>"
        'unbindAnim': None, # (!) real value is "<method 'unbindAnim' of 'panda3d.core.AnimControlCollection' objects>"
        'unbind_anim': None, # (!) real value is "<method 'unbind_anim' of 'panda3d.core.AnimControlCollection' objects>"
        'whichAnimPlaying': None, # (!) real value is "<method 'whichAnimPlaying' of 'panda3d.core.AnimControlCollection' objects>"
        'which_anim_playing': None, # (!) real value is "<method 'which_anim_playing' of 'panda3d.core.AnimControlCollection' objects>"
        'write': None, # (!) real value is "<method 'write' of 'panda3d.core.AnimControlCollection' objects>"
    }


