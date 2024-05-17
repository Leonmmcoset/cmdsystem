# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .CopyOnWriteObject import CopyOnWriteObject

from .GeomEnums import GeomEnums

class GeomVertexData(CopyOnWriteObject, GeomEnums):
    """
    /**
     * This defines the actual numeric vertex data stored in a Geom, in the
     * structure defined by a particular GeomVertexFormat object.
     *
     * The data consists of one or more arrays, each of which in turn consists of
     * a series of rows, one per vertex.  All arrays should have the same number
     * of rows; each vertex is defined by the column data from a particular row
     * across all arrays.
     *
     * Often, there will be only one array per Geom, and the various columns
     * defined in the GeomVertexFormat will be interleaved within that array.
     * However, it is also possible to have multiple different arrays, with a
     * certain subset of the total columns defined in each array.
     *
     * However the data is distributed, the effect is of a single table of
     * vertices, where each vertex is represented by one row of the table.
     *
     * In general, application code should not attempt to directly manipulate the
     * vertex data through this structure; instead, use the GeomVertexReader,
     * GeomVertexWriter, and GeomVertexRewriter objects to read and write vertex
     * data at a high level.
     */
    """
    def animateVertices(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        animate_vertices(GeomVertexData self, bool force, Thread current_thread)
        
        /**
         * Returns a GeomVertexData that represents the results of computing the
         * vertex animation on the CPU for this GeomVertexData.
         *
         * If there is no CPU-defined vertex animation on this object, this just
         * returns the original object.
         *
         * If there is vertex animation, but the VertexTransform values have not
         * changed since last time, this may return the same pointer it returned
         * previously.  Even if the VertexTransform values have changed, it may still
         * return the same pointer, but with its contents modified (this is preferred,
         * since it allows the graphics backend to update vertex buffers optimally).
         *
         * If force is false, this method may return immediately with stale data, if
         * the vertex data is not completely resident.  If force is true, this method
         * will never return stale data, but may block until the data is available.
         */
        """
        pass

    def animate_vertices(self, GeomVertexData_self, bool_force, Thread_current_thread): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        animate_vertices(GeomVertexData self, bool force, Thread current_thread)
        
        /**
         * Returns a GeomVertexData that represents the results of computing the
         * vertex animation on the CPU for this GeomVertexData.
         *
         * If there is no CPU-defined vertex animation on this object, this just
         * returns the original object.
         *
         * If there is vertex animation, but the VertexTransform values have not
         * changed since last time, this may return the same pointer it returned
         * previously.  Even if the VertexTransform values have changed, it may still
         * return the same pointer, but with its contents modified (this is preferred,
         * since it allows the graphics backend to update vertex buffers optimally).
         *
         * If force is false, this method may return immediately with stale data, if
         * the vertex data is not completely resident.  If force is true, this method
         * will never return stale data, but may block until the data is available.
         */
        """
        pass

    def assign(self, const_GeomVertexData_self, const_GeomVertexData_copy): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        assign(const GeomVertexData self, const GeomVertexData copy)
        """
        pass

    def clearAnimatedVertices(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_animated_vertices(const GeomVertexData self)
        
        /**
         * Removes the cache of animated vertices computed by a previous call to
         * animate_vertices() within the same frame.  This will force the next call to
         * animate_vertices() to recompute these values from scratch.  Normally it is
         * not necessary to call this.
         */
        """
        pass

    def clearCache(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_cache(const GeomVertexData self)
        
        /**
         * Removes all of the previously-cached results of convert_to().
         *
         * This blows away the entire cache, upstream and downstream the pipeline.
         * Use clear_cache_stage() instead if you only want to blow away the cache at
         * the current stage and upstream.
         */
        """
        pass

    def clearCacheStage(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_cache_stage(const GeomVertexData self)
        
        /**
         * Removes all of the previously-cached results of convert_to(), at the
         * current pipeline stage and upstream.  Does not affect the downstream cache.
         *
         * Don't call this in a downstream thread unless you don't mind it blowing
         * away other changes you might have recently made in an upstream thread.
         */
        """
        pass

    def clearRows(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_rows(const GeomVertexData self)
        
        /**
         * Removes all of the rows from the arrays; functionally equivalent to
         * set_num_rows(0) (but faster).
         *
         * Don't call this in a downstream thread unless you don't mind it blowing
         * away other changes you might have recently made in an upstream thread.
         */
        """
        pass

    def clearSliderTable(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_slider_table(const GeomVertexData self)
        
        /**
         * Sets the SliderTable pointer to NULL, removing the table from the vertex
         * data.  This disables morph (blend shape) animation.
         */
        """
        pass

    def clearTransformBlendTable(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_transform_blend_table(const GeomVertexData self)
        
        /**
         * Sets the TransformBlendTable pointer to NULL, removing the table from the
         * vertex data.  This disables CPU-driven vertex animation.
         */
        """
        pass

    def clearTransformTable(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_transform_table(const GeomVertexData self)
        
        /**
         * Sets the TransformTable pointer to NULL, removing the table from the vertex
         * data.  This disables hardware-driven vertex animation.
         */
        """
        pass

    def clear_animated_vertices(self, const_GeomVertexData_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_animated_vertices(const GeomVertexData self)
        
        /**
         * Removes the cache of animated vertices computed by a previous call to
         * animate_vertices() within the same frame.  This will force the next call to
         * animate_vertices() to recompute these values from scratch.  Normally it is
         * not necessary to call this.
         */
        """
        pass

    def clear_cache(self, const_GeomVertexData_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_cache(const GeomVertexData self)
        
        /**
         * Removes all of the previously-cached results of convert_to().
         *
         * This blows away the entire cache, upstream and downstream the pipeline.
         * Use clear_cache_stage() instead if you only want to blow away the cache at
         * the current stage and upstream.
         */
        """
        pass

    def clear_cache_stage(self, const_GeomVertexData_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_cache_stage(const GeomVertexData self)
        
        /**
         * Removes all of the previously-cached results of convert_to(), at the
         * current pipeline stage and upstream.  Does not affect the downstream cache.
         *
         * Don't call this in a downstream thread unless you don't mind it blowing
         * away other changes you might have recently made in an upstream thread.
         */
        """
        pass

    def clear_rows(self, const_GeomVertexData_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_rows(const GeomVertexData self)
        
        /**
         * Removes all of the rows from the arrays; functionally equivalent to
         * set_num_rows(0) (but faster).
         *
         * Don't call this in a downstream thread unless you don't mind it blowing
         * away other changes you might have recently made in an upstream thread.
         */
        """
        pass

    def clear_slider_table(self, const_GeomVertexData_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_slider_table(const GeomVertexData self)
        
        /**
         * Sets the SliderTable pointer to NULL, removing the table from the vertex
         * data.  This disables morph (blend shape) animation.
         */
        """
        pass

    def clear_transform_blend_table(self, const_GeomVertexData_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_transform_blend_table(const GeomVertexData self)
        
        /**
         * Sets the TransformBlendTable pointer to NULL, removing the table from the
         * vertex data.  This disables CPU-driven vertex animation.
         */
        """
        pass

    def clear_transform_table(self, const_GeomVertexData_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_transform_table(const GeomVertexData self)
        
        /**
         * Sets the TransformTable pointer to NULL, removing the table from the vertex
         * data.  This disables hardware-driven vertex animation.
         */
        """
        pass

    def compareTo(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        compare_to(GeomVertexData self, const GeomVertexData other)
        
        /**
         * Returns 0 if the two objects are equivalent, even if they are not the same
         * pointer.
         */
        """
        pass

    def compare_to(self, GeomVertexData_self, const_GeomVertexData_other): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        compare_to(GeomVertexData self, const GeomVertexData other)
        
        /**
         * Returns 0 if the two objects are equivalent, even if they are not the same
         * pointer.
         */
        """
        pass

    def convertTo(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        convert_to(GeomVertexData self, const GeomVertexFormat new_format)
        
        /**
         * Returns a new GeomVertexData that represents the same contents as this one,
         * with all data types matched up name-by-name to the indicated new format.
         */
        """
        pass

    def convert_to(self, GeomVertexData_self, const_GeomVertexFormat_new_format): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        convert_to(GeomVertexData self, const GeomVertexFormat new_format)
        
        /**
         * Returns a new GeomVertexData that represents the same contents as this one,
         * with all data types matched up name-by-name to the indicated new format.
         */
        """
        pass

    def copyFrom(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        copy_from(const GeomVertexData self, const GeomVertexData source, bool keep_data_objects, Thread current_thread)
        
        /**
         * Copies all the data from the other array into the corresponding data types
         * in this array, by matching data types name-by-name.
         *
         * keep_data_objects specifies what to do when one or more of the arrays can
         * be copied without the need to apply any conversion operation.  If it is
         * true, the original GeomVertexArrayData objects in this object are retained,
         * and their data arrays are copied byte-by-byte from the source; if it is
         * false, then the GeomVertexArrayData objects are copied pointerwise from the
         * source.
         *
         * Don't call this in a downstream thread unless you don't mind it blowing
         * away other changes you might have recently made in an upstream thread.
         */
        """
        pass

    def copyRowFrom(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        copy_row_from(const GeomVertexData self, int dest_row, const GeomVertexData source, int source_row, Thread current_thread)
        
        /**
         * Copies a single row of the data from the other array into the indicated row
         * of this array.  In this case, the source format must exactly match the
         * destination format.
         *
         * Don't call this in a downstream thread unless you don't mind it blowing
         * away other changes you might have recently made in an upstream thread.
         */
        """
        pass

    def copy_from(self, const_GeomVertexData_self, const_GeomVertexData_source, bool_keep_data_objects, Thread_current_thread): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        copy_from(const GeomVertexData self, const GeomVertexData source, bool keep_data_objects, Thread current_thread)
        
        /**
         * Copies all the data from the other array into the corresponding data types
         * in this array, by matching data types name-by-name.
         *
         * keep_data_objects specifies what to do when one or more of the arrays can
         * be copied without the need to apply any conversion operation.  If it is
         * true, the original GeomVertexArrayData objects in this object are retained,
         * and their data arrays are copied byte-by-byte from the source; if it is
         * false, then the GeomVertexArrayData objects are copied pointerwise from the
         * source.
         *
         * Don't call this in a downstream thread unless you don't mind it blowing
         * away other changes you might have recently made in an upstream thread.
         */
        """
        pass

    def copy_row_from(self, const_GeomVertexData_self, int_dest_row, const_GeomVertexData_source, int_source_row, Thread_current_thread): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        copy_row_from(const GeomVertexData self, int dest_row, const GeomVertexData source, int source_row, Thread current_thread)
        
        /**
         * Copies a single row of the data from the other array into the indicated row
         * of this array.  In this case, the source format must exactly match the
         * destination format.
         *
         * Don't call this in a downstream thread unless you don't mind it blowing
         * away other changes you might have recently made in an upstream thread.
         */
        """
        pass

    def describeVertex(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        describe_vertex(GeomVertexData self, ostream out, int row)
        
        /**
         * Writes a verbose, human-friendly description of the indicated vertex
         * number.
         */
        """
        pass

    def describe_vertex(self, GeomVertexData_self, ostream_out, int_row): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        describe_vertex(GeomVertexData self, ostream out, int row)
        
        /**
         * Writes a verbose, human-friendly description of the indicated vertex
         * number.
         */
        """
        pass

    def getArray(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_array(GeomVertexData self, int i)
        
        /**
         * Returns a const pointer to the vertex data for the indicated array, for
         * application code to directly examine (but not modify) the underlying vertex
         * data.
         */
        """
        pass

    def getArrayHandle(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_array_handle(GeomVertexData self, int i)
        
        /**
         * Equivalent to get_array(i).get_handle().
         */
        """
        pass

    def getArrays(self, *args, **kwargs): # real signature unknown
        pass

    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getFormat(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_format(GeomVertexData self)
        
        /**
         * Returns a pointer to the GeomVertexFormat structure that defines this data.
         */
        """
        pass

    def getModified(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_modified(GeomVertexData self, Thread current_thread)
        
        /**
         * Returns a sequence number which is guaranteed to change at least every time
         * the vertex data is modified.
         */
        """
        pass

    def getName(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_name(GeomVertexData self)
        
        /**
         * Returns the name passed to the constructor, if any.  This name is reported
         * on the PStats graph for vertex computations.
         */
        """
        pass

    def getNumArrays(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_arrays(GeomVertexData self)
        
        /**
         * Returns the number of individual arrays stored within the data.  This must
         * match get_format()->get_num_arrays().
         */
        """
        pass

    def getNumBytes(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_bytes(GeomVertexData self)
        
        /**
         * Returns the total number of bytes consumed by the different arrays of the
         * vertex data.
         */
        """
        pass

    def getNumRows(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_rows(GeomVertexData self)
        
        /**
         * Returns the number of rows stored within all the arrays.  All arrays store
         * data for the same n rows.
         */
        """
        pass

    def getSliderTable(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_slider_table(GeomVertexData self)
        
        /**
         * Returns a const pointer to the SliderTable assigned to this data.  Vertices
         * within the vertex data will look up their morph offsets, if any, within
         * this table.
         *
         * This will return NULL if the vertex data does not have a SliderTable
         * assigned.
         */
        """
        pass

    def getTransformBlendTable(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_transform_blend_table(GeomVertexData self)
        
        /**
         * Returns a const pointer to the TransformBlendTable assigned to this data.
         * Vertices within the table will index into this table to indicate their
         * dynamic skinning information; this table is used when the vertex animation
         * is to be performed by the CPU (but also see get_transform_table()).
         *
         * This will return NULL if the vertex data does not have a
         * TransformBlendTable assigned (which implies the vertices will not be
         * animated by the CPU).
         */
        """
        pass

    def getTransformTable(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_transform_table(GeomVertexData self)
        
        /**
         * Returns a const pointer to the TransformTable assigned to this data.
         * Vertices within the table will index into this table to indicate their
         * dynamic skinning information; this table is used when the vertex animation
         * is to be performed by the graphics hardware (but also see
         * get_transform_blend_table()).
         *
         * This will return NULL if the vertex data does not have a TransformTable
         * assigned (which implies the vertices will not be animated by the graphics
         * hardware).
         */
        """
        pass

    def getUsageHint(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_usage_hint(GeomVertexData self)
        
        /**
         * Returns the usage hint that was passed to the constructor, and which will
         * be passed to each array data object created initially, and arrays created
         * as the result of a convert_to() operation.  See geomEnums.h.
         *
         * However, each individual array may be replaced with a different array
         * object with an independent usage hint specified, so there is no guarantee
         * that the individual arrays all have the same usage_hint.
         */
        """
        pass

    def get_array(self, GeomVertexData_self, int_i): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_array(GeomVertexData self, int i)
        
        /**
         * Returns a const pointer to the vertex data for the indicated array, for
         * application code to directly examine (but not modify) the underlying vertex
         * data.
         */
        """
        pass

    def get_arrays(self, *args, **kwargs): # real signature unknown
        pass

    def get_array_handle(self, GeomVertexData_self, int_i): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_array_handle(GeomVertexData self, int i)
        
        /**
         * Equivalent to get_array(i).get_handle().
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_format(self, GeomVertexData_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_format(GeomVertexData self)
        
        /**
         * Returns a pointer to the GeomVertexFormat structure that defines this data.
         */
        """
        pass

    def get_modified(self, GeomVertexData_self, Thread_current_thread): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_modified(GeomVertexData self, Thread current_thread)
        
        /**
         * Returns a sequence number which is guaranteed to change at least every time
         * the vertex data is modified.
         */
        """
        pass

    def get_name(self, GeomVertexData_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_name(GeomVertexData self)
        
        /**
         * Returns the name passed to the constructor, if any.  This name is reported
         * on the PStats graph for vertex computations.
         */
        """
        pass

    def get_num_arrays(self, GeomVertexData_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_arrays(GeomVertexData self)
        
        /**
         * Returns the number of individual arrays stored within the data.  This must
         * match get_format()->get_num_arrays().
         */
        """
        pass

    def get_num_bytes(self, GeomVertexData_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_bytes(GeomVertexData self)
        
        /**
         * Returns the total number of bytes consumed by the different arrays of the
         * vertex data.
         */
        """
        pass

    def get_num_rows(self, GeomVertexData_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_rows(GeomVertexData self)
        
        /**
         * Returns the number of rows stored within all the arrays.  All arrays store
         * data for the same n rows.
         */
        """
        pass

    def get_slider_table(self, GeomVertexData_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_slider_table(GeomVertexData self)
        
        /**
         * Returns a const pointer to the SliderTable assigned to this data.  Vertices
         * within the vertex data will look up their morph offsets, if any, within
         * this table.
         *
         * This will return NULL if the vertex data does not have a SliderTable
         * assigned.
         */
        """
        pass

    def get_transform_blend_table(self, GeomVertexData_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_transform_blend_table(GeomVertexData self)
        
        /**
         * Returns a const pointer to the TransformBlendTable assigned to this data.
         * Vertices within the table will index into this table to indicate their
         * dynamic skinning information; this table is used when the vertex animation
         * is to be performed by the CPU (but also see get_transform_table()).
         *
         * This will return NULL if the vertex data does not have a
         * TransformBlendTable assigned (which implies the vertices will not be
         * animated by the CPU).
         */
        """
        pass

    def get_transform_table(self, GeomVertexData_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_transform_table(GeomVertexData self)
        
        /**
         * Returns a const pointer to the TransformTable assigned to this data.
         * Vertices within the table will index into this table to indicate their
         * dynamic skinning information; this table is used when the vertex animation
         * is to be performed by the graphics hardware (but also see
         * get_transform_blend_table()).
         *
         * This will return NULL if the vertex data does not have a TransformTable
         * assigned (which implies the vertices will not be animated by the graphics
         * hardware).
         */
        """
        pass

    def get_usage_hint(self, GeomVertexData_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_usage_hint(GeomVertexData self)
        
        /**
         * Returns the usage hint that was passed to the constructor, and which will
         * be passed to each array data object created initially, and arrays created
         * as the result of a convert_to() operation.  See geomEnums.h.
         *
         * However, each individual array may be replaced with a different array
         * object with an independent usage hint specified, so there is no guarantee
         * that the individual arrays all have the same usage_hint.
         */
        """
        pass

    def hasColumn(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_column(GeomVertexData self, const InternalName name)
        
        /**
         * Returns true if the data has the named column, false otherwise.  This is
         * really just a shortcut for asking the same thing from the format.
         */
        """
        pass

    def has_column(self, GeomVertexData_self, const_InternalName_name): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_column(GeomVertexData self, const InternalName name)
        
        /**
         * Returns true if the data has the named column, false otherwise.  This is
         * really just a shortcut for asking the same thing from the format.
         */
        """
        pass

    def modifyArray(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        modify_array(const GeomVertexData self, int i)
        
        /**
         * Returns a modifiable pointer to the indicated vertex array, so that
         * application code may directly manipulate the data.  You should avoid
         * changing the length of this array, since all of the arrays should be kept
         * in sync--use set_num_rows() instead.
         *
         * Don't call this in a downstream thread unless you don't mind it blowing
         * away other changes you might have recently made in an upstream thread.
         */
        """
        pass

    def modifyArrayHandle(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        modify_array_handle(const GeomVertexData self, int i)
        
        /**
         * Equivalent to modify_array(i).modify_handle().
         */
        """
        pass

    def modifyTransformBlendTable(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        modify_transform_blend_table(const GeomVertexData self)
        
        /**
         * Returns a modifiable pointer to the current TransformBlendTable on this
         * vertex data, if any, or NULL if there is not a TransformBlendTable.  See
         * get_transform_blend_table().
         *
         * Don't call this in a downstream thread unless you don't mind it blowing
         * away other changes you might have recently made in an upstream thread.
         */
        """
        pass

    def modify_array(self, const_GeomVertexData_self, int_i): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        modify_array(const GeomVertexData self, int i)
        
        /**
         * Returns a modifiable pointer to the indicated vertex array, so that
         * application code may directly manipulate the data.  You should avoid
         * changing the length of this array, since all of the arrays should be kept
         * in sync--use set_num_rows() instead.
         *
         * Don't call this in a downstream thread unless you don't mind it blowing
         * away other changes you might have recently made in an upstream thread.
         */
        """
        pass

    def modify_array_handle(self, const_GeomVertexData_self, int_i): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        modify_array_handle(const GeomVertexData self, int i)
        
        /**
         * Equivalent to modify_array(i).modify_handle().
         */
        """
        pass

    def modify_transform_blend_table(self, const_GeomVertexData_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        modify_transform_blend_table(const GeomVertexData self)
        
        /**
         * Returns a modifiable pointer to the current TransformBlendTable on this
         * vertex data, if any, or NULL if there is not a TransformBlendTable.  See
         * get_transform_blend_table().
         *
         * Don't call this in a downstream thread unless you don't mind it blowing
         * away other changes you might have recently made in an upstream thread.
         */
        """
        pass

    def output(self, GeomVertexData_self, ostream_out): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        output(GeomVertexData self, ostream out)
        
        /**
         *
         */
        """
        pass

    def replaceColumn(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        replace_column(GeomVertexData self, InternalName name, int num_components, int numeric_type, int contents)
        
        /**
         * Returns a new GeomVertexData object, suitable for modification, with the
         * indicated data type replaced with a new table filled with undefined values.
         * The new table will be added as a new array; if the old table was
         * interleaved with a previous array, the previous array will not be repacked.
         *
         * If num_components is 0, the indicated name is simply removed from the type,
         * without replacing it with anything else.
         */
        """
        pass

    def replace_column(self, GeomVertexData_self, InternalName_name, int_num_components, int_numeric_type, int_contents): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        replace_column(GeomVertexData self, InternalName name, int num_components, int numeric_type, int contents)
        
        /**
         * Returns a new GeomVertexData object, suitable for modification, with the
         * indicated data type replaced with a new table filled with undefined values.
         * The new table will be added as a new array; if the old table was
         * interleaved with a previous array, the previous array will not be repacked.
         *
         * If num_components is 0, the indicated name is simply removed from the type,
         * without replacing it with anything else.
         */
        """
        pass

    def requestResident(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        request_resident(GeomVertexData self)
        
        /**
         * Returns true if the vertex data is currently resident in memory.  If this
         * returns false, the vertex data will be brought back into memory shortly;
         * try again later.
         */
        """
        pass

    def request_resident(self, GeomVertexData_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        request_resident(GeomVertexData self)
        
        /**
         * Returns true if the vertex data is currently resident in memory.  If this
         * returns false, the vertex data will be brought back into memory shortly;
         * try again later.
         */
        """
        pass

    def reserveNumRows(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        reserve_num_rows(const GeomVertexData self, int n)
        
        /**
         * This ensures that enough memory space for n rows is allocated, so that you
         * may increase the number of rows to n without causing a new memory
         * allocation.  This is a performance optimization only; it is especially
         * useful when you know ahead of time that you will be adding n rows to the
         * data.
         *
         * If you know exactly how many rows you will be needing, it is significantly
         * faster to use set_num_rows() or unclean_set_num_rows() instead.
         */
        """
        pass

    def reserve_num_rows(self, const_GeomVertexData_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        reserve_num_rows(const GeomVertexData self, int n)
        
        /**
         * This ensures that enough memory space for n rows is allocated, so that you
         * may increase the number of rows to n without causing a new memory
         * allocation.  This is a performance optimization only; it is especially
         * useful when you know ahead of time that you will be adding n rows to the
         * data.
         *
         * If you know exactly how many rows you will be needing, it is significantly
         * faster to use set_num_rows() or unclean_set_num_rows() instead.
         */
        """
        pass

    def reverseNormals(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        reverse_normals(GeomVertexData self)
        
        /**
         * Returns a new GeomVertexData object with the normal data modified in-place,
         * so that each lighting normal is now facing in the opposite direction.
         *
         * If the vertex data does not include a normal column, this returns the
         * original GeomVertexData object, unchanged.
         */
        """
        pass

    def reverse_normals(self, GeomVertexData_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        reverse_normals(GeomVertexData self)
        
        /**
         * Returns a new GeomVertexData object with the normal data modified in-place,
         * so that each lighting normal is now facing in the opposite direction.
         *
         * If the vertex data does not include a normal column, this returns the
         * original GeomVertexData object, unchanged.
         */
        """
        pass

    def scaleColor(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        scale_color(GeomVertexData self, const LVecBase4f color_scale)
        scale_color(GeomVertexData self, const LVecBase4f color_scale, int num_components, int numeric_type, int contents)
        
        /**
         * Returns a new GeomVertexData object with the color table modified in-place
         * to apply the indicated scale.
         *
         * If the vertex data does not include a color column, a new one will not be
         * added.
         */
        
        /**
         * Returns a new GeomVertexData object with the color table replaced with a
         * new color table that has been scaled by the indicated value.  The new color
         * table will be added as a new array; if the old color table was interleaved
         * with a previous array, the previous array will not be repacked.
         */
        """
        pass

    def scale_color(self, GeomVertexData_self, const_LVecBase4f_color_scale): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        scale_color(GeomVertexData self, const LVecBase4f color_scale)
        scale_color(GeomVertexData self, const LVecBase4f color_scale, int num_components, int numeric_type, int contents)
        
        /**
         * Returns a new GeomVertexData object with the color table modified in-place
         * to apply the indicated scale.
         *
         * If the vertex data does not include a color column, a new one will not be
         * added.
         */
        
        /**
         * Returns a new GeomVertexData object with the color table replaced with a
         * new color table that has been scaled by the indicated value.  The new color
         * table will be added as a new array; if the old color table was interleaved
         * with a previous array, the previous array will not be repacked.
         */
        """
        pass

    def setArray(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_array(const GeomVertexData self, int i, const GeomVertexArrayData array)
        
        /**
         * Replaces the indicated vertex data array with a completely new array.  You
         * should be careful that the new array has the same length and format as the
         * old one, unless you know what you are doing.
         *
         * Don't call this in a downstream thread unless you don't mind it blowing
         * away other changes you might have recently made in an upstream thread.
         */
        """
        pass

    def setColor(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_color(GeomVertexData self, const LVecBase4f color)
        set_color(GeomVertexData self, const LVecBase4f color, int num_components, int numeric_type, int contents)
        
        /**
         * Returns a new GeomVertexData object with the color data modified in-place
         * with the new value.
         *
         * If the vertex data does not include a color column, a new one will not be
         * added.
         */
        
        /**
         * Returns a new GeomVertexData object with the color table replaced with a
         * new color table for which each vertex has the indicated value.  The new
         * color table will be added as a new array; if the old color table was
         * interleaved with a previous array, the previous array will not be repacked.
         */
        """
        pass

    def setFormat(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_format(const GeomVertexData self, const GeomVertexFormat format)
        
        /**
         * Changes the format of the vertex data.  If the data is not empty, this will
         * implicitly change every row to match the new format.
         *
         * Don't call this in a downstream thread unless you don't mind it blowing
         * away other changes you might have recently made in an upstream thread.
         */
        """
        pass

    def setName(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_name(const GeomVertexData self, str name)
        
        /**
         * Changes the name of the vertex data.  This name is reported on the PStats
         * graph for vertex computations.
         */
        """
        pass

    def setNumRows(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_num_rows(const GeomVertexData self, int n)
        
        /**
         * Sets the length of the array to n rows in all of the various arrays
         * (presumably by adding rows).
         *
         * The new vertex data is initialized to 0, except for the "color" column,
         * which is initialized to (1, 1, 1, 1).
         *
         * The return value is true if the number of rows was changed, false if the
         * object already contained n rows (or if there was some error).
         *
         * This can be used when you know exactly how many rows you will be needing.
         * It is faster than reserve_num_rows().  Also see unclean_set_num_rows() if
         * you are planning to fill in all the data yourself.
         *
         * Don't call this in a downstream thread unless you don't mind it blowing
         * away other changes you might have recently made in an upstream thread.
         */
        """
        pass

    def setSliderTable(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_slider_table(const GeomVertexData self, const SliderTable table)
        
        /**
         * Replaces the SliderTable on this vertex data with the indicated table.
         * There should be an entry in this table for each kind of morph offset
         * defined in the vertex data.
         *
         * The SliderTable object must have been registered prior to setting it on the
         * GeomVertexData.
         *
         * Don't call this in a downstream thread unless you don't mind it blowing
         * away other changes you might have recently made in an upstream thread.
         */
        """
        pass

    def setTransformBlendTable(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_transform_blend_table(const GeomVertexData self, const TransformBlendTable table)
        
        /**
         * Replaces the TransformBlendTable on this vertex data with the indicated
         * table.  The length of this table should be consistent with the maximum
         * table index assigned to the vertices under the "transform_blend" name.
         *
         * Don't call this in a downstream thread unless you don't mind it blowing
         * away other changes you might have recently made in an upstream thread.
         */
        """
        pass

    def setTransformTable(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_transform_table(const GeomVertexData self, const TransformTable table)
        
        /**
         * Replaces the TransformTable on this vertex data with the indicated table.
         * The length of this table should be consistent with the maximum table index
         * assigned to the vertices under the "transform_index" name.
         *
         * Don't call this in a downstream thread unless you don't mind it blowing
         * away other changes you might have recently made in an upstream thread.
         */
        """
        pass

    def setUsageHint(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_usage_hint(const GeomVertexData self, int usage_hint)
        
        /**
         * Changes the UsageHint hint for this vertex data, and for all of the arrays
         * that share this data.  See get_usage_hint().
         *
         * Don't call this in a downstream thread unless you don't mind it blowing
         * away other changes you might have recently made in an upstream thread.
         */
        """
        pass

    def set_array(self, const_GeomVertexData_self, int_i, const_GeomVertexArrayData_array): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_array(const GeomVertexData self, int i, const GeomVertexArrayData array)
        
        /**
         * Replaces the indicated vertex data array with a completely new array.  You
         * should be careful that the new array has the same length and format as the
         * old one, unless you know what you are doing.
         *
         * Don't call this in a downstream thread unless you don't mind it blowing
         * away other changes you might have recently made in an upstream thread.
         */
        """
        pass

    def set_color(self, GeomVertexData_self, const_LVecBase4f_color): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_color(GeomVertexData self, const LVecBase4f color)
        set_color(GeomVertexData self, const LVecBase4f color, int num_components, int numeric_type, int contents)
        
        /**
         * Returns a new GeomVertexData object with the color data modified in-place
         * with the new value.
         *
         * If the vertex data does not include a color column, a new one will not be
         * added.
         */
        
        /**
         * Returns a new GeomVertexData object with the color table replaced with a
         * new color table for which each vertex has the indicated value.  The new
         * color table will be added as a new array; if the old color table was
         * interleaved with a previous array, the previous array will not be repacked.
         */
        """
        pass

    def set_format(self, const_GeomVertexData_self, const_GeomVertexFormat_format): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_format(const GeomVertexData self, const GeomVertexFormat format)
        
        /**
         * Changes the format of the vertex data.  If the data is not empty, this will
         * implicitly change every row to match the new format.
         *
         * Don't call this in a downstream thread unless you don't mind it blowing
         * away other changes you might have recently made in an upstream thread.
         */
        """
        pass

    def set_name(self, const_GeomVertexData_self, str_name): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_name(const GeomVertexData self, str name)
        
        /**
         * Changes the name of the vertex data.  This name is reported on the PStats
         * graph for vertex computations.
         */
        """
        pass

    def set_num_rows(self, const_GeomVertexData_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_num_rows(const GeomVertexData self, int n)
        
        /**
         * Sets the length of the array to n rows in all of the various arrays
         * (presumably by adding rows).
         *
         * The new vertex data is initialized to 0, except for the "color" column,
         * which is initialized to (1, 1, 1, 1).
         *
         * The return value is true if the number of rows was changed, false if the
         * object already contained n rows (or if there was some error).
         *
         * This can be used when you know exactly how many rows you will be needing.
         * It is faster than reserve_num_rows().  Also see unclean_set_num_rows() if
         * you are planning to fill in all the data yourself.
         *
         * Don't call this in a downstream thread unless you don't mind it blowing
         * away other changes you might have recently made in an upstream thread.
         */
        """
        pass

    def set_slider_table(self, const_GeomVertexData_self, const_SliderTable_table): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_slider_table(const GeomVertexData self, const SliderTable table)
        
        /**
         * Replaces the SliderTable on this vertex data with the indicated table.
         * There should be an entry in this table for each kind of morph offset
         * defined in the vertex data.
         *
         * The SliderTable object must have been registered prior to setting it on the
         * GeomVertexData.
         *
         * Don't call this in a downstream thread unless you don't mind it blowing
         * away other changes you might have recently made in an upstream thread.
         */
        """
        pass

    def set_transform_blend_table(self, const_GeomVertexData_self, const_TransformBlendTable_table): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_transform_blend_table(const GeomVertexData self, const TransformBlendTable table)
        
        /**
         * Replaces the TransformBlendTable on this vertex data with the indicated
         * table.  The length of this table should be consistent with the maximum
         * table index assigned to the vertices under the "transform_blend" name.
         *
         * Don't call this in a downstream thread unless you don't mind it blowing
         * away other changes you might have recently made in an upstream thread.
         */
        """
        pass

    def set_transform_table(self, const_GeomVertexData_self, const_TransformTable_table): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_transform_table(const GeomVertexData self, const TransformTable table)
        
        /**
         * Replaces the TransformTable on this vertex data with the indicated table.
         * The length of this table should be consistent with the maximum table index
         * assigned to the vertices under the "transform_index" name.
         *
         * Don't call this in a downstream thread unless you don't mind it blowing
         * away other changes you might have recently made in an upstream thread.
         */
        """
        pass

    def set_usage_hint(self, const_GeomVertexData_self, int_usage_hint): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_usage_hint(const GeomVertexData self, int usage_hint)
        
        /**
         * Changes the UsageHint hint for this vertex data, and for all of the arrays
         * that share this data.  See get_usage_hint().
         *
         * Don't call this in a downstream thread unless you don't mind it blowing
         * away other changes you might have recently made in an upstream thread.
         */
        """
        pass

    def transformVertices(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        transform_vertices(const GeomVertexData self, const LMatrix4f mat)
        transform_vertices(const GeomVertexData self, const LMatrix4f mat, const SparseArray rows)
        transform_vertices(const GeomVertexData self, const LMatrix4f mat, int begin_row, int end_row)
        
        /**
         * Applies the indicated transform matrix to all of the vertices in the
         * GeomVertexData.  The transform is applied to all "point" and "vector" type
         * columns described in the format.
         */
        
        /**
         * Applies the indicated transform matrix to all of the vertices from
         * begin_row up to but not including end_row.  The transform is applied to all
         * "point" and "vector" type columns described in the format.
         */
        
        /**
         * Applies the indicated transform matrix to all of the vertices mentioned in
         * the sparse array.  The transform is applied to all "point" and "vector"
         * type columns described in the format.
         */
        """
        pass

    def transform_vertices(self, const_GeomVertexData_self, const_LMatrix4f_mat): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        transform_vertices(const GeomVertexData self, const LMatrix4f mat)
        transform_vertices(const GeomVertexData self, const LMatrix4f mat, const SparseArray rows)
        transform_vertices(const GeomVertexData self, const LMatrix4f mat, int begin_row, int end_row)
        
        /**
         * Applies the indicated transform matrix to all of the vertices in the
         * GeomVertexData.  The transform is applied to all "point" and "vector" type
         * columns described in the format.
         */
        
        /**
         * Applies the indicated transform matrix to all of the vertices from
         * begin_row up to but not including end_row.  The transform is applied to all
         * "point" and "vector" type columns described in the format.
         */
        
        /**
         * Applies the indicated transform matrix to all of the vertices mentioned in
         * the sparse array.  The transform is applied to all "point" and "vector"
         * type columns described in the format.
         */
        """
        pass

    def uncleanSetFormat(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        unclean_set_format(const GeomVertexData self, const GeomVertexFormat format)
        
        /**
         * Changes the format of the vertex data, without reformatting the data to
         * match.  The data is exactly the same after this operation, but will be
         * reinterpreted according to the new format.  This assumes that the new
         * format is fundamentally compatible with the old format; in particular, it
         * must have the same number of arrays with the same stride in each one.  No
         * checking is performed that the data remains sensible.
         */
        """
        pass

    def uncleanSetNumRows(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        unclean_set_num_rows(const GeomVertexData self, int n)
        
        /**
         * This method behaves like set_num_rows(), except the new data is not
         * initialized.  Furthermore, after this call, *any* of the data in the
         * GeomVertexData may be uninitialized, including the earlier rows.
         *
         * This is intended for applications that are about to completely fill the
         * GeomVertexData with new data anyway; it provides a tiny performance boost
         * over set_num_rows().
         *
         * This can be used when you know exactly how many rows you will be needing.
         * It is faster than reserve_num_rows().
         */
        """
        pass

    def unclean_set_format(self, const_GeomVertexData_self, const_GeomVertexFormat_format): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        unclean_set_format(const GeomVertexData self, const GeomVertexFormat format)
        
        /**
         * Changes the format of the vertex data, without reformatting the data to
         * match.  The data is exactly the same after this operation, but will be
         * reinterpreted according to the new format.  This assumes that the new
         * format is fundamentally compatible with the old format; in particular, it
         * must have the same number of arrays with the same stride in each one.  No
         * checking is performed that the data remains sensible.
         */
        """
        pass

    def unclean_set_num_rows(self, const_GeomVertexData_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        unclean_set_num_rows(const GeomVertexData self, int n)
        
        /**
         * This method behaves like set_num_rows(), except the new data is not
         * initialized.  Furthermore, after this call, *any* of the data in the
         * GeomVertexData may be uninitialized, including the earlier rows.
         *
         * This is intended for applications that are about to completely fill the
         * GeomVertexData with new data anyway; it provides a tiny performance boost
         * over set_num_rows().
         *
         * This can be used when you know exactly how many rows you will be needing.
         * It is faster than reserve_num_rows().
         */
        """
        pass

    def upcastToCopyOnWriteObject(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        upcast_to_CopyOnWriteObject(const GeomVertexData self)
        
        upcast from GeomVertexData to CopyOnWriteObject
        """
        pass

    def upcastToGeomEnums(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        upcast_to_GeomEnums(const GeomVertexData self)
        
        upcast from GeomVertexData to GeomEnums
        """
        pass

    def upcast_to_CopyOnWriteObject(self, const_GeomVertexData_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        upcast_to_CopyOnWriteObject(const GeomVertexData self)
        
        upcast from GeomVertexData to CopyOnWriteObject
        """
        pass

    def upcast_to_GeomEnums(self, const_GeomVertexData_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        upcast_to_GeomEnums(const GeomVertexData self)
        
        upcast from GeomVertexData to GeomEnums
        """
        pass

    def write(self, GeomVertexData_self, ostream_out, int_indent_level): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        write(GeomVertexData self, ostream out, int indent_level)
        
        /**
         *
         */
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

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    arrays = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    format = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    modified = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    num_bytes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    slider_table = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    transform_table = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    usage_hint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.core.GeomVertexData' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.core.GeomVertexData' objects>"
        '__doc__': '/**\n * This defines the actual numeric vertex data stored in a Geom, in the\n * structure defined by a particular GeomVertexFormat object.\n *\n * The data consists of one or more arrays, each of which in turn consists of\n * a series of rows, one per vertex.  All arrays should have the same number\n * of rows; each vertex is defined by the column data from a particular row\n * across all arrays.\n *\n * Often, there will be only one array per Geom, and the various columns\n * defined in the GeomVertexFormat will be interleaved within that array.\n * However, it is also possible to have multiple different arrays, with a\n * certain subset of the total columns defined in each array.\n *\n * However the data is distributed, the effect is of a single table of\n * vertices, where each vertex is represented by one row of the table.\n *\n * In general, application code should not attempt to directly manipulate the\n * vertex data through this structure; instead, use the GeomVertexReader,\n * GeomVertexWriter, and GeomVertexRewriter objects to read and write vertex\n * data at a high level.\n */',
        '__eq__': None, # (!) real value is "<slot wrapper '__eq__' of 'panda3d.core.GeomVertexData' objects>"
        '__ge__': None, # (!) real value is "<slot wrapper '__ge__' of 'panda3d.core.GeomVertexData' objects>"
        '__gt__': None, # (!) real value is "<slot wrapper '__gt__' of 'panda3d.core.GeomVertexData' objects>"
        '__hash__': None, # (!) real value is "<slot wrapper '__hash__' of 'panda3d.core.GeomVertexData' objects>"
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.GeomVertexData' objects>"
        '__le__': None, # (!) real value is "<slot wrapper '__le__' of 'panda3d.core.GeomVertexData' objects>"
        '__lt__': None, # (!) real value is "<slot wrapper '__lt__' of 'panda3d.core.GeomVertexData' objects>"
        '__ne__': None, # (!) real value is "<slot wrapper '__ne__' of 'panda3d.core.GeomVertexData' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE2FC390>'
        '__repr__': None, # (!) real value is "<slot wrapper '__repr__' of 'panda3d.core.GeomVertexData' objects>"
        '__str__': None, # (!) real value is "<slot wrapper '__str__' of 'panda3d.core.GeomVertexData' objects>"
        'animateVertices': None, # (!) real value is "<method 'animateVertices' of 'panda3d.core.GeomVertexData' objects>"
        'animate_vertices': None, # (!) real value is "<method 'animate_vertices' of 'panda3d.core.GeomVertexData' objects>"
        'arrays': None, # (!) real value is "<attribute 'arrays' of 'panda3d.core.GeomVertexData' objects>"
        'assign': None, # (!) real value is "<method 'assign' of 'panda3d.core.GeomVertexData' objects>"
        'clearAnimatedVertices': None, # (!) real value is "<method 'clearAnimatedVertices' of 'panda3d.core.GeomVertexData' objects>"
        'clearCache': None, # (!) real value is "<method 'clearCache' of 'panda3d.core.GeomVertexData' objects>"
        'clearCacheStage': None, # (!) real value is "<method 'clearCacheStage' of 'panda3d.core.GeomVertexData' objects>"
        'clearRows': None, # (!) real value is "<method 'clearRows' of 'panda3d.core.GeomVertexData' objects>"
        'clearSliderTable': None, # (!) real value is "<method 'clearSliderTable' of 'panda3d.core.GeomVertexData' objects>"
        'clearTransformBlendTable': None, # (!) real value is "<method 'clearTransformBlendTable' of 'panda3d.core.GeomVertexData' objects>"
        'clearTransformTable': None, # (!) real value is "<method 'clearTransformTable' of 'panda3d.core.GeomVertexData' objects>"
        'clear_animated_vertices': None, # (!) real value is "<method 'clear_animated_vertices' of 'panda3d.core.GeomVertexData' objects>"
        'clear_cache': None, # (!) real value is "<method 'clear_cache' of 'panda3d.core.GeomVertexData' objects>"
        'clear_cache_stage': None, # (!) real value is "<method 'clear_cache_stage' of 'panda3d.core.GeomVertexData' objects>"
        'clear_rows': None, # (!) real value is "<method 'clear_rows' of 'panda3d.core.GeomVertexData' objects>"
        'clear_slider_table': None, # (!) real value is "<method 'clear_slider_table' of 'panda3d.core.GeomVertexData' objects>"
        'clear_transform_blend_table': None, # (!) real value is "<method 'clear_transform_blend_table' of 'panda3d.core.GeomVertexData' objects>"
        'clear_transform_table': None, # (!) real value is "<method 'clear_transform_table' of 'panda3d.core.GeomVertexData' objects>"
        'compareTo': None, # (!) real value is "<method 'compareTo' of 'panda3d.core.GeomVertexData' objects>"
        'compare_to': None, # (!) real value is "<method 'compare_to' of 'panda3d.core.GeomVertexData' objects>"
        'convertTo': None, # (!) real value is "<method 'convertTo' of 'panda3d.core.GeomVertexData' objects>"
        'convert_to': None, # (!) real value is "<method 'convert_to' of 'panda3d.core.GeomVertexData' objects>"
        'copyFrom': None, # (!) real value is "<method 'copyFrom' of 'panda3d.core.GeomVertexData' objects>"
        'copyRowFrom': None, # (!) real value is "<method 'copyRowFrom' of 'panda3d.core.GeomVertexData' objects>"
        'copy_from': None, # (!) real value is "<method 'copy_from' of 'panda3d.core.GeomVertexData' objects>"
        'copy_row_from': None, # (!) real value is "<method 'copy_row_from' of 'panda3d.core.GeomVertexData' objects>"
        'describeVertex': None, # (!) real value is "<method 'describeVertex' of 'panda3d.core.GeomVertexData' objects>"
        'describe_vertex': None, # (!) real value is "<method 'describe_vertex' of 'panda3d.core.GeomVertexData' objects>"
        'format': None, # (!) real value is "<attribute 'format' of 'panda3d.core.GeomVertexData' objects>"
        'getArray': None, # (!) real value is "<method 'getArray' of 'panda3d.core.GeomVertexData' objects>"
        'getArrayHandle': None, # (!) real value is "<method 'getArrayHandle' of 'panda3d.core.GeomVertexData' objects>"
        'getArrays': None, # (!) real value is "<method 'getArrays' of 'panda3d.core.GeomVertexData' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE2FC390>)>'
        'getFormat': None, # (!) real value is "<method 'getFormat' of 'panda3d.core.GeomVertexData' objects>"
        'getModified': None, # (!) real value is "<method 'getModified' of 'panda3d.core.GeomVertexData' objects>"
        'getName': None, # (!) real value is "<method 'getName' of 'panda3d.core.GeomVertexData' objects>"
        'getNumArrays': None, # (!) real value is "<method 'getNumArrays' of 'panda3d.core.GeomVertexData' objects>"
        'getNumBytes': None, # (!) real value is "<method 'getNumBytes' of 'panda3d.core.GeomVertexData' objects>"
        'getNumRows': None, # (!) real value is "<method 'getNumRows' of 'panda3d.core.GeomVertexData' objects>"
        'getSliderTable': None, # (!) real value is "<method 'getSliderTable' of 'panda3d.core.GeomVertexData' objects>"
        'getTransformBlendTable': None, # (!) real value is "<method 'getTransformBlendTable' of 'panda3d.core.GeomVertexData' objects>"
        'getTransformTable': None, # (!) real value is "<method 'getTransformTable' of 'panda3d.core.GeomVertexData' objects>"
        'getUsageHint': None, # (!) real value is "<method 'getUsageHint' of 'panda3d.core.GeomVertexData' objects>"
        'get_array': None, # (!) real value is "<method 'get_array' of 'panda3d.core.GeomVertexData' objects>"
        'get_array_handle': None, # (!) real value is "<method 'get_array_handle' of 'panda3d.core.GeomVertexData' objects>"
        'get_arrays': None, # (!) real value is "<method 'get_arrays' of 'panda3d.core.GeomVertexData' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE2FC390>)>'
        'get_format': None, # (!) real value is "<method 'get_format' of 'panda3d.core.GeomVertexData' objects>"
        'get_modified': None, # (!) real value is "<method 'get_modified' of 'panda3d.core.GeomVertexData' objects>"
        'get_name': None, # (!) real value is "<method 'get_name' of 'panda3d.core.GeomVertexData' objects>"
        'get_num_arrays': None, # (!) real value is "<method 'get_num_arrays' of 'panda3d.core.GeomVertexData' objects>"
        'get_num_bytes': None, # (!) real value is "<method 'get_num_bytes' of 'panda3d.core.GeomVertexData' objects>"
        'get_num_rows': None, # (!) real value is "<method 'get_num_rows' of 'panda3d.core.GeomVertexData' objects>"
        'get_slider_table': None, # (!) real value is "<method 'get_slider_table' of 'panda3d.core.GeomVertexData' objects>"
        'get_transform_blend_table': None, # (!) real value is "<method 'get_transform_blend_table' of 'panda3d.core.GeomVertexData' objects>"
        'get_transform_table': None, # (!) real value is "<method 'get_transform_table' of 'panda3d.core.GeomVertexData' objects>"
        'get_usage_hint': None, # (!) real value is "<method 'get_usage_hint' of 'panda3d.core.GeomVertexData' objects>"
        'hasColumn': None, # (!) real value is "<method 'hasColumn' of 'panda3d.core.GeomVertexData' objects>"
        'has_column': None, # (!) real value is "<method 'has_column' of 'panda3d.core.GeomVertexData' objects>"
        'modified': None, # (!) real value is "<attribute 'modified' of 'panda3d.core.GeomVertexData' objects>"
        'modifyArray': None, # (!) real value is "<method 'modifyArray' of 'panda3d.core.GeomVertexData' objects>"
        'modifyArrayHandle': None, # (!) real value is "<method 'modifyArrayHandle' of 'panda3d.core.GeomVertexData' objects>"
        'modifyTransformBlendTable': None, # (!) real value is "<method 'modifyTransformBlendTable' of 'panda3d.core.GeomVertexData' objects>"
        'modify_array': None, # (!) real value is "<method 'modify_array' of 'panda3d.core.GeomVertexData' objects>"
        'modify_array_handle': None, # (!) real value is "<method 'modify_array_handle' of 'panda3d.core.GeomVertexData' objects>"
        'modify_transform_blend_table': None, # (!) real value is "<method 'modify_transform_blend_table' of 'panda3d.core.GeomVertexData' objects>"
        'name': None, # (!) real value is "<attribute 'name' of 'panda3d.core.GeomVertexData' objects>"
        'num_bytes': None, # (!) real value is "<attribute 'num_bytes' of 'panda3d.core.GeomVertexData' objects>"
        'output': None, # (!) real value is "<method 'output' of 'panda3d.core.GeomVertexData' objects>"
        'replaceColumn': None, # (!) real value is "<method 'replaceColumn' of 'panda3d.core.GeomVertexData' objects>"
        'replace_column': None, # (!) real value is "<method 'replace_column' of 'panda3d.core.GeomVertexData' objects>"
        'requestResident': None, # (!) real value is "<method 'requestResident' of 'panda3d.core.GeomVertexData' objects>"
        'request_resident': None, # (!) real value is "<method 'request_resident' of 'panda3d.core.GeomVertexData' objects>"
        'reserveNumRows': None, # (!) real value is "<method 'reserveNumRows' of 'panda3d.core.GeomVertexData' objects>"
        'reserve_num_rows': None, # (!) real value is "<method 'reserve_num_rows' of 'panda3d.core.GeomVertexData' objects>"
        'reverseNormals': None, # (!) real value is "<method 'reverseNormals' of 'panda3d.core.GeomVertexData' objects>"
        'reverse_normals': None, # (!) real value is "<method 'reverse_normals' of 'panda3d.core.GeomVertexData' objects>"
        'scaleColor': None, # (!) real value is "<method 'scaleColor' of 'panda3d.core.GeomVertexData' objects>"
        'scale_color': None, # (!) real value is "<method 'scale_color' of 'panda3d.core.GeomVertexData' objects>"
        'setArray': None, # (!) real value is "<method 'setArray' of 'panda3d.core.GeomVertexData' objects>"
        'setColor': None, # (!) real value is "<method 'setColor' of 'panda3d.core.GeomVertexData' objects>"
        'setFormat': None, # (!) real value is "<method 'setFormat' of 'panda3d.core.GeomVertexData' objects>"
        'setName': None, # (!) real value is "<method 'setName' of 'panda3d.core.GeomVertexData' objects>"
        'setNumRows': None, # (!) real value is "<method 'setNumRows' of 'panda3d.core.GeomVertexData' objects>"
        'setSliderTable': None, # (!) real value is "<method 'setSliderTable' of 'panda3d.core.GeomVertexData' objects>"
        'setTransformBlendTable': None, # (!) real value is "<method 'setTransformBlendTable' of 'panda3d.core.GeomVertexData' objects>"
        'setTransformTable': None, # (!) real value is "<method 'setTransformTable' of 'panda3d.core.GeomVertexData' objects>"
        'setUsageHint': None, # (!) real value is "<method 'setUsageHint' of 'panda3d.core.GeomVertexData' objects>"
        'set_array': None, # (!) real value is "<method 'set_array' of 'panda3d.core.GeomVertexData' objects>"
        'set_color': None, # (!) real value is "<method 'set_color' of 'panda3d.core.GeomVertexData' objects>"
        'set_format': None, # (!) real value is "<method 'set_format' of 'panda3d.core.GeomVertexData' objects>"
        'set_name': None, # (!) real value is "<method 'set_name' of 'panda3d.core.GeomVertexData' objects>"
        'set_num_rows': None, # (!) real value is "<method 'set_num_rows' of 'panda3d.core.GeomVertexData' objects>"
        'set_slider_table': None, # (!) real value is "<method 'set_slider_table' of 'panda3d.core.GeomVertexData' objects>"
        'set_transform_blend_table': None, # (!) real value is "<method 'set_transform_blend_table' of 'panda3d.core.GeomVertexData' objects>"
        'set_transform_table': None, # (!) real value is "<method 'set_transform_table' of 'panda3d.core.GeomVertexData' objects>"
        'set_usage_hint': None, # (!) real value is "<method 'set_usage_hint' of 'panda3d.core.GeomVertexData' objects>"
        'slider_table': None, # (!) real value is "<attribute 'slider_table' of 'panda3d.core.GeomVertexData' objects>"
        'transformVertices': None, # (!) real value is "<method 'transformVertices' of 'panda3d.core.GeomVertexData' objects>"
        'transform_table': None, # (!) real value is "<attribute 'transform_table' of 'panda3d.core.GeomVertexData' objects>"
        'transform_vertices': None, # (!) real value is "<method 'transform_vertices' of 'panda3d.core.GeomVertexData' objects>"
        'uncleanSetFormat': None, # (!) real value is "<method 'uncleanSetFormat' of 'panda3d.core.GeomVertexData' objects>"
        'uncleanSetNumRows': None, # (!) real value is "<method 'uncleanSetNumRows' of 'panda3d.core.GeomVertexData' objects>"
        'unclean_set_format': None, # (!) real value is "<method 'unclean_set_format' of 'panda3d.core.GeomVertexData' objects>"
        'unclean_set_num_rows': None, # (!) real value is "<method 'unclean_set_num_rows' of 'panda3d.core.GeomVertexData' objects>"
        'upcastToCopyOnWriteObject': None, # (!) real value is "<method 'upcastToCopyOnWriteObject' of 'panda3d.core.GeomVertexData' objects>"
        'upcastToGeomEnums': None, # (!) real value is "<method 'upcastToGeomEnums' of 'panda3d.core.GeomVertexData' objects>"
        'upcast_to_CopyOnWriteObject': None, # (!) real value is "<method 'upcast_to_CopyOnWriteObject' of 'panda3d.core.GeomVertexData' objects>"
        'upcast_to_GeomEnums': None, # (!) real value is "<method 'upcast_to_GeomEnums' of 'panda3d.core.GeomVertexData' objects>"
        'usage_hint': None, # (!) real value is "<attribute 'usage_hint' of 'panda3d.core.GeomVertexData' objects>"
        'write': None, # (!) real value is "<method 'write' of 'panda3d.core.GeomVertexData' objects>"
    }


