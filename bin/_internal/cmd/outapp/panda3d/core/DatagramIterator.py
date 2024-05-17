# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


class DatagramIterator(__dtoolconfig.DTOOL_SUPER_BASE):
    """
    /**
     * A class to retrieve the individual data elements previously stored in a
     * Datagram.  Elements may be retrieved one at a time; it is up to the caller
     * to know the correct type and order of each element.
     *
     * Note that it is the responsibility of the caller to ensure that the datagram
     * object is not destructed while this DatagramIterator is in use.
     */
    """
    def extractBytes(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        extract_bytes(const DatagramIterator self, int size)
        
        /**
         * Extracts the indicated number of bytes in the datagram and returns them as
         * a string.
         */
        
        /**
         * Extracts the indicated number of bytes in the datagram into the given
         * character buffer.  Assumes that the buffer is big enough to hold the
         * requested number of bytes.  Returns the number of bytes that were
         * successfully written.
         */
        """
        pass

    def extract_bytes(self, const_DatagramIterator_self, int_size): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        extract_bytes(const DatagramIterator self, int size)
        
        /**
         * Extracts the indicated number of bytes in the datagram and returns them as
         * a string.
         */
        
        /**
         * Extracts the indicated number of bytes in the datagram into the given
         * character buffer.  Assumes that the buffer is big enough to hold the
         * requested number of bytes.  Returns the number of bytes that were
         * successfully written.
         */
        """
        pass

    def getBeFloat32(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_be_float32(const DatagramIterator self)
        
        /**
         * Extracts a 32-bit big-endian single-precision floating-point number.
         */
        """
        pass

    def getBeFloat64(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_be_float64(const DatagramIterator self)
        
        /**
         * Extracts a 64-bit big-endian floating-point number.
         */
        """
        pass

    def getBeInt16(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_be_int16(const DatagramIterator self)
        
        /**
         * Extracts a signed 16-bit big-endian integer.
         */
        """
        pass

    def getBeInt32(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_be_int32(const DatagramIterator self)
        
        /**
         * Extracts a signed 32-bit big-endian integer.
         */
        """
        pass

    def getBeInt64(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_be_int64(const DatagramIterator self)
        
        /**
         * Extracts a signed 64-bit big-endian integer.
         */
        """
        pass

    def getBeUint16(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_be_uint16(const DatagramIterator self)
        
        /**
         * Extracts an unsigned 16-bit big-endian integer.
         */
        """
        pass

    def getBeUint32(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_be_uint32(const DatagramIterator self)
        
        /**
         * Extracts an unsigned 32-bit big-endian integer.
         */
        """
        pass

    def getBeUint64(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_be_uint64(const DatagramIterator self)
        
        /**
         * Extracts an unsigned 64-bit big-endian integer.
         */
        """
        pass

    def getBlob(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_blob(const DatagramIterator self)
        
        /**
         * Extracts a variable-length binary blob.
         */
        """
        pass

    def getBlob32(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_blob32(const DatagramIterator self)
        
        /**
         * Extracts a variable-length binary blob with a 32-bit size field.
         */
        """
        pass

    def getBool(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_bool(const DatagramIterator self)
        
        /**
         * Extracts a boolean value.
         */
        """
        pass

    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getCurrentIndex(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_current_index(DatagramIterator self)
        
        /**
         * Returns the current position within the datagram of the next piece of data
         * to extract.
         */
        """
        pass

    def getDatagram(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_datagram(DatagramIterator self)
        
        /**
         * Return the datagram of this iterator.
         */
        """
        pass

    def getFixedString(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_fixed_string(const DatagramIterator self, int size)
        
        /**
         * Extracts a fixed-length string.  However, if a zero byte occurs within the
         * string, it marks the end of the string.
         */
        """
        pass

    def getFloat32(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_float32(const DatagramIterator self)
        
        /**
         * Extracts a 32-bit single-precision floating-point number.
         */
        """
        pass

    def getFloat64(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_float64(const DatagramIterator self)
        
        /**
         * Extracts a 64-bit floating-point number.
         */
        """
        pass

    def getInt16(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_int16(const DatagramIterator self)
        
        /**
         * Extracts a signed 16-bit integer.
         */
        """
        pass

    def getInt32(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_int32(const DatagramIterator self)
        
        /**
         * Extracts a signed 32-bit integer.
         */
        """
        pass

    def getInt64(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_int64(const DatagramIterator self)
        
        /**
         * Extracts a signed 64-bit integer.
         */
        """
        pass

    def getInt8(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_int8(const DatagramIterator self)
        
        /**
         * Extracts a signed 8-bit integer.
         */
        """
        pass

    def getRemainingBytes(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_remaining_bytes(DatagramIterator self)
        
        /**
         * Returns the remaining bytes in the datagram as a string, but does not
         * extract them from the iterator.
         */
        """
        pass

    def getRemainingSize(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_remaining_size(DatagramIterator self)
        
        /**
         * Return the bytes left in the datagram.
         */
        """
        pass

    def getStdfloat(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_stdfloat(const DatagramIterator self)
        
        /**
         * Extracts either a 32-bit or a 64-bit floating-point number, according to
         * Datagram::set_stdfloat_double().
         */
        """
        pass

    def getString(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_string(const DatagramIterator self)
        
        /**
         * Extracts a variable-length string.
         */
        """
        pass

    def getString32(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_string32(const DatagramIterator self)
        
        /**
         * Extracts a variable-length string with a 32-bit length field.
         */
        """
        pass

    def getUint16(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_uint16(const DatagramIterator self)
        
        /**
         * Extracts an unsigned 16-bit integer.
         */
        """
        pass

    def getUint32(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_uint32(const DatagramIterator self)
        
        /**
         * Extracts an unsigned 32-bit integer.
         */
        """
        pass

    def getUint64(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_uint64(const DatagramIterator self)
        
        /**
         * Extracts an unsigned 64-bit integer.
         */
        """
        pass

    def getUint8(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_uint8(const DatagramIterator self)
        
        /**
         * Extracts an unsigned 8-bit integer.
         */
        """
        pass

    def getWstring(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_wstring(const DatagramIterator self)
        
        /**
         * Extracts a variable-length wstring (with a 32-bit length field).
         */
        """
        pass

    def getZString(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_z_string(const DatagramIterator self)
        
        /**
         * Extracts a variable-length string, as a NULL-terminated string.
         */
        """
        pass

    def get_be_float32(self, const_DatagramIterator_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_be_float32(const DatagramIterator self)
        
        /**
         * Extracts a 32-bit big-endian single-precision floating-point number.
         */
        """
        pass

    def get_be_float64(self, const_DatagramIterator_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_be_float64(const DatagramIterator self)
        
        /**
         * Extracts a 64-bit big-endian floating-point number.
         */
        """
        pass

    def get_be_int16(self, const_DatagramIterator_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_be_int16(const DatagramIterator self)
        
        /**
         * Extracts a signed 16-bit big-endian integer.
         */
        """
        pass

    def get_be_int32(self, const_DatagramIterator_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_be_int32(const DatagramIterator self)
        
        /**
         * Extracts a signed 32-bit big-endian integer.
         */
        """
        pass

    def get_be_int64(self, const_DatagramIterator_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_be_int64(const DatagramIterator self)
        
        /**
         * Extracts a signed 64-bit big-endian integer.
         */
        """
        pass

    def get_be_uint16(self, const_DatagramIterator_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_be_uint16(const DatagramIterator self)
        
        /**
         * Extracts an unsigned 16-bit big-endian integer.
         */
        """
        pass

    def get_be_uint32(self, const_DatagramIterator_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_be_uint32(const DatagramIterator self)
        
        /**
         * Extracts an unsigned 32-bit big-endian integer.
         */
        """
        pass

    def get_be_uint64(self, const_DatagramIterator_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_be_uint64(const DatagramIterator self)
        
        /**
         * Extracts an unsigned 64-bit big-endian integer.
         */
        """
        pass

    def get_blob(self, const_DatagramIterator_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_blob(const DatagramIterator self)
        
        /**
         * Extracts a variable-length binary blob.
         */
        """
        pass

    def get_blob32(self, const_DatagramIterator_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_blob32(const DatagramIterator self)
        
        /**
         * Extracts a variable-length binary blob with a 32-bit size field.
         */
        """
        pass

    def get_bool(self, const_DatagramIterator_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_bool(const DatagramIterator self)
        
        /**
         * Extracts a boolean value.
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_current_index(self, DatagramIterator_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_current_index(DatagramIterator self)
        
        /**
         * Returns the current position within the datagram of the next piece of data
         * to extract.
         */
        """
        pass

    def get_datagram(self, DatagramIterator_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_datagram(DatagramIterator self)
        
        /**
         * Return the datagram of this iterator.
         */
        """
        pass

    def get_fixed_string(self, const_DatagramIterator_self, int_size): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_fixed_string(const DatagramIterator self, int size)
        
        /**
         * Extracts a fixed-length string.  However, if a zero byte occurs within the
         * string, it marks the end of the string.
         */
        """
        pass

    def get_float32(self, const_DatagramIterator_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_float32(const DatagramIterator self)
        
        /**
         * Extracts a 32-bit single-precision floating-point number.
         */
        """
        pass

    def get_float64(self, const_DatagramIterator_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_float64(const DatagramIterator self)
        
        /**
         * Extracts a 64-bit floating-point number.
         */
        """
        pass

    def get_int16(self, const_DatagramIterator_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_int16(const DatagramIterator self)
        
        /**
         * Extracts a signed 16-bit integer.
         */
        """
        pass

    def get_int32(self, const_DatagramIterator_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_int32(const DatagramIterator self)
        
        /**
         * Extracts a signed 32-bit integer.
         */
        """
        pass

    def get_int64(self, const_DatagramIterator_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_int64(const DatagramIterator self)
        
        /**
         * Extracts a signed 64-bit integer.
         */
        """
        pass

    def get_int8(self, const_DatagramIterator_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_int8(const DatagramIterator self)
        
        /**
         * Extracts a signed 8-bit integer.
         */
        """
        pass

    def get_remaining_bytes(self, DatagramIterator_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_remaining_bytes(DatagramIterator self)
        
        /**
         * Returns the remaining bytes in the datagram as a string, but does not
         * extract them from the iterator.
         */
        """
        pass

    def get_remaining_size(self, DatagramIterator_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_remaining_size(DatagramIterator self)
        
        /**
         * Return the bytes left in the datagram.
         */
        """
        pass

    def get_stdfloat(self, const_DatagramIterator_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_stdfloat(const DatagramIterator self)
        
        /**
         * Extracts either a 32-bit or a 64-bit floating-point number, according to
         * Datagram::set_stdfloat_double().
         */
        """
        pass

    def get_string(self, const_DatagramIterator_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_string(const DatagramIterator self)
        
        /**
         * Extracts a variable-length string.
         */
        """
        pass

    def get_string32(self, const_DatagramIterator_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_string32(const DatagramIterator self)
        
        /**
         * Extracts a variable-length string with a 32-bit length field.
         */
        """
        pass

    def get_uint16(self, const_DatagramIterator_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_uint16(const DatagramIterator self)
        
        /**
         * Extracts an unsigned 16-bit integer.
         */
        """
        pass

    def get_uint32(self, const_DatagramIterator_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_uint32(const DatagramIterator self)
        
        /**
         * Extracts an unsigned 32-bit integer.
         */
        """
        pass

    def get_uint64(self, const_DatagramIterator_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_uint64(const DatagramIterator self)
        
        /**
         * Extracts an unsigned 64-bit integer.
         */
        """
        pass

    def get_uint8(self, const_DatagramIterator_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_uint8(const DatagramIterator self)
        
        /**
         * Extracts an unsigned 8-bit integer.
         */
        """
        pass

    def get_wstring(self, const_DatagramIterator_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_wstring(const DatagramIterator self)
        
        /**
         * Extracts a variable-length wstring (with a 32-bit length field).
         */
        """
        pass

    def get_z_string(self, const_DatagramIterator_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_z_string(const DatagramIterator self)
        
        /**
         * Extracts a variable-length string, as a NULL-terminated string.
         */
        """
        pass

    def output(self, DatagramIterator_self, ostream_out): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        output(DatagramIterator self, ostream out)
        
        /**
         * Write a string representation of this instance to <out>.
         */
        """
        pass

    def skipBytes(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        skip_bytes(const DatagramIterator self, int size)
        
        /**
         * Skips over the indicated number of bytes in the datagram.
         */
        """
        pass

    def skip_bytes(self, const_DatagramIterator_self, int_size): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        skip_bytes(const DatagramIterator self, int size)
        
        /**
         * Skips over the indicated number of bytes in the datagram.
         */
        """
        pass

    def write(self, DatagramIterator_self, ostream_out, int_indent): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        write(DatagramIterator self, ostream out, int indent)
        
        /**
         * Write a string representation of this instance to <out>.
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
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.core.DatagramIterator' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.core.DatagramIterator' objects>"
        '__doc__': '/**\n * A class to retrieve the individual data elements previously stored in a\n * Datagram.  Elements may be retrieved one at a time; it is up to the caller\n * to know the correct type and order of each element.\n *\n * Note that it is the responsibility of the caller to ensure that the datagram\n * object is not destructed while this DatagramIterator is in use.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.DatagramIterator' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE277CF0>'
        '__repr__': None, # (!) real value is "<slot wrapper '__repr__' of 'panda3d.core.DatagramIterator' objects>"
        '__str__': None, # (!) real value is "<slot wrapper '__str__' of 'panda3d.core.DatagramIterator' objects>"
        'extractBytes': None, # (!) real value is "<method 'extractBytes' of 'panda3d.core.DatagramIterator' objects>"
        'extract_bytes': None, # (!) real value is "<method 'extract_bytes' of 'panda3d.core.DatagramIterator' objects>"
        'getBeFloat32': None, # (!) real value is "<method 'getBeFloat32' of 'panda3d.core.DatagramIterator' objects>"
        'getBeFloat64': None, # (!) real value is "<method 'getBeFloat64' of 'panda3d.core.DatagramIterator' objects>"
        'getBeInt16': None, # (!) real value is "<method 'getBeInt16' of 'panda3d.core.DatagramIterator' objects>"
        'getBeInt32': None, # (!) real value is "<method 'getBeInt32' of 'panda3d.core.DatagramIterator' objects>"
        'getBeInt64': None, # (!) real value is "<method 'getBeInt64' of 'panda3d.core.DatagramIterator' objects>"
        'getBeUint16': None, # (!) real value is "<method 'getBeUint16' of 'panda3d.core.DatagramIterator' objects>"
        'getBeUint32': None, # (!) real value is "<method 'getBeUint32' of 'panda3d.core.DatagramIterator' objects>"
        'getBeUint64': None, # (!) real value is "<method 'getBeUint64' of 'panda3d.core.DatagramIterator' objects>"
        'getBlob': None, # (!) real value is "<method 'getBlob' of 'panda3d.core.DatagramIterator' objects>"
        'getBlob32': None, # (!) real value is "<method 'getBlob32' of 'panda3d.core.DatagramIterator' objects>"
        'getBool': None, # (!) real value is "<method 'getBool' of 'panda3d.core.DatagramIterator' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE277CF0>)>'
        'getCurrentIndex': None, # (!) real value is "<method 'getCurrentIndex' of 'panda3d.core.DatagramIterator' objects>"
        'getDatagram': None, # (!) real value is "<method 'getDatagram' of 'panda3d.core.DatagramIterator' objects>"
        'getFixedString': None, # (!) real value is "<method 'getFixedString' of 'panda3d.core.DatagramIterator' objects>"
        'getFloat32': None, # (!) real value is "<method 'getFloat32' of 'panda3d.core.DatagramIterator' objects>"
        'getFloat64': None, # (!) real value is "<method 'getFloat64' of 'panda3d.core.DatagramIterator' objects>"
        'getInt16': None, # (!) real value is "<method 'getInt16' of 'panda3d.core.DatagramIterator' objects>"
        'getInt32': None, # (!) real value is "<method 'getInt32' of 'panda3d.core.DatagramIterator' objects>"
        'getInt64': None, # (!) real value is "<method 'getInt64' of 'panda3d.core.DatagramIterator' objects>"
        'getInt8': None, # (!) real value is "<method 'getInt8' of 'panda3d.core.DatagramIterator' objects>"
        'getRemainingBytes': None, # (!) real value is "<method 'getRemainingBytes' of 'panda3d.core.DatagramIterator' objects>"
        'getRemainingSize': None, # (!) real value is "<method 'getRemainingSize' of 'panda3d.core.DatagramIterator' objects>"
        'getStdfloat': None, # (!) real value is "<method 'getStdfloat' of 'panda3d.core.DatagramIterator' objects>"
        'getString': None, # (!) real value is "<method 'getString' of 'panda3d.core.DatagramIterator' objects>"
        'getString32': None, # (!) real value is "<method 'getString32' of 'panda3d.core.DatagramIterator' objects>"
        'getUint16': None, # (!) real value is "<method 'getUint16' of 'panda3d.core.DatagramIterator' objects>"
        'getUint32': None, # (!) real value is "<method 'getUint32' of 'panda3d.core.DatagramIterator' objects>"
        'getUint64': None, # (!) real value is "<method 'getUint64' of 'panda3d.core.DatagramIterator' objects>"
        'getUint8': None, # (!) real value is "<method 'getUint8' of 'panda3d.core.DatagramIterator' objects>"
        'getWstring': None, # (!) real value is "<method 'getWstring' of 'panda3d.core.DatagramIterator' objects>"
        'getZString': None, # (!) real value is "<method 'getZString' of 'panda3d.core.DatagramIterator' objects>"
        'get_be_float32': None, # (!) real value is "<method 'get_be_float32' of 'panda3d.core.DatagramIterator' objects>"
        'get_be_float64': None, # (!) real value is "<method 'get_be_float64' of 'panda3d.core.DatagramIterator' objects>"
        'get_be_int16': None, # (!) real value is "<method 'get_be_int16' of 'panda3d.core.DatagramIterator' objects>"
        'get_be_int32': None, # (!) real value is "<method 'get_be_int32' of 'panda3d.core.DatagramIterator' objects>"
        'get_be_int64': None, # (!) real value is "<method 'get_be_int64' of 'panda3d.core.DatagramIterator' objects>"
        'get_be_uint16': None, # (!) real value is "<method 'get_be_uint16' of 'panda3d.core.DatagramIterator' objects>"
        'get_be_uint32': None, # (!) real value is "<method 'get_be_uint32' of 'panda3d.core.DatagramIterator' objects>"
        'get_be_uint64': None, # (!) real value is "<method 'get_be_uint64' of 'panda3d.core.DatagramIterator' objects>"
        'get_blob': None, # (!) real value is "<method 'get_blob' of 'panda3d.core.DatagramIterator' objects>"
        'get_blob32': None, # (!) real value is "<method 'get_blob32' of 'panda3d.core.DatagramIterator' objects>"
        'get_bool': None, # (!) real value is "<method 'get_bool' of 'panda3d.core.DatagramIterator' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE277CF0>)>'
        'get_current_index': None, # (!) real value is "<method 'get_current_index' of 'panda3d.core.DatagramIterator' objects>"
        'get_datagram': None, # (!) real value is "<method 'get_datagram' of 'panda3d.core.DatagramIterator' objects>"
        'get_fixed_string': None, # (!) real value is "<method 'get_fixed_string' of 'panda3d.core.DatagramIterator' objects>"
        'get_float32': None, # (!) real value is "<method 'get_float32' of 'panda3d.core.DatagramIterator' objects>"
        'get_float64': None, # (!) real value is "<method 'get_float64' of 'panda3d.core.DatagramIterator' objects>"
        'get_int16': None, # (!) real value is "<method 'get_int16' of 'panda3d.core.DatagramIterator' objects>"
        'get_int32': None, # (!) real value is "<method 'get_int32' of 'panda3d.core.DatagramIterator' objects>"
        'get_int64': None, # (!) real value is "<method 'get_int64' of 'panda3d.core.DatagramIterator' objects>"
        'get_int8': None, # (!) real value is "<method 'get_int8' of 'panda3d.core.DatagramIterator' objects>"
        'get_remaining_bytes': None, # (!) real value is "<method 'get_remaining_bytes' of 'panda3d.core.DatagramIterator' objects>"
        'get_remaining_size': None, # (!) real value is "<method 'get_remaining_size' of 'panda3d.core.DatagramIterator' objects>"
        'get_stdfloat': None, # (!) real value is "<method 'get_stdfloat' of 'panda3d.core.DatagramIterator' objects>"
        'get_string': None, # (!) real value is "<method 'get_string' of 'panda3d.core.DatagramIterator' objects>"
        'get_string32': None, # (!) real value is "<method 'get_string32' of 'panda3d.core.DatagramIterator' objects>"
        'get_uint16': None, # (!) real value is "<method 'get_uint16' of 'panda3d.core.DatagramIterator' objects>"
        'get_uint32': None, # (!) real value is "<method 'get_uint32' of 'panda3d.core.DatagramIterator' objects>"
        'get_uint64': None, # (!) real value is "<method 'get_uint64' of 'panda3d.core.DatagramIterator' objects>"
        'get_uint8': None, # (!) real value is "<method 'get_uint8' of 'panda3d.core.DatagramIterator' objects>"
        'get_wstring': None, # (!) real value is "<method 'get_wstring' of 'panda3d.core.DatagramIterator' objects>"
        'get_z_string': None, # (!) real value is "<method 'get_z_string' of 'panda3d.core.DatagramIterator' objects>"
        'output': None, # (!) real value is "<method 'output' of 'panda3d.core.DatagramIterator' objects>"
        'skipBytes': None, # (!) real value is "<method 'skipBytes' of 'panda3d.core.DatagramIterator' objects>"
        'skip_bytes': None, # (!) real value is "<method 'skip_bytes' of 'panda3d.core.DatagramIterator' objects>"
        'write': None, # (!) real value is "<method 'write' of 'panda3d.core.DatagramIterator' objects>"
    }


