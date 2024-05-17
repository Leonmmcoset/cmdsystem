# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .CallbackObject import CallbackObject

class PythonCallbackObject(CallbackObject):
    """
    /**
     * This is a specialization on CallbackObject to allow a callback to directly
     * call an arbitrary Python function.  Powerful!  But use with caution.
     */
    """
    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getFunction(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_function(const PythonCallbackObject self)
        
        /**
         * Returns the function that is called for the callback.
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_function(self, const_PythonCallbackObject_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_function(const PythonCallbackObject self)
        
        /**
         * Returns the function that is called for the callback.
         */
        """
        pass

    def setFunction(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_function(const PythonCallbackObject self, object function)
        
        /**
         * Replaces the function that is called for the callback.  runs.  The
         * parameter should be a Python callable object.
         */
        """
        pass

    def set_function(self, const_PythonCallbackObject_self, object_function): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_function(const PythonCallbackObject self, object function)
        
        /**
         * Replaces the function that is called for the callback.  runs.  The
         * parameter should be a Python callable object.
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

    function = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.core.PythonCallbackObject' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.core.PythonCallbackObject' objects>"
        '__doc__': '/**\n * This is a specialization on CallbackObject to allow a callback to directly\n * call an arbitrary Python function.  Powerful!  But use with caution.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.PythonCallbackObject' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE3715D0>'
        'function': None, # (!) real value is "<attribute 'function' of 'panda3d.core.PythonCallbackObject' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE3715D0>)>'
        'getFunction': None, # (!) real value is "<method 'getFunction' of 'panda3d.core.PythonCallbackObject' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE3715D0>)>'
        'get_function': None, # (!) real value is "<method 'get_function' of 'panda3d.core.PythonCallbackObject' objects>"
        'setFunction': None, # (!) real value is "<method 'setFunction' of 'panda3d.core.PythonCallbackObject' objects>"
        'set_function': None, # (!) real value is "<method 'set_function' of 'panda3d.core.PythonCallbackObject' objects>"
    }


