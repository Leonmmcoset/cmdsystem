# encoding: utf-8
# module panda3d.egg
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\egg.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import panda3d.core as __panda3d_core


from .EggNamedObject import EggNamedObject

class EggNode(EggNamedObject):
    """
    /**
     * A base class for things that may be directly added into the egg hierarchy.
     * This includes groups, joints, polygons, vertex pools, etc., but does not
     * include things like vertices.
     */
    """
    def applyTexmats(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        apply_texmats(const EggNode self)
        
        /**
         * Applies the texture matrices to the UV's of the vertices that reference
         * them, and then removes the texture matrices from the textures themselves.
         */
        """
        pass

    def apply_texmats(self, const_EggNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        apply_texmats(const EggNode self)
        
        /**
         * Applies the texture matrices to the UV's of the vertices that reference
         * them, and then removes the texture matrices from the textures themselves.
         */
        """
        pass

    def assign(self, const_EggNode_self, const_EggNode_copy): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        assign(const EggNode self, const EggNode copy)
        
        /**
         *
         */
        """
        pass

    def determineAlphaMode(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        determine_alpha_mode(const EggNode self)
        
        /**
         * Walks back up the hierarchy, looking for an EggGroup or EggPrimitive or
         * some such object at this level or above this node that has an alpha_mode
         * other than AM_unspecified.  Returns a valid EggRenderMode pointer if one is
         * found, or NULL otherwise.
         */
        """
        pass

    def determineBin(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        determine_bin(const EggNode self)
        
        /**
         * Walks back up the hierarchy, looking for an EggGroup or EggPrimitive or
         * some such object at this level or above this node that has a bin specified.
         * Returns a valid EggRenderMode pointer if one is found, or NULL otherwise.
         */
        """
        pass

    def determineDecal(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        determine_decal(const EggNode self)
        
        /**
         * Walks back up the hierarchy, looking for an EggGroup at this level or above
         * that has the "decal" flag set.  Returns the value of the decal flag if it
         * is found, or false if it is not.
         *
         * In other words, returns true if the "decal" flag is in effect for the
         * indicated node, false otherwise.
         */
        """
        pass

    def determineDepthOffset(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        determine_depth_offset(const EggNode self)
        
        /**
         * Walks back up the hierarchy, looking for an EggGroup or EggPrimitive or
         * some such object at this level or above this node that has a depth_offset
         * specified.  Returns a valid EggRenderMode pointer if one is found, or NULL
         * otherwise.
         */
        """
        pass

    def determineDepthTestMode(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        determine_depth_test_mode(const EggNode self)
        
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
        determine_depth_write_mode(const EggNode self)
        
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
        determine_draw_order(const EggNode self)
        
        /**
         * Walks back up the hierarchy, looking for an EggGroup or EggPrimitive or
         * some such object at this level or above this node that has a draw_order
         * specified.  Returns a valid EggRenderMode pointer if one is found, or NULL
         * otherwise.
         */
        """
        pass

    def determineIndexed(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        determine_indexed(const EggNode self)
        
        /**
         * Walks back up the hierarchy, looking for an EggGroup at this level or above
         * that has the "indexed" scalar set.  Returns the value of the indexed scalar
         * if it is found, or false if it is not.
         *
         * In other words, returns true if the "indexed" flag is in effect for the
         * indicated node, false otherwise.
         */
        """
        pass

    def determineVisibilityMode(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        determine_visibility_mode(const EggNode self)
        
        /**
         * Walks back up the hierarchy, looking for an EggGroup or EggPrimitive or
         * some such object at this level or above this node that has a
         * visibility_mode other than VM_unspecified.  Returns a valid EggRenderMode
         * pointer if one is found, or NULL otherwise.
         */
        """
        pass

    def determine_alpha_mode(self, const_EggNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        determine_alpha_mode(const EggNode self)
        
        /**
         * Walks back up the hierarchy, looking for an EggGroup or EggPrimitive or
         * some such object at this level or above this node that has an alpha_mode
         * other than AM_unspecified.  Returns a valid EggRenderMode pointer if one is
         * found, or NULL otherwise.
         */
        """
        pass

    def determine_bin(self, const_EggNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        determine_bin(const EggNode self)
        
        /**
         * Walks back up the hierarchy, looking for an EggGroup or EggPrimitive or
         * some such object at this level or above this node that has a bin specified.
         * Returns a valid EggRenderMode pointer if one is found, or NULL otherwise.
         */
        """
        pass

    def determine_decal(self, const_EggNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        determine_decal(const EggNode self)
        
        /**
         * Walks back up the hierarchy, looking for an EggGroup at this level or above
         * that has the "decal" flag set.  Returns the value of the decal flag if it
         * is found, or false if it is not.
         *
         * In other words, returns true if the "decal" flag is in effect for the
         * indicated node, false otherwise.
         */
        """
        pass

    def determine_depth_offset(self, const_EggNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        determine_depth_offset(const EggNode self)
        
        /**
         * Walks back up the hierarchy, looking for an EggGroup or EggPrimitive or
         * some such object at this level or above this node that has a depth_offset
         * specified.  Returns a valid EggRenderMode pointer if one is found, or NULL
         * otherwise.
         */
        """
        pass

    def determine_depth_test_mode(self, const_EggNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        determine_depth_test_mode(const EggNode self)
        
        /**
         * Walks back up the hierarchy, looking for an EggGroup or EggPrimitive or
         * some such object at this level or above this node that has a
         * depth_test_mode other than DTM_unspecified.  Returns a valid EggRenderMode
         * pointer if one is found, or NULL otherwise.
         */
        """
        pass

    def determine_depth_write_mode(self, const_EggNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        determine_depth_write_mode(const EggNode self)
        
        /**
         * Walks back up the hierarchy, looking for an EggGroup or EggPrimitive or
         * some such object at this level or above this node that has a
         * depth_write_mode other than DWM_unspecified.  Returns a valid EggRenderMode
         * pointer if one is found, or NULL otherwise.
         */
        """
        pass

    def determine_draw_order(self, const_EggNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        determine_draw_order(const EggNode self)
        
        /**
         * Walks back up the hierarchy, looking for an EggGroup or EggPrimitive or
         * some such object at this level or above this node that has a draw_order
         * specified.  Returns a valid EggRenderMode pointer if one is found, or NULL
         * otherwise.
         */
        """
        pass

    def determine_indexed(self, const_EggNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        determine_indexed(const EggNode self)
        
        /**
         * Walks back up the hierarchy, looking for an EggGroup at this level or above
         * that has the "indexed" scalar set.  Returns the value of the indexed scalar
         * if it is found, or false if it is not.
         *
         * In other words, returns true if the "indexed" flag is in effect for the
         * indicated node, false otherwise.
         */
        """
        pass

    def determine_visibility_mode(self, const_EggNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        determine_visibility_mode(const EggNode self)
        
        /**
         * Walks back up the hierarchy, looking for an EggGroup or EggPrimitive or
         * some such object at this level or above this node that has a
         * visibility_mode other than VM_unspecified.  Returns a valid EggRenderMode
         * pointer if one is found, or NULL otherwise.
         */
        """
        pass

    def flattenTransforms(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        flatten_transforms(const EggNode self)
        
        /**
         * Removes any transform and instance records from this node in the scene
         * graph and below.  If an instance node is encountered, removes the instance
         * and applies the transform to its vertices, duplicating vertices if
         * necessary.
         *
         * Since this function may result in duplicated vertices, it may be a good
         * idea to call remove_unused_vertices() after calling this.
         */
        """
        pass

    def flatten_transforms(self, const_EggNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        flatten_transforms(const EggNode self)
        
        /**
         * Removes any transform and instance records from this node in the scene
         * graph and below.  If an instance node is encountered, removes the instance
         * and applies the transform to its vertices, duplicating vertices if
         * necessary.
         *
         * Since this function may result in duplicated vertices, it may be a good
         * idea to call remove_unused_vertices() after calling this.
         */
        """
        pass

    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getDepth(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_depth(EggNode self)
        
        /**
         * Returns the number of nodes above this node in the egg hierarchy.
         */
        """
        pass

    def getNodeFrame(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_node_frame(EggNode self)
        
        /**
         * Returns the coordinate frame of the node itself.  This is simply the net
         * product of all transformations up to the root.
         */
        """
        pass

    def getNodeFrameInv(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_node_frame_inv(EggNode self)
        
        /**
         * Returns the inverse of the matrix returned by get_node_frame().  See
         * get_node_frame().
         */
        """
        pass

    def getNodeFrameInvPtr(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_node_frame_inv_ptr(EggNode self)
        
        /**
         * Returns either a NULL pointer or a unique pointer shared by nodes with the
         * same get_node_frame_inv() matrix.
         */
        """
        pass

    def getNodeFramePtr(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_node_frame_ptr(EggNode self)
        
        /**
         * Returns either a NULL pointer or a unique pointer shared by nodes with the
         * same get_node_frame() matrix.
         */
        """
        pass

    def getNodeToVertex(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_node_to_vertex(EggNode self)
        
        /**
         * Returns the transformation matrix suitable for converting vertices in the
         * coordinate space of the node to the appropriate coordinate space for
         * storing in the egg file.  This is the same thing as:
         *
         * get_node_frame() * get_vertex_frame_inv()
         *
         */
        """
        pass

    def getNodeToVertexPtr(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_node_to_vertex_ptr(EggNode self)
        
        /**
         * Returns either a NULL pointer or a unique pointer shared by nodes with the
         * same get_node_to_vertex() matrix.
         */
        """
        pass

    def getParent(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_parent(EggNode self)
        
        /**
         *
         */
        """
        pass

    def getVertexFrame(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_vertex_frame(EggNode self)
        
        /**
         * Returns the coordinate frame of the vertices referenced by primitives at or
         * under this node.  This is not the same as get_node_frame().
         *
         * Generally, vertices in an egg file are stored in the global coordinate
         * space, regardless of the transforms defined at each node.  Thus,
         * get_vertex_frame() will usually return the identity transform (global
         * coordinate space).  However, primitives under an <Instance> entry reference
         * their vertices in the coordinate system under effect at the time of the
         * <Instance>.  Thus, nodes under an <Instance> entry may return this non-
         * identity matrix.
         *
         * Specifically, this may return a non-identity matrix only if
         * is_local_coord() is true.
         */
        """
        pass

    def getVertexFrameInv(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_vertex_frame_inv(EggNode self)
        
        /**
         * Returns the inverse of the matrix returned by get_vertex_frame().  See
         * get_vertex_frame().
         */
        """
        pass

    def getVertexFrameInvPtr(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_vertex_frame_inv_ptr(EggNode self)
        
        /**
         * Returns either a NULL pointer or a unique pointer shared by nodes with the
         * same get_vertex_frame_inv() matrix.
         */
        """
        pass

    def getVertexFramePtr(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_vertex_frame_ptr(EggNode self)
        
        /**
         * Returns either a NULL pointer or a unique pointer shared by nodes with the
         * same get_vertex_frame() matrix.
         */
        """
        pass

    def getVertexToNode(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_vertex_to_node(EggNode self)
        
        /**
         * Returns the transformation matrix suitable for converting the vertices as
         * read from the egg file into the coordinate space of the node.  This is the
         * same thing as:
         *
         * get_vertex_frame() * get_node_frame_inv()
         *
         */
        """
        pass

    def getVertexToNodePtr(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_vertex_to_node_ptr(EggNode self)
        
        /**
         * Returns either a NULL pointer or a unique pointer shared by nodes with the
         * same get_vertex_to_node() matrix.
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_depth(self, EggNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_depth(EggNode self)
        
        /**
         * Returns the number of nodes above this node in the egg hierarchy.
         */
        """
        pass

    def get_node_frame(self, EggNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_node_frame(EggNode self)
        
        /**
         * Returns the coordinate frame of the node itself.  This is simply the net
         * product of all transformations up to the root.
         */
        """
        pass

    def get_node_frame_inv(self, EggNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_node_frame_inv(EggNode self)
        
        /**
         * Returns the inverse of the matrix returned by get_node_frame().  See
         * get_node_frame().
         */
        """
        pass

    def get_node_frame_inv_ptr(self, EggNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_node_frame_inv_ptr(EggNode self)
        
        /**
         * Returns either a NULL pointer or a unique pointer shared by nodes with the
         * same get_node_frame_inv() matrix.
         */
        """
        pass

    def get_node_frame_ptr(self, EggNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_node_frame_ptr(EggNode self)
        
        /**
         * Returns either a NULL pointer or a unique pointer shared by nodes with the
         * same get_node_frame() matrix.
         */
        """
        pass

    def get_node_to_vertex(self, EggNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_node_to_vertex(EggNode self)
        
        /**
         * Returns the transformation matrix suitable for converting vertices in the
         * coordinate space of the node to the appropriate coordinate space for
         * storing in the egg file.  This is the same thing as:
         *
         * get_node_frame() * get_vertex_frame_inv()
         *
         */
        """
        pass

    def get_node_to_vertex_ptr(self, EggNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_node_to_vertex_ptr(EggNode self)
        
        /**
         * Returns either a NULL pointer or a unique pointer shared by nodes with the
         * same get_node_to_vertex() matrix.
         */
        """
        pass

    def get_parent(self, EggNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_parent(EggNode self)
        
        /**
         *
         */
        """
        pass

    def get_vertex_frame(self, EggNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_vertex_frame(EggNode self)
        
        /**
         * Returns the coordinate frame of the vertices referenced by primitives at or
         * under this node.  This is not the same as get_node_frame().
         *
         * Generally, vertices in an egg file are stored in the global coordinate
         * space, regardless of the transforms defined at each node.  Thus,
         * get_vertex_frame() will usually return the identity transform (global
         * coordinate space).  However, primitives under an <Instance> entry reference
         * their vertices in the coordinate system under effect at the time of the
         * <Instance>.  Thus, nodes under an <Instance> entry may return this non-
         * identity matrix.
         *
         * Specifically, this may return a non-identity matrix only if
         * is_local_coord() is true.
         */
        """
        pass

    def get_vertex_frame_inv(self, EggNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_vertex_frame_inv(EggNode self)
        
        /**
         * Returns the inverse of the matrix returned by get_vertex_frame().  See
         * get_vertex_frame().
         */
        """
        pass

    def get_vertex_frame_inv_ptr(self, EggNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_vertex_frame_inv_ptr(EggNode self)
        
        /**
         * Returns either a NULL pointer or a unique pointer shared by nodes with the
         * same get_vertex_frame_inv() matrix.
         */
        """
        pass

    def get_vertex_frame_ptr(self, EggNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_vertex_frame_ptr(EggNode self)
        
        /**
         * Returns either a NULL pointer or a unique pointer shared by nodes with the
         * same get_vertex_frame() matrix.
         */
        """
        pass

    def get_vertex_to_node(self, EggNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_vertex_to_node(EggNode self)
        
        /**
         * Returns the transformation matrix suitable for converting the vertices as
         * read from the egg file into the coordinate space of the node.  This is the
         * same thing as:
         *
         * get_vertex_frame() * get_node_frame_inv()
         *
         */
        """
        pass

    def get_vertex_to_node_ptr(self, EggNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_vertex_to_node_ptr(EggNode self)
        
        /**
         * Returns either a NULL pointer or a unique pointer shared by nodes with the
         * same get_vertex_to_node() matrix.
         */
        """
        pass

    def isAnimMatrix(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_anim_matrix(EggNode self)
        
        /**
         * Returns true if this node represents a table of animation transformation
         * data, false otherwise.
         */
        """
        pass

    def isJoint(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_joint(EggNode self)
        
        /**
         * Returns true if this particular node represents a <Joint> entry or not.
         * This is a handy thing to know since Joints are sorted to the end of their
         * sibling list when writing an egg file.  See EggGroupNode::write().
         */
        """
        pass

    def isLocalCoord(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_local_coord(EggNode self)
        
        /**
         * Returns true if this node's vertices are not in the global coordinate
         * space.  This will be the case if there was an <Instance> node under a
         * transform at or above this node.
         */
        """
        pass

    def isUnderInstance(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_under_instance(EggNode self)
        
        /**
         * Returns true if there is an <Instance> node somewhere in the egg tree at or
         * above this node, false otherwise.
         */
        """
        pass

    def isUnderTransform(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_under_transform(EggNode self)
        
        /**
         * Returns true if there is a <Transform> entry somewhere in the egg tree at
         * or above this node, false otherwise.
         */
        """
        pass

    def is_anim_matrix(self, EggNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_anim_matrix(EggNode self)
        
        /**
         * Returns true if this node represents a table of animation transformation
         * data, false otherwise.
         */
        """
        pass

    def is_joint(self, EggNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_joint(EggNode self)
        
        /**
         * Returns true if this particular node represents a <Joint> entry or not.
         * This is a handy thing to know since Joints are sorted to the end of their
         * sibling list when writing an egg file.  See EggGroupNode::write().
         */
        """
        pass

    def is_local_coord(self, EggNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_local_coord(EggNode self)
        
        /**
         * Returns true if this node's vertices are not in the global coordinate
         * space.  This will be the case if there was an <Instance> node under a
         * transform at or above this node.
         */
        """
        pass

    def is_under_instance(self, EggNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_under_instance(EggNode self)
        
        /**
         * Returns true if there is an <Instance> node somewhere in the egg tree at or
         * above this node, false otherwise.
         */
        """
        pass

    def is_under_transform(self, EggNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_under_transform(EggNode self)
        
        /**
         * Returns true if there is a <Transform> entry somewhere in the egg tree at
         * or above this node, false otherwise.
         */
        """
        pass

    def parseEgg(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        parse_egg(const EggNode self, str egg_syntax)
        
        /**
         * Parses the egg syntax given in the indicate string as if it had been read
         * from the egg file within this object's definition.  Updates the object
         * accordingly.  Returns true if successful, false if there was some parse
         * error or if the object does not support this functionality.
         */
        """
        pass

    def parse_egg(self, const_EggNode_self, str_egg_syntax): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        parse_egg(const EggNode self, str egg_syntax)
        
        /**
         * Parses the egg syntax given in the indicate string as if it had been read
         * from the egg file within this object's definition.  Updates the object
         * accordingly.  Returns true if successful, false if there was some parse
         * error or if the object does not support this functionality.
         */
        """
        pass

    def testUnderIntegrity(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        test_under_integrity(EggNode self)
        """
        pass

    def test_under_integrity(self, EggNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        test_under_integrity(EggNode self)
        """
        pass

    def transform(self, const_EggNode_self, const_LMatrix4d_mat): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        transform(const EggNode self, const LMatrix4d mat)
        
        /**
         * Applies the indicated transformation to the node and all of its
         * descendants.
         */
        """
        pass

    def transformVerticesOnly(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        transform_vertices_only(const EggNode self, const LMatrix4d mat)
        
        /**
         * Applies the indicated transformation only to vertices that appear in global
         * space within vertex pools at this node and below.  Joints and other
         * transforms are not affected, nor are local vertices.
         */
        """
        pass

    def transform_vertices_only(self, const_EggNode_self, const_LMatrix4d_mat): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        transform_vertices_only(const EggNode self, const LMatrix4d mat)
        
        /**
         * Applies the indicated transformation only to vertices that appear in global
         * space within vertex pools at this node and below.  Joints and other
         * transforms are not affected, nor are local vertices.
         */
        """
        pass

    def write(self, EggNode_self, ostream_out, int_indent_level): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        write(EggNode self, ostream out, int indent_level)
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, EggNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        __reduce__(EggNode self)
        """
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    depth = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__doc__': '/**\n * A base class for things that may be directly added into the egg hierarchy.\n * This includes groups, joints, polygons, vertex pools, etc., but does not\n * include things like vertices.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.egg.EggNode' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFDC68CCB20>'
        '__reduce__': None, # (!) real value is "<method '__reduce__' of 'panda3d.egg.EggNode' objects>"
        '__str__': None, # (!) real value is "<slot wrapper '__str__' of 'panda3d.egg.EggNode' objects>"
        'applyTexmats': None, # (!) real value is "<method 'applyTexmats' of 'panda3d.egg.EggNode' objects>"
        'apply_texmats': None, # (!) real value is "<method 'apply_texmats' of 'panda3d.egg.EggNode' objects>"
        'assign': None, # (!) real value is "<method 'assign' of 'panda3d.egg.EggNode' objects>"
        'depth': None, # (!) real value is "<attribute 'depth' of 'panda3d.egg.EggNode' objects>"
        'determineAlphaMode': None, # (!) real value is "<method 'determineAlphaMode' of 'panda3d.egg.EggNode' objects>"
        'determineBin': None, # (!) real value is "<method 'determineBin' of 'panda3d.egg.EggNode' objects>"
        'determineDecal': None, # (!) real value is "<method 'determineDecal' of 'panda3d.egg.EggNode' objects>"
        'determineDepthOffset': None, # (!) real value is "<method 'determineDepthOffset' of 'panda3d.egg.EggNode' objects>"
        'determineDepthTestMode': None, # (!) real value is "<method 'determineDepthTestMode' of 'panda3d.egg.EggNode' objects>"
        'determineDepthWriteMode': None, # (!) real value is "<method 'determineDepthWriteMode' of 'panda3d.egg.EggNode' objects>"
        'determineDrawOrder': None, # (!) real value is "<method 'determineDrawOrder' of 'panda3d.egg.EggNode' objects>"
        'determineIndexed': None, # (!) real value is "<method 'determineIndexed' of 'panda3d.egg.EggNode' objects>"
        'determineVisibilityMode': None, # (!) real value is "<method 'determineVisibilityMode' of 'panda3d.egg.EggNode' objects>"
        'determine_alpha_mode': None, # (!) real value is "<method 'determine_alpha_mode' of 'panda3d.egg.EggNode' objects>"
        'determine_bin': None, # (!) real value is "<method 'determine_bin' of 'panda3d.egg.EggNode' objects>"
        'determine_decal': None, # (!) real value is "<method 'determine_decal' of 'panda3d.egg.EggNode' objects>"
        'determine_depth_offset': None, # (!) real value is "<method 'determine_depth_offset' of 'panda3d.egg.EggNode' objects>"
        'determine_depth_test_mode': None, # (!) real value is "<method 'determine_depth_test_mode' of 'panda3d.egg.EggNode' objects>"
        'determine_depth_write_mode': None, # (!) real value is "<method 'determine_depth_write_mode' of 'panda3d.egg.EggNode' objects>"
        'determine_draw_order': None, # (!) real value is "<method 'determine_draw_order' of 'panda3d.egg.EggNode' objects>"
        'determine_indexed': None, # (!) real value is "<method 'determine_indexed' of 'panda3d.egg.EggNode' objects>"
        'determine_visibility_mode': None, # (!) real value is "<method 'determine_visibility_mode' of 'panda3d.egg.EggNode' objects>"
        'flattenTransforms': None, # (!) real value is "<method 'flattenTransforms' of 'panda3d.egg.EggNode' objects>"
        'flatten_transforms': None, # (!) real value is "<method 'flatten_transforms' of 'panda3d.egg.EggNode' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFDC68CCB20>)>'
        'getDepth': None, # (!) real value is "<method 'getDepth' of 'panda3d.egg.EggNode' objects>"
        'getNodeFrame': None, # (!) real value is "<method 'getNodeFrame' of 'panda3d.egg.EggNode' objects>"
        'getNodeFrameInv': None, # (!) real value is "<method 'getNodeFrameInv' of 'panda3d.egg.EggNode' objects>"
        'getNodeFrameInvPtr': None, # (!) real value is "<method 'getNodeFrameInvPtr' of 'panda3d.egg.EggNode' objects>"
        'getNodeFramePtr': None, # (!) real value is "<method 'getNodeFramePtr' of 'panda3d.egg.EggNode' objects>"
        'getNodeToVertex': None, # (!) real value is "<method 'getNodeToVertex' of 'panda3d.egg.EggNode' objects>"
        'getNodeToVertexPtr': None, # (!) real value is "<method 'getNodeToVertexPtr' of 'panda3d.egg.EggNode' objects>"
        'getParent': None, # (!) real value is "<method 'getParent' of 'panda3d.egg.EggNode' objects>"
        'getVertexFrame': None, # (!) real value is "<method 'getVertexFrame' of 'panda3d.egg.EggNode' objects>"
        'getVertexFrameInv': None, # (!) real value is "<method 'getVertexFrameInv' of 'panda3d.egg.EggNode' objects>"
        'getVertexFrameInvPtr': None, # (!) real value is "<method 'getVertexFrameInvPtr' of 'panda3d.egg.EggNode' objects>"
        'getVertexFramePtr': None, # (!) real value is "<method 'getVertexFramePtr' of 'panda3d.egg.EggNode' objects>"
        'getVertexToNode': None, # (!) real value is "<method 'getVertexToNode' of 'panda3d.egg.EggNode' objects>"
        'getVertexToNodePtr': None, # (!) real value is "<method 'getVertexToNodePtr' of 'panda3d.egg.EggNode' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFDC68CCB20>)>'
        'get_depth': None, # (!) real value is "<method 'get_depth' of 'panda3d.egg.EggNode' objects>"
        'get_node_frame': None, # (!) real value is "<method 'get_node_frame' of 'panda3d.egg.EggNode' objects>"
        'get_node_frame_inv': None, # (!) real value is "<method 'get_node_frame_inv' of 'panda3d.egg.EggNode' objects>"
        'get_node_frame_inv_ptr': None, # (!) real value is "<method 'get_node_frame_inv_ptr' of 'panda3d.egg.EggNode' objects>"
        'get_node_frame_ptr': None, # (!) real value is "<method 'get_node_frame_ptr' of 'panda3d.egg.EggNode' objects>"
        'get_node_to_vertex': None, # (!) real value is "<method 'get_node_to_vertex' of 'panda3d.egg.EggNode' objects>"
        'get_node_to_vertex_ptr': None, # (!) real value is "<method 'get_node_to_vertex_ptr' of 'panda3d.egg.EggNode' objects>"
        'get_parent': None, # (!) real value is "<method 'get_parent' of 'panda3d.egg.EggNode' objects>"
        'get_vertex_frame': None, # (!) real value is "<method 'get_vertex_frame' of 'panda3d.egg.EggNode' objects>"
        'get_vertex_frame_inv': None, # (!) real value is "<method 'get_vertex_frame_inv' of 'panda3d.egg.EggNode' objects>"
        'get_vertex_frame_inv_ptr': None, # (!) real value is "<method 'get_vertex_frame_inv_ptr' of 'panda3d.egg.EggNode' objects>"
        'get_vertex_frame_ptr': None, # (!) real value is "<method 'get_vertex_frame_ptr' of 'panda3d.egg.EggNode' objects>"
        'get_vertex_to_node': None, # (!) real value is "<method 'get_vertex_to_node' of 'panda3d.egg.EggNode' objects>"
        'get_vertex_to_node_ptr': None, # (!) real value is "<method 'get_vertex_to_node_ptr' of 'panda3d.egg.EggNode' objects>"
        'isAnimMatrix': None, # (!) real value is "<method 'isAnimMatrix' of 'panda3d.egg.EggNode' objects>"
        'isJoint': None, # (!) real value is "<method 'isJoint' of 'panda3d.egg.EggNode' objects>"
        'isLocalCoord': None, # (!) real value is "<method 'isLocalCoord' of 'panda3d.egg.EggNode' objects>"
        'isUnderInstance': None, # (!) real value is "<method 'isUnderInstance' of 'panda3d.egg.EggNode' objects>"
        'isUnderTransform': None, # (!) real value is "<method 'isUnderTransform' of 'panda3d.egg.EggNode' objects>"
        'is_anim_matrix': None, # (!) real value is "<method 'is_anim_matrix' of 'panda3d.egg.EggNode' objects>"
        'is_joint': None, # (!) real value is "<method 'is_joint' of 'panda3d.egg.EggNode' objects>"
        'is_local_coord': None, # (!) real value is "<method 'is_local_coord' of 'panda3d.egg.EggNode' objects>"
        'is_under_instance': None, # (!) real value is "<method 'is_under_instance' of 'panda3d.egg.EggNode' objects>"
        'is_under_transform': None, # (!) real value is "<method 'is_under_transform' of 'panda3d.egg.EggNode' objects>"
        'parent': None, # (!) real value is "<attribute 'parent' of 'panda3d.egg.EggNode' objects>"
        'parseEgg': None, # (!) real value is "<method 'parseEgg' of 'panda3d.egg.EggNode' objects>"
        'parse_egg': None, # (!) real value is "<method 'parse_egg' of 'panda3d.egg.EggNode' objects>"
        'testUnderIntegrity': None, # (!) real value is "<method 'testUnderIntegrity' of 'panda3d.egg.EggNode' objects>"
        'test_under_integrity': None, # (!) real value is "<method 'test_under_integrity' of 'panda3d.egg.EggNode' objects>"
        'transform': None, # (!) real value is "<method 'transform' of 'panda3d.egg.EggNode' objects>"
        'transformVerticesOnly': None, # (!) real value is "<method 'transformVerticesOnly' of 'panda3d.egg.EggNode' objects>"
        'transform_vertices_only': None, # (!) real value is "<method 'transform_vertices_only' of 'panda3d.egg.EggNode' objects>"
        'write': None, # (!) real value is "<method 'write' of 'panda3d.egg.EggNode' objects>"
    }


