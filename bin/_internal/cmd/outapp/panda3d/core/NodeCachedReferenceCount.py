# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .CachedTypedWritableReferenceCount import CachedTypedWritableReferenceCount

class NodeCachedReferenceCount(CachedTypedWritableReferenceCount):
    """
    /**
     * This class further specializes CachedTypedWritableReferenceCount to also
     * add a node_ref_count, for the purposes of counting the number of times the
     * object is referenced by a "node", presumably a PandaNode.
     *
     * This essentially combines the functionality of NodeReferenceCount and
     * CachedTypedWritableReferenceCount, so that a derivative of this object
     * actually has three counters: the standard reference count, the "cache"
     * reference count, and the "node" reference count.  Rather than multiply
     * inheriting from the two reference count classes, we inherit only from
     * CachedTypedWritableReferenceCount and simply duplicate the functionality of
     * NodeReferenceCount, to avoid all of the problems associated with multiple
     * inheritance.
     *
     * The intended design is to use this as a base class for RenderState and
     * TransformState, both of which are held by PandaNodes, and also have caches
     * which are independently maintained.  By keeping track of how many nodes
     * hold a pointer to a particular object, we can classify each object into
     * node-referenced, cache-referenced, or other, which is primarily useful for
     * PStats reporting.
     *
     * As with CachedTypedWritableReferenceCount's cache_ref() and cache_unref(),
     * the new methods node_ref() and node_unref() automatically increment and
     * decrement the primary reference count as well.  In this case, however,
     * there does exist a NodePointerTo<> class to maintain the node_ref counters
     * automatically.
     */
    """
    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getNodeRefCount(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_node_ref_count(NodeCachedReferenceCount self)
        
        /**
         * Returns the current reference count.
         */
        """
        pass

    def getReferencedBits(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_referenced_bits(NodeCachedReferenceCount self)
        
        /**
         * Returns the union of the values defined in the Referenced enum that
         * represents the various things that appear to be holding a pointer to this
         * object.
         *
         * If R_node is included, at least one node is holding a pointer; if R_cache
         * is included, at least one cache element is.
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_node_ref_count(self, NodeCachedReferenceCount_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_node_ref_count(NodeCachedReferenceCount self)
        
        /**
         * Returns the current reference count.
         */
        """
        pass

    def get_referenced_bits(self, NodeCachedReferenceCount_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_referenced_bits(NodeCachedReferenceCount self)
        
        /**
         * Returns the union of the values defined in the Referenced enum that
         * represents the various things that appear to be holding a pointer to this
         * object.
         *
         * If R_node is included, at least one node is holding a pointer; if R_cache
         * is included, at least one cache element is.
         */
        """
        pass

    def nodeRef(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        node_ref(NodeCachedReferenceCount self)
        
        /**
         * Explicitly increments the reference count.
         *
         * This function is const, even though it changes the object, because
         * generally fiddling with an object's reference count isn't considered part
         * of fiddling with the object.  An object might be const in other ways, but
         * we still need to accurately count the number of references to it.
         */
        """
        pass

    def nodeUnref(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        node_unref(NodeCachedReferenceCount self)
        
        /**
         * Explicitly decrements the node reference count and the normal reference
         * count simultaneously.
         *
         * The return value is true if the new reference count is nonzero, false if it
         * is zero.
         */
        """
        pass

    def node_ref(self, NodeCachedReferenceCount_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        node_ref(NodeCachedReferenceCount self)
        
        /**
         * Explicitly increments the reference count.
         *
         * This function is const, even though it changes the object, because
         * generally fiddling with an object's reference count isn't considered part
         * of fiddling with the object.  An object might be const in other ways, but
         * we still need to accurately count the number of references to it.
         */
        """
        pass

    def node_unref(self, NodeCachedReferenceCount_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        node_unref(NodeCachedReferenceCount self)
        
        /**
         * Explicitly decrements the node reference count and the normal reference
         * count simultaneously.
         *
         * The return value is true if the new reference count is nonzero, false if it
         * is zero.
         */
        """
        pass

    def testRefCountIntegrity(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        test_ref_count_integrity(NodeCachedReferenceCount self)
        
        /**
         * Does some easy checks to make sure that the reference count isn't
         * completely bogus.
         */
        """
        pass

    def test_ref_count_integrity(self, NodeCachedReferenceCount_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        test_ref_count_integrity(NodeCachedReferenceCount self)
        
        /**
         * Does some easy checks to make sure that the reference count isn't
         * completely bogus.
         */
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        'RCache': 2,
        'RNode': 1,
        'R_cache': 2,
        'R_node': 1,
        '__doc__': '/**\n * This class further specializes CachedTypedWritableReferenceCount to also\n * add a node_ref_count, for the purposes of counting the number of times the\n * object is referenced by a "node", presumably a PandaNode.\n *\n * This essentially combines the functionality of NodeReferenceCount and\n * CachedTypedWritableReferenceCount, so that a derivative of this object\n * actually has three counters: the standard reference count, the "cache"\n * reference count, and the "node" reference count.  Rather than multiply\n * inheriting from the two reference count classes, we inherit only from\n * CachedTypedWritableReferenceCount and simply duplicate the functionality of\n * NodeReferenceCount, to avoid all of the problems associated with multiple\n * inheritance.\n *\n * The intended design is to use this as a base class for RenderState and\n * TransformState, both of which are held by PandaNodes, and also have caches\n * which are independently maintained.  By keeping track of how many nodes\n * hold a pointer to a particular object, we can classify each object into\n * node-referenced, cache-referenced, or other, which is primarily useful for\n * PStats reporting.\n *\n * As with CachedTypedWritableReferenceCount\'s cache_ref() and cache_unref(),\n * the new methods node_ref() and node_unref() automatically increment and\n * decrement the primary reference count as well.  In this case, however,\n * there does exist a NodePointerTo<> class to maintain the node_ref counters\n * automatically.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.NodeCachedReferenceCount' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE372F30>'
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE372F30>)>'
        'getNodeRefCount': None, # (!) real value is "<method 'getNodeRefCount' of 'panda3d.core.NodeCachedReferenceCount' objects>"
        'getReferencedBits': None, # (!) real value is "<method 'getReferencedBits' of 'panda3d.core.NodeCachedReferenceCount' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE372F30>)>'
        'get_node_ref_count': None, # (!) real value is "<method 'get_node_ref_count' of 'panda3d.core.NodeCachedReferenceCount' objects>"
        'get_referenced_bits': None, # (!) real value is "<method 'get_referenced_bits' of 'panda3d.core.NodeCachedReferenceCount' objects>"
        'nodeRef': None, # (!) real value is "<method 'nodeRef' of 'panda3d.core.NodeCachedReferenceCount' objects>"
        'nodeUnref': None, # (!) real value is "<method 'nodeUnref' of 'panda3d.core.NodeCachedReferenceCount' objects>"
        'node_ref': None, # (!) real value is "<method 'node_ref' of 'panda3d.core.NodeCachedReferenceCount' objects>"
        'node_unref': None, # (!) real value is "<method 'node_unref' of 'panda3d.core.NodeCachedReferenceCount' objects>"
        'testRefCountIntegrity': None, # (!) real value is "<method 'testRefCountIntegrity' of 'panda3d.core.NodeCachedReferenceCount' objects>"
        'test_ref_count_integrity': None, # (!) real value is "<method 'test_ref_count_integrity' of 'panda3d.core.NodeCachedReferenceCount' objects>"
    }
    RCache = 2
    RNode = 1
    R_cache = 2
    R_node = 1


