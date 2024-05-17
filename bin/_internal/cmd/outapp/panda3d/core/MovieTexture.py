# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .Texture import Texture

class MovieTexture(Texture):
    """
    /**
     * A texture that fetches video frames from an underlying object of class
     * Movie.
     */
    """
    def getAlphaCursor(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_alpha_cursor(const MovieTexture self, int page)
        
        /**
         * Returns the MovieVideoCursor that is feeding the alpha channel for the
         * indicated page, where 0 <= page < get_num_pages().
         */
        """
        pass

    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getColorCursor(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_color_cursor(const MovieTexture self, int page)
        
        /**
         * Returns the MovieVideoCursor that is feeding the color channels for the
         * indicated page, where 0 <= page < get_num_pages().
         */
        """
        pass

    def getLoop(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_loop(MovieTexture self)
        
        /**
         * Returns true if the movie's loop count is not equal to one.
         */
        """
        pass

    def getLoopCount(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_loop_count(MovieTexture self)
        
        /**
         * Returns the movie's loop count.
         */
        """
        pass

    def getPlayRate(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_play_rate(MovieTexture self)
        
        /**
         * Gets the movie's play-rate.
         */
        """
        pass

    def getTime(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_time(MovieTexture self)
        
        /**
         * Returns the current value of the movie's cursor.  If the movie's loop count
         * is greater than one, then its length is effectively multiplied for the
         * purposes of this function.  In other words, the return value will be in the
         * range 0.0 to (length * loopcount).
         */
        """
        pass

    def getVideoHeight(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_video_height(MovieTexture self)
        
        /**
         * Returns the height in texels of the source video stream.  This is not
         * necessarily the height of the actual texture, since the texture may have
         * been expanded to raise it to a power of 2.
         */
        """
        pass

    def getVideoLength(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_video_length(MovieTexture self)
        
        /**
         * Returns the length of the video.
         */
        """
        pass

    def getVideoWidth(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_video_width(MovieTexture self)
        
        /**
         * Returns the width in texels of the source video stream.  This is not
         * necessarily the width of the actual texture, since the texture may have
         * been expanded to raise it to a power of 2.
         */
        """
        pass

    def get_alpha_cursor(self, const_MovieTexture_self, int_page): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_alpha_cursor(const MovieTexture self, int page)
        
        /**
         * Returns the MovieVideoCursor that is feeding the alpha channel for the
         * indicated page, where 0 <= page < get_num_pages().
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_color_cursor(self, const_MovieTexture_self, int_page): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_color_cursor(const MovieTexture self, int page)
        
        /**
         * Returns the MovieVideoCursor that is feeding the color channels for the
         * indicated page, where 0 <= page < get_num_pages().
         */
        """
        pass

    def get_loop(self, MovieTexture_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_loop(MovieTexture self)
        
        /**
         * Returns true if the movie's loop count is not equal to one.
         */
        """
        pass

    def get_loop_count(self, MovieTexture_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_loop_count(MovieTexture self)
        
        /**
         * Returns the movie's loop count.
         */
        """
        pass

    def get_play_rate(self, MovieTexture_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_play_rate(MovieTexture self)
        
        /**
         * Gets the movie's play-rate.
         */
        """
        pass

    def get_time(self, MovieTexture_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_time(MovieTexture self)
        
        /**
         * Returns the current value of the movie's cursor.  If the movie's loop count
         * is greater than one, then its length is effectively multiplied for the
         * purposes of this function.  In other words, the return value will be in the
         * range 0.0 to (length * loopcount).
         */
        """
        pass

    def get_video_height(self, MovieTexture_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_video_height(MovieTexture self)
        
        /**
         * Returns the height in texels of the source video stream.  This is not
         * necessarily the height of the actual texture, since the texture may have
         * been expanded to raise it to a power of 2.
         */
        """
        pass

    def get_video_length(self, MovieTexture_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_video_length(MovieTexture self)
        
        /**
         * Returns the length of the video.
         */
        """
        pass

    def get_video_width(self, MovieTexture_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_video_width(MovieTexture self)
        
        /**
         * Returns the width in texels of the source video stream.  This is not
         * necessarily the width of the actual texture, since the texture may have
         * been expanded to raise it to a power of 2.
         */
        """
        pass

    def isPlaying(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_playing(MovieTexture self)
        
        /**
         * Returns true if the movie's cursor is advancing.
         */
        """
        pass

    def is_playing(self, MovieTexture_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_playing(MovieTexture self)
        
        /**
         * Returns true if the movie's cursor is advancing.
         */
        """
        pass

    def play(self, const_MovieTexture_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        play(const MovieTexture self)
        
        /**
         * Plays the movie from the beginning.
         */
        """
        pass

    def restart(self, const_MovieTexture_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        restart(const MovieTexture self)
        
        /**
         * Start playing the movie from where it was last paused.  Has no effect if
         * the movie is not paused, or if the movie's cursor is already at the end.
         */
        """
        pass

    def setLoop(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_loop(const MovieTexture self, bool enable)
        
        /**
         * If true, sets the movie's loop count to 1 billion.  If false, sets the
         * movie's loop count to one.
         */
        """
        pass

    def setLoopCount(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_loop_count(const MovieTexture self, int count)
        
        /**
         * Sets the movie's loop count to the desired value.
         */
        """
        pass

    def setPlayRate(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_play_rate(const MovieTexture self, double play_rate)
        
        /**
         * Sets the movie's play-rate.  This is the speed at which the movie's cursor
         * advances.  The default is to advance 1.0 movie-seconds per real-time
         * second.
         */
        """
        pass

    def setTime(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_time(const MovieTexture self, double t)
        
        /**
         * Sets the movie's cursor.
         */
        """
        pass

    def set_loop(self, const_MovieTexture_self, bool_enable): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_loop(const MovieTexture self, bool enable)
        
        /**
         * If true, sets the movie's loop count to 1 billion.  If false, sets the
         * movie's loop count to one.
         */
        """
        pass

    def set_loop_count(self, const_MovieTexture_self, int_count): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_loop_count(const MovieTexture self, int count)
        
        /**
         * Sets the movie's loop count to the desired value.
         */
        """
        pass

    def set_play_rate(self, const_MovieTexture_self, double_play_rate): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_play_rate(const MovieTexture self, double play_rate)
        
        /**
         * Sets the movie's play-rate.  This is the speed at which the movie's cursor
         * advances.  The default is to advance 1.0 movie-seconds per real-time
         * second.
         */
        """
        pass

    def set_time(self, const_MovieTexture_self, double_t): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_time(const MovieTexture self, double t)
        
        /**
         * Sets the movie's cursor.
         */
        """
        pass

    def stop(self, const_MovieTexture_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        stop(const MovieTexture self)
        
        /**
         * Stops a currently playing or looping movie right where it is.  The movie's
         * cursor remains frozen at the point where it was stopped.
         */
        """
        pass

    def synchronizeTo(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        synchronize_to(const MovieTexture self, AudioSound sound)
        
        /**
         * Synchronize this texture to a sound.  Typically, you would load the texture
         * and the sound from the same AVI file.
         */
        """
        pass

    def synchronize_to(self, const_MovieTexture_self, AudioSound_sound): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        synchronize_to(const MovieTexture self, AudioSound sound)
        
        /**
         * Synchronize this texture to a sound.  Typically, you would load the texture
         * and the sound from the same AVI file.
         */
        """
        pass

    def unsynchronize(self, const_MovieTexture_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        unsynchronize(const MovieTexture self)
        
        /**
         * Stop synchronizing with a sound.
         */
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    loop = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    loop_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    playing = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    play_rate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    time = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    video_height = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    video_length = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    video_width = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__doc__': '/**\n * A texture that fetches video frames from an underlying object of class\n * Movie.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.MovieTexture' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE2BCE70>'
        'getAlphaCursor': None, # (!) real value is "<method 'getAlphaCursor' of 'panda3d.core.MovieTexture' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE2BCE70>)>'
        'getColorCursor': None, # (!) real value is "<method 'getColorCursor' of 'panda3d.core.MovieTexture' objects>"
        'getLoop': None, # (!) real value is "<method 'getLoop' of 'panda3d.core.MovieTexture' objects>"
        'getLoopCount': None, # (!) real value is "<method 'getLoopCount' of 'panda3d.core.MovieTexture' objects>"
        'getPlayRate': None, # (!) real value is "<method 'getPlayRate' of 'panda3d.core.MovieTexture' objects>"
        'getTime': None, # (!) real value is "<method 'getTime' of 'panda3d.core.MovieTexture' objects>"
        'getVideoHeight': None, # (!) real value is "<method 'getVideoHeight' of 'panda3d.core.MovieTexture' objects>"
        'getVideoLength': None, # (!) real value is "<method 'getVideoLength' of 'panda3d.core.MovieTexture' objects>"
        'getVideoWidth': None, # (!) real value is "<method 'getVideoWidth' of 'panda3d.core.MovieTexture' objects>"
        'get_alpha_cursor': None, # (!) real value is "<method 'get_alpha_cursor' of 'panda3d.core.MovieTexture' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE2BCE70>)>'
        'get_color_cursor': None, # (!) real value is "<method 'get_color_cursor' of 'panda3d.core.MovieTexture' objects>"
        'get_loop': None, # (!) real value is "<method 'get_loop' of 'panda3d.core.MovieTexture' objects>"
        'get_loop_count': None, # (!) real value is "<method 'get_loop_count' of 'panda3d.core.MovieTexture' objects>"
        'get_play_rate': None, # (!) real value is "<method 'get_play_rate' of 'panda3d.core.MovieTexture' objects>"
        'get_time': None, # (!) real value is "<method 'get_time' of 'panda3d.core.MovieTexture' objects>"
        'get_video_height': None, # (!) real value is "<method 'get_video_height' of 'panda3d.core.MovieTexture' objects>"
        'get_video_length': None, # (!) real value is "<method 'get_video_length' of 'panda3d.core.MovieTexture' objects>"
        'get_video_width': None, # (!) real value is "<method 'get_video_width' of 'panda3d.core.MovieTexture' objects>"
        'isPlaying': None, # (!) real value is "<method 'isPlaying' of 'panda3d.core.MovieTexture' objects>"
        'is_playing': None, # (!) real value is "<method 'is_playing' of 'panda3d.core.MovieTexture' objects>"
        'loop': None, # (!) real value is "<attribute 'loop' of 'panda3d.core.MovieTexture' objects>"
        'loop_count': None, # (!) real value is "<attribute 'loop_count' of 'panda3d.core.MovieTexture' objects>"
        'play': None, # (!) real value is "<method 'play' of 'panda3d.core.MovieTexture' objects>"
        'play_rate': None, # (!) real value is "<attribute 'play_rate' of 'panda3d.core.MovieTexture' objects>"
        'playing': None, # (!) real value is "<attribute 'playing' of 'panda3d.core.MovieTexture' objects>"
        'restart': None, # (!) real value is "<method 'restart' of 'panda3d.core.MovieTexture' objects>"
        'setLoop': None, # (!) real value is "<method 'setLoop' of 'panda3d.core.MovieTexture' objects>"
        'setLoopCount': None, # (!) real value is "<method 'setLoopCount' of 'panda3d.core.MovieTexture' objects>"
        'setPlayRate': None, # (!) real value is "<method 'setPlayRate' of 'panda3d.core.MovieTexture' objects>"
        'setTime': None, # (!) real value is "<method 'setTime' of 'panda3d.core.MovieTexture' objects>"
        'set_loop': None, # (!) real value is "<method 'set_loop' of 'panda3d.core.MovieTexture' objects>"
        'set_loop_count': None, # (!) real value is "<method 'set_loop_count' of 'panda3d.core.MovieTexture' objects>"
        'set_play_rate': None, # (!) real value is "<method 'set_play_rate' of 'panda3d.core.MovieTexture' objects>"
        'set_time': None, # (!) real value is "<method 'set_time' of 'panda3d.core.MovieTexture' objects>"
        'stop': None, # (!) real value is "<method 'stop' of 'panda3d.core.MovieTexture' objects>"
        'synchronizeTo': None, # (!) real value is "<method 'synchronizeTo' of 'panda3d.core.MovieTexture' objects>"
        'synchronize_to': None, # (!) real value is "<method 'synchronize_to' of 'panda3d.core.MovieTexture' objects>"
        'time': None, # (!) real value is "<attribute 'time' of 'panda3d.core.MovieTexture' objects>"
        'unsynchronize': None, # (!) real value is "<method 'unsynchronize' of 'panda3d.core.MovieTexture' objects>"
        'video_height': None, # (!) real value is "<attribute 'video_height' of 'panda3d.core.MovieTexture' objects>"
        'video_length': None, # (!) real value is "<attribute 'video_length' of 'panda3d.core.MovieTexture' objects>"
        'video_width': None, # (!) real value is "<attribute 'video_width' of 'panda3d.core.MovieTexture' objects>"
    }


