# encoding: utf-8
# module panda3d.direct
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\direct.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import panda3d.core as __panda3d_core


from .DCParameter import DCParameter

class DCArrayParameter(DCParameter):
    """
    /**
     * This represents an array of some other kind of object, meaning this
     * parameter type accepts an arbitrary (or possibly fixed) number of nested
     * fields, all of which are of the same type.
     */
    """
    def getArraySize(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_array_size(DCArrayParameter self)
        
        /**
         * Returns the fixed number of elements in this array, or -1 if the array may
         * contain a variable number of elements.
         */
        """
        pass

    def getElementType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_element_type(DCArrayParameter self)
        
        /**
         * Returns the type of the individual elements of this array.
         */
        """
        pass

    def get_array_size(self, DCArrayParameter_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_array_size(DCArrayParameter self)
        
        /**
         * Returns the fixed number of elements in this array, or -1 if the array may
         * contain a variable number of elements.
         */
        """
        pass

    def get_element_type(self, DCArrayParameter_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_element_type(DCArrayParameter self)
        
        /**
         * Returns the type of the individual elements of this array.
         */
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__doc__': '/**\n * This represents an array of some other kind of object, meaning this\n * parameter type accepts an arbitrary (or possibly fixed) number of nested\n * fields, all of which are of the same type.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.direct.DCArrayParameter' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFDC68DE260>'
        'getArraySize': None, # (!) real value is "<method 'getArraySize' of 'panda3d.direct.DCArrayParameter' objects>"
        'getElementType': None, # (!) real value is "<method 'getElementType' of 'panda3d.direct.DCArrayParameter' objects>"
        'get_array_size': None, # (!) real value is "<method 'get_array_size' of 'panda3d.direct.DCArrayParameter' objects>"
        'get_element_type': None, # (!) real value is "<method 'get_element_type' of 'panda3d.direct.DCArrayParameter' objects>"
    }


