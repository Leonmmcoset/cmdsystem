# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .RenderAttrib import RenderAttrib

class FogAttrib(RenderAttrib):
    """
    /**
     * Applies a Fog to the geometry at and below this node.
     */
    """
    def getClassSlot(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_slot()
        """
        pass

    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getFog(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_fog(FogAttrib self)
        
        /**
         * If the FogAttrib is not an 'off' FogAttrib, returns the fog that is
         * associated.  Otherwise, return NULL.
         */
        """
        pass

    def get_class_slot(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_slot()
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_fog(self, FogAttrib_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_fog(FogAttrib self)
        
        /**
         * If the FogAttrib is not an 'off' FogAttrib, returns the fog that is
         * associated.  Otherwise, return NULL.
         */
        """
        pass

    def isOff(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_off(FogAttrib self)
        
        /**
         * Returns true if the FogAttrib is an 'off' FogAttrib, indicating that it
         * should disable fog.
         */
        """
        pass

    def is_off(self, FogAttrib_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_off(FogAttrib self)
        
        /**
         * Returns true if the FogAttrib is an 'off' FogAttrib, indicating that it
         * should disable fog.
         */
        """
        pass

    def make(self, Fog_fog): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        make(Fog fog)
        
        /**
         * Constructs a new FogAttrib object suitable for rendering the indicated fog
         * onto geometry.
         */
        """
        pass

    def makeDefault(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        make_default()
        
        /**
         * Returns a RenderAttrib that corresponds to whatever the standard default
         * properties for render attributes of this type ought to be.
         */
        """
        pass

    def makeOff(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        make_off()
        
        /**
         * Constructs a new FogAttrib object suitable for rendering unfogd geometry.
         */
        """
        pass

    def make_default(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        make_default()
        
        /**
         * Returns a RenderAttrib that corresponds to whatever the standard default
         * properties for render attributes of this type ought to be.
         */
        """
        pass

    def make_off(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        make_off()
        
        /**
         * Constructs a new FogAttrib object suitable for rendering unfogd geometry.
         */
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    fog = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    class_slot = 15
    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__doc__': '/**\n * Applies a Fog to the geometry at and below this node.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.FogAttrib' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE296B60>'
        'class_slot': None, # (!) real value is "<attribute 'class_slot' of 'panda3d.core.FogAttrib'>"
        'fog': None, # (!) real value is "<attribute 'fog' of 'panda3d.core.FogAttrib' objects>"
        'getClassSlot': None, # (!) real value is '<staticmethod(<built-in method getClassSlot of type object at 0x00007FFCFE296B60>)>'
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE296B60>)>'
        'getFog': None, # (!) real value is "<method 'getFog' of 'panda3d.core.FogAttrib' objects>"
        'get_class_slot': None, # (!) real value is '<staticmethod(<built-in method get_class_slot of type object at 0x00007FFCFE296B60>)>'
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE296B60>)>'
        'get_fog': None, # (!) real value is "<method 'get_fog' of 'panda3d.core.FogAttrib' objects>"
        'isOff': None, # (!) real value is "<method 'isOff' of 'panda3d.core.FogAttrib' objects>"
        'is_off': None, # (!) real value is "<method 'is_off' of 'panda3d.core.FogAttrib' objects>"
        'make': None, # (!) real value is '<staticmethod(<built-in method make of type object at 0x00007FFCFE296B60>)>'
        'makeDefault': None, # (!) real value is '<staticmethod(<built-in method makeDefault of type object at 0x00007FFCFE296B60>)>'
        'makeOff': None, # (!) real value is '<staticmethod(<built-in method makeOff of type object at 0x00007FFCFE296B60>)>'
        'make_default': None, # (!) real value is '<staticmethod(<built-in method make_default of type object at 0x00007FFCFE296B60>)>'
        'make_off': None, # (!) real value is '<staticmethod(<built-in method make_off of type object at 0x00007FFCFE296B60>)>'
    }


