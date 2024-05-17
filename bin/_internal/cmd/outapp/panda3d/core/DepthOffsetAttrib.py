# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .RenderAttrib import RenderAttrib

class DepthOffsetAttrib(RenderAttrib):
    """
    /**
     * This is a special kind of attribute that instructs the graphics driver to
     * apply an offset or bias to the generated depth values for rendered
     * polygons, before they are written to the depth buffer.
     *
     * This can be used to shift polygons forward slightly, to resolve depth
     * conflicts.  The cull traverser may optionally use this, for instance, to
     * implement decals.  However, driver support for this feature seems to be
     * spotty, so use with caution.
     *
     * The bias is always an integer number, and each integer increment represents
     * the smallest possible increment in Z that is sufficient to completely
     * resolve two coplanar polygons.  Positive numbers are closer towards the
     * camera.
     *
     * Nested DepthOffsetAttrib values accumulate; that is, a DepthOffsetAttrib
     * with a value of 1 beneath another DepthOffsetAttrib with a value of 2
     * presents a net offset of 3.  (A DepthOffsetAttrib will not, however,
     * combine with any other DepthOffsetAttribs with a lower override parameter.)
     * The net value should probably not exceed 16 or drop below 0 for maximum
     * portability.
     *
     * Also, and only tangentially related, the DepthOffsetAttrib can be used to
     * constrain the Z output value to a subset of the usual [0, 1] range (or
     * reversing its direction) by specifying a new min_value and max_value.
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

    def getMaxValue(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_max_value(DepthOffsetAttrib self)
        
        /**
         * Returns the value for the maximum (farthest) depth value to be stored in
         * the buffer, in the range 0 .. 1.
         */
        """
        pass

    def getMinValue(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_min_value(DepthOffsetAttrib self)
        
        /**
         * Returns the value for the minimum (closest) depth value to be stored in the
         * buffer, in the range 0 .. 1.
         */
        """
        pass

    def getOffset(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_offset(DepthOffsetAttrib self)
        
        /**
         * Returns the depth offset represented by this attrib.
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

    def get_max_value(self, DepthOffsetAttrib_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_max_value(DepthOffsetAttrib self)
        
        /**
         * Returns the value for the maximum (farthest) depth value to be stored in
         * the buffer, in the range 0 .. 1.
         */
        """
        pass

    def get_min_value(self, DepthOffsetAttrib_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_min_value(DepthOffsetAttrib self)
        
        /**
         * Returns the value for the minimum (closest) depth value to be stored in the
         * buffer, in the range 0 .. 1.
         */
        """
        pass

    def get_offset(self, DepthOffsetAttrib_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_offset(DepthOffsetAttrib self)
        
        /**
         * Returns the depth offset represented by this attrib.
         */
        """
        pass

    def make(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        make()
        make(int offset)
        make(int offset, float min_value, float max_value)
        
        /**
         * Constructs a new DepthOffsetAttrib object that indicates the relative
         * amount of bias to write to the depth buffer for subsequent geometry.
         */
        
        /**
         * Constructs a new DepthOffsetAttrib object that indicates the bias, and also
         * specifies a minimum and maximum (or, more precisely, nearest and farthest)
         * values to write to the depth buffer, in the range 0 .. 1.  This range is 0,
         * 1 by default; setting it to some other range can be used to create
         * additional depth buffer effects.
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

    max_value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    min_value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    offset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    class_slot = 12
    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__doc__': '/**\n * This is a special kind of attribute that instructs the graphics driver to\n * apply an offset or bias to the generated depth values for rendered\n * polygons, before they are written to the depth buffer.\n *\n * This can be used to shift polygons forward slightly, to resolve depth\n * conflicts.  The cull traverser may optionally use this, for instance, to\n * implement decals.  However, driver support for this feature seems to be\n * spotty, so use with caution.\n *\n * The bias is always an integer number, and each integer increment represents\n * the smallest possible increment in Z that is sufficient to completely\n * resolve two coplanar polygons.  Positive numbers are closer towards the\n * camera.\n *\n * Nested DepthOffsetAttrib values accumulate; that is, a DepthOffsetAttrib\n * with a value of 1 beneath another DepthOffsetAttrib with a value of 2\n * presents a net offset of 3.  (A DepthOffsetAttrib will not, however,\n * combine with any other DepthOffsetAttribs with a lower override parameter.)\n * The net value should probably not exceed 16 or drop below 0 for maximum\n * portability.\n *\n * Also, and only tangentially related, the DepthOffsetAttrib can be used to\n * constrain the Z output value to a subset of the usual [0, 1] range (or\n * reversing its direction) by specifying a new min_value and max_value.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.DepthOffsetAttrib' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE297640>'
        'class_slot': None, # (!) real value is "<attribute 'class_slot' of 'panda3d.core.DepthOffsetAttrib'>"
        'getClassSlot': None, # (!) real value is '<staticmethod(<built-in method getClassSlot of type object at 0x00007FFCFE297640>)>'
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE297640>)>'
        'getMaxValue': None, # (!) real value is "<method 'getMaxValue' of 'panda3d.core.DepthOffsetAttrib' objects>"
        'getMinValue': None, # (!) real value is "<method 'getMinValue' of 'panda3d.core.DepthOffsetAttrib' objects>"
        'getOffset': None, # (!) real value is "<method 'getOffset' of 'panda3d.core.DepthOffsetAttrib' objects>"
        'get_class_slot': None, # (!) real value is '<staticmethod(<built-in method get_class_slot of type object at 0x00007FFCFE297640>)>'
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE297640>)>'
        'get_max_value': None, # (!) real value is "<method 'get_max_value' of 'panda3d.core.DepthOffsetAttrib' objects>"
        'get_min_value': None, # (!) real value is "<method 'get_min_value' of 'panda3d.core.DepthOffsetAttrib' objects>"
        'get_offset': None, # (!) real value is "<method 'get_offset' of 'panda3d.core.DepthOffsetAttrib' objects>"
        'make': None, # (!) real value is '<staticmethod(<built-in method make of type object at 0x00007FFCFE297640>)>'
        'makeDefault': None, # (!) real value is '<staticmethod(<built-in method makeDefault of type object at 0x00007FFCFE297640>)>'
        'make_default': None, # (!) real value is '<staticmethod(<built-in method make_default of type object at 0x00007FFCFE297640>)>'
        'max_value': None, # (!) real value is "<attribute 'max_value' of 'panda3d.core.DepthOffsetAttrib' objects>"
        'min_value': None, # (!) real value is "<attribute 'min_value' of 'panda3d.core.DepthOffsetAttrib' objects>"
        'offset': None, # (!) real value is "<attribute 'offset' of 'panda3d.core.DepthOffsetAttrib' objects>"
    }


