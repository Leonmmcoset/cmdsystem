# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .TypedWritableReferenceCount import TypedWritableReferenceCount

class MovieVideoCursor(TypedWritableReferenceCount):
    """
    /**
     * A MovieVideo is actually any source that provides a sequence of video
     * frames.  That could include an AVI file, a digital camera, or an internet
     * TV station.  A MovieVideoCursor is a handle that lets you read data
     * sequentially from a MovieVideo.
     *
     * Thread safety: each individual MovieVideoCursor must be owned and accessed
     * by a single thread.  It is OK for two different threads to open the same
     * file at the same time, as long as they use separate MovieVideoCursor
     * objects.
     */
    """
    def aborted(self, MovieVideoCursor_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        aborted(MovieVideoCursor self)
        
        /**
         * Returns true if the video has aborted prematurely.  For example, this could
         * occur if the Movie was actually an internet TV station, and the connection
         * was lost.  Reaching the normal end of the video does not constitute an
         * 'abort' condition.
         */
        """
        pass

    def applyToTexture(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        apply_to_texture(const MovieVideoCursor self, const Buffer buffer, Texture t, int page)
        
        /**
         * Stores this buffer's contents in the indicated texture.
         */
        """
        pass

    def applyToTextureAlpha(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        apply_to_texture_alpha(const MovieVideoCursor self, const Buffer buffer, Texture t, int page, int alpha_src)
        
        /**
         * Copies this buffer's contents into the alpha channel of the supplied
         * texture.  The RGB channels of the texture are not touched.
         */
        """
        pass

    def applyToTextureRgb(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        apply_to_texture_rgb(const MovieVideoCursor self, const Buffer buffer, Texture t, int page)
        
        /**
         * Copies this buffer's contents into the RGB channels of the supplied
         * texture.  The alpha channel of the texture is not touched.
         */
        """
        pass

    def apply_to_texture(self, const_MovieVideoCursor_self, const_Buffer_buffer, Texture_t, int_page): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        apply_to_texture(const MovieVideoCursor self, const Buffer buffer, Texture t, int page)
        
        /**
         * Stores this buffer's contents in the indicated texture.
         */
        """
        pass

    def apply_to_texture_alpha(self, const_MovieVideoCursor_self, const_Buffer_buffer, Texture_t, int_page, int_alpha_src): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        apply_to_texture_alpha(const MovieVideoCursor self, const Buffer buffer, Texture t, int page, int alpha_src)
        
        /**
         * Copies this buffer's contents into the alpha channel of the supplied
         * texture.  The RGB channels of the texture are not touched.
         */
        """
        pass

    def apply_to_texture_rgb(self, const_MovieVideoCursor_self, const_Buffer_buffer, Texture_t, int_page): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        apply_to_texture_rgb(const MovieVideoCursor self, const Buffer buffer, Texture t, int page)
        
        /**
         * Copies this buffer's contents into the RGB channels of the supplied
         * texture.  The alpha channel of the texture is not touched.
         */
        """
        pass

    def canSeek(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        can_seek(MovieVideoCursor self)
        
        /**
         * Returns true if the movie can seek.  If this is true, seeking is still not
         * guaranteed to be fast: for some movies, seeking is implemented by rewinding
         * to the beginning and then fast-forwarding to the desired location.  Even if
         * the movie cannot seek, the fetch methods can still advance to an arbitrary
         * location by reading frames and discarding them.  However, to move backward,
         * can_seek must return true.
         */
        """
        pass

    def canSeekFast(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        can_seek_fast(MovieVideoCursor self)
        
        /**
         * Returns true if seek operations are constant time.
         */
        """
        pass

    def can_seek(self, MovieVideoCursor_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        can_seek(MovieVideoCursor self)
        
        /**
         * Returns true if the movie can seek.  If this is true, seeking is still not
         * guaranteed to be fast: for some movies, seeking is implemented by rewinding
         * to the beginning and then fast-forwarding to the desired location.  Even if
         * the movie cannot seek, the fetch methods can still advance to an arbitrary
         * location by reading frames and discarding them.  However, to move backward,
         * can_seek must return true.
         */
        """
        pass

    def can_seek_fast(self, MovieVideoCursor_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        can_seek_fast(MovieVideoCursor self)
        
        /**
         * Returns true if seek operations are constant time.
         */
        """
        pass

    def fetchBuffer(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        fetch_buffer(const MovieVideoCursor self)
        
        /**
         * Gets the current video frame (as specified by set_time()) from the movie
         * and returns it in a pre-allocated buffer.  You may simply let the buffer
         * dereference and delete itself when you are done with it.
         *
         * This may return NULL (even if set_time() returned true) if the frame is not
         * available for some reason.
         */
        """
        pass

    def fetch_buffer(self, const_MovieVideoCursor_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        fetch_buffer(const MovieVideoCursor self)
        
        /**
         * Gets the current video frame (as specified by set_time()) from the movie
         * and returns it in a pre-allocated buffer.  You may simply let the buffer
         * dereference and delete itself when you are done with it.
         *
         * This may return NULL (even if set_time() returned true) if the frame is not
         * available for some reason.
         */
        """
        pass

    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getNumComponents(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_components(MovieVideoCursor self)
        
        /**
         * Returns 4 if the movie has an alpha channel, 3 otherwise.
         */
        """
        pass

    def getSource(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_source(MovieVideoCursor self)
        
        /**
         * Get the MovieVideo which this cursor references.
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_num_components(self, MovieVideoCursor_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_components(MovieVideoCursor self)
        
        /**
         * Returns 4 if the movie has an alpha channel, 3 otherwise.
         */
        """
        pass

    def get_source(self, MovieVideoCursor_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_source(MovieVideoCursor self)
        
        /**
         * Get the MovieVideo which this cursor references.
         */
        """
        pass

    def length(self, MovieVideoCursor_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        length(MovieVideoCursor self)
        
        /**
         * Returns the length of the movie.
         *
         * Some kinds of Movie, such as internet TV station, might not have a
         * predictable length.  In that case, the length will be set to a very large
         * number: 1.0E10. If the internet TV station goes offline, the video or audio
         * stream will set its abort flag.  Reaching the end of the movie (ie, the
         * specified length) normally does not cause the abort flag to be set.
         *
         * The video and audio streams produced by get_video and get_audio are always
         * of unlimited duration - you can always read another video frame or another
         * audio sample.  This is true even if the specified length is reached, or an
         * abort is flagged.  If either stream runs out of data, it will synthesize
         * blank video frames and silent audio samples as necessary to satisfy read
         * requests.
         *
         * Some AVI files have incorrect length values encoded into them - usually,
         * they're a second or two long or short.  When playing such an AVI using the
         * Movie class, you may see a slightly truncated video, or a slightly
         * elongated video (padded with black frames).  There are utilities out there
         * to fix the length values in AVI files.
         *
         */
        """
        pass

    def ready(self, MovieVideoCursor_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        ready(MovieVideoCursor self)
        
        /**
         * Returns true if the cursor is a streaming source, and if a video frame is
         * ready to be read.  For non- streaming sources, this is always false.
         */
        """
        pass

    def setTime(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_time(const MovieVideoCursor self, double timestamp, int loop_count)
        
        /**
         * Updates the cursor to the indicated time.  If loop_count >= 1, the time is
         * clamped to the movie's length * loop_count.  If loop_count <= 0, the time
         * is understood to be modulo the movie's length.
         *
         * Returns true if a new frame is now available, false otherwise.  If this
         * returns true, you should immediately follow this with exactly *one* call to
         * fetch_buffer().
         *
         * If the movie reports that it can_seek, you may also specify a time value
         * less than the previous value you passed to set_time().  Otherwise, you may
         * only specify a time value greater than or equal to the previous value.
         *
         * If the movie reports that it can_seek, it doesn't mean that it can do so
         * quickly.  It may have to rewind the movie and then fast forward to the
         * desired location.  Only if can_seek_fast returns true can it seek rapidly.
         */
        """
        pass

    def setupTexture(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        setup_texture(MovieVideoCursor self, Texture tex)
        
        /**
         * Set up the specified Texture object to contain content from this movie.
         * This should be called once, not every frame.
         */
        """
        pass

    def setup_texture(self, MovieVideoCursor_self, Texture_tex): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        setup_texture(MovieVideoCursor self, Texture tex)
        
        /**
         * Set up the specified Texture object to contain content from this movie.
         * This should be called once, not every frame.
         */
        """
        pass

    def set_time(self, const_MovieVideoCursor_self, double_timestamp, int_loop_count): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_time(const MovieVideoCursor self, double timestamp, int loop_count)
        
        /**
         * Updates the cursor to the indicated time.  If loop_count >= 1, the time is
         * clamped to the movie's length * loop_count.  If loop_count <= 0, the time
         * is understood to be modulo the movie's length.
         *
         * Returns true if a new frame is now available, false otherwise.  If this
         * returns true, you should immediately follow this with exactly *one* call to
         * fetch_buffer().
         *
         * If the movie reports that it can_seek, you may also specify a time value
         * less than the previous value you passed to set_time().  Otherwise, you may
         * only specify a time value greater than or equal to the previous value.
         *
         * If the movie reports that it can_seek, it doesn't mean that it can do so
         * quickly.  It may have to rewind the movie and then fast forward to the
         * desired location.  Only if can_seek_fast returns true can it seek rapidly.
         */
        """
        pass

    def sizeX(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        size_x(MovieVideoCursor self)
        
        /**
         * Get the horizontal size of the movie.
         */
        """
        pass

    def sizeY(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        size_y(MovieVideoCursor self)
        
        /**
         * Get the vertical size of the movie.
         */
        """
        pass

    def size_x(self, MovieVideoCursor_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        size_x(MovieVideoCursor self)
        
        /**
         * Get the horizontal size of the movie.
         */
        """
        pass

    def size_y(self, MovieVideoCursor_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        size_y(MovieVideoCursor self)
        
        /**
         * Get the vertical size of the movie.
         */
        """
        pass

    def streaming(self, MovieVideoCursor_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        streaming(MovieVideoCursor self)
        
        /**
         * Returns true if the video frames are being "pushed" at us by something that
         * operates at its own speed - for example, a webcam.  In this case, the
         * frames come when they're ready to come.  Attempting to read too soon will
         * produce nothing, reading too late will cause frames to be dropped.  In this
         * case, the ready flag can be used to determine whether or not a frame is
         * ready for reading.
         *
         * When streaming, you should still pay attention to last_start, but the value
         * of next_start is only a guess.
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

    Buffer = None # (!) real value is "<class 'panda3d.core.Buffer'>"
    DtoolClassDict = {
        'Buffer': None, # (!) real value is "<class 'panda3d.core.Buffer'>"
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.core.MovieVideoCursor' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.core.MovieVideoCursor' objects>"
        '__doc__': '/**\n * A MovieVideo is actually any source that provides a sequence of video\n * frames.  That could include an AVI file, a digital camera, or an internet\n * TV station.  A MovieVideoCursor is a handle that lets you read data\n * sequentially from a MovieVideo.\n *\n * Thread safety: each individual MovieVideoCursor must be owned and accessed\n * by a single thread.  It is OK for two different threads to open the same\n * file at the same time, as long as they use separate MovieVideoCursor\n * objects.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.MovieVideoCursor' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE2B8690>'
        'aborted': None, # (!) real value is "<method 'aborted' of 'panda3d.core.MovieVideoCursor' objects>"
        'applyToTexture': None, # (!) real value is "<method 'applyToTexture' of 'panda3d.core.MovieVideoCursor' objects>"
        'applyToTextureAlpha': None, # (!) real value is "<method 'applyToTextureAlpha' of 'panda3d.core.MovieVideoCursor' objects>"
        'applyToTextureRgb': None, # (!) real value is "<method 'applyToTextureRgb' of 'panda3d.core.MovieVideoCursor' objects>"
        'apply_to_texture': None, # (!) real value is "<method 'apply_to_texture' of 'panda3d.core.MovieVideoCursor' objects>"
        'apply_to_texture_alpha': None, # (!) real value is "<method 'apply_to_texture_alpha' of 'panda3d.core.MovieVideoCursor' objects>"
        'apply_to_texture_rgb': None, # (!) real value is "<method 'apply_to_texture_rgb' of 'panda3d.core.MovieVideoCursor' objects>"
        'canSeek': None, # (!) real value is "<method 'canSeek' of 'panda3d.core.MovieVideoCursor' objects>"
        'canSeekFast': None, # (!) real value is "<method 'canSeekFast' of 'panda3d.core.MovieVideoCursor' objects>"
        'can_seek': None, # (!) real value is "<method 'can_seek' of 'panda3d.core.MovieVideoCursor' objects>"
        'can_seek_fast': None, # (!) real value is "<method 'can_seek_fast' of 'panda3d.core.MovieVideoCursor' objects>"
        'fetchBuffer': None, # (!) real value is "<method 'fetchBuffer' of 'panda3d.core.MovieVideoCursor' objects>"
        'fetch_buffer': None, # (!) real value is "<method 'fetch_buffer' of 'panda3d.core.MovieVideoCursor' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE2B8690>)>'
        'getNumComponents': None, # (!) real value is "<method 'getNumComponents' of 'panda3d.core.MovieVideoCursor' objects>"
        'getSource': None, # (!) real value is "<method 'getSource' of 'panda3d.core.MovieVideoCursor' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE2B8690>)>'
        'get_num_components': None, # (!) real value is "<method 'get_num_components' of 'panda3d.core.MovieVideoCursor' objects>"
        'get_source': None, # (!) real value is "<method 'get_source' of 'panda3d.core.MovieVideoCursor' objects>"
        'length': None, # (!) real value is "<method 'length' of 'panda3d.core.MovieVideoCursor' objects>"
        'ready': None, # (!) real value is "<method 'ready' of 'panda3d.core.MovieVideoCursor' objects>"
        'setTime': None, # (!) real value is "<method 'setTime' of 'panda3d.core.MovieVideoCursor' objects>"
        'set_time': None, # (!) real value is "<method 'set_time' of 'panda3d.core.MovieVideoCursor' objects>"
        'setupTexture': None, # (!) real value is "<method 'setupTexture' of 'panda3d.core.MovieVideoCursor' objects>"
        'setup_texture': None, # (!) real value is "<method 'setup_texture' of 'panda3d.core.MovieVideoCursor' objects>"
        'sizeX': None, # (!) real value is "<method 'sizeX' of 'panda3d.core.MovieVideoCursor' objects>"
        'sizeY': None, # (!) real value is "<method 'sizeY' of 'panda3d.core.MovieVideoCursor' objects>"
        'size_x': None, # (!) real value is "<method 'size_x' of 'panda3d.core.MovieVideoCursor' objects>"
        'size_y': None, # (!) real value is "<method 'size_y' of 'panda3d.core.MovieVideoCursor' objects>"
        'streaming': None, # (!) real value is "<method 'streaming' of 'panda3d.core.MovieVideoCursor' objects>"
    }


