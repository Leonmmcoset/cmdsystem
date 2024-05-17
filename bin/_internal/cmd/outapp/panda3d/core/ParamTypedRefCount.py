# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .ParamValueBase import ParamValueBase

class ParamTypedRefCount(ParamValueBase):
    """
    /**
     * A class object for storing specifically objects of type
     * TypedReferenceCount, which is different than TypedWritableReferenceCount.
     */
    """
    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getValue(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_value(ParamTypedRefCount self)
        
        /**
         * Retrieves the value stored in the parameter.
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_value(self, ParamTypedRefCount_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_value(ParamTypedRefCount self)
        
        /**
         * Retrieves the value stored in the parameter.
         */
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__doc__': '/**\n * A class object for storing specifically objects of type\n * TypedReferenceCount, which is different than TypedWritableReferenceCount.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.ParamTypedRefCount' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE3734A0>'
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE3734A0>)>'
        'getValue': None, # (!) real value is "<method 'getValue' of 'panda3d.core.ParamTypedRefCount' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE3734A0>)>'
        'get_value': None, # (!) real value is "<method 'get_value' of 'panda3d.core.ParamTypedRefCount' objects>"
        'value': None, # (!) real value is "<attribute 'value' of 'panda3d.core.ParamTypedRefCount' objects>"
    }


