# encoding: utf-8
# module panda3d.egg
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\egg.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import panda3d.core as __panda3d_core


from .EggObject import EggObject

from .EggAttributes import EggAttributes

class EggVertex(EggObject, EggAttributes):
    """
    /**
     * Any one-, two-, three-, or four-component vertex, possibly with attributes
     * such as a normal.
     */
    """
    def assign(self, const_EggVertex_self, const_EggVertex_copy): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        assign(const EggVertex self, const EggVertex copy)
        
        /**
         * Copies all properties of the vertex except its vertex pool, index number,
         * and group membership.
         */
        """
        pass

    def clearAux(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_aux(const EggVertex self)
        clear_aux(const EggVertex self, str name)
        
        /**
         * Removes all auxiliary data from the vertex.
         */
        
        /**
         * Removes the named auxiliary data from the vertex.
         */
        """
        pass

    def clearGrefs(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_grefs(const EggVertex self)
        
        /**
         * Removes all group references from the vertex, so that it is not assigned to
         * any group.
         */
        """
        pass

    def clearUv(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_uv(const EggVertex self)
        clear_uv(const EggVertex self, str name)
        
        /**
         * Removes all UV coordinate pairs from the vertex.
         */
        
        /**
         * Removes the named UV coordinate pair from the vertex, along with any UV
         * morphs.
         */
        """
        pass

    def clear_aux(self, const_EggVertex_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_aux(const EggVertex self)
        clear_aux(const EggVertex self, str name)
        
        /**
         * Removes all auxiliary data from the vertex.
         */
        
        /**
         * Removes the named auxiliary data from the vertex.
         */
        """
        pass

    def clear_grefs(self, const_EggVertex_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_grefs(const EggVertex self)
        
        /**
         * Removes all group references from the vertex, so that it is not assigned to
         * any group.
         */
        """
        pass

    def clear_uv(self, const_EggVertex_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_uv(const EggVertex self)
        clear_uv(const EggVertex self, str name)
        
        /**
         * Removes all UV coordinate pairs from the vertex.
         */
        
        /**
         * Removes the named UV coordinate pair from the vertex, along with any UV
         * morphs.
         */
        """
        pass

    def compareTo(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        compare_to(EggVertex self, const EggVertex other)
        
        /**
         * An ordering operator to compare two vertices for sorting order.  This
         * imposes an arbitrary ordering useful to identify unique vertices.
         *
         * Group membership is not considered in this comparison.  This is somewhat
         * problematic, but cannot easily be helped, because considering group
         * membership would make it difficult to add and remove groups from vertices.
         * It also makes it impossible to meaningfully compare with a concrete
         * EggVertex object (which cannot have group memberships).
         *
         * However, this is not altogether bad, because two vertices that are
         * identical in all other properties should generally also be identical in
         * group memberships, else the vertices will tend to fly apart when the joints
         * animate.
         */
        """
        pass

    def compare_to(self, EggVertex_self, const_EggVertex_other): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        compare_to(EggVertex self, const EggVertex other)
        
        /**
         * An ordering operator to compare two vertices for sorting order.  This
         * imposes an arbitrary ordering useful to identify unique vertices.
         *
         * Group membership is not considered in this comparison.  This is somewhat
         * problematic, but cannot easily be helped, because considering group
         * membership would make it difficult to add and remove groups from vertices.
         * It also makes it impossible to meaningfully compare with a concrete
         * EggVertex object (which cannot have group memberships).
         *
         * However, this is not altogether bad, because two vertices that are
         * identical in all other properties should generally also be identical in
         * group memberships, else the vertices will tend to fly apart when the joints
         * animate.
         */
        """
        pass

    def copyGrefsFrom(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        copy_grefs_from(const EggVertex self, const EggVertex other)
        
        /**
         * Copies all the group references from the other vertex onto this one.  This
         * assigns the current vertex to exactly the same groups, with exactly the
         * same memberships, as the given one.
         *
         * Warning: only an EggVertex allocated from the free store may have groups
         * assigned to it.  Do not attempt to call this on a temporary concrete
         * EggVertex object; a core dump will certainly result.
         */
        """
        pass

    def copy_grefs_from(self, const_EggVertex_self, const_EggVertex_other): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        copy_grefs_from(const EggVertex self, const EggVertex other)
        
        /**
         * Copies all the group references from the other vertex onto this one.  This
         * assigns the current vertex to exactly the same groups, with exactly the
         * same memberships, as the given one.
         *
         * Warning: only an EggVertex allocated from the free store may have groups
         * assigned to it.  Do not attempt to call this on a temporary concrete
         * EggVertex object; a core dump will certainly result.
         */
        """
        pass

    def getAux(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_aux(EggVertex self, str name)
        
        /**
         * Returns the named auxiliary data quadruple on the vertex.  It is an error
         * to call this if has_aux(name) returned false.
         */
        """
        pass

    def getAuxObj(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_aux_obj(EggVertex self, str name)
        
        /**
         * Returns the named EggVertexAux object, which defines the auxiliary data for
         * this name.  This object might be shared between multiple vertices.  You
         * should not attempt to modify this object; instead, call modify_aux_object
         * to return a modifiable pointer.
         */
        """
        pass

    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getExternalIndex(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_external_index(EggVertex self)
        
        /**
         * Returns the number set by set_external_index().  See set_external_index().
         */
        """
        pass

    def getExternalIndex2(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_external_index2(EggVertex self)
        
        /**
         * Returns the number set by set_external_index2().  See
         * set_external_index2().
         */
        """
        pass

    def getIndex(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_index(EggVertex self)
        
        /**
         * Returns the index number of the vertex within its pool.
         */
        """
        pass

    def getNumDimensions(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_dimensions(EggVertex self)
        
        // get_pos[123] return the pos as the corresponding type.  It is an error to
        // call any of these without first verifying that get_num_dimensions()
        // matches the desired type.  However, get_pos4() may always be called; it
        // returns the pos as a four-component point in homogeneous space (with a
        // 1.0 in the last position if the pos has fewer than four components).
        
        /**
         * Returns the number of dimensions the vertex uses.  Usually this will be 3,
         * but it may be 1, 2, 3, or 4.
         */
        """
        pass

    def getNumGlobalCoord(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_global_coord(EggVertex self)
        
        /**
         * Returns the number of primitives that own this vertex whose vertices are
         * interpreted in the global coordinate system.
         */
        """
        pass

    def getNumLocalCoord(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_local_coord(EggVertex self)
        
        /**
         * Returns the number of primitives that own this vertex whose vertices are
         * interpreted to be in a local coordinate system.
         */
        """
        pass

    def getPool(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_pool(EggVertex self)
        
        /**
         * Returns the vertex pool this vertex belongs in.  This may be NULL if the
         * vertex has not been added to a pool.
         */
        """
        pass

    def getPos1(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_pos1(EggVertex self)
        
        /**
         * Only valid if get_num_dimensions() returns 1. Returns the position as a
         * one-dimensional value.
         */
        """
        pass

    def getPos2(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_pos2(EggVertex self)
        
        /**
         * Only valid if get_num_dimensions() returns 2. Returns the position as a
         * two-dimensional value.
         */
        """
        pass

    def getPos3(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_pos3(EggVertex self)
        
        /**
         * Valid if get_num_dimensions() returns 3 or 4. Returns the position as a
         * three-dimensional value.
         */
        """
        pass

    def getPos4(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_pos4(EggVertex self)
        
        /**
         * This is always valid, regardless of the value of get_num_dimensions.  It
         * returns the position as a four-dimensional value.  If the pos has fewer
         * than four dimensions, this value represents the pos extended into four-
         * dimensional homogenous space, e.g.  by adding 1 as the fourth component.
         */
        """
        pass

    def getUv(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_uv(EggVertex self)
        get_uv(EggVertex self, str name)
        
        /**
         * Returns the unnamed UV coordinate pair on the vertex.  It is an error to
         * call this if has_uv() has returned false.
         *
         * This is the more restrictive interface, and is generally useful only in the
         * absence of multitexturing; see get_uv(name) for the interface that supports
         * multitexturing.
         */
        
        /**
         * Returns the named UV coordinate pair on the vertex.  It is an error to call
         * this if has_uv(name) returned false.
         */
        """
        pass

    def getUvObj(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_uv_obj(EggVertex self, str name)
        
        /**
         * Returns the named EggVertexUV object, which defines both the UV coordinate
         * pair for this name and the UV morphs.  This object might be shared between
         * multiple vertices.  You should not attempt to modify this object; instead,
         * call modify_uv_object to return a modifiable pointer.
         */
        """
        pass

    def getUvw(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_uvw(EggVertex self, str name)
        
        /**
         * Returns the named UV coordinate triple on the vertex.  It is an error to
         * call this if has_uvw(name) returned false.
         */
        """
        pass

    def get_aux(self, EggVertex_self, str_name): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_aux(EggVertex self, str name)
        
        /**
         * Returns the named auxiliary data quadruple on the vertex.  It is an error
         * to call this if has_aux(name) returned false.
         */
        """
        pass

    def get_aux_obj(self, EggVertex_self, str_name): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_aux_obj(EggVertex self, str name)
        
        /**
         * Returns the named EggVertexAux object, which defines the auxiliary data for
         * this name.  This object might be shared between multiple vertices.  You
         * should not attempt to modify this object; instead, call modify_aux_object
         * to return a modifiable pointer.
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_external_index(self, EggVertex_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_external_index(EggVertex self)
        
        /**
         * Returns the number set by set_external_index().  See set_external_index().
         */
        """
        pass

    def get_external_index2(self, EggVertex_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_external_index2(EggVertex self)
        
        /**
         * Returns the number set by set_external_index2().  See
         * set_external_index2().
         */
        """
        pass

    def get_index(self, EggVertex_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_index(EggVertex self)
        
        /**
         * Returns the index number of the vertex within its pool.
         */
        """
        pass

    def get_num_dimensions(self, EggVertex_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_dimensions(EggVertex self)
        
        // get_pos[123] return the pos as the corresponding type.  It is an error to
        // call any of these without first verifying that get_num_dimensions()
        // matches the desired type.  However, get_pos4() may always be called; it
        // returns the pos as a four-component point in homogeneous space (with a
        // 1.0 in the last position if the pos has fewer than four components).
        
        /**
         * Returns the number of dimensions the vertex uses.  Usually this will be 3,
         * but it may be 1, 2, 3, or 4.
         */
        """
        pass

    def get_num_global_coord(self, EggVertex_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_global_coord(EggVertex self)
        
        /**
         * Returns the number of primitives that own this vertex whose vertices are
         * interpreted in the global coordinate system.
         */
        """
        pass

    def get_num_local_coord(self, EggVertex_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_local_coord(EggVertex self)
        
        /**
         * Returns the number of primitives that own this vertex whose vertices are
         * interpreted to be in a local coordinate system.
         */
        """
        pass

    def get_pool(self, EggVertex_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_pool(EggVertex self)
        
        /**
         * Returns the vertex pool this vertex belongs in.  This may be NULL if the
         * vertex has not been added to a pool.
         */
        """
        pass

    def get_pos1(self, EggVertex_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_pos1(EggVertex self)
        
        /**
         * Only valid if get_num_dimensions() returns 1. Returns the position as a
         * one-dimensional value.
         */
        """
        pass

    def get_pos2(self, EggVertex_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_pos2(EggVertex self)
        
        /**
         * Only valid if get_num_dimensions() returns 2. Returns the position as a
         * two-dimensional value.
         */
        """
        pass

    def get_pos3(self, EggVertex_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_pos3(EggVertex self)
        
        /**
         * Valid if get_num_dimensions() returns 3 or 4. Returns the position as a
         * three-dimensional value.
         */
        """
        pass

    def get_pos4(self, EggVertex_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_pos4(EggVertex self)
        
        /**
         * This is always valid, regardless of the value of get_num_dimensions.  It
         * returns the position as a four-dimensional value.  If the pos has fewer
         * than four dimensions, this value represents the pos extended into four-
         * dimensional homogenous space, e.g.  by adding 1 as the fourth component.
         */
        """
        pass

    def get_uv(self, EggVertex_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_uv(EggVertex self)
        get_uv(EggVertex self, str name)
        
        /**
         * Returns the unnamed UV coordinate pair on the vertex.  It is an error to
         * call this if has_uv() has returned false.
         *
         * This is the more restrictive interface, and is generally useful only in the
         * absence of multitexturing; see get_uv(name) for the interface that supports
         * multitexturing.
         */
        
        /**
         * Returns the named UV coordinate pair on the vertex.  It is an error to call
         * this if has_uv(name) returned false.
         */
        """
        pass

    def get_uvw(self, EggVertex_self, str_name): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_uvw(EggVertex self, str name)
        
        /**
         * Returns the named UV coordinate triple on the vertex.  It is an error to
         * call this if has_uvw(name) returned false.
         */
        """
        pass

    def get_uv_obj(self, EggVertex_self, str_name): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_uv_obj(EggVertex self, str name)
        
        /**
         * Returns the named EggVertexUV object, which defines both the UV coordinate
         * pair for this name and the UV morphs.  This object might be shared between
         * multiple vertices.  You should not attempt to modify this object; instead,
         * call modify_uv_object to return a modifiable pointer.
         */
        """
        pass

    def hasAux(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_aux(EggVertex self)
        has_aux(EggVertex self, str name)
        
        /**
         * Returns true if the vertex has any auxiliary data, false otherwise.
         */
        
        /**
         * Returns true if the vertex has the named auxiliary data quadruple.
         */
        """
        pass

    def hasGref(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_gref(EggVertex self, const EggGroup group)
        
        /**
         * Returns true if the indicated group references this vertex, false
         * otherwise.
         */
        """
        pass

    def hasPref(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_pref(EggVertex self, const EggPrimitive prim)
        
        /**
         * Returns the number of times the vertex appears in the indicated primitive,
         * or 0 if it does not appear.
         */
        """
        pass

    def hasUv(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_uv(EggVertex self)
        has_uv(EggVertex self, str name)
        
        /**
         * Returns true if the vertex has an unnamed UV coordinate pair, false
         * otherwise.
         *
         * This is the more restrictive interface, and is generally useful only in the
         * absence of multitexturing; see has_uv(name) for the interface that supports
         * multitexturing.
         */
        
        /**
         * Returns true if the vertex has the named UV coordinate pair, and the named
         * UV coordinate pair is 2-d, false otherwise.
         */
        """
        pass

    def hasUvw(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_uvw(EggVertex self, str name)
        
        /**
         * Returns true if the vertex has the named UV coordinate triple, and the
         * named UV coordinate triple is 3-d, false otherwise.
         */
        """
        pass

    def has_aux(self, EggVertex_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_aux(EggVertex self)
        has_aux(EggVertex self, str name)
        
        /**
         * Returns true if the vertex has any auxiliary data, false otherwise.
         */
        
        /**
         * Returns true if the vertex has the named auxiliary data quadruple.
         */
        """
        pass

    def has_gref(self, EggVertex_self, const_EggGroup_group): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_gref(EggVertex self, const EggGroup group)
        
        /**
         * Returns true if the indicated group references this vertex, false
         * otherwise.
         */
        """
        pass

    def has_pref(self, EggVertex_self, const_EggPrimitive_prim): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_pref(EggVertex self, const EggPrimitive prim)
        
        /**
         * Returns the number of times the vertex appears in the indicated primitive,
         * or 0 if it does not appear.
         */
        """
        pass

    def has_uv(self, EggVertex_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_uv(EggVertex self)
        has_uv(EggVertex self, str name)
        
        /**
         * Returns true if the vertex has an unnamed UV coordinate pair, false
         * otherwise.
         *
         * This is the more restrictive interface, and is generally useful only in the
         * absence of multitexturing; see has_uv(name) for the interface that supports
         * multitexturing.
         */
        
        /**
         * Returns true if the vertex has the named UV coordinate pair, and the named
         * UV coordinate pair is 2-d, false otherwise.
         */
        """
        pass

    def has_uvw(self, EggVertex_self, str_name): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_uvw(EggVertex self, str name)
        
        /**
         * Returns true if the vertex has the named UV coordinate triple, and the
         * named UV coordinate triple is 3-d, false otherwise.
         */
        """
        pass

    def isForwardReference(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_forward_reference(EggVertex self)
        
        /**
         * Returns true if the vertex is a forward reference to some vertex that
         * hasn't been defined yet.  In this case, the vertex may not have any
         * properties filled in yet.
         *
         * This can only happen if you implicitly create a vertex via
         * EggVertexPool::get_forward_vertex(). Presumably, when the vertex pool is
         * later filled in, this vertex will be replaced with real data.
         */
        """
        pass

    def is_forward_reference(self, EggVertex_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_forward_reference(EggVertex self)
        
        /**
         * Returns true if the vertex is a forward reference to some vertex that
         * hasn't been defined yet.  In this case, the vertex may not have any
         * properties filled in yet.
         *
         * This can only happen if you implicitly create a vertex via
         * EggVertexPool::get_forward_vertex(). Presumably, when the vertex pool is
         * later filled in, this vertex will be replaced with real data.
         */
        """
        pass

    def makeAverage(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        make_average(const EggVertex first, const EggVertex second)
        
        /**
         * Creates a new vertex that lies in between the two given vertices.  The
         * attributes for the UV sets they have in common are averaged.
         *
         * Both vertices need to be either in no pool, or in the same pool.  In the
         * latter case, the new vertex will be placed in that pool.
         */
        """
        pass

    def make_average(self, const_EggVertex_first, const_EggVertex_second): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        make_average(const EggVertex first, const EggVertex second)
        
        /**
         * Creates a new vertex that lies in between the two given vertices.  The
         * attributes for the UV sets they have in common are averaged.
         *
         * Both vertices need to be either in no pool, or in the same pool.  In the
         * latter case, the new vertex will be placed in that pool.
         */
        """
        pass

    def modifyAuxObj(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        modify_aux_obj(const EggVertex self, str name)
        
        /**
         * Returns a modifiable pointer to the named EggVertexAux object, which
         * defines the auxiliary data for this name.  Returns NULL if there is no such
         * named UV object.
         */
        """
        pass

    def modifyUvObj(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        modify_uv_obj(const EggVertex self, str name)
        
        /**
         * Returns a modifiable pointer to the named EggVertexUV object, which defines
         * both the UV coordinate pair for this name and the UV morphs.  Returns NULL
         * if there is no such named UV object.
         */
        """
        pass

    def modify_aux_obj(self, const_EggVertex_self, str_name): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        modify_aux_obj(const EggVertex self, str name)
        
        /**
         * Returns a modifiable pointer to the named EggVertexAux object, which
         * defines the auxiliary data for this name.  Returns NULL if there is no such
         * named UV object.
         */
        """
        pass

    def modify_uv_obj(self, const_EggVertex_self, str_name): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        modify_uv_obj(const EggVertex self, str name)
        
        /**
         * Returns a modifiable pointer to the named EggVertexUV object, which defines
         * both the UV coordinate pair for this name and the UV morphs.  Returns NULL
         * if there is no such named UV object.
         */
        """
        pass

    def output(self, EggVertex_self, ostream_out): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        output(EggVertex self, ostream out)
        
        /**
         *
         */
        """
        pass

    def setAux(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_aux(const EggVertex self, str name, const LVecBase4d aux)
        
        /**
         * Sets the indicated auxiliary data quadruple on the vertex.  This replaces
         * any auxiliary data with the same name already on the vertex.
         */
        """
        pass

    def setAuxObj(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_aux_obj(const EggVertex self, EggVertexAux vertex_aux)
        
        /**
         * Sets the indicated EggVertexAux on the vertex.  This replaces any auxiliary
         * data with the same name already on the vertex.
         */
        """
        pass

    def setExternalIndex(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_external_index(const EggVertex self, int external_index)
        
        /**
         * Sets a special index number that is associated with the EggVertex (but is
         * not written to the egg file). This number is not interpreted by any egg
         * code; it is simply maintained along with the vertex.  It *is* used to
         * differentiate otherwise identical vertices in
         * EggVertexPool::create_unique_vertex(), however.
         *
         * The intention of this number is as an aid for file converters, to associate
         * an EggVertex back to the index number of the original source vertex.
         */
        """
        pass

    def setExternalIndex2(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_external_index2(const EggVertex self, int external_index2)
        
        /**
         * Similar to set_external_index(), but this is a different number which may
         * be used for a different purpose by the calling code.  The egg library does
         * not assign any meaning to this number or use it in any way.
         */
        """
        pass

    def setPos(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_pos(const EggVertex self, const LPoint4d pos)
        set_pos(const EggVertex self, const LPoint2d pos)
        set_pos(const EggVertex self, const LPoint3d pos)
        set_pos(const EggVertex self, double pos)
        
        // The pos might have 1, 2, 3, or 4 dimensions.  That complicates things a
        // bit.
        
        /**
         * Sets the vertex position.  This variant sets the vertex to a one-
         * dimensional value.
         */
        
        /**
         * Sets the vertex position.  This variant sets the vertex to a two-
         * dimensional value.
         */
        
        /**
         * Sets the vertex position.  This variant sets the vertex to a three-
         * dimensional value.
         */
        
        /**
         * Sets the vertex position.  This variant sets the vertex to a four-
         * dimensional value.
         */
        """
        pass

    def setPos4(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_pos4(const EggVertex self, const LPoint4d pos)
        
        /**
         * This special flavor of set_pos() sets the vertex as a four-component value,
         * but does not change the set number of dimensions.  It's handy for
         * retrieving the vertex position via get_pos4, manipulating it, then storing
         * it back again, without worrying about the number of dimensions it actually
         * had.
         */
        """
        pass

    def setUv(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_uv(const EggVertex self, const LPoint2d texCoord)
        set_uv(const EggVertex self, str name, const LPoint2d texCoord)
        
        /**
         * Replaces the unnamed UV coordinate pair on the vertex with the indicated
         * value.
         *
         * This is the more restrictive interface, and is generally useful only in the
         * absence of multitexturing; see set_uv(name, uv) for the interface that
         * supports multitexturing.
         */
        
        /**
         * Sets the indicated UV coordinate pair on the vertex.  This replaces any UV
         * coordinate pair with the same name already on the vertex, but preserves UV
         * morphs.
         */
        """
        pass

    def setUvObj(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_uv_obj(const EggVertex self, EggVertexUV vertex_uv)
        
        /**
         * Sets the indicated EggVertexUV on the vertex.  This replaces any UV
         * coordinate pair with the same name already on the vertex, including UV
         * morphs.
         */
        """
        pass

    def setUvw(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_uvw(const EggVertex self, str name, const LPoint3d texCoord)
        
        /**
         * Sets the indicated UV coordinate triple on the vertex.  This replaces any
         * UV coordinate pair or triple with the same name already on the vertex, but
         * preserves UV morphs.
         */
        """
        pass

    def set_aux(self, const_EggVertex_self, str_name, const_LVecBase4d_aux): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_aux(const EggVertex self, str name, const LVecBase4d aux)
        
        /**
         * Sets the indicated auxiliary data quadruple on the vertex.  This replaces
         * any auxiliary data with the same name already on the vertex.
         */
        """
        pass

    def set_aux_obj(self, const_EggVertex_self, EggVertexAux_vertex_aux): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_aux_obj(const EggVertex self, EggVertexAux vertex_aux)
        
        /**
         * Sets the indicated EggVertexAux on the vertex.  This replaces any auxiliary
         * data with the same name already on the vertex.
         */
        """
        pass

    def set_external_index(self, const_EggVertex_self, int_external_index): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_external_index(const EggVertex self, int external_index)
        
        /**
         * Sets a special index number that is associated with the EggVertex (but is
         * not written to the egg file). This number is not interpreted by any egg
         * code; it is simply maintained along with the vertex.  It *is* used to
         * differentiate otherwise identical vertices in
         * EggVertexPool::create_unique_vertex(), however.
         *
         * The intention of this number is as an aid for file converters, to associate
         * an EggVertex back to the index number of the original source vertex.
         */
        """
        pass

    def set_external_index2(self, const_EggVertex_self, int_external_index2): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_external_index2(const EggVertex self, int external_index2)
        
        /**
         * Similar to set_external_index(), but this is a different number which may
         * be used for a different purpose by the calling code.  The egg library does
         * not assign any meaning to this number or use it in any way.
         */
        """
        pass

    def set_pos(self, const_EggVertex_self, const_LPoint4d_pos): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_pos(const EggVertex self, const LPoint4d pos)
        set_pos(const EggVertex self, const LPoint2d pos)
        set_pos(const EggVertex self, const LPoint3d pos)
        set_pos(const EggVertex self, double pos)
        
        // The pos might have 1, 2, 3, or 4 dimensions.  That complicates things a
        // bit.
        
        /**
         * Sets the vertex position.  This variant sets the vertex to a one-
         * dimensional value.
         */
        
        /**
         * Sets the vertex position.  This variant sets the vertex to a two-
         * dimensional value.
         */
        
        /**
         * Sets the vertex position.  This variant sets the vertex to a three-
         * dimensional value.
         */
        
        /**
         * Sets the vertex position.  This variant sets the vertex to a four-
         * dimensional value.
         */
        """
        pass

    def set_pos4(self, const_EggVertex_self, const_LPoint4d_pos): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_pos4(const EggVertex self, const LPoint4d pos)
        
        /**
         * This special flavor of set_pos() sets the vertex as a four-component value,
         * but does not change the set number of dimensions.  It's handy for
         * retrieving the vertex position via get_pos4, manipulating it, then storing
         * it back again, without worrying about the number of dimensions it actually
         * had.
         */
        """
        pass

    def set_uv(self, const_EggVertex_self, const_LPoint2d_texCoord): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_uv(const EggVertex self, const LPoint2d texCoord)
        set_uv(const EggVertex self, str name, const LPoint2d texCoord)
        
        /**
         * Replaces the unnamed UV coordinate pair on the vertex with the indicated
         * value.
         *
         * This is the more restrictive interface, and is generally useful only in the
         * absence of multitexturing; see set_uv(name, uv) for the interface that
         * supports multitexturing.
         */
        
        /**
         * Sets the indicated UV coordinate pair on the vertex.  This replaces any UV
         * coordinate pair with the same name already on the vertex, but preserves UV
         * morphs.
         */
        """
        pass

    def set_uvw(self, const_EggVertex_self, str_name, const_LPoint3d_texCoord): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_uvw(const EggVertex self, str name, const LPoint3d texCoord)
        
        /**
         * Sets the indicated UV coordinate triple on the vertex.  This replaces any
         * UV coordinate pair or triple with the same name already on the vertex, but
         * preserves UV morphs.
         */
        """
        pass

    def set_uv_obj(self, const_EggVertex_self, EggVertexUV_vertex_uv): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_uv_obj(const EggVertex self, EggVertexUV vertex_uv)
        
        /**
         * Sets the indicated EggVertexUV on the vertex.  This replaces any UV
         * coordinate pair with the same name already on the vertex, including UV
         * morphs.
         */
        """
        pass

    def sortsLessThan(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        sorts_less_than(EggVertex self, const EggVertex other)
        
        /**
         * An ordering operator to compare two vertices for sorting order.  This
         * imposes an arbitrary ordering useful to identify unique vertices.
         */
        """
        pass

    def sorts_less_than(self, EggVertex_self, const_EggVertex_other): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        sorts_less_than(EggVertex self, const EggVertex other)
        
        /**
         * An ordering operator to compare two vertices for sorting order.  This
         * imposes an arbitrary ordering useful to identify unique vertices.
         */
        """
        pass

    def testGrefIntegrity(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        test_gref_integrity(EggVertex self)
        """
        pass

    def testPrefIntegrity(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        test_pref_integrity(EggVertex self)
        """
        pass

    def test_gref_integrity(self, EggVertex_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        test_gref_integrity(EggVertex self)
        """
        pass

    def test_pref_integrity(self, EggVertex_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        test_pref_integrity(EggVertex self)
        """
        pass

    def transform(self, const_EggVertex_self, const_LMatrix4d_mat): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        transform(const EggVertex self, const LMatrix4d mat)
        
        /**
         * Applies the indicated transformation matrix to the vertex.
         */
        """
        pass

    def upcastToEggAttributes(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        upcast_to_EggAttributes(const EggVertex self)
        
        upcast from EggVertex to EggAttributes
        """
        pass

    def upcastToEggObject(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        upcast_to_EggObject(const EggVertex self)
        
        upcast from EggVertex to EggObject
        """
        pass

    def upcast_to_EggAttributes(self, const_EggVertex_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        upcast_to_EggAttributes(const EggVertex self)
        
        upcast from EggVertex to EggAttributes
        """
        pass

    def upcast_to_EggObject(self, const_EggVertex_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        upcast_to_EggObject(const EggVertex self)
        
        upcast from EggVertex to EggObject
        """
        pass

    def write(self, EggVertex_self, ostream_out, int_indent_level): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        write(EggVertex self, ostream out, int indent_level)
        
        /**
         * Writes the vertex to the indicated output stream in Egg format.
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

    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.egg.EggVertex' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.egg.EggVertex' objects>"
        '__doc__': '/**\n * Any one-, two-, three-, or four-component vertex, possibly with attributes\n * such as a normal.\n */',
        '__eq__': None, # (!) real value is "<slot wrapper '__eq__' of 'panda3d.egg.EggVertex' objects>"
        '__ge__': None, # (!) real value is "<slot wrapper '__ge__' of 'panda3d.egg.EggVertex' objects>"
        '__gt__': None, # (!) real value is "<slot wrapper '__gt__' of 'panda3d.egg.EggVertex' objects>"
        '__hash__': None, # (!) real value is "<slot wrapper '__hash__' of 'panda3d.egg.EggVertex' objects>"
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.egg.EggVertex' objects>"
        '__le__': None, # (!) real value is "<slot wrapper '__le__' of 'panda3d.egg.EggVertex' objects>"
        '__lt__': None, # (!) real value is "<slot wrapper '__lt__' of 'panda3d.egg.EggVertex' objects>"
        '__ne__': None, # (!) real value is "<slot wrapper '__ne__' of 'panda3d.egg.EggVertex' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFDC68CD7D0>'
        '__repr__': None, # (!) real value is "<slot wrapper '__repr__' of 'panda3d.egg.EggVertex' objects>"
        '__str__': None, # (!) real value is "<slot wrapper '__str__' of 'panda3d.egg.EggVertex' objects>"
        'assign': None, # (!) real value is "<method 'assign' of 'panda3d.egg.EggVertex' objects>"
        'clearAux': None, # (!) real value is "<method 'clearAux' of 'panda3d.egg.EggVertex' objects>"
        'clearGrefs': None, # (!) real value is "<method 'clearGrefs' of 'panda3d.egg.EggVertex' objects>"
        'clearUv': None, # (!) real value is "<method 'clearUv' of 'panda3d.egg.EggVertex' objects>"
        'clear_aux': None, # (!) real value is "<method 'clear_aux' of 'panda3d.egg.EggVertex' objects>"
        'clear_grefs': None, # (!) real value is "<method 'clear_grefs' of 'panda3d.egg.EggVertex' objects>"
        'clear_uv': None, # (!) real value is "<method 'clear_uv' of 'panda3d.egg.EggVertex' objects>"
        'compareTo': None, # (!) real value is "<method 'compareTo' of 'panda3d.egg.EggVertex' objects>"
        'compare_to': None, # (!) real value is "<method 'compare_to' of 'panda3d.egg.EggVertex' objects>"
        'copyGrefsFrom': None, # (!) real value is "<method 'copyGrefsFrom' of 'panda3d.egg.EggVertex' objects>"
        'copy_grefs_from': None, # (!) real value is "<method 'copy_grefs_from' of 'panda3d.egg.EggVertex' objects>"
        'getAux': None, # (!) real value is "<method 'getAux' of 'panda3d.egg.EggVertex' objects>"
        'getAuxObj': None, # (!) real value is "<method 'getAuxObj' of 'panda3d.egg.EggVertex' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFDC68CD7D0>)>'
        'getExternalIndex': None, # (!) real value is "<method 'getExternalIndex' of 'panda3d.egg.EggVertex' objects>"
        'getExternalIndex2': None, # (!) real value is "<method 'getExternalIndex2' of 'panda3d.egg.EggVertex' objects>"
        'getIndex': None, # (!) real value is "<method 'getIndex' of 'panda3d.egg.EggVertex' objects>"
        'getNumDimensions': None, # (!) real value is "<method 'getNumDimensions' of 'panda3d.egg.EggVertex' objects>"
        'getNumGlobalCoord': None, # (!) real value is "<method 'getNumGlobalCoord' of 'panda3d.egg.EggVertex' objects>"
        'getNumLocalCoord': None, # (!) real value is "<method 'getNumLocalCoord' of 'panda3d.egg.EggVertex' objects>"
        'getPool': None, # (!) real value is "<method 'getPool' of 'panda3d.egg.EggVertex' objects>"
        'getPos1': None, # (!) real value is "<method 'getPos1' of 'panda3d.egg.EggVertex' objects>"
        'getPos2': None, # (!) real value is "<method 'getPos2' of 'panda3d.egg.EggVertex' objects>"
        'getPos3': None, # (!) real value is "<method 'getPos3' of 'panda3d.egg.EggVertex' objects>"
        'getPos4': None, # (!) real value is "<method 'getPos4' of 'panda3d.egg.EggVertex' objects>"
        'getUv': None, # (!) real value is "<method 'getUv' of 'panda3d.egg.EggVertex' objects>"
        'getUvObj': None, # (!) real value is "<method 'getUvObj' of 'panda3d.egg.EggVertex' objects>"
        'getUvw': None, # (!) real value is "<method 'getUvw' of 'panda3d.egg.EggVertex' objects>"
        'get_aux': None, # (!) real value is "<method 'get_aux' of 'panda3d.egg.EggVertex' objects>"
        'get_aux_obj': None, # (!) real value is "<method 'get_aux_obj' of 'panda3d.egg.EggVertex' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFDC68CD7D0>)>'
        'get_external_index': None, # (!) real value is "<method 'get_external_index' of 'panda3d.egg.EggVertex' objects>"
        'get_external_index2': None, # (!) real value is "<method 'get_external_index2' of 'panda3d.egg.EggVertex' objects>"
        'get_index': None, # (!) real value is "<method 'get_index' of 'panda3d.egg.EggVertex' objects>"
        'get_num_dimensions': None, # (!) real value is "<method 'get_num_dimensions' of 'panda3d.egg.EggVertex' objects>"
        'get_num_global_coord': None, # (!) real value is "<method 'get_num_global_coord' of 'panda3d.egg.EggVertex' objects>"
        'get_num_local_coord': None, # (!) real value is "<method 'get_num_local_coord' of 'panda3d.egg.EggVertex' objects>"
        'get_pool': None, # (!) real value is "<method 'get_pool' of 'panda3d.egg.EggVertex' objects>"
        'get_pos1': None, # (!) real value is "<method 'get_pos1' of 'panda3d.egg.EggVertex' objects>"
        'get_pos2': None, # (!) real value is "<method 'get_pos2' of 'panda3d.egg.EggVertex' objects>"
        'get_pos3': None, # (!) real value is "<method 'get_pos3' of 'panda3d.egg.EggVertex' objects>"
        'get_pos4': None, # (!) real value is "<method 'get_pos4' of 'panda3d.egg.EggVertex' objects>"
        'get_uv': None, # (!) real value is "<method 'get_uv' of 'panda3d.egg.EggVertex' objects>"
        'get_uv_obj': None, # (!) real value is "<method 'get_uv_obj' of 'panda3d.egg.EggVertex' objects>"
        'get_uvw': None, # (!) real value is "<method 'get_uvw' of 'panda3d.egg.EggVertex' objects>"
        'hasAux': None, # (!) real value is "<method 'hasAux' of 'panda3d.egg.EggVertex' objects>"
        'hasGref': None, # (!) real value is "<method 'hasGref' of 'panda3d.egg.EggVertex' objects>"
        'hasPref': None, # (!) real value is "<method 'hasPref' of 'panda3d.egg.EggVertex' objects>"
        'hasUv': None, # (!) real value is "<method 'hasUv' of 'panda3d.egg.EggVertex' objects>"
        'hasUvw': None, # (!) real value is "<method 'hasUvw' of 'panda3d.egg.EggVertex' objects>"
        'has_aux': None, # (!) real value is "<method 'has_aux' of 'panda3d.egg.EggVertex' objects>"
        'has_gref': None, # (!) real value is "<method 'has_gref' of 'panda3d.egg.EggVertex' objects>"
        'has_pref': None, # (!) real value is "<method 'has_pref' of 'panda3d.egg.EggVertex' objects>"
        'has_uv': None, # (!) real value is "<method 'has_uv' of 'panda3d.egg.EggVertex' objects>"
        'has_uvw': None, # (!) real value is "<method 'has_uvw' of 'panda3d.egg.EggVertex' objects>"
        'isForwardReference': None, # (!) real value is "<method 'isForwardReference' of 'panda3d.egg.EggVertex' objects>"
        'is_forward_reference': None, # (!) real value is "<method 'is_forward_reference' of 'panda3d.egg.EggVertex' objects>"
        'makeAverage': None, # (!) real value is '<staticmethod(<built-in method makeAverage of type object at 0x00007FFDC68CD7D0>)>'
        'make_average': None, # (!) real value is '<staticmethod(<built-in method make_average of type object at 0x00007FFDC68CD7D0>)>'
        'modifyAuxObj': None, # (!) real value is "<method 'modifyAuxObj' of 'panda3d.egg.EggVertex' objects>"
        'modifyUvObj': None, # (!) real value is "<method 'modifyUvObj' of 'panda3d.egg.EggVertex' objects>"
        'modify_aux_obj': None, # (!) real value is "<method 'modify_aux_obj' of 'panda3d.egg.EggVertex' objects>"
        'modify_uv_obj': None, # (!) real value is "<method 'modify_uv_obj' of 'panda3d.egg.EggVertex' objects>"
        'output': None, # (!) real value is "<method 'output' of 'panda3d.egg.EggVertex' objects>"
        'setAux': None, # (!) real value is "<method 'setAux' of 'panda3d.egg.EggVertex' objects>"
        'setAuxObj': None, # (!) real value is "<method 'setAuxObj' of 'panda3d.egg.EggVertex' objects>"
        'setExternalIndex': None, # (!) real value is "<method 'setExternalIndex' of 'panda3d.egg.EggVertex' objects>"
        'setExternalIndex2': None, # (!) real value is "<method 'setExternalIndex2' of 'panda3d.egg.EggVertex' objects>"
        'setPos': None, # (!) real value is "<method 'setPos' of 'panda3d.egg.EggVertex' objects>"
        'setPos4': None, # (!) real value is "<method 'setPos4' of 'panda3d.egg.EggVertex' objects>"
        'setUv': None, # (!) real value is "<method 'setUv' of 'panda3d.egg.EggVertex' objects>"
        'setUvObj': None, # (!) real value is "<method 'setUvObj' of 'panda3d.egg.EggVertex' objects>"
        'setUvw': None, # (!) real value is "<method 'setUvw' of 'panda3d.egg.EggVertex' objects>"
        'set_aux': None, # (!) real value is "<method 'set_aux' of 'panda3d.egg.EggVertex' objects>"
        'set_aux_obj': None, # (!) real value is "<method 'set_aux_obj' of 'panda3d.egg.EggVertex' objects>"
        'set_external_index': None, # (!) real value is "<method 'set_external_index' of 'panda3d.egg.EggVertex' objects>"
        'set_external_index2': None, # (!) real value is "<method 'set_external_index2' of 'panda3d.egg.EggVertex' objects>"
        'set_pos': None, # (!) real value is "<method 'set_pos' of 'panda3d.egg.EggVertex' objects>"
        'set_pos4': None, # (!) real value is "<method 'set_pos4' of 'panda3d.egg.EggVertex' objects>"
        'set_uv': None, # (!) real value is "<method 'set_uv' of 'panda3d.egg.EggVertex' objects>"
        'set_uv_obj': None, # (!) real value is "<method 'set_uv_obj' of 'panda3d.egg.EggVertex' objects>"
        'set_uvw': None, # (!) real value is "<method 'set_uvw' of 'panda3d.egg.EggVertex' objects>"
        'sortsLessThan': None, # (!) real value is "<method 'sortsLessThan' of 'panda3d.egg.EggVertex' objects>"
        'sorts_less_than': None, # (!) real value is "<method 'sorts_less_than' of 'panda3d.egg.EggVertex' objects>"
        'testGrefIntegrity': None, # (!) real value is "<method 'testGrefIntegrity' of 'panda3d.egg.EggVertex' objects>"
        'testPrefIntegrity': None, # (!) real value is "<method 'testPrefIntegrity' of 'panda3d.egg.EggVertex' objects>"
        'test_gref_integrity': None, # (!) real value is "<method 'test_gref_integrity' of 'panda3d.egg.EggVertex' objects>"
        'test_pref_integrity': None, # (!) real value is "<method 'test_pref_integrity' of 'panda3d.egg.EggVertex' objects>"
        'transform': None, # (!) real value is "<method 'transform' of 'panda3d.egg.EggVertex' objects>"
        'upcastToEggAttributes': None, # (!) real value is "<method 'upcastToEggAttributes' of 'panda3d.egg.EggVertex' objects>"
        'upcastToEggObject': None, # (!) real value is "<method 'upcastToEggObject' of 'panda3d.egg.EggVertex' objects>"
        'upcast_to_EggAttributes': None, # (!) real value is "<method 'upcast_to_EggAttributes' of 'panda3d.egg.EggVertex' objects>"
        'upcast_to_EggObject': None, # (!) real value is "<method 'upcast_to_EggObject' of 'panda3d.egg.EggVertex' objects>"
        'write': None, # (!) real value is "<method 'write' of 'panda3d.egg.EggVertex' objects>"
    }


