# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .GeomEnums import GeomEnums

class GeomVertexReader(GeomEnums):
    """
    /**
     * This object provides a high-level interface for quickly reading a sequence
     * of numeric values from a vertex table.
     *
     * It is particularly optimized for reading a single column of data values for
     * a series of vertices, without changing columns between each number.
     * Although you can also use one GeomVertexReader to read across the columns
     * if it is convenient, by calling set_column() repeatedly at each vertex, it
     * is faster to read down the columns, and to use a different GeomVertexReader
     * for each column.
     *
     * Note that a GeomVertexReader does not keep a reference count to the actual
     * vertex data buffer (it grabs the current data buffer from the
     * GeomVertexData whenever set_column() is called).  This means that it is
     * important not to keep a GeomVertexReader object around over a long period
     * of time in which the data buffer is likely to be deallocated; it is
     * intended for making a quick pass over the data in one session.
     *
     * It also means that you should create any GeomVertexWriters *before*
     * creating GeomVertexReaders on the same data, since the writer itself might
     * cause the vertex buffer to be deallocated.  Better yet, use a
     * GeomVertexRewriter if you are going to create both of them anyway.
     */
    """
    def assign(self, const_GeomVertexReader_self, const_GeomVertexReader_copy): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        assign(const GeomVertexReader self, const GeomVertexReader copy)
        """
        pass

    def clear(self, const_GeomVertexReader_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear(const GeomVertexReader self)
        
        /**
         * Resets the GeomVertexReader to the initial state.
         */
        """
        pass

    def getArray(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_array(GeomVertexReader self)
        
        /**
         * Returns the array index containing the data type that the reader is working
         * on.
         */
        """
        pass

    def getArrayData(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_array_data(GeomVertexReader self)
        
        /**
         * Returns the particular array object that the reader is currently
         * processing.
         */
        """
        pass

    def getArrayHandle(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_array_handle(GeomVertexReader self)
        
        /**
         * Returns the read handle to the array object that the read is currently
         * processing.  This low-level call should be used with caution.
         */
        """
        pass

    def getColumn(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_column(GeomVertexReader self)
        
        /**
         * Returns the description of the data type that the reader is working on.
         */
        """
        pass

    def getCurrentThread(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_current_thread(GeomVertexReader self)
        
        /**
         * Returns the Thread pointer of the currently-executing thread, as passed to
         * the constructor of this object.
         */
        """
        pass

    def getData1(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_data1(const GeomVertexReader self)
        
        /**
         * Returns the data associated with the read row, expressed as a 1-component
         * value, and advances the read row.
         */
        """
        pass

    def getData1d(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_data1d(const GeomVertexReader self)
        
        /**
         * Returns the data associated with the read row, expressed as a 1-component
         * value, and advances the read row.
         */
        """
        pass

    def getData1f(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_data1f(const GeomVertexReader self)
        
        /**
         * Returns the data associated with the read row, expressed as a 1-component
         * value, and advances the read row.
         */
        """
        pass

    def getData1i(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_data1i(const GeomVertexReader self)
        
        /**
         * Returns the data associated with the read row, expressed as a 1-component
         * value, and advances the read row.
         */
        """
        pass

    def getData2(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_data2(const GeomVertexReader self)
        
        /**
         * Returns the data associated with the read row, expressed as a 2-component
         * value, and advances the read row.
         */
        """
        pass

    def getData2d(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_data2d(const GeomVertexReader self)
        
        /**
         * Returns the data associated with the read row, expressed as a 2-component
         * value, and advances the read row.
         */
        """
        pass

    def getData2f(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_data2f(const GeomVertexReader self)
        
        /**
         * Returns the data associated with the read row, expressed as a 2-component
         * value, and advances the read row.
         */
        """
        pass

    def getData2i(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_data2i(const GeomVertexReader self)
        
        /**
         * Returns the data associated with the read row, expressed as a 2-component
         * value, and advances the read row.
         */
        """
        pass

    def getData3(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_data3(const GeomVertexReader self)
        
        /**
         * Returns the data associated with the read row, expressed as a 3-component
         * value, and advances the read row.
         */
        """
        pass

    def getData3d(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_data3d(const GeomVertexReader self)
        
        /**
         * Returns the data associated with the read row, expressed as a 3-component
         * value, and advances the read row.
         */
        """
        pass

    def getData3f(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_data3f(const GeomVertexReader self)
        
        /**
         * Returns the data associated with the read row, expressed as a 3-component
         * value, and advances the read row.
         */
        """
        pass

    def getData3i(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_data3i(const GeomVertexReader self)
        
        /**
         * Returns the data associated with the read row, expressed as a 3-component
         * value, and advances the read row.
         */
        """
        pass

    def getData4(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_data4(const GeomVertexReader self)
        
        /**
         * Returns the data associated with the read row, expressed as a 4-component
         * value, and advances the read row.
         */
        """
        pass

    def getData4d(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_data4d(const GeomVertexReader self)
        
        /**
         * Returns the data associated with the read row, expressed as a 4-component
         * value, and advances the read row.
         */
        """
        pass

    def getData4f(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_data4f(const GeomVertexReader self)
        
        /**
         * Returns the data associated with the read row, expressed as a 4-component
         * value, and advances the read row.
         */
        """
        pass

    def getData4i(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_data4i(const GeomVertexReader self)
        
        /**
         * Returns the data associated with the read row, expressed as a 4-component
         * value, and advances the read row.
         */
        """
        pass

    def getForce(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_force(GeomVertexReader self)
        
        /**
         * Returns the value of the force flag.  See set_force().
         */
        """
        pass

    def getMatrix3(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_matrix3(const GeomVertexReader self)
        
        /**
         * Returns the 3-by-3 matrix associated with the read row and advances the
         * read row.  This is a special method that only works when the column in
         * question contains a matrix of an appropriate size.
         */
        """
        pass

    def getMatrix3d(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_matrix3d(const GeomVertexReader self)
        
        /**
         * Returns the 3-by-3 matrix associated with the read row and advances the
         * read row.  This is a special method that only works when the column in
         * question contains a matrix of an appropriate size.
         */
        """
        pass

    def getMatrix3f(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_matrix3f(const GeomVertexReader self)
        
        /**
         * Returns the 3-by-3 matrix associated with the read row and advances the
         * read row.  This is a special method that only works when the column in
         * question contains a matrix of an appropriate size.
         */
        """
        pass

    def getMatrix4(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_matrix4(const GeomVertexReader self)
        
        /**
         * Returns the 4-by-4 matrix associated with the read row and advances the
         * read row.  This is a special method that only works when the column in
         * question contains a matrix of an appropriate size.
         */
        """
        pass

    def getMatrix4d(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_matrix4d(const GeomVertexReader self)
        
        /**
         * Returns the 4-by-4 matrix associated with the read row and advances the
         * read row.  This is a special method that only works when the column in
         * question contains a matrix of an appropriate size.
         */
        """
        pass

    def getMatrix4f(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_matrix4f(const GeomVertexReader self)
        
        /**
         * Returns the 4-by-4 matrix associated with the read row and advances the
         * read row.  This is a special method that only works when the column in
         * question contains a matrix of an appropriate size.
         */
        """
        pass

    def getReadRow(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_read_row(GeomVertexReader self)
        
        /**
         * Returns the row index from which the data will be retrieved by the next
         * call to get_data*().
         */
        """
        pass

    def getStartRow(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_start_row(GeomVertexReader self)
        
        /**
         * Returns the row index at which the reader started.  It will return to this
         * row if you reset the current column.
         */
        """
        pass

    def getStride(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_stride(GeomVertexReader self)
        
        /**
         * Returns the per-row stride (bytes between consecutive rows) of the
         * underlying vertex array.  This low-level information is normally not needed
         * to use the GeomVertexReader directly.
         */
        """
        pass

    def getVertexData(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_vertex_data(GeomVertexReader self)
        
        /**
         * Returns the vertex data object that the reader is processing.  This may
         * return NULL if the reader was constructed with just an array pointer.
         */
        """
        pass

    def get_array(self, GeomVertexReader_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_array(GeomVertexReader self)
        
        /**
         * Returns the array index containing the data type that the reader is working
         * on.
         */
        """
        pass

    def get_array_data(self, GeomVertexReader_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_array_data(GeomVertexReader self)
        
        /**
         * Returns the particular array object that the reader is currently
         * processing.
         */
        """
        pass

    def get_array_handle(self, GeomVertexReader_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_array_handle(GeomVertexReader self)
        
        /**
         * Returns the read handle to the array object that the read is currently
         * processing.  This low-level call should be used with caution.
         */
        """
        pass

    def get_column(self, GeomVertexReader_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_column(GeomVertexReader self)
        
        /**
         * Returns the description of the data type that the reader is working on.
         */
        """
        pass

    def get_current_thread(self, GeomVertexReader_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_current_thread(GeomVertexReader self)
        
        /**
         * Returns the Thread pointer of the currently-executing thread, as passed to
         * the constructor of this object.
         */
        """
        pass

    def get_data1(self, const_GeomVertexReader_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_data1(const GeomVertexReader self)
        
        /**
         * Returns the data associated with the read row, expressed as a 1-component
         * value, and advances the read row.
         */
        """
        pass

    def get_data1d(self, const_GeomVertexReader_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_data1d(const GeomVertexReader self)
        
        /**
         * Returns the data associated with the read row, expressed as a 1-component
         * value, and advances the read row.
         */
        """
        pass

    def get_data1f(self, const_GeomVertexReader_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_data1f(const GeomVertexReader self)
        
        /**
         * Returns the data associated with the read row, expressed as a 1-component
         * value, and advances the read row.
         */
        """
        pass

    def get_data1i(self, const_GeomVertexReader_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_data1i(const GeomVertexReader self)
        
        /**
         * Returns the data associated with the read row, expressed as a 1-component
         * value, and advances the read row.
         */
        """
        pass

    def get_data2(self, const_GeomVertexReader_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_data2(const GeomVertexReader self)
        
        /**
         * Returns the data associated with the read row, expressed as a 2-component
         * value, and advances the read row.
         */
        """
        pass

    def get_data2d(self, const_GeomVertexReader_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_data2d(const GeomVertexReader self)
        
        /**
         * Returns the data associated with the read row, expressed as a 2-component
         * value, and advances the read row.
         */
        """
        pass

    def get_data2f(self, const_GeomVertexReader_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_data2f(const GeomVertexReader self)
        
        /**
         * Returns the data associated with the read row, expressed as a 2-component
         * value, and advances the read row.
         */
        """
        pass

    def get_data2i(self, const_GeomVertexReader_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_data2i(const GeomVertexReader self)
        
        /**
         * Returns the data associated with the read row, expressed as a 2-component
         * value, and advances the read row.
         */
        """
        pass

    def get_data3(self, const_GeomVertexReader_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_data3(const GeomVertexReader self)
        
        /**
         * Returns the data associated with the read row, expressed as a 3-component
         * value, and advances the read row.
         */
        """
        pass

    def get_data3d(self, const_GeomVertexReader_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_data3d(const GeomVertexReader self)
        
        /**
         * Returns the data associated with the read row, expressed as a 3-component
         * value, and advances the read row.
         */
        """
        pass

    def get_data3f(self, const_GeomVertexReader_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_data3f(const GeomVertexReader self)
        
        /**
         * Returns the data associated with the read row, expressed as a 3-component
         * value, and advances the read row.
         */
        """
        pass

    def get_data3i(self, const_GeomVertexReader_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_data3i(const GeomVertexReader self)
        
        /**
         * Returns the data associated with the read row, expressed as a 3-component
         * value, and advances the read row.
         */
        """
        pass

    def get_data4(self, const_GeomVertexReader_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_data4(const GeomVertexReader self)
        
        /**
         * Returns the data associated with the read row, expressed as a 4-component
         * value, and advances the read row.
         */
        """
        pass

    def get_data4d(self, const_GeomVertexReader_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_data4d(const GeomVertexReader self)
        
        /**
         * Returns the data associated with the read row, expressed as a 4-component
         * value, and advances the read row.
         */
        """
        pass

    def get_data4f(self, const_GeomVertexReader_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_data4f(const GeomVertexReader self)
        
        /**
         * Returns the data associated with the read row, expressed as a 4-component
         * value, and advances the read row.
         */
        """
        pass

    def get_data4i(self, const_GeomVertexReader_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_data4i(const GeomVertexReader self)
        
        /**
         * Returns the data associated with the read row, expressed as a 4-component
         * value, and advances the read row.
         */
        """
        pass

    def get_force(self, GeomVertexReader_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_force(GeomVertexReader self)
        
        /**
         * Returns the value of the force flag.  See set_force().
         */
        """
        pass

    def get_matrix3(self, const_GeomVertexReader_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_matrix3(const GeomVertexReader self)
        
        /**
         * Returns the 3-by-3 matrix associated with the read row and advances the
         * read row.  This is a special method that only works when the column in
         * question contains a matrix of an appropriate size.
         */
        """
        pass

    def get_matrix3d(self, const_GeomVertexReader_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_matrix3d(const GeomVertexReader self)
        
        /**
         * Returns the 3-by-3 matrix associated with the read row and advances the
         * read row.  This is a special method that only works when the column in
         * question contains a matrix of an appropriate size.
         */
        """
        pass

    def get_matrix3f(self, const_GeomVertexReader_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_matrix3f(const GeomVertexReader self)
        
        /**
         * Returns the 3-by-3 matrix associated with the read row and advances the
         * read row.  This is a special method that only works when the column in
         * question contains a matrix of an appropriate size.
         */
        """
        pass

    def get_matrix4(self, const_GeomVertexReader_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_matrix4(const GeomVertexReader self)
        
        /**
         * Returns the 4-by-4 matrix associated with the read row and advances the
         * read row.  This is a special method that only works when the column in
         * question contains a matrix of an appropriate size.
         */
        """
        pass

    def get_matrix4d(self, const_GeomVertexReader_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_matrix4d(const GeomVertexReader self)
        
        /**
         * Returns the 4-by-4 matrix associated with the read row and advances the
         * read row.  This is a special method that only works when the column in
         * question contains a matrix of an appropriate size.
         */
        """
        pass

    def get_matrix4f(self, const_GeomVertexReader_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_matrix4f(const GeomVertexReader self)
        
        /**
         * Returns the 4-by-4 matrix associated with the read row and advances the
         * read row.  This is a special method that only works when the column in
         * question contains a matrix of an appropriate size.
         */
        """
        pass

    def get_read_row(self, GeomVertexReader_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_read_row(GeomVertexReader self)
        
        /**
         * Returns the row index from which the data will be retrieved by the next
         * call to get_data*().
         */
        """
        pass

    def get_start_row(self, GeomVertexReader_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_start_row(GeomVertexReader self)
        
        /**
         * Returns the row index at which the reader started.  It will return to this
         * row if you reset the current column.
         */
        """
        pass

    def get_stride(self, GeomVertexReader_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_stride(GeomVertexReader self)
        
        /**
         * Returns the per-row stride (bytes between consecutive rows) of the
         * underlying vertex array.  This low-level information is normally not needed
         * to use the GeomVertexReader directly.
         */
        """
        pass

    def get_vertex_data(self, GeomVertexReader_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_vertex_data(GeomVertexReader self)
        
        /**
         * Returns the vertex data object that the reader is processing.  This may
         * return NULL if the reader was constructed with just an array pointer.
         */
        """
        pass

    def hasColumn(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_column(GeomVertexReader self)
        
        /**
         * Returns true if a valid data type has been successfully set, or false if
         * the data type does not exist (or if get_force() is false and the vertex
         * data is nonresident).
         */
        """
        pass

    def has_column(self, GeomVertexReader_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_column(GeomVertexReader self)
        
        /**
         * Returns true if a valid data type has been successfully set, or false if
         * the data type does not exist (or if get_force() is false and the vertex
         * data is nonresident).
         */
        """
        pass

    def isAtEnd(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_at_end(GeomVertexReader self)
        
        /**
         * Returns true if the reader is currently at the end of the list of vertices,
         * false otherwise.  If this is true, another call to get_data*() will result
         * in a crash.
         */
        """
        pass

    def is_at_end(self, GeomVertexReader_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_at_end(GeomVertexReader self)
        
        /**
         * Returns true if the reader is currently at the end of the list of vertices,
         * false otherwise.  If this is true, another call to get_data*() will result
         * in a crash.
         */
        """
        pass

    def output(self, GeomVertexReader_self, ostream_out): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        output(GeomVertexReader self, ostream out)
        
        /**
         *
         */
        """
        pass

    def setColumn(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_column(const GeomVertexReader self, const InternalName name)
        set_column(const GeomVertexReader self, int column)
        set_column(const GeomVertexReader self, int array, const GeomVertexColumn column)
        
        /**
         * Sets up the reader to use the nth data type of the GeomVertexFormat,
         * numbering from 0.
         *
         * This also resets the read row number to the start row (the same value
         * passed to a previous call to set_row(), or 0 if set_row() was never
         * called.)
         *
         * The return value is true if the data type is valid, false otherwise.
         */
        
        /**
         * Sets up the reader to use the data type with the indicated name.
         *
         * This also resets the read row number to the start row (the same value
         * passed to a previous call to set_row(), or 0 if set_row() was never
         * called.)
         *
         * The return value is true if the data type is valid, false otherwise.
         */
        
        /**
         * Sets up the reader to use the indicated column description on the given
         * array.
         *
         * This also resets the current read row number to the start row (the same
         * value passed to a previous call to set_row(), or 0 if set_row() was never
         * called.)
         *
         * The return value is true if the data type is valid, false otherwise.
         */
        """
        pass

    def setForce(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_force(const GeomVertexReader self, bool force)
        
        /**
         * Sets the value of the force flag.  When this is true (the default), vertex
         * data will be paged in from disk if necessary.  When this is false, the
         * GeomVertexData will simply return a failure code when attempting to read
         * vertex data that is not resident (but will put it on the queue to become
         * resident later).
         *
         * Normally, vertex data is always resident, so this will not be an issue.  It
         * is only possible for vertex data to be nonresident if you have enabled
         * vertex paging via the GeomVertexArrayData and VertexDataPage interfaces.
         */
        """
        pass

    def setRow(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_row(const GeomVertexReader self, int row)
        
        /**
         * Sets the start row to the indicated value.  The reader will begin reading
         * from the indicated row; each subsequent get_data*() call will return the
         * data from the subsequent row.  If set_column() is called, the reader will
         * return to this row.
         */
        """
        pass

    def setRowUnsafe(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_row_unsafe(const GeomVertexReader self, int row)
        
        /**
         * Sets the start row to the indicated value, without internal checks.  This
         * is the same as set_row(), but it does not check for the possibility that
         * the array has been reallocated internally for some reason; use only when
         * you are confident that the array is unchanged and you really need every bit
         * of available performance.
         */
        """
        pass

    def set_column(self, const_GeomVertexReader_self, const_InternalName_name): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_column(const GeomVertexReader self, const InternalName name)
        set_column(const GeomVertexReader self, int column)
        set_column(const GeomVertexReader self, int array, const GeomVertexColumn column)
        
        /**
         * Sets up the reader to use the nth data type of the GeomVertexFormat,
         * numbering from 0.
         *
         * This also resets the read row number to the start row (the same value
         * passed to a previous call to set_row(), or 0 if set_row() was never
         * called.)
         *
         * The return value is true if the data type is valid, false otherwise.
         */
        
        /**
         * Sets up the reader to use the data type with the indicated name.
         *
         * This also resets the read row number to the start row (the same value
         * passed to a previous call to set_row(), or 0 if set_row() was never
         * called.)
         *
         * The return value is true if the data type is valid, false otherwise.
         */
        
        /**
         * Sets up the reader to use the indicated column description on the given
         * array.
         *
         * This also resets the current read row number to the start row (the same
         * value passed to a previous call to set_row(), or 0 if set_row() was never
         * called.)
         *
         * The return value is true if the data type is valid, false otherwise.
         */
        """
        pass

    def set_force(self, const_GeomVertexReader_self, bool_force): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_force(const GeomVertexReader self, bool force)
        
        /**
         * Sets the value of the force flag.  When this is true (the default), vertex
         * data will be paged in from disk if necessary.  When this is false, the
         * GeomVertexData will simply return a failure code when attempting to read
         * vertex data that is not resident (but will put it on the queue to become
         * resident later).
         *
         * Normally, vertex data is always resident, so this will not be an issue.  It
         * is only possible for vertex data to be nonresident if you have enabled
         * vertex paging via the GeomVertexArrayData and VertexDataPage interfaces.
         */
        """
        pass

    def set_row(self, const_GeomVertexReader_self, int_row): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_row(const GeomVertexReader self, int row)
        
        /**
         * Sets the start row to the indicated value.  The reader will begin reading
         * from the indicated row; each subsequent get_data*() call will return the
         * data from the subsequent row.  If set_column() is called, the reader will
         * return to this row.
         */
        """
        pass

    def set_row_unsafe(self, const_GeomVertexReader_self, int_row): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_row_unsafe(const GeomVertexReader self, int row)
        
        /**
         * Sets the start row to the indicated value, without internal checks.  This
         * is the same as set_row(), but it does not check for the possibility that
         * the array has been reallocated internally for some reason; use only when
         * you are confident that the array is unchanged and you really need every bit
         * of available performance.
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
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.core.GeomVertexReader' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.core.GeomVertexReader' objects>"
        '__doc__': '/**\n * This object provides a high-level interface for quickly reading a sequence\n * of numeric values from a vertex table.\n *\n * It is particularly optimized for reading a single column of data values for\n * a series of vertices, without changing columns between each number.\n * Although you can also use one GeomVertexReader to read across the columns\n * if it is convenient, by calling set_column() repeatedly at each vertex, it\n * is faster to read down the columns, and to use a different GeomVertexReader\n * for each column.\n *\n * Note that a GeomVertexReader does not keep a reference count to the actual\n * vertex data buffer (it grabs the current data buffer from the\n * GeomVertexData whenever set_column() is called).  This means that it is\n * important not to keep a GeomVertexReader object around over a long period\n * of time in which the data buffer is likely to be deallocated; it is\n * intended for making a quick pass over the data in one session.\n *\n * It also means that you should create any GeomVertexWriters *before*\n * creating GeomVertexReaders on the same data, since the writer itself might\n * cause the vertex buffer to be deallocated.  Better yet, use a\n * GeomVertexRewriter if you are going to create both of them anyway.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.GeomVertexReader' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE2FE600>'
        '__repr__': None, # (!) real value is "<slot wrapper '__repr__' of 'panda3d.core.GeomVertexReader' objects>"
        '__str__': None, # (!) real value is "<slot wrapper '__str__' of 'panda3d.core.GeomVertexReader' objects>"
        'assign': None, # (!) real value is "<method 'assign' of 'panda3d.core.GeomVertexReader' objects>"
        'clear': None, # (!) real value is "<method 'clear' of 'panda3d.core.GeomVertexReader' objects>"
        'getArray': None, # (!) real value is "<method 'getArray' of 'panda3d.core.GeomVertexReader' objects>"
        'getArrayData': None, # (!) real value is "<method 'getArrayData' of 'panda3d.core.GeomVertexReader' objects>"
        'getArrayHandle': None, # (!) real value is "<method 'getArrayHandle' of 'panda3d.core.GeomVertexReader' objects>"
        'getColumn': None, # (!) real value is "<method 'getColumn' of 'panda3d.core.GeomVertexReader' objects>"
        'getCurrentThread': None, # (!) real value is "<method 'getCurrentThread' of 'panda3d.core.GeomVertexReader' objects>"
        'getData1': None, # (!) real value is "<method 'getData1' of 'panda3d.core.GeomVertexReader' objects>"
        'getData1d': None, # (!) real value is "<method 'getData1d' of 'panda3d.core.GeomVertexReader' objects>"
        'getData1f': None, # (!) real value is "<method 'getData1f' of 'panda3d.core.GeomVertexReader' objects>"
        'getData1i': None, # (!) real value is "<method 'getData1i' of 'panda3d.core.GeomVertexReader' objects>"
        'getData2': None, # (!) real value is "<method 'getData2' of 'panda3d.core.GeomVertexReader' objects>"
        'getData2d': None, # (!) real value is "<method 'getData2d' of 'panda3d.core.GeomVertexReader' objects>"
        'getData2f': None, # (!) real value is "<method 'getData2f' of 'panda3d.core.GeomVertexReader' objects>"
        'getData2i': None, # (!) real value is "<method 'getData2i' of 'panda3d.core.GeomVertexReader' objects>"
        'getData3': None, # (!) real value is "<method 'getData3' of 'panda3d.core.GeomVertexReader' objects>"
        'getData3d': None, # (!) real value is "<method 'getData3d' of 'panda3d.core.GeomVertexReader' objects>"
        'getData3f': None, # (!) real value is "<method 'getData3f' of 'panda3d.core.GeomVertexReader' objects>"
        'getData3i': None, # (!) real value is "<method 'getData3i' of 'panda3d.core.GeomVertexReader' objects>"
        'getData4': None, # (!) real value is "<method 'getData4' of 'panda3d.core.GeomVertexReader' objects>"
        'getData4d': None, # (!) real value is "<method 'getData4d' of 'panda3d.core.GeomVertexReader' objects>"
        'getData4f': None, # (!) real value is "<method 'getData4f' of 'panda3d.core.GeomVertexReader' objects>"
        'getData4i': None, # (!) real value is "<method 'getData4i' of 'panda3d.core.GeomVertexReader' objects>"
        'getForce': None, # (!) real value is "<method 'getForce' of 'panda3d.core.GeomVertexReader' objects>"
        'getMatrix3': None, # (!) real value is "<method 'getMatrix3' of 'panda3d.core.GeomVertexReader' objects>"
        'getMatrix3d': None, # (!) real value is "<method 'getMatrix3d' of 'panda3d.core.GeomVertexReader' objects>"
        'getMatrix3f': None, # (!) real value is "<method 'getMatrix3f' of 'panda3d.core.GeomVertexReader' objects>"
        'getMatrix4': None, # (!) real value is "<method 'getMatrix4' of 'panda3d.core.GeomVertexReader' objects>"
        'getMatrix4d': None, # (!) real value is "<method 'getMatrix4d' of 'panda3d.core.GeomVertexReader' objects>"
        'getMatrix4f': None, # (!) real value is "<method 'getMatrix4f' of 'panda3d.core.GeomVertexReader' objects>"
        'getReadRow': None, # (!) real value is "<method 'getReadRow' of 'panda3d.core.GeomVertexReader' objects>"
        'getStartRow': None, # (!) real value is "<method 'getStartRow' of 'panda3d.core.GeomVertexReader' objects>"
        'getStride': None, # (!) real value is "<method 'getStride' of 'panda3d.core.GeomVertexReader' objects>"
        'getVertexData': None, # (!) real value is "<method 'getVertexData' of 'panda3d.core.GeomVertexReader' objects>"
        'get_array': None, # (!) real value is "<method 'get_array' of 'panda3d.core.GeomVertexReader' objects>"
        'get_array_data': None, # (!) real value is "<method 'get_array_data' of 'panda3d.core.GeomVertexReader' objects>"
        'get_array_handle': None, # (!) real value is "<method 'get_array_handle' of 'panda3d.core.GeomVertexReader' objects>"
        'get_column': None, # (!) real value is "<method 'get_column' of 'panda3d.core.GeomVertexReader' objects>"
        'get_current_thread': None, # (!) real value is "<method 'get_current_thread' of 'panda3d.core.GeomVertexReader' objects>"
        'get_data1': None, # (!) real value is "<method 'get_data1' of 'panda3d.core.GeomVertexReader' objects>"
        'get_data1d': None, # (!) real value is "<method 'get_data1d' of 'panda3d.core.GeomVertexReader' objects>"
        'get_data1f': None, # (!) real value is "<method 'get_data1f' of 'panda3d.core.GeomVertexReader' objects>"
        'get_data1i': None, # (!) real value is "<method 'get_data1i' of 'panda3d.core.GeomVertexReader' objects>"
        'get_data2': None, # (!) real value is "<method 'get_data2' of 'panda3d.core.GeomVertexReader' objects>"
        'get_data2d': None, # (!) real value is "<method 'get_data2d' of 'panda3d.core.GeomVertexReader' objects>"
        'get_data2f': None, # (!) real value is "<method 'get_data2f' of 'panda3d.core.GeomVertexReader' objects>"
        'get_data2i': None, # (!) real value is "<method 'get_data2i' of 'panda3d.core.GeomVertexReader' objects>"
        'get_data3': None, # (!) real value is "<method 'get_data3' of 'panda3d.core.GeomVertexReader' objects>"
        'get_data3d': None, # (!) real value is "<method 'get_data3d' of 'panda3d.core.GeomVertexReader' objects>"
        'get_data3f': None, # (!) real value is "<method 'get_data3f' of 'panda3d.core.GeomVertexReader' objects>"
        'get_data3i': None, # (!) real value is "<method 'get_data3i' of 'panda3d.core.GeomVertexReader' objects>"
        'get_data4': None, # (!) real value is "<method 'get_data4' of 'panda3d.core.GeomVertexReader' objects>"
        'get_data4d': None, # (!) real value is "<method 'get_data4d' of 'panda3d.core.GeomVertexReader' objects>"
        'get_data4f': None, # (!) real value is "<method 'get_data4f' of 'panda3d.core.GeomVertexReader' objects>"
        'get_data4i': None, # (!) real value is "<method 'get_data4i' of 'panda3d.core.GeomVertexReader' objects>"
        'get_force': None, # (!) real value is "<method 'get_force' of 'panda3d.core.GeomVertexReader' objects>"
        'get_matrix3': None, # (!) real value is "<method 'get_matrix3' of 'panda3d.core.GeomVertexReader' objects>"
        'get_matrix3d': None, # (!) real value is "<method 'get_matrix3d' of 'panda3d.core.GeomVertexReader' objects>"
        'get_matrix3f': None, # (!) real value is "<method 'get_matrix3f' of 'panda3d.core.GeomVertexReader' objects>"
        'get_matrix4': None, # (!) real value is "<method 'get_matrix4' of 'panda3d.core.GeomVertexReader' objects>"
        'get_matrix4d': None, # (!) real value is "<method 'get_matrix4d' of 'panda3d.core.GeomVertexReader' objects>"
        'get_matrix4f': None, # (!) real value is "<method 'get_matrix4f' of 'panda3d.core.GeomVertexReader' objects>"
        'get_read_row': None, # (!) real value is "<method 'get_read_row' of 'panda3d.core.GeomVertexReader' objects>"
        'get_start_row': None, # (!) real value is "<method 'get_start_row' of 'panda3d.core.GeomVertexReader' objects>"
        'get_stride': None, # (!) real value is "<method 'get_stride' of 'panda3d.core.GeomVertexReader' objects>"
        'get_vertex_data': None, # (!) real value is "<method 'get_vertex_data' of 'panda3d.core.GeomVertexReader' objects>"
        'hasColumn': None, # (!) real value is "<method 'hasColumn' of 'panda3d.core.GeomVertexReader' objects>"
        'has_column': None, # (!) real value is "<method 'has_column' of 'panda3d.core.GeomVertexReader' objects>"
        'isAtEnd': None, # (!) real value is "<method 'isAtEnd' of 'panda3d.core.GeomVertexReader' objects>"
        'is_at_end': None, # (!) real value is "<method 'is_at_end' of 'panda3d.core.GeomVertexReader' objects>"
        'output': None, # (!) real value is "<method 'output' of 'panda3d.core.GeomVertexReader' objects>"
        'setColumn': None, # (!) real value is "<method 'setColumn' of 'panda3d.core.GeomVertexReader' objects>"
        'setForce': None, # (!) real value is "<method 'setForce' of 'panda3d.core.GeomVertexReader' objects>"
        'setRow': None, # (!) real value is "<method 'setRow' of 'panda3d.core.GeomVertexReader' objects>"
        'setRowUnsafe': None, # (!) real value is "<method 'setRowUnsafe' of 'panda3d.core.GeomVertexReader' objects>"
        'set_column': None, # (!) real value is "<method 'set_column' of 'panda3d.core.GeomVertexReader' objects>"
        'set_force': None, # (!) real value is "<method 'set_force' of 'panda3d.core.GeomVertexReader' objects>"
        'set_row': None, # (!) real value is "<method 'set_row' of 'panda3d.core.GeomVertexReader' objects>"
        'set_row_unsafe': None, # (!) real value is "<method 'set_row_unsafe' of 'panda3d.core.GeomVertexReader' objects>"
    }


