# encoding: utf-8
# module panda3d.skel
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\skel.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import panda3d.core as __panda3d_core


# Variables with simple values

Dtool_PyNativeInterface = 1

# functions

def Dtool_BorrowThisReference(*args, **kwargs): # real signature unknown
    """
    Used to borrow 'this' pointer (to, from)
    Assumes no ownership.
    """
    pass

# classes

class BasicSkel(__dtoolconfig.DTOOL_SUPER_BASE):
    """
    /**
     * This is the most basic of the skeleton classes.  It stores an integer, and
     * will return it on request.
     *
     * The skeleton classes are intended to help you learn how to add C++ classes
     * to panda.  See also the manual, "Adding C++ Classes to Panda."
     */
    """
    def getValue(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_value(const BasicSkel self)
        
        /**
         * Retreives a value that was previously stored.
         */
        """
        pass

    def getValueAlt(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_value_alt(const BasicSkel self)
        
        /**
         * Retreives a value that was previously stored.  Exact same functionality as
         * get_value, except that this isn't an inline function.
         */
        """
        pass

    def get_value(self, const_BasicSkel_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_value(const BasicSkel self)
        
        /**
         * Retreives a value that was previously stored.
         */
        """
        pass

    def get_value_alt(self, const_BasicSkel_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_value_alt(const BasicSkel self)
        
        /**
         * Retreives a value that was previously stored.  Exact same functionality as
         * get_value, except that this isn't an inline function.
         */
        """
        pass

    def setValue(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_value(const BasicSkel self, int n)
        
        // These inline functions allow you to get and set _value.
        
        /**
         * Stores an integer value.
         */
        """
        pass

    def setValueAlt(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_value_alt(const BasicSkel self, int n)
        
        // These do the same thing as the functions above.
        
        /**
         * Stores an integer value.  Exact same functionality as set_value, except
         * that this isn't an inline function.
         */
        """
        pass

    def set_value(self, const_BasicSkel_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_value(const BasicSkel self, int n)
        
        // These inline functions allow you to get and set _value.
        
        /**
         * Stores an integer value.
         */
        """
        pass

    def set_value_alt(self, const_BasicSkel_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_value_alt(const BasicSkel self, int n)
        
        // These do the same thing as the functions above.
        
        /**
         * Stores an integer value.  Exact same functionality as set_value, except
         * that this isn't an inline function.
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
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.skel.BasicSkel' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.skel.BasicSkel' objects>"
        '__doc__': '/**\n * This is the most basic of the skeleton classes.  It stores an integer, and\n * will return it on request.\n *\n * The skeleton classes are intended to help you learn how to add C++ classes\n * to panda.  See also the manual, "Adding C++ Classes to Panda."\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.skel.BasicSkel' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFDE565D430>'
        'getValue': None, # (!) real value is "<method 'getValue' of 'panda3d.skel.BasicSkel' objects>"
        'getValueAlt': None, # (!) real value is "<method 'getValueAlt' of 'panda3d.skel.BasicSkel' objects>"
        'get_value': None, # (!) real value is "<method 'get_value' of 'panda3d.skel.BasicSkel' objects>"
        'get_value_alt': None, # (!) real value is "<method 'get_value_alt' of 'panda3d.skel.BasicSkel' objects>"
        'setValue': None, # (!) real value is "<method 'setValue' of 'panda3d.skel.BasicSkel' objects>"
        'setValueAlt': None, # (!) real value is "<method 'setValueAlt' of 'panda3d.skel.BasicSkel' objects>"
        'set_value': None, # (!) real value is "<method 'set_value' of 'panda3d.skel.BasicSkel' objects>"
        'set_value_alt': None, # (!) real value is "<method 'set_value_alt' of 'panda3d.skel.BasicSkel' objects>"
    }


class TypedSkel(__panda3d_core.TypedObject):
    """
    /**
     * Skeleton object that inherits from TypedObject.  Stores an integer, and
     * will return it on request.
     *
     * The skeleton classes are intended to help you learn how to add C++ classes
     * to panda.  See also the manual, "Adding C++ Classes to Panda."
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
        get_value(const TypedSkel self)
        
        /**
         * Retreives a value that was previously stored.
         */
        """
        pass

    def getValueAlt(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_value_alt(const TypedSkel self)
        
        /**
         * Retreives a value that was previously stored.  Exact same functionality as
         * get_value, except that this isn't an inline function.
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_value(self, const_TypedSkel_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_value(const TypedSkel self)
        
        /**
         * Retreives a value that was previously stored.
         */
        """
        pass

    def get_value_alt(self, const_TypedSkel_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_value_alt(const TypedSkel self)
        
        /**
         * Retreives a value that was previously stored.  Exact same functionality as
         * get_value, except that this isn't an inline function.
         */
        """
        pass

    def setValue(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_value(const TypedSkel self, int n)
        
        // These inline functions allow you to get and set _value.
        
        /**
         * Stores an integer value.
         */
        """
        pass

    def setValueAlt(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_value_alt(const TypedSkel self, int n)
        
        // These do the same thing as the functions above.
        
        /**
         * Stores an integer value.  Exact same functionality as set_value, except
         * that this isn't an inline function.
         */
        """
        pass

    def set_value(self, const_TypedSkel_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_value(const TypedSkel self, int n)
        
        // These inline functions allow you to get and set _value.
        
        /**
         * Stores an integer value.
         */
        """
        pass

    def set_value_alt(self, const_TypedSkel_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_value_alt(const TypedSkel self, int n)
        
        // These do the same thing as the functions above.
        
        /**
         * Stores an integer value.  Exact same functionality as set_value, except
         * that this isn't an inline function.
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
        '__doc__': '/**\n * Skeleton object that inherits from TypedObject.  Stores an integer, and\n * will return it on request.\n *\n * The skeleton classes are intended to help you learn how to add C++ classes\n * to panda.  See also the manual, "Adding C++ Classes to Panda."\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.skel.TypedSkel' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFDE565D610>'
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFDE565D610>)>'
        'getValue': None, # (!) real value is "<method 'getValue' of 'panda3d.skel.TypedSkel' objects>"
        'getValueAlt': None, # (!) real value is "<method 'getValueAlt' of 'panda3d.skel.TypedSkel' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFDE565D610>)>'
        'get_value': None, # (!) real value is "<method 'get_value' of 'panda3d.skel.TypedSkel' objects>"
        'get_value_alt': None, # (!) real value is "<method 'get_value_alt' of 'panda3d.skel.TypedSkel' objects>"
        'setValue': None, # (!) real value is "<method 'setValue' of 'panda3d.skel.TypedSkel' objects>"
        'setValueAlt': None, # (!) real value is "<method 'setValueAlt' of 'panda3d.skel.TypedSkel' objects>"
        'set_value': None, # (!) real value is "<method 'set_value' of 'panda3d.skel.TypedSkel' objects>"
        'set_value_alt': None, # (!) real value is "<method 'set_value_alt' of 'panda3d.skel.TypedSkel' objects>"
    }


# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x000001837BF79D50>'

__spec__ = None # (!) real value is "ModuleSpec(name='panda3d.skel', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x000001837BF79D50>, origin='C:\\\\Users\\\\leonm\\\\PycharmProjects\\\\LeonRandomPlus\\\\venv\\\\Lib\\\\site-packages\\\\panda3d\\\\skel.cp311-win_amd64.pyd')"

