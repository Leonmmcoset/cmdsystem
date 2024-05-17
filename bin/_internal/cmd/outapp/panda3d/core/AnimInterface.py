# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


class AnimInterface(__dtoolconfig.DTOOL_SUPER_BASE):
    """
    /**
     * This is the fundamental interface for things that have a play/loop/stop
     * type interface for frame-based animation, such as animated characters.
     * This is the base class for AnimControl and other, similar classes.
     */
    """
    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getFrac(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_frac(AnimInterface self)
        
        /**
         * Returns the fractional part of the current frame.  Normally, this is in the
         * range 0.0 <= f < 1.0, but in the one special case of an animation playing
         * to its end frame and stopping, it might exactly equal 1.0.
         *
         * It will always be true that get_full_frame() + get_frac() ==
         * get_full_fframe().
         */
        """
        pass

    def getFrame(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_frame(AnimInterface self)
        
        /**
         * Returns the current integer frame number.  This number will be in the range
         * 0 <= f < get_num_frames().
         */
        """
        pass

    def getFrameRate(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_frame_rate(AnimInterface self)
        
        /**
         * Returns the native frame rate of the animation.  This is the number of
         * frames per second that will elapse when the play_rate is set to 1.0.  It is
         * a fixed property of the animation and may not be adjusted by the user.
         */
        """
        pass

    def getFullFframe(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_full_fframe(AnimInterface self)
        
        /**
         * Returns the current floating-point frame number.
         *
         * Unlike the value returned by get_frame(), this frame number may extend
         * beyond the range of get_num_frames() if the frame range passed to play(),
         * loop(), etc.  did.
         *
         * Unlike the value returned by get_full_frame(), this return value may equal
         * (to_frame + 1.0), when the animation has played to its natural end.
         * However, in this case the return value of get_full_frame() will be
         * to_frame, not (to_frame + 1).
         */
        """
        pass

    def getFullFrame(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_full_frame(AnimInterface self)
        
        /**
         * Returns the current integer frame number.
         *
         * Unlike the value returned by get_frame(), this frame number may extend
         * beyond the range of get_num_frames() if the frame range passed to play(),
         * loop(), etc.  did.
         *
         * Unlike the value returned by get_full_fframe(), this return value will
         * never exceed the value passed to to_frame in the play() method.
         */
        """
        pass

    def getNextFrame(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_next_frame(AnimInterface self)
        
        /**
         * Returns the current integer frame number + 1, constrained to the range 0 <=
         * f < get_num_frames().
         *
         * If the play mode is PM_play, this will clamp to the same value as
         * get_frame() at the end of the animation.  If the play mode is any other
         * value, this will wrap around to frame 0 at the end of the animation.
         */
        """
        pass

    def getNumFrames(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_frames(AnimInterface self)
        
        /**
         * Returns the number of frames in the animation.  This is a property of the
         * animation and may not be directly adjusted by the user (although it may
         * change without warning with certain kinds of animations, since this is a
         * virtual method that may be overridden).
         */
        """
        pass

    def getPlayRate(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_play_rate(AnimInterface self)
        
        /**
         * Returns the rate at which the animation plays.  See set_play_rate().
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_frac(self, AnimInterface_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_frac(AnimInterface self)
        
        /**
         * Returns the fractional part of the current frame.  Normally, this is in the
         * range 0.0 <= f < 1.0, but in the one special case of an animation playing
         * to its end frame and stopping, it might exactly equal 1.0.
         *
         * It will always be true that get_full_frame() + get_frac() ==
         * get_full_fframe().
         */
        """
        pass

    def get_frame(self, AnimInterface_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_frame(AnimInterface self)
        
        /**
         * Returns the current integer frame number.  This number will be in the range
         * 0 <= f < get_num_frames().
         */
        """
        pass

    def get_frame_rate(self, AnimInterface_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_frame_rate(AnimInterface self)
        
        /**
         * Returns the native frame rate of the animation.  This is the number of
         * frames per second that will elapse when the play_rate is set to 1.0.  It is
         * a fixed property of the animation and may not be adjusted by the user.
         */
        """
        pass

    def get_full_fframe(self, AnimInterface_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_full_fframe(AnimInterface self)
        
        /**
         * Returns the current floating-point frame number.
         *
         * Unlike the value returned by get_frame(), this frame number may extend
         * beyond the range of get_num_frames() if the frame range passed to play(),
         * loop(), etc.  did.
         *
         * Unlike the value returned by get_full_frame(), this return value may equal
         * (to_frame + 1.0), when the animation has played to its natural end.
         * However, in this case the return value of get_full_frame() will be
         * to_frame, not (to_frame + 1).
         */
        """
        pass

    def get_full_frame(self, AnimInterface_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_full_frame(AnimInterface self)
        
        /**
         * Returns the current integer frame number.
         *
         * Unlike the value returned by get_frame(), this frame number may extend
         * beyond the range of get_num_frames() if the frame range passed to play(),
         * loop(), etc.  did.
         *
         * Unlike the value returned by get_full_fframe(), this return value will
         * never exceed the value passed to to_frame in the play() method.
         */
        """
        pass

    def get_next_frame(self, AnimInterface_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_next_frame(AnimInterface self)
        
        /**
         * Returns the current integer frame number + 1, constrained to the range 0 <=
         * f < get_num_frames().
         *
         * If the play mode is PM_play, this will clamp to the same value as
         * get_frame() at the end of the animation.  If the play mode is any other
         * value, this will wrap around to frame 0 at the end of the animation.
         */
        """
        pass

    def get_num_frames(self, AnimInterface_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_frames(AnimInterface self)
        
        /**
         * Returns the number of frames in the animation.  This is a property of the
         * animation and may not be directly adjusted by the user (although it may
         * change without warning with certain kinds of animations, since this is a
         * virtual method that may be overridden).
         */
        """
        pass

    def get_play_rate(self, AnimInterface_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_play_rate(AnimInterface self)
        
        /**
         * Returns the rate at which the animation plays.  See set_play_rate().
         */
        """
        pass

    def isPlaying(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_playing(AnimInterface self)
        
        /**
         * Returns true if the animation is currently playing, false if it is stopped
         * (e.g.  because stop() or pose() was called, or because it reached the end
         * of the animation after play() was called).
         */
        """
        pass

    def is_playing(self, AnimInterface_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_playing(AnimInterface self)
        
        /**
         * Returns true if the animation is currently playing, false if it is stopped
         * (e.g.  because stop() or pose() was called, or because it reached the end
         * of the animation after play() was called).
         */
        """
        pass

    def loop(self, const_AnimInterface_self, bool_restart): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        loop(const AnimInterface self, bool restart)
        loop(const AnimInterface self, bool restart, double from, double to)
        
        /**
         * Starts the entire animation looping.  If restart is true, the animation is
         * restarted from the beginning; otherwise, it continues from the current
         * frame.
         */
        
        /**
         * Loops the animation from the frame "from" to and including the frame "to",
         * indefinitely.  If restart is true, the animation is restarted from the
         * beginning; otherwise, it continues from the current frame.
         */
        """
        pass

    def output(self, AnimInterface_self, ostream_out): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        output(AnimInterface self, ostream out)
        
        /**
         *
         */
        """
        pass

    def pingpong(self, const_AnimInterface_self, bool_restart): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        pingpong(const AnimInterface self, bool restart)
        pingpong(const AnimInterface self, bool restart, double from, double to)
        
        /**
         * Starts the entire animation bouncing back and forth between its first frame
         * and last frame.  If restart is true, the animation is restarted from the
         * beginning; otherwise, it continues from the current frame.
         */
        
        /**
         * Loops the animation from the frame "from" to and including the frame "to",
         * and then back in the opposite direction, indefinitely.
         */
        """
        pass

    def play(self, const_AnimInterface_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        play(const AnimInterface self)
        play(const AnimInterface self, double from, double to)
        
        /**
         * Runs the entire animation from beginning to end and stops.
         */
        
        /**
         * Runs the animation from the frame "from" to and including the frame "to",
         * at which point the animation is stopped.  Both "from" and "to" frame
         * numbers may be outside the range (0, get_num_frames()) and the animation
         * will follow the range correctly, reporting numbers modulo get_num_frames().
         * For instance, play(0, get_num_frames() * 2) will play the animation twice
         * and then stop.
         */
        """
        pass

    def pose(self, const_AnimInterface_self, double_frame): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        pose(const AnimInterface self, double frame)
        
        /**
         * Sets the animation to the indicated frame and holds it there.
         */
        """
        pass

    def setPlayRate(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_play_rate(const AnimInterface self, double play_rate)
        
        /**
         * Changes the rate at which the animation plays.  1.0 is the normal speed,
         * 2.0 is twice normal speed, and 0.5 is half normal speed.  0.0 is legal to
         * pause the animation, and a negative value will play the animation
         * backwards.
         */
        """
        pass

    def set_play_rate(self, const_AnimInterface_self, double_play_rate): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_play_rate(const AnimInterface self, double play_rate)
        
        /**
         * Changes the rate at which the animation plays.  1.0 is the normal speed,
         * 2.0 is twice normal speed, and 0.5 is half normal speed.  0.0 is legal to
         * pause the animation, and a negative value will play the animation
         * backwards.
         */
        """
        pass

    def stop(self, const_AnimInterface_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        stop(const AnimInterface self)
        
        /**
         * Stops a currently playing or looping animation right where it is.  The
         * animation remains posed at the current frame.
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

    frac = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    frame = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    frame_rate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    full_fframe = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    full_frame = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    next_frame = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    num_frames = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    playing = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    play_rate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__doc__': '/**\n * This is the fundamental interface for things that have a play/loop/stop\n * type interface for frame-based animation, such as animated characters.\n * This is the base class for AnimControl and other, similar classes.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.AnimInterface' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE36F190>'
        '__repr__': None, # (!) real value is "<slot wrapper '__repr__' of 'panda3d.core.AnimInterface' objects>"
        '__str__': None, # (!) real value is "<slot wrapper '__str__' of 'panda3d.core.AnimInterface' objects>"
        'frac': None, # (!) real value is "<attribute 'frac' of 'panda3d.core.AnimInterface' objects>"
        'frame': None, # (!) real value is "<attribute 'frame' of 'panda3d.core.AnimInterface' objects>"
        'frame_rate': None, # (!) real value is "<attribute 'frame_rate' of 'panda3d.core.AnimInterface' objects>"
        'full_fframe': None, # (!) real value is "<attribute 'full_fframe' of 'panda3d.core.AnimInterface' objects>"
        'full_frame': None, # (!) real value is "<attribute 'full_frame' of 'panda3d.core.AnimInterface' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE36F190>)>'
        'getFrac': None, # (!) real value is "<method 'getFrac' of 'panda3d.core.AnimInterface' objects>"
        'getFrame': None, # (!) real value is "<method 'getFrame' of 'panda3d.core.AnimInterface' objects>"
        'getFrameRate': None, # (!) real value is "<method 'getFrameRate' of 'panda3d.core.AnimInterface' objects>"
        'getFullFframe': None, # (!) real value is "<method 'getFullFframe' of 'panda3d.core.AnimInterface' objects>"
        'getFullFrame': None, # (!) real value is "<method 'getFullFrame' of 'panda3d.core.AnimInterface' objects>"
        'getNextFrame': None, # (!) real value is "<method 'getNextFrame' of 'panda3d.core.AnimInterface' objects>"
        'getNumFrames': None, # (!) real value is "<method 'getNumFrames' of 'panda3d.core.AnimInterface' objects>"
        'getPlayRate': None, # (!) real value is "<method 'getPlayRate' of 'panda3d.core.AnimInterface' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE36F190>)>'
        'get_frac': None, # (!) real value is "<method 'get_frac' of 'panda3d.core.AnimInterface' objects>"
        'get_frame': None, # (!) real value is "<method 'get_frame' of 'panda3d.core.AnimInterface' objects>"
        'get_frame_rate': None, # (!) real value is "<method 'get_frame_rate' of 'panda3d.core.AnimInterface' objects>"
        'get_full_fframe': None, # (!) real value is "<method 'get_full_fframe' of 'panda3d.core.AnimInterface' objects>"
        'get_full_frame': None, # (!) real value is "<method 'get_full_frame' of 'panda3d.core.AnimInterface' objects>"
        'get_next_frame': None, # (!) real value is "<method 'get_next_frame' of 'panda3d.core.AnimInterface' objects>"
        'get_num_frames': None, # (!) real value is "<method 'get_num_frames' of 'panda3d.core.AnimInterface' objects>"
        'get_play_rate': None, # (!) real value is "<method 'get_play_rate' of 'panda3d.core.AnimInterface' objects>"
        'isPlaying': None, # (!) real value is "<method 'isPlaying' of 'panda3d.core.AnimInterface' objects>"
        'is_playing': None, # (!) real value is "<method 'is_playing' of 'panda3d.core.AnimInterface' objects>"
        'loop': None, # (!) real value is "<method 'loop' of 'panda3d.core.AnimInterface' objects>"
        'next_frame': None, # (!) real value is "<attribute 'next_frame' of 'panda3d.core.AnimInterface' objects>"
        'num_frames': None, # (!) real value is "<attribute 'num_frames' of 'panda3d.core.AnimInterface' objects>"
        'output': None, # (!) real value is "<method 'output' of 'panda3d.core.AnimInterface' objects>"
        'pingpong': None, # (!) real value is "<method 'pingpong' of 'panda3d.core.AnimInterface' objects>"
        'play': None, # (!) real value is "<method 'play' of 'panda3d.core.AnimInterface' objects>"
        'play_rate': None, # (!) real value is "<attribute 'play_rate' of 'panda3d.core.AnimInterface' objects>"
        'playing': None, # (!) real value is "<attribute 'playing' of 'panda3d.core.AnimInterface' objects>"
        'pose': None, # (!) real value is "<method 'pose' of 'panda3d.core.AnimInterface' objects>"
        'setPlayRate': None, # (!) real value is "<method 'setPlayRate' of 'panda3d.core.AnimInterface' objects>"
        'set_play_rate': None, # (!) real value is "<method 'set_play_rate' of 'panda3d.core.AnimInterface' objects>"
        'stop': None, # (!) real value is "<method 'stop' of 'panda3d.core.AnimInterface' objects>"
    }


