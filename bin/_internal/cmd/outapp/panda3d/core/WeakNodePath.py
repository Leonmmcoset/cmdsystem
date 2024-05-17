# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


class WeakNodePath(__dtoolconfig.DTOOL_SUPER_BASE):
    """
    /**
     * This class is a wrapper around a NodePath that, unlike the actual NodePath
     * class, doesn't hold a reference count to the node.  Thus the node may be
     * detached from the scene graph and destructed at any time.
     *
     * You can call is_valid() or was_deleted() at any time to determine whether
     * the node is still around; if it is, get_node_path() will return the
     * associated NodePath.
     */
    """
    def assign(self, const_WeakNodePath_self, const_WeakNodePath_copy): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        assign(const WeakNodePath self, const WeakNodePath copy)
        assign(const WeakNodePath self, const NodePath node_path)
        """
        pass

    def clear(self, const_WeakNodePath_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear(const WeakNodePath self)
        
        /**
         * Sets this NodePath to the empty NodePath.  It will no longer point to any
         * node.
         */
        """
        pass

    def compareTo(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        compare_to(WeakNodePath self, const WeakNodePath other)
        compare_to(WeakNodePath self, const NodePath other)
        
        /**
         * Returns a number less than zero if this NodePath sorts before the other
         * one, greater than zero if it sorts after, or zero if they are equivalent.
         *
         * Two NodePaths are considered equivalent if they consist of exactly the same
         * list of nodes in the same order.  Otherwise, they are different; different
         * NodePaths will be ranked in a consistent but undefined ordering; the
         * ordering is useful only for placing the NodePaths in a sorted container
         * like an STL set.
         */
        
        /**
         * Returns a number less than zero if this WeakNodePath sorts before the other
         * one, greater than zero if it sorts after, or zero if they are equivalent.
         *
         * Two WeakNodePaths are considered equivalent if they consist of exactly the
         * same list of nodes in the same order.  Otherwise, they are different;
         * different WeakNodePaths will be ranked in a consistent but undefined
         * ordering; the ordering is useful only for placing the WeakNodePaths in a
         * sorted container like an STL set.
         */
        """
        pass

    def compare_to(self, WeakNodePath_self, const_WeakNodePath_other): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        compare_to(WeakNodePath self, const WeakNodePath other)
        compare_to(WeakNodePath self, const NodePath other)
        
        /**
         * Returns a number less than zero if this NodePath sorts before the other
         * one, greater than zero if it sorts after, or zero if they are equivalent.
         *
         * Two NodePaths are considered equivalent if they consist of exactly the same
         * list of nodes in the same order.  Otherwise, they are different; different
         * NodePaths will be ranked in a consistent but undefined ordering; the
         * ordering is useful only for placing the NodePaths in a sorted container
         * like an STL set.
         */
        
        /**
         * Returns a number less than zero if this WeakNodePath sorts before the other
         * one, greater than zero if it sorts after, or zero if they are equivalent.
         *
         * Two WeakNodePaths are considered equivalent if they consist of exactly the
         * same list of nodes in the same order.  Otherwise, they are different;
         * different WeakNodePaths will be ranked in a consistent but undefined
         * ordering; the ordering is useful only for placing the WeakNodePaths in a
         * sorted container like an STL set.
         */
        """
        pass

    def getKey(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_key(WeakNodePath self)
        
        /**
         * Returns the same values as NodePath::get_key().
         */
        """
        pass

    def getNodePath(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_node_path(WeakNodePath self)
        
        /**
         * Returns the NodePath held within this object, or an empty NodePath with the
         * error flag set if the object was deleted.
         */
        """
        pass

    def get_key(self, WeakNodePath_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_key(WeakNodePath self)
        
        /**
         * Returns the same values as NodePath::get_key().
         */
        """
        pass

    def get_node_path(self, WeakNodePath_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_node_path(WeakNodePath self)
        
        /**
         * Returns the NodePath held within this object, or an empty NodePath with the
         * error flag set if the object was deleted.
         */
        """
        pass

    def isEmpty(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_empty(WeakNodePath self)
        
        /**
         * Returns true if the NodePath contains no nodes, or if it has been deleted.
         */
        """
        pass

    def is_empty(self, WeakNodePath_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_empty(WeakNodePath self)
        
        /**
         * Returns true if the NodePath contains no nodes, or if it has been deleted.
         */
        """
        pass

    def node(self, WeakNodePath_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        node(WeakNodePath self)
        
        /**
         * Returns the PandaNode held within this object, or nullptr if the object was
         * deleted.
         */
        """
        pass

    def output(self, WeakNodePath_self, ostream_out): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        output(WeakNodePath self, ostream out)
        
        /**
         *
         */
        """
        pass

    def wasDeleted(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        was_deleted(WeakNodePath self)
        
        /**
         * Returns true if the NodePath we were referencing has been quietly deleted
         * outside of the WeakNodePath.
         */
        """
        pass

    def was_deleted(self, WeakNodePath_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        was_deleted(WeakNodePath self)
        
        /**
         * Returns true if the NodePath we were referencing has been quietly deleted
         * outside of the WeakNodePath.
         */
        """
        pass

    def __bool__(self, *args, **kwargs): # real signature unknown
        """ True if self else False """
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
        '__bool__': None, # (!) real value is "<slot wrapper '__bool__' of 'panda3d.core.WeakNodePath' objects>"
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.core.WeakNodePath' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.core.WeakNodePath' objects>"
        '__doc__': "/**\n * This class is a wrapper around a NodePath that, unlike the actual NodePath\n * class, doesn't hold a reference count to the node.  Thus the node may be\n * detached from the scene graph and destructed at any time.\n *\n * You can call is_valid() or was_deleted() at any time to determine whether\n * the node is still around; if it is, get_node_path() will return the\n * associated NodePath.\n */",
        '__eq__': None, # (!) real value is "<slot wrapper '__eq__' of 'panda3d.core.WeakNodePath' objects>"
        '__ge__': None, # (!) real value is "<slot wrapper '__ge__' of 'panda3d.core.WeakNodePath' objects>"
        '__gt__': None, # (!) real value is "<slot wrapper '__gt__' of 'panda3d.core.WeakNodePath' objects>"
        '__hash__': None, # (!) real value is "<slot wrapper '__hash__' of 'panda3d.core.WeakNodePath' objects>"
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.WeakNodePath' objects>"
        '__le__': None, # (!) real value is "<slot wrapper '__le__' of 'panda3d.core.WeakNodePath' objects>"
        '__lt__': None, # (!) real value is "<slot wrapper '__lt__' of 'panda3d.core.WeakNodePath' objects>"
        '__ne__': None, # (!) real value is "<slot wrapper '__ne__' of 'panda3d.core.WeakNodePath' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE294AC0>'
        '__repr__': None, # (!) real value is "<slot wrapper '__repr__' of 'panda3d.core.WeakNodePath' objects>"
        '__str__': None, # (!) real value is "<slot wrapper '__str__' of 'panda3d.core.WeakNodePath' objects>"
        'assign': None, # (!) real value is "<method 'assign' of 'panda3d.core.WeakNodePath' objects>"
        'clear': None, # (!) real value is "<method 'clear' of 'panda3d.core.WeakNodePath' objects>"
        'compareTo': None, # (!) real value is "<method 'compareTo' of 'panda3d.core.WeakNodePath' objects>"
        'compare_to': None, # (!) real value is "<method 'compare_to' of 'panda3d.core.WeakNodePath' objects>"
        'getKey': None, # (!) real value is "<method 'getKey' of 'panda3d.core.WeakNodePath' objects>"
        'getNodePath': None, # (!) real value is "<method 'getNodePath' of 'panda3d.core.WeakNodePath' objects>"
        'get_key': None, # (!) real value is "<method 'get_key' of 'panda3d.core.WeakNodePath' objects>"
        'get_node_path': None, # (!) real value is "<method 'get_node_path' of 'panda3d.core.WeakNodePath' objects>"
        'isEmpty': None, # (!) real value is "<method 'isEmpty' of 'panda3d.core.WeakNodePath' objects>"
        'is_empty': None, # (!) real value is "<method 'is_empty' of 'panda3d.core.WeakNodePath' objects>"
        'node': None, # (!) real value is "<method 'node' of 'panda3d.core.WeakNodePath' objects>"
        'output': None, # (!) real value is "<method 'output' of 'panda3d.core.WeakNodePath' objects>"
        'wasDeleted': None, # (!) real value is "<method 'wasDeleted' of 'panda3d.core.WeakNodePath' objects>"
        'was_deleted': None, # (!) real value is "<method 'was_deleted' of 'panda3d.core.WeakNodePath' objects>"
    }


