# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .GeomVertexWriter import GeomVertexWriter

from .GeomVertexReader import GeomVertexReader

class GeomVertexRewriter(GeomVertexWriter, GeomVertexReader):
    """
    /**
     * This object provides the functionality of both a GeomVertexReader and a
     * GeomVertexWriter, combined together into one convenient package.  It is
     * designed for making a single pass over a GeomVertexData object, modifying
     * rows as it goes.
     *
     * Although it doesn't provide any real performance benefit over using a
     * separate reader and writer on the same data, it should probably be used in
     * preference to a separate reader and writer, because it makes an effort to
     * manage the reference counts properly between the reader and the writer to
     * avoid accidentally dereferencing either array while recopying.
     */
    """
    def assign(self, const_GeomVertexRewriter_self, const_GeomVertexRewriter_copy): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        assign(const GeomVertexRewriter self, const GeomVertexRewriter copy)
        """
        pass

    def clear(self, const_GeomVertexRewriter_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear(const GeomVertexRewriter self)
        
        /**
         * Resets the GeomVertexRewriter to the initial state.
         */
        """
        pass

    def getArray(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_array(GeomVertexRewriter self)
        
        /**
         * Returns the array index containing the data type that the rewriter is
         * working on.
         */
        """
        pass

    def getArrayData(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_array_data(GeomVertexRewriter self)
        
        /**
         * Returns the particular array object that the rewriter is currently
         * processing.
         */
        """
        pass

    def getArrayHandle(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_array_handle(GeomVertexRewriter self)
        
        /**
         * Returns the write handle to the array object that the rewriter is currently
         * processing.  This low-level call should be used with caution; be careful
         * with modifying the data in the handle out from under the
         * GeomVertexRewriter.
         */
        """
        pass

    def getColumn(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_column(GeomVertexRewriter self)
        
        /**
         * Returns the description of the data type that the rewriter is working on.
         */
        """
        pass

    def getCurrentThread(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_current_thread(GeomVertexRewriter self)
        
        /**
         * Returns the Thread pointer of the currently-executing thread, as passed to
         * the constructor of this object.
         */
        """
        pass

    def getStartRow(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_start_row(GeomVertexRewriter self)
        
        /**
         * Returns the row index at which the rewriter started.  It will return to
         * this row if you reset the current column.
         */
        """
        pass

    def getStride(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_stride(GeomVertexRewriter self)
        
        /**
         * Returns the per-row stride (bytes between consecutive rows) of the
         * underlying vertex array.  This low-level information is normally not needed
         * to use the GeomVertexRewriter directly.
         */
        """
        pass

    def getVertexData(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_vertex_data(GeomVertexRewriter self)
        
        /**
         * Returns the vertex data object that the rewriter is processing.
         */
        """
        pass

    def get_array(self, GeomVertexRewriter_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_array(GeomVertexRewriter self)
        
        /**
         * Returns the array index containing the data type that the rewriter is
         * working on.
         */
        """
        pass

    def get_array_data(self, GeomVertexRewriter_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_array_data(GeomVertexRewriter self)
        
        /**
         * Returns the particular array object that the rewriter is currently
         * processing.
         */
        """
        pass

    def get_array_handle(self, GeomVertexRewriter_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_array_handle(GeomVertexRewriter self)
        
        /**
         * Returns the write handle to the array object that the rewriter is currently
         * processing.  This low-level call should be used with caution; be careful
         * with modifying the data in the handle out from under the
         * GeomVertexRewriter.
         */
        """
        pass

    def get_column(self, GeomVertexRewriter_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_column(GeomVertexRewriter self)
        
        /**
         * Returns the description of the data type that the rewriter is working on.
         */
        """
        pass

    def get_current_thread(self, GeomVertexRewriter_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_current_thread(GeomVertexRewriter self)
        
        /**
         * Returns the Thread pointer of the currently-executing thread, as passed to
         * the constructor of this object.
         */
        """
        pass

    def get_start_row(self, GeomVertexRewriter_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_start_row(GeomVertexRewriter self)
        
        /**
         * Returns the row index at which the rewriter started.  It will return to
         * this row if you reset the current column.
         */
        """
        pass

    def get_stride(self, GeomVertexRewriter_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_stride(GeomVertexRewriter self)
        
        /**
         * Returns the per-row stride (bytes between consecutive rows) of the
         * underlying vertex array.  This low-level information is normally not needed
         * to use the GeomVertexRewriter directly.
         */
        """
        pass

    def get_vertex_data(self, GeomVertexRewriter_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_vertex_data(GeomVertexRewriter self)
        
        /**
         * Returns the vertex data object that the rewriter is processing.
         */
        """
        pass

    def hasColumn(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_column(GeomVertexRewriter self)
        
        /**
         * Returns true if a valid data type has been successfully set, or false if
         * the data type does not exist.
         */
        """
        pass

    def has_column(self, GeomVertexRewriter_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_column(GeomVertexRewriter self)
        
        /**
         * Returns true if a valid data type has been successfully set, or false if
         * the data type does not exist.
         */
        """
        pass

    def isAtEnd(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_at_end(GeomVertexRewriter self)
        
        /**
         * Returns true if the reader or writer is currently at the end of the list of
         * vertices, false otherwise.
         */
        """
        pass

    def is_at_end(self, GeomVertexRewriter_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_at_end(GeomVertexRewriter self)
        
        /**
         * Returns true if the reader or writer is currently at the end of the list of
         * vertices, false otherwise.
         */
        """
        pass

    def output(self, GeomVertexRewriter_self, ostream_out): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        output(GeomVertexRewriter self, ostream out)
        
        /**
         *
         */
        """
        pass

    def setColumn(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_column(const GeomVertexRewriter self, const InternalName name)
        set_column(const GeomVertexRewriter self, int column)
        set_column(const GeomVertexRewriter self, int array, const GeomVertexColumn column)
        
        /**
         * Sets up the rewriter to use the nth data type of the GeomVertexFormat,
         * numbering from 0.
         *
         * This also resets both the read and write row numbers to the start row (the
         * same value passed to a previous call to set_row(), or 0 if set_row() was
         * never called.)
         *
         * The return value is true if the data type is valid, false otherwise.
         */
        
        /**
         * Sets up the rewriter to use the data type with the indicated name.
         *
         * This also resets both the read and write row numbers to the start row (the
         * same value passed to a previous call to set_row(), or 0 if set_row() was
         * never called.)
         *
         * The return value is true if the data type is valid, false otherwise.
         */
        
        /**
         * Sets up the rewriter to use the indicated column description on the given
         * array.
         *
         * This also resets both the read and write row numbers to the start row (the
         * same value passed to a previous call to set_row(), or 0 if set_row() was
         * never called.)
         *
         * The return value is true if the data type is valid, false otherwise.
         */
        """
        pass

    def setRow(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_row(const GeomVertexRewriter self, int row)
        
        /**
         * Sets the start, write, and write index to the indicated value.  The
         * rewriter will begin traversing from the given row.
         */
        """
        pass

    def setRowUnsafe(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_row_unsafe(const GeomVertexRewriter self, int row)
        
        /**
         * Sets the start row to the indicated value, without internal checks.  This
         * is the same as set_row(), but it does not check for the possibility that
         * the array has been reallocated internally for some reason; use only when
         * you are confident that the array is unchanged and you really need every bit
         * of available performance.
         */
        """
        pass

    def set_column(self, const_GeomVertexRewriter_self, const_InternalName_name): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_column(const GeomVertexRewriter self, const InternalName name)
        set_column(const GeomVertexRewriter self, int column)
        set_column(const GeomVertexRewriter self, int array, const GeomVertexColumn column)
        
        /**
         * Sets up the rewriter to use the nth data type of the GeomVertexFormat,
         * numbering from 0.
         *
         * This also resets both the read and write row numbers to the start row (the
         * same value passed to a previous call to set_row(), or 0 if set_row() was
         * never called.)
         *
         * The return value is true if the data type is valid, false otherwise.
         */
        
        /**
         * Sets up the rewriter to use the data type with the indicated name.
         *
         * This also resets both the read and write row numbers to the start row (the
         * same value passed to a previous call to set_row(), or 0 if set_row() was
         * never called.)
         *
         * The return value is true if the data type is valid, false otherwise.
         */
        
        /**
         * Sets up the rewriter to use the indicated column description on the given
         * array.
         *
         * This also resets both the read and write row numbers to the start row (the
         * same value passed to a previous call to set_row(), or 0 if set_row() was
         * never called.)
         *
         * The return value is true if the data type is valid, false otherwise.
         */
        """
        pass

    def set_row(self, const_GeomVertexRewriter_self, int_row): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_row(const GeomVertexRewriter self, int row)
        
        /**
         * Sets the start, write, and write index to the indicated value.  The
         * rewriter will begin traversing from the given row.
         */
        """
        pass

    def set_row_unsafe(self, const_GeomVertexRewriter_self, int_row): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_row_unsafe(const GeomVertexRewriter self, int row)
        
        /**
         * Sets the start row to the indicated value, without internal checks.  This
         * is the same as set_row(), but it does not check for the possibility that
         * the array has been reallocated internally for some reason; use only when
         * you are confident that the array is unchanged and you really need every bit
         * of available performance.
         */
        """
        pass

    def upcastToGeomVertexReader(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        upcast_to_GeomVertexReader(const GeomVertexRewriter self)
        
        upcast from GeomVertexRewriter to GeomVertexReader
        """
        pass

    def upcastToGeomVertexWriter(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        upcast_to_GeomVertexWriter(const GeomVertexRewriter self)
        
        upcast from GeomVertexRewriter to GeomVertexWriter
        """
        pass

    def upcast_to_GeomVertexReader(self, const_GeomVertexRewriter_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        upcast_to_GeomVertexReader(const GeomVertexRewriter self)
        
        upcast from GeomVertexRewriter to GeomVertexReader
        """
        pass

    def upcast_to_GeomVertexWriter(self, const_GeomVertexRewriter_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        upcast_to_GeomVertexWriter(const GeomVertexRewriter self)
        
        upcast from GeomVertexRewriter to GeomVertexWriter
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
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.core.GeomVertexRewriter' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.core.GeomVertexRewriter' objects>"
        '__doc__': "/**\n * This object provides the functionality of both a GeomVertexReader and a\n * GeomVertexWriter, combined together into one convenient package.  It is\n * designed for making a single pass over a GeomVertexData object, modifying\n * rows as it goes.\n *\n * Although it doesn't provide any real performance benefit over using a\n * separate reader and writer on the same data, it should probably be used in\n * preference to a separate reader and writer, because it makes an effort to\n * manage the reference counts properly between the reader and the writer to\n * avoid accidentally dereferencing either array while recopying.\n */",
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.GeomVertexRewriter' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE2FE9A0>'
        '__repr__': None, # (!) real value is "<slot wrapper '__repr__' of 'panda3d.core.GeomVertexRewriter' objects>"
        '__str__': None, # (!) real value is "<slot wrapper '__str__' of 'panda3d.core.GeomVertexRewriter' objects>"
        'assign': None, # (!) real value is "<method 'assign' of 'panda3d.core.GeomVertexRewriter' objects>"
        'clear': None, # (!) real value is "<method 'clear' of 'panda3d.core.GeomVertexRewriter' objects>"
        'getArray': None, # (!) real value is "<method 'getArray' of 'panda3d.core.GeomVertexRewriter' objects>"
        'getArrayData': None, # (!) real value is "<method 'getArrayData' of 'panda3d.core.GeomVertexRewriter' objects>"
        'getArrayHandle': None, # (!) real value is "<method 'getArrayHandle' of 'panda3d.core.GeomVertexRewriter' objects>"
        'getColumn': None, # (!) real value is "<method 'getColumn' of 'panda3d.core.GeomVertexRewriter' objects>"
        'getCurrentThread': None, # (!) real value is "<method 'getCurrentThread' of 'panda3d.core.GeomVertexRewriter' objects>"
        'getStartRow': None, # (!) real value is "<method 'getStartRow' of 'panda3d.core.GeomVertexRewriter' objects>"
        'getStride': None, # (!) real value is "<method 'getStride' of 'panda3d.core.GeomVertexRewriter' objects>"
        'getVertexData': None, # (!) real value is "<method 'getVertexData' of 'panda3d.core.GeomVertexRewriter' objects>"
        'get_array': None, # (!) real value is "<method 'get_array' of 'panda3d.core.GeomVertexRewriter' objects>"
        'get_array_data': None, # (!) real value is "<method 'get_array_data' of 'panda3d.core.GeomVertexRewriter' objects>"
        'get_array_handle': None, # (!) real value is "<method 'get_array_handle' of 'panda3d.core.GeomVertexRewriter' objects>"
        'get_column': None, # (!) real value is "<method 'get_column' of 'panda3d.core.GeomVertexRewriter' objects>"
        'get_current_thread': None, # (!) real value is "<method 'get_current_thread' of 'panda3d.core.GeomVertexRewriter' objects>"
        'get_start_row': None, # (!) real value is "<method 'get_start_row' of 'panda3d.core.GeomVertexRewriter' objects>"
        'get_stride': None, # (!) real value is "<method 'get_stride' of 'panda3d.core.GeomVertexRewriter' objects>"
        'get_vertex_data': None, # (!) real value is "<method 'get_vertex_data' of 'panda3d.core.GeomVertexRewriter' objects>"
        'hasColumn': None, # (!) real value is "<method 'hasColumn' of 'panda3d.core.GeomVertexRewriter' objects>"
        'has_column': None, # (!) real value is "<method 'has_column' of 'panda3d.core.GeomVertexRewriter' objects>"
        'isAtEnd': None, # (!) real value is "<method 'isAtEnd' of 'panda3d.core.GeomVertexRewriter' objects>"
        'is_at_end': None, # (!) real value is "<method 'is_at_end' of 'panda3d.core.GeomVertexRewriter' objects>"
        'output': None, # (!) real value is "<method 'output' of 'panda3d.core.GeomVertexRewriter' objects>"
        'setColumn': None, # (!) real value is "<method 'setColumn' of 'panda3d.core.GeomVertexRewriter' objects>"
        'setRow': None, # (!) real value is "<method 'setRow' of 'panda3d.core.GeomVertexRewriter' objects>"
        'setRowUnsafe': None, # (!) real value is "<method 'setRowUnsafe' of 'panda3d.core.GeomVertexRewriter' objects>"
        'set_column': None, # (!) real value is "<method 'set_column' of 'panda3d.core.GeomVertexRewriter' objects>"
        'set_row': None, # (!) real value is "<method 'set_row' of 'panda3d.core.GeomVertexRewriter' objects>"
        'set_row_unsafe': None, # (!) real value is "<method 'set_row_unsafe' of 'panda3d.core.GeomVertexRewriter' objects>"
        'upcastToGeomVertexReader': None, # (!) real value is "<method 'upcastToGeomVertexReader' of 'panda3d.core.GeomVertexRewriter' objects>"
        'upcastToGeomVertexWriter': None, # (!) real value is "<method 'upcastToGeomVertexWriter' of 'panda3d.core.GeomVertexRewriter' objects>"
        'upcast_to_GeomVertexReader': None, # (!) real value is "<method 'upcast_to_GeomVertexReader' of 'panda3d.core.GeomVertexRewriter' objects>"
        'upcast_to_GeomVertexWriter': None, # (!) real value is "<method 'upcast_to_GeomVertexWriter' of 'panda3d.core.GeomVertexRewriter' objects>"
    }


