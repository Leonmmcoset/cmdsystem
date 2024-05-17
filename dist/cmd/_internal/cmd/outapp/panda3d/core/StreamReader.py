# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


class StreamReader(__dtoolconfig.DTOOL_SUPER_BASE):
    """
    /**
     * A class to read sequential binary data directly from an istream.  Its
     * interface is similar to DatagramIterator by design; see also StreamWriter.
     */
    """
    def assign(self, const_StreamReader_self, const_StreamReader_copy): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        assign(const StreamReader self, const StreamReader copy)
        """
        pass

    def extractBytes(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        extract_bytes(const StreamReader self, int size)
        
        /**
         * Extracts the indicated number of bytes in the stream into the given
         * character buffer.  Assumes that the buffer is big enough to hold the
         * requested number of bytes.  Returns the number of bytes that were
         * successfully written.
         */
        
        /**
         * Extracts the indicated number of bytes in the stream and returns them as a
         * string.  Returns empty string at end-of-file.
         */
        """
        pass

    def extract_bytes(self, const_StreamReader_self, int_size): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        extract_bytes(const StreamReader self, int size)
        
        /**
         * Extracts the indicated number of bytes in the stream into the given
         * character buffer.  Assumes that the buffer is big enough to hold the
         * requested number of bytes.  Returns the number of bytes that were
         * successfully written.
         */
        
        /**
         * Extracts the indicated number of bytes in the stream and returns them as a
         * string.  Returns empty string at end-of-file.
         */
        """
        pass

    def getBeFloat32(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_be_float32(const StreamReader self)
        
        /**
         * Extracts a 32-bit single-precision big-endian floating-point number.  Since
         * this kind of float is not necessarily portable across different
         * architectures, special care is required.
         */
        """
        pass

    def getBeFloat64(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_be_float64(const StreamReader self)
        
        /**
         * Extracts a 64-bit big-endian floating-point number.
         */
        """
        pass

    def getBeInt16(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_be_int16(const StreamReader self)
        
        /**
         * Extracts a signed big-endian 16-bit integer.
         */
        """
        pass

    def getBeInt32(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_be_int32(const StreamReader self)
        
        /**
         * Extracts a signed big-endian 32-bit integer.
         */
        """
        pass

    def getBeInt64(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_be_int64(const StreamReader self)
        
        /**
         * Extracts a signed big-endian 64-bit integer.
         */
        """
        pass

    def getBeUint16(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_be_uint16(const StreamReader self)
        
        /**
         * Extracts an unsigned big-endian 16-bit integer.
         */
        """
        pass

    def getBeUint32(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_be_uint32(const StreamReader self)
        
        /**
         * Extracts an unsigned big-endian 32-bit integer.
         */
        """
        pass

    def getBeUint64(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_be_uint64(const StreamReader self)
        
        /**
         * Extracts an unsigned big-endian 64-bit integer.
         */
        """
        pass

    def getBool(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_bool(const StreamReader self)
        
        /**
         * Extracts a boolean value.
         */
        """
        pass

    def getFixedString(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_fixed_string(const StreamReader self, int size)
        
        /**
         * Extracts a fixed-length string.  However, if a zero byte occurs within the
         * string, it marks the end of the string.
         */
        """
        pass

    def getFloat32(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_float32(const StreamReader self)
        
        /**
         * Extracts a 32-bit single-precision floating-point number.  Since this kind
         * of float is not necessarily portable across different architectures,
         * special care is required.
         */
        """
        pass

    def getFloat64(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_float64(const StreamReader self)
        
        /**
         * Extracts a 64-bit floating-point number.
         */
        """
        pass

    def getInt16(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_int16(const StreamReader self)
        
        /**
         * Extracts a signed 16-bit integer.
         */
        """
        pass

    def getInt32(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_int32(const StreamReader self)
        
        /**
         * Extracts a signed 32-bit integer.
         */
        """
        pass

    def getInt64(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_int64(const StreamReader self)
        
        /**
         * Extracts a signed 64-bit integer.
         */
        """
        pass

    def getInt8(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_int8(const StreamReader self)
        
        /**
         * Extracts a signed 8-bit integer.
         */
        """
        pass

    def getIstream(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_istream(StreamReader self)
        
        /**
         * Returns the stream in use.
         */
        """
        pass

    def getString(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_string(const StreamReader self)
        
        /**
         * Extracts a variable-length string.
         */
        """
        pass

    def getString32(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_string32(const StreamReader self)
        
        /**
         * Extracts a variable-length string with a 32-bit length field.
         */
        """
        pass

    def getUint16(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_uint16(const StreamReader self)
        
        /**
         * Extracts an unsigned 16-bit integer.
         */
        """
        pass

    def getUint32(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_uint32(const StreamReader self)
        
        /**
         * Extracts an unsigned 32-bit integer.
         */
        """
        pass

    def getUint64(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_uint64(const StreamReader self)
        
        /**
         * Extracts an unsigned 64-bit integer.
         */
        """
        pass

    def getUint8(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_uint8(const StreamReader self)
        
        /**
         * Extracts an unsigned 8-bit integer.
         */
        """
        pass

    def getZString(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_z_string(const StreamReader self)
        
        /**
         * Extracts a variable-length string, as a NULL-terminated string.
         */
        """
        pass

    def get_be_float32(self, const_StreamReader_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_be_float32(const StreamReader self)
        
        /**
         * Extracts a 32-bit single-precision big-endian floating-point number.  Since
         * this kind of float is not necessarily portable across different
         * architectures, special care is required.
         */
        """
        pass

    def get_be_float64(self, const_StreamReader_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_be_float64(const StreamReader self)
        
        /**
         * Extracts a 64-bit big-endian floating-point number.
         */
        """
        pass

    def get_be_int16(self, const_StreamReader_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_be_int16(const StreamReader self)
        
        /**
         * Extracts a signed big-endian 16-bit integer.
         */
        """
        pass

    def get_be_int32(self, const_StreamReader_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_be_int32(const StreamReader self)
        
        /**
         * Extracts a signed big-endian 32-bit integer.
         */
        """
        pass

    def get_be_int64(self, const_StreamReader_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_be_int64(const StreamReader self)
        
        /**
         * Extracts a signed big-endian 64-bit integer.
         */
        """
        pass

    def get_be_uint16(self, const_StreamReader_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_be_uint16(const StreamReader self)
        
        /**
         * Extracts an unsigned big-endian 16-bit integer.
         */
        """
        pass

    def get_be_uint32(self, const_StreamReader_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_be_uint32(const StreamReader self)
        
        /**
         * Extracts an unsigned big-endian 32-bit integer.
         */
        """
        pass

    def get_be_uint64(self, const_StreamReader_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_be_uint64(const StreamReader self)
        
        /**
         * Extracts an unsigned big-endian 64-bit integer.
         */
        """
        pass

    def get_bool(self, const_StreamReader_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_bool(const StreamReader self)
        
        /**
         * Extracts a boolean value.
         */
        """
        pass

    def get_fixed_string(self, const_StreamReader_self, int_size): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_fixed_string(const StreamReader self, int size)
        
        /**
         * Extracts a fixed-length string.  However, if a zero byte occurs within the
         * string, it marks the end of the string.
         */
        """
        pass

    def get_float32(self, const_StreamReader_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_float32(const StreamReader self)
        
        /**
         * Extracts a 32-bit single-precision floating-point number.  Since this kind
         * of float is not necessarily portable across different architectures,
         * special care is required.
         */
        """
        pass

    def get_float64(self, const_StreamReader_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_float64(const StreamReader self)
        
        /**
         * Extracts a 64-bit floating-point number.
         */
        """
        pass

    def get_int16(self, const_StreamReader_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_int16(const StreamReader self)
        
        /**
         * Extracts a signed 16-bit integer.
         */
        """
        pass

    def get_int32(self, const_StreamReader_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_int32(const StreamReader self)
        
        /**
         * Extracts a signed 32-bit integer.
         */
        """
        pass

    def get_int64(self, const_StreamReader_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_int64(const StreamReader self)
        
        /**
         * Extracts a signed 64-bit integer.
         */
        """
        pass

    def get_int8(self, const_StreamReader_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_int8(const StreamReader self)
        
        /**
         * Extracts a signed 8-bit integer.
         */
        """
        pass

    def get_istream(self, StreamReader_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_istream(StreamReader self)
        
        /**
         * Returns the stream in use.
         */
        """
        pass

    def get_string(self, const_StreamReader_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_string(const StreamReader self)
        
        /**
         * Extracts a variable-length string.
         */
        """
        pass

    def get_string32(self, const_StreamReader_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_string32(const StreamReader self)
        
        /**
         * Extracts a variable-length string with a 32-bit length field.
         */
        """
        pass

    def get_uint16(self, const_StreamReader_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_uint16(const StreamReader self)
        
        /**
         * Extracts an unsigned 16-bit integer.
         */
        """
        pass

    def get_uint32(self, const_StreamReader_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_uint32(const StreamReader self)
        
        /**
         * Extracts an unsigned 32-bit integer.
         */
        """
        pass

    def get_uint64(self, const_StreamReader_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_uint64(const StreamReader self)
        
        /**
         * Extracts an unsigned 64-bit integer.
         */
        """
        pass

    def get_uint8(self, const_StreamReader_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_uint8(const StreamReader self)
        
        /**
         * Extracts an unsigned 8-bit integer.
         */
        """
        pass

    def get_z_string(self, const_StreamReader_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_z_string(const StreamReader self)
        
        /**
         * Extracts a variable-length string, as a NULL-terminated string.
         */
        """
        pass

    def readline(self, const_StreamReader_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        readline(const StreamReader self)
        
        /**
         * Assumes the stream represents a text file, and extracts one line up to and
         * including the trailing newline character.  Returns empty string when the
         * end of file is reached.
         *
         * The interface here is intentionally designed to be similar to that for
         * Python's File.readline() function.
         */
        """
        pass

    def readlines(self, const_StreamReader_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        readlines(const StreamReader self)
        """
        pass

    def skipBytes(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        skip_bytes(const StreamReader self, int size)
        
        /**
         * Skips over the indicated number of bytes in the stream.
         */
        """
        pass

    def skip_bytes(self, const_StreamReader_self, int_size): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        skip_bytes(const StreamReader self, int size)
        
        /**
         * Skips over the indicated number of bytes in the stream.
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

    istream = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.core.StreamReader' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.core.StreamReader' objects>"
        '__doc__': '/**\n * A class to read sequential binary data directly from an istream.  Its\n * interface is similar to DatagramIterator by design; see also StreamWriter.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.StreamReader' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE2644F0>'
        'assign': None, # (!) real value is "<method 'assign' of 'panda3d.core.StreamReader' objects>"
        'extractBytes': None, # (!) real value is "<method 'extractBytes' of 'panda3d.core.StreamReader' objects>"
        'extract_bytes': None, # (!) real value is "<method 'extract_bytes' of 'panda3d.core.StreamReader' objects>"
        'getBeFloat32': None, # (!) real value is "<method 'getBeFloat32' of 'panda3d.core.StreamReader' objects>"
        'getBeFloat64': None, # (!) real value is "<method 'getBeFloat64' of 'panda3d.core.StreamReader' objects>"
        'getBeInt16': None, # (!) real value is "<method 'getBeInt16' of 'panda3d.core.StreamReader' objects>"
        'getBeInt32': None, # (!) real value is "<method 'getBeInt32' of 'panda3d.core.StreamReader' objects>"
        'getBeInt64': None, # (!) real value is "<method 'getBeInt64' of 'panda3d.core.StreamReader' objects>"
        'getBeUint16': None, # (!) real value is "<method 'getBeUint16' of 'panda3d.core.StreamReader' objects>"
        'getBeUint32': None, # (!) real value is "<method 'getBeUint32' of 'panda3d.core.StreamReader' objects>"
        'getBeUint64': None, # (!) real value is "<method 'getBeUint64' of 'panda3d.core.StreamReader' objects>"
        'getBool': None, # (!) real value is "<method 'getBool' of 'panda3d.core.StreamReader' objects>"
        'getFixedString': None, # (!) real value is "<method 'getFixedString' of 'panda3d.core.StreamReader' objects>"
        'getFloat32': None, # (!) real value is "<method 'getFloat32' of 'panda3d.core.StreamReader' objects>"
        'getFloat64': None, # (!) real value is "<method 'getFloat64' of 'panda3d.core.StreamReader' objects>"
        'getInt16': None, # (!) real value is "<method 'getInt16' of 'panda3d.core.StreamReader' objects>"
        'getInt32': None, # (!) real value is "<method 'getInt32' of 'panda3d.core.StreamReader' objects>"
        'getInt64': None, # (!) real value is "<method 'getInt64' of 'panda3d.core.StreamReader' objects>"
        'getInt8': None, # (!) real value is "<method 'getInt8' of 'panda3d.core.StreamReader' objects>"
        'getIstream': None, # (!) real value is "<method 'getIstream' of 'panda3d.core.StreamReader' objects>"
        'getString': None, # (!) real value is "<method 'getString' of 'panda3d.core.StreamReader' objects>"
        'getString32': None, # (!) real value is "<method 'getString32' of 'panda3d.core.StreamReader' objects>"
        'getUint16': None, # (!) real value is "<method 'getUint16' of 'panda3d.core.StreamReader' objects>"
        'getUint32': None, # (!) real value is "<method 'getUint32' of 'panda3d.core.StreamReader' objects>"
        'getUint64': None, # (!) real value is "<method 'getUint64' of 'panda3d.core.StreamReader' objects>"
        'getUint8': None, # (!) real value is "<method 'getUint8' of 'panda3d.core.StreamReader' objects>"
        'getZString': None, # (!) real value is "<method 'getZString' of 'panda3d.core.StreamReader' objects>"
        'get_be_float32': None, # (!) real value is "<method 'get_be_float32' of 'panda3d.core.StreamReader' objects>"
        'get_be_float64': None, # (!) real value is "<method 'get_be_float64' of 'panda3d.core.StreamReader' objects>"
        'get_be_int16': None, # (!) real value is "<method 'get_be_int16' of 'panda3d.core.StreamReader' objects>"
        'get_be_int32': None, # (!) real value is "<method 'get_be_int32' of 'panda3d.core.StreamReader' objects>"
        'get_be_int64': None, # (!) real value is "<method 'get_be_int64' of 'panda3d.core.StreamReader' objects>"
        'get_be_uint16': None, # (!) real value is "<method 'get_be_uint16' of 'panda3d.core.StreamReader' objects>"
        'get_be_uint32': None, # (!) real value is "<method 'get_be_uint32' of 'panda3d.core.StreamReader' objects>"
        'get_be_uint64': None, # (!) real value is "<method 'get_be_uint64' of 'panda3d.core.StreamReader' objects>"
        'get_bool': None, # (!) real value is "<method 'get_bool' of 'panda3d.core.StreamReader' objects>"
        'get_fixed_string': None, # (!) real value is "<method 'get_fixed_string' of 'panda3d.core.StreamReader' objects>"
        'get_float32': None, # (!) real value is "<method 'get_float32' of 'panda3d.core.StreamReader' objects>"
        'get_float64': None, # (!) real value is "<method 'get_float64' of 'panda3d.core.StreamReader' objects>"
        'get_int16': None, # (!) real value is "<method 'get_int16' of 'panda3d.core.StreamReader' objects>"
        'get_int32': None, # (!) real value is "<method 'get_int32' of 'panda3d.core.StreamReader' objects>"
        'get_int64': None, # (!) real value is "<method 'get_int64' of 'panda3d.core.StreamReader' objects>"
        'get_int8': None, # (!) real value is "<method 'get_int8' of 'panda3d.core.StreamReader' objects>"
        'get_istream': None, # (!) real value is "<method 'get_istream' of 'panda3d.core.StreamReader' objects>"
        'get_string': None, # (!) real value is "<method 'get_string' of 'panda3d.core.StreamReader' objects>"
        'get_string32': None, # (!) real value is "<method 'get_string32' of 'panda3d.core.StreamReader' objects>"
        'get_uint16': None, # (!) real value is "<method 'get_uint16' of 'panda3d.core.StreamReader' objects>"
        'get_uint32': None, # (!) real value is "<method 'get_uint32' of 'panda3d.core.StreamReader' objects>"
        'get_uint64': None, # (!) real value is "<method 'get_uint64' of 'panda3d.core.StreamReader' objects>"
        'get_uint8': None, # (!) real value is "<method 'get_uint8' of 'panda3d.core.StreamReader' objects>"
        'get_z_string': None, # (!) real value is "<method 'get_z_string' of 'panda3d.core.StreamReader' objects>"
        'istream': None, # (!) real value is "<attribute 'istream' of 'panda3d.core.StreamReader' objects>"
        'readline': None, # (!) real value is "<method 'readline' of 'panda3d.core.StreamReader' objects>"
        'readlines': None, # (!) real value is "<method 'readlines' of 'panda3d.core.StreamReader' objects>"
        'skipBytes': None, # (!) real value is "<method 'skipBytes' of 'panda3d.core.StreamReader' objects>"
        'skip_bytes': None, # (!) real value is "<method 'skip_bytes' of 'panda3d.core.StreamReader' objects>"
    }


