# encoding: utf-8
# module panda3d.egg
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\egg.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import panda3d.core as __panda3d_core


class EggObject(__panda3d_core.TypedReferenceCount):
    """
    /**
     * The highest-level base class in the egg directory.  (Almost) all things egg
     * inherit from this.
     */
    """
    def assign(self, const_EggObject_self, const_EggObject_copy): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        assign(const EggObject self, const EggObject copy)
        
        /**
         *
         */
        """
        pass

    def clearUserData(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_user_data(const EggObject self)
        clear_user_data(const EggObject self, TypeHandle type)
        
        /**
         * Removes *all* user data pointers from the node.
         */
        
        /**
         * Removes the user data pointer of the indicated type.
         */
        """
        pass

    def clear_user_data(self, const_EggObject_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_user_data(const EggObject self)
        clear_user_data(const EggObject self, TypeHandle type)
        
        /**
         * Removes *all* user data pointers from the node.
         */
        
        /**
         * Removes the user data pointer of the indicated type.
         */
        """
        pass

    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getUserData(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_user_data(EggObject self)
        get_user_data(EggObject self, TypeHandle type)
        
        /**
         * Returns the user data pointer most recently stored on this object, or NULL
         * if nothing was previously stored.
         */
        
        /**
         * Returns the user data pointer of the indicated type, if it exists, or NULL
         * if it does not.
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_user_data(self, EggObject_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_user_data(EggObject self)
        get_user_data(EggObject self, TypeHandle type)
        
        /**
         * Returns the user data pointer most recently stored on this object, or NULL
         * if nothing was previously stored.
         */
        
        /**
         * Returns the user data pointer of the indicated type, if it exists, or NULL
         * if it does not.
         */
        """
        pass

    def hasUserData(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_user_data(EggObject self)
        has_user_data(EggObject self, TypeHandle type)
        
        /**
         * Returns true if a generic user data pointer has recently been set and not
         * yet cleared, false otherwise.
         */
        
        /**
         * Returns true if the user data pointer of the indicated type has been set,
         * false otherwise.
         */
        """
        pass

    def has_user_data(self, EggObject_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_user_data(EggObject self)
        has_user_data(EggObject self, TypeHandle type)
        
        /**
         * Returns true if a generic user data pointer has recently been set and not
         * yet cleared, false otherwise.
         */
        
        /**
         * Returns true if the user data pointer of the indicated type has been set,
         * false otherwise.
         */
        """
        pass

    def setUserData(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_user_data(const EggObject self, EggUserData user_data)
        
        /**
         * Sets the user data associated with this object.  This may be any
         * EggUserData-derived object.  The egg library will do nothing with this
         * pointer, except to hold its reference count and return the pointer on
         * request.
         *
         * The EggObject maintains multiple different EggUserData pointers, one for
         * each unique type (as reported by get_type()).  If you know that only one
         * type of EggUserData object will be added in your application, you may use
         * the query functions that accept no parameters, but it is recommended that
         * in general you pass in the type of your particular user data, to allow
         * multiple applications to coexist in the same egg data.
         *
         * This pointer is also copied by the copy assignment operator and copy
         * constructor.
         */
        """
        pass

    def set_user_data(self, const_EggObject_self, EggUserData_user_data): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_user_data(const EggObject self, EggUserData user_data)
        
        /**
         * Sets the user data associated with this object.  This may be any
         * EggUserData-derived object.  The egg library will do nothing with this
         * pointer, except to hold its reference count and return the pointer on
         * request.
         *
         * The EggObject maintains multiple different EggUserData pointers, one for
         * each unique type (as reported by get_type()).  If you know that only one
         * type of EggUserData object will be added in your application, you may use
         * the query functions that accept no parameters, but it is recommended that
         * in general you pass in the type of your particular user data, to allow
         * multiple applications to coexist in the same egg data.
         *
         * This pointer is also copied by the copy assignment operator and copy
         * constructor.
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
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.egg.EggObject' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.egg.EggObject' objects>"
        '__doc__': '/**\n * The highest-level base class in the egg directory.  (Almost) all things egg\n * inherit from this.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.egg.EggObject' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFDC68CC780>'
        'assign': None, # (!) real value is "<method 'assign' of 'panda3d.egg.EggObject' objects>"
        'clearUserData': None, # (!) real value is "<method 'clearUserData' of 'panda3d.egg.EggObject' objects>"
        'clear_user_data': None, # (!) real value is "<method 'clear_user_data' of 'panda3d.egg.EggObject' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFDC68CC780>)>'
        'getUserData': None, # (!) real value is "<method 'getUserData' of 'panda3d.egg.EggObject' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFDC68CC780>)>'
        'get_user_data': None, # (!) real value is "<method 'get_user_data' of 'panda3d.egg.EggObject' objects>"
        'hasUserData': None, # (!) real value is "<method 'hasUserData' of 'panda3d.egg.EggObject' objects>"
        'has_user_data': None, # (!) real value is "<method 'has_user_data' of 'panda3d.egg.EggObject' objects>"
        'setUserData': None, # (!) real value is "<method 'setUserData' of 'panda3d.egg.EggObject' objects>"
        'set_user_data': None, # (!) real value is "<method 'set_user_data' of 'panda3d.egg.EggObject' objects>"
    }


