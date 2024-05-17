# encoding: utf-8
# module panda3d.direct
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\direct.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import panda3d.core as __panda3d_core


from .DCField import DCField

class DCParameter(DCField):
    """
    /**
     * Represents the type specification for a single parameter within a field
     * specification.  This may be a simple type, or it may be a class or an array
     * reference.
     *
     * This may also be a typedef reference to another type, which has the same
     * properties as the referenced type, but a different name.
     */
    """
    def asArrayParameter(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        as_array_parameter(const DCParameter self)
        as_array_parameter(DCParameter self)
        
        /**
         *
         */
        
        /**
         *
         */
        """
        pass

    def asSimpleParameter(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        as_simple_parameter(const DCParameter self)
        as_simple_parameter(DCParameter self)
        
        /**
         *
         */
        
        /**
         *
         */
        """
        pass

    def as_array_parameter(self, const_DCParameter_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        as_array_parameter(const DCParameter self)
        as_array_parameter(DCParameter self)
        
        /**
         *
         */
        
        /**
         *
         */
        """
        pass

    def as_simple_parameter(self, const_DCParameter_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        as_simple_parameter(const DCParameter self)
        as_simple_parameter(DCParameter self)
        
        /**
         *
         */
        
        /**
         *
         */
        """
        pass

    def getTypedef(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_typedef(DCParameter self)
        
        /**
         * If this type has been referenced from a typedef, returns the DCTypedef
         * instance, or NULL if the type was declared on-the-fly.
         */
        """
        pass

    def get_typedef(self, DCParameter_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_typedef(DCParameter self)
        
        /**
         * If this type has been referenced from a typedef, returns the DCTypedef
         * instance, or NULL if the type was declared on-the-fly.
         */
        """
        pass

    def isValid(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_valid(DCParameter self)
        """
        pass

    def is_valid(self, DCParameter_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_valid(DCParameter self)
        """
        pass

    def makeCopy(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        make_copy(DCParameter self)
        """
        pass

    def make_copy(self, DCParameter_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        make_copy(DCParameter self)
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
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.direct.DCParameter' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.direct.DCParameter' objects>"
        '__doc__': '/**\n * Represents the type specification for a single parameter within a field\n * specification.  This may be a simple type, or it may be a class or an array\n * reference.\n *\n * This may also be a typedef reference to another type, which has the same\n * properties as the referenced type, but a different name.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.direct.DCParameter' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFDC68DE090>'
        'asArrayParameter': None, # (!) real value is "<method 'asArrayParameter' of 'panda3d.direct.DCParameter' objects>"
        'asSimpleParameter': None, # (!) real value is "<method 'asSimpleParameter' of 'panda3d.direct.DCParameter' objects>"
        'as_array_parameter': None, # (!) real value is "<method 'as_array_parameter' of 'panda3d.direct.DCParameter' objects>"
        'as_simple_parameter': None, # (!) real value is "<method 'as_simple_parameter' of 'panda3d.direct.DCParameter' objects>"
        'getTypedef': None, # (!) real value is "<method 'getTypedef' of 'panda3d.direct.DCParameter' objects>"
        'get_typedef': None, # (!) real value is "<method 'get_typedef' of 'panda3d.direct.DCParameter' objects>"
        'isValid': None, # (!) real value is "<method 'isValid' of 'panda3d.direct.DCParameter' objects>"
        'is_valid': None, # (!) real value is "<method 'is_valid' of 'panda3d.direct.DCParameter' objects>"
        'makeCopy': None, # (!) real value is "<method 'makeCopy' of 'panda3d.direct.DCParameter' objects>"
        'make_copy': None, # (!) real value is "<method 'make_copy' of 'panda3d.direct.DCParameter' objects>"
    }


