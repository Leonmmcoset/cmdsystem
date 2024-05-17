# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .PandaNode import PandaNode

class RopeNode(PandaNode):
    """
    /**
     * This class draws a visible representation of the NURBS curve stored in its
     * NurbsCurveEvaluator.  It automatically recomputes the curve every frame.
     *
     * This is not related to NurbsCurve, CubicCurveseg or any of the
     * ParametricCurve-derived objects in this module.  It is a completely
     * parallel implementation of NURBS curves, and will probably eventually
     * replace the whole ParametricCurve class hierarchy.
     */
    """
    def clearMatrix(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_matrix(const RopeNode self)
        
        /**
         * Resets the node's matrix to identity.  See set_matrix().
         */
        """
        pass

    def clear_matrix(self, const_RopeNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_matrix(const RopeNode self)
        
        /**
         * Resets the node's matrix to identity.  See set_matrix().
         */
        """
        pass

    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getCurve(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_curve(RopeNode self)
        
        /**
         * Returns the curve represented by the RopeNode.
         */
        """
        pass

    def getMatrix(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_matrix(RopeNode self)
        
        /**
         * Returns the optional matrix which is used to transform each control vertex
         * after it has been transformed into the RopeNode's coordinate space, but
         * before the polygon vertices are generated.
         */
        """
        pass

    def getNormalMode(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_normal_mode(RopeNode self)
        
        /**
         * Returns the kind of normals to generate for the rope.  This is only
         * applicable when the RenderMode is set to RM_tube.
         */
        """
        pass

    def getNumSlices(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_slices(RopeNode self)
        
        /**
         * Returns the number of radial subdivisions to make if RenderMode is RM_tube.
         * It is ignored in the other render modes.  See set_num_slices().
         */
        """
        pass

    def getNumSubdiv(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_subdiv(RopeNode self)
        
        /**
         * Returns the number of subdivisions per cubic segment to draw.  See
         * set_num_subdiv().
         */
        """
        pass

    def getRenderMode(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_render_mode(RopeNode self)
        
        /**
         * Returns the method used to render the rope.  See set_render_mode().
         */
        """
        pass

    def getThickness(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_thickness(RopeNode self)
        
        /**
         * Returns the thickness of the rope.  See set_thickness().
         */
        """
        pass

    def getTubeUp(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_tube_up(RopeNode self)
        
        /**
         * Returns the normal vector used to control the "top" of the curve, when
         * RenderMode is RM_tube.  See set_tube_up().
         */
        """
        pass

    def getUseVertexColor(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_use_vertex_color(RopeNode self)
        
        /**
         * Returns the "use vertex color" flag.  See set_use_vertex_color().
         */
        """
        pass

    def getUseVertexThickness(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_use_vertex_thickness(RopeNode self)
        
        /**
         * Returns the "use vertex thickness" flag.  See set_use_vertex_thickness().
         */
        """
        pass

    def getUvDirection(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_uv_direction(RopeNode self)
        
        /**
         * Returns true if the rope runs down the U coordinate of the texture, or
         * false if it runs down the V coordinate.
         */
        """
        pass

    def getUvMode(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_uv_mode(RopeNode self)
        
        /**
         * Returns the algorithm to use to generate UV's for the rope.
         */
        """
        pass

    def getUvScale(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_uv_scale(RopeNode self)
        
        /**
         * Returns the scaling factor to apply to generated UV's for the rope.
         */
        """
        pass

    def getVertexColorDimension(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_vertex_color_dimension()
        
        /**
         * Returns the numeric extended dimension in which the color components should
         * be found.  See NurbsCurveEvaluator::set_extended_vertex().
         *
         * The color components will be expected at (n, n + 1, n + 2, n + 3).
         */
        """
        pass

    def getVertexThicknessDimension(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_vertex_thickness_dimension()
        
        /**
         * Returns the numeric extended dimension in which the thickness component
         * should be found.  See NurbsCurveEvaluator::set_extended_vertex().
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_curve(self, RopeNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_curve(RopeNode self)
        
        /**
         * Returns the curve represented by the RopeNode.
         */
        """
        pass

    def get_matrix(self, RopeNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_matrix(RopeNode self)
        
        /**
         * Returns the optional matrix which is used to transform each control vertex
         * after it has been transformed into the RopeNode's coordinate space, but
         * before the polygon vertices are generated.
         */
        """
        pass

    def get_normal_mode(self, RopeNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_normal_mode(RopeNode self)
        
        /**
         * Returns the kind of normals to generate for the rope.  This is only
         * applicable when the RenderMode is set to RM_tube.
         */
        """
        pass

    def get_num_slices(self, RopeNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_slices(RopeNode self)
        
        /**
         * Returns the number of radial subdivisions to make if RenderMode is RM_tube.
         * It is ignored in the other render modes.  See set_num_slices().
         */
        """
        pass

    def get_num_subdiv(self, RopeNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_subdiv(RopeNode self)
        
        /**
         * Returns the number of subdivisions per cubic segment to draw.  See
         * set_num_subdiv().
         */
        """
        pass

    def get_render_mode(self, RopeNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_render_mode(RopeNode self)
        
        /**
         * Returns the method used to render the rope.  See set_render_mode().
         */
        """
        pass

    def get_thickness(self, RopeNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_thickness(RopeNode self)
        
        /**
         * Returns the thickness of the rope.  See set_thickness().
         */
        """
        pass

    def get_tube_up(self, RopeNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_tube_up(RopeNode self)
        
        /**
         * Returns the normal vector used to control the "top" of the curve, when
         * RenderMode is RM_tube.  See set_tube_up().
         */
        """
        pass

    def get_use_vertex_color(self, RopeNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_use_vertex_color(RopeNode self)
        
        /**
         * Returns the "use vertex color" flag.  See set_use_vertex_color().
         */
        """
        pass

    def get_use_vertex_thickness(self, RopeNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_use_vertex_thickness(RopeNode self)
        
        /**
         * Returns the "use vertex thickness" flag.  See set_use_vertex_thickness().
         */
        """
        pass

    def get_uv_direction(self, RopeNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_uv_direction(RopeNode self)
        
        /**
         * Returns true if the rope runs down the U coordinate of the texture, or
         * false if it runs down the V coordinate.
         */
        """
        pass

    def get_uv_mode(self, RopeNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_uv_mode(RopeNode self)
        
        /**
         * Returns the algorithm to use to generate UV's for the rope.
         */
        """
        pass

    def get_uv_scale(self, RopeNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_uv_scale(RopeNode self)
        
        /**
         * Returns the scaling factor to apply to generated UV's for the rope.
         */
        """
        pass

    def get_vertex_color_dimension(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_vertex_color_dimension()
        
        /**
         * Returns the numeric extended dimension in which the color components should
         * be found.  See NurbsCurveEvaluator::set_extended_vertex().
         *
         * The color components will be expected at (n, n + 1, n + 2, n + 3).
         */
        """
        pass

    def get_vertex_thickness_dimension(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_vertex_thickness_dimension()
        
        /**
         * Returns the numeric extended dimension in which the thickness component
         * should be found.  See NurbsCurveEvaluator::set_extended_vertex().
         */
        """
        pass

    def hasMatrix(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_matrix(RopeNode self)
        
        /**
         * Returns true if the node has a matrix set, false otherwise.  See
         * set_matrix().
         */
        """
        pass

    def has_matrix(self, RopeNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_matrix(RopeNode self)
        
        /**
         * Returns true if the node has a matrix set, false otherwise.  See
         * set_matrix().
         */
        """
        pass

    def resetBound(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        reset_bound(const RopeNode self, const NodePath rel_to)
        
        /**
         * Recomputes the bounding volume.  This is normally called automatically, but
         * it must occasionally be called explicitly when the curve has changed
         * properties outside of this node's knowledge.
         */
        """
        pass

    def reset_bound(self, const_RopeNode_self, const_NodePath_rel_to): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        reset_bound(const RopeNode self, const NodePath rel_to)
        
        /**
         * Recomputes the bounding volume.  This is normally called automatically, but
         * it must occasionally be called explicitly when the curve has changed
         * properties outside of this node's knowledge.
         */
        """
        pass

    def setCurve(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_curve(const RopeNode self, NurbsCurveEvaluator curve)
        
        /**
         * Sets the particular curve represented by the RopeNode.
         */
        """
        pass

    def setMatrix(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_matrix(const RopeNode self, const LMatrix4f matrix)
        
        /**
         * Specifies an optional matrix which is used to transform each control vertex
         * after it has been transformed into the RopeNode's coordinate space, but
         * before the polygon vertices are generated.
         */
        """
        pass

    def setNormalMode(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_normal_mode(const RopeNode self, int normal_mode)
        
        /**
         * Specifies the kind of normals to generate for the rope.  This is only
         * applicable when the RenderMode is set to RM_tube; in the other render
         * modes, normals are never generated.
         */
        """
        pass

    def setNumSlices(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_num_slices(const RopeNode self, int num_slices)
        
        /**
         * Specifies the number of radial subdivisions to make if RenderMode is
         * RM_tube.  It is ignored in the other render modes.
         *
         * Increasing this number increases the roundness of a cross-section of the
         * tube.  The minimum value for a dimensional tube is 3; setting it to 2 will
         * get you a thin piece of tape (which is similar to RM_billboard, except it
         * won't rotate to face the camera).
         */
        """
        pass

    def setNumSubdiv(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_num_subdiv(const RopeNode self, int num_subdiv)
        
        /**
         * Specifies the number of subdivisions per cubic segment (that is, per unique
         * knot value) to draw in a fixed uniform tesselation of the curve.
         */
        """
        pass

    def setRenderMode(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_render_mode(const RopeNode self, int render_mode)
        
        /**
         * Specifies the method used to render the rope.  The simplest is RM_thread,
         * which just draws a one-pixel line segment.
         */
        """
        pass

    def setThickness(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_thickness(const RopeNode self, float thickness)
        
        /**
         * Specifies the thickness of the rope, in pixels or in spatial units,
         * depending on the render mode.  See set_render_mode().
         *
         * The thickness may also be specified on a per-vertex basis.  See
         * set_use_vertex_thickness().
         */
        """
        pass

    def setTubeUp(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_tube_up(const RopeNode self, const LVector3f tube_up)
        
        /**
         * Specifies a normal vector, generally perpendicular to the main axis of the
         * starting point of the curve, that controls the "top" of the curve, when
         * RenderMode is RM_tube.  This is used to orient the vertices that make up
         * the tube.  If this vector is too nearly parallel with the starting
         * direction of the curve, there may be a tendency for the whole tube to
         * gimble-lock around its primary axis.
         */
        """
        pass

    def setUseVertexColor(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_use_vertex_color(const RopeNode self, bool flag)
        
        /**
         * Sets the "use vertex color" flag.  When this is true, the R, G, B, A vertex
         * color is assumed to be stored as the dimensions n + 0, n + 1, n + 2, n + 3,
         * respectively, of the extended vertex values, where n is the value returned
         * by get_vertex_color_dimension().  Use
         * NurbsCurveEvaluator::set_extended_vertex() to set these values.
         */
        """
        pass

    def setUseVertexThickness(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_use_vertex_thickness(const RopeNode self, bool flag)
        
        /**
         * Sets the "use vertex thickness" flag.  When this is true, the vertex
         * thickness is assumed to be stored as the dimension
         * get_vertex_thickness_dimension(), of the extended vertex values.  Use
         * NurbsCurveEvaluator::set_extended_vertex() to set these values.
         *
         * In this mode, the overall thickness is also applied as a scale to the
         * vertex thickness.  Not all render modes support vertex thickness.
         */
        """
        pass

    def setUvDirection(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_uv_direction(const RopeNode self, bool u_dominant)
        
        /**
         * Specify true to vary the U coordinate down the length of the rope, or false
         * to vary the V coordinate.
         */
        """
        pass

    def setUvMode(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_uv_mode(const RopeNode self, int uv_mode)
        
        /**
         * Specifies the algorithm to use to generate UV's for the rope.
         */
        """
        pass

    def setUvScale(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_uv_scale(const RopeNode self, float scale)
        
        /**
         * Specifies an additional scaling factor to apply to generated UV's along the
         * rope.  This scale factor is applied in whichever direction is along the
         * rope, as specified by set_uv_direction().
         */
        """
        pass

    def set_curve(self, const_RopeNode_self, NurbsCurveEvaluator_curve): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_curve(const RopeNode self, NurbsCurveEvaluator curve)
        
        /**
         * Sets the particular curve represented by the RopeNode.
         */
        """
        pass

    def set_matrix(self, const_RopeNode_self, const_LMatrix4f_matrix): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_matrix(const RopeNode self, const LMatrix4f matrix)
        
        /**
         * Specifies an optional matrix which is used to transform each control vertex
         * after it has been transformed into the RopeNode's coordinate space, but
         * before the polygon vertices are generated.
         */
        """
        pass

    def set_normal_mode(self, const_RopeNode_self, int_normal_mode): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_normal_mode(const RopeNode self, int normal_mode)
        
        /**
         * Specifies the kind of normals to generate for the rope.  This is only
         * applicable when the RenderMode is set to RM_tube; in the other render
         * modes, normals are never generated.
         */
        """
        pass

    def set_num_slices(self, const_RopeNode_self, int_num_slices): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_num_slices(const RopeNode self, int num_slices)
        
        /**
         * Specifies the number of radial subdivisions to make if RenderMode is
         * RM_tube.  It is ignored in the other render modes.
         *
         * Increasing this number increases the roundness of a cross-section of the
         * tube.  The minimum value for a dimensional tube is 3; setting it to 2 will
         * get you a thin piece of tape (which is similar to RM_billboard, except it
         * won't rotate to face the camera).
         */
        """
        pass

    def set_num_subdiv(self, const_RopeNode_self, int_num_subdiv): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_num_subdiv(const RopeNode self, int num_subdiv)
        
        /**
         * Specifies the number of subdivisions per cubic segment (that is, per unique
         * knot value) to draw in a fixed uniform tesselation of the curve.
         */
        """
        pass

    def set_render_mode(self, const_RopeNode_self, int_render_mode): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_render_mode(const RopeNode self, int render_mode)
        
        /**
         * Specifies the method used to render the rope.  The simplest is RM_thread,
         * which just draws a one-pixel line segment.
         */
        """
        pass

    def set_thickness(self, const_RopeNode_self, float_thickness): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_thickness(const RopeNode self, float thickness)
        
        /**
         * Specifies the thickness of the rope, in pixels or in spatial units,
         * depending on the render mode.  See set_render_mode().
         *
         * The thickness may also be specified on a per-vertex basis.  See
         * set_use_vertex_thickness().
         */
        """
        pass

    def set_tube_up(self, const_RopeNode_self, const_LVector3f_tube_up): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_tube_up(const RopeNode self, const LVector3f tube_up)
        
        /**
         * Specifies a normal vector, generally perpendicular to the main axis of the
         * starting point of the curve, that controls the "top" of the curve, when
         * RenderMode is RM_tube.  This is used to orient the vertices that make up
         * the tube.  If this vector is too nearly parallel with the starting
         * direction of the curve, there may be a tendency for the whole tube to
         * gimble-lock around its primary axis.
         */
        """
        pass

    def set_use_vertex_color(self, const_RopeNode_self, bool_flag): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_use_vertex_color(const RopeNode self, bool flag)
        
        /**
         * Sets the "use vertex color" flag.  When this is true, the R, G, B, A vertex
         * color is assumed to be stored as the dimensions n + 0, n + 1, n + 2, n + 3,
         * respectively, of the extended vertex values, where n is the value returned
         * by get_vertex_color_dimension().  Use
         * NurbsCurveEvaluator::set_extended_vertex() to set these values.
         */
        """
        pass

    def set_use_vertex_thickness(self, const_RopeNode_self, bool_flag): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_use_vertex_thickness(const RopeNode self, bool flag)
        
        /**
         * Sets the "use vertex thickness" flag.  When this is true, the vertex
         * thickness is assumed to be stored as the dimension
         * get_vertex_thickness_dimension(), of the extended vertex values.  Use
         * NurbsCurveEvaluator::set_extended_vertex() to set these values.
         *
         * In this mode, the overall thickness is also applied as a scale to the
         * vertex thickness.  Not all render modes support vertex thickness.
         */
        """
        pass

    def set_uv_direction(self, const_RopeNode_self, bool_u_dominant): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_uv_direction(const RopeNode self, bool u_dominant)
        
        /**
         * Specify true to vary the U coordinate down the length of the rope, or false
         * to vary the V coordinate.
         */
        """
        pass

    def set_uv_mode(self, const_RopeNode_self, int_uv_mode): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_uv_mode(const RopeNode self, int uv_mode)
        
        /**
         * Specifies the algorithm to use to generate UV's for the rope.
         */
        """
        pass

    def set_uv_scale(self, const_RopeNode_self, float_scale): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_uv_scale(const RopeNode self, float scale)
        
        /**
         * Specifies an additional scaling factor to apply to generated UV's along the
         * rope.  This scale factor is applied in whichever direction is along the
         * rope, as specified by set_uv_direction().
         */
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    curve = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    matrix = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    normal_mode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    num_slices = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    num_subdiv = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    render_mode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thickness = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tube_up = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    use_vertex_color = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    use_vertex_thickness = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    uv_direction = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    uv_mode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    uv_scale = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        'NMNone': 0,
        'NMVertex': 1,
        'NM_none': 0,
        'NM_vertex': 1,
        'RMBillboard': 2,
        'RMTape': 1,
        'RMThread': 0,
        'RMTube': 3,
        'RM_billboard': 2,
        'RM_tape': 1,
        'RM_thread': 0,
        'RM_tube': 3,
        'UVDistance': 2,
        'UVDistance2': 3,
        'UVNone': 0,
        'UVParametric': 1,
        'UV_distance': 2,
        'UV_distance2': 3,
        'UV_none': 0,
        'UV_parametric': 1,
        '__doc__': '/**\n * This class draws a visible representation of the NURBS curve stored in its\n * NurbsCurveEvaluator.  It automatically recomputes the curve every frame.\n *\n * This is not related to NurbsCurve, CubicCurveseg or any of the\n * ParametricCurve-derived objects in this module.  It is a completely\n * parallel implementation of NURBS curves, and will probably eventually\n * replace the whole ParametricCurve class hierarchy.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.RopeNode' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE34F470>'
        'clearMatrix': None, # (!) real value is "<method 'clearMatrix' of 'panda3d.core.RopeNode' objects>"
        'clear_matrix': None, # (!) real value is "<method 'clear_matrix' of 'panda3d.core.RopeNode' objects>"
        'curve': None, # (!) real value is "<attribute 'curve' of 'panda3d.core.RopeNode' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE34F470>)>'
        'getCurve': None, # (!) real value is "<method 'getCurve' of 'panda3d.core.RopeNode' objects>"
        'getMatrix': None, # (!) real value is "<method 'getMatrix' of 'panda3d.core.RopeNode' objects>"
        'getNormalMode': None, # (!) real value is "<method 'getNormalMode' of 'panda3d.core.RopeNode' objects>"
        'getNumSlices': None, # (!) real value is "<method 'getNumSlices' of 'panda3d.core.RopeNode' objects>"
        'getNumSubdiv': None, # (!) real value is "<method 'getNumSubdiv' of 'panda3d.core.RopeNode' objects>"
        'getRenderMode': None, # (!) real value is "<method 'getRenderMode' of 'panda3d.core.RopeNode' objects>"
        'getThickness': None, # (!) real value is "<method 'getThickness' of 'panda3d.core.RopeNode' objects>"
        'getTubeUp': None, # (!) real value is "<method 'getTubeUp' of 'panda3d.core.RopeNode' objects>"
        'getUseVertexColor': None, # (!) real value is "<method 'getUseVertexColor' of 'panda3d.core.RopeNode' objects>"
        'getUseVertexThickness': None, # (!) real value is "<method 'getUseVertexThickness' of 'panda3d.core.RopeNode' objects>"
        'getUvDirection': None, # (!) real value is "<method 'getUvDirection' of 'panda3d.core.RopeNode' objects>"
        'getUvMode': None, # (!) real value is "<method 'getUvMode' of 'panda3d.core.RopeNode' objects>"
        'getUvScale': None, # (!) real value is "<method 'getUvScale' of 'panda3d.core.RopeNode' objects>"
        'getVertexColorDimension': None, # (!) real value is '<staticmethod(<built-in method getVertexColorDimension of type object at 0x00007FFCFE34F470>)>'
        'getVertexThicknessDimension': None, # (!) real value is '<staticmethod(<built-in method getVertexThicknessDimension of type object at 0x00007FFCFE34F470>)>'
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE34F470>)>'
        'get_curve': None, # (!) real value is "<method 'get_curve' of 'panda3d.core.RopeNode' objects>"
        'get_matrix': None, # (!) real value is "<method 'get_matrix' of 'panda3d.core.RopeNode' objects>"
        'get_normal_mode': None, # (!) real value is "<method 'get_normal_mode' of 'panda3d.core.RopeNode' objects>"
        'get_num_slices': None, # (!) real value is "<method 'get_num_slices' of 'panda3d.core.RopeNode' objects>"
        'get_num_subdiv': None, # (!) real value is "<method 'get_num_subdiv' of 'panda3d.core.RopeNode' objects>"
        'get_render_mode': None, # (!) real value is "<method 'get_render_mode' of 'panda3d.core.RopeNode' objects>"
        'get_thickness': None, # (!) real value is "<method 'get_thickness' of 'panda3d.core.RopeNode' objects>"
        'get_tube_up': None, # (!) real value is "<method 'get_tube_up' of 'panda3d.core.RopeNode' objects>"
        'get_use_vertex_color': None, # (!) real value is "<method 'get_use_vertex_color' of 'panda3d.core.RopeNode' objects>"
        'get_use_vertex_thickness': None, # (!) real value is "<method 'get_use_vertex_thickness' of 'panda3d.core.RopeNode' objects>"
        'get_uv_direction': None, # (!) real value is "<method 'get_uv_direction' of 'panda3d.core.RopeNode' objects>"
        'get_uv_mode': None, # (!) real value is "<method 'get_uv_mode' of 'panda3d.core.RopeNode' objects>"
        'get_uv_scale': None, # (!) real value is "<method 'get_uv_scale' of 'panda3d.core.RopeNode' objects>"
        'get_vertex_color_dimension': None, # (!) real value is '<staticmethod(<built-in method get_vertex_color_dimension of type object at 0x00007FFCFE34F470>)>'
        'get_vertex_thickness_dimension': None, # (!) real value is '<staticmethod(<built-in method get_vertex_thickness_dimension of type object at 0x00007FFCFE34F470>)>'
        'hasMatrix': None, # (!) real value is "<method 'hasMatrix' of 'panda3d.core.RopeNode' objects>"
        'has_matrix': None, # (!) real value is "<method 'has_matrix' of 'panda3d.core.RopeNode' objects>"
        'matrix': None, # (!) real value is "<attribute 'matrix' of 'panda3d.core.RopeNode' objects>"
        'normal_mode': None, # (!) real value is "<attribute 'normal_mode' of 'panda3d.core.RopeNode' objects>"
        'num_slices': None, # (!) real value is "<attribute 'num_slices' of 'panda3d.core.RopeNode' objects>"
        'num_subdiv': None, # (!) real value is "<attribute 'num_subdiv' of 'panda3d.core.RopeNode' objects>"
        'render_mode': None, # (!) real value is "<attribute 'render_mode' of 'panda3d.core.RopeNode' objects>"
        'resetBound': None, # (!) real value is "<method 'resetBound' of 'panda3d.core.RopeNode' objects>"
        'reset_bound': None, # (!) real value is "<method 'reset_bound' of 'panda3d.core.RopeNode' objects>"
        'setCurve': None, # (!) real value is "<method 'setCurve' of 'panda3d.core.RopeNode' objects>"
        'setMatrix': None, # (!) real value is "<method 'setMatrix' of 'panda3d.core.RopeNode' objects>"
        'setNormalMode': None, # (!) real value is "<method 'setNormalMode' of 'panda3d.core.RopeNode' objects>"
        'setNumSlices': None, # (!) real value is "<method 'setNumSlices' of 'panda3d.core.RopeNode' objects>"
        'setNumSubdiv': None, # (!) real value is "<method 'setNumSubdiv' of 'panda3d.core.RopeNode' objects>"
        'setRenderMode': None, # (!) real value is "<method 'setRenderMode' of 'panda3d.core.RopeNode' objects>"
        'setThickness': None, # (!) real value is "<method 'setThickness' of 'panda3d.core.RopeNode' objects>"
        'setTubeUp': None, # (!) real value is "<method 'setTubeUp' of 'panda3d.core.RopeNode' objects>"
        'setUseVertexColor': None, # (!) real value is "<method 'setUseVertexColor' of 'panda3d.core.RopeNode' objects>"
        'setUseVertexThickness': None, # (!) real value is "<method 'setUseVertexThickness' of 'panda3d.core.RopeNode' objects>"
        'setUvDirection': None, # (!) real value is "<method 'setUvDirection' of 'panda3d.core.RopeNode' objects>"
        'setUvMode': None, # (!) real value is "<method 'setUvMode' of 'panda3d.core.RopeNode' objects>"
        'setUvScale': None, # (!) real value is "<method 'setUvScale' of 'panda3d.core.RopeNode' objects>"
        'set_curve': None, # (!) real value is "<method 'set_curve' of 'panda3d.core.RopeNode' objects>"
        'set_matrix': None, # (!) real value is "<method 'set_matrix' of 'panda3d.core.RopeNode' objects>"
        'set_normal_mode': None, # (!) real value is "<method 'set_normal_mode' of 'panda3d.core.RopeNode' objects>"
        'set_num_slices': None, # (!) real value is "<method 'set_num_slices' of 'panda3d.core.RopeNode' objects>"
        'set_num_subdiv': None, # (!) real value is "<method 'set_num_subdiv' of 'panda3d.core.RopeNode' objects>"
        'set_render_mode': None, # (!) real value is "<method 'set_render_mode' of 'panda3d.core.RopeNode' objects>"
        'set_thickness': None, # (!) real value is "<method 'set_thickness' of 'panda3d.core.RopeNode' objects>"
        'set_tube_up': None, # (!) real value is "<method 'set_tube_up' of 'panda3d.core.RopeNode' objects>"
        'set_use_vertex_color': None, # (!) real value is "<method 'set_use_vertex_color' of 'panda3d.core.RopeNode' objects>"
        'set_use_vertex_thickness': None, # (!) real value is "<method 'set_use_vertex_thickness' of 'panda3d.core.RopeNode' objects>"
        'set_uv_direction': None, # (!) real value is "<method 'set_uv_direction' of 'panda3d.core.RopeNode' objects>"
        'set_uv_mode': None, # (!) real value is "<method 'set_uv_mode' of 'panda3d.core.RopeNode' objects>"
        'set_uv_scale': None, # (!) real value is "<method 'set_uv_scale' of 'panda3d.core.RopeNode' objects>"
        'thickness': None, # (!) real value is "<attribute 'thickness' of 'panda3d.core.RopeNode' objects>"
        'tube_up': None, # (!) real value is "<attribute 'tube_up' of 'panda3d.core.RopeNode' objects>"
        'use_vertex_color': None, # (!) real value is "<attribute 'use_vertex_color' of 'panda3d.core.RopeNode' objects>"
        'use_vertex_thickness': None, # (!) real value is "<attribute 'use_vertex_thickness' of 'panda3d.core.RopeNode' objects>"
        'uv_direction': None, # (!) real value is "<attribute 'uv_direction' of 'panda3d.core.RopeNode' objects>"
        'uv_mode': None, # (!) real value is "<attribute 'uv_mode' of 'panda3d.core.RopeNode' objects>"
        'uv_scale': None, # (!) real value is "<attribute 'uv_scale' of 'panda3d.core.RopeNode' objects>"
        'vertex_color_dimension': None, # (!) real value is "<attribute 'vertex_color_dimension' of 'panda3d.core.RopeNode'>"
        'vertex_thickness_dimension': None, # (!) real value is "<attribute 'vertex_thickness_dimension' of 'panda3d.core.RopeNode'>"
    }
    NMNone = 0
    NMVertex = 1
    NM_none = 0
    NM_vertex = 1
    RMBillboard = 2
    RMTape = 1
    RMThread = 0
    RMTube = 3
    RM_billboard = 2
    RM_tape = 1
    RM_thread = 0
    RM_tube = 3
    UVDistance = 2
    UVDistance2 = 3
    UVNone = 0
    UVParametric = 1
    UV_distance = 2
    UV_distance2 = 3
    UV_none = 0
    UV_parametric = 1
    vertex_color_dimension = 0
    vertex_thickness_dimension = 4


