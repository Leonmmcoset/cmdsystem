# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .RenderAttrib import RenderAttrib

class AlphaTestAttrib(RenderAttrib):
    """
    /**
     * Enables or disables writing of pixel to framebuffer based on its alpha
     * value relative to a reference alpha value
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

    def getMode(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_mode(AlphaTestAttrib self)
        
        /**
         * Returns the alpha write mode.
         */
        """
        pass

    def getReferenceAlpha(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_reference_alpha(AlphaTestAttrib self)
        
        /**
         * Returns the alpha reference value.
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

    def get_mode(self, AlphaTestAttrib_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_mode(AlphaTestAttrib self)
        
        /**
         * Returns the alpha write mode.
         */
        """
        pass

    def get_reference_alpha(self, AlphaTestAttrib_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_reference_alpha(AlphaTestAttrib self)
        
        /**
         * Returns the alpha reference value.
         */
        """
        pass

    def make(self, int_mode, float_reference_alpha): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        make(int mode, float reference_alpha)
        
        /**
         * Constructs a new AlphaTestAttrib object.
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

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    mode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    reference_alpha = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    class_slot = 1
    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__doc__': '/**\n * Enables or disables writing of pixel to framebuffer based on its alpha\n * value relative to a reference alpha value\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.AlphaTestAttrib' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE292110>'
        'class_slot': None, # (!) real value is "<attribute 'class_slot' of 'panda3d.core.AlphaTestAttrib'>"
        'getClassSlot': None, # (!) real value is '<staticmethod(<built-in method getClassSlot of type object at 0x00007FFCFE292110>)>'
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE292110>)>'
        'getMode': None, # (!) real value is "<method 'getMode' of 'panda3d.core.AlphaTestAttrib' objects>"
        'getReferenceAlpha': None, # (!) real value is "<method 'getReferenceAlpha' of 'panda3d.core.AlphaTestAttrib' objects>"
        'get_class_slot': None, # (!) real value is '<staticmethod(<built-in method get_class_slot of type object at 0x00007FFCFE292110>)>'
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE292110>)>'
        'get_mode': None, # (!) real value is "<method 'get_mode' of 'panda3d.core.AlphaTestAttrib' objects>"
        'get_reference_alpha': None, # (!) real value is "<method 'get_reference_alpha' of 'panda3d.core.AlphaTestAttrib' objects>"
        'make': None, # (!) real value is '<staticmethod(<built-in method make of type object at 0x00007FFCFE292110>)>'
        'makeDefault': None, # (!) real value is '<staticmethod(<built-in method makeDefault of type object at 0x00007FFCFE292110>)>'
        'make_default': None, # (!) real value is '<staticmethod(<built-in method make_default of type object at 0x00007FFCFE292110>)>'
        'mode': None, # (!) real value is "<attribute 'mode' of 'panda3d.core.AlphaTestAttrib' objects>"
        'reference_alpha': None, # (!) real value is "<attribute 'reference_alpha' of 'panda3d.core.AlphaTestAttrib' objects>"
    }


