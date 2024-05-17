# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .TypedWritableReferenceCount import TypedWritableReferenceCount

class MovieAudioCursor(TypedWritableReferenceCount):
    """
    /**
     * A MovieAudio is actually any source that provides a sequence of audio
     * samples.  That could include an AVI file, a microphone, or an internet TV
     * station.  A MovieAudioCursor is a handle that lets you read data
     * sequentially from a MovieAudio.
     *
     * Thread safety: each individual MovieAudioCursor must be owned and accessed
     * by a single thread.  It is OK for two different threads to open the same
     * file at the same time, as long as they use separate MovieAudioCursor
     * objects.
     */
    """
    def aborted(self, MovieAudioCursor_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        aborted(MovieAudioCursor self)
        
        /**
         * If aborted is true, it means that the "ready" samples are not being
         * replenished.  See the method "ready" for an explanation.
         */
        """
        pass

    def audioChannels(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        audio_channels(MovieAudioCursor self)
        
        /**
         * Returns the number of audio channels (ie, two for stereo, one for mono).
         */
        """
        pass

    def audioRate(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        audio_rate(MovieAudioCursor self)
        
        /**
         * Returns the audio sample rate.
         */
        """
        pass

    def audio_channels(self, MovieAudioCursor_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        audio_channels(MovieAudioCursor self)
        
        /**
         * Returns the number of audio channels (ie, two for stereo, one for mono).
         */
        """
        pass

    def audio_rate(self, MovieAudioCursor_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        audio_rate(MovieAudioCursor self)
        
        /**
         * Returns the audio sample rate.
         */
        """
        pass

    def canSeek(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        can_seek(MovieAudioCursor self)
        
        /**
         * Returns true if the movie can seek.  If this is true, seeking is still not
         * guaranteed to be fast: for some movies, seeking is implemented by rewinding
         * to the beginning and then fast-forwarding to the desired location.  Even if
         * the movie cannot seek, the seek method can still advance to an arbitrary
         * location by reading samples and discarding them.  However, to move
         * backward, can_seek must return true.
         */
        """
        pass

    def canSeekFast(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        can_seek_fast(MovieAudioCursor self)
        
        /**
         * Returns true if seek operations are constant time.
         */
        """
        pass

    def can_seek(self, MovieAudioCursor_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        can_seek(MovieAudioCursor self)
        
        /**
         * Returns true if the movie can seek.  If this is true, seeking is still not
         * guaranteed to be fast: for some movies, seeking is implemented by rewinding
         * to the beginning and then fast-forwarding to the desired location.  Even if
         * the movie cannot seek, the seek method can still advance to an arbitrary
         * location by reading samples and discarding them.  However, to move
         * backward, can_seek must return true.
         */
        """
        pass

    def can_seek_fast(self, MovieAudioCursor_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        can_seek_fast(MovieAudioCursor self)
        
        /**
         * Returns true if seek operations are constant time.
         */
        """
        pass

    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getSource(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_source(MovieAudioCursor self)
        
        /**
         * Returns the MovieAudio which this cursor references.
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_source(self, MovieAudioCursor_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_source(MovieAudioCursor self)
        
        /**
         * Returns the MovieAudio which this cursor references.
         */
        """
        pass

    def length(self, MovieAudioCursor_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        length(MovieAudioCursor self)
        
        /**
         * Returns the length of the movie.  Attempting to read audio samples beyond
         * the specified length will produce silent samples.
         *
         * Some kinds of Movie, such as internet TV station, might not have a
         * predictable length.  In that case, the length will be set to a very large
         * number: 1.0E10.
         *
         * Some AVI files have incorrect length values encoded into them - they may be
         * a second or two long or short.  When playing such an AVI using the Movie
         * class, you may see a slightly truncated video, or a slightly elongated
         * video (padded with black frames).  There are utilities out there to fix the
         * length values in AVI files.
         *
         * An audio consumer needs to check the length, the ready status, and the
         * aborted flag.
         */
        """
        pass

    def readSamples(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        read_samples(const MovieAudioCursor self, int n)
        read_samples(const MovieAudioCursor self, int n, Datagram dg)
        
        /**
         * Read audio samples from the stream.  N is the number of samples you wish to
         * read.  Your buffer must be equal in size to N * channels.  Multiple-channel
         * audio will be interleaved.
         */
        
        /**
         * Read audio samples from the stream into a Datagram.  N is the number of
         * samples you wish to read.  Multiple-channel audio will be interleaved.
         *
         * This is not particularly efficient, but it may be a convenient way to
         * manipulate samples in python.
         */
        
        /**
         * Read audio samples from the stream and returns them as a string.  The
         * samples are stored little-endian in the string.  N is the number of samples
         * you wish to read.  Multiple-channel audio will be interleaved.
         *
         * This is not particularly efficient, but it may be a convenient way to
         * manipulate samples in python.
         */
        """
        pass

    def ready(self, MovieAudioCursor_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        ready(MovieAudioCursor self)
        
        /**
         * Returns the number of audio samples that are ready to read.  This is
         * primarily relevant for sources like microphones which produce samples at a
         * fixed rate.  If you try to read more samples than are ready, the result
         * will be silent samples.
         *
         * Some audio streams do not have a limit on how fast they can produce
         * samples.  Such streams will always return 0x40000000 as the ready-count.
         * This may well exceed the length of the audio stream.  You therefore need to
         * check length separately.
         *
         * If the aborted flag is set, that means the ready count is no longer being
         * replenished.  For example, a MovieAudioCursor might be reading from an
         * internet radio station, and it might buffer data to avoid underruns.  If it
         * loses connection to the radio station, it will set the aborted flag to
         * indicate that the buffer is no longer being replenished.  But it is still
         * ok to read the samples that are in the buffer, at least until they run out.
         * Once those are gone, there will be no more.
         *
         * An audio consumer needs to check the length, the ready status, and the
         * aborted flag.
         */
        """
        pass

    def read_samples(self, const_MovieAudioCursor_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        read_samples(const MovieAudioCursor self, int n)
        read_samples(const MovieAudioCursor self, int n, Datagram dg)
        
        /**
         * Read audio samples from the stream.  N is the number of samples you wish to
         * read.  Your buffer must be equal in size to N * channels.  Multiple-channel
         * audio will be interleaved.
         */
        
        /**
         * Read audio samples from the stream into a Datagram.  N is the number of
         * samples you wish to read.  Multiple-channel audio will be interleaved.
         *
         * This is not particularly efficient, but it may be a convenient way to
         * manipulate samples in python.
         */
        
        /**
         * Read audio samples from the stream and returns them as a string.  The
         * samples are stored little-endian in the string.  N is the number of samples
         * you wish to read.  Multiple-channel audio will be interleaved.
         *
         * This is not particularly efficient, but it may be a convenient way to
         * manipulate samples in python.
         */
        """
        pass

    def seek(self, const_MovieAudioCursor_self, double_offset): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        seek(const MovieAudioCursor self, double offset)
        
        /**
         * Skips to the specified offset within the file.
         *
         * If the movie reports that it cannot seek, then this method can still
         * advance by reading samples and discarding them.  However, to move backward,
         * can_seek must be true.
         *
         * If the movie reports that it can_seek, it doesn't mean that it can do so
         * quickly.  It may have to rewind the movie and then fast forward to the
         * desired location.  Only if can_seek_fast returns true can seek operations
         * be done in constant time.
         *
         * Seeking may not be precise, because AVI files often have inaccurate
         * indices.  After seeking, tell will indicate that the cursor is at the
         * target location.  However, in truth, the data you read may come from a
         * slightly offset location.
         */
        """
        pass

    def skipSamples(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        skip_samples(const MovieAudioCursor self, int n)
        
        /**
         * Skip audio samples from the stream.  This is mostly for debugging purposes.
         */
        """
        pass

    def skip_samples(self, const_MovieAudioCursor_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        skip_samples(const MovieAudioCursor self, int n)
        
        /**
         * Skip audio samples from the stream.  This is mostly for debugging purposes.
         */
        """
        pass

    def tell(self, MovieAudioCursor_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        tell(MovieAudioCursor self)
        
        /**
         * Returns the current offset within the file.
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

    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.core.MovieAudioCursor' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.core.MovieAudioCursor' objects>"
        '__doc__': '/**\n * A MovieAudio is actually any source that provides a sequence of audio\n * samples.  That could include an AVI file, a microphone, or an internet TV\n * station.  A MovieAudioCursor is a handle that lets you read data\n * sequentially from a MovieAudio.\n *\n * Thread safety: each individual MovieAudioCursor must be owned and accessed\n * by a single thread.  It is OK for two different threads to open the same\n * file at the same time, as long as they use separate MovieAudioCursor\n * objects.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.MovieAudioCursor' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE2B7F50>'
        'aborted': None, # (!) real value is "<method 'aborted' of 'panda3d.core.MovieAudioCursor' objects>"
        'audioChannels': None, # (!) real value is "<method 'audioChannels' of 'panda3d.core.MovieAudioCursor' objects>"
        'audioRate': None, # (!) real value is "<method 'audioRate' of 'panda3d.core.MovieAudioCursor' objects>"
        'audio_channels': None, # (!) real value is "<method 'audio_channels' of 'panda3d.core.MovieAudioCursor' objects>"
        'audio_rate': None, # (!) real value is "<method 'audio_rate' of 'panda3d.core.MovieAudioCursor' objects>"
        'canSeek': None, # (!) real value is "<method 'canSeek' of 'panda3d.core.MovieAudioCursor' objects>"
        'canSeekFast': None, # (!) real value is "<method 'canSeekFast' of 'panda3d.core.MovieAudioCursor' objects>"
        'can_seek': None, # (!) real value is "<method 'can_seek' of 'panda3d.core.MovieAudioCursor' objects>"
        'can_seek_fast': None, # (!) real value is "<method 'can_seek_fast' of 'panda3d.core.MovieAudioCursor' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE2B7F50>)>'
        'getSource': None, # (!) real value is "<method 'getSource' of 'panda3d.core.MovieAudioCursor' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE2B7F50>)>'
        'get_source': None, # (!) real value is "<method 'get_source' of 'panda3d.core.MovieAudioCursor' objects>"
        'length': None, # (!) real value is "<method 'length' of 'panda3d.core.MovieAudioCursor' objects>"
        'readSamples': None, # (!) real value is "<method 'readSamples' of 'panda3d.core.MovieAudioCursor' objects>"
        'read_samples': None, # (!) real value is "<method 'read_samples' of 'panda3d.core.MovieAudioCursor' objects>"
        'ready': None, # (!) real value is "<method 'ready' of 'panda3d.core.MovieAudioCursor' objects>"
        'seek': None, # (!) real value is "<method 'seek' of 'panda3d.core.MovieAudioCursor' objects>"
        'skipSamples': None, # (!) real value is "<method 'skipSamples' of 'panda3d.core.MovieAudioCursor' objects>"
        'skip_samples': None, # (!) real value is "<method 'skip_samples' of 'panda3d.core.MovieAudioCursor' objects>"
        'tell': None, # (!) real value is "<method 'tell' of 'panda3d.core.MovieAudioCursor' objects>"
    }


