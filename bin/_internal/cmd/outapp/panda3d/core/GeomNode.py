# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .PandaNode import PandaNode

class GeomNode(PandaNode):
    """
    /**
     * A node that holds Geom objects, renderable pieces of geometry.  This is the
     * primary kind of leaf node in the scene graph; almost all visible objects
     * will be contained in a GeomNode somewhere.
     */
    """
    def addGeom(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_geom(const GeomNode self, Geom geom, const RenderState state)
        
        /**
         * Adds a new Geom to the node.  The geom is given the indicated state (which
         * may be RenderState::make_empty(), to completely inherit its state from the
         * scene graph).
         */
        """
        pass

    def addGeomsFrom(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_geoms_from(const GeomNode self, const GeomNode other)
        
        /**
         * Copies the Geoms (and their associated RenderStates) from the indicated
         * GeomNode into this one.
         */
        """
        pass

    def add_geom(self, const_GeomNode_self, Geom_geom, const_RenderState_state): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_geom(const GeomNode self, Geom geom, const RenderState state)
        
        /**
         * Adds a new Geom to the node.  The geom is given the indicated state (which
         * may be RenderState::make_empty(), to completely inherit its state from the
         * scene graph).
         */
        """
        pass

    def add_geoms_from(self, const_GeomNode_self, const_GeomNode_other): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_geoms_from(const GeomNode self, const GeomNode other)
        
        /**
         * Copies the Geoms (and their associated RenderStates) from the indicated
         * GeomNode into this one.
         */
        """
        pass

    def checkValid(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        check_valid(GeomNode self)
        
        /**
         * Verifies that the each Geom within the GeomNode reference vertices that
         * actually exist within its GeomVertexData.  Returns true if the GeomNode
         * appears to be valid, false otherwise.
         */
        """
        pass

    def check_valid(self, GeomNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        check_valid(GeomNode self)
        
        /**
         * Verifies that the each Geom within the GeomNode reference vertices that
         * actually exist within its GeomVertexData.  Returns true if the GeomNode
         * appears to be valid, false otherwise.
         */
        """
        pass

    def decompose(self, const_GeomNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        decompose(const GeomNode self)
        
        /**
         * Calls decompose() on each Geom with the GeomNode.  This decomposes higher-
         * order primitive types, like triangle strips, into lower-order types like
         * indexed triangles.  Normally there is no reason to do this, but it can be
         * useful as an early preprocessing step, to allow a later call to unify() to
         * proceed more quickly.
         *
         * See also SceneGraphReducer::decompose(), which is the normal way this is
         * called.
         */
        """
        pass

    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getDefaultCollideMask(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_default_collide_mask()
        
        /**
         * Returns the default into_collide_mask assigned to new GeomNodes.
         */
        """
        pass

    def getGeom(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_geom(GeomNode self, int n)
        
        /**
         * Returns the nth geom of the node.  This object should not be modified,
         * since the same object might be shared between multiple different GeomNodes,
         * but see modify_geom().
         */
        """
        pass

    def getGeoms(self, *args, **kwargs): # real signature unknown
        pass

    def getGeomState(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_geom_state(GeomNode self, int n)
        
        /**
         * Returns the RenderState associated with the nth geom of the node.  This is
         * just the RenderState directly associated with the Geom; the actual state in
         * which the Geom is rendered will also be affected by RenderStates that
         * appear on the scene graph in nodes above this GeomNode.
         */
        """
        pass

    def getGeomStates(self, *args, **kwargs): # real signature unknown
        pass

    def getNumGeoms(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_geoms(GeomNode self)
        
        /**
         * Returns the number of geoms in the node.
         */
        """
        pass

    def getPreserved(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_preserved(GeomNode self)
        
        /**
         * Returns the "preserved" flag.  When this is true, the GeomNode will be left
         * untouched by any flatten operations.
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_default_collide_mask(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_default_collide_mask()
        
        /**
         * Returns the default into_collide_mask assigned to new GeomNodes.
         */
        """
        pass

    def get_geom(self, GeomNode_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_geom(GeomNode self, int n)
        
        /**
         * Returns the nth geom of the node.  This object should not be modified,
         * since the same object might be shared between multiple different GeomNodes,
         * but see modify_geom().
         */
        """
        pass

    def get_geoms(self, *args, **kwargs): # real signature unknown
        pass

    def get_geom_state(self, GeomNode_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_geom_state(GeomNode self, int n)
        
        /**
         * Returns the RenderState associated with the nth geom of the node.  This is
         * just the RenderState directly associated with the Geom; the actual state in
         * which the Geom is rendered will also be affected by RenderStates that
         * appear on the scene graph in nodes above this GeomNode.
         */
        """
        pass

    def get_geom_states(self, *args, **kwargs): # real signature unknown
        pass

    def get_num_geoms(self, GeomNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_geoms(GeomNode self)
        
        /**
         * Returns the number of geoms in the node.
         */
        """
        pass

    def get_preserved(self, GeomNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_preserved(GeomNode self)
        
        /**
         * Returns the "preserved" flag.  When this is true, the GeomNode will be left
         * untouched by any flatten operations.
         */
        """
        pass

    def modifyGeom(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        modify_geom(const GeomNode self, int n)
        
        /**
         * Returns the nth geom of the node, suitable for modifying it.  If the nth
         * Geom has multiple reference counts to it, reassigns it to an identical copy
         * first, and returns the new copy--this provides a "copy on write" that
         * ensures that the Geom that is returned is unique to this GeomNode and is
         * not shared with any other GeomNodes.
         *
         * Note that if this method is called in a downstream stage (for instance,
         * during cull or draw), then it will propagate the new list of Geoms upstream
         * all the way to pipeline stage 0, which may step on changes that were made
         * independently in pipeline stage 0. Use with caution.
         */
        """
        pass

    def modifyGeoms(self, *args, **kwargs): # real signature unknown
        pass

    def modify_geom(self, const_GeomNode_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        modify_geom(const GeomNode self, int n)
        
        /**
         * Returns the nth geom of the node, suitable for modifying it.  If the nth
         * Geom has multiple reference counts to it, reassigns it to an identical copy
         * first, and returns the new copy--this provides a "copy on write" that
         * ensures that the Geom that is returned is unique to this GeomNode and is
         * not shared with any other GeomNodes.
         *
         * Note that if this method is called in a downstream stage (for instance,
         * during cull or draw), then it will propagate the new list of Geoms upstream
         * all the way to pipeline stage 0, which may step on changes that were made
         * independently in pipeline stage 0. Use with caution.
         */
        """
        pass

    def modify_geoms(self, *args, **kwargs): # real signature unknown
        pass

    def removeAllGeoms(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        remove_all_geoms(const GeomNode self)
        
        /**
         * Removes all the geoms from the node at once.
         */
        """
        pass

    def removeGeom(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        remove_geom(const GeomNode self, int n)
        
        /**
         * Removes the nth geom from the node.
         */
        """
        pass

    def remove_all_geoms(self, const_GeomNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        remove_all_geoms(const GeomNode self)
        
        /**
         * Removes all the geoms from the node at once.
         */
        """
        pass

    def remove_geom(self, const_GeomNode_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        remove_geom(const GeomNode self, int n)
        
        /**
         * Removes the nth geom from the node.
         */
        """
        pass

    def setGeom(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_geom(const GeomNode self, int n, Geom geom)
        
        /**
         * Replaces the nth Geom of the node with a new pointer.  There must already
         * be a Geom in this slot.
         *
         * Note that if this method is called in a downstream stage (for instance,
         * during cull or draw), then it will propagate the new list of Geoms upstream
         * all the way to pipeline stage 0, which may step on changes that were made
         * independently in pipeline stage 0. Use with caution.
         */
        """
        pass

    def setGeomState(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_geom_state(const GeomNode self, int n, const RenderState state)
        
        /**
         * Changes the RenderState associated with the nth geom of the node.  This is
         * just the RenderState directly associated with the Geom; the actual state in
         * which the Geom is rendered will also be affected by RenderStates that
         * appear on the scene graph in nodes above this GeomNode.
         *
         * Note that if this method is called in a downstream stage (for instance,
         * during cull or draw), then it will propagate the new list of Geoms upstream
         * all the way to pipeline stage 0, which may step on changes that were made
         * independently in pipeline stage 0. Use with caution.
         */
        """
        pass

    def setPreserved(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_preserved(const GeomNode self, bool value)
        
        /**
         * Sets the "preserved" flag.  When this is true, the GeomNode will be left
         * untouched by any flatten operations.
         */
        """
        pass

    def set_geom(self, const_GeomNode_self, int_n, Geom_geom): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_geom(const GeomNode self, int n, Geom geom)
        
        /**
         * Replaces the nth Geom of the node with a new pointer.  There must already
         * be a Geom in this slot.
         *
         * Note that if this method is called in a downstream stage (for instance,
         * during cull or draw), then it will propagate the new list of Geoms upstream
         * all the way to pipeline stage 0, which may step on changes that were made
         * independently in pipeline stage 0. Use with caution.
         */
        """
        pass

    def set_geom_state(self, const_GeomNode_self, int_n, const_RenderState_state): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_geom_state(const GeomNode self, int n, const RenderState state)
        
        /**
         * Changes the RenderState associated with the nth geom of the node.  This is
         * just the RenderState directly associated with the Geom; the actual state in
         * which the Geom is rendered will also be affected by RenderStates that
         * appear on the scene graph in nodes above this GeomNode.
         *
         * Note that if this method is called in a downstream stage (for instance,
         * during cull or draw), then it will propagate the new list of Geoms upstream
         * all the way to pipeline stage 0, which may step on changes that were made
         * independently in pipeline stage 0. Use with caution.
         */
        """
        pass

    def set_preserved(self, const_GeomNode_self, bool_value): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_preserved(const GeomNode self, bool value)
        
        /**
         * Sets the "preserved" flag.  When this is true, the GeomNode will be left
         * untouched by any flatten operations.
         */
        """
        pass

    def unify(self, const_GeomNode_self, int_max_indices, bool_preserve_order): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        unify(const GeomNode self, int max_indices, bool preserve_order)
        
        /**
         * Attempts to unify all of the Geoms contained within this node into a single
         * Geom, or at least as few Geoms as possible.  In turn, the individual
         * GeomPrimitives contained within each resulting Geom are also unified.  The
         * goal is to reduce the number of GeomPrimitives within the node as far as
         * possible.  This may result in composite primitives, such as triangle strips
         * and triangle fans, being decomposed into triangles.  See also
         * Geom::unify().
         *
         * max_indices represents the maximum number of indices that will be put in
         * any one GeomPrimitive.  If preserve_order is true, then the primitives will
         * not be reordered during the operation, even if this results in a suboptimal
         * result.
         *
         * In order for this to be successful, the primitives must reference the same
         * GeomVertexData, have the same fundamental primitive type, and have
         * compatible shade models.
         */
        """
        pass

    def writeGeoms(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        write_geoms(GeomNode self, ostream out, int indent_level)
        
        /**
         * Writes a short description of all the Geoms in the node.
         */
        """
        pass

    def writeVerbose(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        write_verbose(GeomNode self, ostream out, int indent_level)
        
        /**
         * Writes a detailed description of all the Geoms in the node.
         */
        """
        pass

    def write_geoms(self, GeomNode_self, ostream_out, int_indent_level): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        write_geoms(GeomNode self, ostream out, int indent_level)
        
        /**
         * Writes a short description of all the Geoms in the node.
         */
        """
        pass

    def write_verbose(self, GeomNode_self, ostream_out, int_indent_level): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        write_verbose(GeomNode self, ostream out, int indent_level)
        
        /**
         * Writes a detailed description of all the Geoms in the node.
         */
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    default_collide_mask = None # (!) real value is ' 0000 0000 0001 0000 0000 0000 0000 0000'
    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__doc__': '/**\n * A node that holds Geom objects, renderable pieces of geometry.  This is the\n * primary kind of leaf node in the scene graph; almost all visible objects\n * will be contained in a GeomNode somewhere.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.GeomNode' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE295CE0>'
        'addGeom': None, # (!) real value is "<method 'addGeom' of 'panda3d.core.GeomNode' objects>"
        'addGeomsFrom': None, # (!) real value is "<method 'addGeomsFrom' of 'panda3d.core.GeomNode' objects>"
        'add_geom': None, # (!) real value is "<method 'add_geom' of 'panda3d.core.GeomNode' objects>"
        'add_geoms_from': None, # (!) real value is "<method 'add_geoms_from' of 'panda3d.core.GeomNode' objects>"
        'checkValid': None, # (!) real value is "<method 'checkValid' of 'panda3d.core.GeomNode' objects>"
        'check_valid': None, # (!) real value is "<method 'check_valid' of 'panda3d.core.GeomNode' objects>"
        'decompose': None, # (!) real value is "<method 'decompose' of 'panda3d.core.GeomNode' objects>"
        'default_collide_mask': None, # (!) real value is "<attribute 'default_collide_mask' of 'panda3d.core.GeomNode'>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE295CE0>)>'
        'getDefaultCollideMask': None, # (!) real value is '<staticmethod(<built-in method getDefaultCollideMask of type object at 0x00007FFCFE295CE0>)>'
        'getGeom': None, # (!) real value is "<method 'getGeom' of 'panda3d.core.GeomNode' objects>"
        'getGeomState': None, # (!) real value is "<method 'getGeomState' of 'panda3d.core.GeomNode' objects>"
        'getGeomStates': None, # (!) real value is "<method 'getGeomStates' of 'panda3d.core.GeomNode' objects>"
        'getGeoms': None, # (!) real value is "<method 'getGeoms' of 'panda3d.core.GeomNode' objects>"
        'getNumGeoms': None, # (!) real value is "<method 'getNumGeoms' of 'panda3d.core.GeomNode' objects>"
        'getPreserved': None, # (!) real value is "<method 'getPreserved' of 'panda3d.core.GeomNode' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE295CE0>)>'
        'get_default_collide_mask': None, # (!) real value is '<staticmethod(<built-in method get_default_collide_mask of type object at 0x00007FFCFE295CE0>)>'
        'get_geom': None, # (!) real value is "<method 'get_geom' of 'panda3d.core.GeomNode' objects>"
        'get_geom_state': None, # (!) real value is "<method 'get_geom_state' of 'panda3d.core.GeomNode' objects>"
        'get_geom_states': None, # (!) real value is "<method 'get_geom_states' of 'panda3d.core.GeomNode' objects>"
        'get_geoms': None, # (!) real value is "<method 'get_geoms' of 'panda3d.core.GeomNode' objects>"
        'get_num_geoms': None, # (!) real value is "<method 'get_num_geoms' of 'panda3d.core.GeomNode' objects>"
        'get_preserved': None, # (!) real value is "<method 'get_preserved' of 'panda3d.core.GeomNode' objects>"
        'modifyGeom': None, # (!) real value is "<method 'modifyGeom' of 'panda3d.core.GeomNode' objects>"
        'modifyGeoms': None, # (!) real value is "<method 'modifyGeoms' of 'panda3d.core.GeomNode' objects>"
        'modify_geom': None, # (!) real value is "<method 'modify_geom' of 'panda3d.core.GeomNode' objects>"
        'modify_geoms': None, # (!) real value is "<method 'modify_geoms' of 'panda3d.core.GeomNode' objects>"
        'removeAllGeoms': None, # (!) real value is "<method 'removeAllGeoms' of 'panda3d.core.GeomNode' objects>"
        'removeGeom': None, # (!) real value is "<method 'removeGeom' of 'panda3d.core.GeomNode' objects>"
        'remove_all_geoms': None, # (!) real value is "<method 'remove_all_geoms' of 'panda3d.core.GeomNode' objects>"
        'remove_geom': None, # (!) real value is "<method 'remove_geom' of 'panda3d.core.GeomNode' objects>"
        'setGeom': None, # (!) real value is "<method 'setGeom' of 'panda3d.core.GeomNode' objects>"
        'setGeomState': None, # (!) real value is "<method 'setGeomState' of 'panda3d.core.GeomNode' objects>"
        'setPreserved': None, # (!) real value is "<method 'setPreserved' of 'panda3d.core.GeomNode' objects>"
        'set_geom': None, # (!) real value is "<method 'set_geom' of 'panda3d.core.GeomNode' objects>"
        'set_geom_state': None, # (!) real value is "<method 'set_geom_state' of 'panda3d.core.GeomNode' objects>"
        'set_preserved': None, # (!) real value is "<method 'set_preserved' of 'panda3d.core.GeomNode' objects>"
        'unify': None, # (!) real value is "<method 'unify' of 'panda3d.core.GeomNode' objects>"
        'writeGeoms': None, # (!) real value is "<method 'writeGeoms' of 'panda3d.core.GeomNode' objects>"
        'writeVerbose': None, # (!) real value is "<method 'writeVerbose' of 'panda3d.core.GeomNode' objects>"
        'write_geoms': None, # (!) real value is "<method 'write_geoms' of 'panda3d.core.GeomNode' objects>"
        'write_verbose': None, # (!) real value is "<method 'write_verbose' of 'panda3d.core.GeomNode' objects>"
    }


