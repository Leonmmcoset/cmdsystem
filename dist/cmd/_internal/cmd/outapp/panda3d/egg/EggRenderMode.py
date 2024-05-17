# encoding: utf-8
# module panda3d.egg
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\egg.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import panda3d.core as __panda3d_core


class EggRenderMode(__dtoolconfig.DTOOL_SUPER_BASE):
    """
    /**
     * This class stores miscellaneous rendering properties that is associated
     * with geometry, and which may be set on the geometry primitive level, on the
     * group above it, or indirectly via a texture.  It's intended to be a base
     * class for egg objects that can have these properties set.
     *
     * This class cannot inherit from EggObject, because it causes problems at the
     * EggPolygon level with multiple appearances of the EggObject base class.
     * And making EggObject a virtual base class is just no fun.
     */
    """
    def assign(self, const_EggRenderMode_self, const_EggRenderMode_copy): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        assign(const EggRenderMode self, const EggRenderMode copy)
        
        /**
         *
         */
        """
        pass

    def clearBin(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_bin(const EggRenderMode self)
        
        /**
         * Removes the bin name that was set for this particular object.  See
         * set_bin().
         */
        """
        pass

    def clearDepthOffset(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_depth_offset(const EggRenderMode self)
        
        /**
         * Removes the depth-offset flag from this particular object.  See
         * set_depth_offset().
         */
        """
        pass

    def clearDrawOrder(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_draw_order(const EggRenderMode self)
        
        /**
         * Removes the draw-order flag from this particular object.  See
         * set_draw_order().
         */
        """
        pass

    def clear_bin(self, const_EggRenderMode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_bin(const EggRenderMode self)
        
        /**
         * Removes the bin name that was set for this particular object.  See
         * set_bin().
         */
        """
        pass

    def clear_depth_offset(self, const_EggRenderMode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_depth_offset(const EggRenderMode self)
        
        /**
         * Removes the depth-offset flag from this particular object.  See
         * set_depth_offset().
         */
        """
        pass

    def clear_draw_order(self, const_EggRenderMode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_draw_order(const EggRenderMode self)
        
        /**
         * Removes the draw-order flag from this particular object.  See
         * set_draw_order().
         */
        """
        pass

    def getAlphaMode(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_alpha_mode(EggRenderMode self)
        
        /**
         * Returns the alpha mode that was set, or AM_unspecified if nothing was set.
         * See set_alpha_mode().
         */
        """
        pass

    def getBin(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_bin(EggRenderMode self)
        
        /**
         * Returns the bin name that has been set for this particular object, if any.
         * See set_bin().
         */
        """
        pass

    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getDepthOffset(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_depth_offset(EggRenderMode self)
        
        /**
         * Returns the "depth-offset" flag as set for this particular object.  See
         * set_depth_offset().
         */
        """
        pass

    def getDepthTestMode(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_depth_test_mode(EggRenderMode self)
        
        /**
         * Returns the depth_test mode that was set, or DTM_unspecified if nothing was
         * set.  See set_depth_test_mode().
         */
        """
        pass

    def getDepthWriteMode(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_depth_write_mode(EggRenderMode self)
        
        /**
         * Returns the depth_write mode that was set, or DWM_unspecified if nothing
         * was set.  See set_depth_write_mode().
         */
        """
        pass

    def getDrawOrder(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_draw_order(EggRenderMode self)
        
        /**
         * Returns the "draw-order" flag as set for this particular object.  See
         * set_draw_order().
         */
        """
        pass

    def getVisibilityMode(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_visibility_mode(EggRenderMode self)
        
        /**
         * Returns the visibility mode that was set, or VM_unspecified if nothing was
         * set.  See set_visibility_mode().
         */
        """
        pass

    def get_alpha_mode(self, EggRenderMode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_alpha_mode(EggRenderMode self)
        
        /**
         * Returns the alpha mode that was set, or AM_unspecified if nothing was set.
         * See set_alpha_mode().
         */
        """
        pass

    def get_bin(self, EggRenderMode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_bin(EggRenderMode self)
        
        /**
         * Returns the bin name that has been set for this particular object, if any.
         * See set_bin().
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_depth_offset(self, EggRenderMode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_depth_offset(EggRenderMode self)
        
        /**
         * Returns the "depth-offset" flag as set for this particular object.  See
         * set_depth_offset().
         */
        """
        pass

    def get_depth_test_mode(self, EggRenderMode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_depth_test_mode(EggRenderMode self)
        
        /**
         * Returns the depth_test mode that was set, or DTM_unspecified if nothing was
         * set.  See set_depth_test_mode().
         */
        """
        pass

    def get_depth_write_mode(self, EggRenderMode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_depth_write_mode(EggRenderMode self)
        
        /**
         * Returns the depth_write mode that was set, or DWM_unspecified if nothing
         * was set.  See set_depth_write_mode().
         */
        """
        pass

    def get_draw_order(self, EggRenderMode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_draw_order(EggRenderMode self)
        
        /**
         * Returns the "draw-order" flag as set for this particular object.  See
         * set_draw_order().
         */
        """
        pass

    def get_visibility_mode(self, EggRenderMode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_visibility_mode(EggRenderMode self)
        
        /**
         * Returns the visibility mode that was set, or VM_unspecified if nothing was
         * set.  See set_visibility_mode().
         */
        """
        pass

    def hasBin(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_bin(EggRenderMode self)
        
        /**
         * Returns true if a bin name has been set for this particular object.  See
         * set_bin().
         */
        """
        pass

    def hasDepthOffset(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_depth_offset(EggRenderMode self)
        
        /**
         * Returns true if the depth-offset flag has been set for this particular
         * object.  See set_depth_offset().
         */
        """
        pass

    def hasDrawOrder(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_draw_order(EggRenderMode self)
        
        /**
         * Returns true if the draw-order flag has been set for this particular
         * object.  See set_draw_order().
         */
        """
        pass

    def has_bin(self, EggRenderMode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_bin(EggRenderMode self)
        
        /**
         * Returns true if a bin name has been set for this particular object.  See
         * set_bin().
         */
        """
        pass

    def has_depth_offset(self, EggRenderMode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_depth_offset(EggRenderMode self)
        
        /**
         * Returns true if the depth-offset flag has been set for this particular
         * object.  See set_depth_offset().
         */
        """
        pass

    def has_draw_order(self, EggRenderMode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_draw_order(EggRenderMode self)
        
        /**
         * Returns true if the draw-order flag has been set for this particular
         * object.  See set_draw_order().
         */
        """
        pass

    def setAlphaMode(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_alpha_mode(const EggRenderMode self, int mode)
        
        /**
         * Specifies precisely how the transparency for this geometry should be
         * achieved, or if it should be used.  The default, AM_unspecified, is to use
         * transparency if the geometry has a color whose alpha value is non-1, or if
         * it has a four-channel texture applied; otherwise, AM_on forces transparency
         * on, and AM_off forces it off.  The other flavors of transparency are
         * specific ways to turn on transparency, which may or may not be supported by
         * a particular rendering backend.
         */
        """
        pass

    def setBin(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_bin(const EggRenderMode self, str bin)
        
        /**
         * Sets the "bin" string for this particular object.  This names a particular
         * bin in which the object should be rendered.  The exact meaning of a bin is
         * implementation defined, but generally a GeomBin matching each bin name must
         * also be specifically added to the rendering engine (e.g.  the
         * CullTraverser) in use for this to work.  See also set_draw_order().
         */
        """
        pass

    def setDepthOffset(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_depth_offset(const EggRenderMode self, int bias)
        
        /**
         * Sets the "depth-offset" flag associated with this object.  This adds or
         * subtracts an offset bias into the depth buffer.  See also DepthOffsetAttrib
         * and NodePath::set_depth_offset().
         */
        """
        pass

    def setDepthTestMode(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_depth_test_mode(const EggRenderMode self, int mode)
        
        /**
         * Specifies whether this geometry should be tested against the depth buffer
         * when it is drawn (assuming the rendering backend provides a depth buffer).
         * Note that this is different, and independent from, the depth_write mode.
         */
        """
        pass

    def setDepthWriteMode(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_depth_write_mode(const EggRenderMode self, int mode)
        
        /**
         * Specifies whether writes should be made to the depth buffer (assuming the
         * rendering backend provides a depth buffer) when rendering this geometry.
         */
        """
        pass

    def setDrawOrder(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_draw_order(const EggRenderMode self, int order)
        
        /**
         * Sets the "draw-order" flag associated with this object.  This specifies a
         * particular order in which objects of this type should be drawn, within the
         * specified bin.  If a bin is not explicitly specified, "fixed" is used.  See
         * also set_bin().
         */
        """
        pass

    def setVisibilityMode(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_visibility_mode(const EggRenderMode self, int mode)
        
        /**
         * Specifies whether this geometry is to be considered normally visible, or
         * hidden.  If it is hidden, it is either not loaded into the scene graph at
         * all, or loaded as a "stashed" node, according to the setting of egg-
         * suppress-hidden.
         */
        """
        pass

    def set_alpha_mode(self, const_EggRenderMode_self, int_mode): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_alpha_mode(const EggRenderMode self, int mode)
        
        /**
         * Specifies precisely how the transparency for this geometry should be
         * achieved, or if it should be used.  The default, AM_unspecified, is to use
         * transparency if the geometry has a color whose alpha value is non-1, or if
         * it has a four-channel texture applied; otherwise, AM_on forces transparency
         * on, and AM_off forces it off.  The other flavors of transparency are
         * specific ways to turn on transparency, which may or may not be supported by
         * a particular rendering backend.
         */
        """
        pass

    def set_bin(self, const_EggRenderMode_self, str_bin): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_bin(const EggRenderMode self, str bin)
        
        /**
         * Sets the "bin" string for this particular object.  This names a particular
         * bin in which the object should be rendered.  The exact meaning of a bin is
         * implementation defined, but generally a GeomBin matching each bin name must
         * also be specifically added to the rendering engine (e.g.  the
         * CullTraverser) in use for this to work.  See also set_draw_order().
         */
        """
        pass

    def set_depth_offset(self, const_EggRenderMode_self, int_bias): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_depth_offset(const EggRenderMode self, int bias)
        
        /**
         * Sets the "depth-offset" flag associated with this object.  This adds or
         * subtracts an offset bias into the depth buffer.  See also DepthOffsetAttrib
         * and NodePath::set_depth_offset().
         */
        """
        pass

    def set_depth_test_mode(self, const_EggRenderMode_self, int_mode): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_depth_test_mode(const EggRenderMode self, int mode)
        
        /**
         * Specifies whether this geometry should be tested against the depth buffer
         * when it is drawn (assuming the rendering backend provides a depth buffer).
         * Note that this is different, and independent from, the depth_write mode.
         */
        """
        pass

    def set_depth_write_mode(self, const_EggRenderMode_self, int_mode): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_depth_write_mode(const EggRenderMode self, int mode)
        
        /**
         * Specifies whether writes should be made to the depth buffer (assuming the
         * rendering backend provides a depth buffer) when rendering this geometry.
         */
        """
        pass

    def set_draw_order(self, const_EggRenderMode_self, int_order): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_draw_order(const EggRenderMode self, int order)
        
        /**
         * Sets the "draw-order" flag associated with this object.  This specifies a
         * particular order in which objects of this type should be drawn, within the
         * specified bin.  If a bin is not explicitly specified, "fixed" is used.  See
         * also set_bin().
         */
        """
        pass

    def set_visibility_mode(self, const_EggRenderMode_self, int_mode): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_visibility_mode(const EggRenderMode self, int mode)
        
        /**
         * Specifies whether this geometry is to be considered normally visible, or
         * hidden.  If it is hidden, it is either not loaded into the scene graph at
         * all, or loaded as a "stashed" node, according to the setting of egg-
         * suppress-hidden.
         */
        """
        pass

    def stringAlphaMode(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        string_alpha_mode(str string)
        
        /**
         * Returns the AlphaMode value associated with the given string
         * representation, or AM_unspecified if the string does not match any known
         * AlphaMode value.
         */
        """
        pass

    def stringDepthTestMode(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        string_depth_test_mode(str string)
        
        /**
         * Returns the DepthTestMode value associated with the given string
         * representation, or DTM_unspecified if the string does not match any known
         * DepthTestMode value.
         */
        """
        pass

    def stringDepthWriteMode(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        string_depth_write_mode(str string)
        
        /**
         * Returns the DepthWriteMode value associated with the given string
         * representation, or DWM_unspecified if the string does not match any known
         * DepthWriteMode value.
         */
        """
        pass

    def stringVisibilityMode(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        string_visibility_mode(str string)
        
        /**
         * Returns the HiddenMode value associated with the given string
         * representation, or VM_unspecified if the string does not match any known
         * HiddenMode value.
         */
        """
        pass

    def string_alpha_mode(self, str_string): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        string_alpha_mode(str string)
        
        /**
         * Returns the AlphaMode value associated with the given string
         * representation, or AM_unspecified if the string does not match any known
         * AlphaMode value.
         */
        """
        pass

    def string_depth_test_mode(self, str_string): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        string_depth_test_mode(str string)
        
        /**
         * Returns the DepthTestMode value associated with the given string
         * representation, or DTM_unspecified if the string does not match any known
         * DepthTestMode value.
         */
        """
        pass

    def string_depth_write_mode(self, str_string): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        string_depth_write_mode(str string)
        
        /**
         * Returns the DepthWriteMode value associated with the given string
         * representation, or DWM_unspecified if the string does not match any known
         * DepthWriteMode value.
         */
        """
        pass

    def string_visibility_mode(self, str_string): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        string_visibility_mode(str string)
        
        /**
         * Returns the HiddenMode value associated with the given string
         * representation, or VM_unspecified if the string does not match any known
         * HiddenMode value.
         */
        """
        pass

    def write(self, EggRenderMode_self, ostream_out, int_indent_level): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        write(EggRenderMode self, ostream out, int indent_level)
        
        /**
         * Writes the attributes to the indicated output stream in Egg format.
         */
        """
        pass

    def __copy__(self, *args, **kwargs): # real signature unknown
        pass

    def __deepcopy__(self, *args, **kwargs): # real signature unknown
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __hash__(self, *args, **kwargs): # real signature unknown
        """ Return hash(self). """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    AMBinary = 7
    AMBlend = 3
    AMBlendNoOcclude = 4
    AMDual = 8
    AMMs = 5
    AMMsMask = 6
    AMOff = 1
    AMOn = 2
    AMPremultiplied = 9
    AMUnspecified = 0
    AM_binary = 7
    AM_blend = 3
    AM_blend_no_occlude = 4
    AM_dual = 8
    AM_ms = 5
    AM_ms_mask = 6
    AM_off = 1
    AM_on = 2
    AM_premultiplied = 9
    AM_unspecified = 0
    DTMOff = 1
    DTMOn = 2
    DTMUnspecified = 0
    DTM_off = 1
    DTM_on = 2
    DTM_unspecified = 0
    DtoolClassDict = {
        'AMBinary': 7,
        'AMBlend': 3,
        'AMBlendNoOcclude': 4,
        'AMDual': 8,
        'AMMs': 5,
        'AMMsMask': 6,
        'AMOff': 1,
        'AMOn': 2,
        'AMPremultiplied': 9,
        'AMUnspecified': 0,
        'AM_binary': 7,
        'AM_blend': 3,
        'AM_blend_no_occlude': 4,
        'AM_dual': 8,
        'AM_ms': 5,
        'AM_ms_mask': 6,
        'AM_off': 1,
        'AM_on': 2,
        'AM_premultiplied': 9,
        'AM_unspecified': 0,
        'DTMOff': 1,
        'DTMOn': 2,
        'DTMUnspecified': 0,
        'DTM_off': 1,
        'DTM_on': 2,
        'DTM_unspecified': 0,
        'DWMOff': 1,
        'DWMOn': 2,
        'DWMUnspecified': 0,
        'DWM_off': 1,
        'DWM_on': 2,
        'DWM_unspecified': 0,
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        'VMHidden': 1,
        'VMNormal': 2,
        'VMUnspecified': 0,
        'VM_hidden': 1,
        'VM_normal': 2,
        'VM_unspecified': 0,
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.egg.EggRenderMode' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.egg.EggRenderMode' objects>"
        '__doc__': "/**\n * This class stores miscellaneous rendering properties that is associated\n * with geometry, and which may be set on the geometry primitive level, on the\n * group above it, or indirectly via a texture.  It's intended to be a base\n * class for egg objects that can have these properties set.\n *\n * This class cannot inherit from EggObject, because it causes problems at the\n * EggPolygon level with multiple appearances of the EggObject base class.\n * And making EggObject a virtual base class is just no fun.\n */",
        '__eq__': None, # (!) real value is "<slot wrapper '__eq__' of 'panda3d.egg.EggRenderMode' objects>"
        '__ge__': None, # (!) real value is "<slot wrapper '__ge__' of 'panda3d.egg.EggRenderMode' objects>"
        '__gt__': None, # (!) real value is "<slot wrapper '__gt__' of 'panda3d.egg.EggRenderMode' objects>"
        '__hash__': None, # (!) real value is "<slot wrapper '__hash__' of 'panda3d.egg.EggRenderMode' objects>"
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.egg.EggRenderMode' objects>"
        '__le__': None, # (!) real value is "<slot wrapper '__le__' of 'panda3d.egg.EggRenderMode' objects>"
        '__lt__': None, # (!) real value is "<slot wrapper '__lt__' of 'panda3d.egg.EggRenderMode' objects>"
        '__ne__': None, # (!) real value is "<slot wrapper '__ne__' of 'panda3d.egg.EggRenderMode' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFDC68CDB70>'
        '__str__': None, # (!) real value is "<slot wrapper '__str__' of 'panda3d.egg.EggRenderMode' objects>"
        'assign': None, # (!) real value is "<method 'assign' of 'panda3d.egg.EggRenderMode' objects>"
        'clearBin': None, # (!) real value is "<method 'clearBin' of 'panda3d.egg.EggRenderMode' objects>"
        'clearDepthOffset': None, # (!) real value is "<method 'clearDepthOffset' of 'panda3d.egg.EggRenderMode' objects>"
        'clearDrawOrder': None, # (!) real value is "<method 'clearDrawOrder' of 'panda3d.egg.EggRenderMode' objects>"
        'clear_bin': None, # (!) real value is "<method 'clear_bin' of 'panda3d.egg.EggRenderMode' objects>"
        'clear_depth_offset': None, # (!) real value is "<method 'clear_depth_offset' of 'panda3d.egg.EggRenderMode' objects>"
        'clear_draw_order': None, # (!) real value is "<method 'clear_draw_order' of 'panda3d.egg.EggRenderMode' objects>"
        'getAlphaMode': None, # (!) real value is "<method 'getAlphaMode' of 'panda3d.egg.EggRenderMode' objects>"
        'getBin': None, # (!) real value is "<method 'getBin' of 'panda3d.egg.EggRenderMode' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFDC68CDB70>)>'
        'getDepthOffset': None, # (!) real value is "<method 'getDepthOffset' of 'panda3d.egg.EggRenderMode' objects>"
        'getDepthTestMode': None, # (!) real value is "<method 'getDepthTestMode' of 'panda3d.egg.EggRenderMode' objects>"
        'getDepthWriteMode': None, # (!) real value is "<method 'getDepthWriteMode' of 'panda3d.egg.EggRenderMode' objects>"
        'getDrawOrder': None, # (!) real value is "<method 'getDrawOrder' of 'panda3d.egg.EggRenderMode' objects>"
        'getVisibilityMode': None, # (!) real value is "<method 'getVisibilityMode' of 'panda3d.egg.EggRenderMode' objects>"
        'get_alpha_mode': None, # (!) real value is "<method 'get_alpha_mode' of 'panda3d.egg.EggRenderMode' objects>"
        'get_bin': None, # (!) real value is "<method 'get_bin' of 'panda3d.egg.EggRenderMode' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFDC68CDB70>)>'
        'get_depth_offset': None, # (!) real value is "<method 'get_depth_offset' of 'panda3d.egg.EggRenderMode' objects>"
        'get_depth_test_mode': None, # (!) real value is "<method 'get_depth_test_mode' of 'panda3d.egg.EggRenderMode' objects>"
        'get_depth_write_mode': None, # (!) real value is "<method 'get_depth_write_mode' of 'panda3d.egg.EggRenderMode' objects>"
        'get_draw_order': None, # (!) real value is "<method 'get_draw_order' of 'panda3d.egg.EggRenderMode' objects>"
        'get_visibility_mode': None, # (!) real value is "<method 'get_visibility_mode' of 'panda3d.egg.EggRenderMode' objects>"
        'hasBin': None, # (!) real value is "<method 'hasBin' of 'panda3d.egg.EggRenderMode' objects>"
        'hasDepthOffset': None, # (!) real value is "<method 'hasDepthOffset' of 'panda3d.egg.EggRenderMode' objects>"
        'hasDrawOrder': None, # (!) real value is "<method 'hasDrawOrder' of 'panda3d.egg.EggRenderMode' objects>"
        'has_bin': None, # (!) real value is "<method 'has_bin' of 'panda3d.egg.EggRenderMode' objects>"
        'has_depth_offset': None, # (!) real value is "<method 'has_depth_offset' of 'panda3d.egg.EggRenderMode' objects>"
        'has_draw_order': None, # (!) real value is "<method 'has_draw_order' of 'panda3d.egg.EggRenderMode' objects>"
        'setAlphaMode': None, # (!) real value is "<method 'setAlphaMode' of 'panda3d.egg.EggRenderMode' objects>"
        'setBin': None, # (!) real value is "<method 'setBin' of 'panda3d.egg.EggRenderMode' objects>"
        'setDepthOffset': None, # (!) real value is "<method 'setDepthOffset' of 'panda3d.egg.EggRenderMode' objects>"
        'setDepthTestMode': None, # (!) real value is "<method 'setDepthTestMode' of 'panda3d.egg.EggRenderMode' objects>"
        'setDepthWriteMode': None, # (!) real value is "<method 'setDepthWriteMode' of 'panda3d.egg.EggRenderMode' objects>"
        'setDrawOrder': None, # (!) real value is "<method 'setDrawOrder' of 'panda3d.egg.EggRenderMode' objects>"
        'setVisibilityMode': None, # (!) real value is "<method 'setVisibilityMode' of 'panda3d.egg.EggRenderMode' objects>"
        'set_alpha_mode': None, # (!) real value is "<method 'set_alpha_mode' of 'panda3d.egg.EggRenderMode' objects>"
        'set_bin': None, # (!) real value is "<method 'set_bin' of 'panda3d.egg.EggRenderMode' objects>"
        'set_depth_offset': None, # (!) real value is "<method 'set_depth_offset' of 'panda3d.egg.EggRenderMode' objects>"
        'set_depth_test_mode': None, # (!) real value is "<method 'set_depth_test_mode' of 'panda3d.egg.EggRenderMode' objects>"
        'set_depth_write_mode': None, # (!) real value is "<method 'set_depth_write_mode' of 'panda3d.egg.EggRenderMode' objects>"
        'set_draw_order': None, # (!) real value is "<method 'set_draw_order' of 'panda3d.egg.EggRenderMode' objects>"
        'set_visibility_mode': None, # (!) real value is "<method 'set_visibility_mode' of 'panda3d.egg.EggRenderMode' objects>"
        'stringAlphaMode': None, # (!) real value is '<staticmethod(<built-in method stringAlphaMode of type object at 0x00007FFDC68CDB70>)>'
        'stringDepthTestMode': None, # (!) real value is '<staticmethod(<built-in method stringDepthTestMode of type object at 0x00007FFDC68CDB70>)>'
        'stringDepthWriteMode': None, # (!) real value is '<staticmethod(<built-in method stringDepthWriteMode of type object at 0x00007FFDC68CDB70>)>'
        'stringVisibilityMode': None, # (!) real value is '<staticmethod(<built-in method stringVisibilityMode of type object at 0x00007FFDC68CDB70>)>'
        'string_alpha_mode': None, # (!) real value is '<staticmethod(<built-in method string_alpha_mode of type object at 0x00007FFDC68CDB70>)>'
        'string_depth_test_mode': None, # (!) real value is '<staticmethod(<built-in method string_depth_test_mode of type object at 0x00007FFDC68CDB70>)>'
        'string_depth_write_mode': None, # (!) real value is '<staticmethod(<built-in method string_depth_write_mode of type object at 0x00007FFDC68CDB70>)>'
        'string_visibility_mode': None, # (!) real value is '<staticmethod(<built-in method string_visibility_mode of type object at 0x00007FFDC68CDB70>)>'
        'write': None, # (!) real value is "<method 'write' of 'panda3d.egg.EggRenderMode' objects>"
    }
    DWMOff = 1
    DWMOn = 2
    DWMUnspecified = 0
    DWM_off = 1
    DWM_on = 2
    DWM_unspecified = 0
    VMHidden = 1
    VMNormal = 2
    VMUnspecified = 0
    VM_hidden = 1
    VM_normal = 2
    VM_unspecified = 0


