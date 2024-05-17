# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .PandaNode import PandaNode

class AnimBundleNode(PandaNode):
    """
    /**
     * This is a node that contains a pointer to an AnimBundle.  Like
     * PartBundleNode, it exists solely to make it easy to store AnimBundles in
     * the scene graph.
     */
    """
    def findAnimBundle(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        find_anim_bundle(PandaNode root)
        
        /**
         * Recursively walks the scene graph beginning at the indicated node (which
         * need not be an AnimBundleNode), and returns the first AnimBundle found.
         * Returns NULL if no AnimBundle can be found.
         */
        """
        pass

    def find_anim_bundle(self, PandaNode_root): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        find_anim_bundle(PandaNode root)
        
        /**
         * Recursively walks the scene graph beginning at the indicated node (which
         * need not be an AnimBundleNode), and returns the first AnimBundle found.
         * Returns NULL if no AnimBundle can be found.
         */
        """
        pass

    def getBundle(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_bundle(AnimBundleNode self)
        
        /**
         *
         */
        """
        pass

    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_bundle(self, AnimBundleNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_bundle(AnimBundleNode self)
        
        /**
         *
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    bundle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__doc__': '/**\n * This is a node that contains a pointer to an AnimBundle.  Like\n * PartBundleNode, it exists solely to make it easy to store AnimBundles in\n * the scene graph.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.AnimBundleNode' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE2C2E10>'
        'bundle': None, # (!) real value is "<attribute 'bundle' of 'panda3d.core.AnimBundleNode' objects>"
        'findAnimBundle': None, # (!) real value is '<staticmethod(<built-in method findAnimBundle of type object at 0x00007FFCFE2C2E10>)>'
        'find_anim_bundle': None, # (!) real value is '<staticmethod(<built-in method find_anim_bundle of type object at 0x00007FFCFE2C2E10>)>'
        'getBundle': None, # (!) real value is "<method 'getBundle' of 'panda3d.core.AnimBundleNode' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE2C2E10>)>'
        'get_bundle': None, # (!) real value is "<method 'get_bundle' of 'panda3d.core.AnimBundleNode' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE2C2E10>)>'
    }


