# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .RenderAttrib import RenderAttrib

class CullFaceAttrib(RenderAttrib):
    """
    /**
     * Indicates which faces should be culled based on their vertex ordering.
     */
    """
    def getActualMode(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_actual_mode(CullFaceAttrib self)
        
        /**
         * Returns the actual culling mode, without considering the effects of the
         * reverse flag.  See also get_effective_mode().
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

    def getEffectiveMode(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_effective_mode(CullFaceAttrib self)
        
        /**
         * Returns the effective culling mode.  This is the same as the actual culling
         * mode, unless the reverse flag is set, which swaps CW for CCW and vice-
         * versa.  Also, M_cull_unchanged is mapped to M_cull_none.
         */
        """
        pass

    def getReverse(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_reverse(CullFaceAttrib self)
        
        /**
         * Returns the 'reverse' flag.  If this is true, the actual cull direction
         * (clockwise vs.  counterclockwise) is the reverse of what is specified here.
         * This allows support for make_reverse(), which defines a CullFaceAttrib that
         * reverses whatever the sense of culling would have been.
         */
        """
        pass

    def get_actual_mode(self, CullFaceAttrib_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_actual_mode(CullFaceAttrib self)
        
        /**
         * Returns the actual culling mode, without considering the effects of the
         * reverse flag.  See also get_effective_mode().
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

    def get_effective_mode(self, CullFaceAttrib_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_effective_mode(CullFaceAttrib self)
        
        /**
         * Returns the effective culling mode.  This is the same as the actual culling
         * mode, unless the reverse flag is set, which swaps CW for CCW and vice-
         * versa.  Also, M_cull_unchanged is mapped to M_cull_none.
         */
        """
        pass

    def get_reverse(self, CullFaceAttrib_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_reverse(CullFaceAttrib self)
        
        /**
         * Returns the 'reverse' flag.  If this is true, the actual cull direction
         * (clockwise vs.  counterclockwise) is the reverse of what is specified here.
         * This allows support for make_reverse(), which defines a CullFaceAttrib that
         * reverses whatever the sense of culling would have been.
         */
        """
        pass

    def make(self, int_mode): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        make(int mode)
        
        /**
         * Constructs a new CullFaceAttrib object that specifies how to cull geometry.
         * By Panda convention, vertices are ordered counterclockwise when seen from
         * the front, so the M_cull_clockwise will cull backfacing polygons.
         *
         * M_cull_unchanged is an identity attrib; if this is applied to vertices
         * without any other intervening attrib, it is the same as applying the
         * default attrib.
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

    def makeReverse(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        make_reverse()
        
        /**
         * Constructs a new CullFaceAttrib object that reverses the effects of any
         * other CullFaceAttrib objects in the scene graph.  M_cull_clockwise will be
         * treated as M_cull_counter_clockwise, and vice-versa.  M_cull_none is
         * unchanged.
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

    def make_reverse(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        make_reverse()
        
        /**
         * Constructs a new CullFaceAttrib object that reverses the effects of any
         * other CullFaceAttrib objects in the scene graph.  M_cull_clockwise will be
         * treated as M_cull_counter_clockwise, and vice-versa.  M_cull_none is
         * unchanged.
         */
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    effective_mode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    mode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    reverse = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    class_slot = 10
    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        'MCullClockwise': 1,
        'MCullCounterClockwise': 2,
        'MCullNone': 0,
        'MCullUnchanged': 3,
        'M_cull_clockwise': 1,
        'M_cull_counter_clockwise': 2,
        'M_cull_none': 0,
        'M_cull_unchanged': 3,
        '__doc__': '/**\n * Indicates which faces should be culled based on their vertex ordering.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.CullFaceAttrib' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE296250>'
        'class_slot': None, # (!) real value is "<attribute 'class_slot' of 'panda3d.core.CullFaceAttrib'>"
        'effective_mode': None, # (!) real value is "<attribute 'effective_mode' of 'panda3d.core.CullFaceAttrib' objects>"
        'getActualMode': None, # (!) real value is "<method 'getActualMode' of 'panda3d.core.CullFaceAttrib' objects>"
        'getClassSlot': None, # (!) real value is '<staticmethod(<built-in method getClassSlot of type object at 0x00007FFCFE296250>)>'
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE296250>)>'
        'getEffectiveMode': None, # (!) real value is "<method 'getEffectiveMode' of 'panda3d.core.CullFaceAttrib' objects>"
        'getReverse': None, # (!) real value is "<method 'getReverse' of 'panda3d.core.CullFaceAttrib' objects>"
        'get_actual_mode': None, # (!) real value is "<method 'get_actual_mode' of 'panda3d.core.CullFaceAttrib' objects>"
        'get_class_slot': None, # (!) real value is '<staticmethod(<built-in method get_class_slot of type object at 0x00007FFCFE296250>)>'
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE296250>)>'
        'get_effective_mode': None, # (!) real value is "<method 'get_effective_mode' of 'panda3d.core.CullFaceAttrib' objects>"
        'get_reverse': None, # (!) real value is "<method 'get_reverse' of 'panda3d.core.CullFaceAttrib' objects>"
        'make': None, # (!) real value is '<staticmethod(<built-in method make of type object at 0x00007FFCFE296250>)>'
        'makeDefault': None, # (!) real value is '<staticmethod(<built-in method makeDefault of type object at 0x00007FFCFE296250>)>'
        'makeReverse': None, # (!) real value is '<staticmethod(<built-in method makeReverse of type object at 0x00007FFCFE296250>)>'
        'make_default': None, # (!) real value is '<staticmethod(<built-in method make_default of type object at 0x00007FFCFE296250>)>'
        'make_reverse': None, # (!) real value is '<staticmethod(<built-in method make_reverse of type object at 0x00007FFCFE296250>)>'
        'mode': None, # (!) real value is "<attribute 'mode' of 'panda3d.core.CullFaceAttrib' objects>"
        'reverse': None, # (!) real value is "<attribute 'reverse' of 'panda3d.core.CullFaceAttrib' objects>"
    }
    MCullClockwise = 1
    MCullCounterClockwise = 2
    MCullNone = 0
    MCullUnchanged = 3
    M_cull_clockwise = 1
    M_cull_counter_clockwise = 2
    M_cull_none = 0
    M_cull_unchanged = 3


