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

class Geom(CopyOnWriteObject, GeomEnums):
    """
    /**
     * A container for geometry primitives.  This class associates one or more
     * GeomPrimitive objects with a table of vertices defined by a GeomVertexData
     * object.  All of the primitives stored in a particular Geom are drawn from
     * the same set of vertices (each primitive uses a subset of all of the
     * vertices in the table), and all of them must be rendered at the same time,
     * in the same graphics state.
     */
    """
    def addPrimitive(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_primitive(const Geom self, const GeomPrimitive primitive)
        
        /**
         * Inserts a new GeomPrimitive structure to the Geom object.  This specifies a
         * particular subset of vertices that are used to define geometric primitives
         * of the indicated type.
         *
         * Don't call this in a downstream thread unless you don't mind it blowing
         * away other changes you might have recently made in an upstream thread.
         */
        """
        pass

    def add_primitive(self, const_Geom_self, const_GeomPrimitive_primitive): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_primitive(const Geom self, const GeomPrimitive primitive)
        
        /**
         * Inserts a new GeomPrimitive structure to the Geom object.  This specifies a
         * particular subset of vertices that are used to define geometric primitives
         * of the indicated type.
         *
         * Don't call this in a downstream thread unless you don't mind it blowing
         * away other changes you might have recently made in an upstream thread.
         */
        """
        pass

    def assign(self, const_Geom_self, const_Geom_copy): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        assign(const Geom self, const Geom copy)
        """
        pass

    def checkValid(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        check_valid(Geom self)
        check_valid(Geom self, const GeomVertexData vertex_data)
        
        /**
         * Verifies that the all of the primitives within the geom reference vertices
         * that actually exist within the geom's GeomVertexData.  Returns true if the
         * geom appears to be valid, false otherwise.
         */
        
        /**
         * Verifies that the all of the primitives within the geom reference vertices
         * that actually exist within the indicated GeomVertexData.  Returns true if
         * the geom appears to be valid, false otherwise.
         */
        """
        pass

    def check_valid(self, Geom_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        check_valid(Geom self)
        check_valid(Geom self, const GeomVertexData vertex_data)
        
        /**
         * Verifies that the all of the primitives within the geom reference vertices
         * that actually exist within the geom's GeomVertexData.  Returns true if the
         * geom appears to be valid, false otherwise.
         */
        
        /**
         * Verifies that the all of the primitives within the geom reference vertices
         * that actually exist within the indicated GeomVertexData.  Returns true if
         * the geom appears to be valid, false otherwise.
         */
        """
        pass

    def clearBounds(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_bounds(const Geom self)
        
        /**
         * Reverses the effect of a previous call to set_bounds(), and allows the
         * bounding volume to be automatically computed once more based on the
         * vertices.
         *
         * Don't call this in a downstream thread unless you don't mind it blowing
         * away other changes you might have recently made in an upstream thread.
         */
        """
        pass

    def clearCache(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_cache(const Geom self)
        
        /**
         * Removes all of the previously-cached results of munge_geom().
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
        clear_cache_stage(const Geom self, Thread current_thread)
        
        /**
         * Removes all of the previously-cached results of munge_geom(), at the
         * current pipeline stage and upstream.  Does not affect the downstream cache.
         *
         * Don't call this in a downstream thread unless you don't mind it blowing
         * away other changes you might have recently made in an upstream thread.
         */
        """
        pass

    def clearPrimitives(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_primitives(const Geom self)
        
        /**
         * Removes all the primitives from the Geom object (but keeps the same table
         * of vertices).  You may then re-add primitives one at a time via calls to
         * add_primitive().
         *
         * Don't call this in a downstream thread unless you don't mind it blowing
         * away other changes you might have recently made in an upstream thread.
         */
        """
        pass

    def clear_bounds(self, const_Geom_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_bounds(const Geom self)
        
        /**
         * Reverses the effect of a previous call to set_bounds(), and allows the
         * bounding volume to be automatically computed once more based on the
         * vertices.
         *
         * Don't call this in a downstream thread unless you don't mind it blowing
         * away other changes you might have recently made in an upstream thread.
         */
        """
        pass

    def clear_cache(self, const_Geom_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_cache(const Geom self)
        
        /**
         * Removes all of the previously-cached results of munge_geom().
         *
         * This blows away the entire cache, upstream and downstream the pipeline.
         * Use clear_cache_stage() instead if you only want to blow away the cache at
         * the current stage and upstream.
         */
        """
        pass

    def clear_cache_stage(self, const_Geom_self, Thread_current_thread): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_cache_stage(const Geom self, Thread current_thread)
        
        /**
         * Removes all of the previously-cached results of munge_geom(), at the
         * current pipeline stage and upstream.  Does not affect the downstream cache.
         *
         * Don't call this in a downstream thread unless you don't mind it blowing
         * away other changes you might have recently made in an upstream thread.
         */
        """
        pass

    def clear_primitives(self, const_Geom_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_primitives(const Geom self)
        
        /**
         * Removes all the primitives from the Geom object (but keeps the same table
         * of vertices).  You may then re-add primitives one at a time via calls to
         * add_primitive().
         *
         * Don't call this in a downstream thread unless you don't mind it blowing
         * away other changes you might have recently made in an upstream thread.
         */
        """
        pass

    def copyPrimitivesFrom(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        copy_primitives_from(const Geom self, const Geom other)
        
        /**
         * Copies the primitives from the indicated Geom into this one.  This does
         * require that both Geoms contain the same fundamental type primitives, both
         * have a compatible shade model, and both use the same GeomVertexData.  Both
         * Geoms must also be the same specific class type (i.e.  if one is a
         * GeomTextGlyph, they both must be.)
         *
         * Returns true if the copy is successful, or false otherwise (because the
         * Geoms were mismatched).
         */
        """
        pass

    def copy_primitives_from(self, const_Geom_self, const_Geom_other): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        copy_primitives_from(const Geom self, const Geom other)
        
        /**
         * Copies the primitives from the indicated Geom into this one.  This does
         * require that both Geoms contain the same fundamental type primitives, both
         * have a compatible shade model, and both use the same GeomVertexData.  Both
         * Geoms must also be the same specific class type (i.e.  if one is a
         * GeomTextGlyph, they both must be.)
         *
         * Returns true if the copy is successful, or false otherwise (because the
         * Geoms were mismatched).
         */
        """
        pass

    def decompose(self, Geom_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        decompose(Geom self)
        
        /**
         * Decomposes all of the primitives within this Geom, returning the result.
         * See GeomPrimitive::decompose().
         */
        """
        pass

    def decomposeInPlace(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        decompose_in_place(const Geom self)
        
        /**
         * Decomposes all of the primitives within this Geom, leaving the results in
         * place.  See GeomPrimitive::decompose().
         *
         * Don't call this in a downstream thread unless you don't mind it blowing
         * away other changes you might have recently made in an upstream thread.
         */
        """
        pass

    def decompose_in_place(self, const_Geom_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        decompose_in_place(const Geom self)
        
        /**
         * Decomposes all of the primitives within this Geom, leaving the results in
         * place.  See GeomPrimitive::decompose().
         *
         * Don't call this in a downstream thread unless you don't mind it blowing
         * away other changes you might have recently made in an upstream thread.
         */
        """
        pass

    def doubleside(self, Geom_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        doubleside(Geom self)
        
        /**
         * Doublesides all of the primitives within this Geom, returning the result.
         * See GeomPrimitive::doubleside().
         */
        """
        pass

    def doublesideInPlace(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        doubleside_in_place(const Geom self)
        
        /**
         * Doublesides all of the primitives within this Geom, leaving the results in
         * place.  See GeomPrimitive::doubleside().
         *
         * Don't call this in a downstream thread unless you don't mind it blowing
         * away other changes you might have recently made in an upstream thread.
         */
        """
        pass

    def doubleside_in_place(self, const_Geom_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        doubleside_in_place(const Geom self)
        
        /**
         * Doublesides all of the primitives within this Geom, leaving the results in
         * place.  See GeomPrimitive::doubleside().
         *
         * Don't call this in a downstream thread unless you don't mind it blowing
         * away other changes you might have recently made in an upstream thread.
         */
        """
        pass

    def getAnimatedVertexData(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_animated_vertex_data(Geom self, bool force, Thread current_thread)
        
        /**
         * Returns a GeomVertexData that represents the results of computing the
         * vertex animation on the CPU for this Geom's vertex data.
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

    def getBounds(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_bounds(Geom self, Thread current_thread)
        
        /**
         * Returns the bounding volume for the Geom.
         */
        """
        pass

    def getBoundsType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_bounds_type(Geom self)
        
        /**
         * Returns the bounding volume type set with set_bounds_type().
         */
        """
        pass

    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getGeomRendering(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_geom_rendering(Geom self)
        
        /**
         * Returns the set of GeomRendering bits that represent the rendering
         * properties required to properly render this Geom.
         */
        """
        pass

    def getModified(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_modified(Geom self, Thread current_thread)
        
        /**
         * Returns a sequence number which is guaranteed to change at least every time
         * any of the primitives in the Geom is modified, or the set of primitives is
         * modified.  However, this does not include modifications to the vertex data,
         * which should be tested separately.
         */
        """
        pass

    def getNestedVertices(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_nested_vertices(Geom self, Thread current_thread)
        
        /**
         * Returns the number of vertices rendered by all primitives within the Geom.
         */
        """
        pass

    def getNumBytes(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_bytes(Geom self)
        
        /**
         * Returns the number of bytes consumed by the geom and its primitives (but
         * not including its vertex table).
         */
        """
        pass

    def getNumPrimitives(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_primitives(Geom self)
        
        /**
         * Returns the number of GeomPrimitive objects stored within the Geom, each of
         * which represents a number of primitives of a particular type.
         */
        """
        pass

    def getPrimitive(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_primitive(Geom self, int i)
        
        /**
         * Returns a const pointer to the ith GeomPrimitive object stored within the
         * Geom.  Use this call only to inspect the ith object; use modify_primitive()
         * or set_primitive() if you want to modify it.
         */
        """
        pass

    def getPrimitives(self, *args, **kwargs): # real signature unknown
        pass

    def getPrimitiveType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_primitive_type(Geom self)
        
        /**
         * Returns the fundamental primitive type that is common to all GeomPrimitives
         * added within the Geom.  All nested primitives within a particular Geom must
         * be the same type (that is, you can mix triangles and tristrips, because
         * they are both the same fundamental type PT_polygons, but you cannot mix
         * triangles and points withn the same Geom).
         */
        """
        pass

    def getShadeModel(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_shade_model(Geom self)
        
        /**
         * Returns the shade model common to all of the individual GeomPrimitives that
         * have been added to the geom.
         */
        """
        pass

    def getUsageHint(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_usage_hint(Geom self)
        
        /**
         * Returns the minimum (i.e.  most dynamic) usage_hint among all of the
         * individual GeomPrimitives that have been added to the geom.
         * @deprecated  This is no longer very useful.
         */
        """
        pass

    def getVertexData(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_vertex_data(Geom self, Thread current_thread)
        
        /**
         * Returns a const pointer to the GeomVertexData, for application code to
         * directly examine (but not modify) the geom's underlying data.
         */
        """
        pass

    def get_animated_vertex_data(self, Geom_self, bool_force, Thread_current_thread): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_animated_vertex_data(Geom self, bool force, Thread current_thread)
        
        /**
         * Returns a GeomVertexData that represents the results of computing the
         * vertex animation on the CPU for this Geom's vertex data.
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

    def get_bounds(self, Geom_self, Thread_current_thread): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_bounds(Geom self, Thread current_thread)
        
        /**
         * Returns the bounding volume for the Geom.
         */
        """
        pass

    def get_bounds_type(self, Geom_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_bounds_type(Geom self)
        
        /**
         * Returns the bounding volume type set with set_bounds_type().
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_geom_rendering(self, Geom_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_geom_rendering(Geom self)
        
        /**
         * Returns the set of GeomRendering bits that represent the rendering
         * properties required to properly render this Geom.
         */
        """
        pass

    def get_modified(self, Geom_self, Thread_current_thread): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_modified(Geom self, Thread current_thread)
        
        /**
         * Returns a sequence number which is guaranteed to change at least every time
         * any of the primitives in the Geom is modified, or the set of primitives is
         * modified.  However, this does not include modifications to the vertex data,
         * which should be tested separately.
         */
        """
        pass

    def get_nested_vertices(self, Geom_self, Thread_current_thread): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_nested_vertices(Geom self, Thread current_thread)
        
        /**
         * Returns the number of vertices rendered by all primitives within the Geom.
         */
        """
        pass

    def get_num_bytes(self, Geom_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_bytes(Geom self)
        
        /**
         * Returns the number of bytes consumed by the geom and its primitives (but
         * not including its vertex table).
         */
        """
        pass

    def get_num_primitives(self, Geom_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_primitives(Geom self)
        
        /**
         * Returns the number of GeomPrimitive objects stored within the Geom, each of
         * which represents a number of primitives of a particular type.
         */
        """
        pass

    def get_primitive(self, Geom_self, int_i): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_primitive(Geom self, int i)
        
        /**
         * Returns a const pointer to the ith GeomPrimitive object stored within the
         * Geom.  Use this call only to inspect the ith object; use modify_primitive()
         * or set_primitive() if you want to modify it.
         */
        """
        pass

    def get_primitives(self, *args, **kwargs): # real signature unknown
        pass

    def get_primitive_type(self, Geom_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_primitive_type(Geom self)
        
        /**
         * Returns the fundamental primitive type that is common to all GeomPrimitives
         * added within the Geom.  All nested primitives within a particular Geom must
         * be the same type (that is, you can mix triangles and tristrips, because
         * they are both the same fundamental type PT_polygons, but you cannot mix
         * triangles and points withn the same Geom).
         */
        """
        pass

    def get_shade_model(self, Geom_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_shade_model(Geom self)
        
        /**
         * Returns the shade model common to all of the individual GeomPrimitives that
         * have been added to the geom.
         */
        """
        pass

    def get_usage_hint(self, Geom_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_usage_hint(Geom self)
        
        /**
         * Returns the minimum (i.e.  most dynamic) usage_hint among all of the
         * individual GeomPrimitives that have been added to the geom.
         * @deprecated  This is no longer very useful.
         */
        """
        pass

    def get_vertex_data(self, Geom_self, Thread_current_thread): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_vertex_data(Geom self, Thread current_thread)
        
        /**
         * Returns a const pointer to the GeomVertexData, for application code to
         * directly examine (but not modify) the geom's underlying data.
         */
        """
        pass

    def insertPrimitive(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        insert_primitive(const Geom self, int i, const GeomPrimitive primitive)
        
        /**
         * Inserts a new GeomPrimitive structure to the Geom object.  This specifies a
         * particular subset of vertices that are used to define geometric primitives
         * of the indicated type.
         *
         * Don't call this in a downstream thread unless you don't mind it blowing
         * away other changes you might have recently made in an upstream thread.
         */
        """
        pass

    def insert_primitive(self, const_Geom_self, int_i, const_GeomPrimitive_primitive): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        insert_primitive(const Geom self, int i, const GeomPrimitive primitive)
        
        /**
         * Inserts a new GeomPrimitive structure to the Geom object.  This specifies a
         * particular subset of vertices that are used to define geometric primitives
         * of the indicated type.
         *
         * Don't call this in a downstream thread unless you don't mind it blowing
         * away other changes you might have recently made in an upstream thread.
         */
        """
        pass

    def isEmpty(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_empty(Geom self)
        
        /**
         * Returns true if there appear to be no vertices to be rendered by this Geom,
         * false if has some actual data.
         */
        """
        pass

    def isPrepared(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_prepared(Geom self, PreparedGraphicsObjects prepared_objects)
        
        /**
         * Returns true if the geom has already been prepared or enqueued for
         * preparation on the indicated GSG, false otherwise.
         */
        """
        pass

    def is_empty(self, Geom_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_empty(Geom self)
        
        /**
         * Returns true if there appear to be no vertices to be rendered by this Geom,
         * false if has some actual data.
         */
        """
        pass

    def is_prepared(self, Geom_self, PreparedGraphicsObjects_prepared_objects): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_prepared(Geom self, PreparedGraphicsObjects prepared_objects)
        
        /**
         * Returns true if the geom has already been prepared or enqueued for
         * preparation on the indicated GSG, false otherwise.
         */
        """
        pass

    def makeAdjacency(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        make_adjacency(Geom self)
        
        /**
         * Returns a new Geom with each primitive converted into a corresponding
         * version with adjacency information.
         *
         * @since 1.10.0
         */
        """
        pass

    def makeAdjacencyInPlace(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        make_adjacency_in_place(const Geom self)
        
        /**
         * Replaces the GeomPrimitives within this Geom with corresponding versions
         * with adjacency information.  See GeomPrimitive::make_adjacency().
         *
         * Don't call this in a downstream thread unless you don't mind it blowing
         * away other changes you might have recently made in an upstream thread.
         *
         * @since 1.10.0
         */
        """
        pass

    def makeCopy(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        make_copy(Geom self)
        
        /**
         * Returns a newly-allocated Geom that is a shallow copy of this one.  It will
         * be a different Geom pointer, but its internal data may or may not be shared
         * with that of the original Geom.
         */
        """
        pass

    def makeLines(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        make_lines(Geom self)
        
        /**
         * Returns a new Geom with lines at all the edges.  See
         * GeomPrimitive::make_lines().
         */
        """
        pass

    def makeLinesInPlace(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        make_lines_in_place(const Geom self)
        
        /**
         * Replaces the GeomPrimitives within this Geom with corresponding GeomLines,
         * representing a wireframe of the primitives.  See
         * GeomPrimitive::make_lines().
         *
         * Don't call this in a downstream thread unless you don't mind it blowing
         * away other changes you might have recently made in an upstream thread.
         */
        """
        pass

    def makeNonindexed(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        make_nonindexed(const Geom self, bool composite_only)
        
        /**
         * Converts the geom from indexed to nonindexed by duplicating vertices as
         * necessary.  If composite_only is true, then only composite primitives such
         * as trifans and tristrips are converted.  Returns the number of
         * GeomPrimitive objects converted.
         *
         * Don't call this in a downstream thread unless you don't mind it blowing
         * away other changes you might have recently made in an upstream thread.
         */
        """
        pass

    def makePatches(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        make_patches(Geom self)
        
        /**
         * Returns a new Geom with each primitive converted into a patch.  Calls
         * decompose() first.
         */
        """
        pass

    def makePatchesInPlace(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        make_patches_in_place(const Geom self)
        
        /**
         * Replaces the GeomPrimitives within this Geom with corresponding
         * GeomPatches.  See GeomPrimitive::make_patches().
         *
         * Don't call this in a downstream thread unless you don't mind it blowing
         * away other changes you might have recently made in an upstream thread.
         */
        """
        pass

    def makePoints(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        make_points(Geom self)
        
        /**
         * Returns a new Geom with points at all the vertices.  See
         * GeomPrimitive::make_points().
         */
        """
        pass

    def makePointsInPlace(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        make_points_in_place(const Geom self)
        
        /**
         * Replaces the GeomPrimitives within this Geom with corresponding GeomPoints.
         * See GeomPrimitive::make_points().
         *
         * Don't call this in a downstream thread unless you don't mind it blowing
         * away other changes you might have recently made in an upstream thread.
         */
        """
        pass

    def make_adjacency(self, Geom_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        make_adjacency(Geom self)
        
        /**
         * Returns a new Geom with each primitive converted into a corresponding
         * version with adjacency information.
         *
         * @since 1.10.0
         */
        """
        pass

    def make_adjacency_in_place(self, const_Geom_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        make_adjacency_in_place(const Geom self)
        
        /**
         * Replaces the GeomPrimitives within this Geom with corresponding versions
         * with adjacency information.  See GeomPrimitive::make_adjacency().
         *
         * Don't call this in a downstream thread unless you don't mind it blowing
         * away other changes you might have recently made in an upstream thread.
         *
         * @since 1.10.0
         */
        """
        pass

    def make_copy(self, Geom_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        make_copy(Geom self)
        
        /**
         * Returns a newly-allocated Geom that is a shallow copy of this one.  It will
         * be a different Geom pointer, but its internal data may or may not be shared
         * with that of the original Geom.
         */
        """
        pass

    def make_lines(self, Geom_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        make_lines(Geom self)
        
        /**
         * Returns a new Geom with lines at all the edges.  See
         * GeomPrimitive::make_lines().
         */
        """
        pass

    def make_lines_in_place(self, const_Geom_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        make_lines_in_place(const Geom self)
        
        /**
         * Replaces the GeomPrimitives within this Geom with corresponding GeomLines,
         * representing a wireframe of the primitives.  See
         * GeomPrimitive::make_lines().
         *
         * Don't call this in a downstream thread unless you don't mind it blowing
         * away other changes you might have recently made in an upstream thread.
         */
        """
        pass

    def make_nonindexed(self, const_Geom_self, bool_composite_only): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        make_nonindexed(const Geom self, bool composite_only)
        
        /**
         * Converts the geom from indexed to nonindexed by duplicating vertices as
         * necessary.  If composite_only is true, then only composite primitives such
         * as trifans and tristrips are converted.  Returns the number of
         * GeomPrimitive objects converted.
         *
         * Don't call this in a downstream thread unless you don't mind it blowing
         * away other changes you might have recently made in an upstream thread.
         */
        """
        pass

    def make_patches(self, Geom_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        make_patches(Geom self)
        
        /**
         * Returns a new Geom with each primitive converted into a patch.  Calls
         * decompose() first.
         */
        """
        pass

    def make_patches_in_place(self, const_Geom_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        make_patches_in_place(const Geom self)
        
        /**
         * Replaces the GeomPrimitives within this Geom with corresponding
         * GeomPatches.  See GeomPrimitive::make_patches().
         *
         * Don't call this in a downstream thread unless you don't mind it blowing
         * away other changes you might have recently made in an upstream thread.
         */
        """
        pass

    def make_points(self, Geom_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        make_points(Geom self)
        
        /**
         * Returns a new Geom with points at all the vertices.  See
         * GeomPrimitive::make_points().
         */
        """
        pass

    def make_points_in_place(self, const_Geom_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        make_points_in_place(const Geom self)
        
        /**
         * Replaces the GeomPrimitives within this Geom with corresponding GeomPoints.
         * See GeomPrimitive::make_points().
         *
         * Don't call this in a downstream thread unless you don't mind it blowing
         * away other changes you might have recently made in an upstream thread.
         */
        """
        pass

    def markBoundsStale(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        mark_bounds_stale(Geom self)
        
        /**
         * Marks the bounding volume of the Geom as stale so that it should be
         * recomputed.  Usually it is not necessary to call this explicitly.
         */
        """
        pass

    def mark_bounds_stale(self, Geom_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        mark_bounds_stale(Geom self)
        
        /**
         * Marks the bounding volume of the Geom as stale so that it should be
         * recomputed.  Usually it is not necessary to call this explicitly.
         */
        """
        pass

    def modifyPrimitive(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        modify_primitive(const Geom self, int i)
        
        /**
         * Returns a modifiable pointer to the ith GeomPrimitive object stored within
         * the Geom, so application code can directly manipulate the properties of
         * this primitive.
         *
         * Don't call this in a downstream thread unless you don't mind it blowing
         * away other changes you might have recently made in an upstream thread.
         */
        """
        pass

    def modifyVertexData(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        modify_vertex_data(const Geom self)
        
        /**
         * Returns a modifiable pointer to the GeomVertexData, so that application
         * code may directly maniuplate the geom's underlying data.
         *
         * Don't call this in a downstream thread unless you don't mind it blowing
         * away other changes you might have recently made in an upstream thread.
         */
        """
        pass

    def modify_primitive(self, const_Geom_self, int_i): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        modify_primitive(const Geom self, int i)
        
        /**
         * Returns a modifiable pointer to the ith GeomPrimitive object stored within
         * the Geom, so application code can directly manipulate the properties of
         * this primitive.
         *
         * Don't call this in a downstream thread unless you don't mind it blowing
         * away other changes you might have recently made in an upstream thread.
         */
        """
        pass

    def modify_vertex_data(self, const_Geom_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        modify_vertex_data(const Geom self)
        
        /**
         * Returns a modifiable pointer to the GeomVertexData, so that application
         * code may directly maniuplate the geom's underlying data.
         *
         * Don't call this in a downstream thread unless you don't mind it blowing
         * away other changes you might have recently made in an upstream thread.
         */
        """
        pass

    def offsetVertices(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        offset_vertices(const Geom self, const GeomVertexData data, int offset)
        
        /**
         * Replaces a Geom's vertex table with a new table, and simultaneously adds
         * the indicated offset to all vertex references within the Geom's primitives.
         * This is intended to be used to combine multiple GeomVertexDatas from
         * different Geoms into a single big buffer, with each Geom referencing a
         * subset of the vertices in the buffer.
         *
         * Don't call this in a downstream thread unless you don't mind it blowing
         * away other changes you might have recently made in an upstream thread.
         */
        """
        pass

    def offset_vertices(self, const_Geom_self, const_GeomVertexData_data, int_offset): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        offset_vertices(const Geom self, const GeomVertexData data, int offset)
        
        /**
         * Replaces a Geom's vertex table with a new table, and simultaneously adds
         * the indicated offset to all vertex references within the Geom's primitives.
         * This is intended to be used to combine multiple GeomVertexDatas from
         * different Geoms into a single big buffer, with each Geom referencing a
         * subset of the vertices in the buffer.
         *
         * Don't call this in a downstream thread unless you don't mind it blowing
         * away other changes you might have recently made in an upstream thread.
         */
        """
        pass

    def output(self, Geom_self, ostream_out): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        output(Geom self, ostream out)
        
        /**
         *
         */
        """
        pass

    def prepare(self, const_Geom_self, PreparedGraphicsObjects_prepared_objects): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        prepare(const Geom self, PreparedGraphicsObjects prepared_objects)
        
        /**
         * Indicates that the geom should be enqueued to be prepared in the indicated
         * prepared_objects at the beginning of the next frame.  This will ensure the
         * geom is already loaded into geom memory if it is expected to be rendered
         * soon.
         *
         * Use this function instead of prepare_now() to preload geoms from a user
         * interface standpoint.
         */
        """
        pass

    def prepareNow(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        prepare_now(const Geom self, PreparedGraphicsObjects prepared_objects, GraphicsStateGuardianBase gsg)
        
        /**
         * Creates a context for the geom on the particular GSG, if it does not
         * already exist.  Returns the new (or old) GeomContext.  This assumes that
         * the GraphicsStateGuardian is the currently active rendering context and
         * that it is ready to accept new geoms.  If this is not necessarily the case,
         * you should use prepare() instead.
         *
         * Normally, this is not called directly except by the GraphicsStateGuardian;
         * a geom does not need to be explicitly prepared by the user before it may be
         * rendered.
         */
        """
        pass

    def prepare_now(self, const_Geom_self, PreparedGraphicsObjects_prepared_objects, GraphicsStateGuardianBase_gsg): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        prepare_now(const Geom self, PreparedGraphicsObjects prepared_objects, GraphicsStateGuardianBase gsg)
        
        /**
         * Creates a context for the geom on the particular GSG, if it does not
         * already exist.  Returns the new (or old) GeomContext.  This assumes that
         * the GraphicsStateGuardian is the currently active rendering context and
         * that it is ready to accept new geoms.  If this is not necessarily the case,
         * you should use prepare() instead.
         *
         * Normally, this is not called directly except by the GraphicsStateGuardian;
         * a geom does not need to be explicitly prepared by the user before it may be
         * rendered.
         */
        """
        pass

    def release(self, const_Geom_self, PreparedGraphicsObjects_prepared_objects): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        release(const Geom self, PreparedGraphicsObjects prepared_objects)
        
        /**
         * Frees the geom context only on the indicated object, if it exists there.
         * Returns true if it was released, false if it had not been prepared.
         */
        """
        pass

    def releaseAll(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        release_all(const Geom self)
        
        /**
         * Frees the context allocated on all objects for which the geom has been
         * declared.  Returns the number of contexts which have been freed.
         */
        """
        pass

    def release_all(self, const_Geom_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        release_all(const Geom self)
        
        /**
         * Frees the context allocated on all objects for which the geom has been
         * declared.  Returns the number of contexts which have been freed.
         */
        """
        pass

    def removePrimitive(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        remove_primitive(const Geom self, int i)
        
        /**
         * Removes the ith primitive from the list.
         *
         * Don't call this in a downstream thread unless you don't mind it blowing
         * away other changes you might have recently made in an upstream thread.
         */
        """
        pass

    def remove_primitive(self, const_Geom_self, int_i): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        remove_primitive(const Geom self, int i)
        
        /**
         * Removes the ith primitive from the list.
         *
         * Don't call this in a downstream thread unless you don't mind it blowing
         * away other changes you might have recently made in an upstream thread.
         */
        """
        pass

    def requestResident(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        request_resident(Geom self)
        
        /**
         * Returns true if all the primitive arrays are currently resident in memory.
         * If this returns false, the data will be brought back into memory shortly;
         * try again later.
         *
         * This does not also test the Geom's associated GeomVertexData.  That must be
         * tested separately.
         */
        """
        pass

    def request_resident(self, Geom_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        request_resident(Geom self)
        
        /**
         * Returns true if all the primitive arrays are currently resident in memory.
         * If this returns false, the data will be brought back into memory shortly;
         * try again later.
         *
         * This does not also test the Geom's associated GeomVertexData.  That must be
         * tested separately.
         */
        """
        pass

    def reverse(self, Geom_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        reverse(Geom self)
        
        /**
         * Reverses all of the primitives within this Geom, returning the result.  See
         * GeomPrimitive::reverse().
         */
        """
        pass

    def reverseInPlace(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        reverse_in_place(const Geom self)
        
        /**
         * Reverses all of the primitives within this Geom, leaving the results in
         * place.  See GeomPrimitive::reverse().
         *
         * Don't call this in a downstream thread unless you don't mind it blowing
         * away other changes you might have recently made in an upstream thread.
         */
        """
        pass

    def reverse_in_place(self, const_Geom_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        reverse_in_place(const Geom self)
        
        /**
         * Reverses all of the primitives within this Geom, leaving the results in
         * place.  See GeomPrimitive::reverse().
         *
         * Don't call this in a downstream thread unless you don't mind it blowing
         * away other changes you might have recently made in an upstream thread.
         */
        """
        pass

    def rotate(self, Geom_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        rotate(Geom self)
        
        /**
         * Rotates all of the primitives within this Geom, returning the result.  See
         * GeomPrimitive::rotate().
         */
        """
        pass

    def rotateInPlace(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        rotate_in_place(const Geom self)
        
        /**
         * Rotates all of the primitives within this Geom, leaving the results in
         * place.  See GeomPrimitive::rotate().
         *
         * Don't call this in a downstream thread unless you don't mind it blowing
         * away other changes you might have recently made in an upstream thread.
         */
        """
        pass

    def rotate_in_place(self, const_Geom_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        rotate_in_place(const Geom self)
        
        /**
         * Rotates all of the primitives within this Geom, leaving the results in
         * place.  See GeomPrimitive::rotate().
         *
         * Don't call this in a downstream thread unless you don't mind it blowing
         * away other changes you might have recently made in an upstream thread.
         */
        """
        pass

    def setBounds(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_bounds(const Geom self, const BoundingVolume volume)
        
        /**
         * Resets the bounding volume so that it is the indicated volume.  When it is
         * explicitly set, the bounding volume will no longer be automatically
         * computed; call clear_bounds() if you would like to return the bounding
         * volume to its default behavior.
         *
         * Don't call this in a downstream thread unless you don't mind it blowing
         * away other changes you might have recently made in an upstream thread.
         */
        """
        pass

    def setBoundsType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_bounds_type(const Geom self, int bounds_type)
        
        /**
         * Specifies the desired type of bounding volume that will be created for this
         * Geom.  This is normally BoundingVolume::BT_default, which means to set the
         * type according to the config variable "bounds-type".
         *
         * If this is BT_sphere or BT_box, a BoundingSphere or BoundingBox is
         * explicitly created.  If it is BT_best, a BoundingBox is created.
         *
         * This affects the implicit bounding volume only.  If an explicit bounding
         * volume is set on the Geom with set_bounds(), that bounding volume type is
         * used.  (This is different behavior from the similar method on PandaNode.)
         */
        """
        pass

    def setPrimitive(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_primitive(const Geom self, int i, const GeomPrimitive primitive)
        
        /**
         * Replaces the ith GeomPrimitive object stored within the Geom with the new
         * object.
         *
         * Don't call this in a downstream thread unless you don't mind it blowing
         * away other changes you might have recently made in an upstream thread.
         */
        """
        pass

    def setUsageHint(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_usage_hint(const Geom self, int usage_hint)
        
        /**
         * Changes the UsageHint hint for all of the primitives on this Geom to the
         * same value.  See get_usage_hint().
         *
         * Don't call this in a downstream thread unless you don't mind it blowing
         * away other changes you might have recently made in an upstream thread.
         */
        """
        pass

    def setVertexData(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_vertex_data(const Geom self, const GeomVertexData data)
        
        /**
         * Replaces the Geom's underlying vertex data table with a completely new
         * table.
         *
         * Don't call this in a downstream thread unless you don't mind it blowing
         * away other changes you might have recently made in an upstream thread.
         */
        """
        pass

    def set_bounds(self, const_Geom_self, const_BoundingVolume_volume): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_bounds(const Geom self, const BoundingVolume volume)
        
        /**
         * Resets the bounding volume so that it is the indicated volume.  When it is
         * explicitly set, the bounding volume will no longer be automatically
         * computed; call clear_bounds() if you would like to return the bounding
         * volume to its default behavior.
         *
         * Don't call this in a downstream thread unless you don't mind it blowing
         * away other changes you might have recently made in an upstream thread.
         */
        """
        pass

    def set_bounds_type(self, const_Geom_self, int_bounds_type): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_bounds_type(const Geom self, int bounds_type)
        
        /**
         * Specifies the desired type of bounding volume that will be created for this
         * Geom.  This is normally BoundingVolume::BT_default, which means to set the
         * type according to the config variable "bounds-type".
         *
         * If this is BT_sphere or BT_box, a BoundingSphere or BoundingBox is
         * explicitly created.  If it is BT_best, a BoundingBox is created.
         *
         * This affects the implicit bounding volume only.  If an explicit bounding
         * volume is set on the Geom with set_bounds(), that bounding volume type is
         * used.  (This is different behavior from the similar method on PandaNode.)
         */
        """
        pass

    def set_primitive(self, const_Geom_self, int_i, const_GeomPrimitive_primitive): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_primitive(const Geom self, int i, const GeomPrimitive primitive)
        
        /**
         * Replaces the ith GeomPrimitive object stored within the Geom with the new
         * object.
         *
         * Don't call this in a downstream thread unless you don't mind it blowing
         * away other changes you might have recently made in an upstream thread.
         */
        """
        pass

    def set_usage_hint(self, const_Geom_self, int_usage_hint): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_usage_hint(const Geom self, int usage_hint)
        
        /**
         * Changes the UsageHint hint for all of the primitives on this Geom to the
         * same value.  See get_usage_hint().
         *
         * Don't call this in a downstream thread unless you don't mind it blowing
         * away other changes you might have recently made in an upstream thread.
         */
        """
        pass

    def set_vertex_data(self, const_Geom_self, const_GeomVertexData_data): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_vertex_data(const Geom self, const GeomVertexData data)
        
        /**
         * Replaces the Geom's underlying vertex data table with a completely new
         * table.
         *
         * Don't call this in a downstream thread unless you don't mind it blowing
         * away other changes you might have recently made in an upstream thread.
         */
        """
        pass

    def transformVertices(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        transform_vertices(const Geom self, const LMatrix4f mat)
        
        /**
         * Applies the indicated transform to all of the vertices in the Geom.  If the
         * Geom happens to share a vertex table with another Geom, this operation will
         * duplicate the vertex table instead of breaking the other Geom; however, if
         * multiple Geoms with shared tables are transformed by the same matrix, they
         * will no longer share tables after the operation.  Consider using the
         * GeomTransformer if you will be applying the same transform to multiple
         * Geoms.
         */
        """
        pass

    def transform_vertices(self, const_Geom_self, const_LMatrix4f_mat): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        transform_vertices(const Geom self, const LMatrix4f mat)
        
        /**
         * Applies the indicated transform to all of the vertices in the Geom.  If the
         * Geom happens to share a vertex table with another Geom, this operation will
         * duplicate the vertex table instead of breaking the other Geom; however, if
         * multiple Geoms with shared tables are transformed by the same matrix, they
         * will no longer share tables after the operation.  Consider using the
         * GeomTransformer if you will be applying the same transform to multiple
         * Geoms.
         */
        """
        pass

    def unify(self, Geom_self, int_max_indices, bool_preserve_order): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        unify(Geom self, int max_indices, bool preserve_order)
        
        /**
         * Unifies all of the primitives contained within this Geom into a single (or
         * as few as possible, within the constraints of max_indices) primitive
         * objects.  This may require decomposing the primitives if, for instance, the
         * Geom contains both triangle strips and triangle fans.
         *
         * max_indices represents the maximum number of indices that will be put in
         * any one GeomPrimitive.  If preserve_order is true, then the primitives will
         * not be reordered during the operation, even if this results in a suboptimal
         * result.
         */
        """
        pass

    def unifyInPlace(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        unify_in_place(const Geom self, int max_indices, bool preserve_order)
        
        /**
         * Unifies all of the primitives contained within this Geom into a single (or
         * as few as possible, within the constraints of max_indices) primitive
         * objects.  This may require decomposing the primitives if, for instance, the
         * Geom contains both triangle strips and triangle fans.
         *
         * max_indices represents the maximum number of indices that will be put in
         * any one GeomPrimitive.  If preserve_order is true, then the primitives will
         * not be reordered during the operation, even if this results in a suboptimal
         * result.
         *
         * Don't call this in a downstream thread unless you don't mind it blowing
         * away other changes you might have recently made in an upstream thread.
         */
        """
        pass

    def unify_in_place(self, const_Geom_self, int_max_indices, bool_preserve_order): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        unify_in_place(const Geom self, int max_indices, bool preserve_order)
        
        /**
         * Unifies all of the primitives contained within this Geom into a single (or
         * as few as possible, within the constraints of max_indices) primitive
         * objects.  This may require decomposing the primitives if, for instance, the
         * Geom contains both triangle strips and triangle fans.
         *
         * max_indices represents the maximum number of indices that will be put in
         * any one GeomPrimitive.  If preserve_order is true, then the primitives will
         * not be reordered during the operation, even if this results in a suboptimal
         * result.
         *
         * Don't call this in a downstream thread unless you don't mind it blowing
         * away other changes you might have recently made in an upstream thread.
         */
        """
        pass

    def upcastToCopyOnWriteObject(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        upcast_to_CopyOnWriteObject(const Geom self)
        
        upcast from Geom to CopyOnWriteObject
        """
        pass

    def upcastToGeomEnums(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        upcast_to_GeomEnums(const Geom self)
        
        upcast from Geom to GeomEnums
        """
        pass

    def upcast_to_CopyOnWriteObject(self, const_Geom_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        upcast_to_CopyOnWriteObject(const Geom self)
        
        upcast from Geom to CopyOnWriteObject
        """
        pass

    def upcast_to_GeomEnums(self, const_Geom_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        upcast_to_GeomEnums(const Geom self)
        
        upcast from Geom to GeomEnums
        """
        pass

    def write(self, Geom_self, ostream_out, int_indent_level): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        write(Geom self, ostream out, int indent_level)
        
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

    bounds_type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    geom_rendering = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    modified = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    num_bytes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    primitives = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    primitive_type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    shade_model = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.core.Geom' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.core.Geom' objects>"
        '__doc__': '/**\n * A container for geometry primitives.  This class associates one or more\n * GeomPrimitive objects with a table of vertices defined by a GeomVertexData\n * object.  All of the primitives stored in a particular Geom are drawn from\n * the same set of vertices (each primitive uses a subset of all of the\n * vertices in the table), and all of them must be rendered at the same time,\n * in the same graphics state.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.Geom' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE2FCE70>'
        '__repr__': None, # (!) real value is "<slot wrapper '__repr__' of 'panda3d.core.Geom' objects>"
        '__str__': None, # (!) real value is "<slot wrapper '__str__' of 'panda3d.core.Geom' objects>"
        'addPrimitive': None, # (!) real value is "<method 'addPrimitive' of 'panda3d.core.Geom' objects>"
        'add_primitive': None, # (!) real value is "<method 'add_primitive' of 'panda3d.core.Geom' objects>"
        'assign': None, # (!) real value is "<method 'assign' of 'panda3d.core.Geom' objects>"
        'bounds_type': None, # (!) real value is "<attribute 'bounds_type' of 'panda3d.core.Geom' objects>"
        'checkValid': None, # (!) real value is "<method 'checkValid' of 'panda3d.core.Geom' objects>"
        'check_valid': None, # (!) real value is "<method 'check_valid' of 'panda3d.core.Geom' objects>"
        'clearBounds': None, # (!) real value is "<method 'clearBounds' of 'panda3d.core.Geom' objects>"
        'clearCache': None, # (!) real value is "<method 'clearCache' of 'panda3d.core.Geom' objects>"
        'clearCacheStage': None, # (!) real value is "<method 'clearCacheStage' of 'panda3d.core.Geom' objects>"
        'clearPrimitives': None, # (!) real value is "<method 'clearPrimitives' of 'panda3d.core.Geom' objects>"
        'clear_bounds': None, # (!) real value is "<method 'clear_bounds' of 'panda3d.core.Geom' objects>"
        'clear_cache': None, # (!) real value is "<method 'clear_cache' of 'panda3d.core.Geom' objects>"
        'clear_cache_stage': None, # (!) real value is "<method 'clear_cache_stage' of 'panda3d.core.Geom' objects>"
        'clear_primitives': None, # (!) real value is "<method 'clear_primitives' of 'panda3d.core.Geom' objects>"
        'copyPrimitivesFrom': None, # (!) real value is "<method 'copyPrimitivesFrom' of 'panda3d.core.Geom' objects>"
        'copy_primitives_from': None, # (!) real value is "<method 'copy_primitives_from' of 'panda3d.core.Geom' objects>"
        'decompose': None, # (!) real value is "<method 'decompose' of 'panda3d.core.Geom' objects>"
        'decomposeInPlace': None, # (!) real value is "<method 'decomposeInPlace' of 'panda3d.core.Geom' objects>"
        'decompose_in_place': None, # (!) real value is "<method 'decompose_in_place' of 'panda3d.core.Geom' objects>"
        'doubleside': None, # (!) real value is "<method 'doubleside' of 'panda3d.core.Geom' objects>"
        'doublesideInPlace': None, # (!) real value is "<method 'doublesideInPlace' of 'panda3d.core.Geom' objects>"
        'doubleside_in_place': None, # (!) real value is "<method 'doubleside_in_place' of 'panda3d.core.Geom' objects>"
        'geom_rendering': None, # (!) real value is "<attribute 'geom_rendering' of 'panda3d.core.Geom' objects>"
        'getAnimatedVertexData': None, # (!) real value is "<method 'getAnimatedVertexData' of 'panda3d.core.Geom' objects>"
        'getBounds': None, # (!) real value is "<method 'getBounds' of 'panda3d.core.Geom' objects>"
        'getBoundsType': None, # (!) real value is "<method 'getBoundsType' of 'panda3d.core.Geom' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE2FCE70>)>'
        'getGeomRendering': None, # (!) real value is "<method 'getGeomRendering' of 'panda3d.core.Geom' objects>"
        'getModified': None, # (!) real value is "<method 'getModified' of 'panda3d.core.Geom' objects>"
        'getNestedVertices': None, # (!) real value is "<method 'getNestedVertices' of 'panda3d.core.Geom' objects>"
        'getNumBytes': None, # (!) real value is "<method 'getNumBytes' of 'panda3d.core.Geom' objects>"
        'getNumPrimitives': None, # (!) real value is "<method 'getNumPrimitives' of 'panda3d.core.Geom' objects>"
        'getPrimitive': None, # (!) real value is "<method 'getPrimitive' of 'panda3d.core.Geom' objects>"
        'getPrimitiveType': None, # (!) real value is "<method 'getPrimitiveType' of 'panda3d.core.Geom' objects>"
        'getPrimitives': None, # (!) real value is "<method 'getPrimitives' of 'panda3d.core.Geom' objects>"
        'getShadeModel': None, # (!) real value is "<method 'getShadeModel' of 'panda3d.core.Geom' objects>"
        'getUsageHint': None, # (!) real value is "<method 'getUsageHint' of 'panda3d.core.Geom' objects>"
        'getVertexData': None, # (!) real value is "<method 'getVertexData' of 'panda3d.core.Geom' objects>"
        'get_animated_vertex_data': None, # (!) real value is "<method 'get_animated_vertex_data' of 'panda3d.core.Geom' objects>"
        'get_bounds': None, # (!) real value is "<method 'get_bounds' of 'panda3d.core.Geom' objects>"
        'get_bounds_type': None, # (!) real value is "<method 'get_bounds_type' of 'panda3d.core.Geom' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE2FCE70>)>'
        'get_geom_rendering': None, # (!) real value is "<method 'get_geom_rendering' of 'panda3d.core.Geom' objects>"
        'get_modified': None, # (!) real value is "<method 'get_modified' of 'panda3d.core.Geom' objects>"
        'get_nested_vertices': None, # (!) real value is "<method 'get_nested_vertices' of 'panda3d.core.Geom' objects>"
        'get_num_bytes': None, # (!) real value is "<method 'get_num_bytes' of 'panda3d.core.Geom' objects>"
        'get_num_primitives': None, # (!) real value is "<method 'get_num_primitives' of 'panda3d.core.Geom' objects>"
        'get_primitive': None, # (!) real value is "<method 'get_primitive' of 'panda3d.core.Geom' objects>"
        'get_primitive_type': None, # (!) real value is "<method 'get_primitive_type' of 'panda3d.core.Geom' objects>"
        'get_primitives': None, # (!) real value is "<method 'get_primitives' of 'panda3d.core.Geom' objects>"
        'get_shade_model': None, # (!) real value is "<method 'get_shade_model' of 'panda3d.core.Geom' objects>"
        'get_usage_hint': None, # (!) real value is "<method 'get_usage_hint' of 'panda3d.core.Geom' objects>"
        'get_vertex_data': None, # (!) real value is "<method 'get_vertex_data' of 'panda3d.core.Geom' objects>"
        'insertPrimitive': None, # (!) real value is "<method 'insertPrimitive' of 'panda3d.core.Geom' objects>"
        'insert_primitive': None, # (!) real value is "<method 'insert_primitive' of 'panda3d.core.Geom' objects>"
        'isEmpty': None, # (!) real value is "<method 'isEmpty' of 'panda3d.core.Geom' objects>"
        'isPrepared': None, # (!) real value is "<method 'isPrepared' of 'panda3d.core.Geom' objects>"
        'is_empty': None, # (!) real value is "<method 'is_empty' of 'panda3d.core.Geom' objects>"
        'is_prepared': None, # (!) real value is "<method 'is_prepared' of 'panda3d.core.Geom' objects>"
        'makeAdjacency': None, # (!) real value is "<method 'makeAdjacency' of 'panda3d.core.Geom' objects>"
        'makeAdjacencyInPlace': None, # (!) real value is "<method 'makeAdjacencyInPlace' of 'panda3d.core.Geom' objects>"
        'makeCopy': None, # (!) real value is "<method 'makeCopy' of 'panda3d.core.Geom' objects>"
        'makeLines': None, # (!) real value is "<method 'makeLines' of 'panda3d.core.Geom' objects>"
        'makeLinesInPlace': None, # (!) real value is "<method 'makeLinesInPlace' of 'panda3d.core.Geom' objects>"
        'makeNonindexed': None, # (!) real value is "<method 'makeNonindexed' of 'panda3d.core.Geom' objects>"
        'makePatches': None, # (!) real value is "<method 'makePatches' of 'panda3d.core.Geom' objects>"
        'makePatchesInPlace': None, # (!) real value is "<method 'makePatchesInPlace' of 'panda3d.core.Geom' objects>"
        'makePoints': None, # (!) real value is "<method 'makePoints' of 'panda3d.core.Geom' objects>"
        'makePointsInPlace': None, # (!) real value is "<method 'makePointsInPlace' of 'panda3d.core.Geom' objects>"
        'make_adjacency': None, # (!) real value is "<method 'make_adjacency' of 'panda3d.core.Geom' objects>"
        'make_adjacency_in_place': None, # (!) real value is "<method 'make_adjacency_in_place' of 'panda3d.core.Geom' objects>"
        'make_copy': None, # (!) real value is "<method 'make_copy' of 'panda3d.core.Geom' objects>"
        'make_lines': None, # (!) real value is "<method 'make_lines' of 'panda3d.core.Geom' objects>"
        'make_lines_in_place': None, # (!) real value is "<method 'make_lines_in_place' of 'panda3d.core.Geom' objects>"
        'make_nonindexed': None, # (!) real value is "<method 'make_nonindexed' of 'panda3d.core.Geom' objects>"
        'make_patches': None, # (!) real value is "<method 'make_patches' of 'panda3d.core.Geom' objects>"
        'make_patches_in_place': None, # (!) real value is "<method 'make_patches_in_place' of 'panda3d.core.Geom' objects>"
        'make_points': None, # (!) real value is "<method 'make_points' of 'panda3d.core.Geom' objects>"
        'make_points_in_place': None, # (!) real value is "<method 'make_points_in_place' of 'panda3d.core.Geom' objects>"
        'markBoundsStale': None, # (!) real value is "<method 'markBoundsStale' of 'panda3d.core.Geom' objects>"
        'mark_bounds_stale': None, # (!) real value is "<method 'mark_bounds_stale' of 'panda3d.core.Geom' objects>"
        'modified': None, # (!) real value is "<attribute 'modified' of 'panda3d.core.Geom' objects>"
        'modifyPrimitive': None, # (!) real value is "<method 'modifyPrimitive' of 'panda3d.core.Geom' objects>"
        'modifyVertexData': None, # (!) real value is "<method 'modifyVertexData' of 'panda3d.core.Geom' objects>"
        'modify_primitive': None, # (!) real value is "<method 'modify_primitive' of 'panda3d.core.Geom' objects>"
        'modify_vertex_data': None, # (!) real value is "<method 'modify_vertex_data' of 'panda3d.core.Geom' objects>"
        'num_bytes': None, # (!) real value is "<attribute 'num_bytes' of 'panda3d.core.Geom' objects>"
        'offsetVertices': None, # (!) real value is "<method 'offsetVertices' of 'panda3d.core.Geom' objects>"
        'offset_vertices': None, # (!) real value is "<method 'offset_vertices' of 'panda3d.core.Geom' objects>"
        'output': None, # (!) real value is "<method 'output' of 'panda3d.core.Geom' objects>"
        'prepare': None, # (!) real value is "<method 'prepare' of 'panda3d.core.Geom' objects>"
        'prepareNow': None, # (!) real value is "<method 'prepareNow' of 'panda3d.core.Geom' objects>"
        'prepare_now': None, # (!) real value is "<method 'prepare_now' of 'panda3d.core.Geom' objects>"
        'primitive_type': None, # (!) real value is "<attribute 'primitive_type' of 'panda3d.core.Geom' objects>"
        'primitives': None, # (!) real value is "<attribute 'primitives' of 'panda3d.core.Geom' objects>"
        'release': None, # (!) real value is "<method 'release' of 'panda3d.core.Geom' objects>"
        'releaseAll': None, # (!) real value is "<method 'releaseAll' of 'panda3d.core.Geom' objects>"
        'release_all': None, # (!) real value is "<method 'release_all' of 'panda3d.core.Geom' objects>"
        'removePrimitive': None, # (!) real value is "<method 'removePrimitive' of 'panda3d.core.Geom' objects>"
        'remove_primitive': None, # (!) real value is "<method 'remove_primitive' of 'panda3d.core.Geom' objects>"
        'requestResident': None, # (!) real value is "<method 'requestResident' of 'panda3d.core.Geom' objects>"
        'request_resident': None, # (!) real value is "<method 'request_resident' of 'panda3d.core.Geom' objects>"
        'reverse': None, # (!) real value is "<method 'reverse' of 'panda3d.core.Geom' objects>"
        'reverseInPlace': None, # (!) real value is "<method 'reverseInPlace' of 'panda3d.core.Geom' objects>"
        'reverse_in_place': None, # (!) real value is "<method 'reverse_in_place' of 'panda3d.core.Geom' objects>"
        'rotate': None, # (!) real value is "<method 'rotate' of 'panda3d.core.Geom' objects>"
        'rotateInPlace': None, # (!) real value is "<method 'rotateInPlace' of 'panda3d.core.Geom' objects>"
        'rotate_in_place': None, # (!) real value is "<method 'rotate_in_place' of 'panda3d.core.Geom' objects>"
        'setBounds': None, # (!) real value is "<method 'setBounds' of 'panda3d.core.Geom' objects>"
        'setBoundsType': None, # (!) real value is "<method 'setBoundsType' of 'panda3d.core.Geom' objects>"
        'setPrimitive': None, # (!) real value is "<method 'setPrimitive' of 'panda3d.core.Geom' objects>"
        'setUsageHint': None, # (!) real value is "<method 'setUsageHint' of 'panda3d.core.Geom' objects>"
        'setVertexData': None, # (!) real value is "<method 'setVertexData' of 'panda3d.core.Geom' objects>"
        'set_bounds': None, # (!) real value is "<method 'set_bounds' of 'panda3d.core.Geom' objects>"
        'set_bounds_type': None, # (!) real value is "<method 'set_bounds_type' of 'panda3d.core.Geom' objects>"
        'set_primitive': None, # (!) real value is "<method 'set_primitive' of 'panda3d.core.Geom' objects>"
        'set_usage_hint': None, # (!) real value is "<method 'set_usage_hint' of 'panda3d.core.Geom' objects>"
        'set_vertex_data': None, # (!) real value is "<method 'set_vertex_data' of 'panda3d.core.Geom' objects>"
        'shade_model': None, # (!) real value is "<attribute 'shade_model' of 'panda3d.core.Geom' objects>"
        'transformVertices': None, # (!) real value is "<method 'transformVertices' of 'panda3d.core.Geom' objects>"
        'transform_vertices': None, # (!) real value is "<method 'transform_vertices' of 'panda3d.core.Geom' objects>"
        'unify': None, # (!) real value is "<method 'unify' of 'panda3d.core.Geom' objects>"
        'unifyInPlace': None, # (!) real value is "<method 'unifyInPlace' of 'panda3d.core.Geom' objects>"
        'unify_in_place': None, # (!) real value is "<method 'unify_in_place' of 'panda3d.core.Geom' objects>"
        'upcastToCopyOnWriteObject': None, # (!) real value is "<method 'upcastToCopyOnWriteObject' of 'panda3d.core.Geom' objects>"
        'upcastToGeomEnums': None, # (!) real value is "<method 'upcastToGeomEnums' of 'panda3d.core.Geom' objects>"
        'upcast_to_CopyOnWriteObject': None, # (!) real value is "<method 'upcast_to_CopyOnWriteObject' of 'panda3d.core.Geom' objects>"
        'upcast_to_GeomEnums': None, # (!) real value is "<method 'upcast_to_GeomEnums' of 'panda3d.core.Geom' objects>"
        'write': None, # (!) real value is "<method 'write' of 'panda3d.core.Geom' objects>"
    }


