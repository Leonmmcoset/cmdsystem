# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .RenderAttrib import RenderAttrib

class MaterialAttrib(RenderAttrib):
    """
    /**
     * Indicates which, if any, material should be applied to geometry.  The
     * material is used primarily to control lighting effects, and isn't necessary
     * (or useful) in the absence of lighting.
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

    def getMaterial(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_material(MaterialAttrib self)
        
        /**
         * If the MaterialAttrib is not an 'off' MaterialAttrib, returns the material
         * that is associated.  Otherwise, return NULL.
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

    def get_material(self, MaterialAttrib_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_material(MaterialAttrib self)
        
        /**
         * If the MaterialAttrib is not an 'off' MaterialAttrib, returns the material
         * that is associated.  Otherwise, return NULL.
         */
        """
        pass

    def isOff(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_off(MaterialAttrib self)
        
        /**
         * Returns true if the MaterialAttrib is an 'off' MaterialAttrib, indicating
         * that it should disable the use of materials.
         */
        """
        pass

    def is_off(self, MaterialAttrib_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_off(MaterialAttrib self)
        
        /**
         * Returns true if the MaterialAttrib is an 'off' MaterialAttrib, indicating
         * that it should disable the use of materials.
         */
        """
        pass

    def make(self, Material_material): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        make(Material material)
        
        /**
         * Constructs a new MaterialAttrib object suitable for rendering the indicated
         * material onto geometry.
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
         * Constructs a new MaterialAttrib object suitable for rendering unmateriald
         * geometry.
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
         * Constructs a new MaterialAttrib object suitable for rendering unmateriald
         * geometry.
         */
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    material = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    class_slot = 19
    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__doc__': "/**\n * Indicates which, if any, material should be applied to geometry.  The\n * material is used primarily to control lighting effects, and isn't necessary\n * (or useful) in the absence of lighting.\n */",
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.MaterialAttrib' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE298860>'
        'class_slot': None, # (!) real value is "<attribute 'class_slot' of 'panda3d.core.MaterialAttrib'>"
        'getClassSlot': None, # (!) real value is '<staticmethod(<built-in method getClassSlot of type object at 0x00007FFCFE298860>)>'
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE298860>)>'
        'getMaterial': None, # (!) real value is "<method 'getMaterial' of 'panda3d.core.MaterialAttrib' objects>"
        'get_class_slot': None, # (!) real value is '<staticmethod(<built-in method get_class_slot of type object at 0x00007FFCFE298860>)>'
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE298860>)>'
        'get_material': None, # (!) real value is "<method 'get_material' of 'panda3d.core.MaterialAttrib' objects>"
        'isOff': None, # (!) real value is "<method 'isOff' of 'panda3d.core.MaterialAttrib' objects>"
        'is_off': None, # (!) real value is "<method 'is_off' of 'panda3d.core.MaterialAttrib' objects>"
        'make': None, # (!) real value is '<staticmethod(<built-in method make of type object at 0x00007FFCFE298860>)>'
        'makeDefault': None, # (!) real value is '<staticmethod(<built-in method makeDefault of type object at 0x00007FFCFE298860>)>'
        'makeOff': None, # (!) real value is '<staticmethod(<built-in method makeOff of type object at 0x00007FFCFE298860>)>'
        'make_default': None, # (!) real value is '<staticmethod(<built-in method make_default of type object at 0x00007FFCFE298860>)>'
        'make_off': None, # (!) real value is '<staticmethod(<built-in method make_off of type object at 0x00007FFCFE298860>)>'
        'material': None, # (!) real value is "<attribute 'material' of 'panda3d.core.MaterialAttrib' objects>"
    }


