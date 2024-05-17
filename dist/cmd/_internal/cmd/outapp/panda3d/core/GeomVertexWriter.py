# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .GeomEnums import GeomEnums

class GeomVertexWriter(GeomEnums):
    """
    /**
     * This object provides a high-level interface for quickly writing a sequence
     * of numeric values from a vertex table.
     *
     * This object can be used both to replace existing vertices in the table, or
     * to extend the table with new vertices.  The set_data*() family of methods
     * can only be used to replace existing data; it is an error to allow these to
     * run past the end of the data.  The add_data*() family of methods, on the
     * other hand, can be used to replace existing data or add new data; if you
     * call set_row() into the middle of existing data the add_data*() methods
     * will behave like the corresponding set_data*(), but if they run past the
     * end of existing data they will quietly add new vertices.
     *
     * Like GeomVertexReader, the writer is particularly optimized for writing a
     * single column of data values for a series of vertices, without changing
     * columns between each number.  Although you can also use one
     * GeomVertexWriter to write across the columns if it is convenient, by
     * calling set_column() repeatedly at each vertex, it is faster to write down
     * the columns, and to use a different GeomVertexWriter for each column.
     *
     * Note that, like a GeomVertexReader, a GeomVertexWriter does not keep a
     * reference count to the actual vertex data buffer.  This means that it is
     * important not to keep a GeomVertexWriter object around over a long period
     * of time in which the data buffer is likely to be deallocated; it is
     * intended for making a quick pass over the data in one session.
     *
     * It also means that you should create any GeomVertexWriters *before*
     * creating GeomVertexReaders on the same data, since the writer itself might
     * cause the vertex buffer to be deallocated.  Better yet, use a
     * GeomVertexRewriter if you are going to create both of them anyway.
     */
    """
    def addData1(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_data1(const GeomVertexWriter self, float data)
        
        /**
         * Sets the write row to a particular 1-component value, and advances the
         * write row.
         *
         * If the write row advances past the end of data, implicitly adds a new row
         * to the data.
         */
        """
        pass

    def addData1d(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_data1d(const GeomVertexWriter self, double data)
        
        /**
         * Sets the write row to a particular 1-component value, and advances the
         * write row.
         *
         * If the write row advances past the end of data, implicitly adds a new row
         * to the data.
         */
        """
        pass

    def addData1f(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_data1f(const GeomVertexWriter self, float data)
        
        /**
         * Sets the write row to a particular 1-component value, and advances the
         * write row.
         *
         * If the write row advances past the end of data, implicitly adds a new row
         * to the data.
         */
        """
        pass

    def addData1i(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_data1i(const GeomVertexWriter self, int data)
        
        /**
         * Sets the write row to a particular 1-component value, and advances the
         * write row.
         *
         * If the write row advances past the end of data, implicitly adds a new row
         * to the data.
         */
        """
        pass

    def addData2(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_data2(const GeomVertexWriter self, const LVecBase2f data)
        add_data2(const GeomVertexWriter self, float x, float y)
        
        /**
         * Sets the write row to a particular 2-component value, and advances the
         * write row.
         *
         * If the write row advances past the end of data, implicitly adds a new row
         * to the data.
         */
        
        /**
         * Sets the write row to a particular 2-component value, and advances the
         * write row.
         *
         * If the write row advances past the end of data, implicitly adds a new row
         * to the data.
         */
        """
        pass

    def addData2d(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_data2d(const GeomVertexWriter self, const LVecBase2d data)
        add_data2d(const GeomVertexWriter self, double x, double y)
        
        /**
         * Sets the write row to a particular 2-component value, and advances the
         * write row.
         *
         * If the write row advances past the end of data, implicitly adds a new row
         * to the data.
         */
        
        /**
         * Sets the write row to a particular 2-component value, and advances the
         * write row.
         *
         * If the write row advances past the end of data, implicitly adds a new row
         * to the data.
         */
        """
        pass

    def addData2f(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_data2f(const GeomVertexWriter self, const LVecBase2f data)
        add_data2f(const GeomVertexWriter self, float x, float y)
        
        /**
         * Sets the write row to a particular 2-component value, and advances the
         * write row.
         *
         * If the write row advances past the end of data, implicitly adds a new row
         * to the data.
         */
        
        /**
         * Sets the write row to a particular 2-component value, and advances the
         * write row.
         *
         * If the write row advances past the end of data, implicitly adds a new row
         * to the data.
         */
        """
        pass

    def addData2i(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_data2i(const GeomVertexWriter self, const LVecBase2i data)
        add_data2i(const GeomVertexWriter self, int a, int b)
        
        /**
         * Sets the write row to a particular 2-component value, and advances the
         * write row.
         *
         * If the write row advances past the end of data, implicitly adds a new row
         * to the data.
         */
        
        /**
         * Sets the write row to a particular 2-component value, and advances the
         * write row.
         *
         * If the write row advances past the end of data, implicitly adds a new row
         * to the data.
         */
        """
        pass

    def addData3(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_data3(const GeomVertexWriter self, const LVecBase3f data)
        add_data3(const GeomVertexWriter self, float x, float y, float z)
        
        /**
         * Sets the write row to a particular 3-component value, and advances the
         * write row.
         *
         * If the write row advances past the end of data, implicitly adds a new row
         * to the data.
         */
        
        /**
         * Sets the write row to a particular 3-component value, and advances the
         * write row.
         *
         * If the write row advances past the end of data, implicitly adds a new row
         * to the data.
         */
        """
        pass

    def addData3d(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_data3d(const GeomVertexWriter self, const LVecBase3d data)
        add_data3d(const GeomVertexWriter self, double x, double y, double z)
        
        /**
         * Sets the write row to a particular 3-component value, and advances the
         * write row.
         *
         * If the write row advances past the end of data, implicitly adds a new row
         * to the data.
         */
        
        /**
         * Sets the write row to a particular 3-component value, and advances the
         * write row.
         *
         * If the write row advances past the end of data, implicitly adds a new row
         * to the data.
         */
        """
        pass

    def addData3f(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_data3f(const GeomVertexWriter self, const LVecBase3f data)
        add_data3f(const GeomVertexWriter self, float x, float y, float z)
        
        /**
         * Sets the write row to a particular 3-component value, and advances the
         * write row.
         *
         * If the write row advances past the end of data, implicitly adds a new row
         * to the data.
         */
        
        /**
         * Sets the write row to a particular 3-component value, and advances the
         * write row.
         *
         * If the write row advances past the end of data, implicitly adds a new row
         * to the data.
         */
        """
        pass

    def addData3i(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_data3i(const GeomVertexWriter self, const LVecBase3i data)
        add_data3i(const GeomVertexWriter self, int a, int b, int c)
        
        /**
         * Sets the write row to a particular 3-component value, and advances the
         * write row.
         *
         * If the write row advances past the end of data, implicitly adds a new row
         * to the data.
         */
        
        /**
         * Sets the write row to a particular 3-component value, and advances the
         * write row.
         *
         * If the write row advances past the end of data, implicitly adds a new row
         * to the data.
         */
        """
        pass

    def addData4(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_data4(const GeomVertexWriter self, const LVecBase4f data)
        add_data4(const GeomVertexWriter self, float x, float y, float z, float w)
        
        /**
         * Sets the write row to a particular 4-component value, and advances the
         * write row.
         *
         * If the write row advances past the end of data, implicitly adds a new row
         * to the data.
         */
        
        /**
         * Sets the write row to a particular 4-component value, and advances the
         * write row.
         *
         * If the write row advances past the end of data, implicitly adds a new row
         * to the data.
         */
        """
        pass

    def addData4d(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_data4d(const GeomVertexWriter self, const LVecBase4d data)
        add_data4d(const GeomVertexWriter self, double x, double y, double z, double w)
        
        /**
         * Sets the write row to a particular 4-component value, and advances the
         * write row.
         *
         * If the write row advances past the end of data, implicitly adds a new row
         * to the data.
         */
        
        /**
         * Sets the write row to a particular 4-component value, and advances the
         * write row.
         *
         * If the write row advances past the end of data, implicitly adds a new row
         * to the data.
         */
        """
        pass

    def addData4f(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_data4f(const GeomVertexWriter self, const LVecBase4f data)
        add_data4f(const GeomVertexWriter self, float x, float y, float z, float w)
        
        /**
         * Sets the write row to a particular 4-component value, and advances the
         * write row.
         *
         * If the write row advances past the end of data, implicitly adds a new row
         * to the data.
         */
        
        /**
         * Sets the write row to a particular 4-component value, and advances the
         * write row.
         *
         * If the write row advances past the end of data, implicitly adds a new row
         * to the data.
         */
        """
        pass

    def addData4i(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_data4i(const GeomVertexWriter self, const LVecBase4i data)
        add_data4i(const GeomVertexWriter self, int a, int b, int c, int d)
        
        /**
         * Sets the write row to a particular 4-component value, and advances the
         * write row.
         *
         * If the write row advances past the end of data, implicitly adds a new row
         * to the data.
         */
        
        /**
         * Sets the write row to a particular 4-component value, and advances the
         * write row.
         *
         * If the write row advances past the end of data, implicitly adds a new row
         * to the data.
         */
        """
        pass

    def addMatrix3(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_matrix3(const GeomVertexWriter self, const LMatrix3f mat)
        
        /**
         * Sets the write row to a 3-by-3 matrix, and advances the write row.  This is
         * a special method that can only be used on matrix columns.
         *
         * If the write row advances past the end of data, implicitly adds a new row
         * to the data.
         */
        """
        pass

    def addMatrix3d(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_matrix3d(const GeomVertexWriter self, const LMatrix3d mat)
        
        /**
         * Sets the write row to a 3-by-3 matrix, and advances the write row.  This is
         * a special method that can only be used on matrix columns.
         *
         * If the write row advances past the end of data, implicitly adds a new row
         * to the data.
         */
        """
        pass

    def addMatrix3f(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_matrix3f(const GeomVertexWriter self, const LMatrix3f mat)
        
        /**
         * Sets the write row to a 3-by-3 matrix, and advances the write row.  This is
         * a special method that can only be used on matrix columns.
         *
         * If the write row advances past the end of data, implicitly adds a new row
         * to the data.
         */
        """
        pass

    def addMatrix4(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_matrix4(const GeomVertexWriter self, const LMatrix4f mat)
        
        /**
         * Sets the write row to a 4-by-4 matrix, and advances the write row.  This is
         * a special method that can only be used on matrix columns.
         *
         * If the write row advances past the end of data, implicitly adds a new row
         * to the data.
         */
        """
        pass

    def addMatrix4d(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_matrix4d(const GeomVertexWriter self, const LMatrix4d mat)
        
        /**
         * Sets the write row to a 4-by-4 matrix, and advances the write row.  This is
         * a special method that can only be used on matrix columns.
         *
         * If the write row advances past the end of data, implicitly adds a new row
         * to the data.
         */
        """
        pass

    def addMatrix4f(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_matrix4f(const GeomVertexWriter self, const LMatrix4f mat)
        
        /**
         * Sets the write row to a 4-by-4 matrix, and advances the write row.  This is
         * a special method that can only be used on matrix columns.
         *
         * If the write row advances past the end of data, implicitly adds a new row
         * to the data.
         */
        """
        pass

    def add_data1(self, const_GeomVertexWriter_self, float_data): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_data1(const GeomVertexWriter self, float data)
        
        /**
         * Sets the write row to a particular 1-component value, and advances the
         * write row.
         *
         * If the write row advances past the end of data, implicitly adds a new row
         * to the data.
         */
        """
        pass

    def add_data1d(self, const_GeomVertexWriter_self, double_data): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_data1d(const GeomVertexWriter self, double data)
        
        /**
         * Sets the write row to a particular 1-component value, and advances the
         * write row.
         *
         * If the write row advances past the end of data, implicitly adds a new row
         * to the data.
         */
        """
        pass

    def add_data1f(self, const_GeomVertexWriter_self, float_data): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_data1f(const GeomVertexWriter self, float data)
        
        /**
         * Sets the write row to a particular 1-component value, and advances the
         * write row.
         *
         * If the write row advances past the end of data, implicitly adds a new row
         * to the data.
         */
        """
        pass

    def add_data1i(self, const_GeomVertexWriter_self, int_data): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_data1i(const GeomVertexWriter self, int data)
        
        /**
         * Sets the write row to a particular 1-component value, and advances the
         * write row.
         *
         * If the write row advances past the end of data, implicitly adds a new row
         * to the data.
         */
        """
        pass

    def add_data2(self, const_GeomVertexWriter_self, const_LVecBase2f_data): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_data2(const GeomVertexWriter self, const LVecBase2f data)
        add_data2(const GeomVertexWriter self, float x, float y)
        
        /**
         * Sets the write row to a particular 2-component value, and advances the
         * write row.
         *
         * If the write row advances past the end of data, implicitly adds a new row
         * to the data.
         */
        
        /**
         * Sets the write row to a particular 2-component value, and advances the
         * write row.
         *
         * If the write row advances past the end of data, implicitly adds a new row
         * to the data.
         */
        """
        pass

    def add_data2d(self, const_GeomVertexWriter_self, const_LVecBase2d_data): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_data2d(const GeomVertexWriter self, const LVecBase2d data)
        add_data2d(const GeomVertexWriter self, double x, double y)
        
        /**
         * Sets the write row to a particular 2-component value, and advances the
         * write row.
         *
         * If the write row advances past the end of data, implicitly adds a new row
         * to the data.
         */
        
        /**
         * Sets the write row to a particular 2-component value, and advances the
         * write row.
         *
         * If the write row advances past the end of data, implicitly adds a new row
         * to the data.
         */
        """
        pass

    def add_data2f(self, const_GeomVertexWriter_self, const_LVecBase2f_data): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_data2f(const GeomVertexWriter self, const LVecBase2f data)
        add_data2f(const GeomVertexWriter self, float x, float y)
        
        /**
         * Sets the write row to a particular 2-component value, and advances the
         * write row.
         *
         * If the write row advances past the end of data, implicitly adds a new row
         * to the data.
         */
        
        /**
         * Sets the write row to a particular 2-component value, and advances the
         * write row.
         *
         * If the write row advances past the end of data, implicitly adds a new row
         * to the data.
         */
        """
        pass

    def add_data2i(self, const_GeomVertexWriter_self, const_LVecBase2i_data): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_data2i(const GeomVertexWriter self, const LVecBase2i data)
        add_data2i(const GeomVertexWriter self, int a, int b)
        
        /**
         * Sets the write row to a particular 2-component value, and advances the
         * write row.
         *
         * If the write row advances past the end of data, implicitly adds a new row
         * to the data.
         */
        
        /**
         * Sets the write row to a particular 2-component value, and advances the
         * write row.
         *
         * If the write row advances past the end of data, implicitly adds a new row
         * to the data.
         */
        """
        pass

    def add_data3(self, const_GeomVertexWriter_self, const_LVecBase3f_data): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_data3(const GeomVertexWriter self, const LVecBase3f data)
        add_data3(const GeomVertexWriter self, float x, float y, float z)
        
        /**
         * Sets the write row to a particular 3-component value, and advances the
         * write row.
         *
         * If the write row advances past the end of data, implicitly adds a new row
         * to the data.
         */
        
        /**
         * Sets the write row to a particular 3-component value, and advances the
         * write row.
         *
         * If the write row advances past the end of data, implicitly adds a new row
         * to the data.
         */
        """
        pass

    def add_data3d(self, const_GeomVertexWriter_self, const_LVecBase3d_data): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_data3d(const GeomVertexWriter self, const LVecBase3d data)
        add_data3d(const GeomVertexWriter self, double x, double y, double z)
        
        /**
         * Sets the write row to a particular 3-component value, and advances the
         * write row.
         *
         * If the write row advances past the end of data, implicitly adds a new row
         * to the data.
         */
        
        /**
         * Sets the write row to a particular 3-component value, and advances the
         * write row.
         *
         * If the write row advances past the end of data, implicitly adds a new row
         * to the data.
         */
        """
        pass

    def add_data3f(self, const_GeomVertexWriter_self, const_LVecBase3f_data): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_data3f(const GeomVertexWriter self, const LVecBase3f data)
        add_data3f(const GeomVertexWriter self, float x, float y, float z)
        
        /**
         * Sets the write row to a particular 3-component value, and advances the
         * write row.
         *
         * If the write row advances past the end of data, implicitly adds a new row
         * to the data.
         */
        
        /**
         * Sets the write row to a particular 3-component value, and advances the
         * write row.
         *
         * If the write row advances past the end of data, implicitly adds a new row
         * to the data.
         */
        """
        pass

    def add_data3i(self, const_GeomVertexWriter_self, const_LVecBase3i_data): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_data3i(const GeomVertexWriter self, const LVecBase3i data)
        add_data3i(const GeomVertexWriter self, int a, int b, int c)
        
        /**
         * Sets the write row to a particular 3-component value, and advances the
         * write row.
         *
         * If the write row advances past the end of data, implicitly adds a new row
         * to the data.
         */
        
        /**
         * Sets the write row to a particular 3-component value, and advances the
         * write row.
         *
         * If the write row advances past the end of data, implicitly adds a new row
         * to the data.
         */
        """
        pass

    def add_data4(self, const_GeomVertexWriter_self, const_LVecBase4f_data): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_data4(const GeomVertexWriter self, const LVecBase4f data)
        add_data4(const GeomVertexWriter self, float x, float y, float z, float w)
        
        /**
         * Sets the write row to a particular 4-component value, and advances the
         * write row.
         *
         * If the write row advances past the end of data, implicitly adds a new row
         * to the data.
         */
        
        /**
         * Sets the write row to a particular 4-component value, and advances the
         * write row.
         *
         * If the write row advances past the end of data, implicitly adds a new row
         * to the data.
         */
        """
        pass

    def add_data4d(self, const_GeomVertexWriter_self, const_LVecBase4d_data): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_data4d(const GeomVertexWriter self, const LVecBase4d data)
        add_data4d(const GeomVertexWriter self, double x, double y, double z, double w)
        
        /**
         * Sets the write row to a particular 4-component value, and advances the
         * write row.
         *
         * If the write row advances past the end of data, implicitly adds a new row
         * to the data.
         */
        
        /**
         * Sets the write row to a particular 4-component value, and advances the
         * write row.
         *
         * If the write row advances past the end of data, implicitly adds a new row
         * to the data.
         */
        """
        pass

    def add_data4f(self, const_GeomVertexWriter_self, const_LVecBase4f_data): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_data4f(const GeomVertexWriter self, const LVecBase4f data)
        add_data4f(const GeomVertexWriter self, float x, float y, float z, float w)
        
        /**
         * Sets the write row to a particular 4-component value, and advances the
         * write row.
         *
         * If the write row advances past the end of data, implicitly adds a new row
         * to the data.
         */
        
        /**
         * Sets the write row to a particular 4-component value, and advances the
         * write row.
         *
         * If the write row advances past the end of data, implicitly adds a new row
         * to the data.
         */
        """
        pass

    def add_data4i(self, const_GeomVertexWriter_self, const_LVecBase4i_data): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_data4i(const GeomVertexWriter self, const LVecBase4i data)
        add_data4i(const GeomVertexWriter self, int a, int b, int c, int d)
        
        /**
         * Sets the write row to a particular 4-component value, and advances the
         * write row.
         *
         * If the write row advances past the end of data, implicitly adds a new row
         * to the data.
         */
        
        /**
         * Sets the write row to a particular 4-component value, and advances the
         * write row.
         *
         * If the write row advances past the end of data, implicitly adds a new row
         * to the data.
         */
        """
        pass

    def add_matrix3(self, const_GeomVertexWriter_self, const_LMatrix3f_mat): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_matrix3(const GeomVertexWriter self, const LMatrix3f mat)
        
        /**
         * Sets the write row to a 3-by-3 matrix, and advances the write row.  This is
         * a special method that can only be used on matrix columns.
         *
         * If the write row advances past the end of data, implicitly adds a new row
         * to the data.
         */
        """
        pass

    def add_matrix3d(self, const_GeomVertexWriter_self, const_LMatrix3d_mat): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_matrix3d(const GeomVertexWriter self, const LMatrix3d mat)
        
        /**
         * Sets the write row to a 3-by-3 matrix, and advances the write row.  This is
         * a special method that can only be used on matrix columns.
         *
         * If the write row advances past the end of data, implicitly adds a new row
         * to the data.
         */
        """
        pass

    def add_matrix3f(self, const_GeomVertexWriter_self, const_LMatrix3f_mat): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_matrix3f(const GeomVertexWriter self, const LMatrix3f mat)
        
        /**
         * Sets the write row to a 3-by-3 matrix, and advances the write row.  This is
         * a special method that can only be used on matrix columns.
         *
         * If the write row advances past the end of data, implicitly adds a new row
         * to the data.
         */
        """
        pass

    def add_matrix4(self, const_GeomVertexWriter_self, const_LMatrix4f_mat): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_matrix4(const GeomVertexWriter self, const LMatrix4f mat)
        
        /**
         * Sets the write row to a 4-by-4 matrix, and advances the write row.  This is
         * a special method that can only be used on matrix columns.
         *
         * If the write row advances past the end of data, implicitly adds a new row
         * to the data.
         */
        """
        pass

    def add_matrix4d(self, const_GeomVertexWriter_self, const_LMatrix4d_mat): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_matrix4d(const GeomVertexWriter self, const LMatrix4d mat)
        
        /**
         * Sets the write row to a 4-by-4 matrix, and advances the write row.  This is
         * a special method that can only be used on matrix columns.
         *
         * If the write row advances past the end of data, implicitly adds a new row
         * to the data.
         */
        """
        pass

    def add_matrix4f(self, const_GeomVertexWriter_self, const_LMatrix4f_mat): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_matrix4f(const GeomVertexWriter self, const LMatrix4f mat)
        
        /**
         * Sets the write row to a 4-by-4 matrix, and advances the write row.  This is
         * a special method that can only be used on matrix columns.
         *
         * If the write row advances past the end of data, implicitly adds a new row
         * to the data.
         */
        """
        pass

    def assign(self, const_GeomVertexWriter_self, const_GeomVertexWriter_copy): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        assign(const GeomVertexWriter self, const GeomVertexWriter copy)
        """
        pass

    def clear(self, const_GeomVertexWriter_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear(const GeomVertexWriter self)
        
        /**
         * Resets the GeomVertexWriter to the initial state.
         */
        """
        pass

    def getArray(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_array(GeomVertexWriter self)
        
        /**
         * Returns the array index containing the data type that the writer is working
         * on.
         */
        """
        pass

    def getArrayData(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_array_data(GeomVertexWriter self)
        
        /**
         * Returns the particular array object that the writer is currently
         * processing.
         */
        """
        pass

    def getArrayHandle(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_array_handle(GeomVertexWriter self)
        
        /**
         * Returns the write handle to the array object that the writer is currently
         * processing.  This low-level call should be used with caution; be careful
         * with modifying the data in the handle out from under the GeomVertexWriter.
         */
        """
        pass

    def getColumn(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_column(GeomVertexWriter self)
        
        /**
         * Returns the description of the data type that the writer is working on.
         */
        """
        pass

    def getCurrentThread(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_current_thread(GeomVertexWriter self)
        
        /**
         * Returns the Thread pointer of the currently-executing thread, as passed to
         * the constructor of this object.
         */
        """
        pass

    def getStartRow(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_start_row(GeomVertexWriter self)
        
        /**
         * Returns the row index at which the writer started.  It will return to this
         * row if you reset the current column.
         */
        """
        pass

    def getStride(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_stride(GeomVertexWriter self)
        
        /**
         * Returns the per-row stride (bytes between consecutive rows) of the
         * underlying vertex array.  This low-level information is normally not needed
         * to use the GeomVertexWriter directly.
         */
        """
        pass

    def getVertexData(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_vertex_data(GeomVertexWriter self)
        
        /**
         * Returns the vertex data object that the writer is processing.  This may
         * return NULL if the writer was constructed with just an array pointer.
         */
        """
        pass

    def getWriteRow(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_write_row(GeomVertexWriter self)
        
        /**
         * Returns the row index to which the data will be written at the next call to
         * set_data*() or add_data*().
         */
        """
        pass

    def get_array(self, GeomVertexWriter_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_array(GeomVertexWriter self)
        
        /**
         * Returns the array index containing the data type that the writer is working
         * on.
         */
        """
        pass

    def get_array_data(self, GeomVertexWriter_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_array_data(GeomVertexWriter self)
        
        /**
         * Returns the particular array object that the writer is currently
         * processing.
         */
        """
        pass

    def get_array_handle(self, GeomVertexWriter_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_array_handle(GeomVertexWriter self)
        
        /**
         * Returns the write handle to the array object that the writer is currently
         * processing.  This low-level call should be used with caution; be careful
         * with modifying the data in the handle out from under the GeomVertexWriter.
         */
        """
        pass

    def get_column(self, GeomVertexWriter_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_column(GeomVertexWriter self)
        
        /**
         * Returns the description of the data type that the writer is working on.
         */
        """
        pass

    def get_current_thread(self, GeomVertexWriter_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_current_thread(GeomVertexWriter self)
        
        /**
         * Returns the Thread pointer of the currently-executing thread, as passed to
         * the constructor of this object.
         */
        """
        pass

    def get_start_row(self, GeomVertexWriter_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_start_row(GeomVertexWriter self)
        
        /**
         * Returns the row index at which the writer started.  It will return to this
         * row if you reset the current column.
         */
        """
        pass

    def get_stride(self, GeomVertexWriter_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_stride(GeomVertexWriter self)
        
        /**
         * Returns the per-row stride (bytes between consecutive rows) of the
         * underlying vertex array.  This low-level information is normally not needed
         * to use the GeomVertexWriter directly.
         */
        """
        pass

    def get_vertex_data(self, GeomVertexWriter_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_vertex_data(GeomVertexWriter self)
        
        /**
         * Returns the vertex data object that the writer is processing.  This may
         * return NULL if the writer was constructed with just an array pointer.
         */
        """
        pass

    def get_write_row(self, GeomVertexWriter_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_write_row(GeomVertexWriter self)
        
        /**
         * Returns the row index to which the data will be written at the next call to
         * set_data*() or add_data*().
         */
        """
        pass

    def hasColumn(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_column(GeomVertexWriter self)
        
        /**
         * Returns true if a valid data type has been successfully set, or false if
         * the data type does not exist.
         */
        """
        pass

    def has_column(self, GeomVertexWriter_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_column(GeomVertexWriter self)
        
        /**
         * Returns true if a valid data type has been successfully set, or false if
         * the data type does not exist.
         */
        """
        pass

    def isAtEnd(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_at_end(GeomVertexWriter self)
        
        /**
         * Returns true if the writer is currently at the end of the list of vertices,
         * false otherwise.  If this is true, another call to set_data*() will result
         * in a crash, but another call to add_data*() will add a new row.
         */
        """
        pass

    def is_at_end(self, GeomVertexWriter_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_at_end(GeomVertexWriter self)
        
        /**
         * Returns true if the writer is currently at the end of the list of vertices,
         * false otherwise.  If this is true, another call to set_data*() will result
         * in a crash, but another call to add_data*() will add a new row.
         */
        """
        pass

    def output(self, GeomVertexWriter_self, ostream_out): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        output(GeomVertexWriter self, ostream out)
        
        /**
         *
         */
        """
        pass

    def reserveNumRows(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        reserve_num_rows(const GeomVertexWriter self, int num_rows)
        
        /**
         * This ensures that enough memory space for num_rows is allocated, so that
         * you may add up to num_rows rows without causing a new memory allocation.
         * This is a performance optimization only; it is especially useful when you
         * know the number of rows you will be adding ahead of time.
         */
        """
        pass

    def reserve_num_rows(self, const_GeomVertexWriter_self, int_num_rows): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        reserve_num_rows(const GeomVertexWriter self, int num_rows)
        
        /**
         * This ensures that enough memory space for num_rows is allocated, so that
         * you may add up to num_rows rows without causing a new memory allocation.
         * This is a performance optimization only; it is especially useful when you
         * know the number of rows you will be adding ahead of time.
         */
        """
        pass

    def setColumn(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_column(const GeomVertexWriter self, const InternalName name)
        set_column(const GeomVertexWriter self, int column)
        set_column(const GeomVertexWriter self, int array, const GeomVertexColumn column)
        
        /**
         * Sets up the writer to use the nth data type of the GeomVertexFormat,
         * numbering from 0.
         *
         * This also resets the write row number to the start row (the same value
         * passed to a previous call to set_row(), or 0 if set_row() was never
         * called.)
         *
         * The return value is true if the data type is valid, false otherwise.
         */
        
        /**
         * Sets up the writer to use the data type with the indicated name.
         *
         * This also resets the write number to the start row (the same value passed
         * to a previous call to set_row(), or 0 if set_row() was never called.)
         *
         * The return value is true if the data type is valid, false otherwise.
         */
        
        /**
         * Sets up the writer to use the indicated column description on the given
         * array.
         *
         * This also resets the current write row number to the start row (the same
         * value passed to a previous call to set_row(), or 0 if set_row() was never
         * called.)
         *
         * The return value is true if the data type is valid, false otherwise.
         */
        """
        pass

    def setData1(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_data1(const GeomVertexWriter self, float data)
        
        /**
         * Sets the write row to a particular 1-component value, and advances the
         * write row.
         *
         * It is an error for the write row to advance past the end of data.
         */
        """
        pass

    def setData1d(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_data1d(const GeomVertexWriter self, double data)
        
        /**
         * Sets the write row to a particular 1-component value, and advances the
         * write row.
         *
         * It is an error for the write row to advance past the end of data.
         */
        """
        pass

    def setData1f(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_data1f(const GeomVertexWriter self, float data)
        
        /**
         * Sets the write row to a particular 1-component value, and advances the
         * write row.
         *
         * It is an error for the write row to advance past the end of data.
         */
        """
        pass

    def setData1i(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_data1i(const GeomVertexWriter self, int data)
        
        /**
         * Sets the write row to a particular 1-component value, and advances the
         * write row.
         *
         * It is an error for the write row to advance past the end of data.
         */
        """
        pass

    def setData2(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_data2(const GeomVertexWriter self, const LVecBase2f data)
        set_data2(const GeomVertexWriter self, float x, float y)
        
        /**
         * Sets the write row to a particular 2-component value, and advances the
         * write row.
         *
         * It is an error for the write row to advance past the end of data.
         */
        
        /**
         * Sets the write row to a particular 2-component value, and advances the
         * write row.
         *
         * It is an error for the write row to advance past the end of data.
         */
        """
        pass

    def setData2d(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_data2d(const GeomVertexWriter self, const LVecBase2d data)
        set_data2d(const GeomVertexWriter self, double x, double y)
        
        /**
         * Sets the write row to a particular 2-component value, and advances the
         * write row.
         *
         * It is an error for the write row to advance past the end of data.
         */
        
        /**
         * Sets the write row to a particular 2-component value, and advances the
         * write row.
         *
         * It is an error for the write row to advance past the end of data.
         */
        """
        pass

    def setData2f(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_data2f(const GeomVertexWriter self, const LVecBase2f data)
        set_data2f(const GeomVertexWriter self, float x, float y)
        
        /**
         * Sets the write row to a particular 2-component value, and advances the
         * write row.
         *
         * It is an error for the write row to advance past the end of data.
         */
        
        /**
         * Sets the write row to a particular 2-component value, and advances the
         * write row.
         *
         * It is an error for the write row to advance past the end of data.
         */
        """
        pass

    def setData2i(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_data2i(const GeomVertexWriter self, const LVecBase2i data)
        set_data2i(const GeomVertexWriter self, int a, int b)
        
        /**
         * Sets the write row to a particular 2-component value, and advances the
         * write row.
         *
         * It is an error for the write row to advance past the end of data.
         */
        
        /**
         * Sets the write row to a particular 2-component value, and advances the
         * write row.
         *
         * It is an error for the write row to advance past the end of data.
         */
        """
        pass

    def setData3(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_data3(const GeomVertexWriter self, const LVecBase3f data)
        set_data3(const GeomVertexWriter self, float x, float y, float z)
        
        /**
         * Sets the write row to a particular 3-component value, and advances the
         * write row.
         *
         * It is an error for the write row to advance past the end of data.
         */
        
        /**
         * Sets the write row to a particular 3-component value, and advances the
         * write row.
         *
         * It is an error for the write row to advance past the end of data.
         */
        """
        pass

    def setData3d(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_data3d(const GeomVertexWriter self, const LVecBase3d data)
        set_data3d(const GeomVertexWriter self, double x, double y, double z)
        
        /**
         * Sets the write row to a particular 3-component value, and advances the
         * write row.
         *
         * It is an error for the write row to advance past the end of data.
         */
        
        /**
         * Sets the write row to a particular 3-component value, and advances the
         * write row.
         *
         * It is an error for the write row to advance past the end of data.
         */
        """
        pass

    def setData3f(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_data3f(const GeomVertexWriter self, const LVecBase3f data)
        set_data3f(const GeomVertexWriter self, float x, float y, float z)
        
        /**
         * Sets the write row to a particular 3-component value, and advances the
         * write row.
         *
         * It is an error for the write row to advance past the end of data.
         */
        
        /**
         * Sets the write row to a particular 3-component value, and advances the
         * write row.
         *
         * It is an error for the write row to advance past the end of data.
         */
        """
        pass

    def setData3i(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_data3i(const GeomVertexWriter self, const LVecBase3i data)
        set_data3i(const GeomVertexWriter self, int a, int b, int c)
        
        /**
         * Sets the write row to a particular 3-component value, and advances the
         * write row.
         *
         * It is an error for the write row to advance past the end of data.
         */
        
        /**
         * Sets the write row to a particular 3-component value, and advances the
         * write row.
         *
         * It is an error for the write row to advance past the end of data.
         */
        """
        pass

    def setData4(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_data4(const GeomVertexWriter self, const LVecBase4f data)
        set_data4(const GeomVertexWriter self, float x, float y, float z, float w)
        
        /**
         * Sets the write row to a particular 4-component value, and advances the
         * write row.
         *
         * It is an error for the write row to advance past the end of data.
         */
        
        /**
         * Sets the write row to a particular 4-component value, and advances the
         * write row.
         *
         * It is an error for the write row to advance past the end of data.
         */
        """
        pass

    def setData4d(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_data4d(const GeomVertexWriter self, const LVecBase4d data)
        set_data4d(const GeomVertexWriter self, double x, double y, double z, double w)
        
        /**
         * Sets the write row to a particular 4-component value, and advances the
         * write row.
         *
         * It is an error for the write row to advance past the end of data.
         */
        
        /**
         * Sets the write row to a particular 4-component value, and advances the
         * write row.
         *
         * It is an error for the write row to advance past the end of data.
         */
        """
        pass

    def setData4f(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_data4f(const GeomVertexWriter self, const LVecBase4f data)
        set_data4f(const GeomVertexWriter self, float x, float y, float z, float w)
        
        /**
         * Sets the write row to a particular 4-component value, and advances the
         * write row.
         *
         * It is an error for the write row to advance past the end of data.
         */
        
        /**
         * Sets the write row to a particular 4-component value, and advances the
         * write row.
         *
         * It is an error for the write row to advance past the end of data.
         */
        """
        pass

    def setData4i(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_data4i(const GeomVertexWriter self, const LVecBase4i data)
        set_data4i(const GeomVertexWriter self, int a, int b, int c, int d)
        
        /**
         * Sets the write row to a particular 4-component value, and advances the
         * write row.
         *
         * It is an error for the write row to advance past the end of data.
         */
        
        /**
         * Sets the write row to a particular 4-component value, and advances the
         * write row.
         *
         * It is an error for the write row to advance past the end of data.
         */
        """
        pass

    def setMatrix3(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_matrix3(const GeomVertexWriter self, const LMatrix3f mat)
        
        /**
         * Sets the write row to a 3-by-3 matrix, and advances the write row.  This is
         * a special method that can only be used on matrix columns.
         *
         * It is an error for the write row to advance past the end of data.
         */
        """
        pass

    def setMatrix3d(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_matrix3d(const GeomVertexWriter self, const LMatrix3d mat)
        
        /**
         * Sets the write row to a 3-by-3 matrix, and advances the write row.  This is
         * a special method that can only be used on matrix columns.
         *
         * It is an error for the write row to advance past the end of data.
         */
        """
        pass

    def setMatrix3f(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_matrix3f(const GeomVertexWriter self, const LMatrix3f mat)
        
        /**
         * Sets the write row to a 3-by-3 matrix, and advances the write row.  This is
         * a special method that can only be used on matrix columns.
         *
         * It is an error for the write row to advance past the end of data.
         */
        """
        pass

    def setMatrix4(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_matrix4(const GeomVertexWriter self, const LMatrix4f mat)
        
        /**
         * Sets the write row to a 4-by-4 matrix, and advances the write row.  This is
         * a special method that can only be used on matrix columns.
         *
         * It is an error for the write row to advance past the end of data.
         */
        """
        pass

    def setMatrix4d(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_matrix4d(const GeomVertexWriter self, const LMatrix4d mat)
        
        /**
         * Sets the write row to a 4-by-4 matrix, and advances the write row.  This is
         * a special method that can only be used on matrix columns.
         *
         * It is an error for the write row to advance past the end of data.
         */
        """
        pass

    def setMatrix4f(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_matrix4f(const GeomVertexWriter self, const LMatrix4f mat)
        
        /**
         * Sets the write row to a 4-by-4 matrix, and advances the write row.  This is
         * a special method that can only be used on matrix columns.
         *
         * It is an error for the write row to advance past the end of data.
         */
        """
        pass

    def setRow(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_row(const GeomVertexWriter self, int row)
        
        /**
         * Sets the start row to the indicated value.  The writer will begin writing
         * to the indicated row; each subsequent set_data*() call will store the data
         * into the subsequent row.  If set_column() is called, the writer will return
         * to this row.
         */
        """
        pass

    def setRowUnsafe(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_row_unsafe(const GeomVertexWriter self, int row)
        
        /**
         * Sets the start row to the indicated value, without internal checks.  This
         * is the same as set_row(), but it does not check for the possibility that
         * the array has been reallocated internally for some reason; use only when
         * you are confident that the array is unchanged and you really need every bit
         * of available performance.
         */
        """
        pass

    def set_column(self, const_GeomVertexWriter_self, const_InternalName_name): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_column(const GeomVertexWriter self, const InternalName name)
        set_column(const GeomVertexWriter self, int column)
        set_column(const GeomVertexWriter self, int array, const GeomVertexColumn column)
        
        /**
         * Sets up the writer to use the nth data type of the GeomVertexFormat,
         * numbering from 0.
         *
         * This also resets the write row number to the start row (the same value
         * passed to a previous call to set_row(), or 0 if set_row() was never
         * called.)
         *
         * The return value is true if the data type is valid, false otherwise.
         */
        
        /**
         * Sets up the writer to use the data type with the indicated name.
         *
         * This also resets the write number to the start row (the same value passed
         * to a previous call to set_row(), or 0 if set_row() was never called.)
         *
         * The return value is true if the data type is valid, false otherwise.
         */
        
        /**
         * Sets up the writer to use the indicated column description on the given
         * array.
         *
         * This also resets the current write row number to the start row (the same
         * value passed to a previous call to set_row(), or 0 if set_row() was never
         * called.)
         *
         * The return value is true if the data type is valid, false otherwise.
         */
        """
        pass

    def set_data1(self, const_GeomVertexWriter_self, float_data): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_data1(const GeomVertexWriter self, float data)
        
        /**
         * Sets the write row to a particular 1-component value, and advances the
         * write row.
         *
         * It is an error for the write row to advance past the end of data.
         */
        """
        pass

    def set_data1d(self, const_GeomVertexWriter_self, double_data): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_data1d(const GeomVertexWriter self, double data)
        
        /**
         * Sets the write row to a particular 1-component value, and advances the
         * write row.
         *
         * It is an error for the write row to advance past the end of data.
         */
        """
        pass

    def set_data1f(self, const_GeomVertexWriter_self, float_data): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_data1f(const GeomVertexWriter self, float data)
        
        /**
         * Sets the write row to a particular 1-component value, and advances the
         * write row.
         *
         * It is an error for the write row to advance past the end of data.
         */
        """
        pass

    def set_data1i(self, const_GeomVertexWriter_self, int_data): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_data1i(const GeomVertexWriter self, int data)
        
        /**
         * Sets the write row to a particular 1-component value, and advances the
         * write row.
         *
         * It is an error for the write row to advance past the end of data.
         */
        """
        pass

    def set_data2(self, const_GeomVertexWriter_self, const_LVecBase2f_data): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_data2(const GeomVertexWriter self, const LVecBase2f data)
        set_data2(const GeomVertexWriter self, float x, float y)
        
        /**
         * Sets the write row to a particular 2-component value, and advances the
         * write row.
         *
         * It is an error for the write row to advance past the end of data.
         */
        
        /**
         * Sets the write row to a particular 2-component value, and advances the
         * write row.
         *
         * It is an error for the write row to advance past the end of data.
         */
        """
        pass

    def set_data2d(self, const_GeomVertexWriter_self, const_LVecBase2d_data): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_data2d(const GeomVertexWriter self, const LVecBase2d data)
        set_data2d(const GeomVertexWriter self, double x, double y)
        
        /**
         * Sets the write row to a particular 2-component value, and advances the
         * write row.
         *
         * It is an error for the write row to advance past the end of data.
         */
        
        /**
         * Sets the write row to a particular 2-component value, and advances the
         * write row.
         *
         * It is an error for the write row to advance past the end of data.
         */
        """
        pass

    def set_data2f(self, const_GeomVertexWriter_self, const_LVecBase2f_data): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_data2f(const GeomVertexWriter self, const LVecBase2f data)
        set_data2f(const GeomVertexWriter self, float x, float y)
        
        /**
         * Sets the write row to a particular 2-component value, and advances the
         * write row.
         *
         * It is an error for the write row to advance past the end of data.
         */
        
        /**
         * Sets the write row to a particular 2-component value, and advances the
         * write row.
         *
         * It is an error for the write row to advance past the end of data.
         */
        """
        pass

    def set_data2i(self, const_GeomVertexWriter_self, const_LVecBase2i_data): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_data2i(const GeomVertexWriter self, const LVecBase2i data)
        set_data2i(const GeomVertexWriter self, int a, int b)
        
        /**
         * Sets the write row to a particular 2-component value, and advances the
         * write row.
         *
         * It is an error for the write row to advance past the end of data.
         */
        
        /**
         * Sets the write row to a particular 2-component value, and advances the
         * write row.
         *
         * It is an error for the write row to advance past the end of data.
         */
        """
        pass

    def set_data3(self, const_GeomVertexWriter_self, const_LVecBase3f_data): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_data3(const GeomVertexWriter self, const LVecBase3f data)
        set_data3(const GeomVertexWriter self, float x, float y, float z)
        
        /**
         * Sets the write row to a particular 3-component value, and advances the
         * write row.
         *
         * It is an error for the write row to advance past the end of data.
         */
        
        /**
         * Sets the write row to a particular 3-component value, and advances the
         * write row.
         *
         * It is an error for the write row to advance past the end of data.
         */
        """
        pass

    def set_data3d(self, const_GeomVertexWriter_self, const_LVecBase3d_data): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_data3d(const GeomVertexWriter self, const LVecBase3d data)
        set_data3d(const GeomVertexWriter self, double x, double y, double z)
        
        /**
         * Sets the write row to a particular 3-component value, and advances the
         * write row.
         *
         * It is an error for the write row to advance past the end of data.
         */
        
        /**
         * Sets the write row to a particular 3-component value, and advances the
         * write row.
         *
         * It is an error for the write row to advance past the end of data.
         */
        """
        pass

    def set_data3f(self, const_GeomVertexWriter_self, const_LVecBase3f_data): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_data3f(const GeomVertexWriter self, const LVecBase3f data)
        set_data3f(const GeomVertexWriter self, float x, float y, float z)
        
        /**
         * Sets the write row to a particular 3-component value, and advances the
         * write row.
         *
         * It is an error for the write row to advance past the end of data.
         */
        
        /**
         * Sets the write row to a particular 3-component value, and advances the
         * write row.
         *
         * It is an error for the write row to advance past the end of data.
         */
        """
        pass

    def set_data3i(self, const_GeomVertexWriter_self, const_LVecBase3i_data): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_data3i(const GeomVertexWriter self, const LVecBase3i data)
        set_data3i(const GeomVertexWriter self, int a, int b, int c)
        
        /**
         * Sets the write row to a particular 3-component value, and advances the
         * write row.
         *
         * It is an error for the write row to advance past the end of data.
         */
        
        /**
         * Sets the write row to a particular 3-component value, and advances the
         * write row.
         *
         * It is an error for the write row to advance past the end of data.
         */
        """
        pass

    def set_data4(self, const_GeomVertexWriter_self, const_LVecBase4f_data): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_data4(const GeomVertexWriter self, const LVecBase4f data)
        set_data4(const GeomVertexWriter self, float x, float y, float z, float w)
        
        /**
         * Sets the write row to a particular 4-component value, and advances the
         * write row.
         *
         * It is an error for the write row to advance past the end of data.
         */
        
        /**
         * Sets the write row to a particular 4-component value, and advances the
         * write row.
         *
         * It is an error for the write row to advance past the end of data.
         */
        """
        pass

    def set_data4d(self, const_GeomVertexWriter_self, const_LVecBase4d_data): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_data4d(const GeomVertexWriter self, const LVecBase4d data)
        set_data4d(const GeomVertexWriter self, double x, double y, double z, double w)
        
        /**
         * Sets the write row to a particular 4-component value, and advances the
         * write row.
         *
         * It is an error for the write row to advance past the end of data.
         */
        
        /**
         * Sets the write row to a particular 4-component value, and advances the
         * write row.
         *
         * It is an error for the write row to advance past the end of data.
         */
        """
        pass

    def set_data4f(self, const_GeomVertexWriter_self, const_LVecBase4f_data): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_data4f(const GeomVertexWriter self, const LVecBase4f data)
        set_data4f(const GeomVertexWriter self, float x, float y, float z, float w)
        
        /**
         * Sets the write row to a particular 4-component value, and advances the
         * write row.
         *
         * It is an error for the write row to advance past the end of data.
         */
        
        /**
         * Sets the write row to a particular 4-component value, and advances the
         * write row.
         *
         * It is an error for the write row to advance past the end of data.
         */
        """
        pass

    def set_data4i(self, const_GeomVertexWriter_self, const_LVecBase4i_data): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_data4i(const GeomVertexWriter self, const LVecBase4i data)
        set_data4i(const GeomVertexWriter self, int a, int b, int c, int d)
        
        /**
         * Sets the write row to a particular 4-component value, and advances the
         * write row.
         *
         * It is an error for the write row to advance past the end of data.
         */
        
        /**
         * Sets the write row to a particular 4-component value, and advances the
         * write row.
         *
         * It is an error for the write row to advance past the end of data.
         */
        """
        pass

    def set_matrix3(self, const_GeomVertexWriter_self, const_LMatrix3f_mat): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_matrix3(const GeomVertexWriter self, const LMatrix3f mat)
        
        /**
         * Sets the write row to a 3-by-3 matrix, and advances the write row.  This is
         * a special method that can only be used on matrix columns.
         *
         * It is an error for the write row to advance past the end of data.
         */
        """
        pass

    def set_matrix3d(self, const_GeomVertexWriter_self, const_LMatrix3d_mat): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_matrix3d(const GeomVertexWriter self, const LMatrix3d mat)
        
        /**
         * Sets the write row to a 3-by-3 matrix, and advances the write row.  This is
         * a special method that can only be used on matrix columns.
         *
         * It is an error for the write row to advance past the end of data.
         */
        """
        pass

    def set_matrix3f(self, const_GeomVertexWriter_self, const_LMatrix3f_mat): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_matrix3f(const GeomVertexWriter self, const LMatrix3f mat)
        
        /**
         * Sets the write row to a 3-by-3 matrix, and advances the write row.  This is
         * a special method that can only be used on matrix columns.
         *
         * It is an error for the write row to advance past the end of data.
         */
        """
        pass

    def set_matrix4(self, const_GeomVertexWriter_self, const_LMatrix4f_mat): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_matrix4(const GeomVertexWriter self, const LMatrix4f mat)
        
        /**
         * Sets the write row to a 4-by-4 matrix, and advances the write row.  This is
         * a special method that can only be used on matrix columns.
         *
         * It is an error for the write row to advance past the end of data.
         */
        """
        pass

    def set_matrix4d(self, const_GeomVertexWriter_self, const_LMatrix4d_mat): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_matrix4d(const GeomVertexWriter self, const LMatrix4d mat)
        
        /**
         * Sets the write row to a 4-by-4 matrix, and advances the write row.  This is
         * a special method that can only be used on matrix columns.
         *
         * It is an error for the write row to advance past the end of data.
         */
        """
        pass

    def set_matrix4f(self, const_GeomVertexWriter_self, const_LMatrix4f_mat): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_matrix4f(const GeomVertexWriter self, const LMatrix4f mat)
        
        /**
         * Sets the write row to a 4-by-4 matrix, and advances the write row.  This is
         * a special method that can only be used on matrix columns.
         *
         * It is an error for the write row to advance past the end of data.
         */
        """
        pass

    def set_row(self, const_GeomVertexWriter_self, int_row): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_row(const GeomVertexWriter self, int row)
        
        /**
         * Sets the start row to the indicated value.  The writer will begin writing
         * to the indicated row; each subsequent set_data*() call will store the data
         * into the subsequent row.  If set_column() is called, the writer will return
         * to this row.
         */
        """
        pass

    def set_row_unsafe(self, const_GeomVertexWriter_self, int_row): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_row_unsafe(const GeomVertexWriter self, int row)
        
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
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.core.GeomVertexWriter' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.core.GeomVertexWriter' objects>"
        '__doc__': '/**\n * This object provides a high-level interface for quickly writing a sequence\n * of numeric values from a vertex table.\n *\n * This object can be used both to replace existing vertices in the table, or\n * to extend the table with new vertices.  The set_data*() family of methods\n * can only be used to replace existing data; it is an error to allow these to\n * run past the end of the data.  The add_data*() family of methods, on the\n * other hand, can be used to replace existing data or add new data; if you\n * call set_row() into the middle of existing data the add_data*() methods\n * will behave like the corresponding set_data*(), but if they run past the\n * end of existing data they will quietly add new vertices.\n *\n * Like GeomVertexReader, the writer is particularly optimized for writing a\n * single column of data values for a series of vertices, without changing\n * columns between each number.  Although you can also use one\n * GeomVertexWriter to write across the columns if it is convenient, by\n * calling set_column() repeatedly at each vertex, it is faster to write down\n * the columns, and to use a different GeomVertexWriter for each column.\n *\n * Note that, like a GeomVertexReader, a GeomVertexWriter does not keep a\n * reference count to the actual vertex data buffer.  This means that it is\n * important not to keep a GeomVertexWriter object around over a long period\n * of time in which the data buffer is likely to be deallocated; it is\n * intended for making a quick pass over the data in one session.\n *\n * It also means that you should create any GeomVertexWriters *before*\n * creating GeomVertexReaders on the same data, since the writer itself might\n * cause the vertex buffer to be deallocated.  Better yet, use a\n * GeomVertexRewriter if you are going to create both of them anyway.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.GeomVertexWriter' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE2FE7D0>'
        '__repr__': None, # (!) real value is "<slot wrapper '__repr__' of 'panda3d.core.GeomVertexWriter' objects>"
        '__str__': None, # (!) real value is "<slot wrapper '__str__' of 'panda3d.core.GeomVertexWriter' objects>"
        'addData1': None, # (!) real value is "<method 'addData1' of 'panda3d.core.GeomVertexWriter' objects>"
        'addData1d': None, # (!) real value is "<method 'addData1d' of 'panda3d.core.GeomVertexWriter' objects>"
        'addData1f': None, # (!) real value is "<method 'addData1f' of 'panda3d.core.GeomVertexWriter' objects>"
        'addData1i': None, # (!) real value is "<method 'addData1i' of 'panda3d.core.GeomVertexWriter' objects>"
        'addData2': None, # (!) real value is "<method 'addData2' of 'panda3d.core.GeomVertexWriter' objects>"
        'addData2d': None, # (!) real value is "<method 'addData2d' of 'panda3d.core.GeomVertexWriter' objects>"
        'addData2f': None, # (!) real value is "<method 'addData2f' of 'panda3d.core.GeomVertexWriter' objects>"
        'addData2i': None, # (!) real value is "<method 'addData2i' of 'panda3d.core.GeomVertexWriter' objects>"
        'addData3': None, # (!) real value is "<method 'addData3' of 'panda3d.core.GeomVertexWriter' objects>"
        'addData3d': None, # (!) real value is "<method 'addData3d' of 'panda3d.core.GeomVertexWriter' objects>"
        'addData3f': None, # (!) real value is "<method 'addData3f' of 'panda3d.core.GeomVertexWriter' objects>"
        'addData3i': None, # (!) real value is "<method 'addData3i' of 'panda3d.core.GeomVertexWriter' objects>"
        'addData4': None, # (!) real value is "<method 'addData4' of 'panda3d.core.GeomVertexWriter' objects>"
        'addData4d': None, # (!) real value is "<method 'addData4d' of 'panda3d.core.GeomVertexWriter' objects>"
        'addData4f': None, # (!) real value is "<method 'addData4f' of 'panda3d.core.GeomVertexWriter' objects>"
        'addData4i': None, # (!) real value is "<method 'addData4i' of 'panda3d.core.GeomVertexWriter' objects>"
        'addMatrix3': None, # (!) real value is "<method 'addMatrix3' of 'panda3d.core.GeomVertexWriter' objects>"
        'addMatrix3d': None, # (!) real value is "<method 'addMatrix3d' of 'panda3d.core.GeomVertexWriter' objects>"
        'addMatrix3f': None, # (!) real value is "<method 'addMatrix3f' of 'panda3d.core.GeomVertexWriter' objects>"
        'addMatrix4': None, # (!) real value is "<method 'addMatrix4' of 'panda3d.core.GeomVertexWriter' objects>"
        'addMatrix4d': None, # (!) real value is "<method 'addMatrix4d' of 'panda3d.core.GeomVertexWriter' objects>"
        'addMatrix4f': None, # (!) real value is "<method 'addMatrix4f' of 'panda3d.core.GeomVertexWriter' objects>"
        'add_data1': None, # (!) real value is "<method 'add_data1' of 'panda3d.core.GeomVertexWriter' objects>"
        'add_data1d': None, # (!) real value is "<method 'add_data1d' of 'panda3d.core.GeomVertexWriter' objects>"
        'add_data1f': None, # (!) real value is "<method 'add_data1f' of 'panda3d.core.GeomVertexWriter' objects>"
        'add_data1i': None, # (!) real value is "<method 'add_data1i' of 'panda3d.core.GeomVertexWriter' objects>"
        'add_data2': None, # (!) real value is "<method 'add_data2' of 'panda3d.core.GeomVertexWriter' objects>"
        'add_data2d': None, # (!) real value is "<method 'add_data2d' of 'panda3d.core.GeomVertexWriter' objects>"
        'add_data2f': None, # (!) real value is "<method 'add_data2f' of 'panda3d.core.GeomVertexWriter' objects>"
        'add_data2i': None, # (!) real value is "<method 'add_data2i' of 'panda3d.core.GeomVertexWriter' objects>"
        'add_data3': None, # (!) real value is "<method 'add_data3' of 'panda3d.core.GeomVertexWriter' objects>"
        'add_data3d': None, # (!) real value is "<method 'add_data3d' of 'panda3d.core.GeomVertexWriter' objects>"
        'add_data3f': None, # (!) real value is "<method 'add_data3f' of 'panda3d.core.GeomVertexWriter' objects>"
        'add_data3i': None, # (!) real value is "<method 'add_data3i' of 'panda3d.core.GeomVertexWriter' objects>"
        'add_data4': None, # (!) real value is "<method 'add_data4' of 'panda3d.core.GeomVertexWriter' objects>"
        'add_data4d': None, # (!) real value is "<method 'add_data4d' of 'panda3d.core.GeomVertexWriter' objects>"
        'add_data4f': None, # (!) real value is "<method 'add_data4f' of 'panda3d.core.GeomVertexWriter' objects>"
        'add_data4i': None, # (!) real value is "<method 'add_data4i' of 'panda3d.core.GeomVertexWriter' objects>"
        'add_matrix3': None, # (!) real value is "<method 'add_matrix3' of 'panda3d.core.GeomVertexWriter' objects>"
        'add_matrix3d': None, # (!) real value is "<method 'add_matrix3d' of 'panda3d.core.GeomVertexWriter' objects>"
        'add_matrix3f': None, # (!) real value is "<method 'add_matrix3f' of 'panda3d.core.GeomVertexWriter' objects>"
        'add_matrix4': None, # (!) real value is "<method 'add_matrix4' of 'panda3d.core.GeomVertexWriter' objects>"
        'add_matrix4d': None, # (!) real value is "<method 'add_matrix4d' of 'panda3d.core.GeomVertexWriter' objects>"
        'add_matrix4f': None, # (!) real value is "<method 'add_matrix4f' of 'panda3d.core.GeomVertexWriter' objects>"
        'assign': None, # (!) real value is "<method 'assign' of 'panda3d.core.GeomVertexWriter' objects>"
        'clear': None, # (!) real value is "<method 'clear' of 'panda3d.core.GeomVertexWriter' objects>"
        'getArray': None, # (!) real value is "<method 'getArray' of 'panda3d.core.GeomVertexWriter' objects>"
        'getArrayData': None, # (!) real value is "<method 'getArrayData' of 'panda3d.core.GeomVertexWriter' objects>"
        'getArrayHandle': None, # (!) real value is "<method 'getArrayHandle' of 'panda3d.core.GeomVertexWriter' objects>"
        'getColumn': None, # (!) real value is "<method 'getColumn' of 'panda3d.core.GeomVertexWriter' objects>"
        'getCurrentThread': None, # (!) real value is "<method 'getCurrentThread' of 'panda3d.core.GeomVertexWriter' objects>"
        'getStartRow': None, # (!) real value is "<method 'getStartRow' of 'panda3d.core.GeomVertexWriter' objects>"
        'getStride': None, # (!) real value is "<method 'getStride' of 'panda3d.core.GeomVertexWriter' objects>"
        'getVertexData': None, # (!) real value is "<method 'getVertexData' of 'panda3d.core.GeomVertexWriter' objects>"
        'getWriteRow': None, # (!) real value is "<method 'getWriteRow' of 'panda3d.core.GeomVertexWriter' objects>"
        'get_array': None, # (!) real value is "<method 'get_array' of 'panda3d.core.GeomVertexWriter' objects>"
        'get_array_data': None, # (!) real value is "<method 'get_array_data' of 'panda3d.core.GeomVertexWriter' objects>"
        'get_array_handle': None, # (!) real value is "<method 'get_array_handle' of 'panda3d.core.GeomVertexWriter' objects>"
        'get_column': None, # (!) real value is "<method 'get_column' of 'panda3d.core.GeomVertexWriter' objects>"
        'get_current_thread': None, # (!) real value is "<method 'get_current_thread' of 'panda3d.core.GeomVertexWriter' objects>"
        'get_start_row': None, # (!) real value is "<method 'get_start_row' of 'panda3d.core.GeomVertexWriter' objects>"
        'get_stride': None, # (!) real value is "<method 'get_stride' of 'panda3d.core.GeomVertexWriter' objects>"
        'get_vertex_data': None, # (!) real value is "<method 'get_vertex_data' of 'panda3d.core.GeomVertexWriter' objects>"
        'get_write_row': None, # (!) real value is "<method 'get_write_row' of 'panda3d.core.GeomVertexWriter' objects>"
        'hasColumn': None, # (!) real value is "<method 'hasColumn' of 'panda3d.core.GeomVertexWriter' objects>"
        'has_column': None, # (!) real value is "<method 'has_column' of 'panda3d.core.GeomVertexWriter' objects>"
        'isAtEnd': None, # (!) real value is "<method 'isAtEnd' of 'panda3d.core.GeomVertexWriter' objects>"
        'is_at_end': None, # (!) real value is "<method 'is_at_end' of 'panda3d.core.GeomVertexWriter' objects>"
        'output': None, # (!) real value is "<method 'output' of 'panda3d.core.GeomVertexWriter' objects>"
        'reserveNumRows': None, # (!) real value is "<method 'reserveNumRows' of 'panda3d.core.GeomVertexWriter' objects>"
        'reserve_num_rows': None, # (!) real value is "<method 'reserve_num_rows' of 'panda3d.core.GeomVertexWriter' objects>"
        'setColumn': None, # (!) real value is "<method 'setColumn' of 'panda3d.core.GeomVertexWriter' objects>"
        'setData1': None, # (!) real value is "<method 'setData1' of 'panda3d.core.GeomVertexWriter' objects>"
        'setData1d': None, # (!) real value is "<method 'setData1d' of 'panda3d.core.GeomVertexWriter' objects>"
        'setData1f': None, # (!) real value is "<method 'setData1f' of 'panda3d.core.GeomVertexWriter' objects>"
        'setData1i': None, # (!) real value is "<method 'setData1i' of 'panda3d.core.GeomVertexWriter' objects>"
        'setData2': None, # (!) real value is "<method 'setData2' of 'panda3d.core.GeomVertexWriter' objects>"
        'setData2d': None, # (!) real value is "<method 'setData2d' of 'panda3d.core.GeomVertexWriter' objects>"
        'setData2f': None, # (!) real value is "<method 'setData2f' of 'panda3d.core.GeomVertexWriter' objects>"
        'setData2i': None, # (!) real value is "<method 'setData2i' of 'panda3d.core.GeomVertexWriter' objects>"
        'setData3': None, # (!) real value is "<method 'setData3' of 'panda3d.core.GeomVertexWriter' objects>"
        'setData3d': None, # (!) real value is "<method 'setData3d' of 'panda3d.core.GeomVertexWriter' objects>"
        'setData3f': None, # (!) real value is "<method 'setData3f' of 'panda3d.core.GeomVertexWriter' objects>"
        'setData3i': None, # (!) real value is "<method 'setData3i' of 'panda3d.core.GeomVertexWriter' objects>"
        'setData4': None, # (!) real value is "<method 'setData4' of 'panda3d.core.GeomVertexWriter' objects>"
        'setData4d': None, # (!) real value is "<method 'setData4d' of 'panda3d.core.GeomVertexWriter' objects>"
        'setData4f': None, # (!) real value is "<method 'setData4f' of 'panda3d.core.GeomVertexWriter' objects>"
        'setData4i': None, # (!) real value is "<method 'setData4i' of 'panda3d.core.GeomVertexWriter' objects>"
        'setMatrix3': None, # (!) real value is "<method 'setMatrix3' of 'panda3d.core.GeomVertexWriter' objects>"
        'setMatrix3d': None, # (!) real value is "<method 'setMatrix3d' of 'panda3d.core.GeomVertexWriter' objects>"
        'setMatrix3f': None, # (!) real value is "<method 'setMatrix3f' of 'panda3d.core.GeomVertexWriter' objects>"
        'setMatrix4': None, # (!) real value is "<method 'setMatrix4' of 'panda3d.core.GeomVertexWriter' objects>"
        'setMatrix4d': None, # (!) real value is "<method 'setMatrix4d' of 'panda3d.core.GeomVertexWriter' objects>"
        'setMatrix4f': None, # (!) real value is "<method 'setMatrix4f' of 'panda3d.core.GeomVertexWriter' objects>"
        'setRow': None, # (!) real value is "<method 'setRow' of 'panda3d.core.GeomVertexWriter' objects>"
        'setRowUnsafe': None, # (!) real value is "<method 'setRowUnsafe' of 'panda3d.core.GeomVertexWriter' objects>"
        'set_column': None, # (!) real value is "<method 'set_column' of 'panda3d.core.GeomVertexWriter' objects>"
        'set_data1': None, # (!) real value is "<method 'set_data1' of 'panda3d.core.GeomVertexWriter' objects>"
        'set_data1d': None, # (!) real value is "<method 'set_data1d' of 'panda3d.core.GeomVertexWriter' objects>"
        'set_data1f': None, # (!) real value is "<method 'set_data1f' of 'panda3d.core.GeomVertexWriter' objects>"
        'set_data1i': None, # (!) real value is "<method 'set_data1i' of 'panda3d.core.GeomVertexWriter' objects>"
        'set_data2': None, # (!) real value is "<method 'set_data2' of 'panda3d.core.GeomVertexWriter' objects>"
        'set_data2d': None, # (!) real value is "<method 'set_data2d' of 'panda3d.core.GeomVertexWriter' objects>"
        'set_data2f': None, # (!) real value is "<method 'set_data2f' of 'panda3d.core.GeomVertexWriter' objects>"
        'set_data2i': None, # (!) real value is "<method 'set_data2i' of 'panda3d.core.GeomVertexWriter' objects>"
        'set_data3': None, # (!) real value is "<method 'set_data3' of 'panda3d.core.GeomVertexWriter' objects>"
        'set_data3d': None, # (!) real value is "<method 'set_data3d' of 'panda3d.core.GeomVertexWriter' objects>"
        'set_data3f': None, # (!) real value is "<method 'set_data3f' of 'panda3d.core.GeomVertexWriter' objects>"
        'set_data3i': None, # (!) real value is "<method 'set_data3i' of 'panda3d.core.GeomVertexWriter' objects>"
        'set_data4': None, # (!) real value is "<method 'set_data4' of 'panda3d.core.GeomVertexWriter' objects>"
        'set_data4d': None, # (!) real value is "<method 'set_data4d' of 'panda3d.core.GeomVertexWriter' objects>"
        'set_data4f': None, # (!) real value is "<method 'set_data4f' of 'panda3d.core.GeomVertexWriter' objects>"
        'set_data4i': None, # (!) real value is "<method 'set_data4i' of 'panda3d.core.GeomVertexWriter' objects>"
        'set_matrix3': None, # (!) real value is "<method 'set_matrix3' of 'panda3d.core.GeomVertexWriter' objects>"
        'set_matrix3d': None, # (!) real value is "<method 'set_matrix3d' of 'panda3d.core.GeomVertexWriter' objects>"
        'set_matrix3f': None, # (!) real value is "<method 'set_matrix3f' of 'panda3d.core.GeomVertexWriter' objects>"
        'set_matrix4': None, # (!) real value is "<method 'set_matrix4' of 'panda3d.core.GeomVertexWriter' objects>"
        'set_matrix4d': None, # (!) real value is "<method 'set_matrix4d' of 'panda3d.core.GeomVertexWriter' objects>"
        'set_matrix4f': None, # (!) real value is "<method 'set_matrix4f' of 'panda3d.core.GeomVertexWriter' objects>"
        'set_row': None, # (!) real value is "<method 'set_row' of 'panda3d.core.GeomVertexWriter' objects>"
        'set_row_unsafe': None, # (!) real value is "<method 'set_row_unsafe' of 'panda3d.core.GeomVertexWriter' objects>"
    }


