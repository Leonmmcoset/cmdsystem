# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .PandaNode import PandaNode

class PartBundleNode(PandaNode):
    """
    /**
     * This is a node that contains a pointer to an PartBundle.  Like
     * AnimBundleNode, it exists to make it easy to store PartBundles in the scene
     * graph.
     *
     * (Unlike AnimBundleNode, however, PartBundleNode has an additional function:
     * it is also the base class of the Character node type, which adds additional
     * functionality.)
     */
    """
    def getBundle(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_bundle(PartBundleNode self, int n)
        
        /**
         *
         */
        """
        pass

    def getBundleHandle(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_bundle_handle(PartBundleNode self, int n)
        
        /**
         * Returns the PartBundleHandle that wraps around the actual nth PartBundle.
         * While the PartBundle pointer might later change due to a future flatten
         * operation, the PartBundleHandle will not.
         */
        """
        pass

    def getBundleHandles(self, *args, **kwargs): # real signature unknown
        pass

    def getBundles(self, *args, **kwargs): # real signature unknown
        pass

    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getNumBundles(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_bundles(PartBundleNode self)
        
        /**
         *
         */
        """
        pass

    def get_bundle(self, PartBundleNode_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_bundle(PartBundleNode self, int n)
        
        /**
         *
         */
        """
        pass

    def get_bundles(self, *args, **kwargs): # real signature unknown
        pass

    def get_bundle_handle(self, PartBundleNode_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_bundle_handle(PartBundleNode self, int n)
        
        /**
         * Returns the PartBundleHandle that wraps around the actual nth PartBundle.
         * While the PartBundle pointer might later change due to a future flatten
         * operation, the PartBundleHandle will not.
         */
        """
        pass

    def get_bundle_handles(self, *args, **kwargs): # real signature unknown
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_num_bundles(self, PartBundleNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_bundles(PartBundleNode self)
        
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

    bundles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    bundle_handles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__doc__': '/**\n * This is a node that contains a pointer to an PartBundle.  Like\n * AnimBundleNode, it exists to make it easy to store PartBundles in the scene\n * graph.\n *\n * (Unlike AnimBundleNode, however, PartBundleNode has an additional function:\n * it is also the base class of the Character node type, which adds additional\n * functionality.)\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.PartBundleNode' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE2C4940>'
        'bundle_handles': None, # (!) real value is "<attribute 'bundle_handles' of 'panda3d.core.PartBundleNode' objects>"
        'bundles': None, # (!) real value is "<attribute 'bundles' of 'panda3d.core.PartBundleNode' objects>"
        'getBundle': None, # (!) real value is "<method 'getBundle' of 'panda3d.core.PartBundleNode' objects>"
        'getBundleHandle': None, # (!) real value is "<method 'getBundleHandle' of 'panda3d.core.PartBundleNode' objects>"
        'getBundleHandles': None, # (!) real value is "<method 'getBundleHandles' of 'panda3d.core.PartBundleNode' objects>"
        'getBundles': None, # (!) real value is "<method 'getBundles' of 'panda3d.core.PartBundleNode' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE2C4940>)>'
        'getNumBundles': None, # (!) real value is "<method 'getNumBundles' of 'panda3d.core.PartBundleNode' objects>"
        'get_bundle': None, # (!) real value is "<method 'get_bundle' of 'panda3d.core.PartBundleNode' objects>"
        'get_bundle_handle': None, # (!) real value is "<method 'get_bundle_handle' of 'panda3d.core.PartBundleNode' objects>"
        'get_bundle_handles': None, # (!) real value is "<method 'get_bundle_handles' of 'panda3d.core.PartBundleNode' objects>"
        'get_bundles': None, # (!) real value is "<method 'get_bundles' of 'panda3d.core.PartBundleNode' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE2C4940>)>'
        'get_num_bundles': None, # (!) real value is "<method 'get_num_bundles' of 'panda3d.core.PartBundleNode' objects>"
    }


