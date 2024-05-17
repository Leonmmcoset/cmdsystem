# encoding: utf-8
# module panda3d.egg
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\egg.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import panda3d.core as __panda3d_core


from .EggObject import EggObject

class EggBinMaker(EggObject):
    """
    /**
     * This is a handy class for collecting related nodes together.  It is an
     * abstract class; to use it you must subclass off of it.  See the somewhat
     * lengthy comment above.
     */
    """
    def collapseGroup(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        collapse_group(const EggBinMaker self, const EggGroup group, int bin_number)
        
        /**
         * May be overridden in derived classes to specify whether a particular group
         * node, apparently redundant, may be safely collapsed out.
         */
        """
        pass

    def collapse_group(self, const_EggBinMaker_self, const_EggGroup_group, int_bin_number): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        collapse_group(const EggBinMaker self, const EggGroup group, int bin_number)
        
        /**
         * May be overridden in derived classes to specify whether a particular group
         * node, apparently redundant, may be safely collapsed out.
         */
        """
        pass

    def getBinName(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_bin_name(const EggBinMaker self, int bin_number, const EggNode child)
        
        /**
         * May be overridden in derived classes to define a name for each new bin,
         * based on its bin number, and a sample child.
         */
        """
        pass

    def getBinNumber(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_bin_number(const EggBinMaker self, const EggNode node)
        """
        pass

    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_bin_name(self, const_EggBinMaker_self, int_bin_number, const_EggNode_child): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_bin_name(const EggBinMaker self, int bin_number, const EggNode child)
        
        /**
         * May be overridden in derived classes to define a name for each new bin,
         * based on its bin number, and a sample child.
         */
        """
        pass

    def get_bin_number(self, const_EggBinMaker_self, const_EggNode_node): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_bin_number(const EggBinMaker self, const EggNode node)
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def makeBin(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        make_bin(const EggBinMaker self, int bin_number, const EggNode child, EggGroup collapse_from)
        
        /**
         * May be overridden in derived classes to construct a new EggBin object (or
         * some derived class, if needed), and preload some initial data into as
         * required.
         *
         * child is an arbitrary child of the bin, and collapse_from is the group the
         * bin is being collapsed with, if any (implying collapse_group() returned
         * true), or NULL if not.
         */
        """
        pass

    def makeBins(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        make_bins(const EggBinMaker self, EggGroupNode root_group)
        
        /**
         * The main entry point to EggBinMaker.  Walks the egg scene graph beginning
         * at the indicated root node, and moves all binnable nodes into EggBin
         * objects.  Returns the number of EggBins created.
         */
        """
        pass

    def make_bin(self, const_EggBinMaker_self, int_bin_number, const_EggNode_child, EggGroup_collapse_from): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        make_bin(const EggBinMaker self, int bin_number, const EggNode child, EggGroup collapse_from)
        
        /**
         * May be overridden in derived classes to construct a new EggBin object (or
         * some derived class, if needed), and preload some initial data into as
         * required.
         *
         * child is an arbitrary child of the bin, and collapse_from is the group the
         * bin is being collapsed with, if any (implying collapse_group() returned
         * true), or NULL if not.
         */
        """
        pass

    def make_bins(self, const_EggBinMaker_self, EggGroupNode_root_group): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        make_bins(const EggBinMaker self, EggGroupNode root_group)
        
        /**
         * The main entry point to EggBinMaker.  Walks the egg scene graph beginning
         * at the indicated root node, and moves all binnable nodes into EggBin
         * objects.  Returns the number of EggBins created.
         */
        """
        pass

    def prepareNode(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        prepare_node(const EggBinMaker self, EggNode node)
        
        /**
         * May be overridden in derived classes to perform some setup work as each
         * node is encountered.  This will be called once for each node in the egg
         * hierarchy.
         */
        """
        pass

    def prepare_node(self, const_EggBinMaker_self, EggNode_node): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        prepare_node(const EggBinMaker self, EggNode node)
        
        /**
         * May be overridden in derived classes to perform some setup work as each
         * node is encountered.  This will be called once for each node in the egg
         * hierarchy.
         */
        """
        pass

    def sortsLess(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        sorts_less(const EggBinMaker self, int bin_number, const EggNode a, const EggNode b)
        
        /**
         * May be overridden in derived classes to create additional bins within a
         * particular bin number, based on some arbitrary property of nodes.  This
         * function establishes an arbitrary but fixed ordering between nodes; if two
         * nodes do not sort to the same position, different bins are created for each
         * one (with the same bin number on each bin).
         */
        """
        pass

    def sorts_less(self, const_EggBinMaker_self, int_bin_number, const_EggNode_a, const_EggNode_b): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        sorts_less(const EggBinMaker self, int bin_number, const EggNode a, const EggNode b)
        
        /**
         * May be overridden in derived classes to create additional bins within a
         * particular bin number, based on some arbitrary property of nodes.  This
         * function establishes an arbitrary but fixed ordering between nodes; if two
         * nodes do not sort to the same position, different bins are created for each
         * one (with the same bin number on each bin).
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
        '__doc__': '/**\n * This is a handy class for collecting related nodes together.  It is an\n * abstract class; to use it you must subclass off of it.  See the somewhat\n * lengthy comment above.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.egg.EggBinMaker' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFDC68CE650>'
        'collapseGroup': None, # (!) real value is "<method 'collapseGroup' of 'panda3d.egg.EggBinMaker' objects>"
        'collapse_group': None, # (!) real value is "<method 'collapse_group' of 'panda3d.egg.EggBinMaker' objects>"
        'getBinName': None, # (!) real value is "<method 'getBinName' of 'panda3d.egg.EggBinMaker' objects>"
        'getBinNumber': None, # (!) real value is "<method 'getBinNumber' of 'panda3d.egg.EggBinMaker' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFDC68CE650>)>'
        'get_bin_name': None, # (!) real value is "<method 'get_bin_name' of 'panda3d.egg.EggBinMaker' objects>"
        'get_bin_number': None, # (!) real value is "<method 'get_bin_number' of 'panda3d.egg.EggBinMaker' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFDC68CE650>)>'
        'makeBin': None, # (!) real value is "<method 'makeBin' of 'panda3d.egg.EggBinMaker' objects>"
        'makeBins': None, # (!) real value is "<method 'makeBins' of 'panda3d.egg.EggBinMaker' objects>"
        'make_bin': None, # (!) real value is "<method 'make_bin' of 'panda3d.egg.EggBinMaker' objects>"
        'make_bins': None, # (!) real value is "<method 'make_bins' of 'panda3d.egg.EggBinMaker' objects>"
        'prepareNode': None, # (!) real value is "<method 'prepareNode' of 'panda3d.egg.EggBinMaker' objects>"
        'prepare_node': None, # (!) real value is "<method 'prepare_node' of 'panda3d.egg.EggBinMaker' objects>"
        'sortsLess': None, # (!) real value is "<method 'sortsLess' of 'panda3d.egg.EggBinMaker' objects>"
        'sorts_less': None, # (!) real value is "<method 'sorts_less' of 'panda3d.egg.EggBinMaker' objects>"
    }


