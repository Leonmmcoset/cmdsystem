# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .VertexTransform import VertexTransform

class NodeVertexTransform(VertexTransform):
    """
    /**
     * This VertexTransform gets its matrix from the Transform stored on a node.
     * It can also compose its node's transform with another VertexTransform,
     * allowing you to build up a chain of NodeVertexTransforms that represent a
     * list of composed matrices.
     */
    """
    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getNode(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_node(NodeVertexTransform self)
        
        /**
         * Returns the PandaNode whose transform supplies this object.
         */
        """
        pass

    def getPrev(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_prev(NodeVertexTransform self)
        
        /**
         * Returns the VertexTransform object whose matrix will be composed with the
         * result of this node's transform.
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_node(self, NodeVertexTransform_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_node(NodeVertexTransform self)
        
        /**
         * Returns the PandaNode whose transform supplies this object.
         */
        """
        pass

    def get_prev(self, NodeVertexTransform_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_prev(NodeVertexTransform self)
        
        /**
         * Returns the VertexTransform object whose matrix will be composed with the
         * result of this node's transform.
         */
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    node = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    prev = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__doc__': "/**\n * This VertexTransform gets its matrix from the Transform stored on a node.\n * It can also compose its node's transform with another VertexTransform,\n * allowing you to build up a chain of NodeVertexTransforms that represent a\n * list of composed matrices.\n */",
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.NodeVertexTransform' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE2BD210>'
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE2BD210>)>'
        'getNode': None, # (!) real value is "<method 'getNode' of 'panda3d.core.NodeVertexTransform' objects>"
        'getPrev': None, # (!) real value is "<method 'getPrev' of 'panda3d.core.NodeVertexTransform' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE2BD210>)>'
        'get_node': None, # (!) real value is "<method 'get_node' of 'panda3d.core.NodeVertexTransform' objects>"
        'get_prev': None, # (!) real value is "<method 'get_prev' of 'panda3d.core.NodeVertexTransform' objects>"
        'node': None, # (!) real value is "<attribute 'node' of 'panda3d.core.NodeVertexTransform' objects>"
        'prev': None, # (!) real value is "<attribute 'prev' of 'panda3d.core.NodeVertexTransform' objects>"
    }


