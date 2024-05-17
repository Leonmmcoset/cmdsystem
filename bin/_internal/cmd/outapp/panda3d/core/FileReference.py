# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .TypedReferenceCount import TypedReferenceCount

class FileReference(TypedReferenceCount):
    """
    /**
     * Keeps a reference-counted pointer to a file on disk.  As long as the
     * FileReference is held, someone presumably has a use for this file.
     */
    """
    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getFilename(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_filename(FileReference self)
        
        /**
         * Returns the filename of the reference.
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_filename(self, FileReference_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_filename(FileReference self)
        
        /**
         * Returns the filename of the reference.
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
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.core.FileReference' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.core.FileReference' objects>"
        '__doc__': '/**\n * Keeps a reference-counted pointer to a file on disk.  As long as the\n * FileReference is held, someone presumably has a use for this file.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.FileReference' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE278090>'
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE278090>)>'
        'getFilename': None, # (!) real value is "<method 'getFilename' of 'panda3d.core.FileReference' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE278090>)>'
        'get_filename': None, # (!) real value is "<method 'get_filename' of 'panda3d.core.FileReference' objects>"
    }


