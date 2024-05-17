# encoding: utf-8
# module panda3d.direct
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\direct.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import panda3d.core as __panda3d_core


class CMotionTrail(__panda3d_core.TypedReferenceCount):
    """
    /**
     * The method used in creating the motion trail is based on taking samples of
     * time and transformations (the position and orientation matrix) in real-
     * time.  The method also requires a number of vertices (positions) that
     * determines "shape" of the motion trail (i.e.  the edge of a blade).  A
     * start color and end color is also required for each vertex.  The color is
     * interpolated as function of time.  The colors are typically used to fade
     * the motion trail so the end color is typically black.
     *
     * The vertices are submitted via the "add_vertex" function.  For each frame,
     * a sample is submited via the "update_motion_trail" function.  During the
     * "update_motion_trail" function, the motion trail geometry is created
     * dynamically from the sample history and the vertices.
     *
     * The user must specifiy a GeomNode via "set_geom_node".
     *
     * The duration of the sample history is specified by a time window.  A larger
     * time window creates longer motion trails (given constant speed).  Samples
     * that are no longer within the time window are automatically discarded.
     *
     * The nurbs option can be used to create smooth interpolated curves from the
     * samples.  The nurbs option is useful for animations that lack sampling to
     * begin with, animations that move very quickly, or low frame rates.
     *
     * The texture option be used to create variation to the motion trail.  The u
     * coordinate of the texture corresponds to time and the v coordinate
     * corresponds to the "shape" of the motion trail.
     */
    """
    def addVertex(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_vertex(const CMotionTrail self, LVector4f vertex, LVector4f start_color, LVector4f end_color, float v)
        
        /**
         * Add a vertex.
         */
        """
        pass

    def add_vertex(self, const_CMotionTrail_self, LVector4f_vertex, LVector4f_start_color, LVector4f_end_color, float_v): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_vertex(const CMotionTrail self, LVector4f vertex, LVector4f start_color, LVector4f end_color, float v)
        
        /**
         * Add a vertex.
         */
        """
        pass

    def checkForUpdate(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        check_for_update(const CMotionTrail self, float current_time)
        
        /**
         * Check if a sample can be submitted.
         */
        """
        pass

    def check_for_update(self, const_CMotionTrail_self, float_current_time): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        check_for_update(const CMotionTrail self, float current_time)
        
        /**
         * Check if a sample can be submitted.
         */
        """
        pass

    def enable(self, const_CMotionTrail_self, bool_enable): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        enable(const CMotionTrail self, bool enable)
        
        /**
         * Enable/disable the motion trail.
         */
        """
        pass

    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def reset(self, const_CMotionTrail_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        reset(const CMotionTrail self)
        
        /**
         * Reset the frame sample history.
         */
        """
        pass

    def resetVertexList(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        reset_vertex_list(const CMotionTrail self)
        
        /**
         * Reset the vertex list.
         */
        """
        pass

    def reset_vertex_list(self, const_CMotionTrail_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        reset_vertex_list(const CMotionTrail self)
        
        /**
         * Reset the vertex list.
         */
        """
        pass

    def setGeomNode(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_geom_node(const CMotionTrail self, GeomNode geom_node)
        
        /**
         * Set the GeomNode.
         */
        """
        pass

    def setParameters(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_parameters(const CMotionTrail self, float sampling_time, float time_window, bool use_texture, bool calculate_relative_matrix, bool use_nurbs, float resolution_distance)
        
        /**
         * Set motion trail parameters.
         *
         * sampling_time = Can be used to specify a lower sampling rate than the frame
         * rate.  Use 0.0 with nurbs.
         *
         * time_window = a component for the "length" of the motion trail.  The motion
         * trail length = time_window * velocity of the object.
         *
         * use_texture = texture option on/off.
         *
         * calculate_relative_matrix = calculate relative matrix on/off.
         *
         * use_nurbs = nurbs option on/off
         *
         * resolution_distance = the distance used to determine the number of geometry
         * samples.  samples = motion trail length / resolution_distance.  Applicable
         * only if nurbs is on.
         */
        """
        pass

    def set_geom_node(self, const_CMotionTrail_self, GeomNode_geom_node): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_geom_node(const CMotionTrail self, GeomNode geom_node)
        
        /**
         * Set the GeomNode.
         */
        """
        pass

    def set_parameters(self, const_CMotionTrail_self, float_sampling_time, float_time_window, bool_use_texture, bool_calculate_relative_matrix, bool_use_nurbs, float_resolution_distance): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_parameters(const CMotionTrail self, float sampling_time, float time_window, bool use_texture, bool calculate_relative_matrix, bool use_nurbs, float resolution_distance)
        
        /**
         * Set motion trail parameters.
         *
         * sampling_time = Can be used to specify a lower sampling rate than the frame
         * rate.  Use 0.0 with nurbs.
         *
         * time_window = a component for the "length" of the motion trail.  The motion
         * trail length = time_window * velocity of the object.
         *
         * use_texture = texture option on/off.
         *
         * calculate_relative_matrix = calculate relative matrix on/off.
         *
         * use_nurbs = nurbs option on/off
         *
         * resolution_distance = the distance used to determine the number of geometry
         * samples.  samples = motion trail length / resolution_distance.  Applicable
         * only if nurbs is on.
         */
        """
        pass

    def updateMotionTrail(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        update_motion_trail(const CMotionTrail self, float current_time, LMatrix4f transform)
        
        /**
         * See class header comments.
         */
        """
        pass

    def update_motion_trail(self, const_CMotionTrail_self, float_current_time, LMatrix4f_transform): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        update_motion_trail(const CMotionTrail self, float current_time, LMatrix4f transform)
        
        /**
         * See class header comments.
         */
        """
        pass

    def __copy__(self, *args, **kwargs): # real signature unknown
        pass

    def __deepcopy__(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.direct.CMotionTrail' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.direct.CMotionTrail' objects>"
        '__doc__': '/**\n * The method used in creating the motion trail is based on taking samples of\n * time and transformations (the position and orientation matrix) in real-\n * time.  The method also requires a number of vertices (positions) that\n * determines "shape" of the motion trail (i.e.  the edge of a blade).  A\n * start color and end color is also required for each vertex.  The color is\n * interpolated as function of time.  The colors are typically used to fade\n * the motion trail so the end color is typically black.\n *\n * The vertices are submitted via the "add_vertex" function.  For each frame,\n * a sample is submited via the "update_motion_trail" function.  During the\n * "update_motion_trail" function, the motion trail geometry is created\n * dynamically from the sample history and the vertices.\n *\n * The user must specifiy a GeomNode via "set_geom_node".\n *\n * The duration of the sample history is specified by a time window.  A larger\n * time window creates longer motion trails (given constant speed).  Samples\n * that are no longer within the time window are automatically discarded.\n *\n * The nurbs option can be used to create smooth interpolated curves from the\n * samples.  The nurbs option is useful for animations that lack sampling to\n * begin with, animations that move very quickly, or low frame rates.\n *\n * The texture option be used to create variation to the motion trail.  The u\n * coordinate of the texture corresponds to time and the v coordinate\n * corresponds to the "shape" of the motion trail.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.direct.CMotionTrail' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFDC68EB700>'
        'addVertex': None, # (!) real value is "<method 'addVertex' of 'panda3d.direct.CMotionTrail' objects>"
        'add_vertex': None, # (!) real value is "<method 'add_vertex' of 'panda3d.direct.CMotionTrail' objects>"
        'checkForUpdate': None, # (!) real value is "<method 'checkForUpdate' of 'panda3d.direct.CMotionTrail' objects>"
        'check_for_update': None, # (!) real value is "<method 'check_for_update' of 'panda3d.direct.CMotionTrail' objects>"
        'enable': None, # (!) real value is "<method 'enable' of 'panda3d.direct.CMotionTrail' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFDC68EB700>)>'
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFDC68EB700>)>'
        'reset': None, # (!) real value is "<method 'reset' of 'panda3d.direct.CMotionTrail' objects>"
        'resetVertexList': None, # (!) real value is "<method 'resetVertexList' of 'panda3d.direct.CMotionTrail' objects>"
        'reset_vertex_list': None, # (!) real value is "<method 'reset_vertex_list' of 'panda3d.direct.CMotionTrail' objects>"
        'setGeomNode': None, # (!) real value is "<method 'setGeomNode' of 'panda3d.direct.CMotionTrail' objects>"
        'setParameters': None, # (!) real value is "<method 'setParameters' of 'panda3d.direct.CMotionTrail' objects>"
        'set_geom_node': None, # (!) real value is "<method 'set_geom_node' of 'panda3d.direct.CMotionTrail' objects>"
        'set_parameters': None, # (!) real value is "<method 'set_parameters' of 'panda3d.direct.CMotionTrail' objects>"
        'updateMotionTrail': None, # (!) real value is "<method 'updateMotionTrail' of 'panda3d.direct.CMotionTrail' objects>"
        'update_motion_trail': None, # (!) real value is "<method 'update_motion_trail' of 'panda3d.direct.CMotionTrail' objects>"
    }


