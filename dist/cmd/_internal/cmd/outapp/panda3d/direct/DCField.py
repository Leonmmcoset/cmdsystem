# encoding: utf-8
# module panda3d.direct
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\direct.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import panda3d.core as __panda3d_core


from .DCPackerInterface import DCPackerInterface

from .DCKeywordList import DCKeywordList

class DCField(DCPackerInterface, DCKeywordList):
    """
    /**
     * A single field of a Distributed Class, either atomic or molecular.
     */
    """
    def aiFormatUpdate(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        ai_format_update(DCField self, int do_id, long to_id, long from_id, object args)
        
        /**
         * Generates a datagram containing the message necessary to send an update for
         * the indicated distributed object from the AI.
         */
        """
        pass

    def aiFormatUpdateMsgType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        ai_format_update_msg_type(DCField self, int do_id, long to_id, long from_id, int msg_type, object args)
        
        /**
         * Generates a datagram containing the message necessary to send an update,
         * with the msg type, for the indicated distributed object from the AI.
         */
        """
        pass

    def ai_format_update(self, DCField_self, int_do_id, long_to_id, long_from_id, object_args): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        ai_format_update(DCField self, int do_id, long to_id, long from_id, object args)
        
        /**
         * Generates a datagram containing the message necessary to send an update for
         * the indicated distributed object from the AI.
         */
        """
        pass

    def ai_format_update_msg_type(self, DCField_self, int_do_id, long_to_id, long_from_id, int_msg_type, object_args): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        ai_format_update_msg_type(DCField self, int do_id, long to_id, long from_id, int msg_type, object args)
        
        /**
         * Generates a datagram containing the message necessary to send an update,
         * with the msg type, for the indicated distributed object from the AI.
         */
        """
        pass

    def asAtomicField(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        as_atomic_field(const DCField self)
        as_atomic_field(DCField self)
        
        /**
         * Returns the same field pointer converted to an atomic field pointer, if
         * this is in fact an atomic field; otherwise, returns NULL.
         */
        
        /**
         * Returns the same field pointer converted to an atomic field pointer, if
         * this is in fact an atomic field; otherwise, returns NULL.
         */
        """
        pass

    def asField(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        as_field(const DCField self)
        as_field(DCField self)
        
        /**
         *
         */
        
        /**
         *
         */
        """
        pass

    def asMolecularField(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        as_molecular_field(const DCField self)
        as_molecular_field(DCField self)
        
        /**
         * Returns the same field pointer converted to a molecular field pointer, if
         * this is in fact a molecular field; otherwise, returns NULL.
         */
        
        /**
         * Returns the same field pointer converted to a molecular field pointer, if
         * this is in fact a molecular field; otherwise, returns NULL.
         */
        """
        pass

    def asParameter(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        as_parameter(const DCField self)
        as_parameter(DCField self)
        
        /**
         *
         */
        
        /**
         *
         */
        """
        pass

    def as_atomic_field(self, const_DCField_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        as_atomic_field(const DCField self)
        as_atomic_field(DCField self)
        
        /**
         * Returns the same field pointer converted to an atomic field pointer, if
         * this is in fact an atomic field; otherwise, returns NULL.
         */
        
        /**
         * Returns the same field pointer converted to an atomic field pointer, if
         * this is in fact an atomic field; otherwise, returns NULL.
         */
        """
        pass

    def as_field(self, const_DCField_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        as_field(const DCField self)
        as_field(DCField self)
        
        /**
         *
         */
        
        /**
         *
         */
        """
        pass

    def as_molecular_field(self, const_DCField_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        as_molecular_field(const DCField self)
        as_molecular_field(DCField self)
        
        /**
         * Returns the same field pointer converted to a molecular field pointer, if
         * this is in fact a molecular field; otherwise, returns NULL.
         */
        
        /**
         * Returns the same field pointer converted to a molecular field pointer, if
         * this is in fact a molecular field; otherwise, returns NULL.
         */
        """
        pass

    def as_parameter(self, const_DCField_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        as_parameter(const DCField self)
        as_parameter(DCField self)
        
        /**
         *
         */
        
        /**
         *
         */
        """
        pass

    def clientFormatUpdate(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        client_format_update(DCField self, int do_id, object args)
        
        /**
         * Generates a datagram containing the message necessary to send an update for
         * the indicated distributed object from the client.
         */
        """
        pass

    def client_format_update(self, DCField_self, int_do_id, object_args): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        client_format_update(DCField self, int do_id, object args)
        
        /**
         * Generates a datagram containing the message necessary to send an update for
         * the indicated distributed object from the client.
         */
        """
        pass

    def formatData(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        format_data(const DCField self, bytes packed_data, bool show_field_names)
        
        /**
         * Given a blob that represents the packed data for this field, returns a
         * string formatting it for human consumption.  Returns empty string if there
         * is an error.
         */
        """
        pass

    def format_data(self, const_DCField_self, bytes_packed_data, bool_show_field_names): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        format_data(const DCField self, bytes packed_data, bool show_field_names)
        
        /**
         * Given a blob that represents the packed data for this field, returns a
         * string formatting it for human consumption.  Returns empty string if there
         * is an error.
         */
        """
        pass

    def getClass(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class(DCField self)
        
        /**
         * Returns the DCClass pointer for the class that contains this field.
         */
        """
        pass

    def getDefaultValue(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_default_value(DCField self)
        
        /**
         * Returns the default value for this field.  If a default value has been
         * explicitly set (e.g.  has_default_value() returns true), returns that
         * value; otherwise, returns an implicit default for the field.
         */
        """
        pass

    def getNumber(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_number(DCField self)
        
        /**
         * Returns a unique index number associated with this field.  This is defined
         * implicitly when the .dc file(s) are read.
         */
        """
        pass

    def get_class(self, DCField_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class(DCField self)
        
        /**
         * Returns the DCClass pointer for the class that contains this field.
         */
        """
        pass

    def get_default_value(self, DCField_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_default_value(DCField self)
        
        /**
         * Returns the default value for this field.  If a default value has been
         * explicitly set (e.g.  has_default_value() returns true), returns that
         * value; otherwise, returns an implicit default for the field.
         */
        """
        pass

    def get_number(self, DCField_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_number(DCField self)
        
        /**
         * Returns a unique index number associated with this field.  This is defined
         * implicitly when the .dc file(s) are read.
         */
        """
        pass

    def hasDefaultValue(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_default_value(DCField self)
        
        /**
         * Returns true if a default value has been explicitly established for this
         * field, false otherwise.
         */
        """
        pass

    def has_default_value(self, DCField_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_default_value(DCField self)
        
        /**
         * Returns true if a default value has been explicitly established for this
         * field, false otherwise.
         */
        """
        pass

    def isAirecv(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_airecv(DCField self)
        
        /**
         * Returns true if the "airecv" flag is set for this field, false otherwise.
         */
        """
        pass

    def isBogusField(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_bogus_field(DCField self)
        
        /**
         * Returns true if the field has been flagged as a bogus field.  This is set
         * for fields that are generated by the parser as placeholder for missing
         * fields, as when reading a partial file; it should not occur in a normal
         * valid dc file.
         */
        """
        pass

    def isBroadcast(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_broadcast(DCField self)
        
        /**
         * Returns true if the "broadcast" flag is set for this field, false
         * otherwise.
         */
        """
        pass

    def isClrecv(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_clrecv(DCField self)
        
        /**
         * Returns true if the "clrecv" flag is set for this field, false otherwise.
         */
        """
        pass

    def isClsend(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_clsend(DCField self)
        
        /**
         * Returns true if the "clsend" flag is set for this field, false otherwise.
         */
        """
        pass

    def isDb(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_db(DCField self)
        
        /**
         * Returns true if the "db" flag is set for this field, false otherwise.
         */
        """
        pass

    def isOwnrecv(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_ownrecv(DCField self)
        
        /**
         * Returns true if the "ownrecv" flag is set for this field, false otherwise.
         */
        """
        pass

    def isOwnsend(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_ownsend(DCField self)
        
        /**
         * Returns true if the "ownsend" flag is set for this field, false otherwise.
         */
        """
        pass

    def isRam(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_ram(DCField self)
        
        /**
         * Returns true if the "ram" flag is set for this field, false otherwise.
         */
        """
        pass

    def isRequired(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_required(DCField self)
        
        /**
         * Returns true if the "required" flag is set for this field, false otherwise.
         */
        """
        pass

    def is_airecv(self, DCField_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_airecv(DCField self)
        
        /**
         * Returns true if the "airecv" flag is set for this field, false otherwise.
         */
        """
        pass

    def is_bogus_field(self, DCField_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_bogus_field(DCField self)
        
        /**
         * Returns true if the field has been flagged as a bogus field.  This is set
         * for fields that are generated by the parser as placeholder for missing
         * fields, as when reading a partial file; it should not occur in a normal
         * valid dc file.
         */
        """
        pass

    def is_broadcast(self, DCField_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_broadcast(DCField self)
        
        /**
         * Returns true if the "broadcast" flag is set for this field, false
         * otherwise.
         */
        """
        pass

    def is_clrecv(self, DCField_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_clrecv(DCField self)
        
        /**
         * Returns true if the "clrecv" flag is set for this field, false otherwise.
         */
        """
        pass

    def is_clsend(self, DCField_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_clsend(DCField self)
        
        /**
         * Returns true if the "clsend" flag is set for this field, false otherwise.
         */
        """
        pass

    def is_db(self, DCField_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_db(DCField self)
        
        /**
         * Returns true if the "db" flag is set for this field, false otherwise.
         */
        """
        pass

    def is_ownrecv(self, DCField_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_ownrecv(DCField self)
        
        /**
         * Returns true if the "ownrecv" flag is set for this field, false otherwise.
         */
        """
        pass

    def is_ownsend(self, DCField_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_ownsend(DCField self)
        
        /**
         * Returns true if the "ownsend" flag is set for this field, false otherwise.
         */
        """
        pass

    def is_ram(self, DCField_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_ram(DCField self)
        
        /**
         * Returns true if the "ram" flag is set for this field, false otherwise.
         */
        """
        pass

    def is_required(self, DCField_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_required(DCField self)
        
        /**
         * Returns true if the "required" flag is set for this field, false otherwise.
         */
        """
        pass

    def output(self, DCField_self, ostream_out): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        output(DCField self, ostream out)
        
        /**
         * Write a string representation of this instance to <out>.
         */
        """
        pass

    def packArgs(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        pack_args(DCField self, DCPacker packer, object sequence)
        
        /**
         * Packs the Python arguments from the indicated tuple into the packer.
         * Returns true on success, false on failure.
         *
         * It is assumed that the packer is currently positioned on this field.
         */
        """
        pass

    def pack_args(self, DCField_self, DCPacker_packer, object_sequence): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        pack_args(DCField self, DCPacker packer, object sequence)
        
        /**
         * Packs the Python arguments from the indicated tuple into the packer.
         * Returns true on success, false on failure.
         *
         * It is assumed that the packer is currently positioned on this field.
         */
        """
        pass

    def parseString(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        parse_string(const DCField self, str formatted_string)
        
        /**
         * Given a human-formatted string (for instance, as returned by format_data(),
         * above) that represents the value of this field, parse the string and return
         * the corresponding packed data.  Returns empty string if there is an error.
         */
        """
        pass

    def parse_string(self, const_DCField_self, str_formatted_string): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        parse_string(const DCField self, str formatted_string)
        
        /**
         * Given a human-formatted string (for instance, as returned by format_data(),
         * above) that represents the value of this field, parse the string and return
         * the corresponding packed data.  Returns empty string if there is an error.
         */
        """
        pass

    def receiveUpdate(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        receive_update(DCField self, DCPacker packer, object distobj)
        
        /**
         * Extracts the update message out of the datagram and applies it to the
         * indicated object by calling the appropriate method.
         */
        """
        pass

    def receive_update(self, DCField_self, DCPacker_packer, object_distobj): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        receive_update(DCField self, DCPacker packer, object distobj)
        
        /**
         * Extracts the update message out of the datagram and applies it to the
         * indicated object by calling the appropriate method.
         */
        """
        pass

    def unpackArgs(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        unpack_args(DCField self, DCPacker packer)
        
        /**
         * Unpacks the values from the packer, beginning at the current point in the
         * unpack_buffer, into a Python tuple and returns the tuple.
         *
         * It is assumed that the packer is currently positioned on this field.
         */
        """
        pass

    def unpack_args(self, DCField_self, DCPacker_packer): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        unpack_args(DCField self, DCPacker packer)
        
        /**
         * Unpacks the values from the packer, beginning at the current point in the
         * unpack_buffer, into a Python tuple and returns the tuple.
         *
         * It is assumed that the packer is currently positioned on this field.
         */
        """
        pass

    def upcastToDCKeywordList(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        upcast_to_DCKeywordList(const DCField self)
        
        upcast from DCField to DCKeywordList
        """
        pass

    def upcastToDCPackerInterface(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        upcast_to_DCPackerInterface(const DCField self)
        
        upcast from DCField to DCPackerInterface
        """
        pass

    def upcast_to_DCKeywordList(self, const_DCField_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        upcast_to_DCKeywordList(const DCField self)
        
        upcast from DCField to DCKeywordList
        """
        pass

    def upcast_to_DCPackerInterface(self, const_DCField_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        upcast_to_DCPackerInterface(const DCField self)
        
        upcast from DCField to DCPackerInterface
        """
        pass

    def validateRanges(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        validate_ranges(DCField self, bytes packed_data)
        
        /**
         * Verifies that all of the packed values in the field data are within the
         * specified ranges and that there are no extra bytes on the end of the
         * record.  Returns true if all fields are valid, false otherwise.
         */
        """
        pass

    def validate_ranges(self, DCField_self, bytes_packed_data): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        validate_ranges(DCField self, bytes packed_data)
        
        /**
         * Verifies that all of the packed values in the field data are within the
         * specified ranges and that there are no extra bytes on the end of the
         * record.  Returns true if all fields are valid, false otherwise.
         */
        """
        pass

    def write(self, DCField_self, ostream_out, int_indent_level): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        write(DCField self, ostream out, int indent_level)
        
        /**
         * Write a string representation of this instance to <out>.
         */
        """
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
        '__doc__': '/**\n * A single field of a Distributed Class, either atomic or molecular.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.direct.DCField' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFDC68DDB20>'
        '__repr__': None, # (!) real value is "<slot wrapper '__repr__' of 'panda3d.direct.DCField' objects>"
        '__str__': None, # (!) real value is "<slot wrapper '__str__' of 'panda3d.direct.DCField' objects>"
        'aiFormatUpdate': None, # (!) real value is "<method 'aiFormatUpdate' of 'panda3d.direct.DCField' objects>"
        'aiFormatUpdateMsgType': None, # (!) real value is "<method 'aiFormatUpdateMsgType' of 'panda3d.direct.DCField' objects>"
        'ai_format_update': None, # (!) real value is "<method 'ai_format_update' of 'panda3d.direct.DCField' objects>"
        'ai_format_update_msg_type': None, # (!) real value is "<method 'ai_format_update_msg_type' of 'panda3d.direct.DCField' objects>"
        'asAtomicField': None, # (!) real value is "<method 'asAtomicField' of 'panda3d.direct.DCField' objects>"
        'asField': None, # (!) real value is "<method 'asField' of 'panda3d.direct.DCField' objects>"
        'asMolecularField': None, # (!) real value is "<method 'asMolecularField' of 'panda3d.direct.DCField' objects>"
        'asParameter': None, # (!) real value is "<method 'asParameter' of 'panda3d.direct.DCField' objects>"
        'as_atomic_field': None, # (!) real value is "<method 'as_atomic_field' of 'panda3d.direct.DCField' objects>"
        'as_field': None, # (!) real value is "<method 'as_field' of 'panda3d.direct.DCField' objects>"
        'as_molecular_field': None, # (!) real value is "<method 'as_molecular_field' of 'panda3d.direct.DCField' objects>"
        'as_parameter': None, # (!) real value is "<method 'as_parameter' of 'panda3d.direct.DCField' objects>"
        'clientFormatUpdate': None, # (!) real value is "<method 'clientFormatUpdate' of 'panda3d.direct.DCField' objects>"
        'client_format_update': None, # (!) real value is "<method 'client_format_update' of 'panda3d.direct.DCField' objects>"
        'formatData': None, # (!) real value is "<method 'formatData' of 'panda3d.direct.DCField' objects>"
        'format_data': None, # (!) real value is "<method 'format_data' of 'panda3d.direct.DCField' objects>"
        'getClass': None, # (!) real value is "<method 'getClass' of 'panda3d.direct.DCField' objects>"
        'getDefaultValue': None, # (!) real value is "<method 'getDefaultValue' of 'panda3d.direct.DCField' objects>"
        'getNumber': None, # (!) real value is "<method 'getNumber' of 'panda3d.direct.DCField' objects>"
        'get_class': None, # (!) real value is "<method 'get_class' of 'panda3d.direct.DCField' objects>"
        'get_default_value': None, # (!) real value is "<method 'get_default_value' of 'panda3d.direct.DCField' objects>"
        'get_number': None, # (!) real value is "<method 'get_number' of 'panda3d.direct.DCField' objects>"
        'hasDefaultValue': None, # (!) real value is "<method 'hasDefaultValue' of 'panda3d.direct.DCField' objects>"
        'has_default_value': None, # (!) real value is "<method 'has_default_value' of 'panda3d.direct.DCField' objects>"
        'isAirecv': None, # (!) real value is "<method 'isAirecv' of 'panda3d.direct.DCField' objects>"
        'isBogusField': None, # (!) real value is "<method 'isBogusField' of 'panda3d.direct.DCField' objects>"
        'isBroadcast': None, # (!) real value is "<method 'isBroadcast' of 'panda3d.direct.DCField' objects>"
        'isClrecv': None, # (!) real value is "<method 'isClrecv' of 'panda3d.direct.DCField' objects>"
        'isClsend': None, # (!) real value is "<method 'isClsend' of 'panda3d.direct.DCField' objects>"
        'isDb': None, # (!) real value is "<method 'isDb' of 'panda3d.direct.DCField' objects>"
        'isOwnrecv': None, # (!) real value is "<method 'isOwnrecv' of 'panda3d.direct.DCField' objects>"
        'isOwnsend': None, # (!) real value is "<method 'isOwnsend' of 'panda3d.direct.DCField' objects>"
        'isRam': None, # (!) real value is "<method 'isRam' of 'panda3d.direct.DCField' objects>"
        'isRequired': None, # (!) real value is "<method 'isRequired' of 'panda3d.direct.DCField' objects>"
        'is_airecv': None, # (!) real value is "<method 'is_airecv' of 'panda3d.direct.DCField' objects>"
        'is_bogus_field': None, # (!) real value is "<method 'is_bogus_field' of 'panda3d.direct.DCField' objects>"
        'is_broadcast': None, # (!) real value is "<method 'is_broadcast' of 'panda3d.direct.DCField' objects>"
        'is_clrecv': None, # (!) real value is "<method 'is_clrecv' of 'panda3d.direct.DCField' objects>"
        'is_clsend': None, # (!) real value is "<method 'is_clsend' of 'panda3d.direct.DCField' objects>"
        'is_db': None, # (!) real value is "<method 'is_db' of 'panda3d.direct.DCField' objects>"
        'is_ownrecv': None, # (!) real value is "<method 'is_ownrecv' of 'panda3d.direct.DCField' objects>"
        'is_ownsend': None, # (!) real value is "<method 'is_ownsend' of 'panda3d.direct.DCField' objects>"
        'is_ram': None, # (!) real value is "<method 'is_ram' of 'panda3d.direct.DCField' objects>"
        'is_required': None, # (!) real value is "<method 'is_required' of 'panda3d.direct.DCField' objects>"
        'output': None, # (!) real value is "<method 'output' of 'panda3d.direct.DCField' objects>"
        'packArgs': None, # (!) real value is "<method 'packArgs' of 'panda3d.direct.DCField' objects>"
        'pack_args': None, # (!) real value is "<method 'pack_args' of 'panda3d.direct.DCField' objects>"
        'parseString': None, # (!) real value is "<method 'parseString' of 'panda3d.direct.DCField' objects>"
        'parse_string': None, # (!) real value is "<method 'parse_string' of 'panda3d.direct.DCField' objects>"
        'receiveUpdate': None, # (!) real value is "<method 'receiveUpdate' of 'panda3d.direct.DCField' objects>"
        'receive_update': None, # (!) real value is "<method 'receive_update' of 'panda3d.direct.DCField' objects>"
        'unpackArgs': None, # (!) real value is "<method 'unpackArgs' of 'panda3d.direct.DCField' objects>"
        'unpack_args': None, # (!) real value is "<method 'unpack_args' of 'panda3d.direct.DCField' objects>"
        'upcastToDCKeywordList': None, # (!) real value is "<method 'upcastToDCKeywordList' of 'panda3d.direct.DCField' objects>"
        'upcastToDCPackerInterface': None, # (!) real value is "<method 'upcastToDCPackerInterface' of 'panda3d.direct.DCField' objects>"
        'upcast_to_DCKeywordList': None, # (!) real value is "<method 'upcast_to_DCKeywordList' of 'panda3d.direct.DCField' objects>"
        'upcast_to_DCPackerInterface': None, # (!) real value is "<method 'upcast_to_DCPackerInterface' of 'panda3d.direct.DCField' objects>"
        'validateRanges': None, # (!) real value is "<method 'validateRanges' of 'panda3d.direct.DCField' objects>"
        'validate_ranges': None, # (!) real value is "<method 'validate_ranges' of 'panda3d.direct.DCField' objects>"
        'write': None, # (!) real value is "<method 'write' of 'panda3d.direct.DCField' objects>"
    }


