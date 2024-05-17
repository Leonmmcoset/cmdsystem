# encoding: utf-8
# module panda3d.direct
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\direct.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import panda3d.core as __panda3d_core


class DCPacker(__dtoolconfig.DTOOL_SUPER_BASE):
    """
    /**
     * This class can be used for packing a series of numeric and string data into
     * a binary stream, according to the DC specification.
     *
     * See also direct/src/doc/dcPacker.txt for a more complete description and
     * examples of using this class.
     */
    """
    def beginPack(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        begin_pack(const DCPacker self, const DCPackerInterface root)
        
        /**
         * Begins a packing session.  The parameter is the DC object that describes
         * the packing format; it may be a DCParameter or DCField.
         *
         * Unless you call clear_data() between sessions, multiple packing sessions
         * will be concatenated together into the same buffer.  If you wish to add
         * bytes to the buffer between packing sessions, use append_data() or
         * get_write_pointer().
         */
        """
        pass

    def beginRepack(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        begin_repack(const DCPacker self, const DCPackerInterface root)
        
        /**
         * Begins a repacking session.  You must have previously called
         * set_unpack_data() to specify a buffer to unpack.
         *
         * Unlike begin_pack() or begin_unpack() you may not concatenate the results
         * of multiple begin_repack() sessions in one buffer.
         *
         * Also, unlike in packing or unpacking modes, you may not walk through the
         * fields from beginning to end, or even pack two consecutive fields at once.
         * Instead, you must call seek() for each field you wish to modify and pack
         * only that one field; then call seek() again to modify another field.
         */
        """
        pass

    def beginUnpack(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        begin_unpack(const DCPacker self, const DCPackerInterface root)
        
        /**
         * Begins an unpacking session.  You must have previously called
         * set_unpack_data() to specify a buffer to unpack.
         *
         * If there was data left in the buffer after a previous begin_unpack() ..
         * end_unpack() session, the new session will resume from the current point.
         * This method may be used, therefore, to unpack a sequence of objects from
         * the same buffer.
         */
        """
        pass

    def begin_pack(self, const_DCPacker_self, const_DCPackerInterface_root): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        begin_pack(const DCPacker self, const DCPackerInterface root)
        
        /**
         * Begins a packing session.  The parameter is the DC object that describes
         * the packing format; it may be a DCParameter or DCField.
         *
         * Unless you call clear_data() between sessions, multiple packing sessions
         * will be concatenated together into the same buffer.  If you wish to add
         * bytes to the buffer between packing sessions, use append_data() or
         * get_write_pointer().
         */
        """
        pass

    def begin_repack(self, const_DCPacker_self, const_DCPackerInterface_root): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        begin_repack(const DCPacker self, const DCPackerInterface root)
        
        /**
         * Begins a repacking session.  You must have previously called
         * set_unpack_data() to specify a buffer to unpack.
         *
         * Unlike begin_pack() or begin_unpack() you may not concatenate the results
         * of multiple begin_repack() sessions in one buffer.
         *
         * Also, unlike in packing or unpacking modes, you may not walk through the
         * fields from beginning to end, or even pack two consecutive fields at once.
         * Instead, you must call seek() for each field you wish to modify and pack
         * only that one field; then call seek() again to modify another field.
         */
        """
        pass

    def begin_unpack(self, const_DCPacker_self, const_DCPackerInterface_root): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        begin_unpack(const DCPacker self, const DCPackerInterface root)
        
        /**
         * Begins an unpacking session.  You must have previously called
         * set_unpack_data() to specify a buffer to unpack.
         *
         * If there was data left in the buffer after a previous begin_unpack() ..
         * end_unpack() session, the new session will resume from the current point.
         * This method may be used, therefore, to unpack a sequence of objects from
         * the same buffer.
         */
        """
        pass

    def clearData(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_data(const DCPacker self)
        
        /**
         * Empties the data in the pack buffer and unpack buffer.  This should be
         * called between calls to begin_pack(), unless you want to concatenate all of
         * the pack results together.
         */
        """
        pass

    def clear_data(self, const_DCPacker_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_data(const DCPacker self)
        
        /**
         * Empties the data in the pack buffer and unpack buffer.  This should be
         * called between calls to begin_pack(), unless you want to concatenate all of
         * the pack results together.
         */
        """
        pass

    def endPack(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        end_pack(const DCPacker self)
        
        /**
         * Finishes a packing session.
         *
         * The return value is true on success, or false if there has been some error
         * during packing.
         */
        """
        pass

    def endRepack(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        end_repack(const DCPacker self)
        
        /**
         * Finishes the repacking session.
         *
         * The return value is true on success, or false if there has been some error
         * during repacking (or if all fields have not been repacked).
         */
        """
        pass

    def endUnpack(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        end_unpack(const DCPacker self)
        
        /**
         * Finishes the unpacking session.
         *
         * The return value is true on success, or false if there has been some error
         * during unpacking (or if all fields have not been unpacked).
         */
        """
        pass

    def end_pack(self, const_DCPacker_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        end_pack(const DCPacker self)
        
        /**
         * Finishes a packing session.
         *
         * The return value is true on success, or false if there has been some error
         * during packing.
         */
        """
        pass

    def end_repack(self, const_DCPacker_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        end_repack(const DCPacker self)
        
        /**
         * Finishes the repacking session.
         *
         * The return value is true on success, or false if there has been some error
         * during repacking (or if all fields have not been repacked).
         */
        """
        pass

    def end_unpack(self, const_DCPacker_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        end_unpack(const DCPacker self)
        
        /**
         * Finishes the unpacking session.
         *
         * The return value is true on success, or false if there has been some error
         * during unpacking (or if all fields have not been unpacked).
         */
        """
        pass

    def getBytes(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_bytes(DCPacker self)
        
        /**
         * Returns the packed data buffer as a bytes object.  Also see get_data().
         */
        """
        pass

    def getCurrentField(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_current_field(DCPacker self)
        
        /**
         * Returns the field that will be referenced by the next call to pack_*() or
         * unpack_*().  This will be NULL if we have unpacked (or packed) all fields,
         * or if it is time to call pop().
         */
        """
        pass

    def getCurrentFieldName(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_current_field_name(DCPacker self)
        
        /**
         * Returns the name of the current field, if it has a name, or the empty
         * string if the field does not have a name or there is no current field.
         */
        """
        pass

    def getCurrentParent(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_current_parent(DCPacker self)
        
        /**
         * Returns the field that we left in our last call to push(): the owner of the
         * current level of fields.  This may be NULL at the beginning of the pack
         * operation.
         */
        """
        pass

    def getLastSwitch(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_last_switch(DCPacker self)
        
        /**
         * Returns a pointer to the last DCSwitch instance that we have passed by and
         * selected one case of during the pack/unpack process.  Each time we
         * encounter a new DCSwitch and select a case, this will change state.
         *
         * This may be used to detect when a DCSwitch has been selected.  At the
         * moment this changes state, get_current_parent() will contain the particular
         * SwitchCase that was selected by the switch.
         */
        """
        pass

    def getLength(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_length(DCPacker self)
        
        /**
         * Returns the current length of the buffer.  This is the number of useful
         * bytes stored in the buffer, not the amount of memory it takes up.
         */
        """
        pass

    def getNumNestedFields(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_nested_fields(DCPacker self)
        
        /**
         * Returns the number of nested fields associated with the current field, if
         * has_nested_fields() returned true.
         *
         * The return value may be -1 to indicate that a variable number of nested
         * fields are accepted by this field type (e.g.  a variable-length array).
         *
         * Note that this method is unreliable to determine how many fields you must
         * traverse before you can call pop(), since particularly in the presence of a
         * DCSwitch, it may change during traversal.  Use more_nested_fields()
         * instead.
         */
        """
        pass

    def getNumStackElementsEverAllocated(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_stack_elements_ever_allocated()
        
        /**
         * Returns the number of DCPacker::StackElement pointers ever simultaneously
         * allocated; these are now either in active use or have been recycled into
         * the deleted DCPacker::StackElement pool to be used again.
         */
        """
        pass

    def getNumUnpackedBytes(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_unpacked_bytes(DCPacker self)
        
        /**
         * Returns the number of bytes that have been unpacked so far, or after
         * unpack_end(), the total number of bytes that were unpacked at all.  This
         * can be used to validate that all of the bytes in the buffer were actually
         * unpacked (which is not otherwise considered an error).
         */
        """
        pass

    def getPackType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_pack_type(DCPacker self)
        
        /**
         * Returns the type of value expected by the current field.  See the
         * enumerated type definition at the top of DCPackerInterface.h.  If this
         * returns one of PT_double, PT_int, PT_int64, or PT_string, then you should
         * call the corresponding pack_double(), pack_int() function (or
         * unpack_double(), unpack_int(), etc.) to transfer data.  Otherwise, you
         * should call push() and begin packing or unpacking the nested fields.
         */
        """
        pass

    def getString(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_string(DCPacker self)
        
        /**
         * Returns the packed data buffer as a string.  Also see get_data().
         */
        
        /**
         * Copies the packed data into the indicated string.  Also see get_data().
         */
        """
        pass

    def getUnpackLength(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_unpack_length(DCPacker self)
        
        /**
         * Returns the total number of bytes in the unpack data buffer.  This is the
         * buffer used when unpacking; it is separate from the pack data returned by
         * get_length(), which is filled during packing.
         */
        """
        pass

    def getUnpackString(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_unpack_string(DCPacker self)
        
        /**
         * Returns the unpack data buffer, as a string.  This is the buffer used when
         * unpacking; it is separate from the pack data returned by get_string(),
         * which is filled during packing.  Also see get_unpack_data().
         */
        """
        pass

    def get_bytes(self, DCPacker_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_bytes(DCPacker self)
        
        /**
         * Returns the packed data buffer as a bytes object.  Also see get_data().
         */
        """
        pass

    def get_current_field(self, DCPacker_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_current_field(DCPacker self)
        
        /**
         * Returns the field that will be referenced by the next call to pack_*() or
         * unpack_*().  This will be NULL if we have unpacked (or packed) all fields,
         * or if it is time to call pop().
         */
        """
        pass

    def get_current_field_name(self, DCPacker_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_current_field_name(DCPacker self)
        
        /**
         * Returns the name of the current field, if it has a name, or the empty
         * string if the field does not have a name or there is no current field.
         */
        """
        pass

    def get_current_parent(self, DCPacker_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_current_parent(DCPacker self)
        
        /**
         * Returns the field that we left in our last call to push(): the owner of the
         * current level of fields.  This may be NULL at the beginning of the pack
         * operation.
         */
        """
        pass

    def get_last_switch(self, DCPacker_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_last_switch(DCPacker self)
        
        /**
         * Returns a pointer to the last DCSwitch instance that we have passed by and
         * selected one case of during the pack/unpack process.  Each time we
         * encounter a new DCSwitch and select a case, this will change state.
         *
         * This may be used to detect when a DCSwitch has been selected.  At the
         * moment this changes state, get_current_parent() will contain the particular
         * SwitchCase that was selected by the switch.
         */
        """
        pass

    def get_length(self, DCPacker_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_length(DCPacker self)
        
        /**
         * Returns the current length of the buffer.  This is the number of useful
         * bytes stored in the buffer, not the amount of memory it takes up.
         */
        """
        pass

    def get_num_nested_fields(self, DCPacker_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_nested_fields(DCPacker self)
        
        /**
         * Returns the number of nested fields associated with the current field, if
         * has_nested_fields() returned true.
         *
         * The return value may be -1 to indicate that a variable number of nested
         * fields are accepted by this field type (e.g.  a variable-length array).
         *
         * Note that this method is unreliable to determine how many fields you must
         * traverse before you can call pop(), since particularly in the presence of a
         * DCSwitch, it may change during traversal.  Use more_nested_fields()
         * instead.
         */
        """
        pass

    def get_num_stack_elements_ever_allocated(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_stack_elements_ever_allocated()
        
        /**
         * Returns the number of DCPacker::StackElement pointers ever simultaneously
         * allocated; these are now either in active use or have been recycled into
         * the deleted DCPacker::StackElement pool to be used again.
         */
        """
        pass

    def get_num_unpacked_bytes(self, DCPacker_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_unpacked_bytes(DCPacker self)
        
        /**
         * Returns the number of bytes that have been unpacked so far, or after
         * unpack_end(), the total number of bytes that were unpacked at all.  This
         * can be used to validate that all of the bytes in the buffer were actually
         * unpacked (which is not otherwise considered an error).
         */
        """
        pass

    def get_pack_type(self, DCPacker_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_pack_type(DCPacker self)
        
        /**
         * Returns the type of value expected by the current field.  See the
         * enumerated type definition at the top of DCPackerInterface.h.  If this
         * returns one of PT_double, PT_int, PT_int64, or PT_string, then you should
         * call the corresponding pack_double(), pack_int() function (or
         * unpack_double(), unpack_int(), etc.) to transfer data.  Otherwise, you
         * should call push() and begin packing or unpacking the nested fields.
         */
        """
        pass

    def get_string(self, DCPacker_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_string(DCPacker self)
        
        /**
         * Returns the packed data buffer as a string.  Also see get_data().
         */
        
        /**
         * Copies the packed data into the indicated string.  Also see get_data().
         */
        """
        pass

    def get_unpack_length(self, DCPacker_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_unpack_length(DCPacker self)
        
        /**
         * Returns the total number of bytes in the unpack data buffer.  This is the
         * buffer used when unpacking; it is separate from the pack data returned by
         * get_length(), which is filled during packing.
         */
        """
        pass

    def get_unpack_string(self, DCPacker_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_unpack_string(DCPacker self)
        
        /**
         * Returns the unpack data buffer, as a string.  This is the buffer used when
         * unpacking; it is separate from the pack data returned by get_string(),
         * which is filled during packing.  Also see get_unpack_data().
         */
        """
        pass

    def hadError(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        had_error(DCPacker self)
        
        /**
         * Returns true if there has been any error (either a pack error or a range
         * error) since the most recent call to begin().  If this returns true, then
         * the matching call to end() will indicate an error (false).
         */
        """
        pass

    def hadPackError(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        had_pack_error(DCPacker self)
        
        /**
         * Returns true if there has been an packing error since the most recent call
         * to begin(); in particular, this may be called after end() has returned
         * false to determine the nature of the failure.
         *
         * A return value of true indicates there was a push/pop mismatch, or the
         * push/pop structure did not match the data structure, or there were the
         * wrong number of elements in a nested push/pop structure, or on unpack that
         * the data stream was truncated.
         */
        """
        pass

    def hadParseError(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        had_parse_error(DCPacker self)
        
        /**
         * Returns true if there has been an parse error since the most recent call to
         * begin(); this can only happen if you call parse_and_pack().
         */
        """
        pass

    def hadRangeError(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        had_range_error(DCPacker self)
        
        /**
         * Returns true if there has been an range validation error since the most
         * recent call to begin(); in particular, this may be called after end() has
         * returned false to determine the nature of the failure.
         *
         * A return value of true indicates a value that was packed or unpacked did
         * not fit within the specified legal range for a parameter, or within the
         * limits of the field size.
         */
        """
        pass

    def had_error(self, DCPacker_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        had_error(DCPacker self)
        
        /**
         * Returns true if there has been any error (either a pack error or a range
         * error) since the most recent call to begin().  If this returns true, then
         * the matching call to end() will indicate an error (false).
         */
        """
        pass

    def had_pack_error(self, DCPacker_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        had_pack_error(DCPacker self)
        
        /**
         * Returns true if there has been an packing error since the most recent call
         * to begin(); in particular, this may be called after end() has returned
         * false to determine the nature of the failure.
         *
         * A return value of true indicates there was a push/pop mismatch, or the
         * push/pop structure did not match the data structure, or there were the
         * wrong number of elements in a nested push/pop structure, or on unpack that
         * the data stream was truncated.
         */
        """
        pass

    def had_parse_error(self, DCPacker_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        had_parse_error(DCPacker self)
        
        /**
         * Returns true if there has been an parse error since the most recent call to
         * begin(); this can only happen if you call parse_and_pack().
         */
        """
        pass

    def had_range_error(self, DCPacker_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        had_range_error(DCPacker self)
        
        /**
         * Returns true if there has been an range validation error since the most
         * recent call to begin(); in particular, this may be called after end() has
         * returned false to determine the nature of the failure.
         *
         * A return value of true indicates a value that was packed or unpacked did
         * not fit within the specified legal range for a parameter, or within the
         * limits of the field size.
         */
        """
        pass

    def hasNestedFields(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_nested_fields(DCPacker self)
        
        /**
         * Returns true if the current field has any nested fields (and thus expects a
         * push() .. pop() interface), or false otherwise.  If this returns true,
         * get_num_nested_fields() may be called to determine how many nested fields
         * are expected.
         */
        """
        pass

    def has_nested_fields(self, DCPacker_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_nested_fields(DCPacker self)
        
        /**
         * Returns true if the current field has any nested fields (and thus expects a
         * push() .. pop() interface), or false otherwise.  If this returns true,
         * get_num_nested_fields() may be called to determine how many nested fields
         * are expected.
         */
        """
        pass

    def moreNestedFields(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        more_nested_fields(DCPacker self)
        
        /**
         * Returns true if there are more nested fields to pack or unpack in the
         * current push sequence, false if it is time to call pop().
         */
        """
        pass

    def more_nested_fields(self, DCPacker_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        more_nested_fields(DCPacker self)
        
        /**
         * Returns true if there are more nested fields to pack or unpack in the
         * current push sequence, false if it is time to call pop().
         */
        """
        pass

    def packBlob(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        pack_blob(const DCPacker self, bytes value)
        
        /**
         * Packs the indicated numeric or string value into the stream.
         */
        """
        pass

    def packDefaultValue(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        pack_default_value(const DCPacker self)
        
        /**
         * Adds the default value for the current element into the stream.  If no
         * default has been set for the current element, creates a sensible default.
         */
        """
        pass

    def packDouble(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        pack_double(const DCPacker self, double value)
        
        /**
         * Packs the indicated numeric or string value into the stream.
         */
        """
        pass

    def packInt(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        pack_int(const DCPacker self, int value)
        
        /**
         * Packs the indicated numeric or string value into the stream.
         */
        """
        pass

    def packInt64(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        pack_int64(const DCPacker self, long value)
        
        /**
         * Packs the indicated numeric or string value into the stream.
         */
        """
        pass

    def packLiteralValue(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        pack_literal_value(const DCPacker self, bytes value)
        
        /**
         * Adds the indicated string value into the stream, representing a single pre-
         * packed field element, or a whole group of field elements at once.
         */
        """
        pass

    def packObject(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        pack_object(const DCPacker self, object object)
        
        /**
         * Packs the Python object of whatever type into the packer.  Each numeric
         * object and string object maps to the corresponding pack_value() call; a
         * tuple or sequence maps to a push() followed by all of the tuple's contents
         * followed by a pop().
         */
        """
        pass

    def packString(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        pack_string(const DCPacker self, str value)
        
        /**
         * Packs the indicated numeric or string value into the stream.
         */
        """
        pass

    def packUint(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        pack_uint(const DCPacker self, int value)
        
        /**
         * Packs the indicated numeric or string value into the stream.
         */
        """
        pass

    def packUint64(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        pack_uint64(const DCPacker self, long value)
        
        /**
         * Packs the indicated numeric or string value into the stream.
         */
        """
        pass

    def pack_blob(self, const_DCPacker_self, bytes_value): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        pack_blob(const DCPacker self, bytes value)
        
        /**
         * Packs the indicated numeric or string value into the stream.
         */
        """
        pass

    def pack_default_value(self, const_DCPacker_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        pack_default_value(const DCPacker self)
        
        /**
         * Adds the default value for the current element into the stream.  If no
         * default has been set for the current element, creates a sensible default.
         */
        """
        pass

    def pack_double(self, const_DCPacker_self, double_value): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        pack_double(const DCPacker self, double value)
        
        /**
         * Packs the indicated numeric or string value into the stream.
         */
        """
        pass

    def pack_int(self, const_DCPacker_self, int_value): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        pack_int(const DCPacker self, int value)
        
        /**
         * Packs the indicated numeric or string value into the stream.
         */
        """
        pass

    def pack_int64(self, const_DCPacker_self, long_value): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        pack_int64(const DCPacker self, long value)
        
        /**
         * Packs the indicated numeric or string value into the stream.
         */
        """
        pass

    def pack_literal_value(self, const_DCPacker_self, bytes_value): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        pack_literal_value(const DCPacker self, bytes value)
        
        /**
         * Adds the indicated string value into the stream, representing a single pre-
         * packed field element, or a whole group of field elements at once.
         */
        """
        pass

    def pack_object(self, const_DCPacker_self, object_object): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        pack_object(const DCPacker self, object object)
        
        /**
         * Packs the Python object of whatever type into the packer.  Each numeric
         * object and string object maps to the corresponding pack_value() call; a
         * tuple or sequence maps to a push() followed by all of the tuple's contents
         * followed by a pop().
         */
        """
        pass

    def pack_string(self, const_DCPacker_self, str_value): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        pack_string(const DCPacker self, str value)
        
        /**
         * Packs the indicated numeric or string value into the stream.
         */
        """
        pass

    def pack_uint(self, const_DCPacker_self, int_value): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        pack_uint(const DCPacker self, int value)
        
        /**
         * Packs the indicated numeric or string value into the stream.
         */
        """
        pass

    def pack_uint64(self, const_DCPacker_self, long_value): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        pack_uint64(const DCPacker self, long value)
        
        /**
         * Packs the indicated numeric or string value into the stream.
         */
        """
        pass

    def parseAndPack(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        parse_and_pack(const DCPacker self, istream in)
        parse_and_pack(const DCPacker self, str formatted_object)
        
        /**
         * Parses an object's value according to the DC file syntax (e.g.  as a
         * default value string) and packs it.  Returns true on success, false on a
         * parse error.
         */
        
        /**
         * Parses an object's value according to the DC file syntax (e.g.  as a
         * default value string) and packs it.  Returns true on success, false on a
         * parse error.
         */
        """
        pass

    def parse_and_pack(self, const_DCPacker_self, istream_in): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        parse_and_pack(const DCPacker self, istream in)
        parse_and_pack(const DCPacker self, str formatted_object)
        
        /**
         * Parses an object's value according to the DC file syntax (e.g.  as a
         * default value string) and packs it.  Returns true on success, false on a
         * parse error.
         */
        
        /**
         * Parses an object's value according to the DC file syntax (e.g.  as a
         * default value string) and packs it.  Returns true on success, false on a
         * parse error.
         */
        """
        pass

    def pop(self, const_DCPacker_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        pop(const DCPacker self)
        
        /**
         * Marks the end of a nested series of fields.
         *
         * This must be called to match a previous push() only after all the expected
         * number of nested fields have been packed.  It is an error to call it too
         * early, or too late.
         */
        """
        pass

    def push(self, const_DCPacker_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        push(const DCPacker self)
        
        /**
         * Marks the beginning of a nested series of fields.
         *
         * This must be called before filling the elements of an array or the
         * individual fields in a structure field.  It must also be balanced by a
         * matching pop().
         *
         * It is necessary to use push() / pop() only if has_nested_fields() returns
         * true.
         */
        """
        pass

    def rawPackBlob(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        raw_pack_blob(const DCPacker self, bytes value)
        
        /**
         * Packs the data into the buffer between packing sessions.
         */
        """
        pass

    def rawPackFloat64(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        raw_pack_float64(const DCPacker self, double value)
        
        /**
         * Packs the data into the buffer between packing sessions.
         */
        """
        pass

    def rawPackInt16(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        raw_pack_int16(const DCPacker self, int value)
        
        /**
         * Packs the data into the buffer between packing sessions.
         */
        """
        pass

    def rawPackInt32(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        raw_pack_int32(const DCPacker self, int value)
        
        /**
         * Packs the data into the buffer between packing sessions.
         */
        """
        pass

    def rawPackInt64(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        raw_pack_int64(const DCPacker self, long value)
        
        /**
         * Packs the data into the buffer between packing sessions.
         */
        """
        pass

    def rawPackInt8(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        raw_pack_int8(const DCPacker self, int value)
        
        /**
         * Packs the data into the buffer between packing sessions.
         */
        """
        pass

    def rawPackString(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        raw_pack_string(const DCPacker self, str value)
        
        /**
         * Packs the data into the buffer between packing sessions.
         */
        """
        pass

    def rawPackUint16(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        raw_pack_uint16(const DCPacker self, int value)
        
        /**
         * Packs the data into the buffer between packing sessions.
         */
        """
        pass

    def rawPackUint32(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        raw_pack_uint32(const DCPacker self, int value)
        
        /**
         * Packs the data into the buffer between packing sessions.
         */
        """
        pass

    def rawPackUint64(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        raw_pack_uint64(const DCPacker self, long value)
        
        /**
         * Packs the data into the buffer between packing sessions.
         */
        """
        pass

    def rawPackUint8(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        raw_pack_uint8(const DCPacker self, int value)
        
        /**
         * Packs the data into the buffer between packing sessions.
         */
        """
        pass

    def rawUnpackBlob(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        raw_unpack_blob(const DCPacker self)
        
        /**
         * Unpacks the data from the buffer between unpacking sessions.
         */
        
        /**
         * Unpacks the data from the buffer between unpacking sessions.
         */
        """
        pass

    def rawUnpackFloat64(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        raw_unpack_float64(const DCPacker self)
        
        /**
         * Unpacks the data from the buffer between unpacking sessions.
         */
        
        /**
         * Unpacks the data from the buffer between unpacking sessions.
         */
        """
        pass

    def rawUnpackInt16(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        raw_unpack_int16(const DCPacker self)
        
        /**
         * Unpacks the data from the buffer between unpacking sessions.
         */
        
        /**
         * Unpacks the data from the buffer between unpacking sessions.
         */
        """
        pass

    def rawUnpackInt32(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        raw_unpack_int32(const DCPacker self)
        
        /**
         * Unpacks the data from the buffer between unpacking sessions.
         */
        
        /**
         * Unpacks the data from the buffer between unpacking sessions.
         */
        """
        pass

    def rawUnpackInt64(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        raw_unpack_int64(const DCPacker self)
        
        /**
         * Unpacks the data from the buffer between unpacking sessions.
         */
        
        /**
         * Unpacks the data from the buffer between unpacking sessions.
         */
        """
        pass

    def rawUnpackInt8(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        raw_unpack_int8(const DCPacker self)
        
        /**
         * Unpacks the data from the buffer between unpacking sessions.
         */
        
        /**
         * Unpacks the data from the buffer between unpacking sessions.
         */
        """
        pass

    def rawUnpackString(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        raw_unpack_string(const DCPacker self)
        
        /**
         * Unpacks the data from the buffer between unpacking sessions.
         */
        
        /**
         * Unpacks the data from the buffer between unpacking sessions.
         */
        """
        pass

    def rawUnpackUint16(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        raw_unpack_uint16(const DCPacker self)
        
        /**
         * Unpacks the data from the buffer between unpacking sessions.
         */
        
        /**
         * Unpacks the data from the buffer between unpacking sessions.
         */
        """
        pass

    def rawUnpackUint32(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        raw_unpack_uint32(const DCPacker self)
        
        /**
         * Unpacks the data from the buffer between unpacking sessions.
         */
        
        /**
         * Unpacks the data from the buffer between unpacking sessions.
         */
        """
        pass

    def rawUnpackUint64(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        raw_unpack_uint64(const DCPacker self)
        
        /**
         * Unpacks the data from the buffer between unpacking sessions.
         */
        
        /**
         * Unpacks the data from the buffer between unpacking sessions.
         */
        """
        pass

    def rawUnpackUint8(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        raw_unpack_uint8(const DCPacker self)
        
        /**
         * Unpacks the data from the buffer between unpacking sessions.
         */
        
        /**
         * Unpacks the data from the buffer between unpacking sessions.
         */
        """
        pass

    def raw_pack_blob(self, const_DCPacker_self, bytes_value): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        raw_pack_blob(const DCPacker self, bytes value)
        
        /**
         * Packs the data into the buffer between packing sessions.
         */
        """
        pass

    def raw_pack_float64(self, const_DCPacker_self, double_value): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        raw_pack_float64(const DCPacker self, double value)
        
        /**
         * Packs the data into the buffer between packing sessions.
         */
        """
        pass

    def raw_pack_int16(self, const_DCPacker_self, int_value): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        raw_pack_int16(const DCPacker self, int value)
        
        /**
         * Packs the data into the buffer between packing sessions.
         */
        """
        pass

    def raw_pack_int32(self, const_DCPacker_self, int_value): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        raw_pack_int32(const DCPacker self, int value)
        
        /**
         * Packs the data into the buffer between packing sessions.
         */
        """
        pass

    def raw_pack_int64(self, const_DCPacker_self, long_value): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        raw_pack_int64(const DCPacker self, long value)
        
        /**
         * Packs the data into the buffer between packing sessions.
         */
        """
        pass

    def raw_pack_int8(self, const_DCPacker_self, int_value): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        raw_pack_int8(const DCPacker self, int value)
        
        /**
         * Packs the data into the buffer between packing sessions.
         */
        """
        pass

    def raw_pack_string(self, const_DCPacker_self, str_value): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        raw_pack_string(const DCPacker self, str value)
        
        /**
         * Packs the data into the buffer between packing sessions.
         */
        """
        pass

    def raw_pack_uint16(self, const_DCPacker_self, int_value): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        raw_pack_uint16(const DCPacker self, int value)
        
        /**
         * Packs the data into the buffer between packing sessions.
         */
        """
        pass

    def raw_pack_uint32(self, const_DCPacker_self, int_value): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        raw_pack_uint32(const DCPacker self, int value)
        
        /**
         * Packs the data into the buffer between packing sessions.
         */
        """
        pass

    def raw_pack_uint64(self, const_DCPacker_self, long_value): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        raw_pack_uint64(const DCPacker self, long value)
        
        /**
         * Packs the data into the buffer between packing sessions.
         */
        """
        pass

    def raw_pack_uint8(self, const_DCPacker_self, int_value): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        raw_pack_uint8(const DCPacker self, int value)
        
        /**
         * Packs the data into the buffer between packing sessions.
         */
        """
        pass

    def raw_unpack_blob(self, const_DCPacker_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        raw_unpack_blob(const DCPacker self)
        
        /**
         * Unpacks the data from the buffer between unpacking sessions.
         */
        
        /**
         * Unpacks the data from the buffer between unpacking sessions.
         */
        """
        pass

    def raw_unpack_float64(self, const_DCPacker_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        raw_unpack_float64(const DCPacker self)
        
        /**
         * Unpacks the data from the buffer between unpacking sessions.
         */
        
        /**
         * Unpacks the data from the buffer between unpacking sessions.
         */
        """
        pass

    def raw_unpack_int16(self, const_DCPacker_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        raw_unpack_int16(const DCPacker self)
        
        /**
         * Unpacks the data from the buffer between unpacking sessions.
         */
        
        /**
         * Unpacks the data from the buffer between unpacking sessions.
         */
        """
        pass

    def raw_unpack_int32(self, const_DCPacker_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        raw_unpack_int32(const DCPacker self)
        
        /**
         * Unpacks the data from the buffer between unpacking sessions.
         */
        
        /**
         * Unpacks the data from the buffer between unpacking sessions.
         */
        """
        pass

    def raw_unpack_int64(self, const_DCPacker_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        raw_unpack_int64(const DCPacker self)
        
        /**
         * Unpacks the data from the buffer between unpacking sessions.
         */
        
        /**
         * Unpacks the data from the buffer between unpacking sessions.
         */
        """
        pass

    def raw_unpack_int8(self, const_DCPacker_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        raw_unpack_int8(const DCPacker self)
        
        /**
         * Unpacks the data from the buffer between unpacking sessions.
         */
        
        /**
         * Unpacks the data from the buffer between unpacking sessions.
         */
        """
        pass

    def raw_unpack_string(self, const_DCPacker_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        raw_unpack_string(const DCPacker self)
        
        /**
         * Unpacks the data from the buffer between unpacking sessions.
         */
        
        /**
         * Unpacks the data from the buffer between unpacking sessions.
         */
        """
        pass

    def raw_unpack_uint16(self, const_DCPacker_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        raw_unpack_uint16(const DCPacker self)
        
        /**
         * Unpacks the data from the buffer between unpacking sessions.
         */
        
        /**
         * Unpacks the data from the buffer between unpacking sessions.
         */
        """
        pass

    def raw_unpack_uint32(self, const_DCPacker_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        raw_unpack_uint32(const DCPacker self)
        
        /**
         * Unpacks the data from the buffer between unpacking sessions.
         */
        
        /**
         * Unpacks the data from the buffer between unpacking sessions.
         */
        """
        pass

    def raw_unpack_uint64(self, const_DCPacker_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        raw_unpack_uint64(const DCPacker self)
        
        /**
         * Unpacks the data from the buffer between unpacking sessions.
         */
        
        /**
         * Unpacks the data from the buffer between unpacking sessions.
         */
        """
        pass

    def raw_unpack_uint8(self, const_DCPacker_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        raw_unpack_uint8(const DCPacker self)
        
        /**
         * Unpacks the data from the buffer between unpacking sessions.
         */
        
        /**
         * Unpacks the data from the buffer between unpacking sessions.
         */
        """
        pass

    def seek(self, const_DCPacker_self, str_field_name): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        seek(const DCPacker self, str field_name)
        seek(const DCPacker self, int seek_index)
        
        /**
         * Sets the current unpack (or repack) position to the named field.  In unpack
         * mode, the next call to unpack_*() or push() will begin to read the named
         * field.  In repack mode, the next call to pack_*() or push() will modify the
         * named field.
         *
         * Returns true if successful, false if the field is not known (or if the
         * packer is in an invalid mode).
         */
        
        /**
         * Seeks to the field indentified by seek_index, which was returned by an
         * earlier call to DCField::find_seek_index() to get the index of some nested
         * field.  Also see the version of seek() that accepts a field name.
         *
         * Returns true if successful, false if the field is not known (or if the
         * packer is in an invalid mode).
         */
        """
        pass

    def setUnpackData(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_unpack_data(const DCPacker self, bytes data)
        
        /**
         * Sets up the unpack_data pointer.  You may call this before calling the
         * version of begin_unpack() that takes only one parameter.
         */
        
        /**
         * Sets up the unpack_data pointer.  You may call this before calling the
         * version of begin_unpack() that takes only one parameter.
         */
        """
        pass

    def set_unpack_data(self, const_DCPacker_self, bytes_data): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_unpack_data(const DCPacker self, bytes data)
        
        /**
         * Sets up the unpack_data pointer.  You may call this before calling the
         * version of begin_unpack() that takes only one parameter.
         */
        
        /**
         * Sets up the unpack_data pointer.  You may call this before calling the
         * version of begin_unpack() that takes only one parameter.
         */
        """
        pass

    def unpackAndFormat(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        unpack_and_format(const DCPacker self)
        unpack_and_format(const DCPacker self, ostream out, bool show_field_names)
        unpack_and_format(const DCPacker self, bool show_field_names)
        
        /**
         * Unpacks an object and formats its value into a syntax suitable for parsing
         * in the dc file (e.g.  as a default value), or as an input to parse_object.
         */
        
        /**
         * Unpacks an object and formats its value into a syntax suitable for parsing
         * in the dc file (e.g.  as a default value), or as an input to parse_object.
         */
        """
        pass

    def unpackBlob(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        unpack_blob(const DCPacker self)
        
        /**
         * Unpacks the current binary data value from the stream.
         */
        
        /**
         * Unpacks the current numeric or string value from the stream.
         */
        """
        pass

    def unpackDouble(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        unpack_double(const DCPacker self)
        
        /**
         * Unpacks the current numeric or string value from the stream.
         */
        
        /**
         * Unpacks the current numeric or string value from the stream.
         */
        """
        pass

    def unpackInt(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        unpack_int(const DCPacker self)
        
        /**
         * Unpacks the current numeric or string value from the stream.
         */
        
        /**
         * Unpacks the current numeric or string value from the stream.
         */
        """
        pass

    def unpackInt64(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        unpack_int64(const DCPacker self)
        
        /**
         * Unpacks the current numeric or string value from the stream.
         */
        
        /**
         * Unpacks the current numeric or string value from the stream.
         */
        """
        pass

    def unpackLiteralValue(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        unpack_literal_value(const DCPacker self)
        
        /**
         * Returns the literal string that represents the packed value of the current
         * field, and advances the field pointer.
         */
        
        /**
         * Returns the literal string that represents the packed value of the current
         * field, and advances the field pointer.
         */
        """
        pass

    def unpackObject(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        unpack_object(const DCPacker self)
        
        /**
         * Unpacks a Python object of the appropriate type from the stream for the
         * current field.  This may be an integer or a string for a simple field
         * object; if the current field represents a list of fields it will be a
         * tuple.
         */
        """
        pass

    def unpackSkip(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        unpack_skip(const DCPacker self)
        
        /**
         * Skips the current field without unpacking it and advances to the next
         * field.  If the current field contains nested fields, skips all of them.
         */
        """
        pass

    def unpackString(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        unpack_string(const DCPacker self)
        
        /**
         * Unpacks the current numeric or string value from the stream.
         */
        
        /**
         * Unpacks the current numeric or string value from the stream.
         */
        """
        pass

    def unpackUint(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        unpack_uint(const DCPacker self)
        
        /**
         * Unpacks the current numeric or string value from the stream.
         */
        
        /**
         * Unpacks the current numeric or string value from the stream.
         */
        """
        pass

    def unpackUint64(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        unpack_uint64(const DCPacker self)
        
        /**
         * Unpacks the current numeric or string value from the stream.
         */
        
        /**
         * Unpacks the current numeric or string value from the stream.
         */
        """
        pass

    def unpackValidate(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        unpack_validate(const DCPacker self)
        
        /**
         * Internally unpacks the current numeric or string value and validates it
         * against the type range limits, but does not return the value.  If the
         * current field contains nested fields, validates all of them.
         */
        """
        pass

    def unpack_and_format(self, const_DCPacker_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        unpack_and_format(const DCPacker self)
        unpack_and_format(const DCPacker self, ostream out, bool show_field_names)
        unpack_and_format(const DCPacker self, bool show_field_names)
        
        /**
         * Unpacks an object and formats its value into a syntax suitable for parsing
         * in the dc file (e.g.  as a default value), or as an input to parse_object.
         */
        
        /**
         * Unpacks an object and formats its value into a syntax suitable for parsing
         * in the dc file (e.g.  as a default value), or as an input to parse_object.
         */
        """
        pass

    def unpack_blob(self, const_DCPacker_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        unpack_blob(const DCPacker self)
        
        /**
         * Unpacks the current binary data value from the stream.
         */
        
        /**
         * Unpacks the current numeric or string value from the stream.
         */
        """
        pass

    def unpack_double(self, const_DCPacker_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        unpack_double(const DCPacker self)
        
        /**
         * Unpacks the current numeric or string value from the stream.
         */
        
        /**
         * Unpacks the current numeric or string value from the stream.
         */
        """
        pass

    def unpack_int(self, const_DCPacker_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        unpack_int(const DCPacker self)
        
        /**
         * Unpacks the current numeric or string value from the stream.
         */
        
        /**
         * Unpacks the current numeric or string value from the stream.
         */
        """
        pass

    def unpack_int64(self, const_DCPacker_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        unpack_int64(const DCPacker self)
        
        /**
         * Unpacks the current numeric or string value from the stream.
         */
        
        /**
         * Unpacks the current numeric or string value from the stream.
         */
        """
        pass

    def unpack_literal_value(self, const_DCPacker_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        unpack_literal_value(const DCPacker self)
        
        /**
         * Returns the literal string that represents the packed value of the current
         * field, and advances the field pointer.
         */
        
        /**
         * Returns the literal string that represents the packed value of the current
         * field, and advances the field pointer.
         */
        """
        pass

    def unpack_object(self, const_DCPacker_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        unpack_object(const DCPacker self)
        
        /**
         * Unpacks a Python object of the appropriate type from the stream for the
         * current field.  This may be an integer or a string for a simple field
         * object; if the current field represents a list of fields it will be a
         * tuple.
         */
        """
        pass

    def unpack_skip(self, const_DCPacker_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        unpack_skip(const DCPacker self)
        
        /**
         * Skips the current field without unpacking it and advances to the next
         * field.  If the current field contains nested fields, skips all of them.
         */
        """
        pass

    def unpack_string(self, const_DCPacker_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        unpack_string(const DCPacker self)
        
        /**
         * Unpacks the current numeric or string value from the stream.
         */
        
        /**
         * Unpacks the current numeric or string value from the stream.
         */
        """
        pass

    def unpack_uint(self, const_DCPacker_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        unpack_uint(const DCPacker self)
        
        /**
         * Unpacks the current numeric or string value from the stream.
         */
        
        /**
         * Unpacks the current numeric or string value from the stream.
         */
        """
        pass

    def unpack_uint64(self, const_DCPacker_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        unpack_uint64(const DCPacker self)
        
        /**
         * Unpacks the current numeric or string value from the stream.
         */
        
        /**
         * Unpacks the current numeric or string value from the stream.
         */
        """
        pass

    def unpack_validate(self, const_DCPacker_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        unpack_validate(const DCPacker self)
        
        /**
         * Internally unpacks the current numeric or string value and validates it
         * against the type range limits, but does not return the value.  If the
         * current field contains nested fields, validates all of them.
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
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.direct.DCPacker' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.direct.DCPacker' objects>"
        '__doc__': '/**\n * This class can be used for packing a series of numeric and string data into\n * a binary stream, according to the DC specification.\n *\n * See also direct/src/doc/dcPacker.txt for a more complete description and\n * examples of using this class.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.direct.DCPacker' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFDC68DDEC0>'
        'beginPack': None, # (!) real value is "<method 'beginPack' of 'panda3d.direct.DCPacker' objects>"
        'beginRepack': None, # (!) real value is "<method 'beginRepack' of 'panda3d.direct.DCPacker' objects>"
        'beginUnpack': None, # (!) real value is "<method 'beginUnpack' of 'panda3d.direct.DCPacker' objects>"
        'begin_pack': None, # (!) real value is "<method 'begin_pack' of 'panda3d.direct.DCPacker' objects>"
        'begin_repack': None, # (!) real value is "<method 'begin_repack' of 'panda3d.direct.DCPacker' objects>"
        'begin_unpack': None, # (!) real value is "<method 'begin_unpack' of 'panda3d.direct.DCPacker' objects>"
        'clearData': None, # (!) real value is "<method 'clearData' of 'panda3d.direct.DCPacker' objects>"
        'clear_data': None, # (!) real value is "<method 'clear_data' of 'panda3d.direct.DCPacker' objects>"
        'endPack': None, # (!) real value is "<method 'endPack' of 'panda3d.direct.DCPacker' objects>"
        'endRepack': None, # (!) real value is "<method 'endRepack' of 'panda3d.direct.DCPacker' objects>"
        'endUnpack': None, # (!) real value is "<method 'endUnpack' of 'panda3d.direct.DCPacker' objects>"
        'end_pack': None, # (!) real value is "<method 'end_pack' of 'panda3d.direct.DCPacker' objects>"
        'end_repack': None, # (!) real value is "<method 'end_repack' of 'panda3d.direct.DCPacker' objects>"
        'end_unpack': None, # (!) real value is "<method 'end_unpack' of 'panda3d.direct.DCPacker' objects>"
        'getBytes': None, # (!) real value is "<method 'getBytes' of 'panda3d.direct.DCPacker' objects>"
        'getCurrentField': None, # (!) real value is "<method 'getCurrentField' of 'panda3d.direct.DCPacker' objects>"
        'getCurrentFieldName': None, # (!) real value is "<method 'getCurrentFieldName' of 'panda3d.direct.DCPacker' objects>"
        'getCurrentParent': None, # (!) real value is "<method 'getCurrentParent' of 'panda3d.direct.DCPacker' objects>"
        'getLastSwitch': None, # (!) real value is "<method 'getLastSwitch' of 'panda3d.direct.DCPacker' objects>"
        'getLength': None, # (!) real value is "<method 'getLength' of 'panda3d.direct.DCPacker' objects>"
        'getNumNestedFields': None, # (!) real value is "<method 'getNumNestedFields' of 'panda3d.direct.DCPacker' objects>"
        'getNumStackElementsEverAllocated': None, # (!) real value is '<staticmethod(<built-in method getNumStackElementsEverAllocated of type object at 0x00007FFDC68DDEC0>)>'
        'getNumUnpackedBytes': None, # (!) real value is "<method 'getNumUnpackedBytes' of 'panda3d.direct.DCPacker' objects>"
        'getPackType': None, # (!) real value is "<method 'getPackType' of 'panda3d.direct.DCPacker' objects>"
        'getString': None, # (!) real value is "<method 'getString' of 'panda3d.direct.DCPacker' objects>"
        'getUnpackLength': None, # (!) real value is "<method 'getUnpackLength' of 'panda3d.direct.DCPacker' objects>"
        'getUnpackString': None, # (!) real value is "<method 'getUnpackString' of 'panda3d.direct.DCPacker' objects>"
        'get_bytes': None, # (!) real value is "<method 'get_bytes' of 'panda3d.direct.DCPacker' objects>"
        'get_current_field': None, # (!) real value is "<method 'get_current_field' of 'panda3d.direct.DCPacker' objects>"
        'get_current_field_name': None, # (!) real value is "<method 'get_current_field_name' of 'panda3d.direct.DCPacker' objects>"
        'get_current_parent': None, # (!) real value is "<method 'get_current_parent' of 'panda3d.direct.DCPacker' objects>"
        'get_last_switch': None, # (!) real value is "<method 'get_last_switch' of 'panda3d.direct.DCPacker' objects>"
        'get_length': None, # (!) real value is "<method 'get_length' of 'panda3d.direct.DCPacker' objects>"
        'get_num_nested_fields': None, # (!) real value is "<method 'get_num_nested_fields' of 'panda3d.direct.DCPacker' objects>"
        'get_num_stack_elements_ever_allocated': None, # (!) real value is '<staticmethod(<built-in method get_num_stack_elements_ever_allocated of type object at 0x00007FFDC68DDEC0>)>'
        'get_num_unpacked_bytes': None, # (!) real value is "<method 'get_num_unpacked_bytes' of 'panda3d.direct.DCPacker' objects>"
        'get_pack_type': None, # (!) real value is "<method 'get_pack_type' of 'panda3d.direct.DCPacker' objects>"
        'get_string': None, # (!) real value is "<method 'get_string' of 'panda3d.direct.DCPacker' objects>"
        'get_unpack_length': None, # (!) real value is "<method 'get_unpack_length' of 'panda3d.direct.DCPacker' objects>"
        'get_unpack_string': None, # (!) real value is "<method 'get_unpack_string' of 'panda3d.direct.DCPacker' objects>"
        'hadError': None, # (!) real value is "<method 'hadError' of 'panda3d.direct.DCPacker' objects>"
        'hadPackError': None, # (!) real value is "<method 'hadPackError' of 'panda3d.direct.DCPacker' objects>"
        'hadParseError': None, # (!) real value is "<method 'hadParseError' of 'panda3d.direct.DCPacker' objects>"
        'hadRangeError': None, # (!) real value is "<method 'hadRangeError' of 'panda3d.direct.DCPacker' objects>"
        'had_error': None, # (!) real value is "<method 'had_error' of 'panda3d.direct.DCPacker' objects>"
        'had_pack_error': None, # (!) real value is "<method 'had_pack_error' of 'panda3d.direct.DCPacker' objects>"
        'had_parse_error': None, # (!) real value is "<method 'had_parse_error' of 'panda3d.direct.DCPacker' objects>"
        'had_range_error': None, # (!) real value is "<method 'had_range_error' of 'panda3d.direct.DCPacker' objects>"
        'hasNestedFields': None, # (!) real value is "<method 'hasNestedFields' of 'panda3d.direct.DCPacker' objects>"
        'has_nested_fields': None, # (!) real value is "<method 'has_nested_fields' of 'panda3d.direct.DCPacker' objects>"
        'moreNestedFields': None, # (!) real value is "<method 'moreNestedFields' of 'panda3d.direct.DCPacker' objects>"
        'more_nested_fields': None, # (!) real value is "<method 'more_nested_fields' of 'panda3d.direct.DCPacker' objects>"
        'packBlob': None, # (!) real value is "<method 'packBlob' of 'panda3d.direct.DCPacker' objects>"
        'packDefaultValue': None, # (!) real value is "<method 'packDefaultValue' of 'panda3d.direct.DCPacker' objects>"
        'packDouble': None, # (!) real value is "<method 'packDouble' of 'panda3d.direct.DCPacker' objects>"
        'packInt': None, # (!) real value is "<method 'packInt' of 'panda3d.direct.DCPacker' objects>"
        'packInt64': None, # (!) real value is "<method 'packInt64' of 'panda3d.direct.DCPacker' objects>"
        'packLiteralValue': None, # (!) real value is "<method 'packLiteralValue' of 'panda3d.direct.DCPacker' objects>"
        'packObject': None, # (!) real value is "<method 'packObject' of 'panda3d.direct.DCPacker' objects>"
        'packString': None, # (!) real value is "<method 'packString' of 'panda3d.direct.DCPacker' objects>"
        'packUint': None, # (!) real value is "<method 'packUint' of 'panda3d.direct.DCPacker' objects>"
        'packUint64': None, # (!) real value is "<method 'packUint64' of 'panda3d.direct.DCPacker' objects>"
        'pack_blob': None, # (!) real value is "<method 'pack_blob' of 'panda3d.direct.DCPacker' objects>"
        'pack_default_value': None, # (!) real value is "<method 'pack_default_value' of 'panda3d.direct.DCPacker' objects>"
        'pack_double': None, # (!) real value is "<method 'pack_double' of 'panda3d.direct.DCPacker' objects>"
        'pack_int': None, # (!) real value is "<method 'pack_int' of 'panda3d.direct.DCPacker' objects>"
        'pack_int64': None, # (!) real value is "<method 'pack_int64' of 'panda3d.direct.DCPacker' objects>"
        'pack_literal_value': None, # (!) real value is "<method 'pack_literal_value' of 'panda3d.direct.DCPacker' objects>"
        'pack_object': None, # (!) real value is "<method 'pack_object' of 'panda3d.direct.DCPacker' objects>"
        'pack_string': None, # (!) real value is "<method 'pack_string' of 'panda3d.direct.DCPacker' objects>"
        'pack_uint': None, # (!) real value is "<method 'pack_uint' of 'panda3d.direct.DCPacker' objects>"
        'pack_uint64': None, # (!) real value is "<method 'pack_uint64' of 'panda3d.direct.DCPacker' objects>"
        'parseAndPack': None, # (!) real value is "<method 'parseAndPack' of 'panda3d.direct.DCPacker' objects>"
        'parse_and_pack': None, # (!) real value is "<method 'parse_and_pack' of 'panda3d.direct.DCPacker' objects>"
        'pop': None, # (!) real value is "<method 'pop' of 'panda3d.direct.DCPacker' objects>"
        'push': None, # (!) real value is "<method 'push' of 'panda3d.direct.DCPacker' objects>"
        'rawPackBlob': None, # (!) real value is "<method 'rawPackBlob' of 'panda3d.direct.DCPacker' objects>"
        'rawPackFloat64': None, # (!) real value is "<method 'rawPackFloat64' of 'panda3d.direct.DCPacker' objects>"
        'rawPackInt16': None, # (!) real value is "<method 'rawPackInt16' of 'panda3d.direct.DCPacker' objects>"
        'rawPackInt32': None, # (!) real value is "<method 'rawPackInt32' of 'panda3d.direct.DCPacker' objects>"
        'rawPackInt64': None, # (!) real value is "<method 'rawPackInt64' of 'panda3d.direct.DCPacker' objects>"
        'rawPackInt8': None, # (!) real value is "<method 'rawPackInt8' of 'panda3d.direct.DCPacker' objects>"
        'rawPackString': None, # (!) real value is "<method 'rawPackString' of 'panda3d.direct.DCPacker' objects>"
        'rawPackUint16': None, # (!) real value is "<method 'rawPackUint16' of 'panda3d.direct.DCPacker' objects>"
        'rawPackUint32': None, # (!) real value is "<method 'rawPackUint32' of 'panda3d.direct.DCPacker' objects>"
        'rawPackUint64': None, # (!) real value is "<method 'rawPackUint64' of 'panda3d.direct.DCPacker' objects>"
        'rawPackUint8': None, # (!) real value is "<method 'rawPackUint8' of 'panda3d.direct.DCPacker' objects>"
        'rawUnpackBlob': None, # (!) real value is "<method 'rawUnpackBlob' of 'panda3d.direct.DCPacker' objects>"
        'rawUnpackFloat64': None, # (!) real value is "<method 'rawUnpackFloat64' of 'panda3d.direct.DCPacker' objects>"
        'rawUnpackInt16': None, # (!) real value is "<method 'rawUnpackInt16' of 'panda3d.direct.DCPacker' objects>"
        'rawUnpackInt32': None, # (!) real value is "<method 'rawUnpackInt32' of 'panda3d.direct.DCPacker' objects>"
        'rawUnpackInt64': None, # (!) real value is "<method 'rawUnpackInt64' of 'panda3d.direct.DCPacker' objects>"
        'rawUnpackInt8': None, # (!) real value is "<method 'rawUnpackInt8' of 'panda3d.direct.DCPacker' objects>"
        'rawUnpackString': None, # (!) real value is "<method 'rawUnpackString' of 'panda3d.direct.DCPacker' objects>"
        'rawUnpackUint16': None, # (!) real value is "<method 'rawUnpackUint16' of 'panda3d.direct.DCPacker' objects>"
        'rawUnpackUint32': None, # (!) real value is "<method 'rawUnpackUint32' of 'panda3d.direct.DCPacker' objects>"
        'rawUnpackUint64': None, # (!) real value is "<method 'rawUnpackUint64' of 'panda3d.direct.DCPacker' objects>"
        'rawUnpackUint8': None, # (!) real value is "<method 'rawUnpackUint8' of 'panda3d.direct.DCPacker' objects>"
        'raw_pack_blob': None, # (!) real value is "<method 'raw_pack_blob' of 'panda3d.direct.DCPacker' objects>"
        'raw_pack_float64': None, # (!) real value is "<method 'raw_pack_float64' of 'panda3d.direct.DCPacker' objects>"
        'raw_pack_int16': None, # (!) real value is "<method 'raw_pack_int16' of 'panda3d.direct.DCPacker' objects>"
        'raw_pack_int32': None, # (!) real value is "<method 'raw_pack_int32' of 'panda3d.direct.DCPacker' objects>"
        'raw_pack_int64': None, # (!) real value is "<method 'raw_pack_int64' of 'panda3d.direct.DCPacker' objects>"
        'raw_pack_int8': None, # (!) real value is "<method 'raw_pack_int8' of 'panda3d.direct.DCPacker' objects>"
        'raw_pack_string': None, # (!) real value is "<method 'raw_pack_string' of 'panda3d.direct.DCPacker' objects>"
        'raw_pack_uint16': None, # (!) real value is "<method 'raw_pack_uint16' of 'panda3d.direct.DCPacker' objects>"
        'raw_pack_uint32': None, # (!) real value is "<method 'raw_pack_uint32' of 'panda3d.direct.DCPacker' objects>"
        'raw_pack_uint64': None, # (!) real value is "<method 'raw_pack_uint64' of 'panda3d.direct.DCPacker' objects>"
        'raw_pack_uint8': None, # (!) real value is "<method 'raw_pack_uint8' of 'panda3d.direct.DCPacker' objects>"
        'raw_unpack_blob': None, # (!) real value is "<method 'raw_unpack_blob' of 'panda3d.direct.DCPacker' objects>"
        'raw_unpack_float64': None, # (!) real value is "<method 'raw_unpack_float64' of 'panda3d.direct.DCPacker' objects>"
        'raw_unpack_int16': None, # (!) real value is "<method 'raw_unpack_int16' of 'panda3d.direct.DCPacker' objects>"
        'raw_unpack_int32': None, # (!) real value is "<method 'raw_unpack_int32' of 'panda3d.direct.DCPacker' objects>"
        'raw_unpack_int64': None, # (!) real value is "<method 'raw_unpack_int64' of 'panda3d.direct.DCPacker' objects>"
        'raw_unpack_int8': None, # (!) real value is "<method 'raw_unpack_int8' of 'panda3d.direct.DCPacker' objects>"
        'raw_unpack_string': None, # (!) real value is "<method 'raw_unpack_string' of 'panda3d.direct.DCPacker' objects>"
        'raw_unpack_uint16': None, # (!) real value is "<method 'raw_unpack_uint16' of 'panda3d.direct.DCPacker' objects>"
        'raw_unpack_uint32': None, # (!) real value is "<method 'raw_unpack_uint32' of 'panda3d.direct.DCPacker' objects>"
        'raw_unpack_uint64': None, # (!) real value is "<method 'raw_unpack_uint64' of 'panda3d.direct.DCPacker' objects>"
        'raw_unpack_uint8': None, # (!) real value is "<method 'raw_unpack_uint8' of 'panda3d.direct.DCPacker' objects>"
        'seek': None, # (!) real value is "<method 'seek' of 'panda3d.direct.DCPacker' objects>"
        'setUnpackData': None, # (!) real value is "<method 'setUnpackData' of 'panda3d.direct.DCPacker' objects>"
        'set_unpack_data': None, # (!) real value is "<method 'set_unpack_data' of 'panda3d.direct.DCPacker' objects>"
        'unpackAndFormat': None, # (!) real value is "<method 'unpackAndFormat' of 'panda3d.direct.DCPacker' objects>"
        'unpackBlob': None, # (!) real value is "<method 'unpackBlob' of 'panda3d.direct.DCPacker' objects>"
        'unpackDouble': None, # (!) real value is "<method 'unpackDouble' of 'panda3d.direct.DCPacker' objects>"
        'unpackInt': None, # (!) real value is "<method 'unpackInt' of 'panda3d.direct.DCPacker' objects>"
        'unpackInt64': None, # (!) real value is "<method 'unpackInt64' of 'panda3d.direct.DCPacker' objects>"
        'unpackLiteralValue': None, # (!) real value is "<method 'unpackLiteralValue' of 'panda3d.direct.DCPacker' objects>"
        'unpackObject': None, # (!) real value is "<method 'unpackObject' of 'panda3d.direct.DCPacker' objects>"
        'unpackSkip': None, # (!) real value is "<method 'unpackSkip' of 'panda3d.direct.DCPacker' objects>"
        'unpackString': None, # (!) real value is "<method 'unpackString' of 'panda3d.direct.DCPacker' objects>"
        'unpackUint': None, # (!) real value is "<method 'unpackUint' of 'panda3d.direct.DCPacker' objects>"
        'unpackUint64': None, # (!) real value is "<method 'unpackUint64' of 'panda3d.direct.DCPacker' objects>"
        'unpackValidate': None, # (!) real value is "<method 'unpackValidate' of 'panda3d.direct.DCPacker' objects>"
        'unpack_and_format': None, # (!) real value is "<method 'unpack_and_format' of 'panda3d.direct.DCPacker' objects>"
        'unpack_blob': None, # (!) real value is "<method 'unpack_blob' of 'panda3d.direct.DCPacker' objects>"
        'unpack_double': None, # (!) real value is "<method 'unpack_double' of 'panda3d.direct.DCPacker' objects>"
        'unpack_int': None, # (!) real value is "<method 'unpack_int' of 'panda3d.direct.DCPacker' objects>"
        'unpack_int64': None, # (!) real value is "<method 'unpack_int64' of 'panda3d.direct.DCPacker' objects>"
        'unpack_literal_value': None, # (!) real value is "<method 'unpack_literal_value' of 'panda3d.direct.DCPacker' objects>"
        'unpack_object': None, # (!) real value is "<method 'unpack_object' of 'panda3d.direct.DCPacker' objects>"
        'unpack_skip': None, # (!) real value is "<method 'unpack_skip' of 'panda3d.direct.DCPacker' objects>"
        'unpack_string': None, # (!) real value is "<method 'unpack_string' of 'panda3d.direct.DCPacker' objects>"
        'unpack_uint': None, # (!) real value is "<method 'unpack_uint' of 'panda3d.direct.DCPacker' objects>"
        'unpack_uint64': None, # (!) real value is "<method 'unpack_uint64' of 'panda3d.direct.DCPacker' objects>"
        'unpack_validate': None, # (!) real value is "<method 'unpack_validate' of 'panda3d.direct.DCPacker' objects>"
    }


