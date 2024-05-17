# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .GeomEnums import GeomEnums

class GeomVertexColumn(GeomEnums):
    """
    /**
     * This defines how a single column is interleaved within a vertex array
     * stored within a Geom.  The GeomVertexArrayFormat class maintains a list of
     * these to completely define a particular array structure.
     */
    """
    def assign(self, const_GeomVertexColumn_self, const_GeomVertexColumn_copy): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        assign(const GeomVertexColumn self, const GeomVertexColumn copy)
        """
        pass

    def getColumnAlignment(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_column_alignment(GeomVertexColumn self)
        
        /**
         * Returns the alignment requirements for this column.  If this is greater
         * than 1, it restricts the column to appear only on memory addresses that are
         * integer multiples of this value; this has implications for this column's
         * start value, as well as the stride of the resulting array.
         */
        """
        pass

    def getComponentBytes(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_component_bytes(GeomVertexColumn self)
        
        /**
         * Returns the number of bytes used by each component (that is, by one element
         * of the numeric type).
         */
        """
        pass

    def getContents(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_contents(GeomVertexColumn self)
        
        /**
         * Returns the token representing the semantic meaning of the stored value.
         */
        """
        pass

    def getElementStride(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_element_stride(GeomVertexColumn self)
        
        /**
         * This value is only relevant for matrix types.  Returns the number of bytes
         * to add to access the next row of the matrix.
         */
        """
        pass

    def getName(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_name(GeomVertexColumn self)
        
        /**
         * Returns the name of this particular data field, e.g.  "vertex" or "normal".
         * The name may be a user-defined string, or it may be one of the standard
         * system-defined field types.  Only the system-defined field types are used
         * for the actual rendering.
         */
        """
        pass

    def getNumComponents(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_components(GeomVertexColumn self)
        
        /**
         * Returns the number of components of the column: the number of instances of
         * the NumericType in each element.  This is usually, but not always, the same
         * thing as get_num_values().
         */
        """
        pass

    def getNumElements(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_elements(GeomVertexColumn self)
        
        /**
         * Returns the number of times this column is repeated.  This is usually 1,
         * except for matrices.
         */
        """
        pass

    def getNumericType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_numeric_type(GeomVertexColumn self)
        
        /**
         * Returns the token representing the numeric type of the data storage.
         */
        """
        pass

    def getNumValues(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_values(GeomVertexColumn self)
        
        /**
         * Returns the number of numeric values of the column: the number of distinct
         * numeric values that go into each element.  This is usually, but not always,
         * the same thing as get_num_components(); the difference is in the case of a
         * composite numeric type like NT_packed_dcba, which has four numeric values
         * per component.
         */
        """
        pass

    def getStart(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_start(GeomVertexColumn self)
        
        /**
         * Returns the byte within the array record at which this column starts.  This
         * can be set to non-zero to implement interleaved arrays.
         */
        """
        pass

    def getTotalBytes(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_total_bytes(GeomVertexColumn self)
        
        /**
         * Returns the number of bytes used by each element of the column:
         * component_bytes * num_components.
         */
        """
        pass

    def get_column_alignment(self, GeomVertexColumn_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_column_alignment(GeomVertexColumn self)
        
        /**
         * Returns the alignment requirements for this column.  If this is greater
         * than 1, it restricts the column to appear only on memory addresses that are
         * integer multiples of this value; this has implications for this column's
         * start value, as well as the stride of the resulting array.
         */
        """
        pass

    def get_component_bytes(self, GeomVertexColumn_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_component_bytes(GeomVertexColumn self)
        
        /**
         * Returns the number of bytes used by each component (that is, by one element
         * of the numeric type).
         */
        """
        pass

    def get_contents(self, GeomVertexColumn_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_contents(GeomVertexColumn self)
        
        /**
         * Returns the token representing the semantic meaning of the stored value.
         */
        """
        pass

    def get_element_stride(self, GeomVertexColumn_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_element_stride(GeomVertexColumn self)
        
        /**
         * This value is only relevant for matrix types.  Returns the number of bytes
         * to add to access the next row of the matrix.
         */
        """
        pass

    def get_name(self, GeomVertexColumn_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_name(GeomVertexColumn self)
        
        /**
         * Returns the name of this particular data field, e.g.  "vertex" or "normal".
         * The name may be a user-defined string, or it may be one of the standard
         * system-defined field types.  Only the system-defined field types are used
         * for the actual rendering.
         */
        """
        pass

    def get_numeric_type(self, GeomVertexColumn_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_numeric_type(GeomVertexColumn self)
        
        /**
         * Returns the token representing the numeric type of the data storage.
         */
        """
        pass

    def get_num_components(self, GeomVertexColumn_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_components(GeomVertexColumn self)
        
        /**
         * Returns the number of components of the column: the number of instances of
         * the NumericType in each element.  This is usually, but not always, the same
         * thing as get_num_values().
         */
        """
        pass

    def get_num_elements(self, GeomVertexColumn_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_elements(GeomVertexColumn self)
        
        /**
         * Returns the number of times this column is repeated.  This is usually 1,
         * except for matrices.
         */
        """
        pass

    def get_num_values(self, GeomVertexColumn_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_values(GeomVertexColumn self)
        
        /**
         * Returns the number of numeric values of the column: the number of distinct
         * numeric values that go into each element.  This is usually, but not always,
         * the same thing as get_num_components(); the difference is in the case of a
         * composite numeric type like NT_packed_dcba, which has four numeric values
         * per component.
         */
        """
        pass

    def get_start(self, GeomVertexColumn_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_start(GeomVertexColumn self)
        
        /**
         * Returns the byte within the array record at which this column starts.  This
         * can be set to non-zero to implement interleaved arrays.
         */
        """
        pass

    def get_total_bytes(self, GeomVertexColumn_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_total_bytes(GeomVertexColumn self)
        
        /**
         * Returns the number of bytes used by each element of the column:
         * component_bytes * num_components.
         */
        """
        pass

    def hasHomogeneousCoord(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_homogeneous_coord(GeomVertexColumn self)
        
        /**
         * Returns true if this Contents type is one that includes a homogeneous
         * coordinate in the fourth component, or false otherwise.  If this is true,
         * correct operation on the vertex data may require scaling by the homogeneous
         * coordinate from time to time (but in general this is handled automatically
         * if you use the 3-component or smaller forms of get_data() and set_data()).
         */
        """
        pass

    def has_homogeneous_coord(self, GeomVertexColumn_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_homogeneous_coord(GeomVertexColumn self)
        
        /**
         * Returns true if this Contents type is one that includes a homogeneous
         * coordinate in the fourth component, or false otherwise.  If this is true,
         * correct operation on the vertex data may require scaling by the homogeneous
         * coordinate from time to time (but in general this is handled automatically
         * if you use the 3-component or smaller forms of get_data() and set_data()).
         */
        """
        pass

    def isBytewiseEquivalent(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_bytewise_equivalent(GeomVertexColumn self, const GeomVertexColumn other)
        
        /**
         * Returns true if the data store of this column is exactly the same as that
         * of the other, irrespective of name or start position within the record.
         */
        """
        pass

    def is_bytewise_equivalent(self, GeomVertexColumn_self, const_GeomVertexColumn_other): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_bytewise_equivalent(GeomVertexColumn self, const GeomVertexColumn other)
        
        /**
         * Returns true if the data store of this column is exactly the same as that
         * of the other, irrespective of name or start position within the record.
         */
        """
        pass

    def output(self, GeomVertexColumn_self, ostream_out): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        output(GeomVertexColumn self, ostream out)
        
        /**
         *
         */
        """
        pass

    def overlapsWith(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        overlaps_with(GeomVertexColumn self, int start_byte, int num_bytes)
        
        /**
         * Returns true if this column overlaps with any of the bytes in the indicated
         * range, false if it does not.
         */
        """
        pass

    def overlaps_with(self, GeomVertexColumn_self, int_start_byte, int_num_bytes): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        overlaps_with(GeomVertexColumn self, int start_byte, int num_bytes)
        
        /**
         * Returns true if this column overlaps with any of the bytes in the indicated
         * range, false if it does not.
         */
        """
        pass

    def setColumnAlignment(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_column_alignment(const GeomVertexColumn self, int column_alignment)
        
        /**
         * Changes the column alignment of an existing column.  This is only legal on
         * an unregistered format (i.e.  when constructing the format initially).
         */
        """
        pass

    def setContents(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_contents(const GeomVertexColumn self, int contents)
        
        /**
         * Changes the semantic meaning of an existing column.  This is only legal on
         * an unregistered format (i.e.  when constructing the format initially).
         */
        """
        pass

    def setName(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_name(const GeomVertexColumn self, InternalName name)
        
        /**
         * Replaces the name of an existing column.  This is only legal on an
         * unregistered format (i.e.  when constructing the format initially).
         */
        """
        pass

    def setNumComponents(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_num_components(const GeomVertexColumn self, int num_components)
        
        /**
         * Changes the number of components of an existing column.  This is only legal
         * on an unregistered format (i.e.  when constructing the format initially).
         */
        """
        pass

    def setNumericType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_numeric_type(const GeomVertexColumn self, int numeric_type)
        
        /**
         * Changes the numeric type an existing column.  This is only legal on an
         * unregistered format (i.e.  when constructing the format initially).
         */
        """
        pass

    def setStart(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_start(const GeomVertexColumn self, int start)
        
        /**
         * Changes the start byte of an existing column.  This is only legal on an
         * unregistered format (i.e.  when constructing the format initially).
         */
        """
        pass

    def set_column_alignment(self, const_GeomVertexColumn_self, int_column_alignment): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_column_alignment(const GeomVertexColumn self, int column_alignment)
        
        /**
         * Changes the column alignment of an existing column.  This is only legal on
         * an unregistered format (i.e.  when constructing the format initially).
         */
        """
        pass

    def set_contents(self, const_GeomVertexColumn_self, int_contents): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_contents(const GeomVertexColumn self, int contents)
        
        /**
         * Changes the semantic meaning of an existing column.  This is only legal on
         * an unregistered format (i.e.  when constructing the format initially).
         */
        """
        pass

    def set_name(self, const_GeomVertexColumn_self, InternalName_name): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_name(const GeomVertexColumn self, InternalName name)
        
        /**
         * Replaces the name of an existing column.  This is only legal on an
         * unregistered format (i.e.  when constructing the format initially).
         */
        """
        pass

    def set_numeric_type(self, const_GeomVertexColumn_self, int_numeric_type): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_numeric_type(const GeomVertexColumn self, int numeric_type)
        
        /**
         * Changes the numeric type an existing column.  This is only legal on an
         * unregistered format (i.e.  when constructing the format initially).
         */
        """
        pass

    def set_num_components(self, const_GeomVertexColumn_self, int_num_components): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_num_components(const GeomVertexColumn self, int num_components)
        
        /**
         * Changes the number of components of an existing column.  This is only legal
         * on an unregistered format (i.e.  when constructing the format initially).
         */
        """
        pass

    def set_start(self, const_GeomVertexColumn_self, int_start): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_start(const GeomVertexColumn self, int start)
        
        /**
         * Changes the start byte of an existing column.  This is only legal on an
         * unregistered format (i.e.  when constructing the format initially).
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
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.core.GeomVertexColumn' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.core.GeomVertexColumn' objects>"
        '__doc__': '/**\n * This defines how a single column is interleaved within a vertex array\n * stored within a Geom.  The GeomVertexArrayFormat class maintains a list of\n * these to completely define a particular array structure.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.GeomVertexColumn' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE2F9F50>'
        '__repr__': None, # (!) real value is "<slot wrapper '__repr__' of 'panda3d.core.GeomVertexColumn' objects>"
        '__str__': None, # (!) real value is "<slot wrapper '__str__' of 'panda3d.core.GeomVertexColumn' objects>"
        'assign': None, # (!) real value is "<method 'assign' of 'panda3d.core.GeomVertexColumn' objects>"
        'getColumnAlignment': None, # (!) real value is "<method 'getColumnAlignment' of 'panda3d.core.GeomVertexColumn' objects>"
        'getComponentBytes': None, # (!) real value is "<method 'getComponentBytes' of 'panda3d.core.GeomVertexColumn' objects>"
        'getContents': None, # (!) real value is "<method 'getContents' of 'panda3d.core.GeomVertexColumn' objects>"
        'getElementStride': None, # (!) real value is "<method 'getElementStride' of 'panda3d.core.GeomVertexColumn' objects>"
        'getName': None, # (!) real value is "<method 'getName' of 'panda3d.core.GeomVertexColumn' objects>"
        'getNumComponents': None, # (!) real value is "<method 'getNumComponents' of 'panda3d.core.GeomVertexColumn' objects>"
        'getNumElements': None, # (!) real value is "<method 'getNumElements' of 'panda3d.core.GeomVertexColumn' objects>"
        'getNumValues': None, # (!) real value is "<method 'getNumValues' of 'panda3d.core.GeomVertexColumn' objects>"
        'getNumericType': None, # (!) real value is "<method 'getNumericType' of 'panda3d.core.GeomVertexColumn' objects>"
        'getStart': None, # (!) real value is "<method 'getStart' of 'panda3d.core.GeomVertexColumn' objects>"
        'getTotalBytes': None, # (!) real value is "<method 'getTotalBytes' of 'panda3d.core.GeomVertexColumn' objects>"
        'get_column_alignment': None, # (!) real value is "<method 'get_column_alignment' of 'panda3d.core.GeomVertexColumn' objects>"
        'get_component_bytes': None, # (!) real value is "<method 'get_component_bytes' of 'panda3d.core.GeomVertexColumn' objects>"
        'get_contents': None, # (!) real value is "<method 'get_contents' of 'panda3d.core.GeomVertexColumn' objects>"
        'get_element_stride': None, # (!) real value is "<method 'get_element_stride' of 'panda3d.core.GeomVertexColumn' objects>"
        'get_name': None, # (!) real value is "<method 'get_name' of 'panda3d.core.GeomVertexColumn' objects>"
        'get_num_components': None, # (!) real value is "<method 'get_num_components' of 'panda3d.core.GeomVertexColumn' objects>"
        'get_num_elements': None, # (!) real value is "<method 'get_num_elements' of 'panda3d.core.GeomVertexColumn' objects>"
        'get_num_values': None, # (!) real value is "<method 'get_num_values' of 'panda3d.core.GeomVertexColumn' objects>"
        'get_numeric_type': None, # (!) real value is "<method 'get_numeric_type' of 'panda3d.core.GeomVertexColumn' objects>"
        'get_start': None, # (!) real value is "<method 'get_start' of 'panda3d.core.GeomVertexColumn' objects>"
        'get_total_bytes': None, # (!) real value is "<method 'get_total_bytes' of 'panda3d.core.GeomVertexColumn' objects>"
        'hasHomogeneousCoord': None, # (!) real value is "<method 'hasHomogeneousCoord' of 'panda3d.core.GeomVertexColumn' objects>"
        'has_homogeneous_coord': None, # (!) real value is "<method 'has_homogeneous_coord' of 'panda3d.core.GeomVertexColumn' objects>"
        'isBytewiseEquivalent': None, # (!) real value is "<method 'isBytewiseEquivalent' of 'panda3d.core.GeomVertexColumn' objects>"
        'is_bytewise_equivalent': None, # (!) real value is "<method 'is_bytewise_equivalent' of 'panda3d.core.GeomVertexColumn' objects>"
        'output': None, # (!) real value is "<method 'output' of 'panda3d.core.GeomVertexColumn' objects>"
        'overlapsWith': None, # (!) real value is "<method 'overlapsWith' of 'panda3d.core.GeomVertexColumn' objects>"
        'overlaps_with': None, # (!) real value is "<method 'overlaps_with' of 'panda3d.core.GeomVertexColumn' objects>"
        'setColumnAlignment': None, # (!) real value is "<method 'setColumnAlignment' of 'panda3d.core.GeomVertexColumn' objects>"
        'setContents': None, # (!) real value is "<method 'setContents' of 'panda3d.core.GeomVertexColumn' objects>"
        'setName': None, # (!) real value is "<method 'setName' of 'panda3d.core.GeomVertexColumn' objects>"
        'setNumComponents': None, # (!) real value is "<method 'setNumComponents' of 'panda3d.core.GeomVertexColumn' objects>"
        'setNumericType': None, # (!) real value is "<method 'setNumericType' of 'panda3d.core.GeomVertexColumn' objects>"
        'setStart': None, # (!) real value is "<method 'setStart' of 'panda3d.core.GeomVertexColumn' objects>"
        'set_column_alignment': None, # (!) real value is "<method 'set_column_alignment' of 'panda3d.core.GeomVertexColumn' objects>"
        'set_contents': None, # (!) real value is "<method 'set_contents' of 'panda3d.core.GeomVertexColumn' objects>"
        'set_name': None, # (!) real value is "<method 'set_name' of 'panda3d.core.GeomVertexColumn' objects>"
        'set_num_components': None, # (!) real value is "<method 'set_num_components' of 'panda3d.core.GeomVertexColumn' objects>"
        'set_numeric_type': None, # (!) real value is "<method 'set_numeric_type' of 'panda3d.core.GeomVertexColumn' objects>"
        'set_start': None, # (!) real value is "<method 'set_start' of 'panda3d.core.GeomVertexColumn' objects>"
    }


