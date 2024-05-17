# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .TypedObject import TypedObject

class Datagram(TypedObject):
    """
    /**
     * An ordered list of data elements, formatted in memory for transmission over
     * a socket or writing to a data file.
     *
     * Data elements should be added one at a time, in order, to the Datagram.
     * The nature and contents of the data elements are totally up to the user.
     * When a Datagram has been transmitted and received, its data elements may be
     * extracted using a DatagramIterator; it is up to the caller to know the
     * correct type of each data element in order.
     *
     * A Datagram is itself headerless; it is simply a collection of data
     * elements.
     */
    """
    def addBeFloat32(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_be_float32(const Datagram self, float value)
        
        /**
         * Adds a 32-bit single-precision big-endian floating-point number to the
         * datagram.
         */
        """
        pass

    def addBeFloat64(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_be_float64(const Datagram self, double value)
        
        /**
         * Adds a 64-bit big-endian floating-point number to the datagram.
         */
        """
        pass

    def addBeInt16(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_be_int16(const Datagram self, int value)
        
        // These functions pack numbers big-endian, in case that's desired.
        
        /**
         * Adds a signed 16-bit big-endian integer to the datagram.
         */
        """
        pass

    def addBeInt32(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_be_int32(const Datagram self, int value)
        
        /**
         * Adds a signed 32-bit big-endian integer to the datagram.
         */
        """
        pass

    def addBeInt64(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_be_int64(const Datagram self, long value)
        
        /**
         * Adds a signed 64-bit big-endian integer to the datagram.
         */
        """
        pass

    def addBeUint16(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_be_uint16(const Datagram self, int value)
        
        /**
         * Adds an unsigned 16-bit big-endian integer to the datagram.
         */
        """
        pass

    def addBeUint32(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_be_uint32(const Datagram self, int value)
        
        /**
         * Adds an unsigned 32-bit big-endian integer to the datagram.
         */
        """
        pass

    def addBeUint64(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_be_uint64(const Datagram self, long value)
        
        /**
         * Adds an unsigned 64-bit big-endian integer to the datagram.
         */
        """
        pass

    def addBlob(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_blob(const Datagram self, bytes param0)
        
        /**
         * Adds a variable-length binary blob to the datagram.  This actually adds a
         * count followed by n bytes.
         */
        """
        pass

    def addBlob32(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_blob32(const Datagram self, bytes param0)
        
        /**
         * Adds a variable-length binary blob to the datagram, using a 32-bit length
         * field to allow very long blobs.
         */
        """
        pass

    def addBool(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_bool(const Datagram self, bool value)
        
        /**
         * Adds a boolean value to the datagram.
         */
        """
        pass

    def addFixedString(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_fixed_string(const Datagram self, str str, int size)
        
        /**
         * Adds a fixed-length string to the datagram.  If the string given is less
         * than the requested size, this will pad the string out with zeroes; if it is
         * greater than the requested size, this will silently truncate the string.
         */
        """
        pass

    def addFloat32(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_float32(const Datagram self, float value)
        
        /**
         * Adds a 32-bit single-precision floating-point number to the datagram.
         * Since this kind of float is not necessarily portable across different
         * architectures, special care is required.
         */
        """
        pass

    def addFloat64(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_float64(const Datagram self, double value)
        
        /**
         * Adds a 64-bit floating-point number to the datagram.
         */
        """
        pass

    def addInt16(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_int16(const Datagram self, int value)
        
        // The default numeric packing is little-endian.
        
        /**
         * Adds a signed 16-bit integer to the datagram.
         */
        """
        pass

    def addInt32(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_int32(const Datagram self, int value)
        
        /**
         * Adds a signed 32-bit integer to the datagram.
         */
        """
        pass

    def addInt64(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_int64(const Datagram self, long value)
        
        /**
         * Adds a signed 64-bit integer to the datagram.
         */
        """
        pass

    def addInt8(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_int8(const Datagram self, int value)
        
        /**
         * Adds a signed 8-bit integer to the datagram.
         */
        """
        pass

    def addStdfloat(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_stdfloat(const Datagram self, float value)
        
        /**
         * Adds either a 32-bit or a 64-bit floating-point number, according to
         * set_stdfloat_double().
         */
        """
        pass

    def addString(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_string(const Datagram self, str str)
        
        /**
         * Adds a variable-length string to the datagram.  This actually adds a count
         * followed by n bytes.
         */
        """
        pass

    def addString32(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_string32(const Datagram self, str str)
        
        /**
         * Adds a variable-length string to the datagram, using a 32-bit length field
         * to allow very long strings.
         */
        """
        pass

    def addUint16(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_uint16(const Datagram self, int value)
        
        /**
         * Adds an unsigned 16-bit integer to the datagram.
         */
        """
        pass

    def addUint32(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_uint32(const Datagram self, int value)
        
        /**
         * Adds an unsigned 32-bit integer to the datagram.
         */
        """
        pass

    def addUint64(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_uint64(const Datagram self, long value)
        
        /**
         * Adds an unsigned 64-bit integer to the datagram.
         */
        """
        pass

    def addUint8(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_uint8(const Datagram self, int value)
        
        /**
         * Adds an unsigned 8-bit integer to the datagram.
         */
        """
        pass

    def addWstring(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_wstring(const Datagram self, unicode str)
        
        /**
         * Adds a variable-length wstring to the datagram.
         */
        """
        pass

    def addZString(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_z_string(const Datagram self, str str)
        
        /**
         * Adds a variable-length string to the datagram, as a NULL-terminated string.
         */
        """
        pass

    def add_be_float32(self, const_Datagram_self, float_value): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_be_float32(const Datagram self, float value)
        
        /**
         * Adds a 32-bit single-precision big-endian floating-point number to the
         * datagram.
         */
        """
        pass

    def add_be_float64(self, const_Datagram_self, double_value): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_be_float64(const Datagram self, double value)
        
        /**
         * Adds a 64-bit big-endian floating-point number to the datagram.
         */
        """
        pass

    def add_be_int16(self, const_Datagram_self, int_value): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_be_int16(const Datagram self, int value)
        
        // These functions pack numbers big-endian, in case that's desired.
        
        /**
         * Adds a signed 16-bit big-endian integer to the datagram.
         */
        """
        pass

    def add_be_int32(self, const_Datagram_self, int_value): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_be_int32(const Datagram self, int value)
        
        /**
         * Adds a signed 32-bit big-endian integer to the datagram.
         */
        """
        pass

    def add_be_int64(self, const_Datagram_self, long_value): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_be_int64(const Datagram self, long value)
        
        /**
         * Adds a signed 64-bit big-endian integer to the datagram.
         */
        """
        pass

    def add_be_uint16(self, const_Datagram_self, int_value): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_be_uint16(const Datagram self, int value)
        
        /**
         * Adds an unsigned 16-bit big-endian integer to the datagram.
         */
        """
        pass

    def add_be_uint32(self, const_Datagram_self, int_value): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_be_uint32(const Datagram self, int value)
        
        /**
         * Adds an unsigned 32-bit big-endian integer to the datagram.
         */
        """
        pass

    def add_be_uint64(self, const_Datagram_self, long_value): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_be_uint64(const Datagram self, long value)
        
        /**
         * Adds an unsigned 64-bit big-endian integer to the datagram.
         */
        """
        pass

    def add_blob(self, const_Datagram_self, bytes_param0): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_blob(const Datagram self, bytes param0)
        
        /**
         * Adds a variable-length binary blob to the datagram.  This actually adds a
         * count followed by n bytes.
         */
        """
        pass

    def add_blob32(self, const_Datagram_self, bytes_param0): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_blob32(const Datagram self, bytes param0)
        
        /**
         * Adds a variable-length binary blob to the datagram, using a 32-bit length
         * field to allow very long blobs.
         */
        """
        pass

    def add_bool(self, const_Datagram_self, bool_value): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_bool(const Datagram self, bool value)
        
        /**
         * Adds a boolean value to the datagram.
         */
        """
        pass

    def add_fixed_string(self, const_Datagram_self, str_str, int_size): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_fixed_string(const Datagram self, str str, int size)
        
        /**
         * Adds a fixed-length string to the datagram.  If the string given is less
         * than the requested size, this will pad the string out with zeroes; if it is
         * greater than the requested size, this will silently truncate the string.
         */
        """
        pass

    def add_float32(self, const_Datagram_self, float_value): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_float32(const Datagram self, float value)
        
        /**
         * Adds a 32-bit single-precision floating-point number to the datagram.
         * Since this kind of float is not necessarily portable across different
         * architectures, special care is required.
         */
        """
        pass

    def add_float64(self, const_Datagram_self, double_value): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_float64(const Datagram self, double value)
        
        /**
         * Adds a 64-bit floating-point number to the datagram.
         */
        """
        pass

    def add_int16(self, const_Datagram_self, int_value): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_int16(const Datagram self, int value)
        
        // The default numeric packing is little-endian.
        
        /**
         * Adds a signed 16-bit integer to the datagram.
         */
        """
        pass

    def add_int32(self, const_Datagram_self, int_value): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_int32(const Datagram self, int value)
        
        /**
         * Adds a signed 32-bit integer to the datagram.
         */
        """
        pass

    def add_int64(self, const_Datagram_self, long_value): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_int64(const Datagram self, long value)
        
        /**
         * Adds a signed 64-bit integer to the datagram.
         */
        """
        pass

    def add_int8(self, const_Datagram_self, int_value): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_int8(const Datagram self, int value)
        
        /**
         * Adds a signed 8-bit integer to the datagram.
         */
        """
        pass

    def add_stdfloat(self, const_Datagram_self, float_value): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_stdfloat(const Datagram self, float value)
        
        /**
         * Adds either a 32-bit or a 64-bit floating-point number, according to
         * set_stdfloat_double().
         */
        """
        pass

    def add_string(self, const_Datagram_self, str_str): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_string(const Datagram self, str str)
        
        /**
         * Adds a variable-length string to the datagram.  This actually adds a count
         * followed by n bytes.
         */
        """
        pass

    def add_string32(self, const_Datagram_self, str_str): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_string32(const Datagram self, str str)
        
        /**
         * Adds a variable-length string to the datagram, using a 32-bit length field
         * to allow very long strings.
         */
        """
        pass

    def add_uint16(self, const_Datagram_self, int_value): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_uint16(const Datagram self, int value)
        
        /**
         * Adds an unsigned 16-bit integer to the datagram.
         */
        """
        pass

    def add_uint32(self, const_Datagram_self, int_value): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_uint32(const Datagram self, int value)
        
        /**
         * Adds an unsigned 32-bit integer to the datagram.
         */
        """
        pass

    def add_uint64(self, const_Datagram_self, long_value): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_uint64(const Datagram self, long value)
        
        /**
         * Adds an unsigned 64-bit integer to the datagram.
         */
        """
        pass

    def add_uint8(self, const_Datagram_self, int_value): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_uint8(const Datagram self, int value)
        
        /**
         * Adds an unsigned 8-bit integer to the datagram.
         */
        """
        pass

    def add_wstring(self, const_Datagram_self, unicode_str): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_wstring(const Datagram self, unicode str)
        
        /**
         * Adds a variable-length wstring to the datagram.
         */
        """
        pass

    def add_z_string(self, const_Datagram_self, str_str): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_z_string(const Datagram self, str str)
        
        /**
         * Adds a variable-length string to the datagram, as a NULL-terminated string.
         */
        """
        pass

    def appendData(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        append_data(const Datagram self, bytes data)
        
        /**
         * Appends some more raw data to the end of the datagram.
         */
        
        /**
         * Appends some more raw data to the end of the datagram.
         */
        """
        pass

    def append_data(self, const_Datagram_self, bytes_data): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        append_data(const Datagram self, bytes data)
        
        /**
         * Appends some more raw data to the end of the datagram.
         */
        
        /**
         * Appends some more raw data to the end of the datagram.
         */
        """
        pass

    def assign(self, const_Datagram_self, const_Datagram_copy): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        assign(const Datagram self, const Datagram copy)
        """
        pass

    def Bytes(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        __bytes__(Datagram self)
        """
        pass

    def clear(self, const_Datagram_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear(const Datagram self)
        
        /**
         * Resets the datagram to empty, in preparation for building up a new
         * datagram.
         */
        """
        pass

    def copyArray(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        copy_array(const Datagram self, ConstPointerToArray data)
        
        /**
         * Replaces the data in the Datagram with a copy of the data in the indicated
         * CPTA_uchar.  Unlike set_array(), a complete copy is made of the data;
         * subsequent changes to the Datagram will *not* change the source CPTA_uchar.
         */
        """
        pass

    def copy_array(self, const_Datagram_self, ConstPointerToArray_data): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        copy_array(const Datagram self, ConstPointerToArray data)
        
        /**
         * Replaces the data in the Datagram with a copy of the data in the indicated
         * CPTA_uchar.  Unlike set_array(), a complete copy is made of the data;
         * subsequent changes to the Datagram will *not* change the source CPTA_uchar.
         */
        """
        pass

    def dumpHex(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        dump_hex(Datagram self, ostream out, int indent)
        
        /**
         * Writes a representation of the entire datagram contents, as a sequence of
         * hex (and ASCII) values.
         */
        """
        pass

    def dump_hex(self, Datagram_self, ostream_out, int_indent): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        dump_hex(Datagram self, ostream out, int indent)
        
        /**
         * Writes a representation of the entire datagram contents, as a sequence of
         * hex (and ASCII) values.
         */
        """
        pass

    def getArray(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_array(Datagram self)
        
        /**
         * Returns a const pointer to the actual data in the Datagram.
         */
        """
        pass

    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getLength(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_length(Datagram self)
        
        /**
         * Returns the number of bytes in the datagram.
         */
        """
        pass

    def getMessage(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_message(Datagram self)
        
        /**
         * Returns the datagram's data as a string.
         */
        """
        pass

    def getStdfloatDouble(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_stdfloat_double(Datagram self)
        
        /**
         * Returns the stdfloat_double flag.  See set_stdfloat_double().
         */
        """
        pass

    def get_array(self, Datagram_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_array(Datagram self)
        
        /**
         * Returns a const pointer to the actual data in the Datagram.
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_length(self, Datagram_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_length(Datagram self)
        
        /**
         * Returns the number of bytes in the datagram.
         */
        """
        pass

    def get_message(self, Datagram_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_message(Datagram self)
        
        /**
         * Returns the datagram's data as a string.
         */
        """
        pass

    def get_stdfloat_double(self, Datagram_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_stdfloat_double(Datagram self)
        
        /**
         * Returns the stdfloat_double flag.  See set_stdfloat_double().
         */
        """
        pass

    def modifyArray(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        modify_array(const Datagram self)
        
        /**
         * Returns a modifiable pointer to the actual data in the Datagram.
         */
        """
        pass

    def modify_array(self, const_Datagram_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        modify_array(const Datagram self)
        
        /**
         * Returns a modifiable pointer to the actual data in the Datagram.
         */
        """
        pass

    def output(self, Datagram_self, ostream_out): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        output(Datagram self, ostream out)
        
        /**
         * Write a string representation of this instance to <out>.
         */
        """
        pass

    def padBytes(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        pad_bytes(const Datagram self, int size)
        
        /**
         * Adds the indicated number of zero bytes to the datagram.
         */
        """
        pass

    def pad_bytes(self, const_Datagram_self, int_size): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        pad_bytes(const Datagram self, int size)
        
        /**
         * Adds the indicated number of zero bytes to the datagram.
         */
        """
        pass

    def setArray(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_array(const Datagram self, PointerToArray data)
        
        /**
         * Replaces the data in the Datagram with the data in the indicated PTA_uchar.
         * This is assignment by reference: subsequent changes to the Datagram will
         * also change the source PTA_uchar.
         */
        """
        pass

    def setStdfloatDouble(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_stdfloat_double(const Datagram self, bool stdfloat_double)
        
        /**
         * Changes the stdfloat_double flag, which defines the operation performed by
         * add_stdfloat() and DatagramIterator::get_stdfloat().  When this is true,
         * add_stdfloat() adds a 64-bit floating-point number; when it is false, it
         * adds a 32-bit floating-point number.  The default is based on the
         * STDFLOAT_DOUBLE compilation flag.
         */
        """
        pass

    def set_array(self, const_Datagram_self, PointerToArray_data): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_array(const Datagram self, PointerToArray data)
        
        /**
         * Replaces the data in the Datagram with the data in the indicated PTA_uchar.
         * This is assignment by reference: subsequent changes to the Datagram will
         * also change the source PTA_uchar.
         */
        """
        pass

    def set_stdfloat_double(self, const_Datagram_self, bool_stdfloat_double): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_stdfloat_double(const Datagram self, bool stdfloat_double)
        
        /**
         * Changes the stdfloat_double flag, which defines the operation performed by
         * add_stdfloat() and DatagramIterator::get_stdfloat().  When this is true,
         * add_stdfloat() adds a 64-bit floating-point number; when it is false, it
         * adds a 32-bit floating-point number.  The default is based on the
         * STDFLOAT_DOUBLE compilation flag.
         */
        """
        pass

    def write(self, Datagram_self, ostream_out, int_indent): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        write(Datagram self, ostream out, int indent)
        
        /**
         * Write a string representation of this instance to <out>.
         */
        """
        pass

    def __bytes__(self, Datagram_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        __bytes__(Datagram self)
        """
        pass

    def __copy__(self, *args, **kwargs): # real signature unknown
        pass

    def __deepcopy__(self, *args, **kwargs): # real signature unknown
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __hash__(self, *args, **kwargs): # real signature unknown
        """ Return hash(self). """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __reduce__(self, Datagram_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        __reduce__(Datagram self)
        """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    DtoolClassDict = {
        'Bytes': None, # (!) real value is "<method 'Bytes' of 'panda3d.core.Datagram' objects>"
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__bytes__': None, # (!) real value is "<method '__bytes__' of 'panda3d.core.Datagram' objects>"
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.core.Datagram' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.core.Datagram' objects>"
        '__doc__': '/**\n * An ordered list of data elements, formatted in memory for transmission over\n * a socket or writing to a data file.\n *\n * Data elements should be added one at a time, in order, to the Datagram.\n * The nature and contents of the data elements are totally up to the user.\n * When a Datagram has been transmitted and received, its data elements may be\n * extracted using a DatagramIterator; it is up to the caller to know the\n * correct type of each data element in order.\n *\n * A Datagram is itself headerless; it is simply a collection of data\n * elements.\n */',
        '__eq__': None, # (!) real value is "<slot wrapper '__eq__' of 'panda3d.core.Datagram' objects>"
        '__ge__': None, # (!) real value is "<slot wrapper '__ge__' of 'panda3d.core.Datagram' objects>"
        '__gt__': None, # (!) real value is "<slot wrapper '__gt__' of 'panda3d.core.Datagram' objects>"
        '__hash__': None, # (!) real value is "<slot wrapper '__hash__' of 'panda3d.core.Datagram' objects>"
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.Datagram' objects>"
        '__le__': None, # (!) real value is "<slot wrapper '__le__' of 'panda3d.core.Datagram' objects>"
        '__lt__': None, # (!) real value is "<slot wrapper '__lt__' of 'panda3d.core.Datagram' objects>"
        '__ne__': None, # (!) real value is "<slot wrapper '__ne__' of 'panda3d.core.Datagram' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE277950>'
        '__reduce__': None, # (!) real value is "<method '__reduce__' of 'panda3d.core.Datagram' objects>"
        '__repr__': None, # (!) real value is "<slot wrapper '__repr__' of 'panda3d.core.Datagram' objects>"
        '__str__': None, # (!) real value is "<slot wrapper '__str__' of 'panda3d.core.Datagram' objects>"
        'addBeFloat32': None, # (!) real value is "<method 'addBeFloat32' of 'panda3d.core.Datagram' objects>"
        'addBeFloat64': None, # (!) real value is "<method 'addBeFloat64' of 'panda3d.core.Datagram' objects>"
        'addBeInt16': None, # (!) real value is "<method 'addBeInt16' of 'panda3d.core.Datagram' objects>"
        'addBeInt32': None, # (!) real value is "<method 'addBeInt32' of 'panda3d.core.Datagram' objects>"
        'addBeInt64': None, # (!) real value is "<method 'addBeInt64' of 'panda3d.core.Datagram' objects>"
        'addBeUint16': None, # (!) real value is "<method 'addBeUint16' of 'panda3d.core.Datagram' objects>"
        'addBeUint32': None, # (!) real value is "<method 'addBeUint32' of 'panda3d.core.Datagram' objects>"
        'addBeUint64': None, # (!) real value is "<method 'addBeUint64' of 'panda3d.core.Datagram' objects>"
        'addBlob': None, # (!) real value is "<method 'addBlob' of 'panda3d.core.Datagram' objects>"
        'addBlob32': None, # (!) real value is "<method 'addBlob32' of 'panda3d.core.Datagram' objects>"
        'addBool': None, # (!) real value is "<method 'addBool' of 'panda3d.core.Datagram' objects>"
        'addFixedString': None, # (!) real value is "<method 'addFixedString' of 'panda3d.core.Datagram' objects>"
        'addFloat32': None, # (!) real value is "<method 'addFloat32' of 'panda3d.core.Datagram' objects>"
        'addFloat64': None, # (!) real value is "<method 'addFloat64' of 'panda3d.core.Datagram' objects>"
        'addInt16': None, # (!) real value is "<method 'addInt16' of 'panda3d.core.Datagram' objects>"
        'addInt32': None, # (!) real value is "<method 'addInt32' of 'panda3d.core.Datagram' objects>"
        'addInt64': None, # (!) real value is "<method 'addInt64' of 'panda3d.core.Datagram' objects>"
        'addInt8': None, # (!) real value is "<method 'addInt8' of 'panda3d.core.Datagram' objects>"
        'addStdfloat': None, # (!) real value is "<method 'addStdfloat' of 'panda3d.core.Datagram' objects>"
        'addString': None, # (!) real value is "<method 'addString' of 'panda3d.core.Datagram' objects>"
        'addString32': None, # (!) real value is "<method 'addString32' of 'panda3d.core.Datagram' objects>"
        'addUint16': None, # (!) real value is "<method 'addUint16' of 'panda3d.core.Datagram' objects>"
        'addUint32': None, # (!) real value is "<method 'addUint32' of 'panda3d.core.Datagram' objects>"
        'addUint64': None, # (!) real value is "<method 'addUint64' of 'panda3d.core.Datagram' objects>"
        'addUint8': None, # (!) real value is "<method 'addUint8' of 'panda3d.core.Datagram' objects>"
        'addWstring': None, # (!) real value is "<method 'addWstring' of 'panda3d.core.Datagram' objects>"
        'addZString': None, # (!) real value is "<method 'addZString' of 'panda3d.core.Datagram' objects>"
        'add_be_float32': None, # (!) real value is "<method 'add_be_float32' of 'panda3d.core.Datagram' objects>"
        'add_be_float64': None, # (!) real value is "<method 'add_be_float64' of 'panda3d.core.Datagram' objects>"
        'add_be_int16': None, # (!) real value is "<method 'add_be_int16' of 'panda3d.core.Datagram' objects>"
        'add_be_int32': None, # (!) real value is "<method 'add_be_int32' of 'panda3d.core.Datagram' objects>"
        'add_be_int64': None, # (!) real value is "<method 'add_be_int64' of 'panda3d.core.Datagram' objects>"
        'add_be_uint16': None, # (!) real value is "<method 'add_be_uint16' of 'panda3d.core.Datagram' objects>"
        'add_be_uint32': None, # (!) real value is "<method 'add_be_uint32' of 'panda3d.core.Datagram' objects>"
        'add_be_uint64': None, # (!) real value is "<method 'add_be_uint64' of 'panda3d.core.Datagram' objects>"
        'add_blob': None, # (!) real value is "<method 'add_blob' of 'panda3d.core.Datagram' objects>"
        'add_blob32': None, # (!) real value is "<method 'add_blob32' of 'panda3d.core.Datagram' objects>"
        'add_bool': None, # (!) real value is "<method 'add_bool' of 'panda3d.core.Datagram' objects>"
        'add_fixed_string': None, # (!) real value is "<method 'add_fixed_string' of 'panda3d.core.Datagram' objects>"
        'add_float32': None, # (!) real value is "<method 'add_float32' of 'panda3d.core.Datagram' objects>"
        'add_float64': None, # (!) real value is "<method 'add_float64' of 'panda3d.core.Datagram' objects>"
        'add_int16': None, # (!) real value is "<method 'add_int16' of 'panda3d.core.Datagram' objects>"
        'add_int32': None, # (!) real value is "<method 'add_int32' of 'panda3d.core.Datagram' objects>"
        'add_int64': None, # (!) real value is "<method 'add_int64' of 'panda3d.core.Datagram' objects>"
        'add_int8': None, # (!) real value is "<method 'add_int8' of 'panda3d.core.Datagram' objects>"
        'add_stdfloat': None, # (!) real value is "<method 'add_stdfloat' of 'panda3d.core.Datagram' objects>"
        'add_string': None, # (!) real value is "<method 'add_string' of 'panda3d.core.Datagram' objects>"
        'add_string32': None, # (!) real value is "<method 'add_string32' of 'panda3d.core.Datagram' objects>"
        'add_uint16': None, # (!) real value is "<method 'add_uint16' of 'panda3d.core.Datagram' objects>"
        'add_uint32': None, # (!) real value is "<method 'add_uint32' of 'panda3d.core.Datagram' objects>"
        'add_uint64': None, # (!) real value is "<method 'add_uint64' of 'panda3d.core.Datagram' objects>"
        'add_uint8': None, # (!) real value is "<method 'add_uint8' of 'panda3d.core.Datagram' objects>"
        'add_wstring': None, # (!) real value is "<method 'add_wstring' of 'panda3d.core.Datagram' objects>"
        'add_z_string': None, # (!) real value is "<method 'add_z_string' of 'panda3d.core.Datagram' objects>"
        'appendData': None, # (!) real value is "<method 'appendData' of 'panda3d.core.Datagram' objects>"
        'append_data': None, # (!) real value is "<method 'append_data' of 'panda3d.core.Datagram' objects>"
        'assign': None, # (!) real value is "<method 'assign' of 'panda3d.core.Datagram' objects>"
        'clear': None, # (!) real value is "<method 'clear' of 'panda3d.core.Datagram' objects>"
        'copyArray': None, # (!) real value is "<method 'copyArray' of 'panda3d.core.Datagram' objects>"
        'copy_array': None, # (!) real value is "<method 'copy_array' of 'panda3d.core.Datagram' objects>"
        'dumpHex': None, # (!) real value is "<method 'dumpHex' of 'panda3d.core.Datagram' objects>"
        'dump_hex': None, # (!) real value is "<method 'dump_hex' of 'panda3d.core.Datagram' objects>"
        'getArray': None, # (!) real value is "<method 'getArray' of 'panda3d.core.Datagram' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE277950>)>'
        'getLength': None, # (!) real value is "<method 'getLength' of 'panda3d.core.Datagram' objects>"
        'getMessage': None, # (!) real value is "<method 'getMessage' of 'panda3d.core.Datagram' objects>"
        'getStdfloatDouble': None, # (!) real value is "<method 'getStdfloatDouble' of 'panda3d.core.Datagram' objects>"
        'get_array': None, # (!) real value is "<method 'get_array' of 'panda3d.core.Datagram' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE277950>)>'
        'get_length': None, # (!) real value is "<method 'get_length' of 'panda3d.core.Datagram' objects>"
        'get_message': None, # (!) real value is "<method 'get_message' of 'panda3d.core.Datagram' objects>"
        'get_stdfloat_double': None, # (!) real value is "<method 'get_stdfloat_double' of 'panda3d.core.Datagram' objects>"
        'modifyArray': None, # (!) real value is "<method 'modifyArray' of 'panda3d.core.Datagram' objects>"
        'modify_array': None, # (!) real value is "<method 'modify_array' of 'panda3d.core.Datagram' objects>"
        'output': None, # (!) real value is "<method 'output' of 'panda3d.core.Datagram' objects>"
        'padBytes': None, # (!) real value is "<method 'padBytes' of 'panda3d.core.Datagram' objects>"
        'pad_bytes': None, # (!) real value is "<method 'pad_bytes' of 'panda3d.core.Datagram' objects>"
        'setArray': None, # (!) real value is "<method 'setArray' of 'panda3d.core.Datagram' objects>"
        'setStdfloatDouble': None, # (!) real value is "<method 'setStdfloatDouble' of 'panda3d.core.Datagram' objects>"
        'set_array': None, # (!) real value is "<method 'set_array' of 'panda3d.core.Datagram' objects>"
        'set_stdfloat_double': None, # (!) real value is "<method 'set_stdfloat_double' of 'panda3d.core.Datagram' objects>"
        'write': None, # (!) real value is "<method 'write' of 'panda3d.core.Datagram' objects>"
    }


