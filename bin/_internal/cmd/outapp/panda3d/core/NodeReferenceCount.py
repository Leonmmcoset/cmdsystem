# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .ReferenceCount import ReferenceCount

class NodeReferenceCount(ReferenceCount):
    """
    /**
     * This class specializes ReferenceCount to add an additional counter, called
     * node_ref_count, for the purposes of counting the number of times the object
     * is referenced by a "node", whatever that may mean in context.
     *
     * The new methods node_ref() and node_unref() automatically increment and
     * decrement the primary reference count as well.  There also exists a
     * NodePointerTo<> class to maintain the node_ref counters automatically.
     *
     * See also CachedTypedWritableReferenceCount, which is similar in principle,
     * as well as NodeCachedReferenceCount, which combines both of these.
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
        get_node_ref_count(NodeReferenceCount self)
        
        /**
         * Returns the current reference count.
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_node_ref_count(self, NodeReferenceCount_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_node_ref_count(NodeReferenceCount self)
        
        /**
         * Returns the current reference count.
         */
        """
        pass

    def nodeRef(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        node_ref(NodeReferenceCount self)
        
        /**
         * Explicitly increments the node reference count and the normal reference
         * count simultaneously.
         */
        """
        pass

    def nodeUnref(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        node_unref(NodeReferenceCount self)
        
        /**
         * Explicitly decrements the node reference count and the normal reference
         * count simultaneously.
         *
         * The return value is true if the new reference count is nonzero, false if it
         * is zero.
         */
        """
        pass

    def nodeUnrefOnly(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        node_unref_only(NodeReferenceCount self)
        
        /**
         * Decrements the node reference count without affecting the normal reference
         * count.  Intended to be called by derived classes only, presumably to
         * reimplement node_unref().
         */
        """
        pass

    def node_ref(self, NodeReferenceCount_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        node_ref(NodeReferenceCount self)
        
        /**
         * Explicitly increments the node reference count and the normal reference
         * count simultaneously.
         */
        """
        pass

    def node_unref(self, NodeReferenceCount_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        node_unref(NodeReferenceCount self)
        
        /**
         * Explicitly decrements the node reference count and the normal reference
         * count simultaneously.
         *
         * The return value is true if the new reference count is nonzero, false if it
         * is zero.
         */
        """
        pass

    def node_unref_only(self, NodeReferenceCount_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        node_unref_only(NodeReferenceCount self)
        
        /**
         * Decrements the node reference count without affecting the normal reference
         * count.  Intended to be called by derived classes only, presumably to
         * reimplement node_unref().
         */
        """
        pass

    def testRefCountIntegrity(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        test_ref_count_integrity(NodeReferenceCount self)
        
        /**
         * Does some easy checks to make sure that the reference count isn't
         * completely bogus.
         */
        """
        pass

    def test_ref_count_integrity(self, NodeReferenceCount_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        test_ref_count_integrity(NodeReferenceCount self)
        
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
        '__doc__': '/**\n * This class specializes ReferenceCount to add an additional counter, called\n * node_ref_count, for the purposes of counting the number of times the object\n * is referenced by a "node", whatever that may mean in context.\n *\n * The new methods node_ref() and node_unref() automatically increment and\n * decrement the primary reference count as well.  There also exists a\n * NodePointerTo<> class to maintain the node_ref counters automatically.\n *\n * See also CachedTypedWritableReferenceCount, which is similar in principle,\n * as well as NodeCachedReferenceCount, which combines both of these.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.NodeReferenceCount' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE277780>'
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE277780>)>'
        'getNodeRefCount': None, # (!) real value is "<method 'getNodeRefCount' of 'panda3d.core.NodeReferenceCount' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE277780>)>'
        'get_node_ref_count': None, # (!) real value is "<method 'get_node_ref_count' of 'panda3d.core.NodeReferenceCount' objects>"
        'nodeRef': None, # (!) real value is "<method 'nodeRef' of 'panda3d.core.NodeReferenceCount' objects>"
        'nodeUnref': None, # (!) real value is "<method 'nodeUnref' of 'panda3d.core.NodeReferenceCount' objects>"
        'nodeUnrefOnly': None, # (!) real value is "<method 'nodeUnrefOnly' of 'panda3d.core.NodeReferenceCount' objects>"
        'node_ref': None, # (!) real value is "<method 'node_ref' of 'panda3d.core.NodeReferenceCount' objects>"
        'node_unref': None, # (!) real value is "<method 'node_unref' of 'panda3d.core.NodeReferenceCount' objects>"
        'node_unref_only': None, # (!) real value is "<method 'node_unref_only' of 'panda3d.core.NodeReferenceCount' objects>"
        'testRefCountIntegrity': None, # (!) real value is "<method 'testRefCountIntegrity' of 'panda3d.core.NodeReferenceCount' objects>"
        'test_ref_count_integrity': None, # (!) real value is "<method 'test_ref_count_integrity' of 'panda3d.core.NodeReferenceCount' objects>"
    }


