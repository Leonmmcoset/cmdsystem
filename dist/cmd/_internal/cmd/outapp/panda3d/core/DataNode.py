# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .PandaNode import PandaNode

class DataNode(PandaNode):
    """
    /**
     * The fundamental type of node for the data graph.  The DataNode class is
     * itself primarily intended as an abstract class; it defines no inputs and no
     * outputs.  Most kinds of data nodes will derive from this to specify the
     * inputs and outputs in the constructor.
     *
     * DataNode does not attempt to cycle its data with a PipelineCycler.  The
     * data graph is intended to be used only within a single thread.
     */
    """
    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def writeConnections(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        write_connections(DataNode self, ostream out)
        
        /**
         * Writes to the indicated ostream a list of all the connections currently
         * showing between this DataNode and its parent(s).
         */
        """
        pass

    def writeInputs(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        write_inputs(DataNode self, ostream out)
        
        /**
         * Writes to the indicated ostream a list of all the inputs this DataNode
         * might expect to receive.
         */
        """
        pass

    def writeOutputs(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        write_outputs(DataNode self, ostream out)
        
        /**
         * Writes to the indicated ostream a list of all the outputs this DataNode
         * might generate.
         */
        """
        pass

    def write_connections(self, DataNode_self, ostream_out): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        write_connections(DataNode self, ostream out)
        
        /**
         * Writes to the indicated ostream a list of all the connections currently
         * showing between this DataNode and its parent(s).
         */
        """
        pass

    def write_inputs(self, DataNode_self, ostream_out): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        write_inputs(DataNode self, ostream out)
        
        /**
         * Writes to the indicated ostream a list of all the inputs this DataNode
         * might expect to receive.
         */
        """
        pass

    def write_outputs(self, DataNode_self, ostream_out): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        write_outputs(DataNode self, ostream out)
        
        /**
         * Writes to the indicated ostream a list of all the outputs this DataNode
         * might generate.
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
        '__doc__': '/**\n * The fundamental type of node for the data graph.  The DataNode class is\n * itself primarily intended as an abstract class; it defines no inputs and no\n * outputs.  Most kinds of data nodes will derive from this to specify the\n * inputs and outputs in the constructor.\n *\n * DataNode does not attempt to cycle its data with a PipelineCycler.  The\n * data graph is intended to be used only within a single thread.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.DataNode' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE2D9240>'
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE2D9240>)>'
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE2D9240>)>'
        'writeConnections': None, # (!) real value is "<method 'writeConnections' of 'panda3d.core.DataNode' objects>"
        'writeInputs': None, # (!) real value is "<method 'writeInputs' of 'panda3d.core.DataNode' objects>"
        'writeOutputs': None, # (!) real value is "<method 'writeOutputs' of 'panda3d.core.DataNode' objects>"
        'write_connections': None, # (!) real value is "<method 'write_connections' of 'panda3d.core.DataNode' objects>"
        'write_inputs': None, # (!) real value is "<method 'write_inputs' of 'panda3d.core.DataNode' objects>"
        'write_outputs': None, # (!) real value is "<method 'write_outputs' of 'panda3d.core.DataNode' objects>"
    }


