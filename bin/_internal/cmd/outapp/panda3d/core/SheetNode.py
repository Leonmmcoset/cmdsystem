# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .PandaNode import PandaNode

class SheetNode(PandaNode):
    """
    /**
     * This class draws a visible representation of the NURBS surface stored in
     * its NurbsSurfaceEvaluator.  It automatically recomputes the surface every
     * frame.
     *
     * This is not related to NurbsSurface, CubicSurfaceseg or any of the
     * ParametricSurface-derived objects in this module.  It is a completely
     * parallel implementation of NURBS surfaces, and will probably eventually
     * replace the whole ParametricSurface class hierarchy.
     */
    """
    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getNumUSubdiv(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_u_subdiv(SheetNode self)
        
        /**
         * Returns the number of subdivisions per cubic segment to draw in the U
         * direction.  See set_num_u_subdiv().
         */
        """
        pass

    def getNumVSubdiv(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_v_subdiv(SheetNode self)
        
        /**
         * Returns the number of subdivisions per cubic segment to draw in the V
         * direction.  See set_num_v_subdiv().
         */
        """
        pass

    def getSurface(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_surface(SheetNode self)
        
        /**
         * Returns the surface represented by the SheetNode.
         */
        """
        pass

    def getUseVertexColor(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_use_vertex_color(SheetNode self)
        
        /**
         * Returns the "use vertex color" flag.  See set_use_vertex_color().
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_num_u_subdiv(self, SheetNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_u_subdiv(SheetNode self)
        
        /**
         * Returns the number of subdivisions per cubic segment to draw in the U
         * direction.  See set_num_u_subdiv().
         */
        """
        pass

    def get_num_v_subdiv(self, SheetNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_v_subdiv(SheetNode self)
        
        /**
         * Returns the number of subdivisions per cubic segment to draw in the V
         * direction.  See set_num_v_subdiv().
         */
        """
        pass

    def get_surface(self, SheetNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_surface(SheetNode self)
        
        /**
         * Returns the surface represented by the SheetNode.
         */
        """
        pass

    def get_use_vertex_color(self, SheetNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_use_vertex_color(SheetNode self)
        
        /**
         * Returns the "use vertex color" flag.  See set_use_vertex_color().
         */
        """
        pass

    def resetBound(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        reset_bound(const SheetNode self, const NodePath rel_to)
        
        /**
         * Recomputes the bounding volume.  This is normally called automatically, but
         * it must occasionally be called explicitly when the surface has changed
         * properties outside of this node's knowledge.
         */
        """
        pass

    def reset_bound(self, const_SheetNode_self, const_NodePath_rel_to): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        reset_bound(const SheetNode self, const NodePath rel_to)
        
        /**
         * Recomputes the bounding volume.  This is normally called automatically, but
         * it must occasionally be called explicitly when the surface has changed
         * properties outside of this node's knowledge.
         */
        """
        pass

    def setNumUSubdiv(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_num_u_subdiv(const SheetNode self, int num_u_subdiv)
        
        /**
         * Specifies the number of subdivisions per cubic segment (that is, per unique
         * knot value) to draw in a fixed uniform tesselation of the surface in the U
         * direction.
         */
        """
        pass

    def setNumVSubdiv(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_num_v_subdiv(const SheetNode self, int num_v_subdiv)
        
        /**
         * Specifies the number of subdivisions per cubic segment (that is, per unique
         * knot value) to draw in a fixed uniform tesselation of the surface in the V
         * direction.
         */
        """
        pass

    def setSurface(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_surface(const SheetNode self, NurbsSurfaceEvaluator surface)
        
        /**
         * Sets the particular surface represented by the SheetNode.
         */
        """
        pass

    def setUseVertexColor(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_use_vertex_color(const SheetNode self, bool flag)
        
        /**
         * Sets the "use vertex color" flag.  When this is true, the R, G, B, A vertex
         * color is assumed to be stored as the dimensions 0, 1, 2, 3, respectively,
         * of the extended vertex values.  Use
         * NurbsCurveEvaluator::set_extended_vertex() to set these values.
         */
        """
        pass

    def set_num_u_subdiv(self, const_SheetNode_self, int_num_u_subdiv): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_num_u_subdiv(const SheetNode self, int num_u_subdiv)
        
        /**
         * Specifies the number of subdivisions per cubic segment (that is, per unique
         * knot value) to draw in a fixed uniform tesselation of the surface in the U
         * direction.
         */
        """
        pass

    def set_num_v_subdiv(self, const_SheetNode_self, int_num_v_subdiv): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_num_v_subdiv(const SheetNode self, int num_v_subdiv)
        
        /**
         * Specifies the number of subdivisions per cubic segment (that is, per unique
         * knot value) to draw in a fixed uniform tesselation of the surface in the V
         * direction.
         */
        """
        pass

    def set_surface(self, const_SheetNode_self, NurbsSurfaceEvaluator_surface): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_surface(const SheetNode self, NurbsSurfaceEvaluator surface)
        
        /**
         * Sets the particular surface represented by the SheetNode.
         */
        """
        pass

    def set_use_vertex_color(self, const_SheetNode_self, bool_flag): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_use_vertex_color(const SheetNode self, bool flag)
        
        /**
         * Sets the "use vertex color" flag.  When this is true, the R, G, B, A vertex
         * color is assumed to be stored as the dimensions 0, 1, 2, 3, respectively,
         * of the extended vertex values.  Use
         * NurbsCurveEvaluator::set_extended_vertex() to set these values.
         */
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__doc__': '/**\n * This class draws a visible representation of the NURBS surface stored in\n * its NurbsSurfaceEvaluator.  It automatically recomputes the surface every\n * frame.\n *\n * This is not related to NurbsSurface, CubicSurfaceseg or any of the\n * ParametricSurface-derived objects in this module.  It is a completely\n * parallel implementation of NURBS surfaces, and will probably eventually\n * replace the whole ParametricSurface class hierarchy.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.SheetNode' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE34F640>'
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE34F640>)>'
        'getNumUSubdiv': None, # (!) real value is "<method 'getNumUSubdiv' of 'panda3d.core.SheetNode' objects>"
        'getNumVSubdiv': None, # (!) real value is "<method 'getNumVSubdiv' of 'panda3d.core.SheetNode' objects>"
        'getSurface': None, # (!) real value is "<method 'getSurface' of 'panda3d.core.SheetNode' objects>"
        'getUseVertexColor': None, # (!) real value is "<method 'getUseVertexColor' of 'panda3d.core.SheetNode' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE34F640>)>'
        'get_num_u_subdiv': None, # (!) real value is "<method 'get_num_u_subdiv' of 'panda3d.core.SheetNode' objects>"
        'get_num_v_subdiv': None, # (!) real value is "<method 'get_num_v_subdiv' of 'panda3d.core.SheetNode' objects>"
        'get_surface': None, # (!) real value is "<method 'get_surface' of 'panda3d.core.SheetNode' objects>"
        'get_use_vertex_color': None, # (!) real value is "<method 'get_use_vertex_color' of 'panda3d.core.SheetNode' objects>"
        'resetBound': None, # (!) real value is "<method 'resetBound' of 'panda3d.core.SheetNode' objects>"
        'reset_bound': None, # (!) real value is "<method 'reset_bound' of 'panda3d.core.SheetNode' objects>"
        'setNumUSubdiv': None, # (!) real value is "<method 'setNumUSubdiv' of 'panda3d.core.SheetNode' objects>"
        'setNumVSubdiv': None, # (!) real value is "<method 'setNumVSubdiv' of 'panda3d.core.SheetNode' objects>"
        'setSurface': None, # (!) real value is "<method 'setSurface' of 'panda3d.core.SheetNode' objects>"
        'setUseVertexColor': None, # (!) real value is "<method 'setUseVertexColor' of 'panda3d.core.SheetNode' objects>"
        'set_num_u_subdiv': None, # (!) real value is "<method 'set_num_u_subdiv' of 'panda3d.core.SheetNode' objects>"
        'set_num_v_subdiv': None, # (!) real value is "<method 'set_num_v_subdiv' of 'panda3d.core.SheetNode' objects>"
        'set_surface': None, # (!) real value is "<method 'set_surface' of 'panda3d.core.SheetNode' objects>"
        'set_use_vertex_color': None, # (!) real value is "<method 'set_use_vertex_color' of 'panda3d.core.SheetNode' objects>"
    }


