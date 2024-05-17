# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .RenderEffect import RenderEffect

class OccluderEffect(RenderEffect):
    """
    /**
     * This functions similarly to a LightAttrib or ClipPlaneAttrib.  It indicates
     * the set of occluders that modify the geometry at this level and below.
     * Unlike a ClipPlaneAttrib, an OccluderEffect takes effect immediately when
     * it is encountered during traversal, and thus can only add occluders; it may
     * not remove them.
     */
    """
    def addOnOccluder(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_on_occluder(OccluderEffect self, const NodePath occluder)
        
        /**
         * Returns a new OccluderEffect, just like this one, but with the indicated
         * occluder added to the list of occluders enabled by this effect.
         */
        """
        pass

    def add_on_occluder(self, OccluderEffect_self, const_NodePath_occluder): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_on_occluder(OccluderEffect self, const NodePath occluder)
        
        /**
         * Returns a new OccluderEffect, just like this one, but with the indicated
         * occluder added to the list of occluders enabled by this effect.
         */
        """
        pass

    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getNumOnOccluders(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_on_occluders(OccluderEffect self)
        
        /**
         * Returns the number of occluders that are enabled by the effectute.
         */
        """
        pass

    def getOnOccluder(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_on_occluder(OccluderEffect self, int n)
        
        /**
         * Returns the nth occluder enabled by the effectute, sorted in render order.
         */
        """
        pass

    def getOnOccluders(self, *args, **kwargs): # real signature unknown
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_num_on_occluders(self, OccluderEffect_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_on_occluders(OccluderEffect self)
        
        /**
         * Returns the number of occluders that are enabled by the effectute.
         */
        """
        pass

    def get_on_occluder(self, OccluderEffect_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_on_occluder(OccluderEffect self, int n)
        
        /**
         * Returns the nth occluder enabled by the effectute, sorted in render order.
         */
        """
        pass

    def get_on_occluders(self, *args, **kwargs): # real signature unknown
        pass

    def hasOnOccluder(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_on_occluder(OccluderEffect self, const NodePath occluder)
        
        /**
         * Returns true if the indicated occluder is enabled by the effect, false
         * otherwise.
         */
        """
        pass

    def has_on_occluder(self, OccluderEffect_self, const_NodePath_occluder): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_on_occluder(OccluderEffect self, const NodePath occluder)
        
        /**
         * Returns true if the indicated occluder is enabled by the effect, false
         * otherwise.
         */
        """
        pass

    def isIdentity(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_identity(OccluderEffect self)
        
        /**
         * Returns true if this is an identity effect: it does not change the set of
         * occluders in use.
         */
        """
        pass

    def is_identity(self, OccluderEffect_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_identity(OccluderEffect self)
        
        /**
         * Returns true if this is an identity effect: it does not change the set of
         * occluders in use.
         */
        """
        pass

    def make(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        make()
        
        /**
         * Constructs a new OccluderEffect object that does nothing.
         */
        """
        pass

    def removeOnOccluder(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        remove_on_occluder(OccluderEffect self, const NodePath occluder)
        
        /**
         * Returns a new OccluderEffect, just like this one, but with the indicated
         * occluder removed from the list of occluders enabled by this effect.
         */
        """
        pass

    def remove_on_occluder(self, OccluderEffect_self, const_NodePath_occluder): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        remove_on_occluder(OccluderEffect self, const NodePath occluder)
        
        /**
         * Returns a new OccluderEffect, just like this one, but with the indicated
         * occluder removed from the list of occluders enabled by this effect.
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
        '__doc__': '/**\n * This functions similarly to a LightAttrib or ClipPlaneAttrib.  It indicates\n * the set of occluders that modify the geometry at this level and below.\n * Unlike a ClipPlaneAttrib, an OccluderEffect takes effect immediately when\n * it is encountered during traversal, and thus can only add occluders; it may\n * not remove them.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.OccluderEffect' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE299C50>'
        'addOnOccluder': None, # (!) real value is "<method 'addOnOccluder' of 'panda3d.core.OccluderEffect' objects>"
        'add_on_occluder': None, # (!) real value is "<method 'add_on_occluder' of 'panda3d.core.OccluderEffect' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE299C50>)>'
        'getNumOnOccluders': None, # (!) real value is "<method 'getNumOnOccluders' of 'panda3d.core.OccluderEffect' objects>"
        'getOnOccluder': None, # (!) real value is "<method 'getOnOccluder' of 'panda3d.core.OccluderEffect' objects>"
        'getOnOccluders': None, # (!) real value is "<method 'getOnOccluders' of 'panda3d.core.OccluderEffect' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE299C50>)>'
        'get_num_on_occluders': None, # (!) real value is "<method 'get_num_on_occluders' of 'panda3d.core.OccluderEffect' objects>"
        'get_on_occluder': None, # (!) real value is "<method 'get_on_occluder' of 'panda3d.core.OccluderEffect' objects>"
        'get_on_occluders': None, # (!) real value is "<method 'get_on_occluders' of 'panda3d.core.OccluderEffect' objects>"
        'hasOnOccluder': None, # (!) real value is "<method 'hasOnOccluder' of 'panda3d.core.OccluderEffect' objects>"
        'has_on_occluder': None, # (!) real value is "<method 'has_on_occluder' of 'panda3d.core.OccluderEffect' objects>"
        'isIdentity': None, # (!) real value is "<method 'isIdentity' of 'panda3d.core.OccluderEffect' objects>"
        'is_identity': None, # (!) real value is "<method 'is_identity' of 'panda3d.core.OccluderEffect' objects>"
        'make': None, # (!) real value is '<staticmethod(<built-in method make of type object at 0x00007FFCFE299C50>)>'
        'removeOnOccluder': None, # (!) real value is "<method 'removeOnOccluder' of 'panda3d.core.OccluderEffect' objects>"
        'remove_on_occluder': None, # (!) real value is "<method 'remove_on_occluder' of 'panda3d.core.OccluderEffect' objects>"
    }


