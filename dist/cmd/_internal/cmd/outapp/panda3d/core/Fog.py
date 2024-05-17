# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .PandaNode import PandaNode

class Fog(PandaNode):
    """
    /**
     * Specifies how atmospheric fog effects are applied to geometry.  The Fog
     * object is now a PandaNode, which means it can be used similarly to a Light
     * to define effects relative to a particular coordinate system within the
     * scene graph.
     *
     * In exponential mode, the fog effects are always camera-relative, and it
     * does not matter where the Fog node is parented.  However, in linear mode,
     * the onset and opaque distances are defined as offsets along the local
     * forward axis (e.g.  the Y axis).  This allows the fog effect to be
     * localized to a particular region in space, rather than always camera-
     * relative.  If the fog object is not parented to any node, it is used to
     * generate traditonal camera-relative fog, as if it were parented to the
     * camera.
     */
    """
    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getColor(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_color(Fog self)
        
        /**
         * Returns the color of the fog.
         */
        """
        pass

    def getExpDensity(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_exp_density(Fog self)
        
        /**
         * Returns the density of the fog for exponential calculations.  This is only
         * used if the mode is not M_linear.
         */
        """
        pass

    def getLinearOnsetPoint(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_linear_onset_point(Fog self)
        
        /**
         * Returns the point in space at which the fog begins.  This is only used if
         * the mode is M_linear.
         */
        """
        pass

    def getLinearOpaquePoint(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_linear_opaque_point(Fog self)
        
        /**
         * Returns the point in space at which the fog completely obscures geometry.
         * This is only used if the mode is M_linear.
         */
        """
        pass

    def getMode(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_mode(Fog self)
        
        /**
         *
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_color(self, Fog_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_color(Fog self)
        
        /**
         * Returns the color of the fog.
         */
        """
        pass

    def get_exp_density(self, Fog_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_exp_density(Fog self)
        
        /**
         * Returns the density of the fog for exponential calculations.  This is only
         * used if the mode is not M_linear.
         */
        """
        pass

    def get_linear_onset_point(self, Fog_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_linear_onset_point(Fog self)
        
        /**
         * Returns the point in space at which the fog begins.  This is only used if
         * the mode is M_linear.
         */
        """
        pass

    def get_linear_opaque_point(self, Fog_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_linear_opaque_point(Fog self)
        
        /**
         * Returns the point in space at which the fog completely obscures geometry.
         * This is only used if the mode is M_linear.
         */
        """
        pass

    def get_mode(self, Fog_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_mode(Fog self)
        
        /**
         *
         */
        """
        pass

    def setColor(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_color(const Fog self, const LVecBase4f color)
        set_color(const Fog self, float r, float g, float b)
        
        /**
         * Sets the color of the fog.
         */
        
        /**
         * Sets the color of the fog.  The alpha component is not used.
         */
        """
        pass

    def setExpDensity(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_exp_density(const Fog self, float exp_density)
        
        /**
         * Sets the density of the fog for exponential calculations.  This is only
         * used if the mode is not M_linear.
         *
         * If the mode is currently set to M_linear, this function implicitly sets it
         * to M_exponential.
         */
        """
        pass

    def setLinearFallback(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_linear_fallback(const Fog self, float angle, float onset, float opaque)
        
        /**
         * Fog effects are traditionally defined in camera-relative space, but the
         * Panda Fog node has a special mode in which it can define a linear fog
         * effect in an arbitrary coordinate space.
         *
         * This is done by specifying 3-d onset and opaque points, and parenting the
         * Fog object somewhere within the scene graph.  In this mode, the fog will be
         * rendered as if it extended along the vector from the onset point to the
         * opaque point, in 3-d space.
         *
         * However, the underlying fog effect supported by hardware is generally only
         * one-dimensional, and must be rendered based on linear distance from the
         * camera plane.  Thus, this in-the-world effect is most effective when the
         * fog vector from onset point to opaque point is most nearly parallel to the
         * camera's eye vector.
         *
         * As the angle between the fog vector and the eye vector increases, the
         * accuracy of the effect diminishes, up to a complete breakdown of the effect
         * at a 90 degree angle.
         *
         * This function exists to define the workaround to this problem.  The linear
         * fallback parameters given here specify how the fog should be rendered when
         * the parameters are exceeded in this way.
         *
         * The angle parameter is the minimum angle, in degrees, of the fog vector to
         * the eye vector, at which the fallback effect should be employed.  The onset
         * and opaque parameters specify the camera-relative onset and opaque
         * distances to pass to the rendering hardware when employing the fallback
         * effect.  This supercedes the 3-d onset point and opaque points.
         */
        """
        pass

    def setLinearOnsetPoint(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_linear_onset_point(const Fog self, const LPoint3f linear_onset_point)
        set_linear_onset_point(const Fog self, float x, float y, float z)
        
        /**
         * Specifies the point in space at which the fog begins.  This is only used if
         * the mode is M_linear.
         */
        
        /**
         * Specifies the point in space at which the fog begins.  This is only used if
         * the mode is M_linear.
         */
        """
        pass

    def setLinearOpaquePoint(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_linear_opaque_point(const Fog self, const LPoint3f linear_opaque_point)
        set_linear_opaque_point(const Fog self, float x, float y, float z)
        
        /**
         * Specifies the point in space at which the fog completely obscures geometry.
         * This is only used if the mode is M_linear.
         */
        
        /**
         * Specifies the point in space at which the fog completely obscures geometry.
         * This is only used if the mode is M_linear.
         */
        """
        pass

    def setLinearRange(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_linear_range(const Fog self, float onset, float opaque)
        
        /**
         * Specifies the effects of the fog in linear distance units.  This is only
         * used if the mode is M_linear.
         *
         * This specifies a fog that begins at distance onset units from the origin,
         * and becomes totally opaque at distance opaque units from the origin, along
         * the forward axis (usually Y).
         *
         * This function also implicitly sets the mode the M_linear, if it is not
         * already set.
         */
        """
        pass

    def setMode(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_mode(const Fog self, int mode)
        
        /**
         * Specifies the computation that is used to determine the fog effect.  If
         * this is M_linear, then the fog will range from linearly from the onset
         * point to the opaque point (or for the distances specified in
         * set_linear_range), and the fog object should be parented into the scene
         * graph, or to the camera.
         *
         * If this is anything else, the onset point and opaque point are not used,
         * and the fog effect is based on the value specified to set_exp_density(),
         * and it doesn't matter to which node the fog object is parented, or if it is
         * parented anywhere at all.
         */
        """
        pass

    def set_color(self, const_Fog_self, const_LVecBase4f_color): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_color(const Fog self, const LVecBase4f color)
        set_color(const Fog self, float r, float g, float b)
        
        /**
         * Sets the color of the fog.
         */
        
        /**
         * Sets the color of the fog.  The alpha component is not used.
         */
        """
        pass

    def set_exp_density(self, const_Fog_self, float_exp_density): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_exp_density(const Fog self, float exp_density)
        
        /**
         * Sets the density of the fog for exponential calculations.  This is only
         * used if the mode is not M_linear.
         *
         * If the mode is currently set to M_linear, this function implicitly sets it
         * to M_exponential.
         */
        """
        pass

    def set_linear_fallback(self, const_Fog_self, float_angle, float_onset, float_opaque): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_linear_fallback(const Fog self, float angle, float onset, float opaque)
        
        /**
         * Fog effects are traditionally defined in camera-relative space, but the
         * Panda Fog node has a special mode in which it can define a linear fog
         * effect in an arbitrary coordinate space.
         *
         * This is done by specifying 3-d onset and opaque points, and parenting the
         * Fog object somewhere within the scene graph.  In this mode, the fog will be
         * rendered as if it extended along the vector from the onset point to the
         * opaque point, in 3-d space.
         *
         * However, the underlying fog effect supported by hardware is generally only
         * one-dimensional, and must be rendered based on linear distance from the
         * camera plane.  Thus, this in-the-world effect is most effective when the
         * fog vector from onset point to opaque point is most nearly parallel to the
         * camera's eye vector.
         *
         * As the angle between the fog vector and the eye vector increases, the
         * accuracy of the effect diminishes, up to a complete breakdown of the effect
         * at a 90 degree angle.
         *
         * This function exists to define the workaround to this problem.  The linear
         * fallback parameters given here specify how the fog should be rendered when
         * the parameters are exceeded in this way.
         *
         * The angle parameter is the minimum angle, in degrees, of the fog vector to
         * the eye vector, at which the fallback effect should be employed.  The onset
         * and opaque parameters specify the camera-relative onset and opaque
         * distances to pass to the rendering hardware when employing the fallback
         * effect.  This supercedes the 3-d onset point and opaque points.
         */
        """
        pass

    def set_linear_onset_point(self, const_Fog_self, const_LPoint3f_linear_onset_point): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_linear_onset_point(const Fog self, const LPoint3f linear_onset_point)
        set_linear_onset_point(const Fog self, float x, float y, float z)
        
        /**
         * Specifies the point in space at which the fog begins.  This is only used if
         * the mode is M_linear.
         */
        
        /**
         * Specifies the point in space at which the fog begins.  This is only used if
         * the mode is M_linear.
         */
        """
        pass

    def set_linear_opaque_point(self, const_Fog_self, const_LPoint3f_linear_opaque_point): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_linear_opaque_point(const Fog self, const LPoint3f linear_opaque_point)
        set_linear_opaque_point(const Fog self, float x, float y, float z)
        
        /**
         * Specifies the point in space at which the fog completely obscures geometry.
         * This is only used if the mode is M_linear.
         */
        
        /**
         * Specifies the point in space at which the fog completely obscures geometry.
         * This is only used if the mode is M_linear.
         */
        """
        pass

    def set_linear_range(self, const_Fog_self, float_onset, float_opaque): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_linear_range(const Fog self, float onset, float opaque)
        
        /**
         * Specifies the effects of the fog in linear distance units.  This is only
         * used if the mode is M_linear.
         *
         * This specifies a fog that begins at distance onset units from the origin,
         * and becomes totally opaque at distance opaque units from the origin, along
         * the forward axis (usually Y).
         *
         * This function also implicitly sets the mode the M_linear, if it is not
         * already set.
         */
        """
        pass

    def set_mode(self, const_Fog_self, int_mode): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_mode(const Fog self, int mode)
        
        /**
         * Specifies the computation that is used to determine the fog effect.  If
         * this is M_linear, then the fog will range from linearly from the onset
         * point to the opaque point (or for the distances specified in
         * set_linear_range), and the fog object should be parented into the scene
         * graph, or to the camera.
         *
         * If this is anything else, the onset point and opaque point are not used,
         * and the fog effect is based on the value specified to set_exp_density(),
         * and it doesn't matter to which node the fog object is parented, or if it is
         * parented anywhere at all.
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

    exp_density = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    linear_onset_point = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    linear_opaque_point = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    mode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        'MExponential': 1,
        'MExponentialSquared': 2,
        'MLinear': 0,
        'M_exponential': 1,
        'M_exponential_squared': 2,
        'M_linear': 0,
        '__doc__': '/**\n * Specifies how atmospheric fog effects are applied to geometry.  The Fog\n * object is now a PandaNode, which means it can be used similarly to a Light\n * to define effects relative to a particular coordinate system within the\n * scene graph.\n *\n * In exponential mode, the fog effects are always camera-relative, and it\n * does not matter where the Fog node is parented.  However, in linear mode,\n * the onset and opaque distances are defined as offsets along the local\n * forward axis (e.g.  the Y axis).  This allows the fog effect to be\n * localized to a particular region in space, rather than always camera-\n * relative.  If the fog object is not parented to any node, it is used to\n * generate traditonal camera-relative fog, as if it were parented to the\n * camera.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.Fog' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE296990>'
        'color': None, # (!) real value is "<attribute 'color' of 'panda3d.core.Fog' objects>"
        'exp_density': None, # (!) real value is "<attribute 'exp_density' of 'panda3d.core.Fog' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE296990>)>'
        'getColor': None, # (!) real value is "<method 'getColor' of 'panda3d.core.Fog' objects>"
        'getExpDensity': None, # (!) real value is "<method 'getExpDensity' of 'panda3d.core.Fog' objects>"
        'getLinearOnsetPoint': None, # (!) real value is "<method 'getLinearOnsetPoint' of 'panda3d.core.Fog' objects>"
        'getLinearOpaquePoint': None, # (!) real value is "<method 'getLinearOpaquePoint' of 'panda3d.core.Fog' objects>"
        'getMode': None, # (!) real value is "<method 'getMode' of 'panda3d.core.Fog' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE296990>)>'
        'get_color': None, # (!) real value is "<method 'get_color' of 'panda3d.core.Fog' objects>"
        'get_exp_density': None, # (!) real value is "<method 'get_exp_density' of 'panda3d.core.Fog' objects>"
        'get_linear_onset_point': None, # (!) real value is "<method 'get_linear_onset_point' of 'panda3d.core.Fog' objects>"
        'get_linear_opaque_point': None, # (!) real value is "<method 'get_linear_opaque_point' of 'panda3d.core.Fog' objects>"
        'get_mode': None, # (!) real value is "<method 'get_mode' of 'panda3d.core.Fog' objects>"
        'linear_onset_point': None, # (!) real value is "<attribute 'linear_onset_point' of 'panda3d.core.Fog' objects>"
        'linear_opaque_point': None, # (!) real value is "<attribute 'linear_opaque_point' of 'panda3d.core.Fog' objects>"
        'mode': None, # (!) real value is "<attribute 'mode' of 'panda3d.core.Fog' objects>"
        'setColor': None, # (!) real value is "<method 'setColor' of 'panda3d.core.Fog' objects>"
        'setExpDensity': None, # (!) real value is "<method 'setExpDensity' of 'panda3d.core.Fog' objects>"
        'setLinearFallback': None, # (!) real value is "<method 'setLinearFallback' of 'panda3d.core.Fog' objects>"
        'setLinearOnsetPoint': None, # (!) real value is "<method 'setLinearOnsetPoint' of 'panda3d.core.Fog' objects>"
        'setLinearOpaquePoint': None, # (!) real value is "<method 'setLinearOpaquePoint' of 'panda3d.core.Fog' objects>"
        'setLinearRange': None, # (!) real value is "<method 'setLinearRange' of 'panda3d.core.Fog' objects>"
        'setMode': None, # (!) real value is "<method 'setMode' of 'panda3d.core.Fog' objects>"
        'set_color': None, # (!) real value is "<method 'set_color' of 'panda3d.core.Fog' objects>"
        'set_exp_density': None, # (!) real value is "<method 'set_exp_density' of 'panda3d.core.Fog' objects>"
        'set_linear_fallback': None, # (!) real value is "<method 'set_linear_fallback' of 'panda3d.core.Fog' objects>"
        'set_linear_onset_point': None, # (!) real value is "<method 'set_linear_onset_point' of 'panda3d.core.Fog' objects>"
        'set_linear_opaque_point': None, # (!) real value is "<method 'set_linear_opaque_point' of 'panda3d.core.Fog' objects>"
        'set_linear_range': None, # (!) real value is "<method 'set_linear_range' of 'panda3d.core.Fog' objects>"
        'set_mode': None, # (!) real value is "<method 'set_mode' of 'panda3d.core.Fog' objects>"
    }
    MExponential = 1
    MExponentialSquared = 2
    MLinear = 0
    M_exponential = 1
    M_exponential_squared = 2
    M_linear = 0


