# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .NodeCachedReferenceCount import NodeCachedReferenceCount

class TransformState(NodeCachedReferenceCount):
    """
    /**
     * Indicates a coordinate-system transform on vertices.  TransformStates are
     * the primary means for storing transformations on the scene graph.
     *
     * Transforms may be specified in one of two ways: componentwise, with a pos-
     * hpr-scale, or with an arbitrary transform matrix.  If you specify a
     * transform componentwise, it will remember its original components.
     *
     * TransformState objects are managed very much like RenderState objects.
     * They are immutable and reference-counted automatically.
     *
     * You should not attempt to create or modify a TransformState object
     * directly.  Instead, call one of the make() functions to create one for you.
     * And instead of modifying a TransformState object, create a new one.
     */
    """
    def cacheRef(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        cache_ref(TransformState self)
        
        /**
         * Overrides this method to update PStats appropriately.
         */
        """
        pass

    def cacheUnref(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        cache_unref(TransformState self)
        
        /**
         * Overrides this method to update PStats appropriately.
         */
        """
        pass

    def cache_ref(self, TransformState_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        cache_ref(TransformState self)
        
        /**
         * Overrides this method to update PStats appropriately.
         */
        """
        pass

    def cache_unref(self, TransformState_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        cache_unref(TransformState self)
        
        /**
         * Overrides this method to update PStats appropriately.
         */
        """
        pass

    def clearCache(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_cache()
        
        /**
         * Empties the cache of composed TransformStates.  This makes every
         * TransformState forget what results when it is composed with other
         * TransformStates.
         *
         * This will eliminate any TransformState objects that have been allocated but
         * have no references outside of the internal TransformState map.  It will not
         * eliminate TransformState objects that are still in use.
         *
         * Nowadays, this method should not be necessary, as reference-count cycles in
         * the composition cache should be automatically detected and broken.
         *
         * The return value is the number of TransformStates freed by this operation.
         */
        """
        pass

    def clear_cache(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_cache()
        
        /**
         * Empties the cache of composed TransformStates.  This makes every
         * TransformState forget what results when it is composed with other
         * TransformStates.
         *
         * This will eliminate any TransformState objects that have been allocated but
         * have no references outside of the internal TransformState map.  It will not
         * eliminate TransformState objects that are still in use.
         *
         * Nowadays, this method should not be necessary, as reference-count cycles in
         * the composition cache should be automatically detected and broken.
         *
         * The return value is the number of TransformStates freed by this operation.
         */
        """
        pass

    def compareTo(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        compare_to(TransformState self, const TransformState other)
        compare_to(TransformState self, const TransformState other, bool uniquify_matrix)
        
        /**
         * Provides an arbitrary ordering among all unique TransformStates, so we can
         * store the essentially different ones in a big set and throw away the rest.
         *
         * Note that if this returns 0, it doesn't necessarily imply that operator ==
         * returns true; it uses a very slightly different comparison threshold.
         */
        
        /**
         * Provides an arbitrary ordering among all unique TransformStates, so we can
         * store the essentially different ones in a big set and throw away the rest.
         *
         * Note that if this returns 0, it doesn't necessarily imply that operator ==
         * returns true; it uses a very slightly different comparison threshold.
         *
         * If uniquify_matrix is true, then matrix-defined TransformStates are also
         * uniqified.  If uniquify_matrix is false, then only component-defined
         * TransformStates are uniquified, which is less expensive.
         */
        """
        pass

    def compare_to(self, TransformState_self, const_TransformState_other): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        compare_to(TransformState self, const TransformState other)
        compare_to(TransformState self, const TransformState other, bool uniquify_matrix)
        
        /**
         * Provides an arbitrary ordering among all unique TransformStates, so we can
         * store the essentially different ones in a big set and throw away the rest.
         *
         * Note that if this returns 0, it doesn't necessarily imply that operator ==
         * returns true; it uses a very slightly different comparison threshold.
         */
        
        /**
         * Provides an arbitrary ordering among all unique TransformStates, so we can
         * store the essentially different ones in a big set and throw away the rest.
         *
         * Note that if this returns 0, it doesn't necessarily imply that operator ==
         * returns true; it uses a very slightly different comparison threshold.
         *
         * If uniquify_matrix is true, then matrix-defined TransformStates are also
         * uniqified.  If uniquify_matrix is false, then only component-defined
         * TransformStates are uniquified, which is less expensive.
         */
        """
        pass

    def componentsGiven(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        components_given(TransformState self)
        
        /**
         * Returns true if the transform was specified componentwise, or false if it
         * was specified with a general 4x4 matrix.  If this is true, the components
         * returned by get_pos() and get_scale() will be exactly those that were set;
         * otherwise, these functions will return computed values.  If this is true,
         * the rotation may have been set either with a hpr trio or with a quaternion;
         * hpr_given() or quat_given() can resolve the difference.
         */
        """
        pass

    def components_given(self, TransformState_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        components_given(TransformState self)
        
        /**
         * Returns true if the transform was specified componentwise, or false if it
         * was specified with a general 4x4 matrix.  If this is true, the components
         * returned by get_pos() and get_scale() will be exactly those that were set;
         * otherwise, these functions will return computed values.  If this is true,
         * the rotation may have been set either with a hpr trio or with a quaternion;
         * hpr_given() or quat_given() can resolve the difference.
         */
        """
        pass

    def compose(self, TransformState_self, const_TransformState_other): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        compose(TransformState self, const TransformState other)
        
        /**
         * Returns a new TransformState object that represents the composition of this
         * state with the other state.
         *
         * The result of this operation is cached, and will be retained as long as
         * both this TransformState object and the other TransformState object
         * continue to exist.  Should one of them destruct, the cached entry will be
         * removed, and its pointer will be allowed to destruct as well.
         */
        """
        pass

    def garbageCollect(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        garbage_collect()
        
        /**
         * Performs a garbage-collection cycle.  This must be called periodically if
         * garbage-collect-states is true to ensure that TransformStates get cleaned
         * up appropriately.  It does no harm to call it even if this variable is not
         * true, but there is probably no advantage in that case.
         */
        """
        pass

    def garbage_collect(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        garbage_collect()
        
        /**
         * Performs a garbage-collection cycle.  This must be called periodically if
         * garbage-collect-states is true to ensure that TransformStates get cleaned
         * up appropriately.  It does no harm to call it even if this variable is not
         * true, but there is probably no advantage in that case.
         */
        """
        pass

    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getCompositionCache(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_composition_cache(TransformState self)
        """
        pass

    def getCompositionCacheNumEntries(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_composition_cache_num_entries(TransformState self)
        
        /**
         * Returns the number of entries in the composition cache for this
         * TransformState.  This is the number of other TransformStates whose
         * composition with this one has been cached.  This number is not useful for
         * any practical reason other than performance analysis.
         */
        """
        pass

    def getCompositionCacheResult(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_composition_cache_result(TransformState self, int n)
        
        /**
         * Returns the result TransformState of the nth element in the composition
         * cache.  Returns NULL if there doesn't happen to be an entry in the nth
         * element.
         *
         * In general, a->compose(a->get_composition_cache_source(n)) ==
         * a->get_composition_cache_result(n).
         *
         * This has no practical value other than for examining the cache for
         * performance analysis.
         */
        """
        pass

    def getCompositionCacheSize(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_composition_cache_size(TransformState self)
        
        /**
         * Returns the number of slots in the composition cache for this
         * TransformState.  You may use this as an upper bound when walking through
         * all of the composition cache results via get_composition_cache_source() or
         * result().
         *
         * This has no practical value other than for examining the cache for
         * performance analysis.
         */
        """
        pass

    def getCompositionCacheSource(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_composition_cache_source(TransformState self, int n)
        
        /**
         * Returns the source TransformState of the nth element in the composition
         * cache.  Returns NULL if there doesn't happen to be an entry in the nth
         * element.  See get_composition_cache_result().
         *
         * This has no practical value other than for examining the cache for
         * performance analysis.
         */
        """
        pass

    def getGeomRendering(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_geom_rendering(TransformState self, int geom_rendering)
        
        /**
         * Returns the union of the Geom::GeomRendering bits that will be required
         * once this TransformState is applied to a geom which includes the indicated
         * geom_rendering bits.  The RenderState's get_geom_rendering() should already
         * have been applied.
         */
        """
        pass

    def getHash(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_hash(TransformState self)
        
        /**
         * Returns a suitable hash value for phash_map.
         */
        """
        pass

    def getHpr(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_hpr(TransformState self)
        
        /**
         * Returns the rotation component of the transform as a trio of Euler angles.
         * It is an error to call this if has_components() returned false.
         */
        """
        pass

    def getInverse(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_inverse(TransformState self)
        
        /**
         * Returns the inverse of this transform.  If you are going to immediately
         * compose this result with another TransformState, it is faster to do it in
         * one operation with invert_compose().
         */
        """
        pass

    def getInvertCompositionCache(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_invert_composition_cache(TransformState self)
        """
        pass

    def getInvertCompositionCacheNumEntries(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_invert_composition_cache_num_entries(TransformState self)
        
        /**
         * Returns the number of entries in the invert_composition cache for this
         * TransformState.  This is similar to the composition cache, but it records
         * cache entries for the invert_compose() operation.  See
         * get_composition_cache_num_entries().
         */
        """
        pass

    def getInvertCompositionCacheResult(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_invert_composition_cache_result(TransformState self, int n)
        
        /**
         * Returns the result TransformState of the nth element in the invert
         * composition cache.  Returns NULL if there doesn't happen to be an entry in
         * the nth element.
         *
         * In general, a->invert_compose(a->get_invert_composition_cache_source(n)) ==
         * a->get_invert_composition_cache_result(n).
         *
         * This has no practical value other than for examining the cache for
         * performance analysis.
         */
        """
        pass

    def getInvertCompositionCacheSize(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_invert_composition_cache_size(TransformState self)
        
        /**
         * Returns the number of slots in the composition cache for this
         * TransformState.  You may use this as an upper bound when walking through
         * all of the composition cache results via
         * get_invert_composition_cache_source() or result().
         *
         * This has no practical value other than for examining the cache for
         * performance analysis.
         */
        """
        pass

    def getInvertCompositionCacheSource(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_invert_composition_cache_source(TransformState self, int n)
        
        /**
         * Returns the source TransformState of the nth element in the invert
         * composition cache.  Returns NULL if there doesn't happen to be an entry in
         * the nth element.  See get_invert_composition_cache_result().
         *
         * This has no practical value other than for examining the cache for
         * performance analysis.
         */
        """
        pass

    def getMat(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_mat(TransformState self)
        
        /**
         * Returns the matrix that describes the transform.
         */
        """
        pass

    def getMat3(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_mat3(TransformState self)
        
        /**
         * Returns the 3x3 matrix that describes the 2-d transform.  It is an error to
         * call this if is_2d() returned false.
         */
        """
        pass

    def getNormQuat(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_norm_quat(TransformState self)
        
        /**
         * Returns the rotation component of the transform as a quaternion.  Unlike
         * the result of get_quat(), the return value of this method is guaranteed to
         * be normalized.  It is an error to call this if has_components() returned
         * false.
         */
        """
        pass

    def getNumStates(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_states()
        
        /**
         * Returns the total number of unique TransformState objects allocated in the
         * world.  This will go up and down during normal operations.
         */
        """
        pass

    def getNumUnusedStates(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_unused_states()
        
        /**
         * Returns the total number of TransformState objects that have been allocated
         * but have no references outside of the internal TransformState cache.
         *
         * A nonzero return value is not necessarily indicative of leaked references;
         * it is normal for two TransformState objects, both of which have references
         * held outside the cache, to have the result of their composition stored
         * within the cache.  This result will be retained within the cache until one
         * of the base TransformStates is released.
         *
         * Use list_cycles() to get an idea of the number of actual "leaked"
         * TransformState objects.
         */
        """
        pass

    def getPos(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_pos(TransformState self)
        
        /**
         * Returns the pos component of the transform.  It is an error to call this if
         * has_pos() returned false.
         */
        """
        pass

    def getPos2d(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_pos2d(TransformState self)
        
        /**
         * Returns the pos component of the 2-d transform.  It is an error to call
         * this if has_pos() or is_2d() returned false.
         */
        """
        pass

    def getQuat(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_quat(TransformState self)
        
        /**
         * Returns the rotation component of the transform as a quaternion.  The
         * return value will be normalized if a normalized quaternion was given to the
         * constructor (or if the quaternion was computed implicitly); it will be non-
         * normalized if a non-normalized quaternion was given to the constructor.
         * See also get_norm_quat().
         *
         * It is an error to call this if has_components() returned false.
         */
        """
        pass

    def getRotate2d(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_rotate2d(TransformState self)
        
        /**
         * Returns the rotation component of the 2-d transform as an angle in degrees
         * clockwise about the origin.  It is an error to call this if
         * has_components() or is_2d() returned false.
         */
        """
        pass

    def getScale(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_scale(TransformState self)
        
        /**
         * Returns the scale component of the transform.  It is an error to call this
         * if has_components() returned false.
         */
        """
        pass

    def getScale2d(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_scale2d(TransformState self)
        
        /**
         * Returns the scale component of the 2-d transform.  It is an error to call
         * this if has_components() or is_2d() returned false.
         */
        """
        pass

    def getShear(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_shear(TransformState self)
        
        /**
         * Returns the shear component of the transform.  It is an error to call this
         * if has_components() returned false.
         */
        """
        pass

    def getShear2d(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_shear2d(TransformState self)
        
        /**
         * Returns the shear component of the 2-d transform.  It is an error to call
         * this if has_components() or is_2d() returned false.
         */
        """
        pass

    def getStates(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_states()
        """
        pass

    def getUniformScale(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_uniform_scale(TransformState self)
        
        /**
         * Returns the scale component of the transform, as a single number.  It is an
         * error to call this if has_uniform_scale() returned false.
         */
        """
        pass

    def getUnique(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_unique(TransformState self)
        
        /**
         * Returns the pointer to the unique TransformState in the cache that is
         * equivalent to this one.  This may be the same pointer as this object, or it
         * may be a different pointer; but it will be an equivalent object, and it
         * will be a shared pointer.  This may be called from time to time to improve
         * cache benefits.
         */
        """
        pass

    def getUnusedStates(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_unused_states()
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_composition_cache(self, TransformState_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_composition_cache(TransformState self)
        """
        pass

    def get_composition_cache_num_entries(self, TransformState_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_composition_cache_num_entries(TransformState self)
        
        /**
         * Returns the number of entries in the composition cache for this
         * TransformState.  This is the number of other TransformStates whose
         * composition with this one has been cached.  This number is not useful for
         * any practical reason other than performance analysis.
         */
        """
        pass

    def get_composition_cache_result(self, TransformState_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_composition_cache_result(TransformState self, int n)
        
        /**
         * Returns the result TransformState of the nth element in the composition
         * cache.  Returns NULL if there doesn't happen to be an entry in the nth
         * element.
         *
         * In general, a->compose(a->get_composition_cache_source(n)) ==
         * a->get_composition_cache_result(n).
         *
         * This has no practical value other than for examining the cache for
         * performance analysis.
         */
        """
        pass

    def get_composition_cache_size(self, TransformState_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_composition_cache_size(TransformState self)
        
        /**
         * Returns the number of slots in the composition cache for this
         * TransformState.  You may use this as an upper bound when walking through
         * all of the composition cache results via get_composition_cache_source() or
         * result().
         *
         * This has no practical value other than for examining the cache for
         * performance analysis.
         */
        """
        pass

    def get_composition_cache_source(self, TransformState_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_composition_cache_source(TransformState self, int n)
        
        /**
         * Returns the source TransformState of the nth element in the composition
         * cache.  Returns NULL if there doesn't happen to be an entry in the nth
         * element.  See get_composition_cache_result().
         *
         * This has no practical value other than for examining the cache for
         * performance analysis.
         */
        """
        pass

    def get_geom_rendering(self, TransformState_self, int_geom_rendering): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_geom_rendering(TransformState self, int geom_rendering)
        
        /**
         * Returns the union of the Geom::GeomRendering bits that will be required
         * once this TransformState is applied to a geom which includes the indicated
         * geom_rendering bits.  The RenderState's get_geom_rendering() should already
         * have been applied.
         */
        """
        pass

    def get_hash(self, TransformState_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_hash(TransformState self)
        
        /**
         * Returns a suitable hash value for phash_map.
         */
        """
        pass

    def get_hpr(self, TransformState_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_hpr(TransformState self)
        
        /**
         * Returns the rotation component of the transform as a trio of Euler angles.
         * It is an error to call this if has_components() returned false.
         */
        """
        pass

    def get_inverse(self, TransformState_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_inverse(TransformState self)
        
        /**
         * Returns the inverse of this transform.  If you are going to immediately
         * compose this result with another TransformState, it is faster to do it in
         * one operation with invert_compose().
         */
        """
        pass

    def get_invert_composition_cache(self, TransformState_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_invert_composition_cache(TransformState self)
        """
        pass

    def get_invert_composition_cache_num_entries(self, TransformState_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_invert_composition_cache_num_entries(TransformState self)
        
        /**
         * Returns the number of entries in the invert_composition cache for this
         * TransformState.  This is similar to the composition cache, but it records
         * cache entries for the invert_compose() operation.  See
         * get_composition_cache_num_entries().
         */
        """
        pass

    def get_invert_composition_cache_result(self, TransformState_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_invert_composition_cache_result(TransformState self, int n)
        
        /**
         * Returns the result TransformState of the nth element in the invert
         * composition cache.  Returns NULL if there doesn't happen to be an entry in
         * the nth element.
         *
         * In general, a->invert_compose(a->get_invert_composition_cache_source(n)) ==
         * a->get_invert_composition_cache_result(n).
         *
         * This has no practical value other than for examining the cache for
         * performance analysis.
         */
        """
        pass

    def get_invert_composition_cache_size(self, TransformState_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_invert_composition_cache_size(TransformState self)
        
        /**
         * Returns the number of slots in the composition cache for this
         * TransformState.  You may use this as an upper bound when walking through
         * all of the composition cache results via
         * get_invert_composition_cache_source() or result().
         *
         * This has no practical value other than for examining the cache for
         * performance analysis.
         */
        """
        pass

    def get_invert_composition_cache_source(self, TransformState_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_invert_composition_cache_source(TransformState self, int n)
        
        /**
         * Returns the source TransformState of the nth element in the invert
         * composition cache.  Returns NULL if there doesn't happen to be an entry in
         * the nth element.  See get_invert_composition_cache_result().
         *
         * This has no practical value other than for examining the cache for
         * performance analysis.
         */
        """
        pass

    def get_mat(self, TransformState_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_mat(TransformState self)
        
        /**
         * Returns the matrix that describes the transform.
         */
        """
        pass

    def get_mat3(self, TransformState_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_mat3(TransformState self)
        
        /**
         * Returns the 3x3 matrix that describes the 2-d transform.  It is an error to
         * call this if is_2d() returned false.
         */
        """
        pass

    def get_norm_quat(self, TransformState_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_norm_quat(TransformState self)
        
        /**
         * Returns the rotation component of the transform as a quaternion.  Unlike
         * the result of get_quat(), the return value of this method is guaranteed to
         * be normalized.  It is an error to call this if has_components() returned
         * false.
         */
        """
        pass

    def get_num_states(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_states()
        
        /**
         * Returns the total number of unique TransformState objects allocated in the
         * world.  This will go up and down during normal operations.
         */
        """
        pass

    def get_num_unused_states(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_unused_states()
        
        /**
         * Returns the total number of TransformState objects that have been allocated
         * but have no references outside of the internal TransformState cache.
         *
         * A nonzero return value is not necessarily indicative of leaked references;
         * it is normal for two TransformState objects, both of which have references
         * held outside the cache, to have the result of their composition stored
         * within the cache.  This result will be retained within the cache until one
         * of the base TransformStates is released.
         *
         * Use list_cycles() to get an idea of the number of actual "leaked"
         * TransformState objects.
         */
        """
        pass

    def get_pos(self, TransformState_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_pos(TransformState self)
        
        /**
         * Returns the pos component of the transform.  It is an error to call this if
         * has_pos() returned false.
         */
        """
        pass

    def get_pos2d(self, TransformState_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_pos2d(TransformState self)
        
        /**
         * Returns the pos component of the 2-d transform.  It is an error to call
         * this if has_pos() or is_2d() returned false.
         */
        """
        pass

    def get_quat(self, TransformState_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_quat(TransformState self)
        
        /**
         * Returns the rotation component of the transform as a quaternion.  The
         * return value will be normalized if a normalized quaternion was given to the
         * constructor (or if the quaternion was computed implicitly); it will be non-
         * normalized if a non-normalized quaternion was given to the constructor.
         * See also get_norm_quat().
         *
         * It is an error to call this if has_components() returned false.
         */
        """
        pass

    def get_rotate2d(self, TransformState_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_rotate2d(TransformState self)
        
        /**
         * Returns the rotation component of the 2-d transform as an angle in degrees
         * clockwise about the origin.  It is an error to call this if
         * has_components() or is_2d() returned false.
         */
        """
        pass

    def get_scale(self, TransformState_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_scale(TransformState self)
        
        /**
         * Returns the scale component of the transform.  It is an error to call this
         * if has_components() returned false.
         */
        """
        pass

    def get_scale2d(self, TransformState_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_scale2d(TransformState self)
        
        /**
         * Returns the scale component of the 2-d transform.  It is an error to call
         * this if has_components() or is_2d() returned false.
         */
        """
        pass

    def get_shear(self, TransformState_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_shear(TransformState self)
        
        /**
         * Returns the shear component of the transform.  It is an error to call this
         * if has_components() returned false.
         */
        """
        pass

    def get_shear2d(self, TransformState_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_shear2d(TransformState self)
        
        /**
         * Returns the shear component of the 2-d transform.  It is an error to call
         * this if has_components() or is_2d() returned false.
         */
        """
        pass

    def get_states(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_states()
        """
        pass

    def get_uniform_scale(self, TransformState_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_uniform_scale(TransformState self)
        
        /**
         * Returns the scale component of the transform, as a single number.  It is an
         * error to call this if has_uniform_scale() returned false.
         */
        """
        pass

    def get_unique(self, TransformState_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_unique(TransformState self)
        
        /**
         * Returns the pointer to the unique TransformState in the cache that is
         * equivalent to this one.  This may be the same pointer as this object, or it
         * may be a different pointer; but it will be an equivalent object, and it
         * will be a shared pointer.  This may be called from time to time to improve
         * cache benefits.
         */
        """
        pass

    def get_unused_states(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_unused_states()
        """
        pass

    def hasComponents(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_components(TransformState self)
        
        /**
         * Returns true if the transform can be described by separate pos, hpr, and
         * scale components.  Most transforms we use in everyday life can be so
         * described, but some kinds of transforms (for instance, those involving a
         * skew) cannot.
         *
         * This is not related to whether the transform was originally described
         * componentwise.  Even a transform that was constructed with a 4x4 may return
         * true here if the matrix is a simple affine matrix with no skew.
         *
         * If this returns true, you may safely call get_hpr() and get_scale() to
         * retrieve the components.  (You may always safely call get_pos() whether
         * this returns true or false.)
         */
        """
        pass

    def hasHpr(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_hpr(TransformState self)
        
        /**
         * Returns true if the transform's rotation component can be extracted out
         * separately and described as a set of Euler angles.  This is generally true
         * only when has_components() is true.
         */
        """
        pass

    def hasIdentityScale(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_identity_scale(TransformState self)
        
        /**
         * Returns true if the scale is uniform 1.0, or false if the scale has some
         * real value.
         */
        """
        pass

    def hasMat(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_mat(TransformState self)
        
        /**
         * Returns true if the transform can be described as a matrix.  This is
         * generally always true, unless is_invalid() is true.
         */
        """
        pass

    def hasNonzeroShear(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_nonzero_shear(TransformState self)
        
        /**
         * Returns true if the shear component is non-zero, false if it is zero or if
         * the matrix cannot be decomposed.
         */
        """
        pass

    def hasPos(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_pos(TransformState self)
        
        /**
         * Returns true if the transform's pos component can be extracted out
         * separately.  This is generally always true, unless the transform is invalid
         * (i.e.  is_invalid() returns true).
         */
        """
        pass

    def hasQuat(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_quat(TransformState self)
        
        /**
         * Returns true if the transform's rotation component can be extracted out
         * separately and described as a quaternion.  This is generally true only when
         * has_components() is true.
         */
        """
        pass

    def hasScale(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_scale(TransformState self)
        
        /**
         * Returns true if the transform's scale component can be extracted out
         * separately.  This is generally true only when has_components() is true.
         */
        """
        pass

    def hasShear(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_shear(TransformState self)
        
        /**
         * Returns true if the transform's shear component can be extracted out
         * separately.  This is generally true only when has_components() is true.
         */
        """
        pass

    def hasUniformScale(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_uniform_scale(TransformState self)
        
        /**
         * Returns true if the scale is uniform across all three axes (and therefore
         * can be expressed as a single number), or false if the transform has a
         * different scale in different dimensions.
         */
        """
        pass

    def has_components(self, TransformState_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_components(TransformState self)
        
        /**
         * Returns true if the transform can be described by separate pos, hpr, and
         * scale components.  Most transforms we use in everyday life can be so
         * described, but some kinds of transforms (for instance, those involving a
         * skew) cannot.
         *
         * This is not related to whether the transform was originally described
         * componentwise.  Even a transform that was constructed with a 4x4 may return
         * true here if the matrix is a simple affine matrix with no skew.
         *
         * If this returns true, you may safely call get_hpr() and get_scale() to
         * retrieve the components.  (You may always safely call get_pos() whether
         * this returns true or false.)
         */
        """
        pass

    def has_hpr(self, TransformState_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_hpr(TransformState self)
        
        /**
         * Returns true if the transform's rotation component can be extracted out
         * separately and described as a set of Euler angles.  This is generally true
         * only when has_components() is true.
         */
        """
        pass

    def has_identity_scale(self, TransformState_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_identity_scale(TransformState self)
        
        /**
         * Returns true if the scale is uniform 1.0, or false if the scale has some
         * real value.
         */
        """
        pass

    def has_mat(self, TransformState_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_mat(TransformState self)
        
        /**
         * Returns true if the transform can be described as a matrix.  This is
         * generally always true, unless is_invalid() is true.
         */
        """
        pass

    def has_nonzero_shear(self, TransformState_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_nonzero_shear(TransformState self)
        
        /**
         * Returns true if the shear component is non-zero, false if it is zero or if
         * the matrix cannot be decomposed.
         */
        """
        pass

    def has_pos(self, TransformState_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_pos(TransformState self)
        
        /**
         * Returns true if the transform's pos component can be extracted out
         * separately.  This is generally always true, unless the transform is invalid
         * (i.e.  is_invalid() returns true).
         */
        """
        pass

    def has_quat(self, TransformState_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_quat(TransformState self)
        
        /**
         * Returns true if the transform's rotation component can be extracted out
         * separately and described as a quaternion.  This is generally true only when
         * has_components() is true.
         */
        """
        pass

    def has_scale(self, TransformState_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_scale(TransformState self)
        
        /**
         * Returns true if the transform's scale component can be extracted out
         * separately.  This is generally true only when has_components() is true.
         */
        """
        pass

    def has_shear(self, TransformState_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_shear(TransformState self)
        
        /**
         * Returns true if the transform's shear component can be extracted out
         * separately.  This is generally true only when has_components() is true.
         */
        """
        pass

    def has_uniform_scale(self, TransformState_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_uniform_scale(TransformState self)
        
        /**
         * Returns true if the scale is uniform across all three axes (and therefore
         * can be expressed as a single number), or false if the transform has a
         * different scale in different dimensions.
         */
        """
        pass

    def hprGiven(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        hpr_given(TransformState self)
        
        /**
         * Returns true if the rotation was specified via a trio of Euler angles,
         * false otherwise.  If this is true, get_hpr() will be exactly as set;
         * otherwise, it will return a computed value.
         */
        """
        pass

    def hpr_given(self, TransformState_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        hpr_given(TransformState self)
        
        /**
         * Returns true if the rotation was specified via a trio of Euler angles,
         * false otherwise.  If this is true, get_hpr() will be exactly as set;
         * otherwise, it will return a computed value.
         */
        """
        pass

    def invertCompose(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        invert_compose(TransformState self, const TransformState other)
        
        /**
         * Returns a new TransformState object that represents the composition of this
         * state's inverse with the other state.
         *
         * This is similar to compose(), but is particularly useful for computing the
         * relative state of a node as viewed from some other node.
         */
        """
        pass

    def invert_compose(self, TransformState_self, const_TransformState_other): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        invert_compose(TransformState self, const TransformState other)
        
        /**
         * Returns a new TransformState object that represents the composition of this
         * state's inverse with the other state.
         *
         * This is similar to compose(), but is particularly useful for computing the
         * relative state of a node as viewed from some other node.
         */
        """
        pass

    def is2d(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_2d(TransformState self)
        
        /**
         * Returns true if the transform has been constructed entirely using the 2-d
         * transform operations, e.g.  make_pos2d(), and therefore operates strictly
         * in two-dimensional space on X and Y only.
         */
        """
        pass

    def isIdentity(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_identity(TransformState self)
        
        /**
         * Returns true if the transform represents the identity matrix, false
         * otherwise.
         */
        """
        pass

    def isInvalid(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_invalid(TransformState self)
        
        /**
         * Returns true if the transform represents an invalid matrix, for instance
         * the result of inverting a singular matrix, or false if the transform is
         * valid.
         */
        """
        pass

    def isSingular(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_singular(TransformState self)
        
        /**
         * Returns true if the transform represents a singular transform (that is, it
         * has a zero scale, and it cannot be inverted), or false otherwise.
         */
        """
        pass

    def is_2d(self, TransformState_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_2d(TransformState self)
        
        /**
         * Returns true if the transform has been constructed entirely using the 2-d
         * transform operations, e.g.  make_pos2d(), and therefore operates strictly
         * in two-dimensional space on X and Y only.
         */
        """
        pass

    def is_identity(self, TransformState_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_identity(TransformState self)
        
        /**
         * Returns true if the transform represents the identity matrix, false
         * otherwise.
         */
        """
        pass

    def is_invalid(self, TransformState_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_invalid(TransformState self)
        
        /**
         * Returns true if the transform represents an invalid matrix, for instance
         * the result of inverting a singular matrix, or false if the transform is
         * valid.
         */
        """
        pass

    def is_singular(self, TransformState_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_singular(TransformState self)
        
        /**
         * Returns true if the transform represents a singular transform (that is, it
         * has a zero scale, and it cannot be inverted), or false otherwise.
         */
        """
        pass

    def listCycles(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        list_cycles(ostream out)
        
        /**
         * Detects all of the reference-count cycles in the cache and reports them to
         * standard output.
         *
         * These cycles may be inadvertently created when state compositions cycle
         * back to a starting point.  Nowadays, these cycles should be automatically
         * detected and broken, so this method should never list any cycles unless
         * there is a bug in that detection logic.
         *
         * The cycles listed here are not leaks in the strictest sense of the word,
         * since they can be reclaimed by a call to clear_cache(); but they will not
         * be reclaimed automatically.
         */
        """
        pass

    def listStates(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        list_states(ostream out)
        
        /**
         * Lists all of the TransformStates in the cache to the output stream, one per
         * line.  This can be quite a lot of output if the cache is large, so be
         * prepared.
         */
        """
        pass

    def list_cycles(self, ostream_out): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        list_cycles(ostream out)
        
        /**
         * Detects all of the reference-count cycles in the cache and reports them to
         * standard output.
         *
         * These cycles may be inadvertently created when state compositions cycle
         * back to a starting point.  Nowadays, these cycles should be automatically
         * detected and broken, so this method should never list any cycles unless
         * there is a bug in that detection logic.
         *
         * The cycles listed here are not leaks in the strictest sense of the word,
         * since they can be reclaimed by a call to clear_cache(); but they will not
         * be reclaimed automatically.
         */
        """
        pass

    def list_states(self, ostream_out): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        list_states(ostream out)
        
        /**
         * Lists all of the TransformStates in the cache to the output stream, one per
         * line.  This can be quite a lot of output if the cache is large, so be
         * prepared.
         */
        """
        pass

    def makeHpr(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        make_hpr(const LVecBase3f hpr)
        
        /**
         * Makes a new TransformState with the specified components.
         */
        """
        pass

    def makeIdentity(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        make_identity()
        
        /**
         * Constructs an identity transform.
         */
        """
        pass

    def makeInvalid(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        make_invalid()
        
        /**
         * Constructs an invalid transform; for instance, the result of inverting a
         * singular matrix.
         */
        """
        pass

    def makeMat(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        make_mat(const LMatrix4f mat)
        
        /**
         * Makes a new TransformState with the specified transformation matrix.
         */
        """
        pass

    def makeMat3(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        make_mat3(const LMatrix3f mat)
        
        /**
         * Makes a new two-dimensional TransformState with the specified 3x3
         * transformation matrix.
         */
        """
        pass

    def makePos(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        make_pos(const LVecBase3f pos)
        
        /**
         * Makes a new TransformState with the specified components.
         */
        """
        pass

    def makePos2d(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        make_pos2d(const LVecBase2f pos)
        
        /**
         * Makes a new 2-d TransformState with the specified components.
         */
        """
        pass

    def makePosHpr(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        make_pos_hpr(const LVecBase3f pos, const LVecBase3f hpr)
        
        /**
         * Makes a new TransformState with the specified components.
         */
        """
        pass

    def makePosHprScale(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        make_pos_hpr_scale(const LVecBase3f pos, const LVecBase3f hpr, const LVecBase3f scale)
        
        /**
         * Makes a new TransformState with the specified components.
         */
        """
        pass

    def makePosHprScaleShear(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        make_pos_hpr_scale_shear(const LVecBase3f pos, const LVecBase3f hpr, const LVecBase3f scale, const LVecBase3f shear)
        
        /**
         * Makes a new TransformState with the specified components.
         */
        """
        pass

    def makePosQuatScale(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        make_pos_quat_scale(const LVecBase3f pos, const LQuaternionf quat, const LVecBase3f scale)
        
        /**
         * Makes a new TransformState with the specified components.
         */
        """
        pass

    def makePosQuatScaleShear(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        make_pos_quat_scale_shear(const LVecBase3f pos, const LQuaternionf quat, const LVecBase3f scale, const LVecBase3f shear)
        
        /**
         * Makes a new TransformState with the specified components.
         */
        """
        pass

    def makePosRotate2d(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        make_pos_rotate2d(const LVecBase2f pos, float rotate)
        
        /**
         * Makes a new 2-d TransformState with the specified components.
         */
        """
        pass

    def makePosRotateScale2d(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        make_pos_rotate_scale2d(const LVecBase2f pos, float rotate, const LVecBase2f scale)
        
        /**
         * Makes a new 2-d TransformState with the specified components.
         */
        """
        pass

    def makePosRotateScaleShear2d(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        make_pos_rotate_scale_shear2d(const LVecBase2f pos, float rotate, const LVecBase2f scale, float shear)
        
        /**
         * Makes a new two-dimensional TransformState with the specified components.
         */
        """
        pass

    def makeQuat(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        make_quat(const LQuaternionf quat)
        
        /**
         * Makes a new TransformState with the specified components.
         */
        """
        pass

    def makeRotate2d(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        make_rotate2d(float rotate)
        
        /**
         * Makes a new 2-d TransformState with the specified components.
         */
        """
        pass

    def makeScale(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        make_scale(const LVecBase3f scale)
        make_scale(float scale)
        
        /**
         * Makes a new TransformState with the specified components.
         */
        
        /**
         * Makes a new TransformState with the specified components.
         */
        """
        pass

    def makeScale2d(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        make_scale2d(const LVecBase2f scale)
        make_scale2d(float scale)
        
        /**
         * Makes a new 2-d TransformState with the specified components.
         */
        
        /**
         * Makes a new 2-d TransformState with the specified components.
         */
        """
        pass

    def makeShear(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        make_shear(const LVecBase3f shear)
        
        /**
         * Makes a new TransformState with the specified components.
         */
        """
        pass

    def makeShear2d(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        make_shear2d(float shear)
        
        /**
         * Makes a new 2-d TransformState with the specified components.
         */
        """
        pass

    def make_hpr(self, const_LVecBase3f_hpr): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        make_hpr(const LVecBase3f hpr)
        
        /**
         * Makes a new TransformState with the specified components.
         */
        """
        pass

    def make_identity(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        make_identity()
        
        /**
         * Constructs an identity transform.
         */
        """
        pass

    def make_invalid(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        make_invalid()
        
        /**
         * Constructs an invalid transform; for instance, the result of inverting a
         * singular matrix.
         */
        """
        pass

    def make_mat(self, const_LMatrix4f_mat): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        make_mat(const LMatrix4f mat)
        
        /**
         * Makes a new TransformState with the specified transformation matrix.
         */
        """
        pass

    def make_mat3(self, const_LMatrix3f_mat): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        make_mat3(const LMatrix3f mat)
        
        /**
         * Makes a new two-dimensional TransformState with the specified 3x3
         * transformation matrix.
         */
        """
        pass

    def make_pos(self, const_LVecBase3f_pos): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        make_pos(const LVecBase3f pos)
        
        /**
         * Makes a new TransformState with the specified components.
         */
        """
        pass

    def make_pos2d(self, const_LVecBase2f_pos): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        make_pos2d(const LVecBase2f pos)
        
        /**
         * Makes a new 2-d TransformState with the specified components.
         */
        """
        pass

    def make_pos_hpr(self, const_LVecBase3f_pos, const_LVecBase3f_hpr): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        make_pos_hpr(const LVecBase3f pos, const LVecBase3f hpr)
        
        /**
         * Makes a new TransformState with the specified components.
         */
        """
        pass

    def make_pos_hpr_scale(self, const_LVecBase3f_pos, const_LVecBase3f_hpr, const_LVecBase3f_scale): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        make_pos_hpr_scale(const LVecBase3f pos, const LVecBase3f hpr, const LVecBase3f scale)
        
        /**
         * Makes a new TransformState with the specified components.
         */
        """
        pass

    def make_pos_hpr_scale_shear(self, const_LVecBase3f_pos, const_LVecBase3f_hpr, const_LVecBase3f_scale, const_LVecBase3f_shear): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        make_pos_hpr_scale_shear(const LVecBase3f pos, const LVecBase3f hpr, const LVecBase3f scale, const LVecBase3f shear)
        
        /**
         * Makes a new TransformState with the specified components.
         */
        """
        pass

    def make_pos_quat_scale(self, const_LVecBase3f_pos, const_LQuaternionf_quat, const_LVecBase3f_scale): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        make_pos_quat_scale(const LVecBase3f pos, const LQuaternionf quat, const LVecBase3f scale)
        
        /**
         * Makes a new TransformState with the specified components.
         */
        """
        pass

    def make_pos_quat_scale_shear(self, const_LVecBase3f_pos, const_LQuaternionf_quat, const_LVecBase3f_scale, const_LVecBase3f_shear): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        make_pos_quat_scale_shear(const LVecBase3f pos, const LQuaternionf quat, const LVecBase3f scale, const LVecBase3f shear)
        
        /**
         * Makes a new TransformState with the specified components.
         */
        """
        pass

    def make_pos_rotate2d(self, const_LVecBase2f_pos, float_rotate): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        make_pos_rotate2d(const LVecBase2f pos, float rotate)
        
        /**
         * Makes a new 2-d TransformState with the specified components.
         */
        """
        pass

    def make_pos_rotate_scale2d(self, const_LVecBase2f_pos, float_rotate, const_LVecBase2f_scale): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        make_pos_rotate_scale2d(const LVecBase2f pos, float rotate, const LVecBase2f scale)
        
        /**
         * Makes a new 2-d TransformState with the specified components.
         */
        """
        pass

    def make_pos_rotate_scale_shear2d(self, const_LVecBase2f_pos, float_rotate, const_LVecBase2f_scale, float_shear): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        make_pos_rotate_scale_shear2d(const LVecBase2f pos, float rotate, const LVecBase2f scale, float shear)
        
        /**
         * Makes a new two-dimensional TransformState with the specified components.
         */
        """
        pass

    def make_quat(self, const_LQuaternionf_quat): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        make_quat(const LQuaternionf quat)
        
        /**
         * Makes a new TransformState with the specified components.
         */
        """
        pass

    def make_rotate2d(self, float_rotate): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        make_rotate2d(float rotate)
        
        /**
         * Makes a new 2-d TransformState with the specified components.
         */
        """
        pass

    def make_scale(self, const_LVecBase3f_scale): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        make_scale(const LVecBase3f scale)
        make_scale(float scale)
        
        /**
         * Makes a new TransformState with the specified components.
         */
        
        /**
         * Makes a new TransformState with the specified components.
         */
        """
        pass

    def make_scale2d(self, const_LVecBase2f_scale): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        make_scale2d(const LVecBase2f scale)
        make_scale2d(float scale)
        
        /**
         * Makes a new 2-d TransformState with the specified components.
         */
        
        /**
         * Makes a new 2-d TransformState with the specified components.
         */
        """
        pass

    def make_shear(self, const_LVecBase3f_shear): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        make_shear(const LVecBase3f shear)
        
        /**
         * Makes a new TransformState with the specified components.
         */
        """
        pass

    def make_shear2d(self, float_shear): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        make_shear2d(float shear)
        
        /**
         * Makes a new 2-d TransformState with the specified components.
         */
        """
        pass

    def nodeRef(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        node_ref(TransformState self)
        
        /**
         * Overrides this method to update PStats appropriately.
         */
        """
        pass

    def nodeUnref(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        node_unref(TransformState self)
        
        /**
         * Overrides this method to update PStats appropriately.
         */
        """
        pass

    def node_ref(self, TransformState_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        node_ref(TransformState self)
        
        /**
         * Overrides this method to update PStats appropriately.
         */
        """
        pass

    def node_unref(self, TransformState_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        node_unref(TransformState self)
        
        /**
         * Overrides this method to update PStats appropriately.
         */
        """
        pass

    def output(self, TransformState_self, ostream_out): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        output(TransformState self, ostream out)
        
        /**
         *
         */
        """
        pass

    def quatGiven(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        quat_given(TransformState self)
        
        /**
         * Returns true if the rotation was specified via a quaternion, false
         * otherwise.  If this is true, get_quat() will be exactly as set; otherwise,
         * it will return a computed value.
         */
        """
        pass

    def quat_given(self, TransformState_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        quat_given(TransformState self)
        
        /**
         * Returns true if the rotation was specified via a quaternion, false
         * otherwise.  If this is true, get_quat() will be exactly as set; otherwise,
         * it will return a computed value.
         */
        """
        pass

    def setHpr(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_hpr(TransformState self, const LVecBase3f hpr)
        
        /**
         * Returns a new TransformState object that represents the original
         * TransformState with its rotation component replaced with the indicated
         * value, if possible.
         */
        """
        pass

    def setPos(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_pos(TransformState self, const LVecBase3f pos)
        
        /**
         * Returns a new TransformState object that represents the original
         * TransformState with its pos component replaced with the indicated value.
         */
        """
        pass

    def setPos2d(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_pos2d(TransformState self, const LVecBase2f pos)
        
        /**
         * Returns a new TransformState object that represents the original 2-d
         * TransformState with its pos component replaced with the indicated value.
         */
        """
        pass

    def setQuat(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_quat(TransformState self, const LQuaternionf quat)
        
        /**
         * Returns a new TransformState object that represents the original
         * TransformState with its rotation component replaced with the indicated
         * value, if possible.
         */
        """
        pass

    def setRotate2d(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_rotate2d(TransformState self, float rotate)
        
        /**
         * Returns a new TransformState object that represents the original 2-d
         * TransformState with its rotation component replaced with the indicated
         * value, if possible.
         */
        """
        pass

    def setScale(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_scale(TransformState self, const LVecBase3f scale)
        
        /**
         * Returns a new TransformState object that represents the original
         * TransformState with its scale component replaced with the indicated value,
         * if possible.
         */
        """
        pass

    def setScale2d(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_scale2d(TransformState self, const LVecBase2f scale)
        
        /**
         * Returns a new TransformState object that represents the original 2-d
         * TransformState with its scale component replaced with the indicated value,
         * if possible.
         */
        """
        pass

    def setShear(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_shear(TransformState self, const LVecBase3f shear)
        
        /**
         * Returns a new TransformState object that represents the original
         * TransformState with its shear component replaced with the indicated value,
         * if possible.
         */
        """
        pass

    def setShear2d(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_shear2d(TransformState self, float shear)
        
        /**
         * Returns a new TransformState object that represents the original 2-d
         * TransformState with its shear component replaced with the indicated value,
         * if possible.
         */
        """
        pass

    def set_hpr(self, TransformState_self, const_LVecBase3f_hpr): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_hpr(TransformState self, const LVecBase3f hpr)
        
        /**
         * Returns a new TransformState object that represents the original
         * TransformState with its rotation component replaced with the indicated
         * value, if possible.
         */
        """
        pass

    def set_pos(self, TransformState_self, const_LVecBase3f_pos): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_pos(TransformState self, const LVecBase3f pos)
        
        /**
         * Returns a new TransformState object that represents the original
         * TransformState with its pos component replaced with the indicated value.
         */
        """
        pass

    def set_pos2d(self, TransformState_self, const_LVecBase2f_pos): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_pos2d(TransformState self, const LVecBase2f pos)
        
        /**
         * Returns a new TransformState object that represents the original 2-d
         * TransformState with its pos component replaced with the indicated value.
         */
        """
        pass

    def set_quat(self, TransformState_self, const_LQuaternionf_quat): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_quat(TransformState self, const LQuaternionf quat)
        
        /**
         * Returns a new TransformState object that represents the original
         * TransformState with its rotation component replaced with the indicated
         * value, if possible.
         */
        """
        pass

    def set_rotate2d(self, TransformState_self, float_rotate): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_rotate2d(TransformState self, float rotate)
        
        /**
         * Returns a new TransformState object that represents the original 2-d
         * TransformState with its rotation component replaced with the indicated
         * value, if possible.
         */
        """
        pass

    def set_scale(self, TransformState_self, const_LVecBase3f_scale): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_scale(TransformState self, const LVecBase3f scale)
        
        /**
         * Returns a new TransformState object that represents the original
         * TransformState with its scale component replaced with the indicated value,
         * if possible.
         */
        """
        pass

    def set_scale2d(self, TransformState_self, const_LVecBase2f_scale): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_scale2d(TransformState self, const LVecBase2f scale)
        
        /**
         * Returns a new TransformState object that represents the original 2-d
         * TransformState with its scale component replaced with the indicated value,
         * if possible.
         */
        """
        pass

    def set_shear(self, TransformState_self, const_LVecBase3f_shear): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_shear(TransformState self, const LVecBase3f shear)
        
        /**
         * Returns a new TransformState object that represents the original
         * TransformState with its shear component replaced with the indicated value,
         * if possible.
         */
        """
        pass

    def set_shear2d(self, TransformState_self, float_shear): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_shear2d(TransformState self, float shear)
        
        /**
         * Returns a new TransformState object that represents the original 2-d
         * TransformState with its shear component replaced with the indicated value,
         * if possible.
         */
        """
        pass

    def validateCompositionCache(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        validate_composition_cache(TransformState self)
        
        /**
         * Returns true if the composition cache and invert composition cache for this
         * particular TransformState are self-consistent and valid, false otherwise.
         */
        """
        pass

    def validateStates(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        validate_states()
        
        /**
         * Ensures that the cache is still stored in sorted order, and that none of
         * the cache elements have been inadvertently deleted.  Returns true if so,
         * false if there is a problem (which implies someone has modified one of the
         * supposedly-const TransformState objects).
         */
        """
        pass

    def validate_composition_cache(self, TransformState_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        validate_composition_cache(TransformState self)
        
        /**
         * Returns true if the composition cache and invert composition cache for this
         * particular TransformState are self-consistent and valid, false otherwise.
         */
        """
        pass

    def validate_states(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        validate_states()
        
        /**
         * Ensures that the cache is still stored in sorted order, and that none of
         * the cache elements have been inadvertently deleted.  Returns true if so,
         * false if there is a problem (which implies someone has modified one of the
         * supposedly-const TransformState objects).
         */
        """
        pass

    def write(self, TransformState_self, ostream_out, int_indent_level): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        write(TransformState self, ostream out, int indent_level)
        
        /**
         *
         */
        """
        pass

    def writeCompositionCache(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        write_composition_cache(TransformState self, ostream out, int indent_level)
        
        /**
         * Writes a brief description of the composition cache and invert composition
         * cache to the indicated ostream.  This is not useful except for performance
         * analysis, to examine the cache structure.
         */
        """
        pass

    def write_composition_cache(self, TransformState_self, ostream_out, int_indent_level): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        write_composition_cache(TransformState self, ostream out, int indent_level)
        
        /**
         * Writes a brief description of the composition cache and invert composition
         * cache to the indicated ostream.  This is not useful except for performance
         * analysis, to examine the cache structure.
         */
        """
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

    hpr = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    mat = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    norm_quat = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pos = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    quat = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    scale = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    shear = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__doc__': '/**\n * Indicates a coordinate-system transform on vertices.  TransformStates are\n * the primary means for storing transformations on the scene graph.\n *\n * Transforms may be specified in one of two ways: componentwise, with a pos-\n * hpr-scale, or with an arbitrary transform matrix.  If you specify a\n * transform componentwise, it will remember its original components.\n *\n * TransformState objects are managed very much like RenderState objects.\n * They are immutable and reference-counted automatically.\n *\n * You should not attempt to create or modify a TransformState object\n * directly.  Instead, call one of the make() functions to create one for you.\n * And instead of modifying a TransformState object, create a new one.\n */',
        '__eq__': None, # (!) real value is "<slot wrapper '__eq__' of 'panda3d.core.TransformState' objects>"
        '__ge__': None, # (!) real value is "<slot wrapper '__ge__' of 'panda3d.core.TransformState' objects>"
        '__gt__': None, # (!) real value is "<slot wrapper '__gt__' of 'panda3d.core.TransformState' objects>"
        '__hash__': None, # (!) real value is "<slot wrapper '__hash__' of 'panda3d.core.TransformState' objects>"
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.TransformState' objects>"
        '__le__': None, # (!) real value is "<slot wrapper '__le__' of 'panda3d.core.TransformState' objects>"
        '__lt__': None, # (!) real value is "<slot wrapper '__lt__' of 'panda3d.core.TransformState' objects>"
        '__ne__': None, # (!) real value is "<slot wrapper '__ne__' of 'panda3d.core.TransformState' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE291630>'
        '__repr__': None, # (!) real value is "<slot wrapper '__repr__' of 'panda3d.core.TransformState' objects>"
        '__str__': None, # (!) real value is "<slot wrapper '__str__' of 'panda3d.core.TransformState' objects>"
        'cacheRef': None, # (!) real value is "<method 'cacheRef' of 'panda3d.core.TransformState' objects>"
        'cacheUnref': None, # (!) real value is "<method 'cacheUnref' of 'panda3d.core.TransformState' objects>"
        'cache_ref': None, # (!) real value is "<method 'cache_ref' of 'panda3d.core.TransformState' objects>"
        'cache_unref': None, # (!) real value is "<method 'cache_unref' of 'panda3d.core.TransformState' objects>"
        'clearCache': None, # (!) real value is '<staticmethod(<built-in method clearCache of type object at 0x00007FFCFE291630>)>'
        'clear_cache': None, # (!) real value is '<staticmethod(<built-in method clear_cache of type object at 0x00007FFCFE291630>)>'
        'compareTo': None, # (!) real value is "<method 'compareTo' of 'panda3d.core.TransformState' objects>"
        'compare_to': None, # (!) real value is "<method 'compare_to' of 'panda3d.core.TransformState' objects>"
        'componentsGiven': None, # (!) real value is "<method 'componentsGiven' of 'panda3d.core.TransformState' objects>"
        'components_given': None, # (!) real value is "<method 'components_given' of 'panda3d.core.TransformState' objects>"
        'compose': None, # (!) real value is "<method 'compose' of 'panda3d.core.TransformState' objects>"
        'garbageCollect': None, # (!) real value is '<staticmethod(<built-in method garbageCollect of type object at 0x00007FFCFE291630>)>'
        'garbage_collect': None, # (!) real value is '<staticmethod(<built-in method garbage_collect of type object at 0x00007FFCFE291630>)>'
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE291630>)>'
        'getCompositionCache': None, # (!) real value is "<method 'getCompositionCache' of 'panda3d.core.TransformState' objects>"
        'getCompositionCacheNumEntries': None, # (!) real value is "<method 'getCompositionCacheNumEntries' of 'panda3d.core.TransformState' objects>"
        'getCompositionCacheResult': None, # (!) real value is "<method 'getCompositionCacheResult' of 'panda3d.core.TransformState' objects>"
        'getCompositionCacheSize': None, # (!) real value is "<method 'getCompositionCacheSize' of 'panda3d.core.TransformState' objects>"
        'getCompositionCacheSource': None, # (!) real value is "<method 'getCompositionCacheSource' of 'panda3d.core.TransformState' objects>"
        'getGeomRendering': None, # (!) real value is "<method 'getGeomRendering' of 'panda3d.core.TransformState' objects>"
        'getHash': None, # (!) real value is "<method 'getHash' of 'panda3d.core.TransformState' objects>"
        'getHpr': None, # (!) real value is "<method 'getHpr' of 'panda3d.core.TransformState' objects>"
        'getInverse': None, # (!) real value is "<method 'getInverse' of 'panda3d.core.TransformState' objects>"
        'getInvertCompositionCache': None, # (!) real value is "<method 'getInvertCompositionCache' of 'panda3d.core.TransformState' objects>"
        'getInvertCompositionCacheNumEntries': None, # (!) real value is "<method 'getInvertCompositionCacheNumEntries' of 'panda3d.core.TransformState' objects>"
        'getInvertCompositionCacheResult': None, # (!) real value is "<method 'getInvertCompositionCacheResult' of 'panda3d.core.TransformState' objects>"
        'getInvertCompositionCacheSize': None, # (!) real value is "<method 'getInvertCompositionCacheSize' of 'panda3d.core.TransformState' objects>"
        'getInvertCompositionCacheSource': None, # (!) real value is "<method 'getInvertCompositionCacheSource' of 'panda3d.core.TransformState' objects>"
        'getMat': None, # (!) real value is "<method 'getMat' of 'panda3d.core.TransformState' objects>"
        'getMat3': None, # (!) real value is "<method 'getMat3' of 'panda3d.core.TransformState' objects>"
        'getNormQuat': None, # (!) real value is "<method 'getNormQuat' of 'panda3d.core.TransformState' objects>"
        'getNumStates': None, # (!) real value is '<staticmethod(<built-in method getNumStates of type object at 0x00007FFCFE291630>)>'
        'getNumUnusedStates': None, # (!) real value is '<staticmethod(<built-in method getNumUnusedStates of type object at 0x00007FFCFE291630>)>'
        'getPos': None, # (!) real value is "<method 'getPos' of 'panda3d.core.TransformState' objects>"
        'getPos2d': None, # (!) real value is "<method 'getPos2d' of 'panda3d.core.TransformState' objects>"
        'getQuat': None, # (!) real value is "<method 'getQuat' of 'panda3d.core.TransformState' objects>"
        'getRotate2d': None, # (!) real value is "<method 'getRotate2d' of 'panda3d.core.TransformState' objects>"
        'getScale': None, # (!) real value is "<method 'getScale' of 'panda3d.core.TransformState' objects>"
        'getScale2d': None, # (!) real value is "<method 'getScale2d' of 'panda3d.core.TransformState' objects>"
        'getShear': None, # (!) real value is "<method 'getShear' of 'panda3d.core.TransformState' objects>"
        'getShear2d': None, # (!) real value is "<method 'getShear2d' of 'panda3d.core.TransformState' objects>"
        'getStates': None, # (!) real value is '<staticmethod(<built-in method getStates of type object at 0x00007FFCFE291630>)>'
        'getUniformScale': None, # (!) real value is "<method 'getUniformScale' of 'panda3d.core.TransformState' objects>"
        'getUnique': None, # (!) real value is "<method 'getUnique' of 'panda3d.core.TransformState' objects>"
        'getUnusedStates': None, # (!) real value is '<staticmethod(<built-in method getUnusedStates of type object at 0x00007FFCFE291630>)>'
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE291630>)>'
        'get_composition_cache': None, # (!) real value is "<method 'get_composition_cache' of 'panda3d.core.TransformState' objects>"
        'get_composition_cache_num_entries': None, # (!) real value is "<method 'get_composition_cache_num_entries' of 'panda3d.core.TransformState' objects>"
        'get_composition_cache_result': None, # (!) real value is "<method 'get_composition_cache_result' of 'panda3d.core.TransformState' objects>"
        'get_composition_cache_size': None, # (!) real value is "<method 'get_composition_cache_size' of 'panda3d.core.TransformState' objects>"
        'get_composition_cache_source': None, # (!) real value is "<method 'get_composition_cache_source' of 'panda3d.core.TransformState' objects>"
        'get_geom_rendering': None, # (!) real value is "<method 'get_geom_rendering' of 'panda3d.core.TransformState' objects>"
        'get_hash': None, # (!) real value is "<method 'get_hash' of 'panda3d.core.TransformState' objects>"
        'get_hpr': None, # (!) real value is "<method 'get_hpr' of 'panda3d.core.TransformState' objects>"
        'get_inverse': None, # (!) real value is "<method 'get_inverse' of 'panda3d.core.TransformState' objects>"
        'get_invert_composition_cache': None, # (!) real value is "<method 'get_invert_composition_cache' of 'panda3d.core.TransformState' objects>"
        'get_invert_composition_cache_num_entries': None, # (!) real value is "<method 'get_invert_composition_cache_num_entries' of 'panda3d.core.TransformState' objects>"
        'get_invert_composition_cache_result': None, # (!) real value is "<method 'get_invert_composition_cache_result' of 'panda3d.core.TransformState' objects>"
        'get_invert_composition_cache_size': None, # (!) real value is "<method 'get_invert_composition_cache_size' of 'panda3d.core.TransformState' objects>"
        'get_invert_composition_cache_source': None, # (!) real value is "<method 'get_invert_composition_cache_source' of 'panda3d.core.TransformState' objects>"
        'get_mat': None, # (!) real value is "<method 'get_mat' of 'panda3d.core.TransformState' objects>"
        'get_mat3': None, # (!) real value is "<method 'get_mat3' of 'panda3d.core.TransformState' objects>"
        'get_norm_quat': None, # (!) real value is "<method 'get_norm_quat' of 'panda3d.core.TransformState' objects>"
        'get_num_states': None, # (!) real value is '<staticmethod(<built-in method get_num_states of type object at 0x00007FFCFE291630>)>'
        'get_num_unused_states': None, # (!) real value is '<staticmethod(<built-in method get_num_unused_states of type object at 0x00007FFCFE291630>)>'
        'get_pos': None, # (!) real value is "<method 'get_pos' of 'panda3d.core.TransformState' objects>"
        'get_pos2d': None, # (!) real value is "<method 'get_pos2d' of 'panda3d.core.TransformState' objects>"
        'get_quat': None, # (!) real value is "<method 'get_quat' of 'panda3d.core.TransformState' objects>"
        'get_rotate2d': None, # (!) real value is "<method 'get_rotate2d' of 'panda3d.core.TransformState' objects>"
        'get_scale': None, # (!) real value is "<method 'get_scale' of 'panda3d.core.TransformState' objects>"
        'get_scale2d': None, # (!) real value is "<method 'get_scale2d' of 'panda3d.core.TransformState' objects>"
        'get_shear': None, # (!) real value is "<method 'get_shear' of 'panda3d.core.TransformState' objects>"
        'get_shear2d': None, # (!) real value is "<method 'get_shear2d' of 'panda3d.core.TransformState' objects>"
        'get_states': None, # (!) real value is '<staticmethod(<built-in method get_states of type object at 0x00007FFCFE291630>)>'
        'get_uniform_scale': None, # (!) real value is "<method 'get_uniform_scale' of 'panda3d.core.TransformState' objects>"
        'get_unique': None, # (!) real value is "<method 'get_unique' of 'panda3d.core.TransformState' objects>"
        'get_unused_states': None, # (!) real value is '<staticmethod(<built-in method get_unused_states of type object at 0x00007FFCFE291630>)>'
        'hasComponents': None, # (!) real value is "<method 'hasComponents' of 'panda3d.core.TransformState' objects>"
        'hasHpr': None, # (!) real value is "<method 'hasHpr' of 'panda3d.core.TransformState' objects>"
        'hasIdentityScale': None, # (!) real value is "<method 'hasIdentityScale' of 'panda3d.core.TransformState' objects>"
        'hasMat': None, # (!) real value is "<method 'hasMat' of 'panda3d.core.TransformState' objects>"
        'hasNonzeroShear': None, # (!) real value is "<method 'hasNonzeroShear' of 'panda3d.core.TransformState' objects>"
        'hasPos': None, # (!) real value is "<method 'hasPos' of 'panda3d.core.TransformState' objects>"
        'hasQuat': None, # (!) real value is "<method 'hasQuat' of 'panda3d.core.TransformState' objects>"
        'hasScale': None, # (!) real value is "<method 'hasScale' of 'panda3d.core.TransformState' objects>"
        'hasShear': None, # (!) real value is "<method 'hasShear' of 'panda3d.core.TransformState' objects>"
        'hasUniformScale': None, # (!) real value is "<method 'hasUniformScale' of 'panda3d.core.TransformState' objects>"
        'has_components': None, # (!) real value is "<method 'has_components' of 'panda3d.core.TransformState' objects>"
        'has_hpr': None, # (!) real value is "<method 'has_hpr' of 'panda3d.core.TransformState' objects>"
        'has_identity_scale': None, # (!) real value is "<method 'has_identity_scale' of 'panda3d.core.TransformState' objects>"
        'has_mat': None, # (!) real value is "<method 'has_mat' of 'panda3d.core.TransformState' objects>"
        'has_nonzero_shear': None, # (!) real value is "<method 'has_nonzero_shear' of 'panda3d.core.TransformState' objects>"
        'has_pos': None, # (!) real value is "<method 'has_pos' of 'panda3d.core.TransformState' objects>"
        'has_quat': None, # (!) real value is "<method 'has_quat' of 'panda3d.core.TransformState' objects>"
        'has_scale': None, # (!) real value is "<method 'has_scale' of 'panda3d.core.TransformState' objects>"
        'has_shear': None, # (!) real value is "<method 'has_shear' of 'panda3d.core.TransformState' objects>"
        'has_uniform_scale': None, # (!) real value is "<method 'has_uniform_scale' of 'panda3d.core.TransformState' objects>"
        'hpr': None, # (!) real value is "<attribute 'hpr' of 'panda3d.core.TransformState' objects>"
        'hprGiven': None, # (!) real value is "<method 'hprGiven' of 'panda3d.core.TransformState' objects>"
        'hpr_given': None, # (!) real value is "<method 'hpr_given' of 'panda3d.core.TransformState' objects>"
        'invertCompose': None, # (!) real value is "<method 'invertCompose' of 'panda3d.core.TransformState' objects>"
        'invert_compose': None, # (!) real value is "<method 'invert_compose' of 'panda3d.core.TransformState' objects>"
        'is2d': None, # (!) real value is "<method 'is2d' of 'panda3d.core.TransformState' objects>"
        'isIdentity': None, # (!) real value is "<method 'isIdentity' of 'panda3d.core.TransformState' objects>"
        'isInvalid': None, # (!) real value is "<method 'isInvalid' of 'panda3d.core.TransformState' objects>"
        'isSingular': None, # (!) real value is "<method 'isSingular' of 'panda3d.core.TransformState' objects>"
        'is_2d': None, # (!) real value is "<method 'is_2d' of 'panda3d.core.TransformState' objects>"
        'is_identity': None, # (!) real value is "<method 'is_identity' of 'panda3d.core.TransformState' objects>"
        'is_invalid': None, # (!) real value is "<method 'is_invalid' of 'panda3d.core.TransformState' objects>"
        'is_singular': None, # (!) real value is "<method 'is_singular' of 'panda3d.core.TransformState' objects>"
        'listCycles': None, # (!) real value is '<staticmethod(<built-in method listCycles of type object at 0x00007FFCFE291630>)>'
        'listStates': None, # (!) real value is '<staticmethod(<built-in method listStates of type object at 0x00007FFCFE291630>)>'
        'list_cycles': None, # (!) real value is '<staticmethod(<built-in method list_cycles of type object at 0x00007FFCFE291630>)>'
        'list_states': None, # (!) real value is '<staticmethod(<built-in method list_states of type object at 0x00007FFCFE291630>)>'
        'makeHpr': None, # (!) real value is '<staticmethod(<built-in method makeHpr of type object at 0x00007FFCFE291630>)>'
        'makeIdentity': None, # (!) real value is '<staticmethod(<built-in method makeIdentity of type object at 0x00007FFCFE291630>)>'
        'makeInvalid': None, # (!) real value is '<staticmethod(<built-in method makeInvalid of type object at 0x00007FFCFE291630>)>'
        'makeMat': None, # (!) real value is '<staticmethod(<built-in method makeMat of type object at 0x00007FFCFE291630>)>'
        'makeMat3': None, # (!) real value is '<staticmethod(<built-in method makeMat3 of type object at 0x00007FFCFE291630>)>'
        'makePos': None, # (!) real value is '<staticmethod(<built-in method makePos of type object at 0x00007FFCFE291630>)>'
        'makePos2d': None, # (!) real value is '<staticmethod(<built-in method makePos2d of type object at 0x00007FFCFE291630>)>'
        'makePosHpr': None, # (!) real value is '<staticmethod(<built-in method makePosHpr of type object at 0x00007FFCFE291630>)>'
        'makePosHprScale': None, # (!) real value is '<staticmethod(<built-in method makePosHprScale of type object at 0x00007FFCFE291630>)>'
        'makePosHprScaleShear': None, # (!) real value is '<staticmethod(<built-in method makePosHprScaleShear of type object at 0x00007FFCFE291630>)>'
        'makePosQuatScale': None, # (!) real value is '<staticmethod(<built-in method makePosQuatScale of type object at 0x00007FFCFE291630>)>'
        'makePosQuatScaleShear': None, # (!) real value is '<staticmethod(<built-in method makePosQuatScaleShear of type object at 0x00007FFCFE291630>)>'
        'makePosRotate2d': None, # (!) real value is '<staticmethod(<built-in method makePosRotate2d of type object at 0x00007FFCFE291630>)>'
        'makePosRotateScale2d': None, # (!) real value is '<staticmethod(<built-in method makePosRotateScale2d of type object at 0x00007FFCFE291630>)>'
        'makePosRotateScaleShear2d': None, # (!) real value is '<staticmethod(<built-in method makePosRotateScaleShear2d of type object at 0x00007FFCFE291630>)>'
        'makeQuat': None, # (!) real value is '<staticmethod(<built-in method makeQuat of type object at 0x00007FFCFE291630>)>'
        'makeRotate2d': None, # (!) real value is '<staticmethod(<built-in method makeRotate2d of type object at 0x00007FFCFE291630>)>'
        'makeScale': None, # (!) real value is '<staticmethod(<built-in method makeScale of type object at 0x00007FFCFE291630>)>'
        'makeScale2d': None, # (!) real value is '<staticmethod(<built-in method makeScale2d of type object at 0x00007FFCFE291630>)>'
        'makeShear': None, # (!) real value is '<staticmethod(<built-in method makeShear of type object at 0x00007FFCFE291630>)>'
        'makeShear2d': None, # (!) real value is '<staticmethod(<built-in method makeShear2d of type object at 0x00007FFCFE291630>)>'
        'make_hpr': None, # (!) real value is '<staticmethod(<built-in method make_hpr of type object at 0x00007FFCFE291630>)>'
        'make_identity': None, # (!) real value is '<staticmethod(<built-in method make_identity of type object at 0x00007FFCFE291630>)>'
        'make_invalid': None, # (!) real value is '<staticmethod(<built-in method make_invalid of type object at 0x00007FFCFE291630>)>'
        'make_mat': None, # (!) real value is '<staticmethod(<built-in method make_mat of type object at 0x00007FFCFE291630>)>'
        'make_mat3': None, # (!) real value is '<staticmethod(<built-in method make_mat3 of type object at 0x00007FFCFE291630>)>'
        'make_pos': None, # (!) real value is '<staticmethod(<built-in method make_pos of type object at 0x00007FFCFE291630>)>'
        'make_pos2d': None, # (!) real value is '<staticmethod(<built-in method make_pos2d of type object at 0x00007FFCFE291630>)>'
        'make_pos_hpr': None, # (!) real value is '<staticmethod(<built-in method make_pos_hpr of type object at 0x00007FFCFE291630>)>'
        'make_pos_hpr_scale': None, # (!) real value is '<staticmethod(<built-in method make_pos_hpr_scale of type object at 0x00007FFCFE291630>)>'
        'make_pos_hpr_scale_shear': None, # (!) real value is '<staticmethod(<built-in method make_pos_hpr_scale_shear of type object at 0x00007FFCFE291630>)>'
        'make_pos_quat_scale': None, # (!) real value is '<staticmethod(<built-in method make_pos_quat_scale of type object at 0x00007FFCFE291630>)>'
        'make_pos_quat_scale_shear': None, # (!) real value is '<staticmethod(<built-in method make_pos_quat_scale_shear of type object at 0x00007FFCFE291630>)>'
        'make_pos_rotate2d': None, # (!) real value is '<staticmethod(<built-in method make_pos_rotate2d of type object at 0x00007FFCFE291630>)>'
        'make_pos_rotate_scale2d': None, # (!) real value is '<staticmethod(<built-in method make_pos_rotate_scale2d of type object at 0x00007FFCFE291630>)>'
        'make_pos_rotate_scale_shear2d': None, # (!) real value is '<staticmethod(<built-in method make_pos_rotate_scale_shear2d of type object at 0x00007FFCFE291630>)>'
        'make_quat': None, # (!) real value is '<staticmethod(<built-in method make_quat of type object at 0x00007FFCFE291630>)>'
        'make_rotate2d': None, # (!) real value is '<staticmethod(<built-in method make_rotate2d of type object at 0x00007FFCFE291630>)>'
        'make_scale': None, # (!) real value is '<staticmethod(<built-in method make_scale of type object at 0x00007FFCFE291630>)>'
        'make_scale2d': None, # (!) real value is '<staticmethod(<built-in method make_scale2d of type object at 0x00007FFCFE291630>)>'
        'make_shear': None, # (!) real value is '<staticmethod(<built-in method make_shear of type object at 0x00007FFCFE291630>)>'
        'make_shear2d': None, # (!) real value is '<staticmethod(<built-in method make_shear2d of type object at 0x00007FFCFE291630>)>'
        'mat': None, # (!) real value is "<attribute 'mat' of 'panda3d.core.TransformState' objects>"
        'nodeRef': None, # (!) real value is "<method 'nodeRef' of 'panda3d.core.TransformState' objects>"
        'nodeUnref': None, # (!) real value is "<method 'nodeUnref' of 'panda3d.core.TransformState' objects>"
        'node_ref': None, # (!) real value is "<method 'node_ref' of 'panda3d.core.TransformState' objects>"
        'node_unref': None, # (!) real value is "<method 'node_unref' of 'panda3d.core.TransformState' objects>"
        'norm_quat': None, # (!) real value is "<attribute 'norm_quat' of 'panda3d.core.TransformState' objects>"
        'output': None, # (!) real value is "<method 'output' of 'panda3d.core.TransformState' objects>"
        'pos': None, # (!) real value is "<attribute 'pos' of 'panda3d.core.TransformState' objects>"
        'quat': None, # (!) real value is "<attribute 'quat' of 'panda3d.core.TransformState' objects>"
        'quatGiven': None, # (!) real value is "<method 'quatGiven' of 'panda3d.core.TransformState' objects>"
        'quat_given': None, # (!) real value is "<method 'quat_given' of 'panda3d.core.TransformState' objects>"
        'scale': None, # (!) real value is "<attribute 'scale' of 'panda3d.core.TransformState' objects>"
        'setHpr': None, # (!) real value is "<method 'setHpr' of 'panda3d.core.TransformState' objects>"
        'setPos': None, # (!) real value is "<method 'setPos' of 'panda3d.core.TransformState' objects>"
        'setPos2d': None, # (!) real value is "<method 'setPos2d' of 'panda3d.core.TransformState' objects>"
        'setQuat': None, # (!) real value is "<method 'setQuat' of 'panda3d.core.TransformState' objects>"
        'setRotate2d': None, # (!) real value is "<method 'setRotate2d' of 'panda3d.core.TransformState' objects>"
        'setScale': None, # (!) real value is "<method 'setScale' of 'panda3d.core.TransformState' objects>"
        'setScale2d': None, # (!) real value is "<method 'setScale2d' of 'panda3d.core.TransformState' objects>"
        'setShear': None, # (!) real value is "<method 'setShear' of 'panda3d.core.TransformState' objects>"
        'setShear2d': None, # (!) real value is "<method 'setShear2d' of 'panda3d.core.TransformState' objects>"
        'set_hpr': None, # (!) real value is "<method 'set_hpr' of 'panda3d.core.TransformState' objects>"
        'set_pos': None, # (!) real value is "<method 'set_pos' of 'panda3d.core.TransformState' objects>"
        'set_pos2d': None, # (!) real value is "<method 'set_pos2d' of 'panda3d.core.TransformState' objects>"
        'set_quat': None, # (!) real value is "<method 'set_quat' of 'panda3d.core.TransformState' objects>"
        'set_rotate2d': None, # (!) real value is "<method 'set_rotate2d' of 'panda3d.core.TransformState' objects>"
        'set_scale': None, # (!) real value is "<method 'set_scale' of 'panda3d.core.TransformState' objects>"
        'set_scale2d': None, # (!) real value is "<method 'set_scale2d' of 'panda3d.core.TransformState' objects>"
        'set_shear': None, # (!) real value is "<method 'set_shear' of 'panda3d.core.TransformState' objects>"
        'set_shear2d': None, # (!) real value is "<method 'set_shear2d' of 'panda3d.core.TransformState' objects>"
        'shear': None, # (!) real value is "<attribute 'shear' of 'panda3d.core.TransformState' objects>"
        'validateCompositionCache': None, # (!) real value is "<method 'validateCompositionCache' of 'panda3d.core.TransformState' objects>"
        'validateStates': None, # (!) real value is '<staticmethod(<built-in method validateStates of type object at 0x00007FFCFE291630>)>'
        'validate_composition_cache': None, # (!) real value is "<method 'validate_composition_cache' of 'panda3d.core.TransformState' objects>"
        'validate_states': None, # (!) real value is '<staticmethod(<built-in method validate_states of type object at 0x00007FFCFE291630>)>'
        'write': None, # (!) real value is "<method 'write' of 'panda3d.core.TransformState' objects>"
        'writeCompositionCache': None, # (!) real value is "<method 'writeCompositionCache' of 'panda3d.core.TransformState' objects>"
        'write_composition_cache': None, # (!) real value is "<method 'write_composition_cache' of 'panda3d.core.TransformState' objects>"
    }


