# encoding: utf-8
# module panda3d.egg
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\egg.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import panda3d.core as __panda3d_core


from .EggNode import EggNode

class EggGroupNode(EggNode):
    """
    /**
     * A base class for nodes in the hierarchy that are not leaf nodes.  (See also
     * EggGroup, which is specifically the "<Group>" node in egg.)
     *
     * An EggGroupNode is an STL-style container of pointers to EggNodes, like a
     * vector.  Functions push_back()/pop_back() and insert()/erase() are provided
     * to manipulate the list.  The list may also be operated on (read-only) via
     * iterators and begin()/end().
     */
    """
    def addChild(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_child(const EggGroupNode self, EggNode node)
        
        /**
         * Adds the indicated child to the group and returns it.  If the child node is
         * already a child of some other node, removes it first.
         */
        """
        pass

    def add_child(self, const_EggGroupNode_self, EggNode_node): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_child(const EggGroupNode self, EggNode node)
        
        /**
         * Adds the indicated child to the group and returns it.  If the child node is
         * already a child of some other node, removes it first.
         */
        """
        pass

    def applyFirstAttribute(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        apply_first_attribute(const EggGroupNode self, bool recurse)
        
        /**
         * Sets the first vertex of the triangle (or each component) to the primitive
         * normal and/or color, if the primitive is flat-shaded.  This reflects the
         * DirectX convention of storing flat-shaded properties on the first vertex,
         * although it is not usually a convention in Egg.
         *
         * This may create redundant vertices in the vertex pool, so it may be a good
         * idea to follow this up with remove_unused_vertices().
         */
        """
        pass

    def applyLastAttribute(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        apply_last_attribute(const EggGroupNode self, bool recurse)
        
        /**
         * Sets the last vertex of the triangle (or each component) to the primitive
         * normal and/or color, if the primitive is flat-shaded.  This reflects the
         * OpenGL convention of storing flat-shaded properties on the last vertex,
         * although it is not usually a convention in Egg.
         *
         * This may create redundant vertices in the vertex pool, so it may be a good
         * idea to follow this up with remove_unused_vertices().
         */
        """
        pass

    def apply_first_attribute(self, const_EggGroupNode_self, bool_recurse): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        apply_first_attribute(const EggGroupNode self, bool recurse)
        
        /**
         * Sets the first vertex of the triangle (or each component) to the primitive
         * normal and/or color, if the primitive is flat-shaded.  This reflects the
         * DirectX convention of storing flat-shaded properties on the first vertex,
         * although it is not usually a convention in Egg.
         *
         * This may create redundant vertices in the vertex pool, so it may be a good
         * idea to follow this up with remove_unused_vertices().
         */
        """
        pass

    def apply_last_attribute(self, const_EggGroupNode_self, bool_recurse): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        apply_last_attribute(const EggGroupNode self, bool recurse)
        
        /**
         * Sets the last vertex of the triangle (or each component) to the primitive
         * normal and/or color, if the primitive is flat-shaded.  This reflects the
         * OpenGL convention of storing flat-shaded properties on the last vertex,
         * although it is not usually a convention in Egg.
         *
         * This may create redundant vertices in the vertex pool, so it may be a good
         * idea to follow this up with remove_unused_vertices().
         */
        """
        pass

    def assign(self, const_EggGroupNode_self, const_EggGroupNode_copy): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        assign(const EggGroupNode self, const EggGroupNode copy)
        
        /**
         *
         */
        """
        pass

    def clear(self, const_EggGroupNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear(const EggGroupNode self)
        
        /**
         *
         */
        """
        pass

    def clearConnectedShading(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_connected_shading(const EggGroupNode self)
        
        /**
         * Resets the connected_shading information on all primitives at this node and
         * below, so that it may be accurately rederived by the next call to
         * get_connected_shading().
         *
         * It may be a good idea to call remove_unused_vertices() as well, to
         * establish the correct connectivity between common vertices.
         */
        """
        pass

    def clear_connected_shading(self, const_EggGroupNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_connected_shading(const EggGroupNode self)
        
        /**
         * Resets the connected_shading information on all primitives at this node and
         * below, so that it may be accurately rederived by the next call to
         * get_connected_shading().
         *
         * It may be a good idea to call remove_unused_vertices() as well, to
         * establish the correct connectivity between common vertices.
         */
        """
        pass

    def empty(self, EggGroupNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        empty(EggGroupNode self)
        
        /**
         *
         */
        """
        pass

    def findChild(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        find_child(EggGroupNode self, str name)
        
        /**
         * Returns the child of this node whose name is the indicated string, or NULL
         * if there is no child of this node by that name.  Does not search
         * recursively.
         */
        """
        pass

    def find_child(self, EggGroupNode_self, str_name): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        find_child(EggGroupNode self, str name)
        
        /**
         * Returns the child of this node whose name is the indicated string, or NULL
         * if there is no child of this node by that name.  Does not search
         * recursively.
         */
        """
        pass

    def forceFilenames(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        force_filenames(const EggGroupNode self, const Filename directory)
        
        /**
         * Similar to resolve_filenames, but each non-absolute filename encountered is
         * arbitrarily taken to be in the indicated directory, whether or not the so-
         * named filename exists.
         */
        """
        pass

    def force_filenames(self, const_EggGroupNode_self, const_Filename_directory): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        force_filenames(const EggGroupNode self, const Filename directory)
        
        /**
         * Similar to resolve_filenames, but each non-absolute filename encountered is
         * arbitrarily taken to be in the indicated directory, whether or not the so-
         * named filename exists.
         */
        """
        pass

    def getChildren(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_children(EggGroupNode self)
        """
        pass

    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getConnectedShading(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_connected_shading(const EggGroupNode self)
        
        /**
         * Queries the connected_shading information on all primitives at this node
         * and below, to ensure that it has been completely filled in before we start
         * mucking around with vertices.
         */
        """
        pass

    def getFirstChild(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_first_child(const EggGroupNode self)
        
        // This is an alternate way to traverse the list of children.  It is mainly
        // provided for scripting code, which can't use the iterators defined above
        // (they don't export through interrogate very well). These are, of course,
        // non-thread-safe.
        
        /**
         * Returns the first child in the group's list of children, or NULL if the
         * list of children is empty.  Can be used with get_next_child() to return the
         * complete list of children without using the iterator class; however, this
         * is non-thread-safe, and so is not recommended except for languages other
         * than C++ which cannot use the iterators.
         */
        """
        pass

    def getNextChild(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_next_child(const EggGroupNode self)
        
        /**
         * Returns the next child in the group's list of children since the last call
         * to get_first_child() or get_next_child(), or NULL if the last child has
         * been returned.  Can be used with get_first_child() to return the complete
         * list of children without using the iterator class; however, this is non-
         * thread-safe, and so is not recommended except for languages other than C++
         * which cannot use the iterators.
         *
         * It is an error to call this without previously calling get_first_child().
         */
        """
        pass

    def get_children(self, EggGroupNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_children(EggGroupNode self)
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_connected_shading(self, const_EggGroupNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_connected_shading(const EggGroupNode self)
        
        /**
         * Queries the connected_shading information on all primitives at this node
         * and below, to ensure that it has been completely filled in before we start
         * mucking around with vertices.
         */
        """
        pass

    def get_first_child(self, const_EggGroupNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_first_child(const EggGroupNode self)
        
        // This is an alternate way to traverse the list of children.  It is mainly
        // provided for scripting code, which can't use the iterators defined above
        // (they don't export through interrogate very well). These are, of course,
        // non-thread-safe.
        
        /**
         * Returns the first child in the group's list of children, or NULL if the
         * list of children is empty.  Can be used with get_next_child() to return the
         * complete list of children without using the iterator class; however, this
         * is non-thread-safe, and so is not recommended except for languages other
         * than C++ which cannot use the iterators.
         */
        """
        pass

    def get_next_child(self, const_EggGroupNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_next_child(const EggGroupNode self)
        
        /**
         * Returns the next child in the group's list of children since the last call
         * to get_first_child() or get_next_child(), or NULL if the last child has
         * been returned.  Can be used with get_first_child() to return the complete
         * list of children without using the iterator class; however, this is non-
         * thread-safe, and so is not recommended except for languages other than C++
         * which cannot use the iterators.
         *
         * It is an error to call this without previously calling get_first_child().
         */
        """
        pass

    def hasAbsolutePathnames(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_absolute_pathnames(EggGroupNode self)
        
        /**
         * Returns true if any nodes at this level and below include a reference to a
         * file via an absolute pathname, or false if all references are relative.
         */
        """
        pass

    def hasNormals(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_normals(EggGroupNode self)
        
        /**
         * Returns true if any of the primitives (e.g.  polygons) defined within this
         * group or below have either face or vertex normals defined, false otherwise.
         */
        """
        pass

    def hasPrimitives(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_primitives(EggGroupNode self)
        
        /**
         * Returns true if there are any primitives (e.g.  polygons) defined within
         * this group or below, false otherwise.
         */
        """
        pass

    def has_absolute_pathnames(self, EggGroupNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_absolute_pathnames(EggGroupNode self)
        
        /**
         * Returns true if any nodes at this level and below include a reference to a
         * file via an absolute pathname, or false if all references are relative.
         */
        """
        pass

    def has_normals(self, EggGroupNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_normals(EggGroupNode self)
        
        /**
         * Returns true if any of the primitives (e.g.  polygons) defined within this
         * group or below have either face or vertex normals defined, false otherwise.
         */
        """
        pass

    def has_primitives(self, EggGroupNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_primitives(EggGroupNode self)
        
        /**
         * Returns true if there are any primitives (e.g.  polygons) defined within
         * this group or below, false otherwise.
         */
        """
        pass

    def isRight(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_right(const LVector2d v1, const LVector2d v2)
        
        /**
         * Returns true if the 2-d v1 is to the right of v2.
         */
        """
        pass

    def is_right(self, const_LVector2d_v1, const_LVector2d_v2): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_right(const LVector2d v1, const LVector2d v2)
        
        /**
         * Returns true if the 2-d v1 is to the right of v2.
         */
        """
        pass

    def jointHasPrimitives(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        joint_has_primitives(EggGroupNode self)
        
        /**
         * Returns true if there are any primitives (e.g.  polygons) defined within
         * this group or below, but the search does not include nested joints.
         */
        """
        pass

    def joint_has_primitives(self, EggGroupNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        joint_has_primitives(EggGroupNode self)
        
        /**
         * Returns true if there are any primitives (e.g.  polygons) defined within
         * this group or below, but the search does not include nested joints.
         */
        """
        pass

    def makePointPrimitives(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        make_point_primitives(const EggGroupNode self)
        
        /**
         * Creates PointLight primitives to reference any otherwise unreferences
         * vertices discovered in this group or below.
         */
        """
        pass

    def make_point_primitives(self, const_EggGroupNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        make_point_primitives(const EggGroupNode self)
        
        /**
         * Creates PointLight primitives to reference any otherwise unreferences
         * vertices discovered in this group or below.
         */
        """
        pass

    def meshTriangles(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        mesh_triangles(const EggGroupNode self, int flags)
        
        /**
         * Combine triangles together into triangle strips, at this group and below.
         */
        """
        pass

    def mesh_triangles(self, const_EggGroupNode_self, int_flags): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        mesh_triangles(const EggGroupNode self, int flags)
        
        /**
         * Combine triangles together into triangle strips, at this group and below.
         */
        """
        pass

    def postApplyFlatAttribute(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        post_apply_flat_attribute(const EggGroupNode self, bool recurse)
        
        /**
         * Intended as a followup to apply_last_attribute(), this also sets an
         * attribute on the first vertices of the primitive, if they don't already
         * have an attribute set, just so they end up with *something*.
         */
        """
        pass

    def post_apply_flat_attribute(self, const_EggGroupNode_self, bool_recurse): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        post_apply_flat_attribute(const EggGroupNode self, bool recurse)
        
        /**
         * Intended as a followup to apply_last_attribute(), this also sets an
         * attribute on the first vertices of the primitive, if they don't already
         * have an attribute set, just so they end up with *something*.
         */
        """
        pass

    def recomputePolygonNormals(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        recompute_polygon_normals(const EggGroupNode self, int cs)
        
        /**
         * Recomputes all the polygon normals for polygon geometry at this group node
         * and below so that they accurately reflect the vertex positions.  Normals
         * are removed from the vertices and defined only on polygons, giving the
         * geometry a faceted appearance.
         *
         * This function also removes degenerate polygons that do not have enough
         * vertices to define a normal.  It does not affect normals for other kinds of
         * primitives like Nurbs or Points.
         *
         * This function does not remove or adjust vertices in the vertex pool; it
         * only adds new vertices with the normals removed.  Thus, it is a good idea
         * to call remove_unused_vertices() after calling this.
         */
        """
        pass

    def recomputeTangentBinormal(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        recompute_tangent_binormal(const EggGroupNode self, const GlobPattern uv_name)
        
        /**
         * This function recomputes the tangent and binormal for the named texture
         * coordinate set for all vertices at this level and below.  Use the empty
         * string for the default texture coordinate set.
         *
         * It is necessary for each vertex to already have a normal (or at least a
         * polygon normal), as well as a texture coordinate in the named texture
         * coordinate set, before calling this function.  You might precede this with
         * recompute_vertex_normals() to ensure that the normals exist.
         *
         * Like recompute_vertex_normals(), this function does not remove or adjust
         * vertices in the vertex pool; it only adds new vertices with the new
         * tangents and binormals computed.  Thus, it is a good idea to call
         * remove_unused_vertices() after calling this.
         */
        
        /**
         * This function recomputes the tangent and binormal for the named texture
         * coordinate sets.  Returns true if anything was done.
         */
        """
        pass

    def recomputeTangentBinormalAuto(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        recompute_tangent_binormal_auto(const EggGroupNode self)
        
        /**
         * This function recomputes the tangent and binormal for any texture
         * coordinate set that affects a normal map.  Returns true if anything was
         * done.
         */
        """
        pass

    def recomputeVertexNormals(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        recompute_vertex_normals(const EggGroupNode self, double threshold, int cs)
        
        /**
         * Recomputes all the vertex normals for polygon geometry at this group node
         * and below so that they accurately reflect the vertex positions.  A shared
         * edge between two polygons (even in different groups) is considered smooth
         * if the angle between the two edges is less than threshold degrees.
         *
         * This function also removes degenerate polygons that do not have enough
         * vertices to define a normal.  It does not affect normals for other kinds of
         * primitives like Nurbs or Points.
         *
         * This function does not remove or adjust vertices in the vertex pool; it
         * only adds new vertices with the correct normals.  Thus, it is a good idea
         * to call remove_unused_vertices() after calling this.
         */
        """
        pass

    def recompute_polygon_normals(self, const_EggGroupNode_self, int_cs): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        recompute_polygon_normals(const EggGroupNode self, int cs)
        
        /**
         * Recomputes all the polygon normals for polygon geometry at this group node
         * and below so that they accurately reflect the vertex positions.  Normals
         * are removed from the vertices and defined only on polygons, giving the
         * geometry a faceted appearance.
         *
         * This function also removes degenerate polygons that do not have enough
         * vertices to define a normal.  It does not affect normals for other kinds of
         * primitives like Nurbs or Points.
         *
         * This function does not remove or adjust vertices in the vertex pool; it
         * only adds new vertices with the normals removed.  Thus, it is a good idea
         * to call remove_unused_vertices() after calling this.
         */
        """
        pass

    def recompute_tangent_binormal(self, const_EggGroupNode_self, const_GlobPattern_uv_name): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        recompute_tangent_binormal(const EggGroupNode self, const GlobPattern uv_name)
        
        /**
         * This function recomputes the tangent and binormal for the named texture
         * coordinate set for all vertices at this level and below.  Use the empty
         * string for the default texture coordinate set.
         *
         * It is necessary for each vertex to already have a normal (or at least a
         * polygon normal), as well as a texture coordinate in the named texture
         * coordinate set, before calling this function.  You might precede this with
         * recompute_vertex_normals() to ensure that the normals exist.
         *
         * Like recompute_vertex_normals(), this function does not remove or adjust
         * vertices in the vertex pool; it only adds new vertices with the new
         * tangents and binormals computed.  Thus, it is a good idea to call
         * remove_unused_vertices() after calling this.
         */
        
        /**
         * This function recomputes the tangent and binormal for the named texture
         * coordinate sets.  Returns true if anything was done.
         */
        """
        pass

    def recompute_tangent_binormal_auto(self, const_EggGroupNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        recompute_tangent_binormal_auto(const EggGroupNode self)
        
        /**
         * This function recomputes the tangent and binormal for any texture
         * coordinate set that affects a normal map.  Returns true if anything was
         * done.
         */
        """
        pass

    def recompute_vertex_normals(self, const_EggGroupNode_self, double_threshold, int_cs): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        recompute_vertex_normals(const EggGroupNode self, double threshold, int cs)
        
        /**
         * Recomputes all the vertex normals for polygon geometry at this group node
         * and below so that they accurately reflect the vertex positions.  A shared
         * edge between two polygons (even in different groups) is considered smooth
         * if the angle between the two edges is less than threshold degrees.
         *
         * This function also removes degenerate polygons that do not have enough
         * vertices to define a normal.  It does not affect normals for other kinds of
         * primitives like Nurbs or Points.
         *
         * This function does not remove or adjust vertices in the vertex pool; it
         * only adds new vertices with the correct normals.  Thus, it is a good idea
         * to call remove_unused_vertices() after calling this.
         */
        """
        pass

    def removeChild(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        remove_child(const EggGroupNode self, EggNode node)
        
        /**
         * Removes the indicated child node from the group and returns it.  If the
         * child was not already in the group, does nothing and returns NULL.
         */
        """
        pass

    def removeInvalidPrimitives(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        remove_invalid_primitives(const EggGroupNode self, bool recurse)
        
        /**
         * Removes primitives at this level and below which appear to be degenerate;
         * e.g.  polygons with fewer than 3 vertices, etc.  Returns the number of
         * primitives removed.
         */
        """
        pass

    def removeUnusedVertices(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        remove_unused_vertices(const EggGroupNode self, bool recurse)
        
        /**
         * Removes all vertices from VertexPools within this group or below that are
         * not referenced by at least one primitive.  Also collapses together
         * equivalent vertices, and renumbers all vertices after the operation so
         * their indices are consecutive, beginning at zero.  Returns the total number
         * of vertices removed.
         *
         * Note that this operates on the VertexPools within this group level, without
         * respect to primitives that reference these vertices (unlike other functions
         * like strip_normals()).  It is therefore most useful to call this on the
         * EggData root, rather than on a subgroup within the hierarchy, since a
         * VertexPool may appear anywhere in the hierarchy.
         */
        """
        pass

    def remove_child(self, const_EggGroupNode_self, EggNode_node): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        remove_child(const EggGroupNode self, EggNode node)
        
        /**
         * Removes the indicated child node from the group and returns it.  If the
         * child was not already in the group, does nothing and returns NULL.
         */
        """
        pass

    def remove_invalid_primitives(self, const_EggGroupNode_self, bool_recurse): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        remove_invalid_primitives(const EggGroupNode self, bool recurse)
        
        /**
         * Removes primitives at this level and below which appear to be degenerate;
         * e.g.  polygons with fewer than 3 vertices, etc.  Returns the number of
         * primitives removed.
         */
        """
        pass

    def remove_unused_vertices(self, const_EggGroupNode_self, bool_recurse): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        remove_unused_vertices(const EggGroupNode self, bool recurse)
        
        /**
         * Removes all vertices from VertexPools within this group or below that are
         * not referenced by at least one primitive.  Also collapses together
         * equivalent vertices, and renumbers all vertices after the operation so
         * their indices are consecutive, beginning at zero.  Returns the total number
         * of vertices removed.
         *
         * Note that this operates on the VertexPools within this group level, without
         * respect to primitives that reference these vertices (unlike other functions
         * like strip_normals()).  It is therefore most useful to call this on the
         * EggData root, rather than on a subgroup within the hierarchy, since a
         * VertexPool may appear anywhere in the hierarchy.
         */
        """
        pass

    def resolveFilenames(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        resolve_filenames(const EggGroupNode self, const DSearchPath searchpath)
        
        /**
         * Walks the tree and attempts to resolve any filenames encountered.  This
         * looks up filenames along the specified search path; it does not
         * automatically search the model_path for missing files.
         */
        """
        pass

    def resolve_filenames(self, const_EggGroupNode_self, const_DSearchPath_searchpath): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        resolve_filenames(const EggGroupNode self, const DSearchPath searchpath)
        
        /**
         * Walks the tree and attempts to resolve any filenames encountered.  This
         * looks up filenames along the specified search path; it does not
         * automatically search the model_path for missing files.
         */
        """
        pass

    def reverseVertexOrdering(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        reverse_vertex_ordering(const EggGroupNode self)
        
        /**
         * Reverses the vertex ordering of all polygons defined at this node and
         * below.  Does not change the surface normals, if any.
         */
        """
        pass

    def reverse_vertex_ordering(self, const_EggGroupNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        reverse_vertex_ordering(const EggGroupNode self)
        
        /**
         * Reverses the vertex ordering of all polygons defined at this node and
         * below.  Does not change the surface normals, if any.
         */
        """
        pass

    def size(self, EggGroupNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        size(EggGroupNode self)
        
        /**
         *
         */
        """
        pass

    def stealChildren(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        steal_children(const EggGroupNode self, EggGroupNode other)
        
        /**
         * Moves all the children from the other node to this one.  This is especially
         * useful because the group node copy assignment operator does not copy
         * children.
         */
        """
        pass

    def steal_children(self, const_EggGroupNode_self, EggGroupNode_other): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        steal_children(const EggGroupNode self, EggGroupNode other)
        
        /**
         * Moves all the children from the other node to this one.  This is especially
         * useful because the group node copy assignment operator does not copy
         * children.
         */
        """
        pass

    def stripNormals(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        strip_normals(const EggGroupNode self)
        
        /**
         * Removes all normals from primitives, and the vertices they reference, at
         * this node and below.
         *
         * This function does not remove or adjust vertices in the vertex pool; it
         * only adds new vertices with the normal removed.  Thus, it is a good idea to
         * call remove_unused_vertices() after calling this.
         */
        """
        pass

    def strip_normals(self, const_EggGroupNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        strip_normals(const EggGroupNode self)
        
        /**
         * Removes all normals from primitives, and the vertices they reference, at
         * this node and below.
         *
         * This function does not remove or adjust vertices in the vertex pool; it
         * only adds new vertices with the normal removed.  Thus, it is a good idea to
         * call remove_unused_vertices() after calling this.
         */
        """
        pass

    def triangulatePolygons(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        triangulate_polygons(const EggGroupNode self, int flags)
        
        /**
         * Replace all higher-order polygons at this point in the scene graph and
         * below with triangles.  Returns the total number of new triangles produced,
         * less degenerate polygons removed.
         *
         * If flags contains T_polygon and T_convex, both concave and convex polygons
         * will be subdivided into triangles; with only T_polygon, only concave
         * polygons will be subdivided, and convex polygons will be largely unchanged.
         */
        """
        pass

    def triangulate_polygons(self, const_EggGroupNode_self, int_flags): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        triangulate_polygons(const EggGroupNode self, int flags)
        
        /**
         * Replace all higher-order polygons at this point in the scene graph and
         * below with triangles.  Returns the total number of new triangles produced,
         * less degenerate polygons removed.
         *
         * If flags contains T_polygon and T_convex, both concave and convex polygons
         * will be subdivided into triangles; with only T_polygon, only concave
         * polygons will be subdivided, and convex polygons will be largely unchanged.
         */
        """
        pass

    def unifyAttributes(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        unify_attributes(const EggGroupNode self, bool use_connected_shading, bool allow_per_primitive, bool recurse)
        
        /**
         * Applies per-vertex normal and color to all vertices, if they are in fact
         * per-vertex (and different for each vertex), or moves them to the primitive
         * if they are all the same.
         *
         * After this call, either the primitive will have normals or its vertices
         * will, but not both.  Ditto for colors.
         *
         * If use_connected_shading is true, each polygon is considered in conjunction
         * with all connected polygons; otherwise, each polygon is considered
         * individually.
         *
         * If allow_per_primitive is false, S_per_face or S_overall will treated like
         * S_per_vertex: normals and colors will always be assigned to the vertices.
         * In this case, there will never be per-primitive colors or normals after
         * this call returns.  On the other hand, if allow_per_primitive is true, then
         * S_per_face means that normals and colors should be assigned to the
         * primitives, and removed from the vertices, as described above.
         *
         * This may create redundant vertices in the vertex pool, so it may be a good
         * idea to follow this up with remove_unused_vertices().
         */
        """
        pass

    def unify_attributes(self, const_EggGroupNode_self, bool_use_connected_shading, bool_allow_per_primitive, bool_recurse): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        unify_attributes(const EggGroupNode self, bool use_connected_shading, bool allow_per_primitive, bool recurse)
        
        /**
         * Applies per-vertex normal and color to all vertices, if they are in fact
         * per-vertex (and different for each vertex), or moves them to the primitive
         * if they are all the same.
         *
         * After this call, either the primitive will have normals or its vertices
         * will, but not both.  Ditto for colors.
         *
         * If use_connected_shading is true, each polygon is considered in conjunction
         * with all connected polygons; otherwise, each polygon is considered
         * individually.
         *
         * If allow_per_primitive is false, S_per_face or S_overall will treated like
         * S_per_vertex: normals and colors will always be assigned to the vertices.
         * In this case, there will never be per-primitive colors or normals after
         * this call returns.  On the other hand, if allow_per_primitive is true, then
         * S_per_face means that normals and colors should be assigned to the
         * primitives, and removed from the vertices, as described above.
         *
         * This may create redundant vertices in the vertex pool, so it may be a good
         * idea to follow this up with remove_unused_vertices().
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

    children = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        'TComposite': 4,
        'TConvex': 2,
        'TFlatShaded': 16,
        'TPolygon': 1,
        'TRecurse': 8,
        'T_composite': 4,
        'T_convex': 2,
        'T_flat_shaded': 16,
        'T_polygon': 1,
        'T_recurse': 8,
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.egg.EggGroupNode' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.egg.EggGroupNode' objects>"
        '__doc__': '/**\n * A base class for nodes in the hierarchy that are not leaf nodes.  (See also\n * EggGroup, which is specifically the "<Group>" node in egg.)\n *\n * An EggGroupNode is an STL-style container of pointers to EggNodes, like a\n * vector.  Functions push_back()/pop_back() and insert()/erase() are provided\n * to manipulate the list.  The list may also be operated on (read-only) via\n * iterators and begin()/end().\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.egg.EggGroupNode' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFDC68CCCF0>'
        'addChild': None, # (!) real value is "<method 'addChild' of 'panda3d.egg.EggGroupNode' objects>"
        'add_child': None, # (!) real value is "<method 'add_child' of 'panda3d.egg.EggGroupNode' objects>"
        'applyFirstAttribute': None, # (!) real value is "<method 'applyFirstAttribute' of 'panda3d.egg.EggGroupNode' objects>"
        'applyLastAttribute': None, # (!) real value is "<method 'applyLastAttribute' of 'panda3d.egg.EggGroupNode' objects>"
        'apply_first_attribute': None, # (!) real value is "<method 'apply_first_attribute' of 'panda3d.egg.EggGroupNode' objects>"
        'apply_last_attribute': None, # (!) real value is "<method 'apply_last_attribute' of 'panda3d.egg.EggGroupNode' objects>"
        'assign': None, # (!) real value is "<method 'assign' of 'panda3d.egg.EggGroupNode' objects>"
        'children': None, # (!) real value is "<attribute 'children' of 'panda3d.egg.EggGroupNode' objects>"
        'clear': None, # (!) real value is "<method 'clear' of 'panda3d.egg.EggGroupNode' objects>"
        'clearConnectedShading': None, # (!) real value is "<method 'clearConnectedShading' of 'panda3d.egg.EggGroupNode' objects>"
        'clear_connected_shading': None, # (!) real value is "<method 'clear_connected_shading' of 'panda3d.egg.EggGroupNode' objects>"
        'empty': None, # (!) real value is "<method 'empty' of 'panda3d.egg.EggGroupNode' objects>"
        'findChild': None, # (!) real value is "<method 'findChild' of 'panda3d.egg.EggGroupNode' objects>"
        'find_child': None, # (!) real value is "<method 'find_child' of 'panda3d.egg.EggGroupNode' objects>"
        'forceFilenames': None, # (!) real value is "<method 'forceFilenames' of 'panda3d.egg.EggGroupNode' objects>"
        'force_filenames': None, # (!) real value is "<method 'force_filenames' of 'panda3d.egg.EggGroupNode' objects>"
        'getChildren': None, # (!) real value is "<method 'getChildren' of 'panda3d.egg.EggGroupNode' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFDC68CCCF0>)>'
        'getConnectedShading': None, # (!) real value is "<method 'getConnectedShading' of 'panda3d.egg.EggGroupNode' objects>"
        'getFirstChild': None, # (!) real value is "<method 'getFirstChild' of 'panda3d.egg.EggGroupNode' objects>"
        'getNextChild': None, # (!) real value is "<method 'getNextChild' of 'panda3d.egg.EggGroupNode' objects>"
        'get_children': None, # (!) real value is "<method 'get_children' of 'panda3d.egg.EggGroupNode' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFDC68CCCF0>)>'
        'get_connected_shading': None, # (!) real value is "<method 'get_connected_shading' of 'panda3d.egg.EggGroupNode' objects>"
        'get_first_child': None, # (!) real value is "<method 'get_first_child' of 'panda3d.egg.EggGroupNode' objects>"
        'get_next_child': None, # (!) real value is "<method 'get_next_child' of 'panda3d.egg.EggGroupNode' objects>"
        'hasAbsolutePathnames': None, # (!) real value is "<method 'hasAbsolutePathnames' of 'panda3d.egg.EggGroupNode' objects>"
        'hasNormals': None, # (!) real value is "<method 'hasNormals' of 'panda3d.egg.EggGroupNode' objects>"
        'hasPrimitives': None, # (!) real value is "<method 'hasPrimitives' of 'panda3d.egg.EggGroupNode' objects>"
        'has_absolute_pathnames': None, # (!) real value is "<method 'has_absolute_pathnames' of 'panda3d.egg.EggGroupNode' objects>"
        'has_normals': None, # (!) real value is "<method 'has_normals' of 'panda3d.egg.EggGroupNode' objects>"
        'has_primitives': None, # (!) real value is "<method 'has_primitives' of 'panda3d.egg.EggGroupNode' objects>"
        'isRight': None, # (!) real value is '<staticmethod(<built-in method isRight of type object at 0x00007FFDC68CCCF0>)>'
        'is_right': None, # (!) real value is '<staticmethod(<built-in method is_right of type object at 0x00007FFDC68CCCF0>)>'
        'jointHasPrimitives': None, # (!) real value is "<method 'jointHasPrimitives' of 'panda3d.egg.EggGroupNode' objects>"
        'joint_has_primitives': None, # (!) real value is "<method 'joint_has_primitives' of 'panda3d.egg.EggGroupNode' objects>"
        'makePointPrimitives': None, # (!) real value is "<method 'makePointPrimitives' of 'panda3d.egg.EggGroupNode' objects>"
        'make_point_primitives': None, # (!) real value is "<method 'make_point_primitives' of 'panda3d.egg.EggGroupNode' objects>"
        'meshTriangles': None, # (!) real value is "<method 'meshTriangles' of 'panda3d.egg.EggGroupNode' objects>"
        'mesh_triangles': None, # (!) real value is "<method 'mesh_triangles' of 'panda3d.egg.EggGroupNode' objects>"
        'postApplyFlatAttribute': None, # (!) real value is "<method 'postApplyFlatAttribute' of 'panda3d.egg.EggGroupNode' objects>"
        'post_apply_flat_attribute': None, # (!) real value is "<method 'post_apply_flat_attribute' of 'panda3d.egg.EggGroupNode' objects>"
        'recomputePolygonNormals': None, # (!) real value is "<method 'recomputePolygonNormals' of 'panda3d.egg.EggGroupNode' objects>"
        'recomputeTangentBinormal': None, # (!) real value is "<method 'recomputeTangentBinormal' of 'panda3d.egg.EggGroupNode' objects>"
        'recomputeTangentBinormalAuto': None, # (!) real value is "<method 'recomputeTangentBinormalAuto' of 'panda3d.egg.EggGroupNode' objects>"
        'recomputeVertexNormals': None, # (!) real value is "<method 'recomputeVertexNormals' of 'panda3d.egg.EggGroupNode' objects>"
        'recompute_polygon_normals': None, # (!) real value is "<method 'recompute_polygon_normals' of 'panda3d.egg.EggGroupNode' objects>"
        'recompute_tangent_binormal': None, # (!) real value is "<method 'recompute_tangent_binormal' of 'panda3d.egg.EggGroupNode' objects>"
        'recompute_tangent_binormal_auto': None, # (!) real value is "<method 'recompute_tangent_binormal_auto' of 'panda3d.egg.EggGroupNode' objects>"
        'recompute_vertex_normals': None, # (!) real value is "<method 'recompute_vertex_normals' of 'panda3d.egg.EggGroupNode' objects>"
        'removeChild': None, # (!) real value is "<method 'removeChild' of 'panda3d.egg.EggGroupNode' objects>"
        'removeInvalidPrimitives': None, # (!) real value is "<method 'removeInvalidPrimitives' of 'panda3d.egg.EggGroupNode' objects>"
        'removeUnusedVertices': None, # (!) real value is "<method 'removeUnusedVertices' of 'panda3d.egg.EggGroupNode' objects>"
        'remove_child': None, # (!) real value is "<method 'remove_child' of 'panda3d.egg.EggGroupNode' objects>"
        'remove_invalid_primitives': None, # (!) real value is "<method 'remove_invalid_primitives' of 'panda3d.egg.EggGroupNode' objects>"
        'remove_unused_vertices': None, # (!) real value is "<method 'remove_unused_vertices' of 'panda3d.egg.EggGroupNode' objects>"
        'resolveFilenames': None, # (!) real value is "<method 'resolveFilenames' of 'panda3d.egg.EggGroupNode' objects>"
        'resolve_filenames': None, # (!) real value is "<method 'resolve_filenames' of 'panda3d.egg.EggGroupNode' objects>"
        'reverseVertexOrdering': None, # (!) real value is "<method 'reverseVertexOrdering' of 'panda3d.egg.EggGroupNode' objects>"
        'reverse_vertex_ordering': None, # (!) real value is "<method 'reverse_vertex_ordering' of 'panda3d.egg.EggGroupNode' objects>"
        'size': None, # (!) real value is "<method 'size' of 'panda3d.egg.EggGroupNode' objects>"
        'stealChildren': None, # (!) real value is "<method 'stealChildren' of 'panda3d.egg.EggGroupNode' objects>"
        'steal_children': None, # (!) real value is "<method 'steal_children' of 'panda3d.egg.EggGroupNode' objects>"
        'stripNormals': None, # (!) real value is "<method 'stripNormals' of 'panda3d.egg.EggGroupNode' objects>"
        'strip_normals': None, # (!) real value is "<method 'strip_normals' of 'panda3d.egg.EggGroupNode' objects>"
        'triangulatePolygons': None, # (!) real value is "<method 'triangulatePolygons' of 'panda3d.egg.EggGroupNode' objects>"
        'triangulate_polygons': None, # (!) real value is "<method 'triangulate_polygons' of 'panda3d.egg.EggGroupNode' objects>"
        'unifyAttributes': None, # (!) real value is "<method 'unifyAttributes' of 'panda3d.egg.EggGroupNode' objects>"
        'unify_attributes': None, # (!) real value is "<method 'unify_attributes' of 'panda3d.egg.EggGroupNode' objects>"
    }
    TComposite = 4
    TConvex = 2
    TFlatShaded = 16
    TPolygon = 1
    TRecurse = 8
    T_composite = 4
    T_convex = 2
    T_flat_shaded = 16
    T_polygon = 1
    T_recurse = 8


