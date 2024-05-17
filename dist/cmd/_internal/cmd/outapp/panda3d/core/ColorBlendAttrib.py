# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .RenderAttrib import RenderAttrib

class ColorBlendAttrib(RenderAttrib):
    """
    /**
     * This specifies how colors are blended into the frame buffer, for special
     * effects.  This overrides transparency if transparency is also specified.
     */
    """
    def getAlphaMode(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_alpha_mode(ColorBlendAttrib self)
        
        /**
         * Returns the blending mode for the alpha channel.
         */
        """
        pass

    def getAlphaOperandA(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_alpha_operand_a(ColorBlendAttrib self)
        
        /**
         * Returns the alpha multiplier for the first component.
         */
        """
        pass

    def getAlphaOperandB(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_alpha_operand_b(ColorBlendAttrib self)
        
        /**
         * Returns the alpha multiplier for the second component.
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

    def getColor(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_color(ColorBlendAttrib self)
        
        /**
         * Returns the constant color associated with the attrib.
         */
        """
        pass

    def getMode(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_mode(ColorBlendAttrib self)
        
        /**
         * Returns the blending mode for the RGB channels.
         */
        """
        pass

    def getOperandA(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_operand_a(ColorBlendAttrib self)
        
        /**
         * Returns the RGB multiplier for the first component.
         */
        """
        pass

    def getOperandB(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_operand_b(ColorBlendAttrib self)
        
        /**
         * Returns the RGB multiplier for the second component.
         */
        """
        pass

    def get_alpha_mode(self, ColorBlendAttrib_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_alpha_mode(ColorBlendAttrib self)
        
        /**
         * Returns the blending mode for the alpha channel.
         */
        """
        pass

    def get_alpha_operand_a(self, ColorBlendAttrib_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_alpha_operand_a(ColorBlendAttrib self)
        
        /**
         * Returns the alpha multiplier for the first component.
         */
        """
        pass

    def get_alpha_operand_b(self, ColorBlendAttrib_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_alpha_operand_b(ColorBlendAttrib self)
        
        /**
         * Returns the alpha multiplier for the second component.
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

    def get_color(self, ColorBlendAttrib_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_color(ColorBlendAttrib self)
        
        /**
         * Returns the constant color associated with the attrib.
         */
        """
        pass

    def get_mode(self, ColorBlendAttrib_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_mode(ColorBlendAttrib self)
        
        /**
         * Returns the blending mode for the RGB channels.
         */
        """
        pass

    def get_operand_a(self, ColorBlendAttrib_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_operand_a(ColorBlendAttrib self)
        
        /**
         * Returns the RGB multiplier for the first component.
         */
        """
        pass

    def get_operand_b(self, ColorBlendAttrib_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_operand_b(ColorBlendAttrib self)
        
        /**
         * Returns the RGB multiplier for the second component.
         */
        """
        pass

    def involvesColorScale(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        involves_color_scale(ColorBlendAttrib self)
        involves_color_scale(int operand)
        
        /**
         * Returns true if the this attrib uses the color scale attrib, false
         * otherwise.
         */
        
        /**
         * Returns true if the indicated operand uses the color scale attrib, false
         * otherwise.
         */
        """
        pass

    def involvesConstantColor(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        involves_constant_color(ColorBlendAttrib self)
        involves_constant_color(int operand)
        
        /**
         * Returns true if the this attrib uses the constant color, false otherwise.
         */
        
        /**
         * Returns true if the indicated operand uses the constant color, false
         * otherwise.
         */
        """
        pass

    def involves_color_scale(self, ColorBlendAttrib_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        involves_color_scale(ColorBlendAttrib self)
        involves_color_scale(int operand)
        
        /**
         * Returns true if the this attrib uses the color scale attrib, false
         * otherwise.
         */
        
        /**
         * Returns true if the indicated operand uses the color scale attrib, false
         * otherwise.
         */
        """
        pass

    def involves_constant_color(self, ColorBlendAttrib_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        involves_constant_color(ColorBlendAttrib self)
        involves_constant_color(int operand)
        
        /**
         * Returns true if the this attrib uses the constant color, false otherwise.
         */
        
        /**
         * Returns true if the indicated operand uses the constant color, false
         * otherwise.
         */
        """
        pass

    def make(self, int_mode): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        make(int mode)
        make(int mode, int a, int b)
        make(int mode, int a, int b, const LVecBase4f color)
        make(int rgb_mode, int rgb_a, int rgb_b, int alpha_mode, int alpha_a, int alpha_b, const LVecBase4f color)
        
        /**
         * Constructs a new ColorBlendAttrib object.
         *
         * @deprecated Use the three- or four-parameter constructor instead.
         */
        
        /**
         * Constructs a new ColorBlendAttrib object that enables special-effect
         * blending.  This supercedes transparency.  The given mode and operands are
         * used for both the RGB and alpha channels.
         */
        
        /**
         * Constructs a new ColorBlendAttrib object that enables special-effect
         * blending.  This supercedes transparency.  This form is used to specify
         * separate blending parameters for the RGB and alpha channels.
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
         * Constructs a new ColorBlendAttrib object that disables special-effect
         * blending, allowing normal transparency to be used instead.
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
         * Constructs a new ColorBlendAttrib object that disables special-effect
         * blending, allowing normal transparency to be used instead.
         */
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    alpha_mode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    alpha_operand_a = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    alpha_operand_b = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    color = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    rgb_mode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    rgb_operand_a = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    rgb_operand_b = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    class_slot = 7
    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        'MAdd': 1,
        'MInvSubtract': 3,
        'MMax': 5,
        'MMin': 4,
        'MNone': 0,
        'MSubtract': 2,
        'M_add': 1,
        'M_inv_subtract': 3,
        'M_max': 5,
        'M_min': 4,
        'M_none': 0,
        'M_subtract': 2,
        'OAlphaScale': 21,
        'OColorScale': 19,
        'OConstantAlpha': 12,
        'OConstantColor': 10,
        'OFbufferAlpha': 8,
        'OFbufferColor': 4,
        'OIncoming1Alpha': 17,
        'OIncoming1Color': 15,
        'OIncomingAlpha': 6,
        'OIncomingColor': 2,
        'OIncomingColorSaturate': 14,
        'OOne': 1,
        'OOneMinusAlphaScale': 22,
        'OOneMinusColorScale': 20,
        'OOneMinusConstantAlpha': 13,
        'OOneMinusConstantColor': 11,
        'OOneMinusFbufferAlpha': 9,
        'OOneMinusFbufferColor': 5,
        'OOneMinusIncoming1Alpha': 18,
        'OOneMinusIncoming1Color': 16,
        'OOneMinusIncomingAlpha': 7,
        'OOneMinusIncomingColor': 3,
        'OZero': 0,
        'O_alpha_scale': 21,
        'O_color_scale': 19,
        'O_constant_alpha': 12,
        'O_constant_color': 10,
        'O_fbuffer_alpha': 8,
        'O_fbuffer_color': 4,
        'O_incoming1_alpha': 17,
        'O_incoming1_color': 15,
        'O_incoming_alpha': 6,
        'O_incoming_color': 2,
        'O_incoming_color_saturate': 14,
        'O_one': 1,
        'O_one_minus_alpha_scale': 22,
        'O_one_minus_color_scale': 20,
        'O_one_minus_constant_alpha': 13,
        'O_one_minus_constant_color': 11,
        'O_one_minus_fbuffer_alpha': 9,
        'O_one_minus_fbuffer_color': 5,
        'O_one_minus_incoming1_alpha': 18,
        'O_one_minus_incoming1_color': 16,
        'O_one_minus_incoming_alpha': 7,
        'O_one_minus_incoming_color': 3,
        'O_zero': 0,
        '__doc__': '/**\n * This specifies how colors are blended into the frame buffer, for special\n * effects.  This overrides transparency if transparency is also specified.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.ColorBlendAttrib' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE2953D0>'
        'alpha_mode': None, # (!) real value is "<attribute 'alpha_mode' of 'panda3d.core.ColorBlendAttrib' objects>"
        'alpha_operand_a': None, # (!) real value is "<attribute 'alpha_operand_a' of 'panda3d.core.ColorBlendAttrib' objects>"
        'alpha_operand_b': None, # (!) real value is "<attribute 'alpha_operand_b' of 'panda3d.core.ColorBlendAttrib' objects>"
        'class_slot': None, # (!) real value is "<attribute 'class_slot' of 'panda3d.core.ColorBlendAttrib'>"
        'color': None, # (!) real value is "<attribute 'color' of 'panda3d.core.ColorBlendAttrib' objects>"
        'getAlphaMode': None, # (!) real value is "<method 'getAlphaMode' of 'panda3d.core.ColorBlendAttrib' objects>"
        'getAlphaOperandA': None, # (!) real value is "<method 'getAlphaOperandA' of 'panda3d.core.ColorBlendAttrib' objects>"
        'getAlphaOperandB': None, # (!) real value is "<method 'getAlphaOperandB' of 'panda3d.core.ColorBlendAttrib' objects>"
        'getClassSlot': None, # (!) real value is '<staticmethod(<built-in method getClassSlot of type object at 0x00007FFCFE2953D0>)>'
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE2953D0>)>'
        'getColor': None, # (!) real value is "<method 'getColor' of 'panda3d.core.ColorBlendAttrib' objects>"
        'getMode': None, # (!) real value is "<method 'getMode' of 'panda3d.core.ColorBlendAttrib' objects>"
        'getOperandA': None, # (!) real value is "<method 'getOperandA' of 'panda3d.core.ColorBlendAttrib' objects>"
        'getOperandB': None, # (!) real value is "<method 'getOperandB' of 'panda3d.core.ColorBlendAttrib' objects>"
        'get_alpha_mode': None, # (!) real value is "<method 'get_alpha_mode' of 'panda3d.core.ColorBlendAttrib' objects>"
        'get_alpha_operand_a': None, # (!) real value is "<method 'get_alpha_operand_a' of 'panda3d.core.ColorBlendAttrib' objects>"
        'get_alpha_operand_b': None, # (!) real value is "<method 'get_alpha_operand_b' of 'panda3d.core.ColorBlendAttrib' objects>"
        'get_class_slot': None, # (!) real value is '<staticmethod(<built-in method get_class_slot of type object at 0x00007FFCFE2953D0>)>'
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE2953D0>)>'
        'get_color': None, # (!) real value is "<method 'get_color' of 'panda3d.core.ColorBlendAttrib' objects>"
        'get_mode': None, # (!) real value is "<method 'get_mode' of 'panda3d.core.ColorBlendAttrib' objects>"
        'get_operand_a': None, # (!) real value is "<method 'get_operand_a' of 'panda3d.core.ColorBlendAttrib' objects>"
        'get_operand_b': None, # (!) real value is "<method 'get_operand_b' of 'panda3d.core.ColorBlendAttrib' objects>"
        'involvesColorScale': None, # (!) real value is "<method 'involvesColorScale' of 'panda3d.core.ColorBlendAttrib' objects>"
        'involvesConstantColor': None, # (!) real value is "<method 'involvesConstantColor' of 'panda3d.core.ColorBlendAttrib' objects>"
        'involves_color_scale': None, # (!) real value is "<method 'involves_color_scale' of 'panda3d.core.ColorBlendAttrib' objects>"
        'involves_constant_color': None, # (!) real value is "<method 'involves_constant_color' of 'panda3d.core.ColorBlendAttrib' objects>"
        'make': None, # (!) real value is '<staticmethod(<built-in method make of type object at 0x00007FFCFE2953D0>)>'
        'makeDefault': None, # (!) real value is '<staticmethod(<built-in method makeDefault of type object at 0x00007FFCFE2953D0>)>'
        'makeOff': None, # (!) real value is '<staticmethod(<built-in method makeOff of type object at 0x00007FFCFE2953D0>)>'
        'make_default': None, # (!) real value is '<staticmethod(<built-in method make_default of type object at 0x00007FFCFE2953D0>)>'
        'make_off': None, # (!) real value is '<staticmethod(<built-in method make_off of type object at 0x00007FFCFE2953D0>)>'
        'rgb_mode': None, # (!) real value is "<attribute 'rgb_mode' of 'panda3d.core.ColorBlendAttrib' objects>"
        'rgb_operand_a': None, # (!) real value is "<attribute 'rgb_operand_a' of 'panda3d.core.ColorBlendAttrib' objects>"
        'rgb_operand_b': None, # (!) real value is "<attribute 'rgb_operand_b' of 'panda3d.core.ColorBlendAttrib' objects>"
    }
    MAdd = 1
    MInvSubtract = 3
    MMax = 5
    MMin = 4
    MNone = 0
    MSubtract = 2
    M_add = 1
    M_inv_subtract = 3
    M_max = 5
    M_min = 4
    M_none = 0
    M_subtract = 2
    OAlphaScale = 21
    OColorScale = 19
    OConstantAlpha = 12
    OConstantColor = 10
    OFbufferAlpha = 8
    OFbufferColor = 4
    OIncoming1Alpha = 17
    OIncoming1Color = 15
    OIncomingAlpha = 6
    OIncomingColor = 2
    OIncomingColorSaturate = 14
    OOne = 1
    OOneMinusAlphaScale = 22
    OOneMinusColorScale = 20
    OOneMinusConstantAlpha = 13
    OOneMinusConstantColor = 11
    OOneMinusFbufferAlpha = 9
    OOneMinusFbufferColor = 5
    OOneMinusIncoming1Alpha = 18
    OOneMinusIncoming1Color = 16
    OOneMinusIncomingAlpha = 7
    OOneMinusIncomingColor = 3
    OZero = 0
    O_alpha_scale = 21
    O_color_scale = 19
    O_constant_alpha = 12
    O_constant_color = 10
    O_fbuffer_alpha = 8
    O_fbuffer_color = 4
    O_incoming1_alpha = 17
    O_incoming1_color = 15
    O_incoming_alpha = 6
    O_incoming_color = 2
    O_incoming_color_saturate = 14
    O_one = 1
    O_one_minus_alpha_scale = 22
    O_one_minus_color_scale = 20
    O_one_minus_constant_alpha = 13
    O_one_minus_constant_color = 11
    O_one_minus_fbuffer_alpha = 9
    O_one_minus_fbuffer_color = 5
    O_one_minus_incoming1_alpha = 18
    O_one_minus_incoming1_color = 16
    O_one_minus_incoming_alpha = 7
    O_one_minus_incoming_color = 3
    O_zero = 0


