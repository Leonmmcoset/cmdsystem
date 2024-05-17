# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .RenderAttrib import RenderAttrib

class ColorAttrib(RenderAttrib):
    """
    /**
     * Indicates what color should be applied to renderable geometry.
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

    def getColor(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_color(ColorAttrib self)
        
        /**
         * If the type is T_flat or T_off, this returns the color that will be applied
         * to geometry.  If the type is T_vertex, this is meaningless.
         */
        """
        pass

    def getColorType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_color_type(ColorAttrib self)
        
        /**
         * Returns the type of color specified by this ColorAttrib.  The options are:
         *
         * T_vertex - use the vertex color specified in the geometry itself.
         *
         * T_flat - use the color specified in this ColorAttrib for all geometry.  You
         * can get this color via get_color().
         *
         * T_off - use the color white.
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

    def get_color(self, ColorAttrib_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_color(ColorAttrib self)
        
        /**
         * If the type is T_flat or T_off, this returns the color that will be applied
         * to geometry.  If the type is T_vertex, this is meaningless.
         */
        """
        pass

    def get_color_type(self, ColorAttrib_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_color_type(ColorAttrib self)
        
        /**
         * Returns the type of color specified by this ColorAttrib.  The options are:
         *
         * T_vertex - use the vertex color specified in the geometry itself.
         *
         * T_flat - use the color specified in this ColorAttrib for all geometry.  You
         * can get this color via get_color().
         *
         * T_off - use the color white.
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

    def makeFlat(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        make_flat(const LVecBase4f color)
        
        /**
         * Constructs a new ColorAttrib object that indicates geometry should be
         * rendered in the indicated color.
         */
        """
        pass

    def makeOff(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        make_off()
        
        /**
         * Constructs a new ColorAttrib object that indicates geometry should be
         * rendered in white.
         */
        """
        pass

    def makeVertex(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        make_vertex()
        
        /**
         * Constructs a new ColorAttrib object that indicates geometry should be
         * rendered according to its own vertex color.
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

    def make_flat(self, const_LVecBase4f_color): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        make_flat(const LVecBase4f color)
        
        /**
         * Constructs a new ColorAttrib object that indicates geometry should be
         * rendered in the indicated color.
         */
        """
        pass

    def make_off(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        make_off()
        
        /**
         * Constructs a new ColorAttrib object that indicates geometry should be
         * rendered in white.
         */
        """
        pass

    def make_vertex(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        make_vertex()
        
        /**
         * Constructs a new ColorAttrib object that indicates geometry should be
         * rendered according to its own vertex color.
         */
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    color = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    color_type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    class_slot = 6
    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        'TFlat': 1,
        'TOff': 2,
        'TVertex': 0,
        'T_flat': 1,
        'T_off': 2,
        'T_vertex': 0,
        '__doc__': '/**\n * Indicates what color should be applied to renderable geometry.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.ColorAttrib' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE295200>'
        'class_slot': None, # (!) real value is "<attribute 'class_slot' of 'panda3d.core.ColorAttrib'>"
        'color': None, # (!) real value is "<attribute 'color' of 'panda3d.core.ColorAttrib' objects>"
        'color_type': None, # (!) real value is "<attribute 'color_type' of 'panda3d.core.ColorAttrib' objects>"
        'getClassSlot': None, # (!) real value is '<staticmethod(<built-in method getClassSlot of type object at 0x00007FFCFE295200>)>'
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE295200>)>'
        'getColor': None, # (!) real value is "<method 'getColor' of 'panda3d.core.ColorAttrib' objects>"
        'getColorType': None, # (!) real value is "<method 'getColorType' of 'panda3d.core.ColorAttrib' objects>"
        'get_class_slot': None, # (!) real value is '<staticmethod(<built-in method get_class_slot of type object at 0x00007FFCFE295200>)>'
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE295200>)>'
        'get_color': None, # (!) real value is "<method 'get_color' of 'panda3d.core.ColorAttrib' objects>"
        'get_color_type': None, # (!) real value is "<method 'get_color_type' of 'panda3d.core.ColorAttrib' objects>"
        'makeDefault': None, # (!) real value is '<staticmethod(<built-in method makeDefault of type object at 0x00007FFCFE295200>)>'
        'makeFlat': None, # (!) real value is '<staticmethod(<built-in method makeFlat of type object at 0x00007FFCFE295200>)>'
        'makeOff': None, # (!) real value is '<staticmethod(<built-in method makeOff of type object at 0x00007FFCFE295200>)>'
        'makeVertex': None, # (!) real value is '<staticmethod(<built-in method makeVertex of type object at 0x00007FFCFE295200>)>'
        'make_default': None, # (!) real value is '<staticmethod(<built-in method make_default of type object at 0x00007FFCFE295200>)>'
        'make_flat': None, # (!) real value is '<staticmethod(<built-in method make_flat of type object at 0x00007FFCFE295200>)>'
        'make_off': None, # (!) real value is '<staticmethod(<built-in method make_off of type object at 0x00007FFCFE295200>)>'
        'make_vertex': None, # (!) real value is '<staticmethod(<built-in method make_vertex of type object at 0x00007FFCFE295200>)>'
    }
    TFlat = 1
    TOff = 2
    TVertex = 0
    T_flat = 1
    T_off = 2
    T_vertex = 0


