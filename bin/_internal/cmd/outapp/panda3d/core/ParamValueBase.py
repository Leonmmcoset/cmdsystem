# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .TypedWritableReferenceCount import TypedWritableReferenceCount

class ParamValueBase(TypedWritableReferenceCount):
    """
    /**
     * A non-template base class of ParamValue (below), which serves mainly to
     * define the placeholder for the virtual output function.
     */
    """
    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getValueType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_value_type(ParamValueBase self)
        
        /**
         * Returns the type of the underlying value.
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_value_type(self, ParamValueBase_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_value_type(ParamValueBase self)
        
        /**
         * Returns the type of the underlying value.
         */
        """
        pass

    def output(self, ParamValueBase_self, ostream_out): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        output(ParamValueBase self, ostream out)
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

    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__doc__': '/**\n * A non-template base class of ParamValue (below), which serves mainly to\n * define the placeholder for the virtual output function.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.ParamValueBase' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE3732D0>'
        '__repr__': None, # (!) real value is "<slot wrapper '__repr__' of 'panda3d.core.ParamValueBase' objects>"
        '__str__': None, # (!) real value is "<slot wrapper '__str__' of 'panda3d.core.ParamValueBase' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE3732D0>)>'
        'getValueType': None, # (!) real value is "<method 'getValueType' of 'panda3d.core.ParamValueBase' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE3732D0>)>'
        'get_value_type': None, # (!) real value is "<method 'get_value_type' of 'panda3d.core.ParamValueBase' objects>"
        'output': None, # (!) real value is "<method 'output' of 'panda3d.core.ParamValueBase' objects>"
    }


