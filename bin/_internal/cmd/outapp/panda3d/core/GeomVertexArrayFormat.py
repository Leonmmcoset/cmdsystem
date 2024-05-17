# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .TypedWritableReferenceCount import TypedWritableReferenceCount

from .GeomEnums import GeomEnums

class GeomVertexArrayFormat(TypedWritableReferenceCount, GeomEnums):
    """
    /**
     * This describes the structure of a single array within a Geom data.  See
     * GeomVertexFormat for the parent class which collects together all of the
     * individual GeomVertexArrayFormat objects.
     *
     * A particular array may include any number of standard or user-defined
     * columns.  All columns consist of a sequence of one or more numeric values,
     * packed in any of a variety of formats; the semantic meaning of each column
     * is defined in general with its contents member, and in particular by its
     * name.  The standard array types used most often are named "vertex",
     * "normal", "texcoord", and "color"; other kinds of data may be piggybacked
     * into the data record simply by choosing a unique name.
     */
    """
    def addColumn(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_column(const GeomVertexArrayFormat self, const GeomVertexColumn column)
        add_column(const GeomVertexArrayFormat self, const InternalName name, int num_components, int numeric_type, int contents, int start, int column_alignment)
        
        /**
         * Adds a new column to the specification.  This is a table of per-vertex
         * floating-point numbers such as "vertex" or "normal"; you must specify where
         * in each record the table starts, and how many components (dimensions) exist
         * per vertex.
         *
         * The return value is the index number of the new data type.
         */
        
        /**
         * Adds a new column to the specification.  This is a table of per-vertex
         * floating-point numbers such as "vertex" or "normal"; you must specify where
         * in each record the table starts, and how many components (dimensions) exist
         * per vertex.
         *
         * Adding a column with the same name as a previous type, or that overlaps
         * with one or more previous types, quietly removes the previous type(s).
         *
         * The return value is the index number of the new data type.
         */
        """
        pass

    def add_column(self, const_GeomVertexArrayFormat_self, const_GeomVertexColumn_column): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_column(const GeomVertexArrayFormat self, const GeomVertexColumn column)
        add_column(const GeomVertexArrayFormat self, const InternalName name, int num_components, int numeric_type, int contents, int start, int column_alignment)
        
        /**
         * Adds a new column to the specification.  This is a table of per-vertex
         * floating-point numbers such as "vertex" or "normal"; you must specify where
         * in each record the table starts, and how many components (dimensions) exist
         * per vertex.
         *
         * The return value is the index number of the new data type.
         */
        
        /**
         * Adds a new column to the specification.  This is a table of per-vertex
         * floating-point numbers such as "vertex" or "normal"; you must specify where
         * in each record the table starts, and how many components (dimensions) exist
         * per vertex.
         *
         * Adding a column with the same name as a previous type, or that overlaps
         * with one or more previous types, quietly removes the previous type(s).
         *
         * The return value is the index number of the new data type.
         */
        """
        pass

    def alignColumnsForAnimation(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        align_columns_for_animation(const GeomVertexArrayFormat self)
        
        /**
         * Reprocesses the columns in the format to align the C_point and C_vector
         * columns to 16-byte boundaries to allow for the more efficient SSE2
         * operations (assuming SSE2 is enabled in the build).
         *
         * The caller is responsible for testing vertex_animation_align_16 to decide
         * whether to call this method.
         */
        """
        pass

    def align_columns_for_animation(self, const_GeomVertexArrayFormat_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        align_columns_for_animation(const GeomVertexArrayFormat self)
        
        /**
         * Reprocesses the columns in the format to align the C_point and C_vector
         * columns to 16-byte boundaries to allow for the more efficient SSE2
         * operations (assuming SSE2 is enabled in the build).
         *
         * The caller is responsible for testing vertex_animation_align_16 to decide
         * whether to call this method.
         */
        """
        pass

    def assign(self, const_GeomVertexArrayFormat_self, const_GeomVertexArrayFormat_copy): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        assign(const GeomVertexArrayFormat self, const GeomVertexArrayFormat copy)
        """
        pass

    def clearColumns(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_columns(const GeomVertexArrayFormat self)
        
        /**
         * Removes all columns previously added, sets the stride to zero, and prepares
         * to start over.
         */
        """
        pass

    def clear_columns(self, const_GeomVertexArrayFormat_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_columns(const GeomVertexArrayFormat self)
        
        /**
         * Removes all columns previously added, sets the stride to zero, and prepares
         * to start over.
         */
        """
        pass

    def countUnusedSpace(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        count_unused_space(GeomVertexArrayFormat self)
        
        /**
         * Returns the number of bytes per row that are not assigned to any column.
         */
        """
        pass

    def count_unused_space(self, GeomVertexArrayFormat_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        count_unused_space(GeomVertexArrayFormat self)
        
        /**
         * Returns the number of bytes per row that are not assigned to any column.
         */
        """
        pass

    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getColumn(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_column(GeomVertexArrayFormat self, const InternalName name)
        get_column(GeomVertexArrayFormat self, int i)
        get_column(GeomVertexArrayFormat self, int start_byte, int num_bytes)
        
        /**
         * Returns the ith column of the array.
         */
        
        /**
         * Returns the specification with the indicated name, or NULL if the name is
         * not used.
         */
        
        /**
         * Returns the first specification that overlaps with any of the indicated
         * bytes in the range, or NULL if none do.
         */
        """
        pass

    def getColumns(self, *args, **kwargs): # real signature unknown
        pass

    def getDivisor(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_divisor(GeomVertexArrayFormat self)
        
        /**
         * Returns the divisor attribute for the data in this array.  If 0, it
         * contains per-vertex data.  If 1, it contains per-instance data.  If higher
         * than 1, the read row is advanced for each n instances.
         */
        """
        pass

    def getFormatString(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_format_string(GeomVertexArrayFormat self, bool pad)
        
        /**
         * Returns a string with format codes representing the exact memory layout of
         * the columns in memory, as understood by Python's struct module.  If pad is
         * true, extra padding bytes are added to the end as 'x' characters as needed.
         */
        """
        pass

    def getNumColumns(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_columns(GeomVertexArrayFormat self)
        
        /**
         * Returns the number of different columns in the array.
         */
        """
        pass

    def getPadTo(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_pad_to(GeomVertexArrayFormat self)
        
        /**
         * Returns the byte divisor to which the data record must be padded to meet
         * hardware limitations.  For instance, if this is 4, the stride will be
         * automatically rounded up to the next multiple of 4 bytes.  This value is
         * automatically increased as needed to ensure the individual numeric
         * components in the array are word-aligned.
         */
        """
        pass

    def getStride(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_stride(GeomVertexArrayFormat self)
        
        /**
         * Returns the total number of bytes reserved in the array for each vertex.
         */
        """
        pass

    def getTotalBytes(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_total_bytes(GeomVertexArrayFormat self)
        
        /**
         * Returns the total number of bytes used by the data types within the format,
         * including gaps between elements.
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_column(self, GeomVertexArrayFormat_self, const_InternalName_name): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_column(GeomVertexArrayFormat self, const InternalName name)
        get_column(GeomVertexArrayFormat self, int i)
        get_column(GeomVertexArrayFormat self, int start_byte, int num_bytes)
        
        /**
         * Returns the ith column of the array.
         */
        
        /**
         * Returns the specification with the indicated name, or NULL if the name is
         * not used.
         */
        
        /**
         * Returns the first specification that overlaps with any of the indicated
         * bytes in the range, or NULL if none do.
         */
        """
        pass

    def get_columns(self, *args, **kwargs): # real signature unknown
        pass

    def get_divisor(self, GeomVertexArrayFormat_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_divisor(GeomVertexArrayFormat self)
        
        /**
         * Returns the divisor attribute for the data in this array.  If 0, it
         * contains per-vertex data.  If 1, it contains per-instance data.  If higher
         * than 1, the read row is advanced for each n instances.
         */
        """
        pass

    def get_format_string(self, GeomVertexArrayFormat_self, bool_pad): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_format_string(GeomVertexArrayFormat self, bool pad)
        
        /**
         * Returns a string with format codes representing the exact memory layout of
         * the columns in memory, as understood by Python's struct module.  If pad is
         * true, extra padding bytes are added to the end as 'x' characters as needed.
         */
        """
        pass

    def get_num_columns(self, GeomVertexArrayFormat_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_columns(GeomVertexArrayFormat self)
        
        /**
         * Returns the number of different columns in the array.
         */
        """
        pass

    def get_pad_to(self, GeomVertexArrayFormat_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_pad_to(GeomVertexArrayFormat self)
        
        /**
         * Returns the byte divisor to which the data record must be padded to meet
         * hardware limitations.  For instance, if this is 4, the stride will be
         * automatically rounded up to the next multiple of 4 bytes.  This value is
         * automatically increased as needed to ensure the individual numeric
         * components in the array are word-aligned.
         */
        """
        pass

    def get_stride(self, GeomVertexArrayFormat_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_stride(GeomVertexArrayFormat self)
        
        /**
         * Returns the total number of bytes reserved in the array for each vertex.
         */
        """
        pass

    def get_total_bytes(self, GeomVertexArrayFormat_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_total_bytes(GeomVertexArrayFormat self)
        
        /**
         * Returns the total number of bytes used by the data types within the format,
         * including gaps between elements.
         */
        """
        pass

    def hasColumn(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_column(GeomVertexArrayFormat self, const InternalName name)
        
        /**
         * Returns true if the array has the named column, false otherwise.
         */
        """
        pass

    def has_column(self, GeomVertexArrayFormat_self, const_InternalName_name): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_column(GeomVertexArrayFormat self, const InternalName name)
        
        /**
         * Returns true if the array has the named column, false otherwise.
         */
        """
        pass

    def isDataSubsetOf(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_data_subset_of(GeomVertexArrayFormat self, const GeomVertexArrayFormat other)
        
        /**
         * Returns true if all of the fields in this array format are also present and
         * equivalent in the other array format, and in the same byte positions, and
         * the stride is the same.  That is, true if this format can share the same
         * data pointer as the other format (with possibly some unused gaps).
         */
        """
        pass

    def isRegistered(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_registered(GeomVertexArrayFormat self)
        
        /**
         * Returns true if this format has been registered, false if it has not.  It
         * may not be used for a Geom until it has been registered, but once
         * registered, it may no longer be modified.
         */
        """
        pass

    def is_data_subset_of(self, GeomVertexArrayFormat_self, const_GeomVertexArrayFormat_other): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_data_subset_of(GeomVertexArrayFormat self, const GeomVertexArrayFormat other)
        
        /**
         * Returns true if all of the fields in this array format are also present and
         * equivalent in the other array format, and in the same byte positions, and
         * the stride is the same.  That is, true if this format can share the same
         * data pointer as the other format (with possibly some unused gaps).
         */
        """
        pass

    def is_registered(self, GeomVertexArrayFormat_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_registered(GeomVertexArrayFormat self)
        
        /**
         * Returns true if this format has been registered, false if it has not.  It
         * may not be used for a Geom until it has been registered, but once
         * registered, it may no longer be modified.
         */
        """
        pass

    def output(self, GeomVertexArrayFormat_self, ostream_out): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        output(GeomVertexArrayFormat self, ostream out)
        
        /**
         *
         */
        """
        pass

    def packColumns(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        pack_columns(const GeomVertexArrayFormat self)
        
        /**
         * Removes wasted space between columns.
         */
        """
        pass

    def pack_columns(self, const_GeomVertexArrayFormat_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        pack_columns(const GeomVertexArrayFormat self)
        
        /**
         * Removes wasted space between columns.
         */
        """
        pass

    def registerFormat(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        register_format(const GeomVertexArrayFormat format)
        
        /**
         * Adds the indicated format to the registry, if there is not an equivalent
         * format already there; in either case, returns the pointer to the equivalent
         * format now in the registry.
         *
         * This is similar to GeomVertexFormat::register_format(), except that you
         * generally need not call it explicitly.  Calling
         * GeomVertexFormat::register_format() automatically registers all of the
         * nested array formats.
         */
        """
        pass

    def register_format(self, const_GeomVertexArrayFormat_format): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        register_format(const GeomVertexArrayFormat format)
        
        /**
         * Adds the indicated format to the registry, if there is not an equivalent
         * format already there; in either case, returns the pointer to the equivalent
         * format now in the registry.
         *
         * This is similar to GeomVertexFormat::register_format(), except that you
         * generally need not call it explicitly.  Calling
         * GeomVertexFormat::register_format() automatically registers all of the
         * nested array formats.
         */
        """
        pass

    def removeColumn(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        remove_column(const GeomVertexArrayFormat self, const InternalName name)
        
        /**
         * Removes the column with the indicated name, if any.  This leaves a gap in
         * the byte structure.
         */
        """
        pass

    def remove_column(self, const_GeomVertexArrayFormat_self, const_InternalName_name): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        remove_column(const GeomVertexArrayFormat self, const InternalName name)
        
        /**
         * Removes the column with the indicated name, if any.  This leaves a gap in
         * the byte structure.
         */
        """
        pass

    def setDivisor(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_divisor(const GeomVertexArrayFormat self, int divisor)
        
        /**
         * Set this to 0 to indicate that this array contains per-vertex data, or to 1
         * to indicate that it contains per-instance data.  If higher than 1, the read
         * row is advanced for each n instances.
         */
        """
        pass

    def setPadTo(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_pad_to(const GeomVertexArrayFormat self, int pad_to)
        
        /**
         * Explicitly sets the byte divisor to which the data record must be padded to
         * meet hardware limitations.  See get_pad_to().  Normally it is not necessary
         * to call this unless you have some specific requirements for row-to-row data
         * alignment.  Note that this value may be automatically increased at each
         * subsequent call to add_column().
         */
        """
        pass

    def setStride(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_stride(const GeomVertexArrayFormat self, int stride)
        
        /**
         * Changes the total number of bytes reserved in the array for each vertex.
         * You may not reduce this below get_total_bytes(), but you may increase it
         * arbitrarily.
         *
         * You should avoid arrays with stride higher than 2048, which is the typical
         * limit supported by graphics hardware.
         */
        """
        pass

    def set_divisor(self, const_GeomVertexArrayFormat_self, int_divisor): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_divisor(const GeomVertexArrayFormat self, int divisor)
        
        /**
         * Set this to 0 to indicate that this array contains per-vertex data, or to 1
         * to indicate that it contains per-instance data.  If higher than 1, the read
         * row is advanced for each n instances.
         */
        """
        pass

    def set_pad_to(self, const_GeomVertexArrayFormat_self, int_pad_to): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_pad_to(const GeomVertexArrayFormat self, int pad_to)
        
        /**
         * Explicitly sets the byte divisor to which the data record must be padded to
         * meet hardware limitations.  See get_pad_to().  Normally it is not necessary
         * to call this unless you have some specific requirements for row-to-row data
         * alignment.  Note that this value may be automatically increased at each
         * subsequent call to add_column().
         */
        """
        pass

    def set_stride(self, const_GeomVertexArrayFormat_self, int_stride): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_stride(const GeomVertexArrayFormat self, int stride)
        
        /**
         * Changes the total number of bytes reserved in the array for each vertex.
         * You may not reduce this below get_total_bytes(), but you may increase it
         * arbitrarily.
         *
         * You should avoid arrays with stride higher than 2048, which is the typical
         * limit supported by graphics hardware.
         */
        """
        pass

    def unref(self, GeomVertexArrayFormat_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        unref(GeomVertexArrayFormat self)
        
        /**
         * This method overrides ReferenceCount::unref() to unregister the object when
         * its reference count goes to zero.
         */
        """
        pass

    def upcastToGeomEnums(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        upcast_to_GeomEnums(const GeomVertexArrayFormat self)
        
        upcast from GeomVertexArrayFormat to GeomEnums
        """
        pass

    def upcastToTypedWritableReferenceCount(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        upcast_to_TypedWritableReferenceCount(const GeomVertexArrayFormat self)
        
        upcast from GeomVertexArrayFormat to TypedWritableReferenceCount
        """
        pass

    def upcast_to_GeomEnums(self, const_GeomVertexArrayFormat_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        upcast_to_GeomEnums(const GeomVertexArrayFormat self)
        
        upcast from GeomVertexArrayFormat to GeomEnums
        """
        pass

    def upcast_to_TypedWritableReferenceCount(self, const_GeomVertexArrayFormat_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        upcast_to_TypedWritableReferenceCount(const GeomVertexArrayFormat self)
        
        upcast from GeomVertexArrayFormat to TypedWritableReferenceCount
        """
        pass

    def write(self, GeomVertexArrayFormat_self, ostream_out, int_indent_level): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        write(GeomVertexArrayFormat self, ostream out, int indent_level)
        
        /**
         *
         */
        """
        pass

    def writeWithData(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        write_with_data(GeomVertexArrayFormat self, ostream out, int indent_level, const GeomVertexArrayData array_data)
        
        /**
         *
         */
        """
        pass

    def write_with_data(self, GeomVertexArrayFormat_self, ostream_out, int_indent_level, const_GeomVertexArrayData_array_data): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        write_with_data(GeomVertexArrayFormat self, ostream out, int indent_level, const GeomVertexArrayData array_data)
        
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

    columns = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    divisor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pad_to = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    registered = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    stride = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    total_bytes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.core.GeomVertexArrayFormat' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.core.GeomVertexArrayFormat' objects>"
        '__doc__': '/**\n * This describes the structure of a single array within a Geom data.  See\n * GeomVertexFormat for the parent class which collects together all of the\n * individual GeomVertexArrayFormat objects.\n *\n * A particular array may include any number of standard or user-defined\n * columns.  All columns consist of a sequence of one or more numeric values,\n * packed in any of a variety of formats; the semantic meaning of each column\n * is defined in general with its contents member, and in particular by its\n * name.  The standard array types used most often are named "vertex",\n * "normal", "texcoord", and "color"; other kinds of data may be piggybacked\n * into the data record simply by choosing a unique name.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.GeomVertexArrayFormat' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE2FA120>'
        '__repr__': None, # (!) real value is "<slot wrapper '__repr__' of 'panda3d.core.GeomVertexArrayFormat' objects>"
        '__str__': None, # (!) real value is "<slot wrapper '__str__' of 'panda3d.core.GeomVertexArrayFormat' objects>"
        'addColumn': None, # (!) real value is "<method 'addColumn' of 'panda3d.core.GeomVertexArrayFormat' objects>"
        'add_column': None, # (!) real value is "<method 'add_column' of 'panda3d.core.GeomVertexArrayFormat' objects>"
        'alignColumnsForAnimation': None, # (!) real value is "<method 'alignColumnsForAnimation' of 'panda3d.core.GeomVertexArrayFormat' objects>"
        'align_columns_for_animation': None, # (!) real value is "<method 'align_columns_for_animation' of 'panda3d.core.GeomVertexArrayFormat' objects>"
        'assign': None, # (!) real value is "<method 'assign' of 'panda3d.core.GeomVertexArrayFormat' objects>"
        'clearColumns': None, # (!) real value is "<method 'clearColumns' of 'panda3d.core.GeomVertexArrayFormat' objects>"
        'clear_columns': None, # (!) real value is "<method 'clear_columns' of 'panda3d.core.GeomVertexArrayFormat' objects>"
        'columns': None, # (!) real value is "<attribute 'columns' of 'panda3d.core.GeomVertexArrayFormat' objects>"
        'countUnusedSpace': None, # (!) real value is "<method 'countUnusedSpace' of 'panda3d.core.GeomVertexArrayFormat' objects>"
        'count_unused_space': None, # (!) real value is "<method 'count_unused_space' of 'panda3d.core.GeomVertexArrayFormat' objects>"
        'divisor': None, # (!) real value is "<attribute 'divisor' of 'panda3d.core.GeomVertexArrayFormat' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE2FA120>)>'
        'getColumn': None, # (!) real value is "<method 'getColumn' of 'panda3d.core.GeomVertexArrayFormat' objects>"
        'getColumns': None, # (!) real value is "<method 'getColumns' of 'panda3d.core.GeomVertexArrayFormat' objects>"
        'getDivisor': None, # (!) real value is "<method 'getDivisor' of 'panda3d.core.GeomVertexArrayFormat' objects>"
        'getFormatString': None, # (!) real value is "<method 'getFormatString' of 'panda3d.core.GeomVertexArrayFormat' objects>"
        'getNumColumns': None, # (!) real value is "<method 'getNumColumns' of 'panda3d.core.GeomVertexArrayFormat' objects>"
        'getPadTo': None, # (!) real value is "<method 'getPadTo' of 'panda3d.core.GeomVertexArrayFormat' objects>"
        'getStride': None, # (!) real value is "<method 'getStride' of 'panda3d.core.GeomVertexArrayFormat' objects>"
        'getTotalBytes': None, # (!) real value is "<method 'getTotalBytes' of 'panda3d.core.GeomVertexArrayFormat' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE2FA120>)>'
        'get_column': None, # (!) real value is "<method 'get_column' of 'panda3d.core.GeomVertexArrayFormat' objects>"
        'get_columns': None, # (!) real value is "<method 'get_columns' of 'panda3d.core.GeomVertexArrayFormat' objects>"
        'get_divisor': None, # (!) real value is "<method 'get_divisor' of 'panda3d.core.GeomVertexArrayFormat' objects>"
        'get_format_string': None, # (!) real value is "<method 'get_format_string' of 'panda3d.core.GeomVertexArrayFormat' objects>"
        'get_num_columns': None, # (!) real value is "<method 'get_num_columns' of 'panda3d.core.GeomVertexArrayFormat' objects>"
        'get_pad_to': None, # (!) real value is "<method 'get_pad_to' of 'panda3d.core.GeomVertexArrayFormat' objects>"
        'get_stride': None, # (!) real value is "<method 'get_stride' of 'panda3d.core.GeomVertexArrayFormat' objects>"
        'get_total_bytes': None, # (!) real value is "<method 'get_total_bytes' of 'panda3d.core.GeomVertexArrayFormat' objects>"
        'hasColumn': None, # (!) real value is "<method 'hasColumn' of 'panda3d.core.GeomVertexArrayFormat' objects>"
        'has_column': None, # (!) real value is "<method 'has_column' of 'panda3d.core.GeomVertexArrayFormat' objects>"
        'isDataSubsetOf': None, # (!) real value is "<method 'isDataSubsetOf' of 'panda3d.core.GeomVertexArrayFormat' objects>"
        'isRegistered': None, # (!) real value is "<method 'isRegistered' of 'panda3d.core.GeomVertexArrayFormat' objects>"
        'is_data_subset_of': None, # (!) real value is "<method 'is_data_subset_of' of 'panda3d.core.GeomVertexArrayFormat' objects>"
        'is_registered': None, # (!) real value is "<method 'is_registered' of 'panda3d.core.GeomVertexArrayFormat' objects>"
        'output': None, # (!) real value is "<method 'output' of 'panda3d.core.GeomVertexArrayFormat' objects>"
        'packColumns': None, # (!) real value is "<method 'packColumns' of 'panda3d.core.GeomVertexArrayFormat' objects>"
        'pack_columns': None, # (!) real value is "<method 'pack_columns' of 'panda3d.core.GeomVertexArrayFormat' objects>"
        'pad_to': None, # (!) real value is "<attribute 'pad_to' of 'panda3d.core.GeomVertexArrayFormat' objects>"
        'registerFormat': None, # (!) real value is '<staticmethod(<built-in method registerFormat of type object at 0x00007FFCFE2FA120>)>'
        'register_format': None, # (!) real value is '<staticmethod(<built-in method register_format of type object at 0x00007FFCFE2FA120>)>'
        'registered': None, # (!) real value is "<attribute 'registered' of 'panda3d.core.GeomVertexArrayFormat' objects>"
        'removeColumn': None, # (!) real value is "<method 'removeColumn' of 'panda3d.core.GeomVertexArrayFormat' objects>"
        'remove_column': None, # (!) real value is "<method 'remove_column' of 'panda3d.core.GeomVertexArrayFormat' objects>"
        'setDivisor': None, # (!) real value is "<method 'setDivisor' of 'panda3d.core.GeomVertexArrayFormat' objects>"
        'setPadTo': None, # (!) real value is "<method 'setPadTo' of 'panda3d.core.GeomVertexArrayFormat' objects>"
        'setStride': None, # (!) real value is "<method 'setStride' of 'panda3d.core.GeomVertexArrayFormat' objects>"
        'set_divisor': None, # (!) real value is "<method 'set_divisor' of 'panda3d.core.GeomVertexArrayFormat' objects>"
        'set_pad_to': None, # (!) real value is "<method 'set_pad_to' of 'panda3d.core.GeomVertexArrayFormat' objects>"
        'set_stride': None, # (!) real value is "<method 'set_stride' of 'panda3d.core.GeomVertexArrayFormat' objects>"
        'stride': None, # (!) real value is "<attribute 'stride' of 'panda3d.core.GeomVertexArrayFormat' objects>"
        'total_bytes': None, # (!) real value is "<attribute 'total_bytes' of 'panda3d.core.GeomVertexArrayFormat' objects>"
        'unref': None, # (!) real value is "<method 'unref' of 'panda3d.core.GeomVertexArrayFormat' objects>"
        'upcastToGeomEnums': None, # (!) real value is "<method 'upcastToGeomEnums' of 'panda3d.core.GeomVertexArrayFormat' objects>"
        'upcastToTypedWritableReferenceCount': None, # (!) real value is "<method 'upcastToTypedWritableReferenceCount' of 'panda3d.core.GeomVertexArrayFormat' objects>"
        'upcast_to_GeomEnums': None, # (!) real value is "<method 'upcast_to_GeomEnums' of 'panda3d.core.GeomVertexArrayFormat' objects>"
        'upcast_to_TypedWritableReferenceCount': None, # (!) real value is "<method 'upcast_to_TypedWritableReferenceCount' of 'panda3d.core.GeomVertexArrayFormat' objects>"
        'write': None, # (!) real value is "<method 'write' of 'panda3d.core.GeomVertexArrayFormat' objects>"
        'writeWithData': None, # (!) real value is "<method 'writeWithData' of 'panda3d.core.GeomVertexArrayFormat' objects>"
        'write_with_data': None, # (!) real value is "<method 'write_with_data' of 'panda3d.core.GeomVertexArrayFormat' objects>"
    }


