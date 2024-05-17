# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .NodeCachedReferenceCount import NodeCachedReferenceCount

class RenderState(NodeCachedReferenceCount):
    """
    /**
     * This represents a unique collection of RenderAttrib objects that correspond
     * to a particular renderable state.
     *
     * You should not attempt to create or modify a RenderState object directly.
     * Instead, call one of the make() functions to create one for you.  And
     * instead of modifying a RenderState object, create a new one.
     */
    """
    def addAttrib(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_attrib(RenderState self, const RenderAttrib attrib, int override)
        
        /**
         * Returns a new RenderState object that represents the same as the source
         * state, with the new RenderAttrib added.  If there is already a RenderAttrib
         * with the same type, it is replaced (unless the override is lower).
         */
        """
        pass

    def add_attrib(self, RenderState_self, const_RenderAttrib_attrib, int_override): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_attrib(RenderState self, const RenderAttrib attrib, int override)
        
        /**
         * Returns a new RenderState object that represents the same as the source
         * state, with the new RenderAttrib added.  If there is already a RenderAttrib
         * with the same type, it is replaced (unless the override is lower).
         */
        """
        pass

    def adjustAllPriorities(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        adjust_all_priorities(RenderState self, int adjustment)
        
        /**
         * Returns a new RenderState object that represents the same as the source
         * state, with all attributes' override values incremented (or decremented, if
         * negative) by the indicated amount.  If the override would drop below zero,
         * it is set to zero.
         */
        """
        pass

    def adjust_all_priorities(self, RenderState_self, int_adjustment): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        adjust_all_priorities(RenderState self, int adjustment)
        
        /**
         * Returns a new RenderState object that represents the same as the source
         * state, with all attributes' override values incremented (or decremented, if
         * negative) by the indicated amount.  If the override would drop below zero,
         * it is set to zero.
         */
        """
        pass

    def cacheRef(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        cache_ref(RenderState self)
        
        /**
         * Overrides this method to update PStats appropriately.
         */
        """
        pass

    def cacheUnref(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        cache_unref(RenderState self)
        
        /**
         * Overrides this method to update PStats appropriately.
         */
        """
        pass

    def cache_ref(self, RenderState_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        cache_ref(RenderState self)
        
        /**
         * Overrides this method to update PStats appropriately.
         */
        """
        pass

    def cache_unref(self, RenderState_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        cache_unref(RenderState self)
        
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
         * Empties the cache of composed RenderStates.  This makes every RenderState
         * forget what results when it is composed with other RenderStates.
         *
         * This will eliminate any RenderState objects that have been allocated but
         * have no references outside of the internal RenderState map.  It will not
         * eliminate RenderState objects that are still in use.
         *
         * Nowadays, this method should not be necessary, as reference-count cycles in
         * the composition cache should be automatically detected and broken.
         *
         * The return value is the number of RenderStates freed by this operation.
         */
        """
        pass

    def clearMungerCache(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_munger_cache()
        
        /**
         * Completely empties the cache of state + gsg -> munger, for all states and
         * all gsg's.  Normally there is no need to empty this cache.
         */
        """
        pass

    def clear_cache(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_cache()
        
        /**
         * Empties the cache of composed RenderStates.  This makes every RenderState
         * forget what results when it is composed with other RenderStates.
         *
         * This will eliminate any RenderState objects that have been allocated but
         * have no references outside of the internal RenderState map.  It will not
         * eliminate RenderState objects that are still in use.
         *
         * Nowadays, this method should not be necessary, as reference-count cycles in
         * the composition cache should be automatically detected and broken.
         *
         * The return value is the number of RenderStates freed by this operation.
         */
        """
        pass

    def clear_munger_cache(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_munger_cache()
        
        /**
         * Completely empties the cache of state + gsg -> munger, for all states and
         * all gsg's.  Normally there is no need to empty this cache.
         */
        """
        pass

    def compareMask(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        compare_mask(RenderState self, const RenderState other, BitMask compare_mask)
        
        /**
         * This version of compare_to takes a slot mask that indicates which
         * attributes to include in the comparison.  Unlike compare_to, this method
         * compares the attributes by pointer.
         */
        """
        pass

    def compareSort(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        compare_sort(RenderState self, const RenderState other)
        
        /**
         * Returns -1, 0, or 1 according to the relative sorting of these two
         * RenderStates, with regards to rendering performance, so that "heavier"
         * RenderAttribs (as defined by RenderAttribRegistry::get_slot_sort()) are
         * more likely to be grouped together.  This is not related to the sorting
         * order defined by compare_to.
         */
        """
        pass

    def compareTo(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        compare_to(RenderState self, const RenderState other)
        
        /**
         * Provides an arbitrary ordering among all unique RenderStates, so we can
         * store the essentially different ones in a big set and throw away the rest.
         *
         * This method is not needed outside of the RenderState class because all
         * equivalent RenderState objects are guaranteed to share the same pointer;
         * thus, a pointer comparison is always sufficient.
         */
        """
        pass

    def compare_mask(self, RenderState_self, const_RenderState_other, BitMask_compare_mask): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        compare_mask(RenderState self, const RenderState other, BitMask compare_mask)
        
        /**
         * This version of compare_to takes a slot mask that indicates which
         * attributes to include in the comparison.  Unlike compare_to, this method
         * compares the attributes by pointer.
         */
        """
        pass

    def compare_sort(self, RenderState_self, const_RenderState_other): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        compare_sort(RenderState self, const RenderState other)
        
        /**
         * Returns -1, 0, or 1 according to the relative sorting of these two
         * RenderStates, with regards to rendering performance, so that "heavier"
         * RenderAttribs (as defined by RenderAttribRegistry::get_slot_sort()) are
         * more likely to be grouped together.  This is not related to the sorting
         * order defined by compare_to.
         */
        """
        pass

    def compare_to(self, RenderState_self, const_RenderState_other): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        compare_to(RenderState self, const RenderState other)
        
        /**
         * Provides an arbitrary ordering among all unique RenderStates, so we can
         * store the essentially different ones in a big set and throw away the rest.
         *
         * This method is not needed outside of the RenderState class because all
         * equivalent RenderState objects are guaranteed to share the same pointer;
         * thus, a pointer comparison is always sufficient.
         */
        """
        pass

    def compose(self, RenderState_self, const_RenderState_other): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        compose(RenderState self, const RenderState other)
        
        /**
         * Returns a new RenderState object that represents the composition of this
         * state with the other state.
         *
         * The result of this operation is cached, and will be retained as long as
         * both this RenderState object and the other RenderState object continue to
         * exist.  Should one of them destruct, the cached entry will be removed, and
         * its pointer will be allowed to destruct as well.
         */
        """
        pass

    def cullCallback(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        cull_callback(RenderState self, CullTraverser trav, const CullTraverserData data)
        
        /**
         * Calls cull_callback() on each attrib.  If any attrib returns false,
         * interrupts the list and returns false immediately; otherwise, completes the
         * list and returns true.
         */
        """
        pass

    def cull_callback(self, RenderState_self, CullTraverser_trav, const_CullTraverserData_data): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        cull_callback(RenderState self, CullTraverser trav, const CullTraverserData data)
        
        /**
         * Calls cull_callback() on each attrib.  If any attrib returns false,
         * interrupts the list and returns false immediately; otherwise, completes the
         * list and returns true.
         */
        """
        pass

    def garbageCollect(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        garbage_collect()
        
        /**
         * Performs a garbage-collection cycle.  This must be called periodically if
         * garbage-collect-states is true to ensure that RenderStates get cleaned up
         * appropriately.  It does no harm to call it even if this variable is not
         * true, but there is probably no advantage in that case.
         *
         * This automatically calls RenderAttrib::garbage_collect() as well.
         */
        """
        pass

    def garbage_collect(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        garbage_collect()
        
        /**
         * Performs a garbage-collection cycle.  This must be called periodically if
         * garbage-collect-states is true to ensure that RenderStates get cleaned up
         * appropriately.  It does no harm to call it even if this variable is not
         * true, but there is probably no advantage in that case.
         *
         * This automatically calls RenderAttrib::garbage_collect() as well.
         */
        """
        pass

    def getAttrib(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_attrib(RenderState self, TypeHandle type)
        get_attrib(RenderState self, int slot)
        
        /**
         * Looks for a RenderAttrib of the indicated type in the state, and returns it
         * if it is found, or NULL if it is not.
         */
        
        /**
         * Returns the RenderAttrib with the indicated slot index, or NULL if there is
         * no such RenderAttrib in the state.
         */
        """
        pass

    def getAttribDef(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_attrib_def(RenderState self, int slot)
        
        /**
         * Returns the RenderAttrib with the indicated slot index, or the default
         * attrib for that slot if there is no such RenderAttrib in the state.
         */
        """
        pass

    def getBinIndex(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_bin_index(RenderState self)
        
        /**
         * Returns the bin index indicated by the CullBinAttrib, if any, associated by
         * this state (or the default bin index if there is no CullBinAttrib).  This
         * function is provided as an optimization for determining this at render
         * time.
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
        get_composition_cache(RenderState self)
        """
        pass

    def getCompositionCacheNumEntries(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_composition_cache_num_entries(RenderState self)
        
        /**
         * Returns the number of entries in the composition cache for this
         * RenderState.  This is the number of other RenderStates whose composition
         * with this one has been cached.  This number is not useful for any practical
         * reason other than performance analysis.
         */
        """
        pass

    def getCompositionCacheResult(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_composition_cache_result(RenderState self, int n)
        
        /**
         * Returns the result RenderState of the nth element in the composition cache.
         * Returns NULL if there doesn't happen to be an entry in the nth element.
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
        get_composition_cache_size(RenderState self)
        
        /**
         * Returns the number of slots in the composition cache for this RenderState.
         * You may use this as an upper bound when walking through all of the
         * composition cache results via get_composition_cache_source() or result().
         *
         * This has no practical value other than for examining the cache for
         * performance analysis.
         */
        """
        pass

    def getCompositionCacheSource(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_composition_cache_source(RenderState self, int n)
        
        /**
         * Returns the source RenderState of the nth element in the composition cache.
         * Returns NULL if there doesn't happen to be an entry in the nth element.
         * See get_composition_cache_result().
         *
         * This has no practical value other than for examining the cache for
         * performance analysis.
         */
        """
        pass

    def getDrawOrder(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_draw_order(RenderState self)
        
        // These methods are intended for use by low-level code, but they're also
        // handy enough to expose to high-level users.
        
        /**
         * Returns the draw order indicated by the CullBinAttrib, if any, associated
         * by this state (or 0 if there is no CullBinAttrib).  See get_bin_index().
         */
        """
        pass

    def getGeomRendering(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_geom_rendering(RenderState self, int geom_rendering)
        
        /**
         * Returns the union of the Geom::GeomRendering bits that will be required
         * once this RenderState is applied to a geom which includes the indicated
         * geom_rendering bits.
         */
        """
        pass

    def getHash(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_hash(RenderState self)
        
        /**
         * Returns a suitable hash value for phash_map.
         */
        """
        pass

    def getInvertCompositionCache(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_invert_composition_cache(RenderState self)
        """
        pass

    def getInvertCompositionCacheNumEntries(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_invert_composition_cache_num_entries(RenderState self)
        
        /**
         * Returns the number of entries in the invert_composition cache for this
         * RenderState.  This is similar to the composition cache, but it records
         * cache entries for the invert_compose() operation.  See
         * get_composition_cache_num_entries().
         */
        """
        pass

    def getInvertCompositionCacheResult(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_invert_composition_cache_result(RenderState self, int n)
        
        /**
         * Returns the result RenderState of the nth element in the invert composition
         * cache.  Returns NULL if there doesn't happen to be an entry in the nth
         * element.
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
        get_invert_composition_cache_size(RenderState self)
        
        /**
         * Returns the number of slots in the composition cache for this RenderState.
         * You may use this as an upper bound when walking through all of the
         * composition cache results via get_invert_composition_cache_source() or
         * result().
         *
         * This has no practical value other than for examining the cache for
         * performance analysis.
         */
        """
        pass

    def getInvertCompositionCacheSource(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_invert_composition_cache_source(RenderState self, int n)
        
        /**
         * Returns the source RenderState of the nth element in the invert composition
         * cache.  Returns NULL if there doesn't happen to be an entry in the nth
         * element.  See get_invert_composition_cache_result().
         *
         * This has no practical value other than for examining the cache for
         * performance analysis.
         */
        """
        pass

    def getMaxPriority(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_max_priority()
        
        /**
         * Returns the maximum priority number (sometimes called override) that may be
         * set on any node.  This may or may not be enforced, but the scene graph code
         * assumes that no priority numbers will be larger than this, and some effects
         * may not work properly if you use a larger number.
         */
        """
        pass

    def getNumStates(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_states()
        
        /**
         * Returns the total number of unique RenderState objects allocated in the
         * world.  This will go up and down during normal operations.
         */
        """
        pass

    def getNumUnusedStates(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_unused_states()
        
        /**
         * Returns the total number of RenderState objects that have been allocated
         * but have no references outside of the internal RenderState cache.
         *
         * A nonzero return value is not necessarily indicative of leaked references;
         * it is normal for two RenderState objects, both of which have references
         * held outside the cache, to have to result of their composition stored
         * within the cache.  This result will be retained within the cache until one
         * of the base RenderStates is released.
         *
         * Use list_cycles() to get an idea of the number of actual "leaked"
         * RenderState objects.
         */
        """
        pass

    def getOverride(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_override(RenderState self, TypeHandle type)
        get_override(RenderState self, int slot)
        
        /**
         * Looks for a RenderAttrib of the indicated type in the state, and returns
         * its override value if it is found, or 0 if it is not.
         */
        
        /**
         * Looks for a RenderAttrib of the indicated type in the state, and returns
         * its override value if it is found, or 0 if it is not.
         */
        """
        pass

    def getStates(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_states()
        """
        pass

    def getUnique(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_unique(RenderState self)
        
        /**
         * Returns the pointer to the unique RenderState in the cache that is
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

    def get_attrib(self, RenderState_self, TypeHandle_type): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_attrib(RenderState self, TypeHandle type)
        get_attrib(RenderState self, int slot)
        
        /**
         * Looks for a RenderAttrib of the indicated type in the state, and returns it
         * if it is found, or NULL if it is not.
         */
        
        /**
         * Returns the RenderAttrib with the indicated slot index, or NULL if there is
         * no such RenderAttrib in the state.
         */
        """
        pass

    def get_attrib_def(self, RenderState_self, int_slot): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_attrib_def(RenderState self, int slot)
        
        /**
         * Returns the RenderAttrib with the indicated slot index, or the default
         * attrib for that slot if there is no such RenderAttrib in the state.
         */
        """
        pass

    def get_bin_index(self, RenderState_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_bin_index(RenderState self)
        
        /**
         * Returns the bin index indicated by the CullBinAttrib, if any, associated by
         * this state (or the default bin index if there is no CullBinAttrib).  This
         * function is provided as an optimization for determining this at render
         * time.
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_composition_cache(self, RenderState_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_composition_cache(RenderState self)
        """
        pass

    def get_composition_cache_num_entries(self, RenderState_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_composition_cache_num_entries(RenderState self)
        
        /**
         * Returns the number of entries in the composition cache for this
         * RenderState.  This is the number of other RenderStates whose composition
         * with this one has been cached.  This number is not useful for any practical
         * reason other than performance analysis.
         */
        """
        pass

    def get_composition_cache_result(self, RenderState_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_composition_cache_result(RenderState self, int n)
        
        /**
         * Returns the result RenderState of the nth element in the composition cache.
         * Returns NULL if there doesn't happen to be an entry in the nth element.
         *
         * In general, a->compose(a->get_composition_cache_source(n)) ==
         * a->get_composition_cache_result(n).
         *
         * This has no practical value other than for examining the cache for
         * performance analysis.
         */
        """
        pass

    def get_composition_cache_size(self, RenderState_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_composition_cache_size(RenderState self)
        
        /**
         * Returns the number of slots in the composition cache for this RenderState.
         * You may use this as an upper bound when walking through all of the
         * composition cache results via get_composition_cache_source() or result().
         *
         * This has no practical value other than for examining the cache for
         * performance analysis.
         */
        """
        pass

    def get_composition_cache_source(self, RenderState_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_composition_cache_source(RenderState self, int n)
        
        /**
         * Returns the source RenderState of the nth element in the composition cache.
         * Returns NULL if there doesn't happen to be an entry in the nth element.
         * See get_composition_cache_result().
         *
         * This has no practical value other than for examining the cache for
         * performance analysis.
         */
        """
        pass

    def get_draw_order(self, RenderState_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_draw_order(RenderState self)
        
        // These methods are intended for use by low-level code, but they're also
        // handy enough to expose to high-level users.
        
        /**
         * Returns the draw order indicated by the CullBinAttrib, if any, associated
         * by this state (or 0 if there is no CullBinAttrib).  See get_bin_index().
         */
        """
        pass

    def get_geom_rendering(self, RenderState_self, int_geom_rendering): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_geom_rendering(RenderState self, int geom_rendering)
        
        /**
         * Returns the union of the Geom::GeomRendering bits that will be required
         * once this RenderState is applied to a geom which includes the indicated
         * geom_rendering bits.
         */
        """
        pass

    def get_hash(self, RenderState_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_hash(RenderState self)
        
        /**
         * Returns a suitable hash value for phash_map.
         */
        """
        pass

    def get_invert_composition_cache(self, RenderState_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_invert_composition_cache(RenderState self)
        """
        pass

    def get_invert_composition_cache_num_entries(self, RenderState_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_invert_composition_cache_num_entries(RenderState self)
        
        /**
         * Returns the number of entries in the invert_composition cache for this
         * RenderState.  This is similar to the composition cache, but it records
         * cache entries for the invert_compose() operation.  See
         * get_composition_cache_num_entries().
         */
        """
        pass

    def get_invert_composition_cache_result(self, RenderState_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_invert_composition_cache_result(RenderState self, int n)
        
        /**
         * Returns the result RenderState of the nth element in the invert composition
         * cache.  Returns NULL if there doesn't happen to be an entry in the nth
         * element.
         *
         * In general, a->invert_compose(a->get_invert_composition_cache_source(n)) ==
         * a->get_invert_composition_cache_result(n).
         *
         * This has no practical value other than for examining the cache for
         * performance analysis.
         */
        """
        pass

    def get_invert_composition_cache_size(self, RenderState_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_invert_composition_cache_size(RenderState self)
        
        /**
         * Returns the number of slots in the composition cache for this RenderState.
         * You may use this as an upper bound when walking through all of the
         * composition cache results via get_invert_composition_cache_source() or
         * result().
         *
         * This has no practical value other than for examining the cache for
         * performance analysis.
         */
        """
        pass

    def get_invert_composition_cache_source(self, RenderState_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_invert_composition_cache_source(RenderState self, int n)
        
        /**
         * Returns the source RenderState of the nth element in the invert composition
         * cache.  Returns NULL if there doesn't happen to be an entry in the nth
         * element.  See get_invert_composition_cache_result().
         *
         * This has no practical value other than for examining the cache for
         * performance analysis.
         */
        """
        pass

    def get_max_priority(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_max_priority()
        
        /**
         * Returns the maximum priority number (sometimes called override) that may be
         * set on any node.  This may or may not be enforced, but the scene graph code
         * assumes that no priority numbers will be larger than this, and some effects
         * may not work properly if you use a larger number.
         */
        """
        pass

    def get_num_states(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_states()
        
        /**
         * Returns the total number of unique RenderState objects allocated in the
         * world.  This will go up and down during normal operations.
         */
        """
        pass

    def get_num_unused_states(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_unused_states()
        
        /**
         * Returns the total number of RenderState objects that have been allocated
         * but have no references outside of the internal RenderState cache.
         *
         * A nonzero return value is not necessarily indicative of leaked references;
         * it is normal for two RenderState objects, both of which have references
         * held outside the cache, to have to result of their composition stored
         * within the cache.  This result will be retained within the cache until one
         * of the base RenderStates is released.
         *
         * Use list_cycles() to get an idea of the number of actual "leaked"
         * RenderState objects.
         */
        """
        pass

    def get_override(self, RenderState_self, TypeHandle_type): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_override(RenderState self, TypeHandle type)
        get_override(RenderState self, int slot)
        
        /**
         * Looks for a RenderAttrib of the indicated type in the state, and returns
         * its override value if it is found, or 0 if it is not.
         */
        
        /**
         * Looks for a RenderAttrib of the indicated type in the state, and returns
         * its override value if it is found, or 0 if it is not.
         */
        """
        pass

    def get_states(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_states()
        """
        pass

    def get_unique(self, RenderState_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_unique(RenderState self)
        
        /**
         * Returns the pointer to the unique RenderState in the cache that is
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

    def hasAttrib(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_attrib(RenderState self, TypeHandle type)
        has_attrib(RenderState self, int slot)
        
        /**
         * Returns true if an attrib of the indicated type is present, false
         * otherwise.
         */
        
        /**
         * Returns true if an attrib of the indicated type is present, false
         * otherwise.
         */
        """
        pass

    def hasCullCallback(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_cull_callback(RenderState self)
        
        /**
         * Returns true if any of the RenderAttribs in this state request a
         * cull_callback(), false if none of them do.
         */
        """
        pass

    def has_attrib(self, RenderState_self, TypeHandle_type): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_attrib(RenderState self, TypeHandle type)
        has_attrib(RenderState self, int slot)
        
        /**
         * Returns true if an attrib of the indicated type is present, false
         * otherwise.
         */
        
        /**
         * Returns true if an attrib of the indicated type is present, false
         * otherwise.
         */
        """
        pass

    def has_cull_callback(self, RenderState_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_cull_callback(RenderState self)
        
        /**
         * Returns true if any of the RenderAttribs in this state request a
         * cull_callback(), false if none of them do.
         */
        """
        pass

    def invertCompose(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        invert_compose(RenderState self, const RenderState other)
        
        /**
         * Returns a new RenderState object that represents the composition of this
         * state's inverse with the other state.
         *
         * This is similar to compose(), but is particularly useful for computing the
         * relative state of a node as viewed from some other node.
         */
        """
        pass

    def invert_compose(self, RenderState_self, const_RenderState_other): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        invert_compose(RenderState self, const RenderState other)
        
        /**
         * Returns a new RenderState object that represents the composition of this
         * state's inverse with the other state.
         *
         * This is similar to compose(), but is particularly useful for computing the
         * relative state of a node as viewed from some other node.
         */
        """
        pass

    def isEmpty(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_empty(RenderState self)
        
        /**
         * Returns true if the state is empty, false otherwise.
         */
        """
        pass

    def is_empty(self, RenderState_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_empty(RenderState self)
        
        /**
         * Returns true if the state is empty, false otherwise.
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
         * Lists all of the RenderStates in the cache to the output stream, one per
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
         * Lists all of the RenderStates in the cache to the output stream, one per
         * line.  This can be quite a lot of output if the cache is large, so be
         * prepared.
         */
        """
        pass

    def make(self, const_RenderAttrib_attrib): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        make(const RenderAttrib attrib)
        make(const RenderAttrib attrib1, const RenderAttrib attrib2)
        make(const RenderAttrib attrib, int override)
        make(const RenderAttrib attrib1, const RenderAttrib attrib2, const RenderAttrib attrib3)
        make(const RenderAttrib attrib1, const RenderAttrib attrib2, int override)
        make(const RenderAttrib attrib1, const RenderAttrib attrib2, const RenderAttrib attrib3, const RenderAttrib attrib4)
        make(const RenderAttrib attrib1, const RenderAttrib attrib2, const RenderAttrib attrib3, int override)
        make(const RenderAttrib attrib1, const RenderAttrib attrib2, const RenderAttrib attrib3, const RenderAttrib attrib4, const RenderAttrib attrib5, int override)
        make(const RenderAttrib attrib1, const RenderAttrib attrib2, const RenderAttrib attrib3, const RenderAttrib attrib4, int override)
        
        /**
         * Returns a RenderState with one attribute set.
         */
        
        /**
         * Returns a RenderState with two attributes set.
         */
        
        /**
         * Returns a RenderState with three attributes set.
         */
        
        /**
         * Returns a RenderState with four attributes set.
         */
        
        /**
         * Returns a RenderState with five attributes set.
         */
        
        /**
         * Returns a RenderState with n attributes set.
         */
        """
        pass

    def makeEmpty(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        make_empty()
        
        /**
         * Returns a RenderState with no attributes set.
         */
        """
        pass

    def make_empty(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        make_empty()
        
        /**
         * Returns a RenderState with no attributes set.
         */
        """
        pass

    def nodeRef(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        node_ref(RenderState self)
        
        /**
         * Overrides this method to update PStats appropriately.
         */
        """
        pass

    def nodeUnref(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        node_unref(RenderState self)
        
        /**
         * Overrides this method to update PStats appropriately.
         */
        """
        pass

    def node_ref(self, RenderState_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        node_ref(RenderState self)
        
        /**
         * Overrides this method to update PStats appropriately.
         */
        """
        pass

    def node_unref(self, RenderState_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        node_unref(RenderState self)
        
        /**
         * Overrides this method to update PStats appropriately.
         */
        """
        pass

    def output(self, RenderState_self, ostream_out): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        output(RenderState self, ostream out)
        
        /**
         *
         */
        """
        pass

    def removeAttrib(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        remove_attrib(RenderState self, TypeHandle type)
        remove_attrib(RenderState self, int slot)
        
        /**
         * Returns a new RenderState object that represents the same as the source
         * state, with the indicated RenderAttrib removed.
         */
        
        /**
         * Returns a new RenderState object that represents the same as the source
         * state, with the indicated RenderAttrib removed.
         */
        """
        pass

    def remove_attrib(self, RenderState_self, TypeHandle_type): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        remove_attrib(RenderState self, TypeHandle type)
        remove_attrib(RenderState self, int slot)
        
        /**
         * Returns a new RenderState object that represents the same as the source
         * state, with the indicated RenderAttrib removed.
         */
        
        /**
         * Returns a new RenderState object that represents the same as the source
         * state, with the indicated RenderAttrib removed.
         */
        """
        pass

    def setAttrib(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_attrib(RenderState self, const RenderAttrib attrib)
        set_attrib(RenderState self, const RenderAttrib attrib, int override)
        
        /**
         * Returns a new RenderState object that represents the same as the source
         * state, with the new RenderAttrib added.  If there is already a RenderAttrib
         * with the same type, it is replaced unconditionally.  The override is not
         * changed.
         */
        
        /**
         * Returns a new RenderState object that represents the same as the source
         * state, with the new RenderAttrib added.  If there is already a RenderAttrib
         * with the same type, it is replaced unconditionally.  The override is also
         * replaced unconditionally.
         */
        """
        pass

    def set_attrib(self, RenderState_self, const_RenderAttrib_attrib): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_attrib(RenderState self, const RenderAttrib attrib)
        set_attrib(RenderState self, const RenderAttrib attrib, int override)
        
        /**
         * Returns a new RenderState object that represents the same as the source
         * state, with the new RenderAttrib added.  If there is already a RenderAttrib
         * with the same type, it is replaced unconditionally.  The override is not
         * changed.
         */
        
        /**
         * Returns a new RenderState object that represents the same as the source
         * state, with the new RenderAttrib added.  If there is already a RenderAttrib
         * with the same type, it is replaced unconditionally.  The override is also
         * replaced unconditionally.
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
         * supposedly-const RenderState objects).
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
         * supposedly-const RenderState objects).
         */
        """
        pass

    def write(self, RenderState_self, ostream_out, int_indent_level): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        write(RenderState self, ostream out, int indent_level)
        
        /**
         *
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

    attribs = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__doc__': '/**\n * This represents a unique collection of RenderAttrib objects that correspond\n * to a particular renderable state.\n *\n * You should not attempt to create or modify a RenderState object directly.\n * Instead, call one of the make() functions to create one for you.  And\n * instead of modifying a RenderState object, create a new one.\n */',
        '__eq__': None, # (!) real value is "<slot wrapper '__eq__' of 'panda3d.core.RenderState' objects>"
        '__ge__': None, # (!) real value is "<slot wrapper '__ge__' of 'panda3d.core.RenderState' objects>"
        '__gt__': None, # (!) real value is "<slot wrapper '__gt__' of 'panda3d.core.RenderState' objects>"
        '__hash__': None, # (!) real value is "<slot wrapper '__hash__' of 'panda3d.core.RenderState' objects>"
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.RenderState' objects>"
        '__le__': None, # (!) real value is "<slot wrapper '__le__' of 'panda3d.core.RenderState' objects>"
        '__lt__': None, # (!) real value is "<slot wrapper '__lt__' of 'panda3d.core.RenderState' objects>"
        '__ne__': None, # (!) real value is "<slot wrapper '__ne__' of 'panda3d.core.RenderState' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE291F40>'
        '__repr__': None, # (!) real value is "<slot wrapper '__repr__' of 'panda3d.core.RenderState' objects>"
        '__str__': None, # (!) real value is "<slot wrapper '__str__' of 'panda3d.core.RenderState' objects>"
        'addAttrib': None, # (!) real value is "<method 'addAttrib' of 'panda3d.core.RenderState' objects>"
        'add_attrib': None, # (!) real value is "<method 'add_attrib' of 'panda3d.core.RenderState' objects>"
        'adjustAllPriorities': None, # (!) real value is "<method 'adjustAllPriorities' of 'panda3d.core.RenderState' objects>"
        'adjust_all_priorities': None, # (!) real value is "<method 'adjust_all_priorities' of 'panda3d.core.RenderState' objects>"
        'attribs': None, # (!) real value is "<attribute 'attribs' of 'panda3d.core.RenderState' objects>"
        'cacheRef': None, # (!) real value is "<method 'cacheRef' of 'panda3d.core.RenderState' objects>"
        'cacheUnref': None, # (!) real value is "<method 'cacheUnref' of 'panda3d.core.RenderState' objects>"
        'cache_ref': None, # (!) real value is "<method 'cache_ref' of 'panda3d.core.RenderState' objects>"
        'cache_unref': None, # (!) real value is "<method 'cache_unref' of 'panda3d.core.RenderState' objects>"
        'clearCache': None, # (!) real value is '<staticmethod(<built-in method clearCache of type object at 0x00007FFCFE291F40>)>'
        'clearMungerCache': None, # (!) real value is '<staticmethod(<built-in method clearMungerCache of type object at 0x00007FFCFE291F40>)>'
        'clear_cache': None, # (!) real value is '<staticmethod(<built-in method clear_cache of type object at 0x00007FFCFE291F40>)>'
        'clear_munger_cache': None, # (!) real value is '<staticmethod(<built-in method clear_munger_cache of type object at 0x00007FFCFE291F40>)>'
        'compareMask': None, # (!) real value is "<method 'compareMask' of 'panda3d.core.RenderState' objects>"
        'compareSort': None, # (!) real value is "<method 'compareSort' of 'panda3d.core.RenderState' objects>"
        'compareTo': None, # (!) real value is "<method 'compareTo' of 'panda3d.core.RenderState' objects>"
        'compare_mask': None, # (!) real value is "<method 'compare_mask' of 'panda3d.core.RenderState' objects>"
        'compare_sort': None, # (!) real value is "<method 'compare_sort' of 'panda3d.core.RenderState' objects>"
        'compare_to': None, # (!) real value is "<method 'compare_to' of 'panda3d.core.RenderState' objects>"
        'compose': None, # (!) real value is "<method 'compose' of 'panda3d.core.RenderState' objects>"
        'cullCallback': None, # (!) real value is "<method 'cullCallback' of 'panda3d.core.RenderState' objects>"
        'cull_callback': None, # (!) real value is "<method 'cull_callback' of 'panda3d.core.RenderState' objects>"
        'garbageCollect': None, # (!) real value is '<staticmethod(<built-in method garbageCollect of type object at 0x00007FFCFE291F40>)>'
        'garbage_collect': None, # (!) real value is '<staticmethod(<built-in method garbage_collect of type object at 0x00007FFCFE291F40>)>'
        'getAttrib': None, # (!) real value is "<method 'getAttrib' of 'panda3d.core.RenderState' objects>"
        'getAttribDef': None, # (!) real value is "<method 'getAttribDef' of 'panda3d.core.RenderState' objects>"
        'getBinIndex': None, # (!) real value is "<method 'getBinIndex' of 'panda3d.core.RenderState' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE291F40>)>'
        'getCompositionCache': None, # (!) real value is "<method 'getCompositionCache' of 'panda3d.core.RenderState' objects>"
        'getCompositionCacheNumEntries': None, # (!) real value is "<method 'getCompositionCacheNumEntries' of 'panda3d.core.RenderState' objects>"
        'getCompositionCacheResult': None, # (!) real value is "<method 'getCompositionCacheResult' of 'panda3d.core.RenderState' objects>"
        'getCompositionCacheSize': None, # (!) real value is "<method 'getCompositionCacheSize' of 'panda3d.core.RenderState' objects>"
        'getCompositionCacheSource': None, # (!) real value is "<method 'getCompositionCacheSource' of 'panda3d.core.RenderState' objects>"
        'getDrawOrder': None, # (!) real value is "<method 'getDrawOrder' of 'panda3d.core.RenderState' objects>"
        'getGeomRendering': None, # (!) real value is "<method 'getGeomRendering' of 'panda3d.core.RenderState' objects>"
        'getHash': None, # (!) real value is "<method 'getHash' of 'panda3d.core.RenderState' objects>"
        'getInvertCompositionCache': None, # (!) real value is "<method 'getInvertCompositionCache' of 'panda3d.core.RenderState' objects>"
        'getInvertCompositionCacheNumEntries': None, # (!) real value is "<method 'getInvertCompositionCacheNumEntries' of 'panda3d.core.RenderState' objects>"
        'getInvertCompositionCacheResult': None, # (!) real value is "<method 'getInvertCompositionCacheResult' of 'panda3d.core.RenderState' objects>"
        'getInvertCompositionCacheSize': None, # (!) real value is "<method 'getInvertCompositionCacheSize' of 'panda3d.core.RenderState' objects>"
        'getInvertCompositionCacheSource': None, # (!) real value is "<method 'getInvertCompositionCacheSource' of 'panda3d.core.RenderState' objects>"
        'getMaxPriority': None, # (!) real value is '<staticmethod(<built-in method getMaxPriority of type object at 0x00007FFCFE291F40>)>'
        'getNumStates': None, # (!) real value is '<staticmethod(<built-in method getNumStates of type object at 0x00007FFCFE291F40>)>'
        'getNumUnusedStates': None, # (!) real value is '<staticmethod(<built-in method getNumUnusedStates of type object at 0x00007FFCFE291F40>)>'
        'getOverride': None, # (!) real value is "<method 'getOverride' of 'panda3d.core.RenderState' objects>"
        'getStates': None, # (!) real value is '<staticmethod(<built-in method getStates of type object at 0x00007FFCFE291F40>)>'
        'getUnique': None, # (!) real value is "<method 'getUnique' of 'panda3d.core.RenderState' objects>"
        'getUnusedStates': None, # (!) real value is '<staticmethod(<built-in method getUnusedStates of type object at 0x00007FFCFE291F40>)>'
        'get_attrib': None, # (!) real value is "<method 'get_attrib' of 'panda3d.core.RenderState' objects>"
        'get_attrib_def': None, # (!) real value is "<method 'get_attrib_def' of 'panda3d.core.RenderState' objects>"
        'get_bin_index': None, # (!) real value is "<method 'get_bin_index' of 'panda3d.core.RenderState' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE291F40>)>'
        'get_composition_cache': None, # (!) real value is "<method 'get_composition_cache' of 'panda3d.core.RenderState' objects>"
        'get_composition_cache_num_entries': None, # (!) real value is "<method 'get_composition_cache_num_entries' of 'panda3d.core.RenderState' objects>"
        'get_composition_cache_result': None, # (!) real value is "<method 'get_composition_cache_result' of 'panda3d.core.RenderState' objects>"
        'get_composition_cache_size': None, # (!) real value is "<method 'get_composition_cache_size' of 'panda3d.core.RenderState' objects>"
        'get_composition_cache_source': None, # (!) real value is "<method 'get_composition_cache_source' of 'panda3d.core.RenderState' objects>"
        'get_draw_order': None, # (!) real value is "<method 'get_draw_order' of 'panda3d.core.RenderState' objects>"
        'get_geom_rendering': None, # (!) real value is "<method 'get_geom_rendering' of 'panda3d.core.RenderState' objects>"
        'get_hash': None, # (!) real value is "<method 'get_hash' of 'panda3d.core.RenderState' objects>"
        'get_invert_composition_cache': None, # (!) real value is "<method 'get_invert_composition_cache' of 'panda3d.core.RenderState' objects>"
        'get_invert_composition_cache_num_entries': None, # (!) real value is "<method 'get_invert_composition_cache_num_entries' of 'panda3d.core.RenderState' objects>"
        'get_invert_composition_cache_result': None, # (!) real value is "<method 'get_invert_composition_cache_result' of 'panda3d.core.RenderState' objects>"
        'get_invert_composition_cache_size': None, # (!) real value is "<method 'get_invert_composition_cache_size' of 'panda3d.core.RenderState' objects>"
        'get_invert_composition_cache_source': None, # (!) real value is "<method 'get_invert_composition_cache_source' of 'panda3d.core.RenderState' objects>"
        'get_max_priority': None, # (!) real value is '<staticmethod(<built-in method get_max_priority of type object at 0x00007FFCFE291F40>)>'
        'get_num_states': None, # (!) real value is '<staticmethod(<built-in method get_num_states of type object at 0x00007FFCFE291F40>)>'
        'get_num_unused_states': None, # (!) real value is '<staticmethod(<built-in method get_num_unused_states of type object at 0x00007FFCFE291F40>)>'
        'get_override': None, # (!) real value is "<method 'get_override' of 'panda3d.core.RenderState' objects>"
        'get_states': None, # (!) real value is '<staticmethod(<built-in method get_states of type object at 0x00007FFCFE291F40>)>'
        'get_unique': None, # (!) real value is "<method 'get_unique' of 'panda3d.core.RenderState' objects>"
        'get_unused_states': None, # (!) real value is '<staticmethod(<built-in method get_unused_states of type object at 0x00007FFCFE291F40>)>'
        'hasAttrib': None, # (!) real value is "<method 'hasAttrib' of 'panda3d.core.RenderState' objects>"
        'hasCullCallback': None, # (!) real value is "<method 'hasCullCallback' of 'panda3d.core.RenderState' objects>"
        'has_attrib': None, # (!) real value is "<method 'has_attrib' of 'panda3d.core.RenderState' objects>"
        'has_cull_callback': None, # (!) real value is "<method 'has_cull_callback' of 'panda3d.core.RenderState' objects>"
        'invertCompose': None, # (!) real value is "<method 'invertCompose' of 'panda3d.core.RenderState' objects>"
        'invert_compose': None, # (!) real value is "<method 'invert_compose' of 'panda3d.core.RenderState' objects>"
        'isEmpty': None, # (!) real value is "<method 'isEmpty' of 'panda3d.core.RenderState' objects>"
        'is_empty': None, # (!) real value is "<method 'is_empty' of 'panda3d.core.RenderState' objects>"
        'listCycles': None, # (!) real value is '<staticmethod(<built-in method listCycles of type object at 0x00007FFCFE291F40>)>'
        'listStates': None, # (!) real value is '<staticmethod(<built-in method listStates of type object at 0x00007FFCFE291F40>)>'
        'list_cycles': None, # (!) real value is '<staticmethod(<built-in method list_cycles of type object at 0x00007FFCFE291F40>)>'
        'list_states': None, # (!) real value is '<staticmethod(<built-in method list_states of type object at 0x00007FFCFE291F40>)>'
        'make': None, # (!) real value is '<staticmethod(<built-in method make of type object at 0x00007FFCFE291F40>)>'
        'makeEmpty': None, # (!) real value is '<staticmethod(<built-in method makeEmpty of type object at 0x00007FFCFE291F40>)>'
        'make_empty': None, # (!) real value is '<staticmethod(<built-in method make_empty of type object at 0x00007FFCFE291F40>)>'
        'nodeRef': None, # (!) real value is "<method 'nodeRef' of 'panda3d.core.RenderState' objects>"
        'nodeUnref': None, # (!) real value is "<method 'nodeUnref' of 'panda3d.core.RenderState' objects>"
        'node_ref': None, # (!) real value is "<method 'node_ref' of 'panda3d.core.RenderState' objects>"
        'node_unref': None, # (!) real value is "<method 'node_unref' of 'panda3d.core.RenderState' objects>"
        'output': None, # (!) real value is "<method 'output' of 'panda3d.core.RenderState' objects>"
        'removeAttrib': None, # (!) real value is "<method 'removeAttrib' of 'panda3d.core.RenderState' objects>"
        'remove_attrib': None, # (!) real value is "<method 'remove_attrib' of 'panda3d.core.RenderState' objects>"
        'setAttrib': None, # (!) real value is "<method 'setAttrib' of 'panda3d.core.RenderState' objects>"
        'set_attrib': None, # (!) real value is "<method 'set_attrib' of 'panda3d.core.RenderState' objects>"
        'validateStates': None, # (!) real value is '<staticmethod(<built-in method validateStates of type object at 0x00007FFCFE291F40>)>'
        'validate_states': None, # (!) real value is '<staticmethod(<built-in method validate_states of type object at 0x00007FFCFE291F40>)>'
        'write': None, # (!) real value is "<method 'write' of 'panda3d.core.RenderState' objects>"
    }


