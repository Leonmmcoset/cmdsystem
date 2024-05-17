# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .TypedObject import TypedObject

class CallbackData(TypedObject):
    """
    /**
     * This is a generic data block that is passed along to a CallbackObject when
     * a callback is made.  It contains data specific to the particular callback
     * type in question.
     *
     * This is actually an abstract base class and contains no data.
     * Specializations of this class will contain the actual data relevant to each
     * callback type.
     */
    """
    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def output(self, CallbackData_self, ostream_out): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        output(CallbackData self, ostream out)
        
        /**
         *
         */
        """
        pass

    def upcall(self, const_CallbackData_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        upcall(const CallbackData self)
        
        /**
         * You should make this call during the callback if you want to continue the
         * normal function that would have been done in the absence of a callback.
         */
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
        '__doc__': '/**\n * This is a generic data block that is passed along to a CallbackObject when\n * a callback is made.  It contains data specific to the particular callback\n * type in question.\n *\n * This is actually an abstract base class and contains no data.\n * Specializations of this class will contain the actual data relevant to each\n * callback type.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.CallbackData' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE371400>'
        '__repr__': None, # (!) real value is "<slot wrapper '__repr__' of 'panda3d.core.CallbackData' objects>"
        '__str__': None, # (!) real value is "<slot wrapper '__str__' of 'panda3d.core.CallbackData' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE371400>)>'
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE371400>)>'
        'output': None, # (!) real value is "<method 'output' of 'panda3d.core.CallbackData' objects>"
        'upcall': None, # (!) real value is "<method 'upcall' of 'panda3d.core.CallbackData' objects>"
    }


