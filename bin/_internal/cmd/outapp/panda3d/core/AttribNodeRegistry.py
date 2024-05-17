# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


class AttribNodeRegistry(__dtoolconfig.DTOOL_SUPER_BASE):
    """
    /**
     * This global object records NodePaths that are referenced by scene graph
     * attribs, such as ClipPlaneAttribs and LightAttribs.
     *
     * Its primary purpose is to unify attribs that are loaded in from bam files.
     * Attrib nodes are identified by name and type; when a bam file that contains
     * references to some attrib nodes is loaded, those nodes are first looked up
     * here in the AttribNodeRegistry.  If there is a match (by name and node
     * type), the identified node is used instead of the node referenced within
     * the bam file itself.
     */
    """
    def addNode(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_node(const AttribNodeRegistry self, const NodePath attrib_node)
        
        /**
         * Adds the indicated NodePath to the registry.  The name and type of the node
         * are noted at the time of this call; if the name changes later, it will not
         * update the registry index.
         *
         * The NodePath must reference some kind of an attribute node, such as a
         * LightNode or a PlaneNode.  When bam files that reference an attribute node
         * of the same type and the same name are loaded, they will quietly be
         * redirected to reference this NodePath.
         *
         * If there is already a node matching the indicated name and type, it will be
         * replaced.
         */
        """
        pass

    def add_node(self, const_AttribNodeRegistry_self, const_NodePath_attrib_node): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_node(const AttribNodeRegistry self, const NodePath attrib_node)
        
        /**
         * Adds the indicated NodePath to the registry.  The name and type of the node
         * are noted at the time of this call; if the name changes later, it will not
         * update the registry index.
         *
         * The NodePath must reference some kind of an attribute node, such as a
         * LightNode or a PlaneNode.  When bam files that reference an attribute node
         * of the same type and the same name are loaded, they will quietly be
         * redirected to reference this NodePath.
         *
         * If there is already a node matching the indicated name and type, it will be
         * replaced.
         */
        """
        pass

    def clear(self, const_AttribNodeRegistry_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear(const AttribNodeRegistry self)
        
        /**
         * Removes all nodes from the registry.
         */
        """
        pass

    def findNode(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        find_node(AttribNodeRegistry self, const NodePath attrib_node)
        find_node(AttribNodeRegistry self, TypeHandle type, str name)
        
        /**
         * Returns the index number of the indicated NodePath in the registry
         * (assuming its name hasn't changed since it was recorded in the registry),
         * or -1 if the NodePath cannot be found (for instance, because its name has
         * changed).
         */
        
        /**
         * Returns the index number of the node with the indicated type and name in
         * the registry, or -1 if there is no such node in the registry.
         */
        """
        pass

    def find_node(self, AttribNodeRegistry_self, const_NodePath_attrib_node): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        find_node(AttribNodeRegistry self, const NodePath attrib_node)
        find_node(AttribNodeRegistry self, TypeHandle type, str name)
        
        /**
         * Returns the index number of the indicated NodePath in the registry
         * (assuming its name hasn't changed since it was recorded in the registry),
         * or -1 if the NodePath cannot be found (for instance, because its name has
         * changed).
         */
        
        /**
         * Returns the index number of the node with the indicated type and name in
         * the registry, or -1 if there is no such node in the registry.
         */
        """
        pass

    def getGlobalPtr(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_global_ptr()
        
        /**
         *
         */
        """
        pass

    def getNode(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_node(AttribNodeRegistry self, int n)
        
        /**
         * Returns the nth NodePath recorded in the registry.
         */
        """
        pass

    def getNodeName(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_node_name(AttribNodeRegistry self, int n)
        
        /**
         * Returns the name of the nth node, as recorded in the registry.  This will
         * be the node name as it was at the time the node was recorded; if the node
         * has changed names since then, this will still return the original name.
         */
        """
        pass

    def getNodes(self, *args, **kwargs): # real signature unknown
        pass

    def getNodeType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_node_type(AttribNodeRegistry self, int n)
        
        /**
         * Returns the type of the nth node, as recorded in the registry.
         */
        """
        pass

    def getNumNodes(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_nodes(AttribNodeRegistry self)
        
        /**
         * Returns the total number of nodes in the registry.
         */
        """
        pass

    def get_global_ptr(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_global_ptr()
        
        /**
         *
         */
        """
        pass

    def get_node(self, AttribNodeRegistry_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_node(AttribNodeRegistry self, int n)
        
        /**
         * Returns the nth NodePath recorded in the registry.
         */
        """
        pass

    def get_nodes(self, *args, **kwargs): # real signature unknown
        pass

    def get_node_name(self, AttribNodeRegistry_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_node_name(AttribNodeRegistry self, int n)
        
        /**
         * Returns the name of the nth node, as recorded in the registry.  This will
         * be the node name as it was at the time the node was recorded; if the node
         * has changed names since then, this will still return the original name.
         */
        """
        pass

    def get_node_type(self, AttribNodeRegistry_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_node_type(AttribNodeRegistry self, int n)
        
        /**
         * Returns the type of the nth node, as recorded in the registry.
         */
        """
        pass

    def get_num_nodes(self, AttribNodeRegistry_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_nodes(AttribNodeRegistry self)
        
        /**
         * Returns the total number of nodes in the registry.
         */
        """
        pass

    def lookupNode(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        lookup_node(AttribNodeRegistry self, const NodePath orig_node)
        
        /**
         * Looks up the indicated NodePath in the registry.  If there is a node
         * already in the registry with the matching name and type, returns that
         * NodePath instead; otherwise, returns the original NodePath.
         */
        """
        pass

    def lookup_node(self, AttribNodeRegistry_self, const_NodePath_orig_node): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        lookup_node(AttribNodeRegistry self, const NodePath orig_node)
        
        /**
         * Looks up the indicated NodePath in the registry.  If there is a node
         * already in the registry with the matching name and type, returns that
         * NodePath instead; otherwise, returns the original NodePath.
         */
        """
        pass

    def output(self, AttribNodeRegistry_self, ostream_out): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        output(AttribNodeRegistry self, ostream out)
        
        /**
         *
         */
        """
        pass

    def removeNode(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        remove_node(const AttribNodeRegistry self, const NodePath attrib_node)
        remove_node(const AttribNodeRegistry self, int n)
        
        /**
         * Removes the indicated NodePath from the registry.  The name of the node
         * must not have changed since the matching call to add_node(), or it will not
         * be successfully removed.
         *
         * Returns true if the NodePath is found and removed, false if it is not found
         * (for instance, because the name has changed).
         */
        
        /**
         * Removes the nth node from the registry.
         */
        """
        pass

    def remove_node(self, const_AttribNodeRegistry_self, const_NodePath_attrib_node): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        remove_node(const AttribNodeRegistry self, const NodePath attrib_node)
        remove_node(const AttribNodeRegistry self, int n)
        
        /**
         * Removes the indicated NodePath from the registry.  The name of the node
         * must not have changed since the matching call to add_node(), or it will not
         * be successfully removed.
         *
         * Returns true if the NodePath is found and removed, false if it is not found
         * (for instance, because the name has changed).
         */
        
        /**
         * Removes the nth node from the registry.
         */
        """
        pass

    def write(self, AttribNodeRegistry_self, ostream_out): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        write(AttribNodeRegistry self, ostream out)
        
        /**
         *
         */
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__doc__': '/**\n * This global object records NodePaths that are referenced by scene graph\n * attribs, such as ClipPlaneAttribs and LightAttribs.\n *\n * Its primary purpose is to unify attribs that are loaded in from bam files.\n * Attrib nodes are identified by name and type; when a bam file that contains\n * references to some attrib nodes is loaded, those nodes are first looked up\n * here in the AttribNodeRegistry.  If there is a match (by name and node\n * type), the identified node is used instead of the node referenced within\n * the bam file itself.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.AttribNodeRegistry' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE293E10>'
        '__repr__': None, # (!) real value is "<slot wrapper '__repr__' of 'panda3d.core.AttribNodeRegistry' objects>"
        '__str__': None, # (!) real value is "<slot wrapper '__str__' of 'panda3d.core.AttribNodeRegistry' objects>"
        'addNode': None, # (!) real value is "<method 'addNode' of 'panda3d.core.AttribNodeRegistry' objects>"
        'add_node': None, # (!) real value is "<method 'add_node' of 'panda3d.core.AttribNodeRegistry' objects>"
        'clear': None, # (!) real value is "<method 'clear' of 'panda3d.core.AttribNodeRegistry' objects>"
        'findNode': None, # (!) real value is "<method 'findNode' of 'panda3d.core.AttribNodeRegistry' objects>"
        'find_node': None, # (!) real value is "<method 'find_node' of 'panda3d.core.AttribNodeRegistry' objects>"
        'getGlobalPtr': None, # (!) real value is '<staticmethod(<built-in method getGlobalPtr of type object at 0x00007FFCFE293E10>)>'
        'getNode': None, # (!) real value is "<method 'getNode' of 'panda3d.core.AttribNodeRegistry' objects>"
        'getNodeName': None, # (!) real value is "<method 'getNodeName' of 'panda3d.core.AttribNodeRegistry' objects>"
        'getNodeType': None, # (!) real value is "<method 'getNodeType' of 'panda3d.core.AttribNodeRegistry' objects>"
        'getNodes': None, # (!) real value is "<method 'getNodes' of 'panda3d.core.AttribNodeRegistry' objects>"
        'getNumNodes': None, # (!) real value is "<method 'getNumNodes' of 'panda3d.core.AttribNodeRegistry' objects>"
        'get_global_ptr': None, # (!) real value is '<staticmethod(<built-in method get_global_ptr of type object at 0x00007FFCFE293E10>)>'
        'get_node': None, # (!) real value is "<method 'get_node' of 'panda3d.core.AttribNodeRegistry' objects>"
        'get_node_name': None, # (!) real value is "<method 'get_node_name' of 'panda3d.core.AttribNodeRegistry' objects>"
        'get_node_type': None, # (!) real value is "<method 'get_node_type' of 'panda3d.core.AttribNodeRegistry' objects>"
        'get_nodes': None, # (!) real value is "<method 'get_nodes' of 'panda3d.core.AttribNodeRegistry' objects>"
        'get_num_nodes': None, # (!) real value is "<method 'get_num_nodes' of 'panda3d.core.AttribNodeRegistry' objects>"
        'lookupNode': None, # (!) real value is "<method 'lookupNode' of 'panda3d.core.AttribNodeRegistry' objects>"
        'lookup_node': None, # (!) real value is "<method 'lookup_node' of 'panda3d.core.AttribNodeRegistry' objects>"
        'output': None, # (!) real value is "<method 'output' of 'panda3d.core.AttribNodeRegistry' objects>"
        'removeNode': None, # (!) real value is "<method 'removeNode' of 'panda3d.core.AttribNodeRegistry' objects>"
        'remove_node': None, # (!) real value is "<method 'remove_node' of 'panda3d.core.AttribNodeRegistry' objects>"
        'write': None, # (!) real value is "<method 'write' of 'panda3d.core.AttribNodeRegistry' objects>"
    }


