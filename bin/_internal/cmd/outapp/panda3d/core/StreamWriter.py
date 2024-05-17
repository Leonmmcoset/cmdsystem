# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


class StreamWriter(__dtoolconfig.DTOOL_SUPER_BASE):
    """
    /**
     * A StreamWriter object is used to write sequential binary data directly to
     * an ostream.  Its interface is very similar to Datagram by design; it's
     * primarily intended as a convenience to eliminate the overhead of writing
     * bytes to a Datagram and then writing the Datagram to a stream.
     */
    """
    def addBeFloat32(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_be_float32(const StreamWriter self, float value)
        
        /**
         * Adds a 32-bit single-precision big-endian floating-point number to the
         * stream.  Since this kind of float is not necessarily portable across
         * different architectures, special care is required.
         */
        """
        pass

    def addBeFloat64(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_be_float64(const StreamWriter self, double value)
        
        /**
         * Adds a 64-bit big-endian floating-point number to the streamWriter.
         */
        """
        pass

    def addBeInt16(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_be_int16(const StreamWriter self, int value)
        
        // These functions pack numbers big-endian, in case that's desired.
        
        /**
         * Adds a signed 16-bit big-endian integer to the streamWriter.
         */
        """
        pass

    def addBeInt32(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_be_int32(const StreamWriter self, int value)
        
        /**
         * Adds a signed 32-bit big-endian integer to the streamWriter.
         */
        """
        pass

    def addBeInt64(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_be_int64(const StreamWriter self, long value)
        
        /**
         * Adds a signed 64-bit big-endian integer to the streamWriter.
         */
        """
        pass

    def addBeUint16(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_be_uint16(const StreamWriter self, int value)
        
        /**
         * Adds an unsigned 16-bit big-endian integer to the streamWriter.
         */
        """
        pass

    def addBeUint32(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_be_uint32(const StreamWriter self, int value)
        
        /**
         * Adds an unsigned 32-bit big-endian integer to the streamWriter.
         */
        """
        pass

    def addBeUint64(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_be_uint64(const StreamWriter self, long value)
        
        /**
         * Adds an unsigned 64-bit big-endian integer to the streamWriter.
         */
        """
        pass

    def addBool(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_bool(const StreamWriter self, bool value)
        
        /**
         * Adds a boolean value to the stream.
         */
        """
        pass

    def addFixedString(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_fixed_string(const StreamWriter self, str str, int size)
        
        /**
         * Adds a fixed-length string to the stream.  If the string given is less than
         * the requested size, this will pad the string out with zeroes; if it is
         * greater than the requested size, this will silently truncate the string.
         */
        """
        pass

    def addFloat32(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_float32(const StreamWriter self, float value)
        
        /**
         * Adds a 32-bit single-precision floating-point number to the stream.  Since
         * this kind of float is not necessarily portable across different
         * architectures, special care is required.
         */
        """
        pass

    def addFloat64(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_float64(const StreamWriter self, double value)
        
        /**
         * Adds a 64-bit floating-point number to the stream.
         */
        """
        pass

    def addInt16(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_int16(const StreamWriter self, int value)
        
        // The default numeric packing is little-endian.
        
        /**
         * Adds a signed 16-bit integer to the stream.
         */
        """
        pass

    def addInt32(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_int32(const StreamWriter self, int value)
        
        /**
         * Adds a signed 32-bit integer to the stream.
         */
        """
        pass

    def addInt64(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_int64(const StreamWriter self, long value)
        
        /**
         * Adds a signed 64-bit integer to the stream.
         */
        """
        pass

    def addInt8(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_int8(const StreamWriter self, int value)
        
        /**
         * Adds a signed 8-bit integer to the stream.
         */
        """
        pass

    def addString(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_string(const StreamWriter self, str str)
        
        /**
         * Adds a variable-length string to the stream.  This actually adds a count
         * followed by n bytes.
         */
        """
        pass

    def addString32(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_string32(const StreamWriter self, str str)
        
        /**
         * Adds a variable-length string to the stream, using a 32-bit length field.
         */
        """
        pass

    def addUint16(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_uint16(const StreamWriter self, int value)
        
        /**
         * Adds an unsigned 16-bit integer to the stream.
         */
        """
        pass

    def addUint32(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_uint32(const StreamWriter self, int value)
        
        /**
         * Adds an unsigned 32-bit integer to the stream.
         */
        """
        pass

    def addUint64(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_uint64(const StreamWriter self, long value)
        
        /**
         * Adds an unsigned 64-bit integer to the stream.
         */
        """
        pass

    def addUint8(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_uint8(const StreamWriter self, int value)
        
        /**
         * Adds an unsigned 8-bit integer to the stream.
         */
        """
        pass

    def addZString(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_z_string(const StreamWriter self, str str)
        
        /**
         * Adds a variable-length string to the stream, as a NULL-terminated string.
         */
        """
        pass

    def add_be_float32(self, const_StreamWriter_self, float_value): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_be_float32(const StreamWriter self, float value)
        
        /**
         * Adds a 32-bit single-precision big-endian floating-point number to the
         * stream.  Since this kind of float is not necessarily portable across
         * different architectures, special care is required.
         */
        """
        pass

    def add_be_float64(self, const_StreamWriter_self, double_value): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_be_float64(const StreamWriter self, double value)
        
        /**
         * Adds a 64-bit big-endian floating-point number to the streamWriter.
         */
        """
        pass

    def add_be_int16(self, const_StreamWriter_self, int_value): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_be_int16(const StreamWriter self, int value)
        
        // These functions pack numbers big-endian, in case that's desired.
        
        /**
         * Adds a signed 16-bit big-endian integer to the streamWriter.
         */
        """
        pass

    def add_be_int32(self, const_StreamWriter_self, int_value): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_be_int32(const StreamWriter self, int value)
        
        /**
         * Adds a signed 32-bit big-endian integer to the streamWriter.
         */
        """
        pass

    def add_be_int64(self, const_StreamWriter_self, long_value): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_be_int64(const StreamWriter self, long value)
        
        /**
         * Adds a signed 64-bit big-endian integer to the streamWriter.
         */
        """
        pass

    def add_be_uint16(self, const_StreamWriter_self, int_value): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_be_uint16(const StreamWriter self, int value)
        
        /**
         * Adds an unsigned 16-bit big-endian integer to the streamWriter.
         */
        """
        pass

    def add_be_uint32(self, const_StreamWriter_self, int_value): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_be_uint32(const StreamWriter self, int value)
        
        /**
         * Adds an unsigned 32-bit big-endian integer to the streamWriter.
         */
        """
        pass

    def add_be_uint64(self, const_StreamWriter_self, long_value): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_be_uint64(const StreamWriter self, long value)
        
        /**
         * Adds an unsigned 64-bit big-endian integer to the streamWriter.
         */
        """
        pass

    def add_bool(self, const_StreamWriter_self, bool_value): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_bool(const StreamWriter self, bool value)
        
        /**
         * Adds a boolean value to the stream.
         */
        """
        pass

    def add_fixed_string(self, const_StreamWriter_self, str_str, int_size): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_fixed_string(const StreamWriter self, str str, int size)
        
        /**
         * Adds a fixed-length string to the stream.  If the string given is less than
         * the requested size, this will pad the string out with zeroes; if it is
         * greater than the requested size, this will silently truncate the string.
         */
        """
        pass

    def add_float32(self, const_StreamWriter_self, float_value): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_float32(const StreamWriter self, float value)
        
        /**
         * Adds a 32-bit single-precision floating-point number to the stream.  Since
         * this kind of float is not necessarily portable across different
         * architectures, special care is required.
         */
        """
        pass

    def add_float64(self, const_StreamWriter_self, double_value): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_float64(const StreamWriter self, double value)
        
        /**
         * Adds a 64-bit floating-point number to the stream.
         */
        """
        pass

    def add_int16(self, const_StreamWriter_self, int_value): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_int16(const StreamWriter self, int value)
        
        // The default numeric packing is little-endian.
        
        /**
         * Adds a signed 16-bit integer to the stream.
         */
        """
        pass

    def add_int32(self, const_StreamWriter_self, int_value): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_int32(const StreamWriter self, int value)
        
        /**
         * Adds a signed 32-bit integer to the stream.
         */
        """
        pass

    def add_int64(self, const_StreamWriter_self, long_value): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_int64(const StreamWriter self, long value)
        
        /**
         * Adds a signed 64-bit integer to the stream.
         */
        """
        pass

    def add_int8(self, const_StreamWriter_self, int_value): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_int8(const StreamWriter self, int value)
        
        /**
         * Adds a signed 8-bit integer to the stream.
         */
        """
        pass

    def add_string(self, const_StreamWriter_self, str_str): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_string(const StreamWriter self, str str)
        
        /**
         * Adds a variable-length string to the stream.  This actually adds a count
         * followed by n bytes.
         */
        """
        pass

    def add_string32(self, const_StreamWriter_self, str_str): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_string32(const StreamWriter self, str str)
        
        /**
         * Adds a variable-length string to the stream, using a 32-bit length field.
         */
        """
        pass

    def add_uint16(self, const_StreamWriter_self, int_value): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_uint16(const StreamWriter self, int value)
        
        /**
         * Adds an unsigned 16-bit integer to the stream.
         */
        """
        pass

    def add_uint32(self, const_StreamWriter_self, int_value): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_uint32(const StreamWriter self, int value)
        
        /**
         * Adds an unsigned 32-bit integer to the stream.
         */
        """
        pass

    def add_uint64(self, const_StreamWriter_self, long_value): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_uint64(const StreamWriter self, long value)
        
        /**
         * Adds an unsigned 64-bit integer to the stream.
         */
        """
        pass

    def add_uint8(self, const_StreamWriter_self, int_value): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_uint8(const StreamWriter self, int value)
        
        /**
         * Adds an unsigned 8-bit integer to the stream.
         */
        """
        pass

    def add_z_string(self, const_StreamWriter_self, str_str): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_z_string(const StreamWriter self, str str)
        
        /**
         * Adds a variable-length string to the stream, as a NULL-terminated string.
         */
        """
        pass

    def appendData(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        append_data(const StreamWriter self, object data)
        
        /**
         * Appends some more raw data to the end of the streamWriter.
         */
        
        /**
         * Appends some more raw data to the end of the streamWriter.
         */
        """
        pass

    def append_data(self, const_StreamWriter_self, object_data): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        append_data(const StreamWriter self, object data)
        
        /**
         * Appends some more raw data to the end of the streamWriter.
         */
        
        /**
         * Appends some more raw data to the end of the streamWriter.
         */
        """
        pass

    def assign(self, const_StreamWriter_self, const_StreamWriter_copy): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        assign(const StreamWriter self, const StreamWriter copy)
        """
        pass

    def flush(self, const_StreamWriter_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        flush(const StreamWriter self)
        
        /**
         * Calls flush() on the underlying stream.
         */
        """
        pass

    def getOstream(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_ostream(StreamWriter self)
        
        /**
         * Returns the stream in use.
         */
        """
        pass

    def get_ostream(self, StreamWriter_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_ostream(StreamWriter self)
        
        /**
         * Returns the stream in use.
         */
        """
        pass

    def padBytes(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        pad_bytes(const StreamWriter self, int size)
        
        /**
         * Adds the indicated number of zero bytes to the stream.
         */
        """
        pass

    def pad_bytes(self, const_StreamWriter_self, int_size): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        pad_bytes(const StreamWriter self, int size)
        
        /**
         * Adds the indicated number of zero bytes to the stream.
         */
        """
        pass

    def write(self, const_StreamWriter_self, str_str): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        write(const StreamWriter self, str str)
        
        /**
         * A synonym of append_data().  This is useful when assigning the StreamWriter
         * to sys.stderr and/or sys.stdout in Python.
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

    ostream = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    softspace = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """// Python 2 needs this for printing to work correctly."""


    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.core.StreamWriter' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.core.StreamWriter' objects>"
        '__doc__': "/**\n * A StreamWriter object is used to write sequential binary data directly to\n * an ostream.  Its interface is very similar to Datagram by design; it's\n * primarily intended as a convenience to eliminate the overhead of writing\n * bytes to a Datagram and then writing the Datagram to a stream.\n */",
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.StreamWriter' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE2646C0>'
        'addBeFloat32': None, # (!) real value is "<method 'addBeFloat32' of 'panda3d.core.StreamWriter' objects>"
        'addBeFloat64': None, # (!) real value is "<method 'addBeFloat64' of 'panda3d.core.StreamWriter' objects>"
        'addBeInt16': None, # (!) real value is "<method 'addBeInt16' of 'panda3d.core.StreamWriter' objects>"
        'addBeInt32': None, # (!) real value is "<method 'addBeInt32' of 'panda3d.core.StreamWriter' objects>"
        'addBeInt64': None, # (!) real value is "<method 'addBeInt64' of 'panda3d.core.StreamWriter' objects>"
        'addBeUint16': None, # (!) real value is "<method 'addBeUint16' of 'panda3d.core.StreamWriter' objects>"
        'addBeUint32': None, # (!) real value is "<method 'addBeUint32' of 'panda3d.core.StreamWriter' objects>"
        'addBeUint64': None, # (!) real value is "<method 'addBeUint64' of 'panda3d.core.StreamWriter' objects>"
        'addBool': None, # (!) real value is "<method 'addBool' of 'panda3d.core.StreamWriter' objects>"
        'addFixedString': None, # (!) real value is "<method 'addFixedString' of 'panda3d.core.StreamWriter' objects>"
        'addFloat32': None, # (!) real value is "<method 'addFloat32' of 'panda3d.core.StreamWriter' objects>"
        'addFloat64': None, # (!) real value is "<method 'addFloat64' of 'panda3d.core.StreamWriter' objects>"
        'addInt16': None, # (!) real value is "<method 'addInt16' of 'panda3d.core.StreamWriter' objects>"
        'addInt32': None, # (!) real value is "<method 'addInt32' of 'panda3d.core.StreamWriter' objects>"
        'addInt64': None, # (!) real value is "<method 'addInt64' of 'panda3d.core.StreamWriter' objects>"
        'addInt8': None, # (!) real value is "<method 'addInt8' of 'panda3d.core.StreamWriter' objects>"
        'addString': None, # (!) real value is "<method 'addString' of 'panda3d.core.StreamWriter' objects>"
        'addString32': None, # (!) real value is "<method 'addString32' of 'panda3d.core.StreamWriter' objects>"
        'addUint16': None, # (!) real value is "<method 'addUint16' of 'panda3d.core.StreamWriter' objects>"
        'addUint32': None, # (!) real value is "<method 'addUint32' of 'panda3d.core.StreamWriter' objects>"
        'addUint64': None, # (!) real value is "<method 'addUint64' of 'panda3d.core.StreamWriter' objects>"
        'addUint8': None, # (!) real value is "<method 'addUint8' of 'panda3d.core.StreamWriter' objects>"
        'addZString': None, # (!) real value is "<method 'addZString' of 'panda3d.core.StreamWriter' objects>"
        'add_be_float32': None, # (!) real value is "<method 'add_be_float32' of 'panda3d.core.StreamWriter' objects>"
        'add_be_float64': None, # (!) real value is "<method 'add_be_float64' of 'panda3d.core.StreamWriter' objects>"
        'add_be_int16': None, # (!) real value is "<method 'add_be_int16' of 'panda3d.core.StreamWriter' objects>"
        'add_be_int32': None, # (!) real value is "<method 'add_be_int32' of 'panda3d.core.StreamWriter' objects>"
        'add_be_int64': None, # (!) real value is "<method 'add_be_int64' of 'panda3d.core.StreamWriter' objects>"
        'add_be_uint16': None, # (!) real value is "<method 'add_be_uint16' of 'panda3d.core.StreamWriter' objects>"
        'add_be_uint32': None, # (!) real value is "<method 'add_be_uint32' of 'panda3d.core.StreamWriter' objects>"
        'add_be_uint64': None, # (!) real value is "<method 'add_be_uint64' of 'panda3d.core.StreamWriter' objects>"
        'add_bool': None, # (!) real value is "<method 'add_bool' of 'panda3d.core.StreamWriter' objects>"
        'add_fixed_string': None, # (!) real value is "<method 'add_fixed_string' of 'panda3d.core.StreamWriter' objects>"
        'add_float32': None, # (!) real value is "<method 'add_float32' of 'panda3d.core.StreamWriter' objects>"
        'add_float64': None, # (!) real value is "<method 'add_float64' of 'panda3d.core.StreamWriter' objects>"
        'add_int16': None, # (!) real value is "<method 'add_int16' of 'panda3d.core.StreamWriter' objects>"
        'add_int32': None, # (!) real value is "<method 'add_int32' of 'panda3d.core.StreamWriter' objects>"
        'add_int64': None, # (!) real value is "<method 'add_int64' of 'panda3d.core.StreamWriter' objects>"
        'add_int8': None, # (!) real value is "<method 'add_int8' of 'panda3d.core.StreamWriter' objects>"
        'add_string': None, # (!) real value is "<method 'add_string' of 'panda3d.core.StreamWriter' objects>"
        'add_string32': None, # (!) real value is "<method 'add_string32' of 'panda3d.core.StreamWriter' objects>"
        'add_uint16': None, # (!) real value is "<method 'add_uint16' of 'panda3d.core.StreamWriter' objects>"
        'add_uint32': None, # (!) real value is "<method 'add_uint32' of 'panda3d.core.StreamWriter' objects>"
        'add_uint64': None, # (!) real value is "<method 'add_uint64' of 'panda3d.core.StreamWriter' objects>"
        'add_uint8': None, # (!) real value is "<method 'add_uint8' of 'panda3d.core.StreamWriter' objects>"
        'add_z_string': None, # (!) real value is "<method 'add_z_string' of 'panda3d.core.StreamWriter' objects>"
        'appendData': None, # (!) real value is "<method 'appendData' of 'panda3d.core.StreamWriter' objects>"
        'append_data': None, # (!) real value is "<method 'append_data' of 'panda3d.core.StreamWriter' objects>"
        'assign': None, # (!) real value is "<method 'assign' of 'panda3d.core.StreamWriter' objects>"
        'flush': None, # (!) real value is "<method 'flush' of 'panda3d.core.StreamWriter' objects>"
        'getOstream': None, # (!) real value is "<method 'getOstream' of 'panda3d.core.StreamWriter' objects>"
        'get_ostream': None, # (!) real value is "<method 'get_ostream' of 'panda3d.core.StreamWriter' objects>"
        'ostream': None, # (!) real value is "<attribute 'ostream' of 'panda3d.core.StreamWriter' objects>"
        'padBytes': None, # (!) real value is "<method 'padBytes' of 'panda3d.core.StreamWriter' objects>"
        'pad_bytes': None, # (!) real value is "<method 'pad_bytes' of 'panda3d.core.StreamWriter' objects>"
        'softspace': None, # (!) real value is "<attribute 'softspace' of 'panda3d.core.StreamWriter' objects>"
        'write': None, # (!) real value is "<method 'write' of 'panda3d.core.StreamWriter' objects>"
    }


