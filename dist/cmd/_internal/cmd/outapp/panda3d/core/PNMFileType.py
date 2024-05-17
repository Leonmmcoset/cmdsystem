# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .TypedWritable import TypedWritable

class PNMFileType(TypedWritable):
    """
    /**
     * This is the base class of a family of classes that represent particular
     * image file types that PNMImage supports.
     */
    """
    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getExtension(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_extension(PNMFileType self, int n)
        
        /**
         * Returns the nth possible filename extension associated with this particular
         * file type, without a leading dot.
         */
        """
        pass

    def getExtensions(self, *args, **kwargs): # real signature unknown
        pass

    def getName(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_name(PNMFileType self)
        """
        pass

    def getNumExtensions(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_extensions(PNMFileType self)
        
        /**
         * Returns the number of different possible filename extensions associated
         * with this particular file type.
         */
        """
        pass

    def getSuggestedExtension(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_suggested_extension(PNMFileType self)
        
        /**
         * Returns a suitable filename extension (without a leading dot) to suggest
         * for files of this type, or empty string if no suggestions are available.
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_extension(self, PNMFileType_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_extension(PNMFileType self, int n)
        
        /**
         * Returns the nth possible filename extension associated with this particular
         * file type, without a leading dot.
         */
        """
        pass

    def get_extensions(self, *args, **kwargs): # real signature unknown
        pass

    def get_name(self, PNMFileType_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_name(PNMFileType self)
        """
        pass

    def get_num_extensions(self, PNMFileType_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_extensions(PNMFileType self)
        
        /**
         * Returns the number of different possible filename extensions associated
         * with this particular file type.
         */
        """
        pass

    def get_suggested_extension(self, PNMFileType_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_suggested_extension(PNMFileType self)
        
        /**
         * Returns a suitable filename extension (without a leading dot) to suggest
         * for files of this type, or empty string if no suggestions are available.
         */
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    extensions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    suggested_extension = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__doc__': '/**\n * This is the base class of a family of classes that represent particular\n * image file types that PNMImage supports.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.PNMFileType' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE3555B0>'
        'extensions': None, # (!) real value is "<attribute 'extensions' of 'panda3d.core.PNMFileType' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE3555B0>)>'
        'getExtension': None, # (!) real value is "<method 'getExtension' of 'panda3d.core.PNMFileType' objects>"
        'getExtensions': None, # (!) real value is "<method 'getExtensions' of 'panda3d.core.PNMFileType' objects>"
        'getName': None, # (!) real value is "<method 'getName' of 'panda3d.core.PNMFileType' objects>"
        'getNumExtensions': None, # (!) real value is "<method 'getNumExtensions' of 'panda3d.core.PNMFileType' objects>"
        'getSuggestedExtension': None, # (!) real value is "<method 'getSuggestedExtension' of 'panda3d.core.PNMFileType' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE3555B0>)>'
        'get_extension': None, # (!) real value is "<method 'get_extension' of 'panda3d.core.PNMFileType' objects>"
        'get_extensions': None, # (!) real value is "<method 'get_extensions' of 'panda3d.core.PNMFileType' objects>"
        'get_name': None, # (!) real value is "<method 'get_name' of 'panda3d.core.PNMFileType' objects>"
        'get_num_extensions': None, # (!) real value is "<method 'get_num_extensions' of 'panda3d.core.PNMFileType' objects>"
        'get_suggested_extension': None, # (!) real value is "<method 'get_suggested_extension' of 'panda3d.core.PNMFileType' objects>"
        'name': None, # (!) real value is "<attribute 'name' of 'panda3d.core.PNMFileType' objects>"
        'suggested_extension': None, # (!) real value is "<attribute 'suggested_extension' of 'panda3d.core.PNMFileType' objects>"
    }


