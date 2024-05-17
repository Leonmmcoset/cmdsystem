# encoding: utf-8
# module panda3d.egg
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\egg.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import panda3d.core as __panda3d_core


from .EggNode import EggNode

from .EggAttributes import EggAttributes

from .EggRenderMode import EggRenderMode

class EggPrimitive(EggNode, EggAttributes, EggRenderMode):
    """
    /**
     * A base class for any of a number of kinds of geometry primitives: polygons,
     * point lights, nurbs patches, parametrics curves, etc.  Things with a set of
     * vertices and some rendering properties like color.
     *
     * An EggPrimitive is an STL-style container of pointers to EggVertex's.  In
     * fact, it IS a vector, and can be manipulated in all the ways that vectors
     * can.  However, it is necessary that all vertices belong to the same vertex
     * pool.
     */
    """
    def addTexture(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_texture(const EggPrimitive self, EggTexture texture)
        
        /**
         * Applies the indicated texture to the primitive.
         *
         * Note that, in the case of multiple textures being applied to a single
         * primitive, the order in which the textures are applied does not affect the
         * rendering order; use EggTexture::set_sort() to specify that.
         */
        """
        pass

    def addVertex(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_vertex(const EggPrimitive self, EggVertex vertex)
        
        /**
         * Adds the indicated vertex to the end of the primitive's list of vertices,
         * and returns it.
         */
        """
        pass

    def add_texture(self, const_EggPrimitive_self, EggTexture_texture): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_texture(const EggPrimitive self, EggTexture texture)
        
        /**
         * Applies the indicated texture to the primitive.
         *
         * Note that, in the case of multiple textures being applied to a single
         * primitive, the order in which the textures are applied does not affect the
         * rendering order; use EggTexture::set_sort() to specify that.
         */
        """
        pass

    def add_vertex(self, const_EggPrimitive_self, EggVertex_vertex): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_vertex(const EggPrimitive self, EggVertex vertex)
        
        /**
         * Adds the indicated vertex to the end of the primitive's list of vertices,
         * and returns it.
         */
        """
        pass

    def applyFirstAttribute(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        apply_first_attribute(const EggPrimitive self)
        
        /**
         * Sets the first vertex of the triangle (or each component) to the primitive
         * normal and/or color, if the primitive is flat-shaded.  This reflects the
         * DirectX convention of storing flat-shaded properties on the first vertex,
         * although it is not usually a convention in Egg.
         *
         * This may introduce redundant vertices to the vertex pool.
         */
        """
        pass

    def applyLastAttribute(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        apply_last_attribute(const EggPrimitive self)
        
        /**
         * Sets the last vertex of the triangle (or each component) to the primitive
         * normal and/or color, if the primitive is flat-shaded.  This reflects the
         * OpenGL convention of storing flat-shaded properties on the last vertex,
         * although it is not usually a convention in Egg.
         *
         * This may introduce redundant vertices to the vertex pool.
         */
        """
        pass

    def apply_first_attribute(self, const_EggPrimitive_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        apply_first_attribute(const EggPrimitive self)
        
        /**
         * Sets the first vertex of the triangle (or each component) to the primitive
         * normal and/or color, if the primitive is flat-shaded.  This reflects the
         * DirectX convention of storing flat-shaded properties on the first vertex,
         * although it is not usually a convention in Egg.
         *
         * This may introduce redundant vertices to the vertex pool.
         */
        """
        pass

    def apply_last_attribute(self, const_EggPrimitive_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        apply_last_attribute(const EggPrimitive self)
        
        /**
         * Sets the last vertex of the triangle (or each component) to the primitive
         * normal and/or color, if the primitive is flat-shaded.  This reflects the
         * OpenGL convention of storing flat-shaded properties on the last vertex,
         * although it is not usually a convention in Egg.
         *
         * This may introduce redundant vertices to the vertex pool.
         */
        """
        pass

    def assign(self, const_EggPrimitive_self, const_EggPrimitive_copy): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        assign(const EggPrimitive self, const EggPrimitive copy)
        
        /**
         *
         */
        """
        pass

    def cleanup(self, const_EggPrimitive_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        cleanup(const EggPrimitive self)
        
        /**
         * Cleans up modeling errors in whatever context this makes sense.  For
         * instance, for a polygon, this calls remove_doubled_verts(true).  For a
         * point, it calls remove_nonunique_verts().  Returns true if the primitive is
         * valid, or false if it is degenerate.
         */
        """
        pass

    def clear(self, const_EggPrimitive_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear(const EggPrimitive self)
        
        /**
         * Removes all of the vertices from the primitive.
         */
        """
        pass

    def clearConnectedShading(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_connected_shading(const EggPrimitive self)
        
        /**
         * Resets the connected_shading member in this primitive, so that
         * get_connected_shading() will recompute a new value.
         */
        """
        pass

    def clearMaterial(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_material(const EggPrimitive self)
        
        /**
         * Removes any material from the primitive.
         */
        """
        pass

    def clearTexture(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_texture(const EggPrimitive self)
        
        /**
         * Removes any texturing from the primitive.
         */
        """
        pass

    def clear_connected_shading(self, const_EggPrimitive_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_connected_shading(const EggPrimitive self)
        
        /**
         * Resets the connected_shading member in this primitive, so that
         * get_connected_shading() will recompute a new value.
         */
        """
        pass

    def clear_material(self, const_EggPrimitive_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_material(const EggPrimitive self)
        
        /**
         * Removes any material from the primitive.
         */
        """
        pass

    def clear_texture(self, const_EggPrimitive_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_texture(const EggPrimitive self)
        
        /**
         * Removes any texturing from the primitive.
         */
        """
        pass

    def copyAttributes(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        copy_attributes(const EggPrimitive self, const EggPrimitive other)
        copy_attributes(const EggPrimitive self, const EggAttributes other)
        
        /**
         * Copies the rendering attributes from the indicated primitive.
         */
        
        /**
         * Copies the rendering attributes from the indicated primitive.
         */
        """
        pass

    def copyVertices(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        copy_vertices(const EggPrimitive self, const EggPrimitive other)
        
        /**
         * Replaces the current primitive's list of vertices with a copy of the list
         * of vertices on the other primitive.
         */
        """
        pass

    def copy_attributes(self, const_EggPrimitive_self, const_EggPrimitive_other): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        copy_attributes(const EggPrimitive self, const EggPrimitive other)
        copy_attributes(const EggPrimitive self, const EggAttributes other)
        
        /**
         * Copies the rendering attributes from the indicated primitive.
         */
        
        /**
         * Copies the rendering attributes from the indicated primitive.
         */
        """
        pass

    def copy_vertices(self, const_EggPrimitive_self, const_EggPrimitive_other): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        copy_vertices(const EggPrimitive self, const EggPrimitive other)
        
        /**
         * Replaces the current primitive's list of vertices with a copy of the list
         * of vertices on the other primitive.
         */
        """
        pass

    def determineAlphaMode(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        determine_alpha_mode(const EggPrimitive self)
        
        /**
         * Walks back up the hierarchy, looking for an EggGroup or EggPrimitive or
         * some such object at this level or above this primitive that has an
         * alpha_mode other than AM_unspecified.  Returns a valid EggRenderMode
         * pointer if one is found, or NULL otherwise.
         */
        """
        pass

    def determineBin(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        determine_bin(const EggPrimitive self)
        
        /**
         * Walks back up the hierarchy, looking for an EggGroup or EggPrimitive or
         * some such object at this level or above this primitive that has a bin
         * specified.  Returns a valid EggRenderMode pointer if one is found, or NULL
         * otherwise.
         */
        """
        pass

    def determineDepthOffset(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        determine_depth_offset(const EggPrimitive self)
        
        /**
         * Walks back up the hierarchy, looking for an EggGroup or EggPrimitive or
         * some such object at this level or above this primitive that has a
         * depth_offset specified.  Returns a valid EggRenderMode pointer if one is
         * found, or NULL otherwise.
         */
        """
        pass

    def determineDepthTestMode(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        determine_depth_test_mode(const EggPrimitive self)
        
        /**
         * Walks back up the hierarchy, looking for an EggGroup or EggPrimitive or
         * some such object at this level or above this node that has a
         * depth_test_mode other than DTM_unspecified.  Returns a valid EggRenderMode
         * pointer if one is found, or NULL otherwise.
         */
        """
        pass

    def determineDepthWriteMode(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        determine_depth_write_mode(const EggPrimitive self)
        
        /**
         * Walks back up the hierarchy, looking for an EggGroup or EggPrimitive or
         * some such object at this level or above this node that has a
         * depth_write_mode other than DWM_unspecified.  Returns a valid EggRenderMode
         * pointer if one is found, or NULL otherwise.
         */
        """
        pass

    def determineDrawOrder(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        determine_draw_order(const EggPrimitive self)
        
        /**
         * Walks back up the hierarchy, looking for an EggGroup or EggPrimitive or
         * some such object at this level or above this primitive that has a
         * draw_order specified.  Returns a valid EggRenderMode pointer if one is
         * found, or NULL otherwise.
         */
        """
        pass

    def determineVisibilityMode(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        determine_visibility_mode(const EggPrimitive self)
        
        /**
         * Walks back up the hierarchy, looking for an EggGroup or EggPrimitive or
         * some such object at this level or above this node that has a
         * visibility_mode other than VM_unspecified.  Returns a valid EggRenderMode
         * pointer if one is found, or NULL otherwise.
         */
        """
        pass

    def determine_alpha_mode(self, const_EggPrimitive_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        determine_alpha_mode(const EggPrimitive self)
        
        /**
         * Walks back up the hierarchy, looking for an EggGroup or EggPrimitive or
         * some such object at this level or above this primitive that has an
         * alpha_mode other than AM_unspecified.  Returns a valid EggRenderMode
         * pointer if one is found, or NULL otherwise.
         */
        """
        pass

    def determine_bin(self, const_EggPrimitive_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        determine_bin(const EggPrimitive self)
        
        /**
         * Walks back up the hierarchy, looking for an EggGroup or EggPrimitive or
         * some such object at this level or above this primitive that has a bin
         * specified.  Returns a valid EggRenderMode pointer if one is found, or NULL
         * otherwise.
         */
        """
        pass

    def determine_depth_offset(self, const_EggPrimitive_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        determine_depth_offset(const EggPrimitive self)
        
        /**
         * Walks back up the hierarchy, looking for an EggGroup or EggPrimitive or
         * some such object at this level or above this primitive that has a
         * depth_offset specified.  Returns a valid EggRenderMode pointer if one is
         * found, or NULL otherwise.
         */
        """
        pass

    def determine_depth_test_mode(self, const_EggPrimitive_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        determine_depth_test_mode(const EggPrimitive self)
        
        /**
         * Walks back up the hierarchy, looking for an EggGroup or EggPrimitive or
         * some such object at this level or above this node that has a
         * depth_test_mode other than DTM_unspecified.  Returns a valid EggRenderMode
         * pointer if one is found, or NULL otherwise.
         */
        """
        pass

    def determine_depth_write_mode(self, const_EggPrimitive_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        determine_depth_write_mode(const EggPrimitive self)
        
        /**
         * Walks back up the hierarchy, looking for an EggGroup or EggPrimitive or
         * some such object at this level or above this node that has a
         * depth_write_mode other than DWM_unspecified.  Returns a valid EggRenderMode
         * pointer if one is found, or NULL otherwise.
         */
        """
        pass

    def determine_draw_order(self, const_EggPrimitive_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        determine_draw_order(const EggPrimitive self)
        
        /**
         * Walks back up the hierarchy, looking for an EggGroup or EggPrimitive or
         * some such object at this level or above this primitive that has a
         * draw_order specified.  Returns a valid EggRenderMode pointer if one is
         * found, or NULL otherwise.
         */
        """
        pass

    def determine_visibility_mode(self, const_EggPrimitive_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        determine_visibility_mode(const EggPrimitive self)
        
        /**
         * Walks back up the hierarchy, looking for an EggGroup or EggPrimitive or
         * some such object at this level or above this node that has a
         * visibility_mode other than VM_unspecified.  Returns a valid EggRenderMode
         * pointer if one is found, or NULL otherwise.
         */
        """
        pass

    def getBfaceFlag(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_bface_flag(EggPrimitive self)
        
        /**
         * Retrieves the backfacing flag of the polygon.  See set_bface_flag().
         */
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
        get_connected_shading(EggPrimitive self)
        
        /**
         * Determines what sort of shading properties this primitive's connected
         * neighbors have.
         *
         * To get the most accurate results, you should first call
         * clear_connected_shading() on all connected primitives (or on all primitives
         * in the egg file). It might also be a good idea to call
         * remove_unused_vertices() to ensure proper connectivity.
         *
         * You may find it easiest to call these other methods on the EggData root
         * node (they are defined on EggGroupNode).
         */
        """
        pass

    def getMaterial(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_material(EggPrimitive self)
        
        /**
         * Returns a pointer to the applied material, or NULL if there is no material
         * applied.
         */
        """
        pass

    def getNumTextures(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_textures(EggPrimitive self)
        
        /**
         * Returns the number of textures applied to the primitive.
         */
        """
        pass

    def getNumVertices(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_vertices(EggPrimitive self)
        
        // These are shorthands if you don't want to use the iterators.
        
        // These are shorthands if you don't want to use the iterators.
        
        // These are shorthands if you don't want to use the iterators.
        
        /**
         *
         */
        """
        pass

    def getPool(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_pool(EggPrimitive self)
        
        /**
         * Returns the vertex pool associated with the vertices of the primitive, or
         * NULL if the primitive has no vertices.
         */
        """
        pass

    def getShading(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_shading(EggPrimitive self)
        
        /**
         * Returns the shading properties apparent on this particular primitive.  This
         * returns S_per_vertex if the vertices have colors or normals (and they are
         * not all the same values), or for a simple primitive, S_overall otherwise.
         * A composite primitive may also return S_per_face if the individual
         * component primitives have colors or normals that are not all the same
         * values.
         *
         * To get the most accurate results, you should call clear_shading() on all
         * connected primitives (or on all primitives in the egg file), followed by
         * get_shading() on each primitive.  You may find it easiest to call these
         * methods on the EggData root node (they are defined on EggGroupNode).
         */
        """
        pass

    def getSortName(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_sort_name(EggPrimitive self)
        
        /**
         * Returns the name of the primitive for the purposes of sorting primitives
         * into different groups, if there is one.
         *
         * Presently, this is defined as the primitive name itself, unless it begins
         * with a digit.
         */
        """
        pass

    def getTexture(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_texture(EggPrimitive self)
        get_texture(EggPrimitive self, int n)
        
        /**
         * Returns the first texture on the primitive, if any, or NULL if there are no
         * textures on the primitive.
         *
         * @deprecated This method is used in support of single-texturing only.
         * New code should be written to use the multitexture variants instead.
         */
        
        /**
         * Returns the nth texture that has been applied to the primitive.
         */
        """
        pass

    def getTextures(self, *args, **kwargs): # real signature unknown
        pass

    def getVertex(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_vertex(EggPrimitive self, int index)
        
        /**
         * Returns a particular index based on its index number.
         */
        """
        pass

    def getVertices(self, *args, **kwargs): # real signature unknown
        pass

    def get_bface_flag(self, EggPrimitive_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_bface_flag(EggPrimitive self)
        
        /**
         * Retrieves the backfacing flag of the polygon.  See set_bface_flag().
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_connected_shading(self, EggPrimitive_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_connected_shading(EggPrimitive self)
        
        /**
         * Determines what sort of shading properties this primitive's connected
         * neighbors have.
         *
         * To get the most accurate results, you should first call
         * clear_connected_shading() on all connected primitives (or on all primitives
         * in the egg file). It might also be a good idea to call
         * remove_unused_vertices() to ensure proper connectivity.
         *
         * You may find it easiest to call these other methods on the EggData root
         * node (they are defined on EggGroupNode).
         */
        """
        pass

    def get_material(self, EggPrimitive_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_material(EggPrimitive self)
        
        /**
         * Returns a pointer to the applied material, or NULL if there is no material
         * applied.
         */
        """
        pass

    def get_num_textures(self, EggPrimitive_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_textures(EggPrimitive self)
        
        /**
         * Returns the number of textures applied to the primitive.
         */
        """
        pass

    def get_num_vertices(self, EggPrimitive_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_vertices(EggPrimitive self)
        
        // These are shorthands if you don't want to use the iterators.
        
        // These are shorthands if you don't want to use the iterators.
        
        // These are shorthands if you don't want to use the iterators.
        
        /**
         *
         */
        """
        pass

    def get_pool(self, EggPrimitive_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_pool(EggPrimitive self)
        
        /**
         * Returns the vertex pool associated with the vertices of the primitive, or
         * NULL if the primitive has no vertices.
         */
        """
        pass

    def get_shading(self, EggPrimitive_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_shading(EggPrimitive self)
        
        /**
         * Returns the shading properties apparent on this particular primitive.  This
         * returns S_per_vertex if the vertices have colors or normals (and they are
         * not all the same values), or for a simple primitive, S_overall otherwise.
         * A composite primitive may also return S_per_face if the individual
         * component primitives have colors or normals that are not all the same
         * values.
         *
         * To get the most accurate results, you should call clear_shading() on all
         * connected primitives (or on all primitives in the egg file), followed by
         * get_shading() on each primitive.  You may find it easiest to call these
         * methods on the EggData root node (they are defined on EggGroupNode).
         */
        """
        pass

    def get_sort_name(self, EggPrimitive_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_sort_name(EggPrimitive self)
        
        /**
         * Returns the name of the primitive for the purposes of sorting primitives
         * into different groups, if there is one.
         *
         * Presently, this is defined as the primitive name itself, unless it begins
         * with a digit.
         */
        """
        pass

    def get_texture(self, EggPrimitive_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_texture(EggPrimitive self)
        get_texture(EggPrimitive self, int n)
        
        /**
         * Returns the first texture on the primitive, if any, or NULL if there are no
         * textures on the primitive.
         *
         * @deprecated This method is used in support of single-texturing only.
         * New code should be written to use the multitexture variants instead.
         */
        
        /**
         * Returns the nth texture that has been applied to the primitive.
         */
        """
        pass

    def get_textures(self, *args, **kwargs): # real signature unknown
        pass

    def get_vertex(self, EggPrimitive_self, int_index): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_vertex(EggPrimitive self, int index)
        
        /**
         * Returns a particular index based on its index number.
         */
        """
        pass

    def get_vertices(self, *args, **kwargs): # real signature unknown
        pass

    def hasMaterial(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_material(EggPrimitive self)
        
        /**
         * Returns true if the primitive is materiald (and get_material() will return
         * a real pointer), false otherwise (and get_material() will return NULL).
         */
        """
        pass

    def hasNormals(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_normals(EggPrimitive self)
        
        /**
         * Returns true if any of the primitives (e.g.  polygons) defined within this
         * group or below have either face or vertex normals defined, false otherwise.
         */
        """
        pass

    def hasPrimitives(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_primitives(EggPrimitive self)
        
        /**
         * Returns true if there are any primitives (e.g.  polygons) defined within
         * this group or below, false otherwise.
         */
        """
        pass

    def hasTexture(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_texture(EggPrimitive self)
        has_texture(EggPrimitive self, EggTexture texture)
        
        /**
         * Returns true if the primitive has any textures specified, false otherwise.
         *
         * @deprecated This method is used in support of single-texturing only.
         * New code should be written to use the multitexture variants instead.
         */
        
        /**
         * Returns true if the primitive has the particular indicated texture, false
         * otherwise.
         */
        """
        pass

    def hasVertexColor(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_vertex_color(EggPrimitive self)
        
        /**
         * Returns true if any vertex on the primitive has a specific color set, false
         * otherwise.
         *
         * If you call unify_attributes() first, this will also return false even if
         * all the vertices were set to the same value (since unify_attributes()
         * removes redundant vertex properties).
         */
        """
        pass

    def hasVertexNormal(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_vertex_normal(EggPrimitive self)
        
        /**
         * Returns true if any vertex on the primitive has a specific normal set,
         * false otherwise.
         *
         * If you call unify_attributes() first, this will also return false even if
         * all the vertices were set to the same value (since unify_attributes()
         * removes redundant vertex properties).
         */
        """
        pass

    def has_material(self, EggPrimitive_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_material(EggPrimitive self)
        
        /**
         * Returns true if the primitive is materiald (and get_material() will return
         * a real pointer), false otherwise (and get_material() will return NULL).
         */
        """
        pass

    def has_normals(self, EggPrimitive_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_normals(EggPrimitive self)
        
        /**
         * Returns true if any of the primitives (e.g.  polygons) defined within this
         * group or below have either face or vertex normals defined, false otherwise.
         */
        """
        pass

    def has_primitives(self, EggPrimitive_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_primitives(EggPrimitive self)
        
        /**
         * Returns true if there are any primitives (e.g.  polygons) defined within
         * this group or below, false otherwise.
         */
        """
        pass

    def has_texture(self, EggPrimitive_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_texture(EggPrimitive self)
        has_texture(EggPrimitive self, EggTexture texture)
        
        /**
         * Returns true if the primitive has any textures specified, false otherwise.
         *
         * @deprecated This method is used in support of single-texturing only.
         * New code should be written to use the multitexture variants instead.
         */
        
        /**
         * Returns true if the primitive has the particular indicated texture, false
         * otherwise.
         */
        """
        pass

    def has_vertex_color(self, EggPrimitive_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_vertex_color(EggPrimitive self)
        
        /**
         * Returns true if any vertex on the primitive has a specific color set, false
         * otherwise.
         *
         * If you call unify_attributes() first, this will also return false even if
         * all the vertices were set to the same value (since unify_attributes()
         * removes redundant vertex properties).
         */
        """
        pass

    def has_vertex_normal(self, EggPrimitive_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_vertex_normal(EggPrimitive self)
        
        /**
         * Returns true if any vertex on the primitive has a specific normal set,
         * false otherwise.
         *
         * If you call unify_attributes() first, this will also return false even if
         * all the vertices were set to the same value (since unify_attributes()
         * removes redundant vertex properties).
         */
        """
        pass

    def insertVertex(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        insert_vertex(const EggPrimitive self, int index, EggVertex vertex)
        
        /**
         * Inserts a vertex at the given position.
         */
        """
        pass

    def insert_vertex(self, const_EggPrimitive_self, int_index, EggVertex_vertex): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        insert_vertex(const EggPrimitive self, int index, EggVertex vertex)
        
        /**
         * Inserts a vertex at the given position.
         */
        """
        pass

    def jointHasPrimitives(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        joint_has_primitives(EggPrimitive self)
        
        /**
         * Returns true if there are any primitives (e.g.  polygons) defined within
         * this group or below, but the search does not include nested joints.
         */
        """
        pass

    def joint_has_primitives(self, EggPrimitive_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        joint_has_primitives(EggPrimitive self)
        
        /**
         * Returns true if there are any primitives (e.g.  polygons) defined within
         * this group or below, but the search does not include nested joints.
         */
        """
        pass

    def makeCopy(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        make_copy(EggPrimitive self)
        """
        pass

    def make_copy(self, EggPrimitive_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        make_copy(EggPrimitive self)
        """
        pass

    def postApplyFlatAttribute(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        post_apply_flat_attribute(const EggPrimitive self)
        
        /**
         * Intended as a followup to apply_last_attribute(), this also sets an
         * attribute on the first vertices of the primitive, if they don't already
         * have an attribute set, just so they end up with *something*.
         */
        """
        pass

    def post_apply_flat_attribute(self, const_EggPrimitive_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        post_apply_flat_attribute(const EggPrimitive self)
        
        /**
         * Intended as a followup to apply_last_attribute(), this also sets an
         * attribute on the first vertices of the primitive, if they don't already
         * have an attribute set, just so they end up with *something*.
         */
        """
        pass

    def removeDoubledVerts(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        remove_doubled_verts(const EggPrimitive self, bool closed)
        
        /**
         * Certain kinds of primitives, particularly polygons, don't like to have the
         * same vertex repeated consecutively.  Unfortunately, some modeling programs
         * (like MultiGen) make this an easy mistake to make.
         *
         * It's handy to have a function to remove these redundant vertices.  If
         * closed is true, it also checks that the first and last vertices are not the
         * same.
         *
         * This function identifies repeated vertices by position only; it does not
         * consider any other properties, such as color or UV, significant in
         * differentiating vertices.
         */
        """
        pass

    def removeNonuniqueVerts(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        remove_nonunique_verts(const EggPrimitive self)
        
        /**
         * Removes any multiple appearances of the same vertex from the primitive.
         * This primarily makes sense for a point primitive, which is really a
         * collection of points and which doesn't make sense to include the same point
         * twice, in any order.
         */
        """
        pass

    def removeVertex(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        remove_vertex(const EggPrimitive self, EggVertex vertex)
        remove_vertex(const EggPrimitive self, int index)
        
        /**
         * Removes the indicated vertex from the primitive and returns it.  If the
         * vertex was not already in the primitive, does nothing and returns NULL.
         */
        
        /**
         * Removes the indicated vertex from the primitive.
         */
        """
        pass

    def remove_doubled_verts(self, const_EggPrimitive_self, bool_closed): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        remove_doubled_verts(const EggPrimitive self, bool closed)
        
        /**
         * Certain kinds of primitives, particularly polygons, don't like to have the
         * same vertex repeated consecutively.  Unfortunately, some modeling programs
         * (like MultiGen) make this an easy mistake to make.
         *
         * It's handy to have a function to remove these redundant vertices.  If
         * closed is true, it also checks that the first and last vertices are not the
         * same.
         *
         * This function identifies repeated vertices by position only; it does not
         * consider any other properties, such as color or UV, significant in
         * differentiating vertices.
         */
        """
        pass

    def remove_nonunique_verts(self, const_EggPrimitive_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        remove_nonunique_verts(const EggPrimitive self)
        
        /**
         * Removes any multiple appearances of the same vertex from the primitive.
         * This primarily makes sense for a point primitive, which is really a
         * collection of points and which doesn't make sense to include the same point
         * twice, in any order.
         */
        """
        pass

    def remove_vertex(self, const_EggPrimitive_self, EggVertex_vertex): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        remove_vertex(const EggPrimitive self, EggVertex vertex)
        remove_vertex(const EggPrimitive self, int index)
        
        /**
         * Removes the indicated vertex from the primitive and returns it.  If the
         * vertex was not already in the primitive, does nothing and returns NULL.
         */
        
        /**
         * Removes the indicated vertex from the primitive.
         */
        """
        pass

    def reverseVertexOrdering(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        reverse_vertex_ordering(const EggPrimitive self)
        
        /**
         * Reverses the ordering of the vertices in this primitive, if appropriate, in
         * order to change the direction the polygon appears to be facing.  Does not
         * adjust the surface normal, if any.
         */
        """
        pass

    def reverse_vertex_ordering(self, const_EggPrimitive_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        reverse_vertex_ordering(const EggPrimitive self)
        
        /**
         * Reverses the ordering of the vertices in this primitive, if appropriate, in
         * order to change the direction the polygon appears to be facing.  Does not
         * adjust the surface normal, if any.
         */
        """
        pass

    def setBfaceFlag(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_bface_flag(const EggPrimitive self, bool flag)
        
        /**
         * Sets the backfacing flag of the polygon.  If this is true, the polygon will
         * be rendered so that both faces are visible; if it is false, only the front
         * face of the polygon will be visible.
         */
        """
        pass

    def setMaterial(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_material(const EggPrimitive self, EggMaterial material)
        
        /**
         * Applies the indicated material to the primitive.
         */
        """
        pass

    def setTexture(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_texture(const EggPrimitive self, EggTexture texture)
        
        /**
         * Replaces the current list of textures with the indicated texture.
         *
         * @deprecated This method is used in support of single-texturing only.
         * Please use the multitexture variant add_texture instead.
         */
        """
        pass

    def setVertex(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_vertex(const EggPrimitive self, int index, EggVertex vertex)
        
        /**
         * Replaces a particular vertex based on its index number in the list of
         * vertices.  This is just a convenience function for people who don't want to
         * mess with the iterators.
         */
        """
        pass

    def set_bface_flag(self, const_EggPrimitive_self, bool_flag): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_bface_flag(const EggPrimitive self, bool flag)
        
        /**
         * Sets the backfacing flag of the polygon.  If this is true, the polygon will
         * be rendered so that both faces are visible; if it is false, only the front
         * face of the polygon will be visible.
         */
        """
        pass

    def set_material(self, const_EggPrimitive_self, EggMaterial_material): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_material(const EggPrimitive self, EggMaterial material)
        
        /**
         * Applies the indicated material to the primitive.
         */
        """
        pass

    def set_texture(self, const_EggPrimitive_self, EggTexture_texture): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_texture(const EggPrimitive self, EggTexture texture)
        
        /**
         * Replaces the current list of textures with the indicated texture.
         *
         * @deprecated This method is used in support of single-texturing only.
         * Please use the multitexture variant add_texture instead.
         */
        """
        pass

    def set_vertex(self, const_EggPrimitive_self, int_index, EggVertex_vertex): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_vertex(const EggPrimitive self, int index, EggVertex vertex)
        
        /**
         * Replaces a particular vertex based on its index number in the list of
         * vertices.  This is just a convenience function for people who don't want to
         * mess with the iterators.
         */
        """
        pass

    def testVrefIntegrity(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        test_vref_integrity(EggPrimitive self)
        """
        pass

    def test_vref_integrity(self, EggPrimitive_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        test_vref_integrity(EggPrimitive self)
        """
        pass

    def unifyAttributes(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        unify_attributes(const EggPrimitive self, int shading)
        
        /**
         * If the shading property is S_per_vertex, ensures that all vertices have a
         * normal and a color, and the overall primitive does not.
         *
         * If the shading property is S_per_face, and this is a composite primitive,
         * ensures that all components have a normal and a color, and the vertices and
         * overall primitive do not.  (If this is a simple primitive, S_per_face works
         * the same as S_overall, below).
         *
         * If the shading property is S_overall, ensures that no vertices or
         * components have a normal or a color, and the overall primitive does (if any
         * exists at all).
         *
         * After this call, either the primitive will have normals or its vertices
         * will, but not both.  Ditto for colors.
         *
         * This may create redundant vertices in the vertex pool.
         */
        """
        pass

    def unify_attributes(self, const_EggPrimitive_self, int_shading): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        unify_attributes(const EggPrimitive self, int shading)
        
        /**
         * If the shading property is S_per_vertex, ensures that all vertices have a
         * normal and a color, and the overall primitive does not.
         *
         * If the shading property is S_per_face, and this is a composite primitive,
         * ensures that all components have a normal and a color, and the vertices and
         * overall primitive do not.  (If this is a simple primitive, S_per_face works
         * the same as S_overall, below).
         *
         * If the shading property is S_overall, ensures that no vertices or
         * components have a normal or a color, and the overall primitive does (if any
         * exists at all).
         *
         * After this call, either the primitive will have normals or its vertices
         * will, but not both.  Ditto for colors.
         *
         * This may create redundant vertices in the vertex pool.
         */
        """
        pass

    def upcastToEggAttributes(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        upcast_to_EggAttributes(const EggPrimitive self)
        
        upcast from EggPrimitive to EggAttributes
        """
        pass

    def upcastToEggNode(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        upcast_to_EggNode(const EggPrimitive self)
        
        upcast from EggPrimitive to EggNode
        """
        pass

    def upcastToEggRenderMode(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        upcast_to_EggRenderMode(const EggPrimitive self)
        
        upcast from EggPrimitive to EggRenderMode
        """
        pass

    def upcast_to_EggAttributes(self, const_EggPrimitive_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        upcast_to_EggAttributes(const EggPrimitive self)
        
        upcast from EggPrimitive to EggAttributes
        """
        pass

    def upcast_to_EggNode(self, const_EggPrimitive_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        upcast_to_EggNode(const EggPrimitive self)
        
        upcast from EggPrimitive to EggNode
        """
        pass

    def upcast_to_EggRenderMode(self, const_EggPrimitive_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        upcast_to_EggRenderMode(const EggPrimitive self)
        
        upcast from EggPrimitive to EggRenderMode
        """
        pass

    def write(self, EggPrimitive_self, ostream_out, int_indent_level): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        write(EggPrimitive self, ostream out, int indent_level)
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

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    bface_flag = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    connected_shading = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    material = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pool = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    shading = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    sort_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    textures = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    vertices = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        'SOverall': 1,
        'SPerFace': 2,
        'SPerVertex': 3,
        'SUnknown': 0,
        'S_overall': 1,
        'S_per_face': 2,
        'S_per_vertex': 3,
        'S_unknown': 0,
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.egg.EggPrimitive' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.egg.EggPrimitive' objects>"
        '__doc__': "/**\n * A base class for any of a number of kinds of geometry primitives: polygons,\n * point lights, nurbs patches, parametrics curves, etc.  Things with a set of\n * vertices and some rendering properties like color.\n *\n * An EggPrimitive is an STL-style container of pointers to EggVertex's.  In\n * fact, it IS a vector, and can be manipulated in all the ways that vectors\n * can.  However, it is necessary that all vertices belong to the same vertex\n * pool.\n */",
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.egg.EggPrimitive' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFDC68CEF60>'
        '__str__': None, # (!) real value is "<slot wrapper '__str__' of 'panda3d.egg.EggPrimitive' objects>"
        'addTexture': None, # (!) real value is "<method 'addTexture' of 'panda3d.egg.EggPrimitive' objects>"
        'addVertex': None, # (!) real value is "<method 'addVertex' of 'panda3d.egg.EggPrimitive' objects>"
        'add_texture': None, # (!) real value is "<method 'add_texture' of 'panda3d.egg.EggPrimitive' objects>"
        'add_vertex': None, # (!) real value is "<method 'add_vertex' of 'panda3d.egg.EggPrimitive' objects>"
        'applyFirstAttribute': None, # (!) real value is "<method 'applyFirstAttribute' of 'panda3d.egg.EggPrimitive' objects>"
        'applyLastAttribute': None, # (!) real value is "<method 'applyLastAttribute' of 'panda3d.egg.EggPrimitive' objects>"
        'apply_first_attribute': None, # (!) real value is "<method 'apply_first_attribute' of 'panda3d.egg.EggPrimitive' objects>"
        'apply_last_attribute': None, # (!) real value is "<method 'apply_last_attribute' of 'panda3d.egg.EggPrimitive' objects>"
        'assign': None, # (!) real value is "<method 'assign' of 'panda3d.egg.EggPrimitive' objects>"
        'bface_flag': None, # (!) real value is "<attribute 'bface_flag' of 'panda3d.egg.EggPrimitive' objects>"
        'cleanup': None, # (!) real value is "<method 'cleanup' of 'panda3d.egg.EggPrimitive' objects>"
        'clear': None, # (!) real value is "<method 'clear' of 'panda3d.egg.EggPrimitive' objects>"
        'clearConnectedShading': None, # (!) real value is "<method 'clearConnectedShading' of 'panda3d.egg.EggPrimitive' objects>"
        'clearMaterial': None, # (!) real value is "<method 'clearMaterial' of 'panda3d.egg.EggPrimitive' objects>"
        'clearTexture': None, # (!) real value is "<method 'clearTexture' of 'panda3d.egg.EggPrimitive' objects>"
        'clear_connected_shading': None, # (!) real value is "<method 'clear_connected_shading' of 'panda3d.egg.EggPrimitive' objects>"
        'clear_material': None, # (!) real value is "<method 'clear_material' of 'panda3d.egg.EggPrimitive' objects>"
        'clear_texture': None, # (!) real value is "<method 'clear_texture' of 'panda3d.egg.EggPrimitive' objects>"
        'connected_shading': None, # (!) real value is "<attribute 'connected_shading' of 'panda3d.egg.EggPrimitive' objects>"
        'copyAttributes': None, # (!) real value is "<method 'copyAttributes' of 'panda3d.egg.EggPrimitive' objects>"
        'copyVertices': None, # (!) real value is "<method 'copyVertices' of 'panda3d.egg.EggPrimitive' objects>"
        'copy_attributes': None, # (!) real value is "<method 'copy_attributes' of 'panda3d.egg.EggPrimitive' objects>"
        'copy_vertices': None, # (!) real value is "<method 'copy_vertices' of 'panda3d.egg.EggPrimitive' objects>"
        'determineAlphaMode': None, # (!) real value is "<method 'determineAlphaMode' of 'panda3d.egg.EggPrimitive' objects>"
        'determineBin': None, # (!) real value is "<method 'determineBin' of 'panda3d.egg.EggPrimitive' objects>"
        'determineDepthOffset': None, # (!) real value is "<method 'determineDepthOffset' of 'panda3d.egg.EggPrimitive' objects>"
        'determineDepthTestMode': None, # (!) real value is "<method 'determineDepthTestMode' of 'panda3d.egg.EggPrimitive' objects>"
        'determineDepthWriteMode': None, # (!) real value is "<method 'determineDepthWriteMode' of 'panda3d.egg.EggPrimitive' objects>"
        'determineDrawOrder': None, # (!) real value is "<method 'determineDrawOrder' of 'panda3d.egg.EggPrimitive' objects>"
        'determineVisibilityMode': None, # (!) real value is "<method 'determineVisibilityMode' of 'panda3d.egg.EggPrimitive' objects>"
        'determine_alpha_mode': None, # (!) real value is "<method 'determine_alpha_mode' of 'panda3d.egg.EggPrimitive' objects>"
        'determine_bin': None, # (!) real value is "<method 'determine_bin' of 'panda3d.egg.EggPrimitive' objects>"
        'determine_depth_offset': None, # (!) real value is "<method 'determine_depth_offset' of 'panda3d.egg.EggPrimitive' objects>"
        'determine_depth_test_mode': None, # (!) real value is "<method 'determine_depth_test_mode' of 'panda3d.egg.EggPrimitive' objects>"
        'determine_depth_write_mode': None, # (!) real value is "<method 'determine_depth_write_mode' of 'panda3d.egg.EggPrimitive' objects>"
        'determine_draw_order': None, # (!) real value is "<method 'determine_draw_order' of 'panda3d.egg.EggPrimitive' objects>"
        'determine_visibility_mode': None, # (!) real value is "<method 'determine_visibility_mode' of 'panda3d.egg.EggPrimitive' objects>"
        'getBfaceFlag': None, # (!) real value is "<method 'getBfaceFlag' of 'panda3d.egg.EggPrimitive' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFDC68CEF60>)>'
        'getConnectedShading': None, # (!) real value is "<method 'getConnectedShading' of 'panda3d.egg.EggPrimitive' objects>"
        'getMaterial': None, # (!) real value is "<method 'getMaterial' of 'panda3d.egg.EggPrimitive' objects>"
        'getNumTextures': None, # (!) real value is "<method 'getNumTextures' of 'panda3d.egg.EggPrimitive' objects>"
        'getNumVertices': None, # (!) real value is "<method 'getNumVertices' of 'panda3d.egg.EggPrimitive' objects>"
        'getPool': None, # (!) real value is "<method 'getPool' of 'panda3d.egg.EggPrimitive' objects>"
        'getShading': None, # (!) real value is "<method 'getShading' of 'panda3d.egg.EggPrimitive' objects>"
        'getSortName': None, # (!) real value is "<method 'getSortName' of 'panda3d.egg.EggPrimitive' objects>"
        'getTexture': None, # (!) real value is "<method 'getTexture' of 'panda3d.egg.EggPrimitive' objects>"
        'getTextures': None, # (!) real value is "<method 'getTextures' of 'panda3d.egg.EggPrimitive' objects>"
        'getVertex': None, # (!) real value is "<method 'getVertex' of 'panda3d.egg.EggPrimitive' objects>"
        'getVertices': None, # (!) real value is "<method 'getVertices' of 'panda3d.egg.EggPrimitive' objects>"
        'get_bface_flag': None, # (!) real value is "<method 'get_bface_flag' of 'panda3d.egg.EggPrimitive' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFDC68CEF60>)>'
        'get_connected_shading': None, # (!) real value is "<method 'get_connected_shading' of 'panda3d.egg.EggPrimitive' objects>"
        'get_material': None, # (!) real value is "<method 'get_material' of 'panda3d.egg.EggPrimitive' objects>"
        'get_num_textures': None, # (!) real value is "<method 'get_num_textures' of 'panda3d.egg.EggPrimitive' objects>"
        'get_num_vertices': None, # (!) real value is "<method 'get_num_vertices' of 'panda3d.egg.EggPrimitive' objects>"
        'get_pool': None, # (!) real value is "<method 'get_pool' of 'panda3d.egg.EggPrimitive' objects>"
        'get_shading': None, # (!) real value is "<method 'get_shading' of 'panda3d.egg.EggPrimitive' objects>"
        'get_sort_name': None, # (!) real value is "<method 'get_sort_name' of 'panda3d.egg.EggPrimitive' objects>"
        'get_texture': None, # (!) real value is "<method 'get_texture' of 'panda3d.egg.EggPrimitive' objects>"
        'get_textures': None, # (!) real value is "<method 'get_textures' of 'panda3d.egg.EggPrimitive' objects>"
        'get_vertex': None, # (!) real value is "<method 'get_vertex' of 'panda3d.egg.EggPrimitive' objects>"
        'get_vertices': None, # (!) real value is "<method 'get_vertices' of 'panda3d.egg.EggPrimitive' objects>"
        'hasMaterial': None, # (!) real value is "<method 'hasMaterial' of 'panda3d.egg.EggPrimitive' objects>"
        'hasNormals': None, # (!) real value is "<method 'hasNormals' of 'panda3d.egg.EggPrimitive' objects>"
        'hasPrimitives': None, # (!) real value is "<method 'hasPrimitives' of 'panda3d.egg.EggPrimitive' objects>"
        'hasTexture': None, # (!) real value is "<method 'hasTexture' of 'panda3d.egg.EggPrimitive' objects>"
        'hasVertexColor': None, # (!) real value is "<method 'hasVertexColor' of 'panda3d.egg.EggPrimitive' objects>"
        'hasVertexNormal': None, # (!) real value is "<method 'hasVertexNormal' of 'panda3d.egg.EggPrimitive' objects>"
        'has_material': None, # (!) real value is "<method 'has_material' of 'panda3d.egg.EggPrimitive' objects>"
        'has_normals': None, # (!) real value is "<method 'has_normals' of 'panda3d.egg.EggPrimitive' objects>"
        'has_primitives': None, # (!) real value is "<method 'has_primitives' of 'panda3d.egg.EggPrimitive' objects>"
        'has_texture': None, # (!) real value is "<method 'has_texture' of 'panda3d.egg.EggPrimitive' objects>"
        'has_vertex_color': None, # (!) real value is "<method 'has_vertex_color' of 'panda3d.egg.EggPrimitive' objects>"
        'has_vertex_normal': None, # (!) real value is "<method 'has_vertex_normal' of 'panda3d.egg.EggPrimitive' objects>"
        'insertVertex': None, # (!) real value is "<method 'insertVertex' of 'panda3d.egg.EggPrimitive' objects>"
        'insert_vertex': None, # (!) real value is "<method 'insert_vertex' of 'panda3d.egg.EggPrimitive' objects>"
        'jointHasPrimitives': None, # (!) real value is "<method 'jointHasPrimitives' of 'panda3d.egg.EggPrimitive' objects>"
        'joint_has_primitives': None, # (!) real value is "<method 'joint_has_primitives' of 'panda3d.egg.EggPrimitive' objects>"
        'makeCopy': None, # (!) real value is "<method 'makeCopy' of 'panda3d.egg.EggPrimitive' objects>"
        'make_copy': None, # (!) real value is "<method 'make_copy' of 'panda3d.egg.EggPrimitive' objects>"
        'material': None, # (!) real value is "<attribute 'material' of 'panda3d.egg.EggPrimitive' objects>"
        'pool': None, # (!) real value is "<attribute 'pool' of 'panda3d.egg.EggPrimitive' objects>"
        'postApplyFlatAttribute': None, # (!) real value is "<method 'postApplyFlatAttribute' of 'panda3d.egg.EggPrimitive' objects>"
        'post_apply_flat_attribute': None, # (!) real value is "<method 'post_apply_flat_attribute' of 'panda3d.egg.EggPrimitive' objects>"
        'removeDoubledVerts': None, # (!) real value is "<method 'removeDoubledVerts' of 'panda3d.egg.EggPrimitive' objects>"
        'removeNonuniqueVerts': None, # (!) real value is "<method 'removeNonuniqueVerts' of 'panda3d.egg.EggPrimitive' objects>"
        'removeVertex': None, # (!) real value is "<method 'removeVertex' of 'panda3d.egg.EggPrimitive' objects>"
        'remove_doubled_verts': None, # (!) real value is "<method 'remove_doubled_verts' of 'panda3d.egg.EggPrimitive' objects>"
        'remove_nonunique_verts': None, # (!) real value is "<method 'remove_nonunique_verts' of 'panda3d.egg.EggPrimitive' objects>"
        'remove_vertex': None, # (!) real value is "<method 'remove_vertex' of 'panda3d.egg.EggPrimitive' objects>"
        'reverseVertexOrdering': None, # (!) real value is "<method 'reverseVertexOrdering' of 'panda3d.egg.EggPrimitive' objects>"
        'reverse_vertex_ordering': None, # (!) real value is "<method 'reverse_vertex_ordering' of 'panda3d.egg.EggPrimitive' objects>"
        'setBfaceFlag': None, # (!) real value is "<method 'setBfaceFlag' of 'panda3d.egg.EggPrimitive' objects>"
        'setMaterial': None, # (!) real value is "<method 'setMaterial' of 'panda3d.egg.EggPrimitive' objects>"
        'setTexture': None, # (!) real value is "<method 'setTexture' of 'panda3d.egg.EggPrimitive' objects>"
        'setVertex': None, # (!) real value is "<method 'setVertex' of 'panda3d.egg.EggPrimitive' objects>"
        'set_bface_flag': None, # (!) real value is "<method 'set_bface_flag' of 'panda3d.egg.EggPrimitive' objects>"
        'set_material': None, # (!) real value is "<method 'set_material' of 'panda3d.egg.EggPrimitive' objects>"
        'set_texture': None, # (!) real value is "<method 'set_texture' of 'panda3d.egg.EggPrimitive' objects>"
        'set_vertex': None, # (!) real value is "<method 'set_vertex' of 'panda3d.egg.EggPrimitive' objects>"
        'shading': None, # (!) real value is "<attribute 'shading' of 'panda3d.egg.EggPrimitive' objects>"
        'sort_name': None, # (!) real value is "<attribute 'sort_name' of 'panda3d.egg.EggPrimitive' objects>"
        'testVrefIntegrity': None, # (!) real value is "<method 'testVrefIntegrity' of 'panda3d.egg.EggPrimitive' objects>"
        'test_vref_integrity': None, # (!) real value is "<method 'test_vref_integrity' of 'panda3d.egg.EggPrimitive' objects>"
        'textures': None, # (!) real value is "<attribute 'textures' of 'panda3d.egg.EggPrimitive' objects>"
        'unifyAttributes': None, # (!) real value is "<method 'unifyAttributes' of 'panda3d.egg.EggPrimitive' objects>"
        'unify_attributes': None, # (!) real value is "<method 'unify_attributes' of 'panda3d.egg.EggPrimitive' objects>"
        'upcastToEggAttributes': None, # (!) real value is "<method 'upcastToEggAttributes' of 'panda3d.egg.EggPrimitive' objects>"
        'upcastToEggNode': None, # (!) real value is "<method 'upcastToEggNode' of 'panda3d.egg.EggPrimitive' objects>"
        'upcastToEggRenderMode': None, # (!) real value is "<method 'upcastToEggRenderMode' of 'panda3d.egg.EggPrimitive' objects>"
        'upcast_to_EggAttributes': None, # (!) real value is "<method 'upcast_to_EggAttributes' of 'panda3d.egg.EggPrimitive' objects>"
        'upcast_to_EggNode': None, # (!) real value is "<method 'upcast_to_EggNode' of 'panda3d.egg.EggPrimitive' objects>"
        'upcast_to_EggRenderMode': None, # (!) real value is "<method 'upcast_to_EggRenderMode' of 'panda3d.egg.EggPrimitive' objects>"
        'vertices': None, # (!) real value is "<attribute 'vertices' of 'panda3d.egg.EggPrimitive' objects>"
        'write': None, # (!) real value is "<method 'write' of 'panda3d.egg.EggPrimitive' objects>"
    }
    SOverall = 1
    SPerFace = 2
    SPerVertex = 3
    SUnknown = 0
    S_overall = 1
    S_per_face = 2
    S_per_vertex = 3
    S_unknown = 0


