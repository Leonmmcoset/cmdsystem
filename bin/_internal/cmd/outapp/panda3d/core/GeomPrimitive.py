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

class GeomPrimitive(CopyOnWriteObject, GeomEnums):
    """
    /**
     * This is an abstract base class for a family of classes that represent the
     * fundamental geometry primitives that may be stored in a Geom.
     *
     * They all have in common the fact that they are defined by tables of vertex
     * data stored in a GeomVertexData object.  Each GeomPrimitive object contains
     * an ordered list of integers, which index into the vertex array defined by
     * the GeomVertexData and define the particular vertices of the GeomVertexData
     * that are used for this primitive.
     *
     * The meaning of a given arrangement of vertices is defined by each
     * individual primitive type; for instance, a GeomTriangle renders a triangle
     * from each three consecutive vertices, while a GeomTriangleStrip renders a
     * strip of (n - 2) connected triangles from each sequence of n vertices.
     */
    """
    def addConsecutiveVertices(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_consecutive_vertices(const GeomPrimitive self, int start, int num_vertices)
        
        /**
         * Adds a consecutive sequence of vertices, beginning at start, to the
         * primitive.
         *
         * Don't call this in a downstream thread unless you don't mind it blowing
         * away other changes you might have recently made in an upstream thread.
         */
        """
        pass

    def addNextVertices(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_next_vertices(const GeomPrimitive self, int num_vertices)
        
        /**
         * Adds the next n vertices in sequence, beginning from the last vertex added
         * to the primitive + 1.
         *
         * This is most useful when you are building up a primitive and a
         * GeomVertexData at the same time, and you just want the primitive to
         * reference the first n vertices from the data, then the next n, and so on.
         */
        """
        pass

    def addVertex(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_vertex(const GeomPrimitive self, int vertex)
        
        /**
         * Adds the indicated vertex to the list of vertex indices used by the
         * graphics primitive type.  To define a primitive, you must call add_vertex()
         * for each vertex of the new primitive, and then call close_primitive() after
         * you have specified the last vertex of each primitive.
         *
         * Don't call this in a downstream thread unless you don't mind it blowing
         * away other changes you might have recently made in an upstream thread.
         */
        """
        pass

    def addVertices(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_vertices(const GeomPrimitive self, int v1, int v2)
        add_vertices(const GeomPrimitive self, int v1, int v2, int v3)
        add_vertices(const GeomPrimitive self, int v1, int v2, int v3, int v4)
        
        /**
         * Adds several vertices in a row.
         */
        
        /**
         * Adds several vertices in a row.
         */
        
        /**
         * Adds several vertices in a row.
         */
        """
        pass

    def add_consecutive_vertices(self, const_GeomPrimitive_self, int_start, int_num_vertices): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_consecutive_vertices(const GeomPrimitive self, int start, int num_vertices)
        
        /**
         * Adds a consecutive sequence of vertices, beginning at start, to the
         * primitive.
         *
         * Don't call this in a downstream thread unless you don't mind it blowing
         * away other changes you might have recently made in an upstream thread.
         */
        """
        pass

    def add_next_vertices(self, const_GeomPrimitive_self, int_num_vertices): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_next_vertices(const GeomPrimitive self, int num_vertices)
        
        /**
         * Adds the next n vertices in sequence, beginning from the last vertex added
         * to the primitive + 1.
         *
         * This is most useful when you are building up a primitive and a
         * GeomVertexData at the same time, and you just want the primitive to
         * reference the first n vertices from the data, then the next n, and so on.
         */
        """
        pass

    def add_vertex(self, const_GeomPrimitive_self, int_vertex): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_vertex(const GeomPrimitive self, int vertex)
        
        /**
         * Adds the indicated vertex to the list of vertex indices used by the
         * graphics primitive type.  To define a primitive, you must call add_vertex()
         * for each vertex of the new primitive, and then call close_primitive() after
         * you have specified the last vertex of each primitive.
         *
         * Don't call this in a downstream thread unless you don't mind it blowing
         * away other changes you might have recently made in an upstream thread.
         */
        """
        pass

    def add_vertices(self, const_GeomPrimitive_self, int_v1, int_v2): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_vertices(const GeomPrimitive self, int v1, int v2)
        add_vertices(const GeomPrimitive self, int v1, int v2, int v3)
        add_vertices(const GeomPrimitive self, int v1, int v2, int v3, int v4)
        
        /**
         * Adds several vertices in a row.
         */
        
        /**
         * Adds several vertices in a row.
         */
        
        /**
         * Adds several vertices in a row.
         */
        """
        pass

    def assign(self, const_GeomPrimitive_self, const_GeomPrimitive_copy): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        assign(const GeomPrimitive self, const GeomPrimitive copy)
        """
        pass

    def checkValid(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        check_valid(GeomPrimitive self, const GeomVertexData vertex_data)
        
        /**
         * Verifies that the primitive only references vertices that actually exist
         * within the indicated GeomVertexData.  Returns true if the primitive appears
         * to be valid, false otherwise.
         */
        
        /**
         *
         */
        """
        pass

    def check_valid(self, GeomPrimitive_self, const_GeomVertexData_vertex_data): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        check_valid(GeomPrimitive self, const GeomVertexData vertex_data)
        
        /**
         * Verifies that the primitive only references vertices that actually exist
         * within the indicated GeomVertexData.  Returns true if the primitive appears
         * to be valid, false otherwise.
         */
        
        /**
         *
         */
        """
        pass

    def clearMinmax(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_minmax(const GeomPrimitive self)
        
        /**
         * Undoes a previous call to set_minmax(), and allows the minimum and maximum
         * values to be recomputed normally.
         *
         * This method is intended for low-level usage only.  There are higher-level
         * methods for more common usage.  We recommend you do not use this method
         * directly.  If you do, be sure you know what you are doing!
         */
        """
        pass

    def clearVertices(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_vertices(const GeomPrimitive self)
        
        /**
         * Removes all of the vertices and primitives from the object, so they can be
         * re-added.
         *
         * Don't call this in a downstream thread unless you don't mind it blowing
         * away other changes you might have recently made in an upstream thread.
         */
        """
        pass

    def clear_minmax(self, const_GeomPrimitive_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_minmax(const GeomPrimitive self)
        
        /**
         * Undoes a previous call to set_minmax(), and allows the minimum and maximum
         * values to be recomputed normally.
         *
         * This method is intended for low-level usage only.  There are higher-level
         * methods for more common usage.  We recommend you do not use this method
         * directly.  If you do, be sure you know what you are doing!
         */
        """
        pass

    def clear_vertices(self, const_GeomPrimitive_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_vertices(const GeomPrimitive self)
        
        /**
         * Removes all of the vertices and primitives from the object, so they can be
         * re-added.
         *
         * Don't call this in a downstream thread unless you don't mind it blowing
         * away other changes you might have recently made in an upstream thread.
         */
        """
        pass

    def closePrimitive(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        close_primitive(const GeomPrimitive self)
        
        /**
         * Indicates that the previous n calls to add_vertex(), since the last call to
         * close_primitive(), have fully defined a new primitive.  Returns true if
         * successful, false otherwise.
         *
         * Don't call this in a downstream thread unless you don't mind it blowing
         * away other changes you might have recently made in an upstream thread.
         */
        """
        pass

    def close_primitive(self, const_GeomPrimitive_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        close_primitive(const GeomPrimitive self)
        
        /**
         * Indicates that the previous n calls to add_vertex(), since the last call to
         * close_primitive(), have fully defined a new primitive.  Returns true if
         * successful, false otherwise.
         *
         * Don't call this in a downstream thread unless you don't mind it blowing
         * away other changes you might have recently made in an upstream thread.
         */
        """
        pass

    def decompose(self, GeomPrimitive_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        decompose(GeomPrimitive self)
        
        /**
         * Decomposes a complex primitive type into a simpler primitive type, for
         * instance triangle strips to triangles, and returns a pointer to the new
         * primitive definition.  If the decomposition cannot be performed, this might
         * return the original object.
         *
         * This method is useful for application code that wants to iterate through
         * the set of triangles on the primitive without having to write handlers for
         * each possible kind of primitive type.
         */
        """
        pass

    def doubleside(self, GeomPrimitive_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        doubleside(GeomPrimitive self)
        
        /**
         * Duplicates triangles in the primitive so that each triangle is back-to-back
         * with another triangle facing in the opposite direction.  Note that this
         * doesn't affect vertex normals, so this operation alone won't work in the
         * presence of lighting (but see SceneGraphReducer::doubleside()).
         *
         * Also see CullFaceAttrib, which can enable rendering of both sides of a
         * triangle without having to duplicate it (but which doesn't necessarily work
         * in the presence of lighting).
         */
        """
        pass

    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getDataSizeBytes(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_data_size_bytes(GeomPrimitive self)
        
        /**
         * Returns the number of bytes stored in the vertices array.
         */
        """
        pass

    def getEnds(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_ends(GeomPrimitive self)
        
        /**
         * Returns a const pointer to the primitive ends array so application code can
         * read it directly.  Do not attempt to modify the returned array; use
         * modify_ends() or set_ends() for this.
         *
         * Note that simple primitive types, like triangles, do not have a ends array:
         * since all the primitives have the same number of vertices, it is not
         * needed.
         *
         * This method is intended for low-level usage only.  There are higher-level
         * methods for more common usage.  We recommend you do not use this method
         * directly.  If you do, be sure you know what you are doing!
         */
        """
        pass

    def getFirstVertex(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_first_vertex(GeomPrimitive self)
        
        /**
         * Returns the first vertex number referenced by the primitive.  This is
         * particularly important in the case of a nonindexed primitive, in which case
         * get_first_vertex() and get_num_vertices() completely define the extent of
         * the vertex range.
         */
        """
        pass

    def getGeomRendering(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_geom_rendering(GeomPrimitive self)
        
        /**
         * Returns the set of GeomRendering bits that represent the rendering
         * properties required to properly render this primitive.
         */
        """
        pass

    def getIndexStride(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_index_stride(GeomPrimitive self)
        
        /**
         * A convenience function to return the gap between successive index numbers,
         * in bytes, of the index data.
         *
         * This method is intended for low-level usage only.  There are higher-level
         * methods for more common usage.  We recommend you do not use this method
         * directly.  If you do, be sure you know what you are doing!
         */
        """
        pass

    def getIndexType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_index_type(GeomPrimitive self)
        
        /**
         * Returns the numeric type of the index column.  Normally, this will be
         * either NT_uint16 or NT_uint32.
         */
        """
        pass

    def getMaxs(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_maxs(GeomPrimitive self)
        
        /**
         * Returns a const pointer to the primitive maxs array so application code can
         * read it directly.  Do not attempt to modify the returned array; use
         * set_minmax().
         *
         * Note that simple primitive types, like triangles, do not have a maxs array.
         *
         * This method is intended for low-level usage only.  There are higher-level
         * methods for more common usage.  We recommend you do not use this method
         * directly.  If you do, be sure you know what you are doing!
         */
        """
        pass

    def getMaxVertex(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_max_vertex(GeomPrimitive self)
        
        /**
         * Returns the maximum vertex index number used by all the primitives in this
         * object.
         */
        """
        pass

    def getMinNumVerticesPerPrimitive(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_min_num_vertices_per_primitive(GeomPrimitive self)
        
        /**
         * Returns the minimum number of vertices that must be added before
         * close_primitive() may legally be called.
         *
         * This method is intended for low-level usage only.  There are higher-level
         * methods for more common usage.  We recommend you do not use this method
         * directly.  If you do, be sure you know what you are doing!
         */
        """
        pass

    def getMins(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_mins(GeomPrimitive self)
        
        /**
         * Returns a const pointer to the primitive mins array so application code can
         * read it directly.  Do not attempt to modify the returned array; use
         * set_minmax() for this.
         *
         * Note that simple primitive types, like triangles, do not have a mins array.
         *
         * This method is intended for low-level usage only.  There are higher-level
         * methods for more common usage.  We recommend you do not use this method
         * directly.  If you do, be sure you know what you are doing!
         */
        """
        pass

    def getMinVertex(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_min_vertex(GeomPrimitive self)
        
        /**
         * Returns the minimum vertex index number used by all the primitives in this
         * object.
         */
        """
        pass

    def getModified(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_modified(GeomPrimitive self)
        
        /**
         * Returns a sequence number which is guaranteed to change at least every time
         * the vertex index array is modified.
         */
        """
        pass

    def getNumBytes(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_bytes(GeomPrimitive self)
        
        /**
         * Returns the number of bytes consumed by the primitive and its index
         * table(s).
         */
        """
        pass

    def getNumFaces(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_faces(GeomPrimitive self)
        
        /**
         * Returns the number of triangles or other fundamental type (such as line
         * segments) represented by all the primitives in this object.
         */
        """
        pass

    def getNumPrimitives(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_primitives(GeomPrimitive self)
        
        /**
         * Returns the number of individual primitives stored within this object.  All
         * primitives are the same type.
         */
        """
        pass

    def getNumUnusedVerticesPerPrimitive(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_unused_vertices_per_primitive(GeomPrimitive self)
        
        /**
         * Returns the number of vertices that are added between primitives that
         * aren't, strictly speaking, part of the primitives themselves.  This is
         * used, for instance, to define degenerate triangles to connect otherwise
         * disconnected triangle strips.
         *
         * This method is intended for low-level usage only.  There are higher-level
         * methods for more common usage.  We recommend you do not use this method
         * directly.  If you do, be sure you know what you are doing!
         */
        """
        pass

    def getNumUsedVertices(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_used_vertices(GeomPrimitive self)
        
        /**
         * Returns the number of vertices used by all of the primitives.  This is the
         * same as summing get_primitive_num_vertices(n) for n in
         * get_num_primitives().  It is like get_num_vertices except that it excludes
         * all of the degenerate vertices and strip-cut indices.
         */
        """
        pass

    def getNumVertices(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_vertices(GeomPrimitive self)
        
        /**
         * Returns the number of indices used by all the primitives in this object.
         */
        """
        pass

    def getNumVerticesPerPrimitive(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_vertices_per_primitive(GeomPrimitive self)
        
        /**
         * If the primitive type is a simple type in which all primitives have the
         * same number of vertices, like triangles, returns the number of vertices per
         * primitive.  If the primitive type is a more complex type in which different
         * primitives might have different numbers of vertices, for instance a
         * triangle strip, returns 0.
         *
         * This method is intended for low-level usage only.  There are higher-level
         * methods for more common usage.  We recommend you do not use this method
         * directly.  If you do, be sure you know what you are doing!
         */
        """
        pass

    def getPrimitiveEnd(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_primitive_end(GeomPrimitive self, int n)
        
        /**
         * Returns the element within the _vertices list at which the nth primitive
         * ends.  This is one past the last valid element for the nth primitive.
         */
        """
        pass

    def getPrimitiveMaxVertex(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_primitive_max_vertex(GeomPrimitive self, int n)
        
        /**
         * Returns the maximum vertex index number used by the nth primitive in this
         * object.
         */
        """
        pass

    def getPrimitiveMinVertex(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_primitive_min_vertex(GeomPrimitive self, int n)
        
        /**
         * Returns the minimum vertex index number used by the nth primitive in this
         * object.
         */
        """
        pass

    def getPrimitiveNumFaces(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_primitive_num_faces(GeomPrimitive self, int n)
        
        /**
         * Returns the number of triangles or other fundamental type (such as line
         * segments) represented by the nth primitive in this object.
         */
        """
        pass

    def getPrimitiveNumVertices(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_primitive_num_vertices(GeomPrimitive self, int n)
        
        /**
         * Returns the number of vertices used by the nth primitive.  This is the same
         * thing as get_primitive_end(n) - get_primitive_start(n).
         */
        """
        pass

    def getPrimitiveStart(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_primitive_start(GeomPrimitive self, int n)
        
        /**
         * Returns the element within the _vertices list at which the nth primitive
         * starts.
         *
         * If i is one more than the highest valid primitive vertex, the return value
         * will be one more than the last valid vertex.  Thus, it is generally true
         * that the vertices used by a particular primitive i are the set
         * get_primitive_start(n) <= vi < get_primitive_start(n + 1) (although this
         * range also includes the unused vertices between primitives).
         */
        """
        pass

    def getPrimitiveType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_primitive_type(GeomPrimitive self)
        """
        pass

    def getShadeModel(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_shade_model(GeomPrimitive self)
        
        /**
         * Returns the ShadeModel hint for this primitive.  This is intended as a hint
         * to the renderer to tell it how the per-vertex colors and normals are
         * applied.
         */
        """
        pass

    def getStripCutIndex(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_strip_cut_index(GeomPrimitive self)
        
        /**
         * If relevant, returns the index value that may be used in some cases to
         * signify the end of a primitive.  This is typically the highest value that
         * the numeric type can store.
         */
        
        /**
         * Returns the index of the indicated type that is reserved for use as a strip
         * cut index, if enabled for the primitive.  When the renderer encounters this
         * index, it will restart the primitive.  This is guaranteed not to point to
         * an actual vertex.
         */
        """
        pass

    def getUsageHint(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_usage_hint(GeomPrimitive self)
        
        /**
         * Returns the usage hint for this primitive.  See geomEnums.h.  This has
         * nothing to do with the usage hint associated with the primitive's vertices;
         * this only specifies how often the vertex indices that define the primitive
         * will be modified.
         *
         * It is perfectly legal (and, in fact, common) for a GeomPrimitive to have
         * UH_static on itself, while referencing vertex data with UH_dynamic.  This
         * means that the vertices themselves will be animated, but the primitive will
         * always reference the same set of vertices from the pool.
         */
        """
        pass

    def getVertex(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_vertex(GeomPrimitive self, int i)
        
        /**
         * Returns the ith vertex index in the table.
         */
        """
        pass

    def getVertexList(self, *args, **kwargs): # real signature unknown
        pass

    def getVertices(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_vertices(GeomPrimitive self)
        
        /**
         * Returns a const pointer to the vertex index array so application code can
         * read it directly.  This might return NULL if the primitive is nonindexed.
         * Do not attempt to modify the returned array; use modify_vertices() or
         * set_vertices() for this.
         *
         * This method is intended for low-level usage only.  There are higher-level
         * methods for more common usage.  We recommend you do not use this method
         * directly.  If you do, be sure you know what you are doing!
         */
        """
        pass

    def getVerticesHandle(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_vertices_handle(GeomPrimitive self, Thread current_thread)
        
        /**
         * Equivalent to get_vertices().get_handle().
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_data_size_bytes(self, GeomPrimitive_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_data_size_bytes(GeomPrimitive self)
        
        /**
         * Returns the number of bytes stored in the vertices array.
         */
        """
        pass

    def get_ends(self, GeomPrimitive_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_ends(GeomPrimitive self)
        
        /**
         * Returns a const pointer to the primitive ends array so application code can
         * read it directly.  Do not attempt to modify the returned array; use
         * modify_ends() or set_ends() for this.
         *
         * Note that simple primitive types, like triangles, do not have a ends array:
         * since all the primitives have the same number of vertices, it is not
         * needed.
         *
         * This method is intended for low-level usage only.  There are higher-level
         * methods for more common usage.  We recommend you do not use this method
         * directly.  If you do, be sure you know what you are doing!
         */
        """
        pass

    def get_first_vertex(self, GeomPrimitive_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_first_vertex(GeomPrimitive self)
        
        /**
         * Returns the first vertex number referenced by the primitive.  This is
         * particularly important in the case of a nonindexed primitive, in which case
         * get_first_vertex() and get_num_vertices() completely define the extent of
         * the vertex range.
         */
        """
        pass

    def get_geom_rendering(self, GeomPrimitive_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_geom_rendering(GeomPrimitive self)
        
        /**
         * Returns the set of GeomRendering bits that represent the rendering
         * properties required to properly render this primitive.
         */
        """
        pass

    def get_index_stride(self, GeomPrimitive_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_index_stride(GeomPrimitive self)
        
        /**
         * A convenience function to return the gap between successive index numbers,
         * in bytes, of the index data.
         *
         * This method is intended for low-level usage only.  There are higher-level
         * methods for more common usage.  We recommend you do not use this method
         * directly.  If you do, be sure you know what you are doing!
         */
        """
        pass

    def get_index_type(self, GeomPrimitive_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_index_type(GeomPrimitive self)
        
        /**
         * Returns the numeric type of the index column.  Normally, this will be
         * either NT_uint16 or NT_uint32.
         */
        """
        pass

    def get_maxs(self, GeomPrimitive_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_maxs(GeomPrimitive self)
        
        /**
         * Returns a const pointer to the primitive maxs array so application code can
         * read it directly.  Do not attempt to modify the returned array; use
         * set_minmax().
         *
         * Note that simple primitive types, like triangles, do not have a maxs array.
         *
         * This method is intended for low-level usage only.  There are higher-level
         * methods for more common usage.  We recommend you do not use this method
         * directly.  If you do, be sure you know what you are doing!
         */
        """
        pass

    def get_max_vertex(self, GeomPrimitive_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_max_vertex(GeomPrimitive self)
        
        /**
         * Returns the maximum vertex index number used by all the primitives in this
         * object.
         */
        """
        pass

    def get_mins(self, GeomPrimitive_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_mins(GeomPrimitive self)
        
        /**
         * Returns a const pointer to the primitive mins array so application code can
         * read it directly.  Do not attempt to modify the returned array; use
         * set_minmax() for this.
         *
         * Note that simple primitive types, like triangles, do not have a mins array.
         *
         * This method is intended for low-level usage only.  There are higher-level
         * methods for more common usage.  We recommend you do not use this method
         * directly.  If you do, be sure you know what you are doing!
         */
        """
        pass

    def get_min_num_vertices_per_primitive(self, GeomPrimitive_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_min_num_vertices_per_primitive(GeomPrimitive self)
        
        /**
         * Returns the minimum number of vertices that must be added before
         * close_primitive() may legally be called.
         *
         * This method is intended for low-level usage only.  There are higher-level
         * methods for more common usage.  We recommend you do not use this method
         * directly.  If you do, be sure you know what you are doing!
         */
        """
        pass

    def get_min_vertex(self, GeomPrimitive_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_min_vertex(GeomPrimitive self)
        
        /**
         * Returns the minimum vertex index number used by all the primitives in this
         * object.
         */
        """
        pass

    def get_modified(self, GeomPrimitive_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_modified(GeomPrimitive self)
        
        /**
         * Returns a sequence number which is guaranteed to change at least every time
         * the vertex index array is modified.
         */
        """
        pass

    def get_num_bytes(self, GeomPrimitive_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_bytes(GeomPrimitive self)
        
        /**
         * Returns the number of bytes consumed by the primitive and its index
         * table(s).
         */
        """
        pass

    def get_num_faces(self, GeomPrimitive_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_faces(GeomPrimitive self)
        
        /**
         * Returns the number of triangles or other fundamental type (such as line
         * segments) represented by all the primitives in this object.
         */
        """
        pass

    def get_num_primitives(self, GeomPrimitive_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_primitives(GeomPrimitive self)
        
        /**
         * Returns the number of individual primitives stored within this object.  All
         * primitives are the same type.
         */
        """
        pass

    def get_num_unused_vertices_per_primitive(self, GeomPrimitive_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_unused_vertices_per_primitive(GeomPrimitive self)
        
        /**
         * Returns the number of vertices that are added between primitives that
         * aren't, strictly speaking, part of the primitives themselves.  This is
         * used, for instance, to define degenerate triangles to connect otherwise
         * disconnected triangle strips.
         *
         * This method is intended for low-level usage only.  There are higher-level
         * methods for more common usage.  We recommend you do not use this method
         * directly.  If you do, be sure you know what you are doing!
         */
        """
        pass

    def get_num_used_vertices(self, GeomPrimitive_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_used_vertices(GeomPrimitive self)
        
        /**
         * Returns the number of vertices used by all of the primitives.  This is the
         * same as summing get_primitive_num_vertices(n) for n in
         * get_num_primitives().  It is like get_num_vertices except that it excludes
         * all of the degenerate vertices and strip-cut indices.
         */
        """
        pass

    def get_num_vertices(self, GeomPrimitive_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_vertices(GeomPrimitive self)
        
        /**
         * Returns the number of indices used by all the primitives in this object.
         */
        """
        pass

    def get_num_vertices_per_primitive(self, GeomPrimitive_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_vertices_per_primitive(GeomPrimitive self)
        
        /**
         * If the primitive type is a simple type in which all primitives have the
         * same number of vertices, like triangles, returns the number of vertices per
         * primitive.  If the primitive type is a more complex type in which different
         * primitives might have different numbers of vertices, for instance a
         * triangle strip, returns 0.
         *
         * This method is intended for low-level usage only.  There are higher-level
         * methods for more common usage.  We recommend you do not use this method
         * directly.  If you do, be sure you know what you are doing!
         */
        """
        pass

    def get_primitive_end(self, GeomPrimitive_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_primitive_end(GeomPrimitive self, int n)
        
        /**
         * Returns the element within the _vertices list at which the nth primitive
         * ends.  This is one past the last valid element for the nth primitive.
         */
        """
        pass

    def get_primitive_max_vertex(self, GeomPrimitive_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_primitive_max_vertex(GeomPrimitive self, int n)
        
        /**
         * Returns the maximum vertex index number used by the nth primitive in this
         * object.
         */
        """
        pass

    def get_primitive_min_vertex(self, GeomPrimitive_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_primitive_min_vertex(GeomPrimitive self, int n)
        
        /**
         * Returns the minimum vertex index number used by the nth primitive in this
         * object.
         */
        """
        pass

    def get_primitive_num_faces(self, GeomPrimitive_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_primitive_num_faces(GeomPrimitive self, int n)
        
        /**
         * Returns the number of triangles or other fundamental type (such as line
         * segments) represented by the nth primitive in this object.
         */
        """
        pass

    def get_primitive_num_vertices(self, GeomPrimitive_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_primitive_num_vertices(GeomPrimitive self, int n)
        
        /**
         * Returns the number of vertices used by the nth primitive.  This is the same
         * thing as get_primitive_end(n) - get_primitive_start(n).
         */
        """
        pass

    def get_primitive_start(self, GeomPrimitive_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_primitive_start(GeomPrimitive self, int n)
        
        /**
         * Returns the element within the _vertices list at which the nth primitive
         * starts.
         *
         * If i is one more than the highest valid primitive vertex, the return value
         * will be one more than the last valid vertex.  Thus, it is generally true
         * that the vertices used by a particular primitive i are the set
         * get_primitive_start(n) <= vi < get_primitive_start(n + 1) (although this
         * range also includes the unused vertices between primitives).
         */
        """
        pass

    def get_primitive_type(self, GeomPrimitive_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_primitive_type(GeomPrimitive self)
        """
        pass

    def get_shade_model(self, GeomPrimitive_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_shade_model(GeomPrimitive self)
        
        /**
         * Returns the ShadeModel hint for this primitive.  This is intended as a hint
         * to the renderer to tell it how the per-vertex colors and normals are
         * applied.
         */
        """
        pass

    def get_strip_cut_index(self, GeomPrimitive_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_strip_cut_index(GeomPrimitive self)
        
        /**
         * If relevant, returns the index value that may be used in some cases to
         * signify the end of a primitive.  This is typically the highest value that
         * the numeric type can store.
         */
        
        /**
         * Returns the index of the indicated type that is reserved for use as a strip
         * cut index, if enabled for the primitive.  When the renderer encounters this
         * index, it will restart the primitive.  This is guaranteed not to point to
         * an actual vertex.
         */
        """
        pass

    def get_usage_hint(self, GeomPrimitive_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_usage_hint(GeomPrimitive self)
        
        /**
         * Returns the usage hint for this primitive.  See geomEnums.h.  This has
         * nothing to do with the usage hint associated with the primitive's vertices;
         * this only specifies how often the vertex indices that define the primitive
         * will be modified.
         *
         * It is perfectly legal (and, in fact, common) for a GeomPrimitive to have
         * UH_static on itself, while referencing vertex data with UH_dynamic.  This
         * means that the vertices themselves will be animated, but the primitive will
         * always reference the same set of vertices from the pool.
         */
        """
        pass

    def get_vertex(self, GeomPrimitive_self, int_i): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_vertex(GeomPrimitive self, int i)
        
        /**
         * Returns the ith vertex index in the table.
         */
        """
        pass

    def get_vertex_list(self, *args, **kwargs): # real signature unknown
        pass

    def get_vertices(self, GeomPrimitive_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_vertices(GeomPrimitive self)
        
        /**
         * Returns a const pointer to the vertex index array so application code can
         * read it directly.  This might return NULL if the primitive is nonindexed.
         * Do not attempt to modify the returned array; use modify_vertices() or
         * set_vertices() for this.
         *
         * This method is intended for low-level usage only.  There are higher-level
         * methods for more common usage.  We recommend you do not use this method
         * directly.  If you do, be sure you know what you are doing!
         */
        """
        pass

    def get_vertices_handle(self, GeomPrimitive_self, Thread_current_thread): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_vertices_handle(GeomPrimitive self, Thread current_thread)
        
        /**
         * Equivalent to get_vertices().get_handle().
         */
        """
        pass

    def isComposite(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_composite(GeomPrimitive self)
        
        /**
         * Returns true if the primitive is a composite primitive such as a tristrip
         * or trifan, or false if it is a fundamental primitive such as a collection
         * of triangles.
         */
        """
        pass

    def isIndexed(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_indexed(GeomPrimitive self)
        
        /**
         * Returns true if the primitive is indexed, false otherwise.  An indexed
         * primitive stores a table of index numbers into its GeomVertexData, so that
         * it can reference the vertices in any order.  A nonindexed primitive, on the
         * other hand, stores only the first vertex number and number of vertices
         * used, so that it can only reference the vertices consecutively.
         */
        """
        pass

    def is_composite(self, GeomPrimitive_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_composite(GeomPrimitive self)
        
        /**
         * Returns true if the primitive is a composite primitive such as a tristrip
         * or trifan, or false if it is a fundamental primitive such as a collection
         * of triangles.
         */
        """
        pass

    def is_indexed(self, GeomPrimitive_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_indexed(GeomPrimitive self)
        
        /**
         * Returns true if the primitive is indexed, false otherwise.  An indexed
         * primitive stores a table of index numbers into its GeomVertexData, so that
         * it can reference the vertices in any order.  A nonindexed primitive, on the
         * other hand, stores only the first vertex number and number of vertices
         * used, so that it can only reference the vertices consecutively.
         */
        """
        pass

    def makeAdjacency(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        make_adjacency(GeomPrimitive self)
        
        /**
         * Adds adjacency information to this primitive.  May return null if this type
         * of geometry does not support adjacency information.
         *
         * @since 1.10.0
         */
        """
        pass

    def makeCopy(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        make_copy(GeomPrimitive self)
        """
        pass

    def makeIndexed(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        make_indexed(const GeomPrimitive self)
        
        /**
         * Converts the primitive from nonindexed form to indexed form.  This will
         * simply create an index table that is numbered consecutively from
         * get_first_vertex(); it does not automatically collapse together identical
         * vertices that may have been split apart by a previous call to
         * make_nonindexed().
         *
         * Don't call this in a downstream thread unless you don't mind it blowing
         * away other changes you might have recently made in an upstream thread.
         */
        """
        pass

    def makeLines(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        make_lines(GeomPrimitive self)
        
        /**
         * Returns a new GeomLines primitive that represents each of the edges in the
         * original primitive rendered as a line.  If the original primitive is
         * already a GeomLines primitive, returns the original primitive unchanged.
         */
        """
        pass

    def makeNonindexed(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        make_nonindexed(const GeomPrimitive self, GeomVertexData dest, const GeomVertexData source)
        
        /**
         * Converts the primitive from indexed to nonindexed by duplicating vertices
         * as necessary into the indicated dest GeomVertexData.  Note: does not
         * support primitives with strip cut indices.
         */
        """
        pass

    def makePatches(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        make_patches(GeomPrimitive self)
        
        /**
         * Decomposes a complex primitive type into a simpler primitive type, for
         * instance triangle strips to triangles, puts these in a new GeomPatches
         * object and returns a pointer to the new primitive definition.  If the
         * decomposition cannot be performed, this might return the original object.
         *
         * This method is useful for application code that wants to use tesselation
         * shaders on arbitrary geometry.
         */
        """
        pass

    def makePoints(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        make_points(GeomPrimitive self)
        
        /**
         * Returns a new GeomPoints primitive that represents each of the vertices in
         * the original primitive, rendered exactly once.  If the original primitive
         * is already a GeomPoints primitive, returns the original primitive
         * unchanged.
         */
        """
        pass

    def make_adjacency(self, GeomPrimitive_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        make_adjacency(GeomPrimitive self)
        
        /**
         * Adds adjacency information to this primitive.  May return null if this type
         * of geometry does not support adjacency information.
         *
         * @since 1.10.0
         */
        """
        pass

    def make_copy(self, GeomPrimitive_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        make_copy(GeomPrimitive self)
        """
        pass

    def make_indexed(self, const_GeomPrimitive_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        make_indexed(const GeomPrimitive self)
        
        /**
         * Converts the primitive from nonindexed form to indexed form.  This will
         * simply create an index table that is numbered consecutively from
         * get_first_vertex(); it does not automatically collapse together identical
         * vertices that may have been split apart by a previous call to
         * make_nonindexed().
         *
         * Don't call this in a downstream thread unless you don't mind it blowing
         * away other changes you might have recently made in an upstream thread.
         */
        """
        pass

    def make_lines(self, GeomPrimitive_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        make_lines(GeomPrimitive self)
        
        /**
         * Returns a new GeomLines primitive that represents each of the edges in the
         * original primitive rendered as a line.  If the original primitive is
         * already a GeomLines primitive, returns the original primitive unchanged.
         */
        """
        pass

    def make_nonindexed(self, const_GeomPrimitive_self, GeomVertexData_dest, const_GeomVertexData_source): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        make_nonindexed(const GeomPrimitive self, GeomVertexData dest, const GeomVertexData source)
        
        /**
         * Converts the primitive from indexed to nonindexed by duplicating vertices
         * as necessary into the indicated dest GeomVertexData.  Note: does not
         * support primitives with strip cut indices.
         */
        """
        pass

    def make_patches(self, GeomPrimitive_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        make_patches(GeomPrimitive self)
        
        /**
         * Decomposes a complex primitive type into a simpler primitive type, for
         * instance triangle strips to triangles, puts these in a new GeomPatches
         * object and returns a pointer to the new primitive definition.  If the
         * decomposition cannot be performed, this might return the original object.
         *
         * This method is useful for application code that wants to use tesselation
         * shaders on arbitrary geometry.
         */
        """
        pass

    def make_points(self, GeomPrimitive_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        make_points(GeomPrimitive self)
        
        /**
         * Returns a new GeomPoints primitive that represents each of the vertices in
         * the original primitive, rendered exactly once.  If the original primitive
         * is already a GeomPoints primitive, returns the original primitive
         * unchanged.
         */
        """
        pass

    def matchShadeModel(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        match_shade_model(GeomPrimitive self, int shade_model)
        
        /**
         * Returns a new primitive that is compatible with the indicated shade model,
         * if possible, or NULL if this is not possible.
         *
         * In most cases, this will return either NULL or the original primitive.  In
         * the case of a SM_flat_first_vertex vs.  a SM_flat_last_vertex (or vice-
         * versa), however, it will return a rotated primitive.
         */
        """
        pass

    def match_shade_model(self, GeomPrimitive_self, int_shade_model): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        match_shade_model(GeomPrimitive self, int shade_model)
        
        /**
         * Returns a new primitive that is compatible with the indicated shade model,
         * if possible, or NULL if this is not possible.
         *
         * In most cases, this will return either NULL or the original primitive.  In
         * the case of a SM_flat_first_vertex vs.  a SM_flat_last_vertex (or vice-
         * versa), however, it will return a rotated primitive.
         */
        """
        pass

    def modifyEnds(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        modify_ends(const GeomPrimitive self)
        
        /**
         * Returns a modifiable pointer to the primitive ends array, so application
         * code can directly fiddle with this data.  Use with caution, since there are
         * no checks that the data will be left in a stable state.
         *
         * Note that simple primitive types, like triangles, do not have a ends array:
         * since all the primitives have the same number of vertices, it is not
         * needed.
         *
         * Don't call this in a downstream thread unless you don't mind it blowing
         * away other changes you might have recently made in an upstream thread.
         *
         * This method is intended for low-level usage only.  There are higher-level
         * methods for more common usage.  We recommend you do not use this method
         * directly.  If you do, be sure you know what you are doing!
         */
        """
        pass

    def modifyVertices(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        modify_vertices(const GeomPrimitive self, int num_vertices)
        
        /**
         * Returns a modifiable pointer to the vertex index list, so application code
         * can directly fiddle with this data.  Use with caution, since there are no
         * checks that the data will be left in a stable state.
         *
         * If this is called on a nonindexed primitive, it will implicitly be
         * converted to an indexed primitive.
         *
         * If num_vertices is not -1, it specifies an artificial limit to the number
         * of vertices in the array.  Otherwise, all of the vertices in the array will
         * be used.
         *
         * Don't call this in a downstream thread unless you don't mind it blowing
         * away other changes you might have recently made in an upstream thread.
         *
         * This method is intended for low-level usage only.  There are higher-level
         * methods for more common usage.  We recommend you do not use this method
         * directly.  If you do, be sure you know what you are doing!
         */
        """
        pass

    def modifyVerticesHandle(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        modify_vertices_handle(const GeomPrimitive self, Thread current_thread)
        
        /**
         * Equivalent to modify_vertices().get_handle().
         */
        """
        pass

    def modify_ends(self, const_GeomPrimitive_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        modify_ends(const GeomPrimitive self)
        
        /**
         * Returns a modifiable pointer to the primitive ends array, so application
         * code can directly fiddle with this data.  Use with caution, since there are
         * no checks that the data will be left in a stable state.
         *
         * Note that simple primitive types, like triangles, do not have a ends array:
         * since all the primitives have the same number of vertices, it is not
         * needed.
         *
         * Don't call this in a downstream thread unless you don't mind it blowing
         * away other changes you might have recently made in an upstream thread.
         *
         * This method is intended for low-level usage only.  There are higher-level
         * methods for more common usage.  We recommend you do not use this method
         * directly.  If you do, be sure you know what you are doing!
         */
        """
        pass

    def modify_vertices(self, const_GeomPrimitive_self, int_num_vertices): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        modify_vertices(const GeomPrimitive self, int num_vertices)
        
        /**
         * Returns a modifiable pointer to the vertex index list, so application code
         * can directly fiddle with this data.  Use with caution, since there are no
         * checks that the data will be left in a stable state.
         *
         * If this is called on a nonindexed primitive, it will implicitly be
         * converted to an indexed primitive.
         *
         * If num_vertices is not -1, it specifies an artificial limit to the number
         * of vertices in the array.  Otherwise, all of the vertices in the array will
         * be used.
         *
         * Don't call this in a downstream thread unless you don't mind it blowing
         * away other changes you might have recently made in an upstream thread.
         *
         * This method is intended for low-level usage only.  There are higher-level
         * methods for more common usage.  We recommend you do not use this method
         * directly.  If you do, be sure you know what you are doing!
         */
        """
        pass

    def modify_vertices_handle(self, const_GeomPrimitive_self, Thread_current_thread): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        modify_vertices_handle(const GeomPrimitive self, Thread current_thread)
        
        /**
         * Equivalent to modify_vertices().get_handle().
         */
        """
        pass

    def offsetVertices(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        offset_vertices(const GeomPrimitive self, int offset)
        offset_vertices(const GeomPrimitive self, int offset, int begin_row, int end_row)
        
        /**
         * Adds the indicated offset to all vertices used by the primitive.
         *
         * Don't call this in a downstream thread unless you don't mind it blowing
         * away other changes you might have recently made in an upstream thread.
         */
        
        /**
         * Adds the indicated offset to the indicated segment of vertices used by the
         * primitive.  Unlike the other version of offset_vertices, this makes the
         * geometry indexed if it isn't already.
         *
         * Note that end_row indicates one past the last row that should be offset.
         * In other words, the number of vertices touched is (end_row - begin_row).
         *
         * Don't call this in a downstream thread unless you don't mind it blowing
         * away other changes you might have recently made in an upstream thread.
         */
        """
        pass

    def offset_vertices(self, const_GeomPrimitive_self, int_offset): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        offset_vertices(const GeomPrimitive self, int offset)
        offset_vertices(const GeomPrimitive self, int offset, int begin_row, int end_row)
        
        /**
         * Adds the indicated offset to all vertices used by the primitive.
         *
         * Don't call this in a downstream thread unless you don't mind it blowing
         * away other changes you might have recently made in an upstream thread.
         */
        
        /**
         * Adds the indicated offset to the indicated segment of vertices used by the
         * primitive.  Unlike the other version of offset_vertices, this makes the
         * geometry indexed if it isn't already.
         *
         * Note that end_row indicates one past the last row that should be offset.
         * In other words, the number of vertices touched is (end_row - begin_row).
         *
         * Don't call this in a downstream thread unless you don't mind it blowing
         * away other changes you might have recently made in an upstream thread.
         */
        """
        pass

    def output(self, GeomPrimitive_self, ostream_out): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        output(GeomPrimitive self, ostream out)
        
        /**
         *
         */
        """
        pass

    def packVertices(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        pack_vertices(const GeomPrimitive self, GeomVertexData dest, const GeomVertexData source)
        
        /**
         * Packs the vertices used by the primitive from the indicated source array
         * onto the end of the indicated destination array.
         */
        """
        pass

    def pack_vertices(self, const_GeomPrimitive_self, GeomVertexData_dest, const_GeomVertexData_source): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        pack_vertices(const GeomPrimitive self, GeomVertexData dest, const GeomVertexData source)
        
        /**
         * Packs the vertices used by the primitive from the indicated source array
         * onto the end of the indicated destination array.
         */
        """
        pass

    def requestResident(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        request_resident(GeomPrimitive self, Thread current_thread)
        
        /**
         * Returns true if the primitive data is currently resident in memory.  If
         * this returns false, the primitive data will be brought back into memory
         * shortly; try again later.
         */
        """
        pass

    def request_resident(self, GeomPrimitive_self, Thread_current_thread): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        request_resident(GeomPrimitive self, Thread current_thread)
        
        /**
         * Returns true if the primitive data is currently resident in memory.  If
         * this returns false, the primitive data will be brought back into memory
         * shortly; try again later.
         */
        """
        pass

    def reserveNumVertices(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        reserve_num_vertices(const GeomPrimitive self, int num_vertices)
        
        /**
         * This ensures that enough memory space for n vertices is allocated, so that
         * you may increase the number of vertices to n without causing a new memory
         * allocation.  This is a performance optimization only; it is especially
         * useful when you know ahead of time that you will be adding n vertices to
         * the primitive.
         *
         * Note that the total you specify here should also include implicit vertices
         * which may be added at each close_primitive() call, according to
         * get_num_unused_vertices_per_primitive().
         *
         * Note also that making this call will implicitly make the primitive indexed
         * if it is not already, which could result in a performance *penalty*.  If
         * you would prefer not to lose the nonindexed nature of your existing
         * GeomPrimitives, check is_indexed() before making this call.
         */
        """
        pass

    def reserve_num_vertices(self, const_GeomPrimitive_self, int_num_vertices): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        reserve_num_vertices(const GeomPrimitive self, int num_vertices)
        
        /**
         * This ensures that enough memory space for n vertices is allocated, so that
         * you may increase the number of vertices to n without causing a new memory
         * allocation.  This is a performance optimization only; it is especially
         * useful when you know ahead of time that you will be adding n vertices to
         * the primitive.
         *
         * Note that the total you specify here should also include implicit vertices
         * which may be added at each close_primitive() call, according to
         * get_num_unused_vertices_per_primitive().
         *
         * Note also that making this call will implicitly make the primitive indexed
         * if it is not already, which could result in a performance *penalty*.  If
         * you would prefer not to lose the nonindexed nature of your existing
         * GeomPrimitives, check is_indexed() before making this call.
         */
        """
        pass

    def reverse(self, GeomPrimitive_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        reverse(GeomPrimitive self)
        
        /**
         * Reverses the winding order in the primitive so that each triangle is facing
         * in the opposite direction it was originally.  Note that this doesn't affect
         * vertex normals, so this operation alone won't work in the presence of
         * lighting (but see SceneGraphReducer::reverse()).
         *
         * Also see CullFaceAttrib, which can change the visible direction of a
         * triangle without having to duplicate it (but which doesn't necessarily work
         * in the presence of lighting).
         */
        """
        pass

    def rotate(self, GeomPrimitive_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        rotate(GeomPrimitive self)
        
        /**
         * Returns a new primitive with the shade_model reversed (if it is flat
         * shaded), if possible.  If the primitive type cannot be rotated, returns the
         * original primitive, unrotated.
         *
         * If the current shade_model indicates flat_vertex_last, this should bring
         * the last vertex to the first position; if it indicates flat_vertex_first,
         * this should bring the first vertex to the last position.
         */
        """
        pass

    def setEnds(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_ends(const GeomPrimitive self, PointerToArray ends)
        
        /**
         * Completely replaces the primitive ends array with a new table.  Chances are
         * good that you should also replace the vertices list with set_vertices() at
         * the same time.
         *
         * Note that simple primitive types, like triangles, do not have a ends array:
         * since all the primitives have the same number of vertices, it is not
         * needed.
         *
         * Don't call this in a downstream thread unless you don't mind it blowing
         * away other changes you might have recently made in an upstream thread.
         *
         * This method is intended for low-level usage only.  There are higher-level
         * methods for more common usage.  We recommend you do not use this method
         * directly.  If you do, be sure you know what you are doing!
         */
        """
        pass

    def setIndexType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_index_type(const GeomPrimitive self, int index_type)
        
        /**
         * Changes the numeric type of the index column.  Normally, this should be
         * either NT_uint16 or NT_uint32.
         *
         * The index type must be large enough to include all of the index values in
         * the primitive.  It may be automatically elevated, if necessary, to a larger
         * index type, by a subsequent call to add_index() that names an index value
         * that does not fit in the index type you specify.
         *
         * Don't call this in a downstream thread unless you don't mind it blowing
         * away other changes you might have recently made in an upstream thread.
         */
        """
        pass

    def setMinmax(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_minmax(const GeomPrimitive self, int min_vertex, int max_vertex, GeomVertexArrayData mins, GeomVertexArrayData maxs)
        
        /**
         * Explicitly specifies the minimum and maximum vertices, as well as the lists
         * of per-component min and max.
         *
         * Use this method with extreme caution.  It's generally better to let the
         * GeomPrimitive compute these explicitly, unless for some reason you can do
         * it faster and you absolutely need the speed improvement.
         *
         * Note that any modification to the vertex array will normally cause this to
         * be recomputed, unless you set it immediately again.
         *
         * This method is intended for low-level usage only.  There are higher-level
         * methods for more common usage.  We recommend you do not use this method
         * directly.  If you do, be sure you know what you are doing!
         */
        """
        pass

    def setNonindexedVertices(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_nonindexed_vertices(const GeomPrimitive self, int first_vertex, int num_vertices)
        
        /**
         * Sets the primitive up as a nonindexed primitive, using the indicated vertex
         * range.
         *
         * Don't call this in a downstream thread unless you don't mind it blowing
         * away other changes you might have recently made in an upstream thread.
         *
         * This method is intended for low-level usage only.  There are higher-level
         * methods for more common usage.  We recommend you do not use this method
         * directly.  If you do, be sure you know what you are doing!
         */
        """
        pass

    def setShadeModel(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_shade_model(const GeomPrimitive self, int shade_model)
        
        /**
         * Changes the ShadeModel hint for this primitive.  This is different from the
         * ShadeModelAttrib that might also be applied from the scene graph.  This
         * does not affect the shade model that is in effect when rendering, but
         * rather serves as a hint to the renderer to tell it how the per-vertex
         * colors and normals on this primitive are applied.
         *
         * Don't call this in a downstream thread unless you don't mind it blowing
         * away other changes you might have recently made in an upstream thread.
         */
        """
        pass

    def setUsageHint(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_usage_hint(const GeomPrimitive self, int usage_hint)
        
        /**
         * Changes the UsageHint hint for this primitive.  See get_usage_hint().
         *
         * Don't call this in a downstream thread unless you don't mind it blowing
         * away other changes you might have recently made in an upstream thread.
         */
        """
        pass

    def setVertices(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_vertices(const GeomPrimitive self, const GeomVertexArrayData vertices, int num_vertices)
        
        /**
         * Completely replaces the vertex index list with a new table.  Chances are
         * good that you should also replace the ends list with set_ends() at the same
         * time.
         *
         * If num_vertices is not -1, it specifies an artificial limit to the number
         * of vertices in the array.  Otherwise, all of the vertices in the array will
         * be used.
         *
         * Don't call this in a downstream thread unless you don't mind it blowing
         * away other changes you might have recently made in an upstream thread.
         *
         * This method is intended for low-level usage only.  There are higher-level
         * methods for more common usage.  We recommend you do not use this method
         * directly.  If you do, be sure you know what you are doing!
         */
        """
        pass

    def set_ends(self, const_GeomPrimitive_self, PointerToArray_ends): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_ends(const GeomPrimitive self, PointerToArray ends)
        
        /**
         * Completely replaces the primitive ends array with a new table.  Chances are
         * good that you should also replace the vertices list with set_vertices() at
         * the same time.
         *
         * Note that simple primitive types, like triangles, do not have a ends array:
         * since all the primitives have the same number of vertices, it is not
         * needed.
         *
         * Don't call this in a downstream thread unless you don't mind it blowing
         * away other changes you might have recently made in an upstream thread.
         *
         * This method is intended for low-level usage only.  There are higher-level
         * methods for more common usage.  We recommend you do not use this method
         * directly.  If you do, be sure you know what you are doing!
         */
        """
        pass

    def set_index_type(self, const_GeomPrimitive_self, int_index_type): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_index_type(const GeomPrimitive self, int index_type)
        
        /**
         * Changes the numeric type of the index column.  Normally, this should be
         * either NT_uint16 or NT_uint32.
         *
         * The index type must be large enough to include all of the index values in
         * the primitive.  It may be automatically elevated, if necessary, to a larger
         * index type, by a subsequent call to add_index() that names an index value
         * that does not fit in the index type you specify.
         *
         * Don't call this in a downstream thread unless you don't mind it blowing
         * away other changes you might have recently made in an upstream thread.
         */
        """
        pass

    def set_minmax(self, const_GeomPrimitive_self, int_min_vertex, int_max_vertex, GeomVertexArrayData_mins, GeomVertexArrayData_maxs): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_minmax(const GeomPrimitive self, int min_vertex, int max_vertex, GeomVertexArrayData mins, GeomVertexArrayData maxs)
        
        /**
         * Explicitly specifies the minimum and maximum vertices, as well as the lists
         * of per-component min and max.
         *
         * Use this method with extreme caution.  It's generally better to let the
         * GeomPrimitive compute these explicitly, unless for some reason you can do
         * it faster and you absolutely need the speed improvement.
         *
         * Note that any modification to the vertex array will normally cause this to
         * be recomputed, unless you set it immediately again.
         *
         * This method is intended for low-level usage only.  There are higher-level
         * methods for more common usage.  We recommend you do not use this method
         * directly.  If you do, be sure you know what you are doing!
         */
        """
        pass

    def set_nonindexed_vertices(self, const_GeomPrimitive_self, int_first_vertex, int_num_vertices): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_nonindexed_vertices(const GeomPrimitive self, int first_vertex, int num_vertices)
        
        /**
         * Sets the primitive up as a nonindexed primitive, using the indicated vertex
         * range.
         *
         * Don't call this in a downstream thread unless you don't mind it blowing
         * away other changes you might have recently made in an upstream thread.
         *
         * This method is intended for low-level usage only.  There are higher-level
         * methods for more common usage.  We recommend you do not use this method
         * directly.  If you do, be sure you know what you are doing!
         */
        """
        pass

    def set_shade_model(self, const_GeomPrimitive_self, int_shade_model): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_shade_model(const GeomPrimitive self, int shade_model)
        
        /**
         * Changes the ShadeModel hint for this primitive.  This is different from the
         * ShadeModelAttrib that might also be applied from the scene graph.  This
         * does not affect the shade model that is in effect when rendering, but
         * rather serves as a hint to the renderer to tell it how the per-vertex
         * colors and normals on this primitive are applied.
         *
         * Don't call this in a downstream thread unless you don't mind it blowing
         * away other changes you might have recently made in an upstream thread.
         */
        """
        pass

    def set_usage_hint(self, const_GeomPrimitive_self, int_usage_hint): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_usage_hint(const GeomPrimitive self, int usage_hint)
        
        /**
         * Changes the UsageHint hint for this primitive.  See get_usage_hint().
         *
         * Don't call this in a downstream thread unless you don't mind it blowing
         * away other changes you might have recently made in an upstream thread.
         */
        """
        pass

    def set_vertices(self, const_GeomPrimitive_self, const_GeomVertexArrayData_vertices, int_num_vertices): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_vertices(const GeomPrimitive self, const GeomVertexArrayData vertices, int num_vertices)
        
        /**
         * Completely replaces the vertex index list with a new table.  Chances are
         * good that you should also replace the ends list with set_ends() at the same
         * time.
         *
         * If num_vertices is not -1, it specifies an artificial limit to the number
         * of vertices in the array.  Otherwise, all of the vertices in the array will
         * be used.
         *
         * Don't call this in a downstream thread unless you don't mind it blowing
         * away other changes you might have recently made in an upstream thread.
         *
         * This method is intended for low-level usage only.  There are higher-level
         * methods for more common usage.  We recommend you do not use this method
         * directly.  If you do, be sure you know what you are doing!
         */
        """
        pass

    def upcastToCopyOnWriteObject(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        upcast_to_CopyOnWriteObject(const GeomPrimitive self)
        
        upcast from GeomPrimitive to CopyOnWriteObject
        """
        pass

    def upcastToGeomEnums(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        upcast_to_GeomEnums(const GeomPrimitive self)
        
        upcast from GeomPrimitive to GeomEnums
        """
        pass

    def upcast_to_CopyOnWriteObject(self, const_GeomPrimitive_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        upcast_to_CopyOnWriteObject(const GeomPrimitive self)
        
        upcast from GeomPrimitive to CopyOnWriteObject
        """
        pass

    def upcast_to_GeomEnums(self, const_GeomPrimitive_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        upcast_to_GeomEnums(const GeomPrimitive self)
        
        upcast from GeomPrimitive to GeomEnums
        """
        pass

    def write(self, GeomPrimitive_self, ostream_out, int_indent_level): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        write(GeomPrimitive self, ostream out, int indent_level)
        
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

    data_size_bytes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    geom_rendering = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    index_stride = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    index_type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    maxs = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    mins = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    min_num_vertices_per_primitive = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    modified = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    num_bytes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    num_unused_vertices_per_primitive = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    num_vertices_per_primitive = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    primitive_type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    shade_model = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    strip_cut_index = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    usage_hint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.core.GeomPrimitive' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.core.GeomPrimitive' objects>"
        '__doc__': '/**\n * This is an abstract base class for a family of classes that represent the\n * fundamental geometry primitives that may be stored in a Geom.\n *\n * They all have in common the fact that they are defined by tables of vertex\n * data stored in a GeomVertexData object.  Each GeomPrimitive object contains\n * an ordered list of integers, which index into the vertex array defined by\n * the GeomVertexData and define the particular vertices of the GeomVertexData\n * that are used for this primitive.\n *\n * The meaning of a given arrangement of vertices is defined by each\n * individual primitive type; for instance, a GeomTriangle renders a triangle\n * from each three consecutive vertices, while a GeomTriangleStrip renders a\n * strip of (n - 2) connected triangles from each sequence of n vertices.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.GeomPrimitive' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE2FCAD0>'
        '__repr__': None, # (!) real value is "<slot wrapper '__repr__' of 'panda3d.core.GeomPrimitive' objects>"
        '__str__': None, # (!) real value is "<slot wrapper '__str__' of 'panda3d.core.GeomPrimitive' objects>"
        'addConsecutiveVertices': None, # (!) real value is "<method 'addConsecutiveVertices' of 'panda3d.core.GeomPrimitive' objects>"
        'addNextVertices': None, # (!) real value is "<method 'addNextVertices' of 'panda3d.core.GeomPrimitive' objects>"
        'addVertex': None, # (!) real value is "<method 'addVertex' of 'panda3d.core.GeomPrimitive' objects>"
        'addVertices': None, # (!) real value is "<method 'addVertices' of 'panda3d.core.GeomPrimitive' objects>"
        'add_consecutive_vertices': None, # (!) real value is "<method 'add_consecutive_vertices' of 'panda3d.core.GeomPrimitive' objects>"
        'add_next_vertices': None, # (!) real value is "<method 'add_next_vertices' of 'panda3d.core.GeomPrimitive' objects>"
        'add_vertex': None, # (!) real value is "<method 'add_vertex' of 'panda3d.core.GeomPrimitive' objects>"
        'add_vertices': None, # (!) real value is "<method 'add_vertices' of 'panda3d.core.GeomPrimitive' objects>"
        'assign': None, # (!) real value is "<method 'assign' of 'panda3d.core.GeomPrimitive' objects>"
        'checkValid': None, # (!) real value is "<method 'checkValid' of 'panda3d.core.GeomPrimitive' objects>"
        'check_valid': None, # (!) real value is "<method 'check_valid' of 'panda3d.core.GeomPrimitive' objects>"
        'clearMinmax': None, # (!) real value is "<method 'clearMinmax' of 'panda3d.core.GeomPrimitive' objects>"
        'clearVertices': None, # (!) real value is "<method 'clearVertices' of 'panda3d.core.GeomPrimitive' objects>"
        'clear_minmax': None, # (!) real value is "<method 'clear_minmax' of 'panda3d.core.GeomPrimitive' objects>"
        'clear_vertices': None, # (!) real value is "<method 'clear_vertices' of 'panda3d.core.GeomPrimitive' objects>"
        'closePrimitive': None, # (!) real value is "<method 'closePrimitive' of 'panda3d.core.GeomPrimitive' objects>"
        'close_primitive': None, # (!) real value is "<method 'close_primitive' of 'panda3d.core.GeomPrimitive' objects>"
        'data_size_bytes': None, # (!) real value is "<attribute 'data_size_bytes' of 'panda3d.core.GeomPrimitive' objects>"
        'decompose': None, # (!) real value is "<method 'decompose' of 'panda3d.core.GeomPrimitive' objects>"
        'doubleside': None, # (!) real value is "<method 'doubleside' of 'panda3d.core.GeomPrimitive' objects>"
        'geom_rendering': None, # (!) real value is "<attribute 'geom_rendering' of 'panda3d.core.GeomPrimitive' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE2FCAD0>)>'
        'getDataSizeBytes': None, # (!) real value is "<method 'getDataSizeBytes' of 'panda3d.core.GeomPrimitive' objects>"
        'getEnds': None, # (!) real value is "<method 'getEnds' of 'panda3d.core.GeomPrimitive' objects>"
        'getFirstVertex': None, # (!) real value is "<method 'getFirstVertex' of 'panda3d.core.GeomPrimitive' objects>"
        'getGeomRendering': None, # (!) real value is "<method 'getGeomRendering' of 'panda3d.core.GeomPrimitive' objects>"
        'getIndexStride': None, # (!) real value is "<method 'getIndexStride' of 'panda3d.core.GeomPrimitive' objects>"
        'getIndexType': None, # (!) real value is "<method 'getIndexType' of 'panda3d.core.GeomPrimitive' objects>"
        'getMaxVertex': None, # (!) real value is "<method 'getMaxVertex' of 'panda3d.core.GeomPrimitive' objects>"
        'getMaxs': None, # (!) real value is "<method 'getMaxs' of 'panda3d.core.GeomPrimitive' objects>"
        'getMinNumVerticesPerPrimitive': None, # (!) real value is "<method 'getMinNumVerticesPerPrimitive' of 'panda3d.core.GeomPrimitive' objects>"
        'getMinVertex': None, # (!) real value is "<method 'getMinVertex' of 'panda3d.core.GeomPrimitive' objects>"
        'getMins': None, # (!) real value is "<method 'getMins' of 'panda3d.core.GeomPrimitive' objects>"
        'getModified': None, # (!) real value is "<method 'getModified' of 'panda3d.core.GeomPrimitive' objects>"
        'getNumBytes': None, # (!) real value is "<method 'getNumBytes' of 'panda3d.core.GeomPrimitive' objects>"
        'getNumFaces': None, # (!) real value is "<method 'getNumFaces' of 'panda3d.core.GeomPrimitive' objects>"
        'getNumPrimitives': None, # (!) real value is "<method 'getNumPrimitives' of 'panda3d.core.GeomPrimitive' objects>"
        'getNumUnusedVerticesPerPrimitive': None, # (!) real value is "<method 'getNumUnusedVerticesPerPrimitive' of 'panda3d.core.GeomPrimitive' objects>"
        'getNumUsedVertices': None, # (!) real value is "<method 'getNumUsedVertices' of 'panda3d.core.GeomPrimitive' objects>"
        'getNumVertices': None, # (!) real value is "<method 'getNumVertices' of 'panda3d.core.GeomPrimitive' objects>"
        'getNumVerticesPerPrimitive': None, # (!) real value is "<method 'getNumVerticesPerPrimitive' of 'panda3d.core.GeomPrimitive' objects>"
        'getPrimitiveEnd': None, # (!) real value is "<method 'getPrimitiveEnd' of 'panda3d.core.GeomPrimitive' objects>"
        'getPrimitiveMaxVertex': None, # (!) real value is "<method 'getPrimitiveMaxVertex' of 'panda3d.core.GeomPrimitive' objects>"
        'getPrimitiveMinVertex': None, # (!) real value is "<method 'getPrimitiveMinVertex' of 'panda3d.core.GeomPrimitive' objects>"
        'getPrimitiveNumFaces': None, # (!) real value is "<method 'getPrimitiveNumFaces' of 'panda3d.core.GeomPrimitive' objects>"
        'getPrimitiveNumVertices': None, # (!) real value is "<method 'getPrimitiveNumVertices' of 'panda3d.core.GeomPrimitive' objects>"
        'getPrimitiveStart': None, # (!) real value is "<method 'getPrimitiveStart' of 'panda3d.core.GeomPrimitive' objects>"
        'getPrimitiveType': None, # (!) real value is "<method 'getPrimitiveType' of 'panda3d.core.GeomPrimitive' objects>"
        'getShadeModel': None, # (!) real value is "<method 'getShadeModel' of 'panda3d.core.GeomPrimitive' objects>"
        'getStripCutIndex': None, # (!) real value is "<method 'getStripCutIndex' of 'panda3d.core.GeomPrimitive' objects>"
        'getUsageHint': None, # (!) real value is "<method 'getUsageHint' of 'panda3d.core.GeomPrimitive' objects>"
        'getVertex': None, # (!) real value is "<method 'getVertex' of 'panda3d.core.GeomPrimitive' objects>"
        'getVertexList': None, # (!) real value is "<method 'getVertexList' of 'panda3d.core.GeomPrimitive' objects>"
        'getVertices': None, # (!) real value is "<method 'getVertices' of 'panda3d.core.GeomPrimitive' objects>"
        'getVerticesHandle': None, # (!) real value is "<method 'getVerticesHandle' of 'panda3d.core.GeomPrimitive' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE2FCAD0>)>'
        'get_data_size_bytes': None, # (!) real value is "<method 'get_data_size_bytes' of 'panda3d.core.GeomPrimitive' objects>"
        'get_ends': None, # (!) real value is "<method 'get_ends' of 'panda3d.core.GeomPrimitive' objects>"
        'get_first_vertex': None, # (!) real value is "<method 'get_first_vertex' of 'panda3d.core.GeomPrimitive' objects>"
        'get_geom_rendering': None, # (!) real value is "<method 'get_geom_rendering' of 'panda3d.core.GeomPrimitive' objects>"
        'get_index_stride': None, # (!) real value is "<method 'get_index_stride' of 'panda3d.core.GeomPrimitive' objects>"
        'get_index_type': None, # (!) real value is "<method 'get_index_type' of 'panda3d.core.GeomPrimitive' objects>"
        'get_max_vertex': None, # (!) real value is "<method 'get_max_vertex' of 'panda3d.core.GeomPrimitive' objects>"
        'get_maxs': None, # (!) real value is "<method 'get_maxs' of 'panda3d.core.GeomPrimitive' objects>"
        'get_min_num_vertices_per_primitive': None, # (!) real value is "<method 'get_min_num_vertices_per_primitive' of 'panda3d.core.GeomPrimitive' objects>"
        'get_min_vertex': None, # (!) real value is "<method 'get_min_vertex' of 'panda3d.core.GeomPrimitive' objects>"
        'get_mins': None, # (!) real value is "<method 'get_mins' of 'panda3d.core.GeomPrimitive' objects>"
        'get_modified': None, # (!) real value is "<method 'get_modified' of 'panda3d.core.GeomPrimitive' objects>"
        'get_num_bytes': None, # (!) real value is "<method 'get_num_bytes' of 'panda3d.core.GeomPrimitive' objects>"
        'get_num_faces': None, # (!) real value is "<method 'get_num_faces' of 'panda3d.core.GeomPrimitive' objects>"
        'get_num_primitives': None, # (!) real value is "<method 'get_num_primitives' of 'panda3d.core.GeomPrimitive' objects>"
        'get_num_unused_vertices_per_primitive': None, # (!) real value is "<method 'get_num_unused_vertices_per_primitive' of 'panda3d.core.GeomPrimitive' objects>"
        'get_num_used_vertices': None, # (!) real value is "<method 'get_num_used_vertices' of 'panda3d.core.GeomPrimitive' objects>"
        'get_num_vertices': None, # (!) real value is "<method 'get_num_vertices' of 'panda3d.core.GeomPrimitive' objects>"
        'get_num_vertices_per_primitive': None, # (!) real value is "<method 'get_num_vertices_per_primitive' of 'panda3d.core.GeomPrimitive' objects>"
        'get_primitive_end': None, # (!) real value is "<method 'get_primitive_end' of 'panda3d.core.GeomPrimitive' objects>"
        'get_primitive_max_vertex': None, # (!) real value is "<method 'get_primitive_max_vertex' of 'panda3d.core.GeomPrimitive' objects>"
        'get_primitive_min_vertex': None, # (!) real value is "<method 'get_primitive_min_vertex' of 'panda3d.core.GeomPrimitive' objects>"
        'get_primitive_num_faces': None, # (!) real value is "<method 'get_primitive_num_faces' of 'panda3d.core.GeomPrimitive' objects>"
        'get_primitive_num_vertices': None, # (!) real value is "<method 'get_primitive_num_vertices' of 'panda3d.core.GeomPrimitive' objects>"
        'get_primitive_start': None, # (!) real value is "<method 'get_primitive_start' of 'panda3d.core.GeomPrimitive' objects>"
        'get_primitive_type': None, # (!) real value is "<method 'get_primitive_type' of 'panda3d.core.GeomPrimitive' objects>"
        'get_shade_model': None, # (!) real value is "<method 'get_shade_model' of 'panda3d.core.GeomPrimitive' objects>"
        'get_strip_cut_index': None, # (!) real value is "<method 'get_strip_cut_index' of 'panda3d.core.GeomPrimitive' objects>"
        'get_usage_hint': None, # (!) real value is "<method 'get_usage_hint' of 'panda3d.core.GeomPrimitive' objects>"
        'get_vertex': None, # (!) real value is "<method 'get_vertex' of 'panda3d.core.GeomPrimitive' objects>"
        'get_vertex_list': None, # (!) real value is "<method 'get_vertex_list' of 'panda3d.core.GeomPrimitive' objects>"
        'get_vertices': None, # (!) real value is "<method 'get_vertices' of 'panda3d.core.GeomPrimitive' objects>"
        'get_vertices_handle': None, # (!) real value is "<method 'get_vertices_handle' of 'panda3d.core.GeomPrimitive' objects>"
        'index_stride': None, # (!) real value is "<attribute 'index_stride' of 'panda3d.core.GeomPrimitive' objects>"
        'index_type': None, # (!) real value is "<attribute 'index_type' of 'panda3d.core.GeomPrimitive' objects>"
        'isComposite': None, # (!) real value is "<method 'isComposite' of 'panda3d.core.GeomPrimitive' objects>"
        'isIndexed': None, # (!) real value is "<method 'isIndexed' of 'panda3d.core.GeomPrimitive' objects>"
        'is_composite': None, # (!) real value is "<method 'is_composite' of 'panda3d.core.GeomPrimitive' objects>"
        'is_indexed': None, # (!) real value is "<method 'is_indexed' of 'panda3d.core.GeomPrimitive' objects>"
        'makeAdjacency': None, # (!) real value is "<method 'makeAdjacency' of 'panda3d.core.GeomPrimitive' objects>"
        'makeCopy': None, # (!) real value is "<method 'makeCopy' of 'panda3d.core.GeomPrimitive' objects>"
        'makeIndexed': None, # (!) real value is "<method 'makeIndexed' of 'panda3d.core.GeomPrimitive' objects>"
        'makeLines': None, # (!) real value is "<method 'makeLines' of 'panda3d.core.GeomPrimitive' objects>"
        'makeNonindexed': None, # (!) real value is "<method 'makeNonindexed' of 'panda3d.core.GeomPrimitive' objects>"
        'makePatches': None, # (!) real value is "<method 'makePatches' of 'panda3d.core.GeomPrimitive' objects>"
        'makePoints': None, # (!) real value is "<method 'makePoints' of 'panda3d.core.GeomPrimitive' objects>"
        'make_adjacency': None, # (!) real value is "<method 'make_adjacency' of 'panda3d.core.GeomPrimitive' objects>"
        'make_copy': None, # (!) real value is "<method 'make_copy' of 'panda3d.core.GeomPrimitive' objects>"
        'make_indexed': None, # (!) real value is "<method 'make_indexed' of 'panda3d.core.GeomPrimitive' objects>"
        'make_lines': None, # (!) real value is "<method 'make_lines' of 'panda3d.core.GeomPrimitive' objects>"
        'make_nonindexed': None, # (!) real value is "<method 'make_nonindexed' of 'panda3d.core.GeomPrimitive' objects>"
        'make_patches': None, # (!) real value is "<method 'make_patches' of 'panda3d.core.GeomPrimitive' objects>"
        'make_points': None, # (!) real value is "<method 'make_points' of 'panda3d.core.GeomPrimitive' objects>"
        'matchShadeModel': None, # (!) real value is "<method 'matchShadeModel' of 'panda3d.core.GeomPrimitive' objects>"
        'match_shade_model': None, # (!) real value is "<method 'match_shade_model' of 'panda3d.core.GeomPrimitive' objects>"
        'maxs': None, # (!) real value is "<attribute 'maxs' of 'panda3d.core.GeomPrimitive' objects>"
        'min_num_vertices_per_primitive': None, # (!) real value is "<attribute 'min_num_vertices_per_primitive' of 'panda3d.core.GeomPrimitive' objects>"
        'mins': None, # (!) real value is "<attribute 'mins' of 'panda3d.core.GeomPrimitive' objects>"
        'modified': None, # (!) real value is "<attribute 'modified' of 'panda3d.core.GeomPrimitive' objects>"
        'modifyEnds': None, # (!) real value is "<method 'modifyEnds' of 'panda3d.core.GeomPrimitive' objects>"
        'modifyVertices': None, # (!) real value is "<method 'modifyVertices' of 'panda3d.core.GeomPrimitive' objects>"
        'modifyVerticesHandle': None, # (!) real value is "<method 'modifyVerticesHandle' of 'panda3d.core.GeomPrimitive' objects>"
        'modify_ends': None, # (!) real value is "<method 'modify_ends' of 'panda3d.core.GeomPrimitive' objects>"
        'modify_vertices': None, # (!) real value is "<method 'modify_vertices' of 'panda3d.core.GeomPrimitive' objects>"
        'modify_vertices_handle': None, # (!) real value is "<method 'modify_vertices_handle' of 'panda3d.core.GeomPrimitive' objects>"
        'num_bytes': None, # (!) real value is "<attribute 'num_bytes' of 'panda3d.core.GeomPrimitive' objects>"
        'num_unused_vertices_per_primitive': None, # (!) real value is "<attribute 'num_unused_vertices_per_primitive' of 'panda3d.core.GeomPrimitive' objects>"
        'num_vertices_per_primitive': None, # (!) real value is "<attribute 'num_vertices_per_primitive' of 'panda3d.core.GeomPrimitive' objects>"
        'offsetVertices': None, # (!) real value is "<method 'offsetVertices' of 'panda3d.core.GeomPrimitive' objects>"
        'offset_vertices': None, # (!) real value is "<method 'offset_vertices' of 'panda3d.core.GeomPrimitive' objects>"
        'output': None, # (!) real value is "<method 'output' of 'panda3d.core.GeomPrimitive' objects>"
        'packVertices': None, # (!) real value is "<method 'packVertices' of 'panda3d.core.GeomPrimitive' objects>"
        'pack_vertices': None, # (!) real value is "<method 'pack_vertices' of 'panda3d.core.GeomPrimitive' objects>"
        'primitive_type': None, # (!) real value is "<attribute 'primitive_type' of 'panda3d.core.GeomPrimitive' objects>"
        'requestResident': None, # (!) real value is "<method 'requestResident' of 'panda3d.core.GeomPrimitive' objects>"
        'request_resident': None, # (!) real value is "<method 'request_resident' of 'panda3d.core.GeomPrimitive' objects>"
        'reserveNumVertices': None, # (!) real value is "<method 'reserveNumVertices' of 'panda3d.core.GeomPrimitive' objects>"
        'reserve_num_vertices': None, # (!) real value is "<method 'reserve_num_vertices' of 'panda3d.core.GeomPrimitive' objects>"
        'reverse': None, # (!) real value is "<method 'reverse' of 'panda3d.core.GeomPrimitive' objects>"
        'rotate': None, # (!) real value is "<method 'rotate' of 'panda3d.core.GeomPrimitive' objects>"
        'setEnds': None, # (!) real value is "<method 'setEnds' of 'panda3d.core.GeomPrimitive' objects>"
        'setIndexType': None, # (!) real value is "<method 'setIndexType' of 'panda3d.core.GeomPrimitive' objects>"
        'setMinmax': None, # (!) real value is "<method 'setMinmax' of 'panda3d.core.GeomPrimitive' objects>"
        'setNonindexedVertices': None, # (!) real value is "<method 'setNonindexedVertices' of 'panda3d.core.GeomPrimitive' objects>"
        'setShadeModel': None, # (!) real value is "<method 'setShadeModel' of 'panda3d.core.GeomPrimitive' objects>"
        'setUsageHint': None, # (!) real value is "<method 'setUsageHint' of 'panda3d.core.GeomPrimitive' objects>"
        'setVertices': None, # (!) real value is "<method 'setVertices' of 'panda3d.core.GeomPrimitive' objects>"
        'set_ends': None, # (!) real value is "<method 'set_ends' of 'panda3d.core.GeomPrimitive' objects>"
        'set_index_type': None, # (!) real value is "<method 'set_index_type' of 'panda3d.core.GeomPrimitive' objects>"
        'set_minmax': None, # (!) real value is "<method 'set_minmax' of 'panda3d.core.GeomPrimitive' objects>"
        'set_nonindexed_vertices': None, # (!) real value is "<method 'set_nonindexed_vertices' of 'panda3d.core.GeomPrimitive' objects>"
        'set_shade_model': None, # (!) real value is "<method 'set_shade_model' of 'panda3d.core.GeomPrimitive' objects>"
        'set_usage_hint': None, # (!) real value is "<method 'set_usage_hint' of 'panda3d.core.GeomPrimitive' objects>"
        'set_vertices': None, # (!) real value is "<method 'set_vertices' of 'panda3d.core.GeomPrimitive' objects>"
        'shade_model': None, # (!) real value is "<attribute 'shade_model' of 'panda3d.core.GeomPrimitive' objects>"
        'strip_cut_index': None, # (!) real value is "<attribute 'strip_cut_index' of 'panda3d.core.GeomPrimitive' objects>"
        'upcastToCopyOnWriteObject': None, # (!) real value is "<method 'upcastToCopyOnWriteObject' of 'panda3d.core.GeomPrimitive' objects>"
        'upcastToGeomEnums': None, # (!) real value is "<method 'upcastToGeomEnums' of 'panda3d.core.GeomPrimitive' objects>"
        'upcast_to_CopyOnWriteObject': None, # (!) real value is "<method 'upcast_to_CopyOnWriteObject' of 'panda3d.core.GeomPrimitive' objects>"
        'upcast_to_GeomEnums': None, # (!) real value is "<method 'upcast_to_GeomEnums' of 'panda3d.core.GeomPrimitive' objects>"
        'usage_hint': None, # (!) real value is "<attribute 'usage_hint' of 'panda3d.core.GeomPrimitive' objects>"
        'write': None, # (!) real value is "<method 'write' of 'panda3d.core.GeomPrimitive' objects>"
    }


