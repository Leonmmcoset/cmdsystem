# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


class EventParameter(__dtoolconfig.DTOOL_SUPER_BASE):
    """
    /**
     * An optional parameter associated with an event.  Each event may have zero
     * or more of these.  Each parameter stores a pointer to a
     * TypedWritableReferenceCount object, which of course could be pretty much
     * anything.  To store a simple value like a double or a string, the
     * EventParameter constructors transparently use the ParamValue template class
     * from paramValue.h.
     */
    """
    def assign(self, const_EventParameter_self, const_EventParameter_copy): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        assign(const EventParameter self, const EventParameter copy)
        
        /**
         *
         */
        """
        pass

    def getDoubleValue(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_double_value(EventParameter self)
        
        /**
         * Retrieves the value stored in the EventParameter.  It is only valid to call
         * this if is_double() has already returned true.
         */
        """
        pass

    def getIntValue(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_int_value(EventParameter self)
        
        /**
         * Retrieves the value stored in the EventParameter.  It is only valid to call
         * this if is_int() has already returned true.
         */
        """
        pass

    def getPtr(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_ptr(EventParameter self)
        
        /**
         * Retrieves a pointer to the actual value stored in the parameter.  The
         * TypeHandle of this pointer may be examined to determine the actual type of
         * parameter it contains.  This is the only way to retrieve the value when it
         * is not one of the above predefined types.
         */
        """
        pass

    def getStringValue(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_string_value(EventParameter self)
        
        /**
         * Retrieves the value stored in the EventParameter.  It is only valid to call
         * this if is_string() has already returned true.
         */
        """
        pass

    def getTypedRefCountValue(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_typed_ref_count_value(EventParameter self)
        
        /**
         * Retrieves the value stored in the EventParameter.  It is only valid to call
         * this if is_typed_ref_count() has already returned true.
         */
        """
        pass

    def getWstringValue(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_wstring_value(EventParameter self)
        
        /**
         * Retrieves the value stored in the EventParameter.  It is only valid to call
         * this if is_wstring() has already returned true.
         */
        """
        pass

    def get_double_value(self, EventParameter_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_double_value(EventParameter self)
        
        /**
         * Retrieves the value stored in the EventParameter.  It is only valid to call
         * this if is_double() has already returned true.
         */
        """
        pass

    def get_int_value(self, EventParameter_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_int_value(EventParameter self)
        
        /**
         * Retrieves the value stored in the EventParameter.  It is only valid to call
         * this if is_int() has already returned true.
         */
        """
        pass

    def get_ptr(self, EventParameter_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_ptr(EventParameter self)
        
        /**
         * Retrieves a pointer to the actual value stored in the parameter.  The
         * TypeHandle of this pointer may be examined to determine the actual type of
         * parameter it contains.  This is the only way to retrieve the value when it
         * is not one of the above predefined types.
         */
        """
        pass

    def get_string_value(self, EventParameter_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_string_value(EventParameter self)
        
        /**
         * Retrieves the value stored in the EventParameter.  It is only valid to call
         * this if is_string() has already returned true.
         */
        """
        pass

    def get_typed_ref_count_value(self, EventParameter_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_typed_ref_count_value(EventParameter self)
        
        /**
         * Retrieves the value stored in the EventParameter.  It is only valid to call
         * this if is_typed_ref_count() has already returned true.
         */
        """
        pass

    def get_wstring_value(self, EventParameter_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_wstring_value(EventParameter self)
        
        /**
         * Retrieves the value stored in the EventParameter.  It is only valid to call
         * this if is_wstring() has already returned true.
         */
        """
        pass

    def isDouble(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_double(EventParameter self)
        
        /**
         * Returns true if the EventParameter stores a double floating-point value,
         * false otherwise.
         */
        """
        pass

    def isEmpty(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_empty(EventParameter self)
        
        // These functions are conveniences to easily determine if the
        // EventParameter is one of the predefined parameter types, and retrieve the
        // corresponding value.  Of course, it is possible that the EventParameter
        // is some user-defined type, and is none of these.
        
        /**
         * Returns true if the EventParameter is the empty parameter, storing nothing,
         * or false otherwise.
         */
        """
        pass

    def isInt(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_int(EventParameter self)
        
        /**
         * Returns true if the EventParameter stores an integer value, false
         * otherwise.
         */
        """
        pass

    def isString(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_string(EventParameter self)
        
        /**
         * Returns true if the EventParameter stores a string value, false otherwise.
         */
        """
        pass

    def isTypedRefCount(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_typed_ref_count(EventParameter self)
        
        /**
         * Returns true if the EventParameter stores a TypedReferenceCount pointer,
         * false otherwise.  Note that a TypedReferenceCount is not exactly the same
         * kind of pointer as a TypedWritableReferenceCount, hence the need for this
         * separate call.
         */
        """
        pass

    def isWstring(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_wstring(EventParameter self)
        
        /**
         * Returns true if the EventParameter stores a wstring value, false otherwise.
         */
        """
        pass

    def is_double(self, EventParameter_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_double(EventParameter self)
        
        /**
         * Returns true if the EventParameter stores a double floating-point value,
         * false otherwise.
         */
        """
        pass

    def is_empty(self, EventParameter_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_empty(EventParameter self)
        
        // These functions are conveniences to easily determine if the
        // EventParameter is one of the predefined parameter types, and retrieve the
        // corresponding value.  Of course, it is possible that the EventParameter
        // is some user-defined type, and is none of these.
        
        /**
         * Returns true if the EventParameter is the empty parameter, storing nothing,
         * or false otherwise.
         */
        """
        pass

    def is_int(self, EventParameter_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_int(EventParameter self)
        
        /**
         * Returns true if the EventParameter stores an integer value, false
         * otherwise.
         */
        """
        pass

    def is_string(self, EventParameter_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_string(EventParameter self)
        
        /**
         * Returns true if the EventParameter stores a string value, false otherwise.
         */
        """
        pass

    def is_typed_ref_count(self, EventParameter_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_typed_ref_count(EventParameter self)
        
        /**
         * Returns true if the EventParameter stores a TypedReferenceCount pointer,
         * false otherwise.  Note that a TypedReferenceCount is not exactly the same
         * kind of pointer as a TypedWritableReferenceCount, hence the need for this
         * separate call.
         */
        """
        pass

    def is_wstring(self, EventParameter_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_wstring(EventParameter self)
        
        /**
         * Returns true if the EventParameter stores a wstring value, false otherwise.
         */
        """
        pass

    def output(self, EventParameter_self, ostream_out): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        output(EventParameter self, ostream out)
        
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
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.core.EventParameter' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.core.EventParameter' objects>"
        '__doc__': '/**\n * An optional parameter associated with an event.  Each event may have zero\n * or more of these.  Each parameter stores a pointer to a\n * TypedWritableReferenceCount object, which of course could be pretty much\n * anything.  To store a simple value like a double or a string, the\n * EventParameter constructors transparently use the ParamValue template class\n * from paramValue.h.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.EventParameter' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE2EF4D0>'
        '__repr__': None, # (!) real value is "<slot wrapper '__repr__' of 'panda3d.core.EventParameter' objects>"
        '__str__': None, # (!) real value is "<slot wrapper '__str__' of 'panda3d.core.EventParameter' objects>"
        'assign': None, # (!) real value is "<method 'assign' of 'panda3d.core.EventParameter' objects>"
        'getDoubleValue': None, # (!) real value is "<method 'getDoubleValue' of 'panda3d.core.EventParameter' objects>"
        'getIntValue': None, # (!) real value is "<method 'getIntValue' of 'panda3d.core.EventParameter' objects>"
        'getPtr': None, # (!) real value is "<method 'getPtr' of 'panda3d.core.EventParameter' objects>"
        'getStringValue': None, # (!) real value is "<method 'getStringValue' of 'panda3d.core.EventParameter' objects>"
        'getTypedRefCountValue': None, # (!) real value is "<method 'getTypedRefCountValue' of 'panda3d.core.EventParameter' objects>"
        'getWstringValue': None, # (!) real value is "<method 'getWstringValue' of 'panda3d.core.EventParameter' objects>"
        'get_double_value': None, # (!) real value is "<method 'get_double_value' of 'panda3d.core.EventParameter' objects>"
        'get_int_value': None, # (!) real value is "<method 'get_int_value' of 'panda3d.core.EventParameter' objects>"
        'get_ptr': None, # (!) real value is "<method 'get_ptr' of 'panda3d.core.EventParameter' objects>"
        'get_string_value': None, # (!) real value is "<method 'get_string_value' of 'panda3d.core.EventParameter' objects>"
        'get_typed_ref_count_value': None, # (!) real value is "<method 'get_typed_ref_count_value' of 'panda3d.core.EventParameter' objects>"
        'get_wstring_value': None, # (!) real value is "<method 'get_wstring_value' of 'panda3d.core.EventParameter' objects>"
        'isDouble': None, # (!) real value is "<method 'isDouble' of 'panda3d.core.EventParameter' objects>"
        'isEmpty': None, # (!) real value is "<method 'isEmpty' of 'panda3d.core.EventParameter' objects>"
        'isInt': None, # (!) real value is "<method 'isInt' of 'panda3d.core.EventParameter' objects>"
        'isString': None, # (!) real value is "<method 'isString' of 'panda3d.core.EventParameter' objects>"
        'isTypedRefCount': None, # (!) real value is "<method 'isTypedRefCount' of 'panda3d.core.EventParameter' objects>"
        'isWstring': None, # (!) real value is "<method 'isWstring' of 'panda3d.core.EventParameter' objects>"
        'is_double': None, # (!) real value is "<method 'is_double' of 'panda3d.core.EventParameter' objects>"
        'is_empty': None, # (!) real value is "<method 'is_empty' of 'panda3d.core.EventParameter' objects>"
        'is_int': None, # (!) real value is "<method 'is_int' of 'panda3d.core.EventParameter' objects>"
        'is_string': None, # (!) real value is "<method 'is_string' of 'panda3d.core.EventParameter' objects>"
        'is_typed_ref_count': None, # (!) real value is "<method 'is_typed_ref_count' of 'panda3d.core.EventParameter' objects>"
        'is_wstring': None, # (!) real value is "<method 'is_wstring' of 'panda3d.core.EventParameter' objects>"
        'output': None, # (!) real value is "<method 'output' of 'panda3d.core.EventParameter' objects>"
    }


