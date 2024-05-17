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

class MovieVideo(TypedWritableReferenceCount, Namable):
    """
    /**
     * A MovieVideo is actually any source that provides a sequence of video
     * frames.  That could include an AVI file, a digital camera, or an internet
     * TV station.
     *
     * The difference between a MovieVideo and a MovieVideoCursor is like the
     * difference between a filename and a file handle.  The MovieVideo just
     * indicates a particular movie.  The MovieVideoCursor is what allows access.
     */
    """
    def get(self, const_Filename_name): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get(const Filename name)
        
        /**
         * Obtains a MovieVideo that references a file.  Just calls
         * MovieTypeRegistry::make_video().
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
        get_filename(MovieVideo self)
        
        /**
         * Returns the movie's filename.  A movie is not guaranteed to have a
         * filename, if not, then this function returns an empty filename.
         */
        """
        pass

    def getSubfileInfo(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_subfile_info(MovieVideo self)
        
        /**
         * If the movie is to be loaded from a subfile on disk, this returns the
         * subfile info.  Check info.is_empty() to see if this is valid data.
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_filename(self, MovieVideo_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_filename(MovieVideo self)
        
        /**
         * Returns the movie's filename.  A movie is not guaranteed to have a
         * filename, if not, then this function returns an empty filename.
         */
        """
        pass

    def get_subfile_info(self, MovieVideo_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_subfile_info(MovieVideo self)
        
        /**
         * If the movie is to be loaded from a subfile on disk, this returns the
         * subfile info.  Check info.is_empty() to see if this is valid data.
         */
        """
        pass

    def open(self, const_MovieVideo_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        open(const MovieVideo self)
        
        /**
         * Open this video, returning a MovieVideoCursor of the appropriate type.
         * Returns NULL on error.
         */
        """
        pass

    def upcastToNamable(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        upcast_to_Namable(const MovieVideo self)
        
        upcast from MovieVideo to Namable
        """
        pass

    def upcastToTypedWritableReferenceCount(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        upcast_to_TypedWritableReferenceCount(const MovieVideo self)
        
        upcast from MovieVideo to TypedWritableReferenceCount
        """
        pass

    def upcast_to_Namable(self, const_MovieVideo_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        upcast_to_Namable(const MovieVideo self)
        
        upcast from MovieVideo to Namable
        """
        pass

    def upcast_to_TypedWritableReferenceCount(self, const_MovieVideo_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        upcast_to_TypedWritableReferenceCount(const MovieVideo self)
        
        upcast from MovieVideo to TypedWritableReferenceCount
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

    subfile_info = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.core.MovieVideo' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.core.MovieVideo' objects>"
        '__doc__': '/**\n * A MovieVideo is actually any source that provides a sequence of video\n * frames.  That could include an AVI file, a digital camera, or an internet\n * TV station.\n *\n * The difference between a MovieVideo and a MovieVideoCursor is like the\n * difference between a filename and a file handle.  The MovieVideo just\n * indicates a particular movie.  The MovieVideoCursor is what allows access.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.MovieVideo' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE2B82F0>'
        'filename': None, # (!) real value is "<attribute 'filename' of 'panda3d.core.MovieVideo' objects>"
        'get': None, # (!) real value is '<staticmethod(<built-in method get of type object at 0x00007FFCFE2B82F0>)>'
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE2B82F0>)>'
        'getFilename': None, # (!) real value is "<method 'getFilename' of 'panda3d.core.MovieVideo' objects>"
        'getSubfileInfo': None, # (!) real value is "<method 'getSubfileInfo' of 'panda3d.core.MovieVideo' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE2B82F0>)>'
        'get_filename': None, # (!) real value is "<method 'get_filename' of 'panda3d.core.MovieVideo' objects>"
        'get_subfile_info': None, # (!) real value is "<method 'get_subfile_info' of 'panda3d.core.MovieVideo' objects>"
        'open': None, # (!) real value is "<method 'open' of 'panda3d.core.MovieVideo' objects>"
        'subfile_info': None, # (!) real value is "<attribute 'subfile_info' of 'panda3d.core.MovieVideo' objects>"
        'upcastToNamable': None, # (!) real value is "<method 'upcastToNamable' of 'panda3d.core.MovieVideo' objects>"
        'upcastToTypedWritableReferenceCount': None, # (!) real value is "<method 'upcastToTypedWritableReferenceCount' of 'panda3d.core.MovieVideo' objects>"
        'upcast_to_Namable': None, # (!) real value is "<method 'upcast_to_Namable' of 'panda3d.core.MovieVideo' objects>"
        'upcast_to_TypedWritableReferenceCount': None, # (!) real value is "<method 'upcast_to_TypedWritableReferenceCount' of 'panda3d.core.MovieVideo' objects>"
    }


