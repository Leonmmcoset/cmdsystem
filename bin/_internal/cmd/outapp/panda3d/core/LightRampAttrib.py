# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .RenderAttrib import RenderAttrib

class LightRampAttrib(RenderAttrib):
    """
    /**
     * A Light Ramp is any unary operator that takes a rendered pixel as input,
     * and adjusts the brightness of that pixel.  For example, gamma correction is
     * a kind of light ramp.  So is HDR tone mapping.  So is cartoon shading.  See
     * the constructors for an explanation of each kind of ramp.
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

    def getLevel(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_level(LightRampAttrib self, int n)
        
        /**
         * Returns the nth lighting level.
         */
        """
        pass

    def getMode(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_mode(LightRampAttrib self)
        
        /**
         * Returns the LightRampAttrib mode.
         */
        """
        pass

    def getThreshold(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_threshold(LightRampAttrib self, int n)
        
        /**
         * Returns the nth threshold level.
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

    def get_level(self, LightRampAttrib_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_level(LightRampAttrib self, int n)
        
        /**
         * Returns the nth lighting level.
         */
        """
        pass

    def get_mode(self, LightRampAttrib_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_mode(LightRampAttrib self)
        
        /**
         * Returns the LightRampAttrib mode.
         */
        """
        pass

    def get_threshold(self, LightRampAttrib_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_threshold(LightRampAttrib self, int n)
        
        /**
         * Returns the nth threshold level.
         */
        """
        pass

    def makeDefault(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        make_default()
        
        /**
         * Constructs a new LightRampAttrib object.  This is the standard OpenGL
         * lighting ramp, which clamps the final light total to the 0-1 range.
         */
        """
        pass

    def makeDoubleThreshold(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        make_double_threshold(float thresh0, float lev0, float thresh1, float lev1)
        
        /**
         * Constructs a new LightRampAttrib object.  This causes the luminance of the
         * diffuse lighting contribution to be quantized using two thresholds:
         *
         * @code
         * if (original_luminance > threshold1) {
         *   luminance = level1;
         * } else if (original_luminance > threshold0) {
         *   luminance = level0;
         * } else {
         *   luminance = 0.0;
         * }
         * @endcode
         */
        """
        pass

    def makeHdr0(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        make_hdr0()
        
        /**
         * Constructs a new LightRampAttrib object.  This causes an HDR tone mapping
         * operation to be applied.
         *
         * Normally, brightness values greater than 1 cannot be distinguished from
         * each other, causing very brightly lit objects to wash out white and all
         * detail to be erased.  HDR tone mapping remaps brightness values in the
         * range 0-infinity into the range (0,1), making it possible to distinguish
         * detail in scenes whose brightness exceeds 1.
         *
         * However, the monitor has finite contrast.  Normally, all of that contrast
         * is used to represent brightnesses in the range 0-1.  The HDR0 tone mapping
         * operator 'steals' one quarter of that contrast to represent brightnesses in
         * the range 1-infinity.
         *
         * @code
         * FINAL_RGB = (RGB^3 + RGB^2 + RGB) / (RGB^3 + RGB^2 + RGB + 1)
         * @endcode
         */
        """
        pass

    def makeHdr1(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        make_hdr1()
        
        /**
         * Constructs a new LightRampAttrib object.  This causes an HDR tone mapping
         * operation to be applied.
         *
         * Normally, brightness values greater than 1 cannot be distinguished from
         * each other, causing very brightly lit objects to wash out white and all
         * detail to be erased.  HDR tone mapping remaps brightness values in the
         * range 0-infinity into the range (0,1), making it possible to distinguish
         * detail in scenes whose brightness exceeds 1.
         *
         * However, the monitor has finite contrast.  Normally, all of that contrast
         * is used to represent brightnesses in the range 0-1.  The HDR1 tone mapping
         * operator 'steals' one third of that contrast to represent brightnesses in
         * the range 1-infinity.
         *
         * @code
         * FINAL_RGB = (RGB^2 + RGB) / (RGB^2 + RGB + 1)
         * @endcode
         */
        """
        pass

    def makeHdr2(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        make_hdr2()
        
        /**
         * Constructs a new LightRampAttrib object.  This causes an HDR tone mapping
         * operation to be applied.
         *
         * Normally, brightness values greater than 1 cannot be distinguished from
         * each other, causing very brightly lit objects to wash out white and all
         * detail to be erased.  HDR tone mapping remaps brightness values in the
         * range 0-infinity into the range (0,1), making it possible to distinguish
         * detail in scenes whose brightness exceeds 1.
         *
         * However, the monitor has finite contrast.  Normally, all of that contrast
         * is used to represent brightnesses in the range 0-1.  The HDR2 tone mapping
         * operator 'steals' one half of that contrast to represent brightnesses in
         * the range 1-infinity.
         *
         * @code
         * FINAL_RGB = (RGB) / (RGB + 1)
         * @endcode
         */
        """
        pass

    def makeIdentity(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        make_identity()
        
        /**
         * Constructs a new LightRampAttrib object.  This differs from the usual
         * OpenGL lighting model in that it does not clamp the final lighting total to
         * (0,1).
         */
        """
        pass

    def makeSingleThreshold(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        make_single_threshold(float thresh0, float lev0)
        
        /**
         * Constructs a new LightRampAttrib object.  This causes the luminance of the
         * diffuse lighting contribution to be quantized using a single threshold:
         *
         * @code
         * if (original_luminance > threshold0) {
         *   luminance = level0;
         * } else {
         *   luminance = 0.0;
         * }
         * @endcode
         */
        """
        pass

    def make_default(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        make_default()
        
        /**
         * Constructs a new LightRampAttrib object.  This is the standard OpenGL
         * lighting ramp, which clamps the final light total to the 0-1 range.
         */
        """
        pass

    def make_double_threshold(self, float_thresh0, float_lev0, float_thresh1, float_lev1): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        make_double_threshold(float thresh0, float lev0, float thresh1, float lev1)
        
        /**
         * Constructs a new LightRampAttrib object.  This causes the luminance of the
         * diffuse lighting contribution to be quantized using two thresholds:
         *
         * @code
         * if (original_luminance > threshold1) {
         *   luminance = level1;
         * } else if (original_luminance > threshold0) {
         *   luminance = level0;
         * } else {
         *   luminance = 0.0;
         * }
         * @endcode
         */
        """
        pass

    def make_hdr0(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        make_hdr0()
        
        /**
         * Constructs a new LightRampAttrib object.  This causes an HDR tone mapping
         * operation to be applied.
         *
         * Normally, brightness values greater than 1 cannot be distinguished from
         * each other, causing very brightly lit objects to wash out white and all
         * detail to be erased.  HDR tone mapping remaps brightness values in the
         * range 0-infinity into the range (0,1), making it possible to distinguish
         * detail in scenes whose brightness exceeds 1.
         *
         * However, the monitor has finite contrast.  Normally, all of that contrast
         * is used to represent brightnesses in the range 0-1.  The HDR0 tone mapping
         * operator 'steals' one quarter of that contrast to represent brightnesses in
         * the range 1-infinity.
         *
         * @code
         * FINAL_RGB = (RGB^3 + RGB^2 + RGB) / (RGB^3 + RGB^2 + RGB + 1)
         * @endcode
         */
        """
        pass

    def make_hdr1(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        make_hdr1()
        
        /**
         * Constructs a new LightRampAttrib object.  This causes an HDR tone mapping
         * operation to be applied.
         *
         * Normally, brightness values greater than 1 cannot be distinguished from
         * each other, causing very brightly lit objects to wash out white and all
         * detail to be erased.  HDR tone mapping remaps brightness values in the
         * range 0-infinity into the range (0,1), making it possible to distinguish
         * detail in scenes whose brightness exceeds 1.
         *
         * However, the monitor has finite contrast.  Normally, all of that contrast
         * is used to represent brightnesses in the range 0-1.  The HDR1 tone mapping
         * operator 'steals' one third of that contrast to represent brightnesses in
         * the range 1-infinity.
         *
         * @code
         * FINAL_RGB = (RGB^2 + RGB) / (RGB^2 + RGB + 1)
         * @endcode
         */
        """
        pass

    def make_hdr2(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        make_hdr2()
        
        /**
         * Constructs a new LightRampAttrib object.  This causes an HDR tone mapping
         * operation to be applied.
         *
         * Normally, brightness values greater than 1 cannot be distinguished from
         * each other, causing very brightly lit objects to wash out white and all
         * detail to be erased.  HDR tone mapping remaps brightness values in the
         * range 0-infinity into the range (0,1), making it possible to distinguish
         * detail in scenes whose brightness exceeds 1.
         *
         * However, the monitor has finite contrast.  Normally, all of that contrast
         * is used to represent brightnesses in the range 0-1.  The HDR2 tone mapping
         * operator 'steals' one half of that contrast to represent brightnesses in
         * the range 1-infinity.
         *
         * @code
         * FINAL_RGB = (RGB) / (RGB + 1)
         * @endcode
         */
        """
        pass

    def make_identity(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        make_identity()
        
        /**
         * Constructs a new LightRampAttrib object.  This differs from the usual
         * OpenGL lighting model in that it does not clamp the final lighting total to
         * (0,1).
         */
        """
        pass

    def make_single_threshold(self, float_thresh0, float_lev0): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        make_single_threshold(float thresh0, float lev0)
        
        /**
         * Constructs a new LightRampAttrib object.  This causes the luminance of the
         * diffuse lighting contribution to be quantized using a single threshold:
         *
         * @code
         * if (original_luminance > threshold0) {
         *   luminance = level0;
         * } else {
         *   luminance = 0.0;
         * }
         * @endcode
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


    class_slot = 17
    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        'LRTDefault': 0,
        'LRTDoubleThreshold': 3,
        'LRTHdr0': 4,
        'LRTHdr1': 5,
        'LRTHdr2': 6,
        'LRTIdentity': 1,
        'LRTSingleThreshold': 2,
        'LRT_default': 0,
        'LRT_double_threshold': 3,
        'LRT_hdr0': 4,
        'LRT_hdr1': 5,
        'LRT_hdr2': 6,
        'LRT_identity': 1,
        'LRT_single_threshold': 2,
        '__doc__': '/**\n * A Light Ramp is any unary operator that takes a rendered pixel as input,\n * and adjusts the brightness of that pixel.  For example, gamma correction is\n * a kind of light ramp.  So is HDR tone mapping.  So is cartoon shading.  See\n * the constructors for an explanation of each kind of ramp.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.LightRampAttrib' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE297F50>'
        'class_slot': None, # (!) real value is "<attribute 'class_slot' of 'panda3d.core.LightRampAttrib'>"
        'getClassSlot': None, # (!) real value is '<staticmethod(<built-in method getClassSlot of type object at 0x00007FFCFE297F50>)>'
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE297F50>)>'
        'getLevel': None, # (!) real value is "<method 'getLevel' of 'panda3d.core.LightRampAttrib' objects>"
        'getMode': None, # (!) real value is "<method 'getMode' of 'panda3d.core.LightRampAttrib' objects>"
        'getThreshold': None, # (!) real value is "<method 'getThreshold' of 'panda3d.core.LightRampAttrib' objects>"
        'get_class_slot': None, # (!) real value is '<staticmethod(<built-in method get_class_slot of type object at 0x00007FFCFE297F50>)>'
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE297F50>)>'
        'get_level': None, # (!) real value is "<method 'get_level' of 'panda3d.core.LightRampAttrib' objects>"
        'get_mode': None, # (!) real value is "<method 'get_mode' of 'panda3d.core.LightRampAttrib' objects>"
        'get_threshold': None, # (!) real value is "<method 'get_threshold' of 'panda3d.core.LightRampAttrib' objects>"
        'makeDefault': None, # (!) real value is '<staticmethod(<built-in method makeDefault of type object at 0x00007FFCFE297F50>)>'
        'makeDoubleThreshold': None, # (!) real value is '<staticmethod(<built-in method makeDoubleThreshold of type object at 0x00007FFCFE297F50>)>'
        'makeHdr0': None, # (!) real value is '<staticmethod(<built-in method makeHdr0 of type object at 0x00007FFCFE297F50>)>'
        'makeHdr1': None, # (!) real value is '<staticmethod(<built-in method makeHdr1 of type object at 0x00007FFCFE297F50>)>'
        'makeHdr2': None, # (!) real value is '<staticmethod(<built-in method makeHdr2 of type object at 0x00007FFCFE297F50>)>'
        'makeIdentity': None, # (!) real value is '<staticmethod(<built-in method makeIdentity of type object at 0x00007FFCFE297F50>)>'
        'makeSingleThreshold': None, # (!) real value is '<staticmethod(<built-in method makeSingleThreshold of type object at 0x00007FFCFE297F50>)>'
        'make_default': None, # (!) real value is '<staticmethod(<built-in method make_default of type object at 0x00007FFCFE297F50>)>'
        'make_double_threshold': None, # (!) real value is '<staticmethod(<built-in method make_double_threshold of type object at 0x00007FFCFE297F50>)>'
        'make_hdr0': None, # (!) real value is '<staticmethod(<built-in method make_hdr0 of type object at 0x00007FFCFE297F50>)>'
        'make_hdr1': None, # (!) real value is '<staticmethod(<built-in method make_hdr1 of type object at 0x00007FFCFE297F50>)>'
        'make_hdr2': None, # (!) real value is '<staticmethod(<built-in method make_hdr2 of type object at 0x00007FFCFE297F50>)>'
        'make_identity': None, # (!) real value is '<staticmethod(<built-in method make_identity of type object at 0x00007FFCFE297F50>)>'
        'make_single_threshold': None, # (!) real value is '<staticmethod(<built-in method make_single_threshold of type object at 0x00007FFCFE297F50>)>'
        'mode': None, # (!) real value is "<attribute 'mode' of 'panda3d.core.LightRampAttrib' objects>"
    }
    LRTDefault = 0
    LRTDoubleThreshold = 3
    LRTHdr0 = 4
    LRTHdr1 = 5
    LRTHdr2 = 6
    LRTIdentity = 1
    LRTSingleThreshold = 2
    LRT_default = 0
    LRT_double_threshold = 3
    LRT_hdr0 = 4
    LRT_hdr1 = 5
    LRT_hdr2 = 6
    LRT_identity = 1
    LRT_single_threshold = 2


