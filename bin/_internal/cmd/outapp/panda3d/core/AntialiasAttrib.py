# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .RenderAttrib import RenderAttrib

class AntialiasAttrib(RenderAttrib):
    """
    /**
     * Specifies whether or how to enable antialiasing, if supported by the
     * backend renderer.
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
        get_mode(AntialiasAttrib self)
        
        /**
         * Returns the specified antialias mode.
         */
        """
        pass

    def getModeQuality(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_mode_quality(AntialiasAttrib self)
        
        /**
         * Returns the specified antialias mode, with the type bits masked out.  This
         * therefore indicates only the requested quality settings: one of M_faster,
         * M_better, M_dont_care, or zero (unspecified).
         */
        """
        pass

    def getModeType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_mode_type(AntialiasAttrib self)
        
        /**
         * Returns the specified antialias mode, with the quality bits masked out.
         * This therefore indicates only the requested type of antialiasing: M_none,
         * M_auto, or some specific combination.
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

    def get_mode(self, AntialiasAttrib_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_mode(AntialiasAttrib self)
        
        /**
         * Returns the specified antialias mode.
         */
        """
        pass

    def get_mode_quality(self, AntialiasAttrib_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_mode_quality(AntialiasAttrib self)
        
        /**
         * Returns the specified antialias mode, with the type bits masked out.  This
         * therefore indicates only the requested quality settings: one of M_faster,
         * M_better, M_dont_care, or zero (unspecified).
         */
        """
        pass

    def get_mode_type(self, AntialiasAttrib_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_mode_type(AntialiasAttrib self)
        
        /**
         * Returns the specified antialias mode, with the quality bits masked out.
         * This therefore indicates only the requested type of antialiasing: M_none,
         * M_auto, or some specific combination.
         */
        """
        pass

    def make(self, int_mode): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        make(int mode)
        
        /**
         * Constructs a new AntialiasAttrib object.
         *
         * The mode should be either M_none, M_auto, or a union of any or all of
         * M_point, M_line, M_polygon, and M_multisample.  Also, in addition to the
         * above choices, it may include either of M_better of M_faster to specify a
         * performance/quality tradeoff hint.
         *
         * If M_none is specified, no antialiasing is performed.
         *
         * If M_multisample is specified, it means to use the special framebuffer
         * multisample bits for antialiasing, if it is available.  If so, the M_point,
         * M_line, and M_polygon modes are ignored.  This advanced antialiasing mode
         * is only available on certain graphics hardware.  If it is not available,
         * the M_multisample bit is ignored (and the other modes may be used instead,
         * if specified).
         *
         * M_point, M_line, and/or M_polygon specify per-primitive smoothing.  When
         * enabled, M_point and M_line may force transparency on.  M_polygon requires
         * a frame buffer that includes an alpha channel, and it works best if the
         * primitives are sorted front-to-back.
         *
         * If M_auto is specified, M_multisample is selected if it is available,
         * otherwise M_polygon is selected, unless drawing lines or points, in which
         * case M_line or M_point is selected (these two generally produce better
         * results than M_multisample)
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

    mode_quality = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    mode_type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    class_slot = 2
    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        'MAuto': 31,
        'MBetter': 64,
        'MDontCare': 96,
        'MFaster': 32,
        'MLine': 2,
        'MMultisample': 8,
        'MNone': 0,
        'MPoint': 1,
        'MPolygon': 4,
        'MTypeMask': 31,
        'M_auto': 31,
        'M_better': 64,
        'M_dont_care': 96,
        'M_faster': 32,
        'M_line': 2,
        'M_multisample': 8,
        'M_none': 0,
        'M_point': 1,
        'M_polygon': 4,
        'M_type_mask': 31,
        '__doc__': '/**\n * Specifies whether or how to enable antialiasing, if supported by the\n * backend renderer.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.AntialiasAttrib' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE2922E0>'
        'class_slot': None, # (!) real value is "<attribute 'class_slot' of 'panda3d.core.AntialiasAttrib'>"
        'getClassSlot': None, # (!) real value is '<staticmethod(<built-in method getClassSlot of type object at 0x00007FFCFE2922E0>)>'
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE2922E0>)>'
        'getMode': None, # (!) real value is "<method 'getMode' of 'panda3d.core.AntialiasAttrib' objects>"
        'getModeQuality': None, # (!) real value is "<method 'getModeQuality' of 'panda3d.core.AntialiasAttrib' objects>"
        'getModeType': None, # (!) real value is "<method 'getModeType' of 'panda3d.core.AntialiasAttrib' objects>"
        'get_class_slot': None, # (!) real value is '<staticmethod(<built-in method get_class_slot of type object at 0x00007FFCFE2922E0>)>'
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE2922E0>)>'
        'get_mode': None, # (!) real value is "<method 'get_mode' of 'panda3d.core.AntialiasAttrib' objects>"
        'get_mode_quality': None, # (!) real value is "<method 'get_mode_quality' of 'panda3d.core.AntialiasAttrib' objects>"
        'get_mode_type': None, # (!) real value is "<method 'get_mode_type' of 'panda3d.core.AntialiasAttrib' objects>"
        'make': None, # (!) real value is '<staticmethod(<built-in method make of type object at 0x00007FFCFE2922E0>)>'
        'makeDefault': None, # (!) real value is '<staticmethod(<built-in method makeDefault of type object at 0x00007FFCFE2922E0>)>'
        'make_default': None, # (!) real value is '<staticmethod(<built-in method make_default of type object at 0x00007FFCFE2922E0>)>'
        'mode': None, # (!) real value is "<attribute 'mode' of 'panda3d.core.AntialiasAttrib' objects>"
        'mode_quality': None, # (!) real value is "<attribute 'mode_quality' of 'panda3d.core.AntialiasAttrib' objects>"
        'mode_type': None, # (!) real value is "<attribute 'mode_type' of 'panda3d.core.AntialiasAttrib' objects>"
    }
    MAuto = 31
    MBetter = 64
    MDontCare = 96
    MFaster = 32
    MLine = 2
    MMultisample = 8
    MNone = 0
    MPoint = 1
    MPolygon = 4
    MTypeMask = 31
    M_auto = 31
    M_better = 64
    M_dont_care = 96
    M_faster = 32
    M_line = 2
    M_multisample = 8
    M_none = 0
    M_point = 1
    M_polygon = 4
    M_type_mask = 31


