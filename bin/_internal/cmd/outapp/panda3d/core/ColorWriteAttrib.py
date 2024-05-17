# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .RenderAttrib import RenderAttrib

class ColorWriteAttrib(RenderAttrib):
    """
    /**
     * Enables or disables writing to the color buffer.  This is primarily useful
     * for certain special effects in which it is important to write to the depth
     * buffer without affecting the color buffer.
     */
    """
    def getChannels(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_channels(ColorWriteAttrib self)
        
        /**
         * Returns the mask of color channels that are enabled by this attrib.
         */
        """
        pass

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

    def get_channels(self, ColorWriteAttrib_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_channels(ColorWriteAttrib self)
        
        /**
         * Returns the mask of color channels that are enabled by this attrib.
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

    def make(self, int_channels): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        make(int channels)
        
        /**
         * Constructs a new ColorWriteAttrib object.
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

    channels = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    CAll = 15
    CAlpha = 8
    CBlue = 4
    CGreen = 2
    class_slot = 9
    COff = 0
    CRed = 1
    CRgb = 7
    C_all = 15
    C_alpha = 8
    C_blue = 4
    C_green = 2
    C_off = 0
    C_red = 1
    C_rgb = 7
    DtoolClassDict = {
        'CAll': 15,
        'CAlpha': 8,
        'CBlue': 4,
        'CGreen': 2,
        'COff': 0,
        'CRed': 1,
        'CRgb': 7,
        'C_all': 15,
        'C_alpha': 8,
        'C_blue': 4,
        'C_green': 2,
        'C_off': 0,
        'C_red': 1,
        'C_rgb': 7,
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__doc__': '/**\n * Enables or disables writing to the color buffer.  This is primarily useful\n * for certain special effects in which it is important to write to the depth\n * buffer without affecting the color buffer.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.ColorWriteAttrib' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE295770>'
        'channels': None, # (!) real value is "<attribute 'channels' of 'panda3d.core.ColorWriteAttrib' objects>"
        'class_slot': None, # (!) real value is "<attribute 'class_slot' of 'panda3d.core.ColorWriteAttrib'>"
        'getChannels': None, # (!) real value is "<method 'getChannels' of 'panda3d.core.ColorWriteAttrib' objects>"
        'getClassSlot': None, # (!) real value is '<staticmethod(<built-in method getClassSlot of type object at 0x00007FFCFE295770>)>'
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE295770>)>'
        'get_channels': None, # (!) real value is "<method 'get_channels' of 'panda3d.core.ColorWriteAttrib' objects>"
        'get_class_slot': None, # (!) real value is '<staticmethod(<built-in method get_class_slot of type object at 0x00007FFCFE295770>)>'
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE295770>)>'
        'make': None, # (!) real value is '<staticmethod(<built-in method make of type object at 0x00007FFCFE295770>)>'
        'makeDefault': None, # (!) real value is '<staticmethod(<built-in method makeDefault of type object at 0x00007FFCFE295770>)>'
        'make_default': None, # (!) real value is '<staticmethod(<built-in method make_default of type object at 0x00007FFCFE295770>)>'
    }


