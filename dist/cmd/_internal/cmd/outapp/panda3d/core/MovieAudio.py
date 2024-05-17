# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .TypedWritableReferenceCount import TypedWritableReferenceCount

from .Namable import Namable

class MovieAudio(TypedWritableReferenceCount, Namable):
    """
    /**
     * A MovieAudio is actually any source that provides a sequence of audio
     * samples.  That could include an AVI file, a microphone, or an internet TV
     * station.
     *
     * The difference between a MovieAudio and a MovieAudioCursor is like the
     * difference between a filename and a file handle.  The MovieAudio just
     * indicates a particular movie.  The MovieAudioCursor is what allows access.
     */
    """
    def get(self, const_Filename_name): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get(const Filename name)
        
        /**
         * Obtains a MovieAudio that references a file.  Just calls
         * MovieTypeRegistry::make_audio().
         */
        """
        pass

    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getFilename(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_filename(MovieAudio self)
        
        /**
         * Returns the movie's filename.  A movie is not guaranteed to have a
         * filename, if not, then this function returns a null filename.
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_filename(self, MovieAudio_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_filename(MovieAudio self)
        
        /**
         * Returns the movie's filename.  A movie is not guaranteed to have a
         * filename, if not, then this function returns a null filename.
         */
        """
        pass

    def open(self, const_MovieAudio_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        open(const MovieAudio self)
        
        /**
         * Open this audio, returning a MovieAudioCursor
         */
        """
        pass

    def upcastToNamable(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        upcast_to_Namable(const MovieAudio self)
        
        upcast from MovieAudio to Namable
        """
        pass

    def upcastToTypedWritableReferenceCount(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        upcast_to_TypedWritableReferenceCount(const MovieAudio self)
        
        upcast from MovieAudio to TypedWritableReferenceCount
        """
        pass

    def upcast_to_Namable(self, const_MovieAudio_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        upcast_to_Namable(const MovieAudio self)
        
        upcast from MovieAudio to Namable
        """
        pass

    def upcast_to_TypedWritableReferenceCount(self, const_MovieAudio_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        upcast_to_TypedWritableReferenceCount(const MovieAudio self)
        
        upcast from MovieAudio to TypedWritableReferenceCount
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

    filename = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.core.MovieAudio' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.core.MovieAudio' objects>"
        '__doc__': '/**\n * A MovieAudio is actually any source that provides a sequence of audio\n * samples.  That could include an AVI file, a microphone, or an internet TV\n * station.\n *\n * The difference between a MovieAudio and a MovieAudioCursor is like the\n * difference between a filename and a file handle.  The MovieAudio just\n * indicates a particular movie.  The MovieAudioCursor is what allows access.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.MovieAudio' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE2B7BB0>'
        'filename': None, # (!) real value is "<attribute 'filename' of 'panda3d.core.MovieAudio' objects>"
        'get': None, # (!) real value is '<staticmethod(<built-in method get of type object at 0x00007FFCFE2B7BB0>)>'
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE2B7BB0>)>'
        'getFilename': None, # (!) real value is "<method 'getFilename' of 'panda3d.core.MovieAudio' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE2B7BB0>)>'
        'get_filename': None, # (!) real value is "<method 'get_filename' of 'panda3d.core.MovieAudio' objects>"
        'open': None, # (!) real value is "<method 'open' of 'panda3d.core.MovieAudio' objects>"
        'upcastToNamable': None, # (!) real value is "<method 'upcastToNamable' of 'panda3d.core.MovieAudio' objects>"
        'upcastToTypedWritableReferenceCount': None, # (!) real value is "<method 'upcastToTypedWritableReferenceCount' of 'panda3d.core.MovieAudio' objects>"
        'upcast_to_Namable': None, # (!) real value is "<method 'upcast_to_Namable' of 'panda3d.core.MovieAudio' objects>"
        'upcast_to_TypedWritableReferenceCount': None, # (!) real value is "<method 'upcast_to_TypedWritableReferenceCount' of 'panda3d.core.MovieAudio' objects>"
    }


