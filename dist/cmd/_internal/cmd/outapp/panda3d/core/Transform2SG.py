# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .DataNode import DataNode

class Transform2SG(DataNode):
    """
    /**
     * input: Transform (matrix)
     *
     * output: none, but applies the matrix as the transform transition for a
     * given arc of the scene graph.
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
        get_node(Transform2SG self)
        
        /**
         * Returns the node that this object will adjust, or NULL if the node has not
         * yet been set.
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_node(self, Transform2SG_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_node(Transform2SG self)
        
        /**
         * Returns the node that this object will adjust, or NULL if the node has not
         * yet been set.
         */
        """
        pass

    def setNode(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_node(const Transform2SG self, PandaNode node)
        
        /**
         * Sets the node that this object will adjust.
         */
        """
        pass

    def set_node(self, const_Transform2SG_self, PandaNode_node): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_node(const Transform2SG self, PandaNode node)
        
        /**
         * Sets the node that this object will adjust.
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

    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.core.Transform2SG' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.core.Transform2SG' objects>"
        '__doc__': '/**\n * input: Transform (matrix)\n *\n * output: none, but applies the matrix as the transform transition for a\n * given arc of the scene graph.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.Transform2SG' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE367120>'
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE367120>)>'
        'getNode': None, # (!) real value is "<method 'getNode' of 'panda3d.core.Transform2SG' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE367120>)>'
        'get_node': None, # (!) real value is "<method 'get_node' of 'panda3d.core.Transform2SG' objects>"
        'setNode': None, # (!) real value is "<method 'setNode' of 'panda3d.core.Transform2SG' objects>"
        'set_node': None, # (!) real value is "<method 'set_node' of 'panda3d.core.Transform2SG' objects>"
    }

