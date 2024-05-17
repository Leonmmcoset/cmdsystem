# encoding: utf-8
# module panda3d.egg
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\egg.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import panda3d.core as __panda3d_core


from .EggNode import EggNode

class EggVertexPool(EggNode):
    """
    /**
     * A collection of vertices.  There may be any number of vertex pools in a
     * single egg structure.  The vertices in a single pool need not necessarily
     * have any connection to each other, but it is necessary that any one
     * primitive (e.g.  a polygon) must pull all its vertices from the same pool.
     *
     * An EggVertexPool is an STL-style container of pointers to EggVertex's.
     * Functions add_vertex() and remove_vertex() are provided to manipulate the
     * list.  The list may also be operated on (read-only) via iterators and
     * begin()/end().
     */
    """
    def addUnusedVerticesToPrim(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_unused_vertices_to_prim(const EggVertexPool self, EggPrimitive prim)
        
        /**
         * Adds all of the unused vertices in this vertex pool to the indicated
         * primitive, in ascending order.
         */
        """
        pass

    def addVertex(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_vertex(const EggVertexPool self, EggVertex vertex, int index)
        
        // add_vertex() adds a freshly-allocated vertex.  It is up to the user to
        // allocate the vertex.
        
        /**
         * Adds the indicated vertex to the pool.  It is an error if the vertex is
         * already a member of this or any other pool.  The vertex must have been
         * allocated from the free store; its pointer will now be owned by the vertex
         * pool.  If the index number is supplied, tries to assign that index number;
         * it is an error if the index number is already in use.
         *
         * It is possible that a forward reference to this vertex was requested in the
         * past; if so, the data from the supplied vertex is copied onto the forward
         * reference, which becomes the actual vertex.  In this case, a different
         * pointer is saved (and returned) than the one actually passed in.  In the
         * usual case, however, the vertex pointer passed in is the one that is saved
         * in the vertex pool and returned from this method.
         */
        """
        pass

    def add_unused_vertices_to_prim(self, const_EggVertexPool_self, EggPrimitive_prim): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_unused_vertices_to_prim(const EggVertexPool self, EggPrimitive prim)
        
        /**
         * Adds all of the unused vertices in this vertex pool to the indicated
         * primitive, in ascending order.
         */
        """
        pass

    def add_vertex(self, const_EggVertexPool_self, EggVertex_vertex, int_index): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_vertex(const EggVertexPool self, EggVertex vertex, int index)
        
        // add_vertex() adds a freshly-allocated vertex.  It is up to the user to
        // allocate the vertex.
        
        /**
         * Adds the indicated vertex to the pool.  It is an error if the vertex is
         * already a member of this or any other pool.  The vertex must have been
         * allocated from the free store; its pointer will now be owned by the vertex
         * pool.  If the index number is supplied, tries to assign that index number;
         * it is an error if the index number is already in use.
         *
         * It is possible that a forward reference to this vertex was requested in the
         * past; if so, the data from the supplied vertex is copied onto the forward
         * reference, which becomes the actual vertex.  In this case, a different
         * pointer is saved (and returned) than the one actually passed in.  In the
         * usual case, however, the vertex pointer passed in is the one that is saved
         * in the vertex pool and returned from this method.
         */
        """
        pass

    def createUniqueVertex(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        create_unique_vertex(const EggVertexPool self, const EggVertex copy)
        
        // create_unique_vertex() creates a new vertex if there is not already one
        // identical to the indicated vertex, or returns the existing one if there
        // is.
        
        /**
         * Creates a new vertex in the pool that is a copy of the indicated one and
         * returns it.  If there is already a vertex in the pool like the indicated
         * one, simply returns that one.
         */
        """
        pass

    def create_unique_vertex(self, const_EggVertexPool_self, const_EggVertex_copy): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        create_unique_vertex(const EggVertexPool self, const EggVertex copy)
        
        // create_unique_vertex() creates a new vertex if there is not already one
        // identical to the indicated vertex, or returns the existing one if there
        // is.
        
        /**
         * Creates a new vertex in the pool that is a copy of the indicated one and
         * returns it.  If there is already a vertex in the pool like the indicated
         * one, simply returns that one.
         */
        """
        pass

    def findMatchingVertex(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        find_matching_vertex(const EggVertexPool self, const EggVertex copy)
        
        /**
         * If the EggVertexPool already has a vertex matching the indicated vertex,
         * returns it; otherwise, returns NULL.  This is similar to
         * create_unique_vertex() except that a new vertex is never created.
         */
        """
        pass

    def find_matching_vertex(self, const_EggVertexPool_self, const_EggVertex_copy): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        find_matching_vertex(const EggVertexPool self, const EggVertex copy)
        
        /**
         * If the EggVertexPool already has a vertex matching the indicated vertex,
         * returns it; otherwise, returns NULL.  This is similar to
         * create_unique_vertex() except that a new vertex is never created.
         */
        """
        pass

    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getForwardVertex(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_forward_vertex(const EggVertexPool self, int index)
        
        // Returns a forward reference if there is no such vertex.
        
        /**
         * Returns the vertex in the pool with the indicated index number.  If there
         * is not a vertex in the pool with the indicated index number, creates a
         * special forward-reference EggVertex that has no data, on the assumption
         * that the vertex pool has not yet been fully read and more data will be
         * available later.
         */
        """
        pass

    def getHighestIndex(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_highest_index(EggVertexPool self)
        
        // Returns 0 if the pool is empty.
        
        /**
         * Returns the highest index number used by any vertex in the pool (except
         * forward references).  Returns -1 if the pool is empty.
         */
        """
        pass

    def getNumDimensions(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_dimensions(EggVertexPool self)
        
        /**
         * Returns the maximum number of dimensions used by any vertex in the pool.
         */
        """
        pass

    def getVertex(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_vertex(EggVertexPool self, int index)
        
        // Returns NULL if there is no such vertex.
        
        /**
         * Returns the vertex in the pool with the indicated index number, or NULL if
         * no vertices have that index number.
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_forward_vertex(self, const_EggVertexPool_self, int_index): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_forward_vertex(const EggVertexPool self, int index)
        
        // Returns a forward reference if there is no such vertex.
        
        /**
         * Returns the vertex in the pool with the indicated index number.  If there
         * is not a vertex in the pool with the indicated index number, creates a
         * special forward-reference EggVertex that has no data, on the assumption
         * that the vertex pool has not yet been fully read and more data will be
         * available later.
         */
        """
        pass

    def get_highest_index(self, EggVertexPool_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_highest_index(EggVertexPool self)
        
        // Returns 0 if the pool is empty.
        
        /**
         * Returns the highest index number used by any vertex in the pool (except
         * forward references).  Returns -1 if the pool is empty.
         */
        """
        pass

    def get_num_dimensions(self, EggVertexPool_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_dimensions(EggVertexPool self)
        
        /**
         * Returns the maximum number of dimensions used by any vertex in the pool.
         */
        """
        pass

    def get_vertex(self, EggVertexPool_self, int_index): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_vertex(EggVertexPool self, int index)
        
        // Returns NULL if there is no such vertex.
        
        /**
         * Returns the vertex in the pool with the indicated index number, or NULL if
         * no vertices have that index number.
         */
        """
        pass

    def hasAux(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_aux(EggVertexPool self)
        
        /**
         * Returns true if any vertex in the pool has auxiliary data defined, false if
         * none of them do.
         */
        """
        pass

    def hasColors(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_colors(EggVertexPool self)
        
        /**
         * Returns true if any vertex in the pool has a color defined, false if none
         * of them do.
         */
        """
        pass

    def hasDefinedVertices(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_defined_vertices(EggVertexPool self)
        
        /**
         * Returns true if any vertices in the pool are fully defined vertices, false
         * if all vertices are forward references.
         */
        """
        pass

    def hasForwardVertices(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_forward_vertices(EggVertexPool self)
        
        /**
         * Returns true if any vertices in the pool are undefined forward-reference
         * vertices, false if all vertices are defined.
         */
        """
        pass

    def hasNonwhiteColors(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_nonwhite_colors(EggVertexPool self)
        
        /**
         * Returns true if any vertex in the pool has a color defined other than
         * white, false if no vertices have colors, or if all colors are white.
         */
        """
        pass

    def hasNormals(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_normals(EggVertexPool self)
        
        /**
         * Returns true if any vertex in the pool has a normal defined, false if none
         * of them do.
         */
        """
        pass

    def hasUvs(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_uvs(EggVertexPool self)
        
        /**
         * Returns true if any vertex in the pool has a uv defined, false if none of
         * them do.
         */
        """
        pass

    def hasVertex(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_vertex(EggVertexPool self, int index)
        
        /**
         * Returns true if the indicated vertex has been defined in the vertex pool,
         * false otherwise.  This does not include forward references.
         */
        """
        pass

    def has_aux(self, EggVertexPool_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_aux(EggVertexPool self)
        
        /**
         * Returns true if any vertex in the pool has auxiliary data defined, false if
         * none of them do.
         */
        """
        pass

    def has_colors(self, EggVertexPool_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_colors(EggVertexPool self)
        
        /**
         * Returns true if any vertex in the pool has a color defined, false if none
         * of them do.
         */
        """
        pass

    def has_defined_vertices(self, EggVertexPool_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_defined_vertices(EggVertexPool self)
        
        /**
         * Returns true if any vertices in the pool are fully defined vertices, false
         * if all vertices are forward references.
         */
        """
        pass

    def has_forward_vertices(self, EggVertexPool_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_forward_vertices(EggVertexPool self)
        
        /**
         * Returns true if any vertices in the pool are undefined forward-reference
         * vertices, false if all vertices are defined.
         */
        """
        pass

    def has_nonwhite_colors(self, EggVertexPool_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_nonwhite_colors(EggVertexPool self)
        
        /**
         * Returns true if any vertex in the pool has a color defined other than
         * white, false if no vertices have colors, or if all colors are white.
         */
        """
        pass

    def has_normals(self, EggVertexPool_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_normals(EggVertexPool self)
        
        /**
         * Returns true if any vertex in the pool has a normal defined, false if none
         * of them do.
         */
        """
        pass

    def has_uvs(self, EggVertexPool_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_uvs(EggVertexPool self)
        
        /**
         * Returns true if any vertex in the pool has a uv defined, false if none of
         * them do.
         */
        """
        pass

    def has_vertex(self, EggVertexPool_self, int_index): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_vertex(EggVertexPool self, int index)
        
        /**
         * Returns true if the indicated vertex has been defined in the vertex pool,
         * false otherwise.  This does not include forward references.
         */
        """
        pass

    def makeNewVertex(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        make_new_vertex(const EggVertexPool self)
        make_new_vertex(const EggVertexPool self, const LPoint2d pos)
        make_new_vertex(const EggVertexPool self, const LPoint4d pos)
        make_new_vertex(const EggVertexPool self, const LPoint3d pos)
        make_new_vertex(const EggVertexPool self, double pos)
        
        // make_new_vertex() allocates and returns a new vertex from the pool.
        
        /**
         * Allocates and returns a new vertex from the pool.  This is one of three
         * ways to add new vertices to a vertex pool.
         */
        
        /**
         * Allocates and returns a new vertex from the pool.  This is one of three
         * ways to add new vertices to a vertex pool.
         *
         * This flavor of make_new_vertex() explicitly sets the vertex position as it
         * is allocated.  It does not attempt to share vertices.
         */
        
        /**
         * Allocates and returns a new vertex from the pool.  This is one of three
         * ways to add new vertices to a vertex pool.
         *
         * This flavor of make_new_vertex() explicitly sets the vertex position as it
         * is allocated.  It does not attempt to share vertices.
         */
        
        /**
         * Allocates and returns a new vertex from the pool.  This is one of three
         * ways to add new vertices to a vertex pool.
         *
         * This flavor of make_new_vertex() explicitly sets the vertex position as it
         * is allocated.  It does not attempt to share vertices.
         */
        
        /**
         * Allocates and returns a new vertex from the pool.  This is one of three
         * ways to add new vertices to a vertex pool.
         *
         * This flavor of make_new_vertex() explicitly sets the vertex position as it
         * is allocated.  It does not attempt to share vertices.
         */
        """
        pass

    def make_new_vertex(self, const_EggVertexPool_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        make_new_vertex(const EggVertexPool self)
        make_new_vertex(const EggVertexPool self, const LPoint2d pos)
        make_new_vertex(const EggVertexPool self, const LPoint4d pos)
        make_new_vertex(const EggVertexPool self, const LPoint3d pos)
        make_new_vertex(const EggVertexPool self, double pos)
        
        // make_new_vertex() allocates and returns a new vertex from the pool.
        
        /**
         * Allocates and returns a new vertex from the pool.  This is one of three
         * ways to add new vertices to a vertex pool.
         */
        
        /**
         * Allocates and returns a new vertex from the pool.  This is one of three
         * ways to add new vertices to a vertex pool.
         *
         * This flavor of make_new_vertex() explicitly sets the vertex position as it
         * is allocated.  It does not attempt to share vertices.
         */
        
        /**
         * Allocates and returns a new vertex from the pool.  This is one of three
         * ways to add new vertices to a vertex pool.
         *
         * This flavor of make_new_vertex() explicitly sets the vertex position as it
         * is allocated.  It does not attempt to share vertices.
         */
        
        /**
         * Allocates and returns a new vertex from the pool.  This is one of three
         * ways to add new vertices to a vertex pool.
         *
         * This flavor of make_new_vertex() explicitly sets the vertex position as it
         * is allocated.  It does not attempt to share vertices.
         */
        
        /**
         * Allocates and returns a new vertex from the pool.  This is one of three
         * ways to add new vertices to a vertex pool.
         *
         * This flavor of make_new_vertex() explicitly sets the vertex position as it
         * is allocated.  It does not attempt to share vertices.
         */
        """
        pass

    def removeUnusedVertices(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        remove_unused_vertices(const EggVertexPool self)
        
        /**
         * Removes all vertices from the pool that are not referenced by at least one
         * primitive.  Also collapses together equivalent vertices, and renumbers all
         * vertices after the operation so their indices are consecutive, beginning at
         * zero.  Returns the number of vertices removed.
         */
        """
        pass

    def removeVertex(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        remove_vertex(const EggVertexPool self, EggVertex vertex)
        
        /**
         * Removes the vertex from the pool.  It is an error if the vertex is not
         * already a member of the pool.
         */
        """
        pass

    def remove_unused_vertices(self, const_EggVertexPool_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        remove_unused_vertices(const EggVertexPool self)
        
        /**
         * Removes all vertices from the pool that are not referenced by at least one
         * primitive.  Also collapses together equivalent vertices, and renumbers all
         * vertices after the operation so their indices are consecutive, beginning at
         * zero.  Returns the number of vertices removed.
         */
        """
        pass

    def remove_vertex(self, const_EggVertexPool_self, EggVertex_vertex): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        remove_vertex(const EggVertexPool self, EggVertex vertex)
        
        /**
         * Removes the vertex from the pool.  It is an error if the vertex is not
         * already a member of the pool.
         */
        """
        pass

    def setHighestIndex(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_highest_index(const EggVertexPool self, int highest_index)
        
        /**
         * Artificially changes the "highest index number", so that a newly created
         * vertex will begin at this number plus 1.  This can be used to default a
         * vertex pool to start counting at 1 (or any other index number), instead of
         * the default of 0.  Use with caution.
         */
        """
        pass

    def set_highest_index(self, const_EggVertexPool_self, int_highest_index): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_highest_index(const EggVertexPool self, int highest_index)
        
        /**
         * Artificially changes the "highest index number", so that a newly created
         * vertex will begin at this number plus 1.  This can be used to default a
         * vertex pool to start counting at 1 (or any other index number), instead of
         * the default of 0.  Use with caution.
         */
        """
        pass

    def sortByExternalIndex(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        sort_by_external_index(const EggVertexPool self)
        
        /**
         * Re-orders (and re-numbers) the vertices in this vertex pool so that they
         * appear in increasing order by the optional external_index that has been
         * assigned to each vertex.
         */
        """
        pass

    def sort_by_external_index(self, const_EggVertexPool_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        sort_by_external_index(const EggVertexPool self)
        
        /**
         * Re-orders (and re-numbers) the vertices in this vertex pool so that they
         * appear in increasing order by the optional external_index that has been
         * assigned to each vertex.
         */
        """
        pass

    def transform(self, const_EggVertexPool_self, const_LMatrix4d_mat): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        transform(const EggVertexPool self, const LMatrix4d mat)
        
        /**
         * Applies the indicated transformation matrix to all the vertices.  However,
         * vertices that are attached to primitives that believe their vertices are in
         * a local coordinate system are transformed only by the scale and rotation
         * component.  If a vertex happens to be attached both to a local and a global
         * primitive, and the transformation includes a translation component, the
         * vertex will be split.
         */
        """
        pass

    def __copy__(self, *args, **kwargs): # real signature unknown
        pass

    def __deepcopy__(self, *args, **kwargs): # real signature unknown
        pass

    def __getitem__(self, *args, **kwargs): # real signature unknown
        """ Return self[key]. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __len__(self, *args, **kwargs): # real signature unknown
        """ Return len(self). """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.egg.EggVertexPool' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.egg.EggVertexPool' objects>"
        '__doc__': "/**\n * A collection of vertices.  There may be any number of vertex pools in a\n * single egg structure.  The vertices in a single pool need not necessarily\n * have any connection to each other, but it is necessary that any one\n * primitive (e.g.  a polygon) must pull all its vertices from the same pool.\n *\n * An EggVertexPool is an STL-style container of pointers to EggVertex's.\n * Functions add_vertex() and remove_vertex() are provided to manipulate the\n * list.  The list may also be operated on (read-only) via iterators and\n * begin()/end().\n */",
        '__getitem__': None, # (!) real value is "<slot wrapper '__getitem__' of 'panda3d.egg.EggVertexPool' objects>"
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.egg.EggVertexPool' objects>"
        '__len__': None, # (!) real value is "<slot wrapper '__len__' of 'panda3d.egg.EggVertexPool' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFDC68CD9A0>'
        'addUnusedVerticesToPrim': None, # (!) real value is "<method 'addUnusedVerticesToPrim' of 'panda3d.egg.EggVertexPool' objects>"
        'addVertex': None, # (!) real value is "<method 'addVertex' of 'panda3d.egg.EggVertexPool' objects>"
        'add_unused_vertices_to_prim': None, # (!) real value is "<method 'add_unused_vertices_to_prim' of 'panda3d.egg.EggVertexPool' objects>"
        'add_vertex': None, # (!) real value is "<method 'add_vertex' of 'panda3d.egg.EggVertexPool' objects>"
        'createUniqueVertex': None, # (!) real value is "<method 'createUniqueVertex' of 'panda3d.egg.EggVertexPool' objects>"
        'create_unique_vertex': None, # (!) real value is "<method 'create_unique_vertex' of 'panda3d.egg.EggVertexPool' objects>"
        'findMatchingVertex': None, # (!) real value is "<method 'findMatchingVertex' of 'panda3d.egg.EggVertexPool' objects>"
        'find_matching_vertex': None, # (!) real value is "<method 'find_matching_vertex' of 'panda3d.egg.EggVertexPool' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFDC68CD9A0>)>'
        'getForwardVertex': None, # (!) real value is "<method 'getForwardVertex' of 'panda3d.egg.EggVertexPool' objects>"
        'getHighestIndex': None, # (!) real value is "<method 'getHighestIndex' of 'panda3d.egg.EggVertexPool' objects>"
        'getNumDimensions': None, # (!) real value is "<method 'getNumDimensions' of 'panda3d.egg.EggVertexPool' objects>"
        'getVertex': None, # (!) real value is "<method 'getVertex' of 'panda3d.egg.EggVertexPool' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFDC68CD9A0>)>'
        'get_forward_vertex': None, # (!) real value is "<method 'get_forward_vertex' of 'panda3d.egg.EggVertexPool' objects>"
        'get_highest_index': None, # (!) real value is "<method 'get_highest_index' of 'panda3d.egg.EggVertexPool' objects>"
        'get_num_dimensions': None, # (!) real value is "<method 'get_num_dimensions' of 'panda3d.egg.EggVertexPool' objects>"
        'get_vertex': None, # (!) real value is "<method 'get_vertex' of 'panda3d.egg.EggVertexPool' objects>"
        'hasAux': None, # (!) real value is "<method 'hasAux' of 'panda3d.egg.EggVertexPool' objects>"
        'hasColors': None, # (!) real value is "<method 'hasColors' of 'panda3d.egg.EggVertexPool' objects>"
        'hasDefinedVertices': None, # (!) real value is "<method 'hasDefinedVertices' of 'panda3d.egg.EggVertexPool' objects>"
        'hasForwardVertices': None, # (!) real value is "<method 'hasForwardVertices' of 'panda3d.egg.EggVertexPool' objects>"
        'hasNonwhiteColors': None, # (!) real value is "<method 'hasNonwhiteColors' of 'panda3d.egg.EggVertexPool' objects>"
        'hasNormals': None, # (!) real value is "<method 'hasNormals' of 'panda3d.egg.EggVertexPool' objects>"
        'hasUvs': None, # (!) real value is "<method 'hasUvs' of 'panda3d.egg.EggVertexPool' objects>"
        'hasVertex': None, # (!) real value is "<method 'hasVertex' of 'panda3d.egg.EggVertexPool' objects>"
        'has_aux': None, # (!) real value is "<method 'has_aux' of 'panda3d.egg.EggVertexPool' objects>"
        'has_colors': None, # (!) real value is "<method 'has_colors' of 'panda3d.egg.EggVertexPool' objects>"
        'has_defined_vertices': None, # (!) real value is "<method 'has_defined_vertices' of 'panda3d.egg.EggVertexPool' objects>"
        'has_forward_vertices': None, # (!) real value is "<method 'has_forward_vertices' of 'panda3d.egg.EggVertexPool' objects>"
        'has_nonwhite_colors': None, # (!) real value is "<method 'has_nonwhite_colors' of 'panda3d.egg.EggVertexPool' objects>"
        'has_normals': None, # (!) real value is "<method 'has_normals' of 'panda3d.egg.EggVertexPool' objects>"
        'has_uvs': None, # (!) real value is "<method 'has_uvs' of 'panda3d.egg.EggVertexPool' objects>"
        'has_vertex': None, # (!) real value is "<method 'has_vertex' of 'panda3d.egg.EggVertexPool' objects>"
        'makeNewVertex': None, # (!) real value is "<method 'makeNewVertex' of 'panda3d.egg.EggVertexPool' objects>"
        'make_new_vertex': None, # (!) real value is "<method 'make_new_vertex' of 'panda3d.egg.EggVertexPool' objects>"
        'removeUnusedVertices': None, # (!) real value is "<method 'removeUnusedVertices' of 'panda3d.egg.EggVertexPool' objects>"
        'removeVertex': None, # (!) real value is "<method 'removeVertex' of 'panda3d.egg.EggVertexPool' objects>"
        'remove_unused_vertices': None, # (!) real value is "<method 'remove_unused_vertices' of 'panda3d.egg.EggVertexPool' objects>"
        'remove_vertex': None, # (!) real value is "<method 'remove_vertex' of 'panda3d.egg.EggVertexPool' objects>"
        'setHighestIndex': None, # (!) real value is "<method 'setHighestIndex' of 'panda3d.egg.EggVertexPool' objects>"
        'set_highest_index': None, # (!) real value is "<method 'set_highest_index' of 'panda3d.egg.EggVertexPool' objects>"
        'sortByExternalIndex': None, # (!) real value is "<method 'sortByExternalIndex' of 'panda3d.egg.EggVertexPool' objects>"
        'sort_by_external_index': None, # (!) real value is "<method 'sort_by_external_index' of 'panda3d.egg.EggVertexPool' objects>"
        'transform': None, # (!) real value is "<method 'transform' of 'panda3d.egg.EggVertexPool' objects>"
    }


