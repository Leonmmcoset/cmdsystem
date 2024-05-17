# encoding: utf-8
# module panda3d.direct
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\direct.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import panda3d.core as __panda3d_core


from .DCDeclaration import DCDeclaration

class DCClass(DCDeclaration):
    """
    /**
     * Defines a particular DistributedClass as read from an input .dc file.
     */
    """
    def aiFormatGenerate(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        ai_format_generate(DCClass self, object distobj, int do_id, int parent_id, int zone_id, long district_channel_id, long from_channel_id, object optional_fields)
        
        /**
         * Generates a datagram containing the message necessary to generate a new
         * distributed object from the AI. This requires querying the object for the
         * initial value of its required fields.
         *
         * optional_fields is a list of fieldNames to generate in addition to the
         * normal required fields.
         */
        """
        pass

    def aiFormatUpdate(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        ai_format_update(DCClass self, str field_name, int do_id, long to_id, long from_id, object args)
        
        /**
         * Generates a datagram containing the message necessary to send an update for
         * the indicated distributed object from the AI.
         */
        """
        pass

    def aiFormatUpdateMsgType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        ai_format_update_msg_type(DCClass self, str field_name, int do_id, long to_id, long from_id, int msg_type, object args)
        
        /**
         * Generates a datagram containing the message necessary to send an update,
         * using the indicated msg type for the indicated distributed object from the
         * AI.
         */
        """
        pass

    def ai_format_generate(self, DCClass_self, object_distobj, int_do_id, int_parent_id, int_zone_id, long_district_channel_id, long_from_channel_id, object_optional_fields): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        ai_format_generate(DCClass self, object distobj, int do_id, int parent_id, int zone_id, long district_channel_id, long from_channel_id, object optional_fields)
        
        /**
         * Generates a datagram containing the message necessary to generate a new
         * distributed object from the AI. This requires querying the object for the
         * initial value of its required fields.
         *
         * optional_fields is a list of fieldNames to generate in addition to the
         * normal required fields.
         */
        """
        pass

    def ai_format_update(self, DCClass_self, str_field_name, int_do_id, long_to_id, long_from_id, object_args): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        ai_format_update(DCClass self, str field_name, int do_id, long to_id, long from_id, object args)
        
        /**
         * Generates a datagram containing the message necessary to send an update for
         * the indicated distributed object from the AI.
         */
        """
        pass

    def ai_format_update_msg_type(self, DCClass_self, str_field_name, int_do_id, long_to_id, long_from_id, int_msg_type, object_args): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        ai_format_update_msg_type(DCClass self, str field_name, int do_id, long to_id, long from_id, int msg_type, object args)
        
        /**
         * Generates a datagram containing the message necessary to send an update,
         * using the indicated msg type for the indicated distributed object from the
         * AI.
         */
        """
        pass

    def clientFormatGenerateCMU(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        client_format_generate_CMU(DCClass self, object distobj, int do_id, int zone_id, object optional_fields)
        
        /**
         * Generates a datagram containing the message necessary to generate a new
         * distributed object from the client.  This requires querying the object for
         * the initial value of its required fields.
         *
         * optional_fields is a list of fieldNames to generate in addition to the
         * normal required fields.
         *
         * This method is only called by the CMU implementation.
         */
        """
        pass

    def clientFormatUpdate(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        client_format_update(DCClass self, str field_name, int do_id, object args)
        
        /**
         * Generates a datagram containing the message necessary to send an update for
         * the indicated distributed object from the client.
         */
        """
        pass

    def client_format_generate_CMU(self, DCClass_self, object_distobj, int_do_id, int_zone_id, object_optional_fields): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        client_format_generate_CMU(DCClass self, object distobj, int do_id, int zone_id, object optional_fields)
        
        /**
         * Generates a datagram containing the message necessary to generate a new
         * distributed object from the client.  This requires querying the object for
         * the initial value of its required fields.
         *
         * optional_fields is a list of fieldNames to generate in addition to the
         * normal required fields.
         *
         * This method is only called by the CMU implementation.
         */
        """
        pass

    def client_format_update(self, DCClass_self, str_field_name, int_do_id, object_args): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        client_format_update(DCClass self, str field_name, int do_id, object args)
        
        /**
         * Generates a datagram containing the message necessary to send an update for
         * the indicated distributed object from the client.
         */
        """
        pass

    def directUpdate(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        direct_update(const DCClass self, object distobj, str field_name, const Datagram datagram)
        direct_update(const DCClass self, object distobj, str field_name, bytes value_blob)
        
        /**
         * Processes an update for a named field from a packed value blob.
         */
        
        /**
         * Processes an update for a named field from a packed datagram.
         */
        """
        pass

    def direct_update(self, const_DCClass_self, object_distobj, str_field_name, const_Datagram_datagram): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        direct_update(const DCClass self, object distobj, str field_name, const Datagram datagram)
        direct_update(const DCClass self, object distobj, str field_name, bytes value_blob)
        
        /**
         * Processes an update for a named field from a packed value blob.
         */
        
        /**
         * Processes an update for a named field from a packed datagram.
         */
        """
        pass

    def getClassDef(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_def(DCClass self)
        
        /**
         * Returns the class object that was previously associated with this
         * DistributedClass.  This will return a new reference to the object.
         */
        """
        pass

    def getConstructor(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_constructor(DCClass self)
        
        /**
         * Returns the constructor method for this class if it is defined, or NULL if
         * the class uses the default constructor.
         */
        """
        pass

    def getDcFile(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_dc_file(DCClass self)
        
        /**
         * Returns the DCFile object that contains the class.
         */
        """
        pass

    def getField(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_field(DCClass self, int n)
        
        /**
         * Returns the nth field in the class.  This is not necessarily the field with
         * index n; this is the nth field defined in the class directly, ignoring
         * inheritance.
         */
        """
        pass

    def getFieldByIndex(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_field_by_index(DCClass self, int index_number)
        
        /**
         * Returns a pointer to the DCField that has the indicated index number.  If
         * the numbered field is not found in the current class, the parent classes
         * will be searched, so the value returned may not actually be a field within
         * this class.  Returns NULL if there is no such field defined.
         */
        """
        pass

    def getFieldByName(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_field_by_name(DCClass self, str name)
        
        /**
         * Returns a pointer to the DCField that shares the indicated name.  If the
         * named field is not found in the current class, the parent classes will be
         * searched, so the value returned may not actually be a field within this
         * class.  Returns NULL if there is no such field defined.
         */
        """
        pass

    def getInheritedField(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_inherited_field(DCClass self, int n)
        
        /**
         * Returns the nth field field in the class and all of its ancestors.
         *
         * This *used* to be the same thing as get_field_by_index(), back when the
         * fields were numbered sequentially within a class's inheritance hierarchy.
         * Now that fields have a globally unique index number, this is no longer
         * true.
         */
        """
        pass

    def getName(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_name(DCClass self)
        
        /**
         * Returns the name of this class.
         */
        """
        pass

    def getNumber(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_number(DCClass self)
        
        /**
         * Returns a unique index number associated with this class.  This is defined
         * implicitly when the .dc file(s) are read.
         */
        """
        pass

    def getNumFields(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_fields(DCClass self)
        
        /**
         * Returns the number of fields defined directly in this class, ignoring
         * inheritance.
         */
        """
        pass

    def getNumInheritedFields(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_inherited_fields(DCClass self)
        
        /**
         * Returns the total number of field fields defined in this class and all
         * ancestor classes.
         */
        """
        pass

    def getNumParents(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_parents(DCClass self)
        
        /**
         * Returns the number of base classes this class inherits from.
         */
        """
        pass

    def getOwnerClassDef(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_owner_class_def(DCClass self)
        
        /**
         * Returns the owner class object that was previously associated with this
         * DistributedClass.  This will return a new reference to the object.
         */
        """
        pass

    def getParent(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_parent(DCClass self, int n)
        
        /**
         * Returns the nth parent class this class inherits from.
         */
        """
        pass

    def get_class_def(self, DCClass_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_def(DCClass self)
        
        /**
         * Returns the class object that was previously associated with this
         * DistributedClass.  This will return a new reference to the object.
         */
        """
        pass

    def get_constructor(self, DCClass_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_constructor(DCClass self)
        
        /**
         * Returns the constructor method for this class if it is defined, or NULL if
         * the class uses the default constructor.
         */
        """
        pass

    def get_dc_file(self, DCClass_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_dc_file(DCClass self)
        
        /**
         * Returns the DCFile object that contains the class.
         */
        """
        pass

    def get_field(self, DCClass_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_field(DCClass self, int n)
        
        /**
         * Returns the nth field in the class.  This is not necessarily the field with
         * index n; this is the nth field defined in the class directly, ignoring
         * inheritance.
         */
        """
        pass

    def get_field_by_index(self, DCClass_self, int_index_number): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_field_by_index(DCClass self, int index_number)
        
        /**
         * Returns a pointer to the DCField that has the indicated index number.  If
         * the numbered field is not found in the current class, the parent classes
         * will be searched, so the value returned may not actually be a field within
         * this class.  Returns NULL if there is no such field defined.
         */
        """
        pass

    def get_field_by_name(self, DCClass_self, str_name): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_field_by_name(DCClass self, str name)
        
        /**
         * Returns a pointer to the DCField that shares the indicated name.  If the
         * named field is not found in the current class, the parent classes will be
         * searched, so the value returned may not actually be a field within this
         * class.  Returns NULL if there is no such field defined.
         */
        """
        pass

    def get_inherited_field(self, DCClass_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_inherited_field(DCClass self, int n)
        
        /**
         * Returns the nth field field in the class and all of its ancestors.
         *
         * This *used* to be the same thing as get_field_by_index(), back when the
         * fields were numbered sequentially within a class's inheritance hierarchy.
         * Now that fields have a globally unique index number, this is no longer
         * true.
         */
        """
        pass

    def get_name(self, DCClass_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_name(DCClass self)
        
        /**
         * Returns the name of this class.
         */
        """
        pass

    def get_number(self, DCClass_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_number(DCClass self)
        
        /**
         * Returns a unique index number associated with this class.  This is defined
         * implicitly when the .dc file(s) are read.
         */
        """
        pass

    def get_num_fields(self, DCClass_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_fields(DCClass self)
        
        /**
         * Returns the number of fields defined directly in this class, ignoring
         * inheritance.
         */
        """
        pass

    def get_num_inherited_fields(self, DCClass_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_inherited_fields(DCClass self)
        
        /**
         * Returns the total number of field fields defined in this class and all
         * ancestor classes.
         */
        """
        pass

    def get_num_parents(self, DCClass_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_parents(DCClass self)
        
        /**
         * Returns the number of base classes this class inherits from.
         */
        """
        pass

    def get_owner_class_def(self, DCClass_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_owner_class_def(DCClass self)
        
        /**
         * Returns the owner class object that was previously associated with this
         * DistributedClass.  This will return a new reference to the object.
         */
        """
        pass

    def get_parent(self, DCClass_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_parent(DCClass self, int n)
        
        /**
         * Returns the nth parent class this class inherits from.
         */
        """
        pass

    def hasClassDef(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_class_def(DCClass self)
        
        /**
         * Returns true if the DCClass object has an associated Python class
         * definition, false otherwise.
         */
        """
        pass

    def hasConstructor(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_constructor(DCClass self)
        
        /**
         * Returns true if this class has a constructor method, false if it just uses
         * the default constructor.
         */
        """
        pass

    def hasOwnerClassDef(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_owner_class_def(DCClass self)
        
        /**
         * Returns true if the DCClass object has an associated Python owner class
         * definition, false otherwise.
         */
        """
        pass

    def has_class_def(self, DCClass_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_class_def(DCClass self)
        
        /**
         * Returns true if the DCClass object has an associated Python class
         * definition, false otherwise.
         */
        """
        pass

    def has_constructor(self, DCClass_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_constructor(DCClass self)
        
        /**
         * Returns true if this class has a constructor method, false if it just uses
         * the default constructor.
         */
        """
        pass

    def has_owner_class_def(self, DCClass_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_owner_class_def(DCClass self)
        
        /**
         * Returns true if the DCClass object has an associated Python owner class
         * definition, false otherwise.
         */
        """
        pass

    def inheritsFromBogusClass(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        inherits_from_bogus_class(DCClass self)
        
        /**
         * Returns true if this class, or any class in the inheritance heirarchy for
         * this class, is a "bogus" class--a forward reference to an as-yet-undefined
         * class.
         */
        """
        pass

    def inherits_from_bogus_class(self, DCClass_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        inherits_from_bogus_class(DCClass self)
        
        /**
         * Returns true if this class, or any class in the inheritance heirarchy for
         * this class, is a "bogus" class--a forward reference to an as-yet-undefined
         * class.
         */
        """
        pass

    def isBogusClass(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_bogus_class(DCClass self)
        
        /**
         * Returns true if the class has been flagged as a bogus class.  This is set
         * for classes that are generated by the parser as placeholder for missing
         * classes, as when reading a partial file; it should not occur in a normal
         * valid dc file.
         */
        """
        pass

    def isStruct(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_struct(DCClass self)
        
        /**
         * Returns true if the class has been identified with the "struct" keyword in
         * the dc file, false if it was declared with "dclass".
         */
        """
        pass

    def is_bogus_class(self, DCClass_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_bogus_class(DCClass self)
        
        /**
         * Returns true if the class has been flagged as a bogus class.  This is set
         * for classes that are generated by the parser as placeholder for missing
         * classes, as when reading a partial file; it should not occur in a normal
         * valid dc file.
         */
        """
        pass

    def is_struct(self, DCClass_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_struct(DCClass self)
        
        /**
         * Returns true if the class has been identified with the "struct" keyword in
         * the dc file, false if it was declared with "dclass".
         */
        """
        pass

    def output(self, DCClass_self, ostream_out): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        output(DCClass self, ostream out)
        
        /**
         * Write a string representation of this instance to <out>.
         */
        
        /**
         * Write a string representation of this instance to <out>.
         */
        """
        pass

    def packRequiredField(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        pack_required_field(DCClass self, Datagram datagram, object distobj, const DCField field)
        pack_required_field(DCClass self, DCPacker packer, object distobj, const DCField field)
        
        /**
         * Looks up the current value of the indicated field by calling the
         * appropriate get*() function, then packs that value into the datagram.  This
         * field is presumably either a required field or a specified optional field,
         * and we are building up a datagram for the generate-with-required message.
         *
         * Returns true on success, false on failure.
         */
        
        /**
         * Looks up the current value of the indicated field by calling the
         * appropriate get*() function, then packs that value into the packer.  This
         * field is presumably either a required field or a specified optional field,
         * and we are building up a datagram for the generate-with-required message.
         *
         * Returns true on success, false on failure.
         */
        """
        pass

    def pack_required_field(self, DCClass_self, Datagram_datagram, object_distobj, const_DCField_field): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        pack_required_field(DCClass self, Datagram datagram, object distobj, const DCField field)
        pack_required_field(DCClass self, DCPacker packer, object distobj, const DCField field)
        
        /**
         * Looks up the current value of the indicated field by calling the
         * appropriate get*() function, then packs that value into the datagram.  This
         * field is presumably either a required field or a specified optional field,
         * and we are building up a datagram for the generate-with-required message.
         *
         * Returns true on success, false on failure.
         */
        
        /**
         * Looks up the current value of the indicated field by calling the
         * appropriate get*() function, then packs that value into the packer.  This
         * field is presumably either a required field or a specified optional field,
         * and we are building up a datagram for the generate-with-required message.
         *
         * Returns true on success, false on failure.
         */
        """
        pass

    def receiveUpdate(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        receive_update(DCClass self, object distobj, DatagramIterator di)
        
        /**
         * Extracts the update message out of the packer and applies it to the
         * indicated object by calling the appropriate method.
         */
        """
        pass

    def receiveUpdateAllRequired(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        receive_update_all_required(DCClass self, object distobj, DatagramIterator di)
        
        /**
         * Processes a big datagram that includes all of the "required" fields that
         * are sent when an avatar is created.  This is all of the atomic fields that
         * are marked "required", whether they are broadcast or not.
         */
        """
        pass

    def receiveUpdateBroadcastRequired(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        receive_update_broadcast_required(DCClass self, object distobj, DatagramIterator di)
        
        /**
         * Processes a big datagram that includes all of the "required" fields that
         * are sent along with a normal "generate with required" message.  This is all
         * of the atomic fields that are marked "broadcast required".
         */
        """
        pass

    def receiveUpdateBroadcastRequiredOwner(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        receive_update_broadcast_required_owner(DCClass self, object distobj, DatagramIterator di)
        
        /**
         * Processes a big datagram that includes all of the "required" fields that
         * are sent along with a normal "generate with required" message.  This is all
         * of the atomic fields that are marked "broadcast ownrecv". Should be used
         * for 'owner-view' objects.
         */
        """
        pass

    def receiveUpdateOther(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        receive_update_other(DCClass self, object distobj, DatagramIterator di)
        
        /**
         * Processes a datagram that lists some additional fields that are broadcast
         * in one chunk.
         */
        """
        pass

    def receive_update(self, DCClass_self, object_distobj, DatagramIterator_di): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        receive_update(DCClass self, object distobj, DatagramIterator di)
        
        /**
         * Extracts the update message out of the packer and applies it to the
         * indicated object by calling the appropriate method.
         */
        """
        pass

    def receive_update_all_required(self, DCClass_self, object_distobj, DatagramIterator_di): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        receive_update_all_required(DCClass self, object distobj, DatagramIterator di)
        
        /**
         * Processes a big datagram that includes all of the "required" fields that
         * are sent when an avatar is created.  This is all of the atomic fields that
         * are marked "required", whether they are broadcast or not.
         */
        """
        pass

    def receive_update_broadcast_required(self, DCClass_self, object_distobj, DatagramIterator_di): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        receive_update_broadcast_required(DCClass self, object distobj, DatagramIterator di)
        
        /**
         * Processes a big datagram that includes all of the "required" fields that
         * are sent along with a normal "generate with required" message.  This is all
         * of the atomic fields that are marked "broadcast required".
         */
        """
        pass

    def receive_update_broadcast_required_owner(self, DCClass_self, object_distobj, DatagramIterator_di): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        receive_update_broadcast_required_owner(DCClass self, object distobj, DatagramIterator di)
        
        /**
         * Processes a big datagram that includes all of the "required" fields that
         * are sent along with a normal "generate with required" message.  This is all
         * of the atomic fields that are marked "broadcast ownrecv". Should be used
         * for 'owner-view' objects.
         */
        """
        pass

    def receive_update_other(self, DCClass_self, object_distobj, DatagramIterator_di): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        receive_update_other(DCClass self, object distobj, DatagramIterator di)
        
        /**
         * Processes a datagram that lists some additional fields that are broadcast
         * in one chunk.
         */
        """
        pass

    def setClassDef(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_class_def(const DCClass self, object class_def)
        
        /**
         * Sets the class object associated with this DistributedClass.  This object
         * will be used to construct new instances of the class.
         */
        """
        pass

    def setOwnerClassDef(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_owner_class_def(const DCClass self, object owner_class_def)
        
        /**
         * Sets the owner class object associated with this DistributedClass.  This
         * object will be used to construct new owner instances of the class.
         */
        """
        pass

    def set_class_def(self, const_DCClass_self, object_class_def): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_class_def(const DCClass self, object class_def)
        
        /**
         * Sets the class object associated with this DistributedClass.  This object
         * will be used to construct new instances of the class.
         */
        """
        pass

    def set_owner_class_def(self, const_DCClass_self, object_owner_class_def): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_owner_class_def(const DCClass self, object owner_class_def)
        
        /**
         * Sets the owner class object associated with this DistributedClass.  This
         * object will be used to construct new owner instances of the class.
         */
        """
        pass

    def startGenerate(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        start_generate(const DCClass self)
        
        /**
         * Starts the PStats timer going on the "generate" task, that is, marks the
         * beginning of the process of generating a new object, for the purposes of
         * timing this process.
         *
         * This should balance with a corresponding call to stop_generate().
         */
        """
        pass

    def start_generate(self, const_DCClass_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        start_generate(const DCClass self)
        
        /**
         * Starts the PStats timer going on the "generate" task, that is, marks the
         * beginning of the process of generating a new object, for the purposes of
         * timing this process.
         *
         * This should balance with a corresponding call to stop_generate().
         */
        """
        pass

    def stopGenerate(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        stop_generate(const DCClass self)
        
        /**
         * Stops the PStats timer on the "generate" task.  This should balance with a
         * preceding call to start_generate().
         */
        """
        pass

    def stop_generate(self, const_DCClass_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        stop_generate(const DCClass self)
        
        /**
         * Stops the PStats timer on the "generate" task.  This should balance with a
         * preceding call to start_generate().
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
        '__doc__': '/**\n * Defines a particular DistributedClass as read from an input .dc file.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.direct.DCClass' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFDC68DE7D0>'
        '__repr__': None, # (!) real value is "<slot wrapper '__repr__' of 'panda3d.direct.DCClass' objects>"
        '__str__': None, # (!) real value is "<slot wrapper '__str__' of 'panda3d.direct.DCClass' objects>"
        'aiFormatGenerate': None, # (!) real value is "<method 'aiFormatGenerate' of 'panda3d.direct.DCClass' objects>"
        'aiFormatUpdate': None, # (!) real value is "<method 'aiFormatUpdate' of 'panda3d.direct.DCClass' objects>"
        'aiFormatUpdateMsgType': None, # (!) real value is "<method 'aiFormatUpdateMsgType' of 'panda3d.direct.DCClass' objects>"
        'ai_format_generate': None, # (!) real value is "<method 'ai_format_generate' of 'panda3d.direct.DCClass' objects>"
        'ai_format_update': None, # (!) real value is "<method 'ai_format_update' of 'panda3d.direct.DCClass' objects>"
        'ai_format_update_msg_type': None, # (!) real value is "<method 'ai_format_update_msg_type' of 'panda3d.direct.DCClass' objects>"
        'clientFormatGenerateCMU': None, # (!) real value is "<method 'clientFormatGenerateCMU' of 'panda3d.direct.DCClass' objects>"
        'clientFormatUpdate': None, # (!) real value is "<method 'clientFormatUpdate' of 'panda3d.direct.DCClass' objects>"
        'client_format_generate_CMU': None, # (!) real value is "<method 'client_format_generate_CMU' of 'panda3d.direct.DCClass' objects>"
        'client_format_update': None, # (!) real value is "<method 'client_format_update' of 'panda3d.direct.DCClass' objects>"
        'directUpdate': None, # (!) real value is "<method 'directUpdate' of 'panda3d.direct.DCClass' objects>"
        'direct_update': None, # (!) real value is "<method 'direct_update' of 'panda3d.direct.DCClass' objects>"
        'getClassDef': None, # (!) real value is "<method 'getClassDef' of 'panda3d.direct.DCClass' objects>"
        'getConstructor': None, # (!) real value is "<method 'getConstructor' of 'panda3d.direct.DCClass' objects>"
        'getDcFile': None, # (!) real value is "<method 'getDcFile' of 'panda3d.direct.DCClass' objects>"
        'getField': None, # (!) real value is "<method 'getField' of 'panda3d.direct.DCClass' objects>"
        'getFieldByIndex': None, # (!) real value is "<method 'getFieldByIndex' of 'panda3d.direct.DCClass' objects>"
        'getFieldByName': None, # (!) real value is "<method 'getFieldByName' of 'panda3d.direct.DCClass' objects>"
        'getInheritedField': None, # (!) real value is "<method 'getInheritedField' of 'panda3d.direct.DCClass' objects>"
        'getName': None, # (!) real value is "<method 'getName' of 'panda3d.direct.DCClass' objects>"
        'getNumFields': None, # (!) real value is "<method 'getNumFields' of 'panda3d.direct.DCClass' objects>"
        'getNumInheritedFields': None, # (!) real value is "<method 'getNumInheritedFields' of 'panda3d.direct.DCClass' objects>"
        'getNumParents': None, # (!) real value is "<method 'getNumParents' of 'panda3d.direct.DCClass' objects>"
        'getNumber': None, # (!) real value is "<method 'getNumber' of 'panda3d.direct.DCClass' objects>"
        'getOwnerClassDef': None, # (!) real value is "<method 'getOwnerClassDef' of 'panda3d.direct.DCClass' objects>"
        'getParent': None, # (!) real value is "<method 'getParent' of 'panda3d.direct.DCClass' objects>"
        'get_class_def': None, # (!) real value is "<method 'get_class_def' of 'panda3d.direct.DCClass' objects>"
        'get_constructor': None, # (!) real value is "<method 'get_constructor' of 'panda3d.direct.DCClass' objects>"
        'get_dc_file': None, # (!) real value is "<method 'get_dc_file' of 'panda3d.direct.DCClass' objects>"
        'get_field': None, # (!) real value is "<method 'get_field' of 'panda3d.direct.DCClass' objects>"
        'get_field_by_index': None, # (!) real value is "<method 'get_field_by_index' of 'panda3d.direct.DCClass' objects>"
        'get_field_by_name': None, # (!) real value is "<method 'get_field_by_name' of 'panda3d.direct.DCClass' objects>"
        'get_inherited_field': None, # (!) real value is "<method 'get_inherited_field' of 'panda3d.direct.DCClass' objects>"
        'get_name': None, # (!) real value is "<method 'get_name' of 'panda3d.direct.DCClass' objects>"
        'get_num_fields': None, # (!) real value is "<method 'get_num_fields' of 'panda3d.direct.DCClass' objects>"
        'get_num_inherited_fields': None, # (!) real value is "<method 'get_num_inherited_fields' of 'panda3d.direct.DCClass' objects>"
        'get_num_parents': None, # (!) real value is "<method 'get_num_parents' of 'panda3d.direct.DCClass' objects>"
        'get_number': None, # (!) real value is "<method 'get_number' of 'panda3d.direct.DCClass' objects>"
        'get_owner_class_def': None, # (!) real value is "<method 'get_owner_class_def' of 'panda3d.direct.DCClass' objects>"
        'get_parent': None, # (!) real value is "<method 'get_parent' of 'panda3d.direct.DCClass' objects>"
        'hasClassDef': None, # (!) real value is "<method 'hasClassDef' of 'panda3d.direct.DCClass' objects>"
        'hasConstructor': None, # (!) real value is "<method 'hasConstructor' of 'panda3d.direct.DCClass' objects>"
        'hasOwnerClassDef': None, # (!) real value is "<method 'hasOwnerClassDef' of 'panda3d.direct.DCClass' objects>"
        'has_class_def': None, # (!) real value is "<method 'has_class_def' of 'panda3d.direct.DCClass' objects>"
        'has_constructor': None, # (!) real value is "<method 'has_constructor' of 'panda3d.direct.DCClass' objects>"
        'has_owner_class_def': None, # (!) real value is "<method 'has_owner_class_def' of 'panda3d.direct.DCClass' objects>"
        'inheritsFromBogusClass': None, # (!) real value is "<method 'inheritsFromBogusClass' of 'panda3d.direct.DCClass' objects>"
        'inherits_from_bogus_class': None, # (!) real value is "<method 'inherits_from_bogus_class' of 'panda3d.direct.DCClass' objects>"
        'isBogusClass': None, # (!) real value is "<method 'isBogusClass' of 'panda3d.direct.DCClass' objects>"
        'isStruct': None, # (!) real value is "<method 'isStruct' of 'panda3d.direct.DCClass' objects>"
        'is_bogus_class': None, # (!) real value is "<method 'is_bogus_class' of 'panda3d.direct.DCClass' objects>"
        'is_struct': None, # (!) real value is "<method 'is_struct' of 'panda3d.direct.DCClass' objects>"
        'output': None, # (!) real value is "<method 'output' of 'panda3d.direct.DCClass' objects>"
        'packRequiredField': None, # (!) real value is "<method 'packRequiredField' of 'panda3d.direct.DCClass' objects>"
        'pack_required_field': None, # (!) real value is "<method 'pack_required_field' of 'panda3d.direct.DCClass' objects>"
        'receiveUpdate': None, # (!) real value is "<method 'receiveUpdate' of 'panda3d.direct.DCClass' objects>"
        'receiveUpdateAllRequired': None, # (!) real value is "<method 'receiveUpdateAllRequired' of 'panda3d.direct.DCClass' objects>"
        'receiveUpdateBroadcastRequired': None, # (!) real value is "<method 'receiveUpdateBroadcastRequired' of 'panda3d.direct.DCClass' objects>"
        'receiveUpdateBroadcastRequiredOwner': None, # (!) real value is "<method 'receiveUpdateBroadcastRequiredOwner' of 'panda3d.direct.DCClass' objects>"
        'receiveUpdateOther': None, # (!) real value is "<method 'receiveUpdateOther' of 'panda3d.direct.DCClass' objects>"
        'receive_update': None, # (!) real value is "<method 'receive_update' of 'panda3d.direct.DCClass' objects>"
        'receive_update_all_required': None, # (!) real value is "<method 'receive_update_all_required' of 'panda3d.direct.DCClass' objects>"
        'receive_update_broadcast_required': None, # (!) real value is "<method 'receive_update_broadcast_required' of 'panda3d.direct.DCClass' objects>"
        'receive_update_broadcast_required_owner': None, # (!) real value is "<method 'receive_update_broadcast_required_owner' of 'panda3d.direct.DCClass' objects>"
        'receive_update_other': None, # (!) real value is "<method 'receive_update_other' of 'panda3d.direct.DCClass' objects>"
        'setClassDef': None, # (!) real value is "<method 'setClassDef' of 'panda3d.direct.DCClass' objects>"
        'setOwnerClassDef': None, # (!) real value is "<method 'setOwnerClassDef' of 'panda3d.direct.DCClass' objects>"
        'set_class_def': None, # (!) real value is "<method 'set_class_def' of 'panda3d.direct.DCClass' objects>"
        'set_owner_class_def': None, # (!) real value is "<method 'set_owner_class_def' of 'panda3d.direct.DCClass' objects>"
        'startGenerate': None, # (!) real value is "<method 'startGenerate' of 'panda3d.direct.DCClass' objects>"
        'start_generate': None, # (!) real value is "<method 'start_generate' of 'panda3d.direct.DCClass' objects>"
        'stopGenerate': None, # (!) real value is "<method 'stopGenerate' of 'panda3d.direct.DCClass' objects>"
        'stop_generate': None, # (!) real value is "<method 'stop_generate' of 'panda3d.direct.DCClass' objects>"
    }


