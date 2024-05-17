# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .RenderAttrib import RenderAttrib

class RenderModeAttrib(RenderAttrib):
    """
    /**
     * Specifies how polygons are to be drawn.
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

    def getGeomRendering(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_geom_rendering(RenderModeAttrib self, int geom_rendering)
        
        /**
         * Returns the union of the Geom::GeomRendering bits that will be required
         * once this RenderModeAttrib is applied to a geom which includes the
         * indicated geom_rendering bits.
         */
        """
        pass

    def getMode(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_mode(RenderModeAttrib self)
        
        /**
         * Returns the render mode.
         */
        """
        pass

    def getPerspective(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_perspective(RenderModeAttrib self)
        
        /**
         * Returns the perspective flag.  When this is true, the point thickness
         * represented by get_thickness() is actually a width in 3-d units, and the
         * points should scale according to perspective.  When it is false, the
         * default, the point thickness is actually a width in pixels, and points are
         * a uniform size regardless of distance from the camera.
         */
        """
        pass

    def getThickness(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_thickness(RenderModeAttrib self)
        
        /**
         * Returns the line width or point thickness.  This is only relevant when
         * rendering points or lines, such as when the mode is M_wireframe or M_point
         * (or when rendering actual points or lines primitives in M_polygon mode).
         */
        """
        pass

    def getWireframeColor(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_wireframe_color(RenderModeAttrib self)
        
        /**
         * Returns the color that is used in M_filled_wireframe mode to distinguish
         * the wireframe from the rest of the geometry.
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

    def get_geom_rendering(self, RenderModeAttrib_self, int_geom_rendering): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_geom_rendering(RenderModeAttrib self, int geom_rendering)
        
        /**
         * Returns the union of the Geom::GeomRendering bits that will be required
         * once this RenderModeAttrib is applied to a geom which includes the
         * indicated geom_rendering bits.
         */
        """
        pass

    def get_mode(self, RenderModeAttrib_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_mode(RenderModeAttrib self)
        
        /**
         * Returns the render mode.
         */
        """
        pass

    def get_perspective(self, RenderModeAttrib_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_perspective(RenderModeAttrib self)
        
        /**
         * Returns the perspective flag.  When this is true, the point thickness
         * represented by get_thickness() is actually a width in 3-d units, and the
         * points should scale according to perspective.  When it is false, the
         * default, the point thickness is actually a width in pixels, and points are
         * a uniform size regardless of distance from the camera.
         */
        """
        pass

    def get_thickness(self, RenderModeAttrib_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_thickness(RenderModeAttrib self)
        
        /**
         * Returns the line width or point thickness.  This is only relevant when
         * rendering points or lines, such as when the mode is M_wireframe or M_point
         * (or when rendering actual points or lines primitives in M_polygon mode).
         */
        """
        pass

    def get_wireframe_color(self, RenderModeAttrib_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_wireframe_color(RenderModeAttrib self)
        
        /**
         * Returns the color that is used in M_filled_wireframe mode to distinguish
         * the wireframe from the rest of the geometry.
         */
        """
        pass

    def make(self, int_mode, float_thickness, bool_perspective, const_LVecBase4f_wireframe_color): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        make(int mode, float thickness, bool perspective, const LVecBase4f wireframe_color)
        
        /**
         * Constructs a new RenderModeAttrib object that specifies whether to draw
         * polygons in the normal, filled mode, or wireframe mode, or in some other
         * yet-to-be-defined mode.
         *
         * The thickness parameter specifies the thickness to be used for wireframe
         * lines, as well as for ordinary linestrip lines; it also specifies the
         * diameter of points.  (Thick lines are presently only supported in OpenGL;
         * but thick points are supported on either platform.)
         *
         * If perspective is true, the point thickness represented is actually a width
         * in 3-d units, and the points should scale according to perspective.  When
         * it is false, the point thickness is actually a width in pixels, and points
         * are a uniform screen size regardless of distance from the camera.
         *
         * In M_filled_wireframe mode, you should also specify the wireframe_color,
         * indicating the flat color to assign to the overlayed wireframe.
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

    perspective = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thickness = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    wireframe_color = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    class_slot = 20
    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        'MFilled': 1,
        'MFilledFlat': 4,
        'MFilledWireframe': 5,
        'MPoint': 3,
        'MUnchanged': 0,
        'MWireframe': 2,
        'M_filled': 1,
        'M_filled_flat': 4,
        'M_filled_wireframe': 5,
        'M_point': 3,
        'M_unchanged': 0,
        'M_wireframe': 2,
        '__doc__': '/**\n * Specifies how polygons are to be drawn.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.RenderModeAttrib' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE291BA0>'
        'class_slot': None, # (!) real value is "<attribute 'class_slot' of 'panda3d.core.RenderModeAttrib'>"
        'getClassSlot': None, # (!) real value is '<staticmethod(<built-in method getClassSlot of type object at 0x00007FFCFE291BA0>)>'
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE291BA0>)>'
        'getGeomRendering': None, # (!) real value is "<method 'getGeomRendering' of 'panda3d.core.RenderModeAttrib' objects>"
        'getMode': None, # (!) real value is "<method 'getMode' of 'panda3d.core.RenderModeAttrib' objects>"
        'getPerspective': None, # (!) real value is "<method 'getPerspective' of 'panda3d.core.RenderModeAttrib' objects>"
        'getThickness': None, # (!) real value is "<method 'getThickness' of 'panda3d.core.RenderModeAttrib' objects>"
        'getWireframeColor': None, # (!) real value is "<method 'getWireframeColor' of 'panda3d.core.RenderModeAttrib' objects>"
        'get_class_slot': None, # (!) real value is '<staticmethod(<built-in method get_class_slot of type object at 0x00007FFCFE291BA0>)>'
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE291BA0>)>'
        'get_geom_rendering': None, # (!) real value is "<method 'get_geom_rendering' of 'panda3d.core.RenderModeAttrib' objects>"
        'get_mode': None, # (!) real value is "<method 'get_mode' of 'panda3d.core.RenderModeAttrib' objects>"
        'get_perspective': None, # (!) real value is "<method 'get_perspective' of 'panda3d.core.RenderModeAttrib' objects>"
        'get_thickness': None, # (!) real value is "<method 'get_thickness' of 'panda3d.core.RenderModeAttrib' objects>"
        'get_wireframe_color': None, # (!) real value is "<method 'get_wireframe_color' of 'panda3d.core.RenderModeAttrib' objects>"
        'make': None, # (!) real value is '<staticmethod(<built-in method make of type object at 0x00007FFCFE291BA0>)>'
        'makeDefault': None, # (!) real value is '<staticmethod(<built-in method makeDefault of type object at 0x00007FFCFE291BA0>)>'
        'make_default': None, # (!) real value is '<staticmethod(<built-in method make_default of type object at 0x00007FFCFE291BA0>)>'
        'mode': None, # (!) real value is "<attribute 'mode' of 'panda3d.core.RenderModeAttrib' objects>"
        'perspective': None, # (!) real value is "<attribute 'perspective' of 'panda3d.core.RenderModeAttrib' objects>"
        'thickness': None, # (!) real value is "<attribute 'thickness' of 'panda3d.core.RenderModeAttrib' objects>"
        'wireframe_color': None, # (!) real value is "<attribute 'wireframe_color' of 'panda3d.core.RenderModeAttrib' objects>"
    }
    MFilled = 1
    MFilledFlat = 4
    MFilledWireframe = 5
    MPoint = 3
    MUnchanged = 0
    MWireframe = 2
    M_filled = 1
    M_filled_flat = 4
    M_filled_wireframe = 5
    M_point = 3
    M_unchanged = 0
    M_wireframe = 2


