# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .ReferenceCount import ReferenceCount

class PartBundleHandle(ReferenceCount):
    """
    /**
     * This is a trivial class returned by PartBundleNode::get_bundle().  Its
     * purpose is to hold the actual PartBundle pointer contained within the
     * PartBundleNode, so that scene graph flatten operations can safely combine
     * or duplicate PartBundles as necessary without affecting high-level bundle
     * operations.
     *
     * The high-level Actor class defined in direct/src/actor, for instance, will
     * store a list of PartBundleHandles instead of on actual PartBundles, so that
     * it will be immune to changes from these flatten operations.
     */
    """
    def getBundle(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_bundle(const PartBundleHandle self)
        
        /**
         * Returns the actual PartBundle embedded within the handle.
         */
        """
        pass

    def get_bundle(self, const_PartBundleHandle_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_bundle(const PartBundleHandle self)
        
        /**
         * Returns the actual PartBundle embedded within the handle.
         */
        """
        pass

    def setBundle(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_bundle(const PartBundleHandle self, PartBundle bundle)
        
        /**
         * Changes the actual PartBundle embedded within the handle.
         */
        """
        pass

    def set_bundle(self, const_PartBundleHandle_self, PartBundle_bundle): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_bundle(const PartBundleHandle self, PartBundle bundle)
        
        /**
         * Changes the actual PartBundle embedded within the handle.
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

    bundle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.core.PartBundleHandle' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.core.PartBundleHandle' objects>"
        '__doc__': '/**\n * This is a trivial class returned by PartBundleNode::get_bundle().  Its\n * purpose is to hold the actual PartBundle pointer contained within the\n * PartBundleNode, so that scene graph flatten operations can safely combine\n * or duplicate PartBundles as necessary without affecting high-level bundle\n * operations.\n *\n * The high-level Actor class defined in direct/src/actor, for instance, will\n * store a list of PartBundleHandles instead of on actual PartBundles, so that\n * it will be immune to changes from these flatten operations.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.PartBundleHandle' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE2C4B10>'
        'bundle': None, # (!) real value is "<attribute 'bundle' of 'panda3d.core.PartBundleHandle' objects>"
        'getBundle': None, # (!) real value is "<method 'getBundle' of 'panda3d.core.PartBundleHandle' objects>"
        'get_bundle': None, # (!) real value is "<method 'get_bundle' of 'panda3d.core.PartBundleHandle' objects>"
        'setBundle': None, # (!) real value is "<method 'setBundle' of 'panda3d.core.PartBundleHandle' objects>"
        'set_bundle': None, # (!) real value is "<method 'set_bundle' of 'panda3d.core.PartBundleHandle' objects>"
    }


