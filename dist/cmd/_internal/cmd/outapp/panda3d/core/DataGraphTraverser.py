# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


class DataGraphTraverser(__dtoolconfig.DTOOL_SUPER_BASE):
    """
    /**
     * This object supervises the traversal of the data graph and the moving of
     * data from one DataNode to its children.  The data graph is used to manage
     * data from input devices, etc.  See the overview of the data graph in
     * dataNode.h.
     */
    """
    def collectLeftovers(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        collect_leftovers(const DataGraphTraverser self)
        
        /**
         * Pick up any nodes that didn't get completely traversed.  These must be
         * nodes that have multiple parents, with at least one parent completely
         * outside of the data graph.
         */
        """
        pass

    def collect_leftovers(self, const_DataGraphTraverser_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        collect_leftovers(const DataGraphTraverser self)
        
        /**
         * Pick up any nodes that didn't get completely traversed.  These must be
         * nodes that have multiple parents, with at least one parent completely
         * outside of the data graph.
         */
        """
        pass

    def getCurrentThread(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_current_thread(DataGraphTraverser self)
        
        /**
         * Returns the currently-executing thread object, as passed to the
         * DataGraphTraverser constructor.
         */
        """
        pass

    def get_current_thread(self, DataGraphTraverser_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_current_thread(DataGraphTraverser self)
        
        /**
         * Returns the currently-executing thread object, as passed to the
         * DataGraphTraverser constructor.
         */
        """
        pass

    def traverse(self, const_DataGraphTraverser_self, PandaNode_node): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        traverse(const DataGraphTraverser self, PandaNode node)
        
        /**
         * Starts the traversal of the data graph at the indicated root node.
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
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.core.DataGraphTraverser' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.core.DataGraphTraverser' objects>"
        '__doc__': '/**\n * This object supervises the traversal of the data graph and the moving of\n * data from one DataNode to its children.  The data graph is used to manage\n * data from input devices, etc.  See the overview of the data graph in\n * dataNode.h.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.DataGraphTraverser' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE2D9060>'
        'collectLeftovers': None, # (!) real value is "<method 'collectLeftovers' of 'panda3d.core.DataGraphTraverser' objects>"
        'collect_leftovers': None, # (!) real value is "<method 'collect_leftovers' of 'panda3d.core.DataGraphTraverser' objects>"
        'getCurrentThread': None, # (!) real value is "<method 'getCurrentThread' of 'panda3d.core.DataGraphTraverser' objects>"
        'get_current_thread': None, # (!) real value is "<method 'get_current_thread' of 'panda3d.core.DataGraphTraverser' objects>"
        'traverse': None, # (!) real value is "<method 'traverse' of 'panda3d.core.DataGraphTraverser' objects>"
    }


