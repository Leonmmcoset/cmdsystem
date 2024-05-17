# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


class MemoryUsagePointers(__dtoolconfig.DTOOL_SUPER_BASE):
    """
    /**
     * This is a list of pointers returned by a MemoryUsage object in response to
     * some query.
     *
     * Warning: once pointers are stored in a MemoryUsagePointers object, they are
     * reference-counted, and will not be freed until the MemoryUsagePointers
     * object is freed (or clear() is called on the object).  However, they may
     * not even be freed then; pointers may leak once they have been added to this
     * structure.  This is because we don't store enough information in this
     * structure to correctly free the pointers that have been added.  Since this
     * is intended primarily as a debugging tool, this is not a major issue.
     *
     * This class is just a user interface to talk about pointers stored in a
     * MemoryUsage object.  It doesn't even exist when compiled with NDEBUG.
     */
    """
    def clear(self, const_MemoryUsagePointers_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear(const MemoryUsagePointers self)
        
        /**
         * Empties the set of pointers.
         */
        """
        pass

    def getAge(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_age(MemoryUsagePointers self, int n)
        
        /**
         * Returns the age of the nth pointer: the number of seconds elapsed between
         * the time it was allocated and the time it was added to this set via a call
         * to MemoryUsage::get_pointers().
         */
        """
        pass

    def getNumPointers(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_pointers(MemoryUsagePointers self)
        
        /**
         * Returns the number of pointers in the set.
         */
        """
        pass

    def getPointer(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_pointer(MemoryUsagePointers self, int n)
        
        /**
         * Returns the nth pointer of the set.
         */
        """
        pass

    def getPointers(self, *args, **kwargs): # real signature unknown
        pass

    def getPythonPointer(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_python_pointer(MemoryUsagePointers self, int n)
        """
        pass

    def getType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_type(MemoryUsagePointers self, int n)
        
        /**
         * Returns the actual type of the nth pointer, if it is known.
         */
        """
        pass

    def getTypedPointer(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_typed_pointer(MemoryUsagePointers self, int n)
        
        /**
         * Returns the nth pointer of the set, typecast to a TypedObject if possible.
         * If the pointer is not a TypedObject or if the cast cannot be made, returns
         * nullptr.
         */
        """
        pass

    def getTypedPointers(self, *args, **kwargs): # real signature unknown
        pass

    def getTypeName(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_type_name(MemoryUsagePointers self, int n)
        
        /**
         * Returns the type name of the nth pointer, if it is known.
         */
        """
        pass

    def get_age(self, MemoryUsagePointers_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_age(MemoryUsagePointers self, int n)
        
        /**
         * Returns the age of the nth pointer: the number of seconds elapsed between
         * the time it was allocated and the time it was added to this set via a call
         * to MemoryUsage::get_pointers().
         */
        """
        pass

    def get_num_pointers(self, MemoryUsagePointers_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_pointers(MemoryUsagePointers self)
        
        /**
         * Returns the number of pointers in the set.
         */
        """
        pass

    def get_pointer(self, MemoryUsagePointers_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_pointer(MemoryUsagePointers self, int n)
        
        /**
         * Returns the nth pointer of the set.
         */
        """
        pass

    def get_pointers(self, *args, **kwargs): # real signature unknown
        pass

    def get_python_pointer(self, MemoryUsagePointers_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_python_pointer(MemoryUsagePointers self, int n)
        """
        pass

    def get_type(self, MemoryUsagePointers_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_type(MemoryUsagePointers self, int n)
        
        /**
         * Returns the actual type of the nth pointer, if it is known.
         */
        """
        pass

    def get_typed_pointer(self, MemoryUsagePointers_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_typed_pointer(MemoryUsagePointers self, int n)
        
        /**
         * Returns the nth pointer of the set, typecast to a TypedObject if possible.
         * If the pointer is not a TypedObject or if the cast cannot be made, returns
         * nullptr.
         */
        """
        pass

    def get_typed_pointers(self, *args, **kwargs): # real signature unknown
        pass

    def get_type_name(self, MemoryUsagePointers_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_type_name(MemoryUsagePointers self, int n)
        
        /**
         * Returns the type name of the nth pointer, if it is known.
         */
        """
        pass

    def output(self, MemoryUsagePointers_self, ostream_out): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        output(MemoryUsagePointers self, ostream out)
        
        /**
         *
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

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.core.MemoryUsagePointers' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.core.MemoryUsagePointers' objects>"
        '__doc__': "/**\n * This is a list of pointers returned by a MemoryUsage object in response to\n * some query.\n *\n * Warning: once pointers are stored in a MemoryUsagePointers object, they are\n * reference-counted, and will not be freed until the MemoryUsagePointers\n * object is freed (or clear() is called on the object).  However, they may\n * not even be freed then; pointers may leak once they have been added to this\n * structure.  This is because we don't store enough information in this\n * structure to correctly free the pointers that have been added.  Since this\n * is intended primarily as a debugging tool, this is not a major issue.\n *\n * This class is just a user interface to talk about pointers stored in a\n * MemoryUsage object.  It doesn't even exist when compiled with NDEBUG.\n */",
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.MemoryUsagePointers' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE2787D0>'
        '__repr__': None, # (!) real value is "<slot wrapper '__repr__' of 'panda3d.core.MemoryUsagePointers' objects>"
        '__str__': None, # (!) real value is "<slot wrapper '__str__' of 'panda3d.core.MemoryUsagePointers' objects>"
        'clear': None, # (!) real value is "<method 'clear' of 'panda3d.core.MemoryUsagePointers' objects>"
        'getAge': None, # (!) real value is "<method 'getAge' of 'panda3d.core.MemoryUsagePointers' objects>"
        'getNumPointers': None, # (!) real value is "<method 'getNumPointers' of 'panda3d.core.MemoryUsagePointers' objects>"
        'getPointer': None, # (!) real value is "<method 'getPointer' of 'panda3d.core.MemoryUsagePointers' objects>"
        'getPointers': None, # (!) real value is "<method 'getPointers' of 'panda3d.core.MemoryUsagePointers' objects>"
        'getPythonPointer': None, # (!) real value is "<method 'getPythonPointer' of 'panda3d.core.MemoryUsagePointers' objects>"
        'getType': None, # (!) real value is "<method 'getType' of 'panda3d.core.MemoryUsagePointers' objects>"
        'getTypeName': None, # (!) real value is "<method 'getTypeName' of 'panda3d.core.MemoryUsagePointers' objects>"
        'getTypedPointer': None, # (!) real value is "<method 'getTypedPointer' of 'panda3d.core.MemoryUsagePointers' objects>"
        'getTypedPointers': None, # (!) real value is "<method 'getTypedPointers' of 'panda3d.core.MemoryUsagePointers' objects>"
        'get_age': None, # (!) real value is "<method 'get_age' of 'panda3d.core.MemoryUsagePointers' objects>"
        'get_num_pointers': None, # (!) real value is "<method 'get_num_pointers' of 'panda3d.core.MemoryUsagePointers' objects>"
        'get_pointer': None, # (!) real value is "<method 'get_pointer' of 'panda3d.core.MemoryUsagePointers' objects>"
        'get_pointers': None, # (!) real value is "<method 'get_pointers' of 'panda3d.core.MemoryUsagePointers' objects>"
        'get_python_pointer': None, # (!) real value is "<method 'get_python_pointer' of 'panda3d.core.MemoryUsagePointers' objects>"
        'get_type': None, # (!) real value is "<method 'get_type' of 'panda3d.core.MemoryUsagePointers' objects>"
        'get_type_name': None, # (!) real value is "<method 'get_type_name' of 'panda3d.core.MemoryUsagePointers' objects>"
        'get_typed_pointer': None, # (!) real value is "<method 'get_typed_pointer' of 'panda3d.core.MemoryUsagePointers' objects>"
        'get_typed_pointers': None, # (!) real value is "<method 'get_typed_pointers' of 'panda3d.core.MemoryUsagePointers' objects>"
        'output': None, # (!) real value is "<method 'output' of 'panda3d.core.MemoryUsagePointers' objects>"
    }


