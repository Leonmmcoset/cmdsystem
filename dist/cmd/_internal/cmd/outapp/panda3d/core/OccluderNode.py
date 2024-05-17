# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .PandaNode import PandaNode

class OccluderNode(PandaNode):
    """
    /**
     * A node in the scene graph that can hold an occluder polygon, which must be
     * a rectangle.  When the occluder is activated with something like
     * render.set_occluder(), then objects whose bouding volume lies entirely
     * behind the occluder will not be rendered.
     */
    """
    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getMinCoverage(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_min_coverage(const OccluderNode self)
        
        /**
         * Returns the minimum screen coverage.
         */
        """
        pass

    def getNumVertices(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_vertices(OccluderNode self)
        
        /**
         * Returns the number of vertices in the occluder polygon.  This should always
         * return 4.
         */
        """
        pass

    def getVertex(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_vertex(OccluderNode self, int n)
        
        /**
         * Returns the nth vertex of the occluder polygon.
         */
        """
        pass

    def getVertices(self, *args, **kwargs): # real signature unknown
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_min_coverage(self, const_OccluderNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_min_coverage(const OccluderNode self)
        
        /**
         * Returns the minimum screen coverage.
         */
        """
        pass

    def get_num_vertices(self, OccluderNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_vertices(OccluderNode self)
        
        /**
         * Returns the number of vertices in the occluder polygon.  This should always
         * return 4.
         */
        """
        pass

    def get_vertex(self, OccluderNode_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_vertex(OccluderNode self, int n)
        
        /**
         * Returns the nth vertex of the occluder polygon.
         */
        """
        pass

    def get_vertices(self, *args, **kwargs): # real signature unknown
        pass

    def isDoubleSided(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_double_sided(const OccluderNode self)
        
        /**
         * Is this occluder double-sided
         */
        """
        pass

    def is_double_sided(self, const_OccluderNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_double_sided(const OccluderNode self)
        
        /**
         * Is this occluder double-sided
         */
        """
        pass

    def setDoubleSided(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_double_sided(const OccluderNode self, bool value)
        
        /**
         * If true, the back-face will also be used to occlude
         */
        """
        pass

    def setMinCoverage(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_min_coverage(const OccluderNode self, float value)
        
        /**
         * Minimum screen coverage needed before occluder used.  Range should be 0 to
         * 1. For example, setting to 0.2 would mean that the occluder needs to cover
         * 20% of the screen to be considered.
         */
        """
        pass

    def setVertex(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_vertex(const OccluderNode self, int n, const LPoint3f v)
        
        /**
         * Sets the nth vertex of the occluder polygon.
         */
        """
        pass

    def setVertices(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_vertices(const OccluderNode self, const LPoint3f v0, const LPoint3f v1, const LPoint3f v2, const LPoint3f v3)
        
        /**
         * Replaces the four vertices of the occluder polygon.  The vertices should be
         * defined in a counterclockwise orientation when looking at the face of the
         * occluder.
         */
        """
        pass

    def set_double_sided(self, const_OccluderNode_self, bool_value): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_double_sided(const OccluderNode self, bool value)
        
        /**
         * If true, the back-face will also be used to occlude
         */
        """
        pass

    def set_min_coverage(self, const_OccluderNode_self, float_value): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_min_coverage(const OccluderNode self, float value)
        
        /**
         * Minimum screen coverage needed before occluder used.  Range should be 0 to
         * 1. For example, setting to 0.2 would mean that the occluder needs to cover
         * 20% of the screen to be considered.
         */
        """
        pass

    def set_vertex(self, const_OccluderNode_self, int_n, const_LPoint3f_v): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_vertex(const OccluderNode self, int n, const LPoint3f v)
        
        /**
         * Sets the nth vertex of the occluder polygon.
         */
        """
        pass

    def set_vertices(self, const_OccluderNode_self, const_LPoint3f_v0, const_LPoint3f_v1, const_LPoint3f_v2, const_LPoint3f_v3): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_vertices(const OccluderNode self, const LPoint3f v0, const LPoint3f v1, const LPoint3f v2, const LPoint3f v3)
        
        /**
         * Replaces the four vertices of the occluder polygon.  The vertices should be
         * defined in a counterclockwise orientation when looking at the face of the
         * occluder.
         */
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    double_sided = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    min_coverage = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    vertices = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__doc__': '/**\n * A node in the scene graph that can hold an occluder polygon, which must be\n * a rectangle.  When the occluder is activated with something like\n * render.set_occluder(), then objects whose bouding volume lies entirely\n * behind the occluder will not be rendered.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.OccluderNode' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE299A80>'
        'double_sided': None, # (!) real value is "<attribute 'double_sided' of 'panda3d.core.OccluderNode' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE299A80>)>'
        'getMinCoverage': None, # (!) real value is "<method 'getMinCoverage' of 'panda3d.core.OccluderNode' objects>"
        'getNumVertices': None, # (!) real value is "<method 'getNumVertices' of 'panda3d.core.OccluderNode' objects>"
        'getVertex': None, # (!) real value is "<method 'getVertex' of 'panda3d.core.OccluderNode' objects>"
        'getVertices': None, # (!) real value is "<method 'getVertices' of 'panda3d.core.OccluderNode' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE299A80>)>'
        'get_min_coverage': None, # (!) real value is "<method 'get_min_coverage' of 'panda3d.core.OccluderNode' objects>"
        'get_num_vertices': None, # (!) real value is "<method 'get_num_vertices' of 'panda3d.core.OccluderNode' objects>"
        'get_vertex': None, # (!) real value is "<method 'get_vertex' of 'panda3d.core.OccluderNode' objects>"
        'get_vertices': None, # (!) real value is "<method 'get_vertices' of 'panda3d.core.OccluderNode' objects>"
        'isDoubleSided': None, # (!) real value is "<method 'isDoubleSided' of 'panda3d.core.OccluderNode' objects>"
        'is_double_sided': None, # (!) real value is "<method 'is_double_sided' of 'panda3d.core.OccluderNode' objects>"
        'min_coverage': None, # (!) real value is "<attribute 'min_coverage' of 'panda3d.core.OccluderNode' objects>"
        'setDoubleSided': None, # (!) real value is "<method 'setDoubleSided' of 'panda3d.core.OccluderNode' objects>"
        'setMinCoverage': None, # (!) real value is "<method 'setMinCoverage' of 'panda3d.core.OccluderNode' objects>"
        'setVertex': None, # (!) real value is "<method 'setVertex' of 'panda3d.core.OccluderNode' objects>"
        'setVertices': None, # (!) real value is "<method 'setVertices' of 'panda3d.core.OccluderNode' objects>"
        'set_double_sided': None, # (!) real value is "<method 'set_double_sided' of 'panda3d.core.OccluderNode' objects>"
        'set_min_coverage': None, # (!) real value is "<method 'set_min_coverage' of 'panda3d.core.OccluderNode' objects>"
        'set_vertex': None, # (!) real value is "<method 'set_vertex' of 'panda3d.core.OccluderNode' objects>"
        'set_vertices': None, # (!) real value is "<method 'set_vertices' of 'panda3d.core.OccluderNode' objects>"
        'vertices': None, # (!) real value is "<attribute 'vertices' of 'panda3d.core.OccluderNode' objects>"
    }


