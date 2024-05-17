# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .PandaNode import PandaNode

from .CollisionRecorder import CollisionRecorder

class CollisionVisualizer(PandaNode, CollisionRecorder):
    """
    /**
     * This class is used to help debug the work the collisions system is doing.
     * It shows the polygons that are detected as collisions, as well as those
     * that are simply considered for collisions.
     *
     * It may be parented anywhere in the scene graph where it will be rendered to
     * achieve this.
     */
    """
    def clear(self, const_CollisionVisualizer_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear(const CollisionVisualizer self)
        
        /**
         * Removes all the visualization data from a previous traversal and resets the
         * visualizer to empty.
         */
        """
        pass

    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getNormalScale(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_normal_scale(CollisionVisualizer self)
        
        /**
         * Returns the value last set by set_normal_scale().
         */
        """
        pass

    def getPointScale(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_point_scale(CollisionVisualizer self)
        
        /**
         * Returns the value last set by set_point_scale().
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_normal_scale(self, CollisionVisualizer_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_normal_scale(CollisionVisualizer self)
        
        /**
         * Returns the value last set by set_normal_scale().
         */
        """
        pass

    def get_point_scale(self, CollisionVisualizer_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_point_scale(CollisionVisualizer self)
        
        /**
         * Returns the value last set by set_point_scale().
         */
        """
        pass

    def setNormalScale(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_normal_scale(const CollisionVisualizer self, float normal_scale)
        
        /**
         * Scales the line segments that are drawn to represent the normals of the
         * collisions.  By default, these objects are drawn at an arbitrary scale
         * which is appropriate if the scene units are measured in feet.  Change this
         * scale accordinatly if the scene units are measured on some other scale or
         * if you need to observe these normals from farther away.
         */
        """
        pass

    def setPointScale(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_point_scale(const CollisionVisualizer self, float point_scale)
        
        /**
         * Scales the points that are drawn to represent the surface and interior
         * intersection points of the collisions.  By default, these objects are drawn
         * at an arbitrary scale which is appropriate if the window units are the
         * default range -1 .. 1.  Change this scale accordinatly if the window units
         * are measured on some other scale or if you need to observe these objects in
         * a smaller window.
         */
        """
        pass

    def set_normal_scale(self, const_CollisionVisualizer_self, float_normal_scale): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_normal_scale(const CollisionVisualizer self, float normal_scale)
        
        /**
         * Scales the line segments that are drawn to represent the normals of the
         * collisions.  By default, these objects are drawn at an arbitrary scale
         * which is appropriate if the scene units are measured in feet.  Change this
         * scale accordinatly if the scene units are measured on some other scale or
         * if you need to observe these normals from farther away.
         */
        """
        pass

    def set_point_scale(self, const_CollisionVisualizer_self, float_point_scale): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_point_scale(const CollisionVisualizer self, float point_scale)
        
        /**
         * Scales the points that are drawn to represent the surface and interior
         * intersection points of the collisions.  By default, these objects are drawn
         * at an arbitrary scale which is appropriate if the window units are the
         * default range -1 .. 1.  Change this scale accordinatly if the window units
         * are measured on some other scale or if you need to observe these objects in
         * a smaller window.
         */
        """
        pass

    def upcastToCollisionRecorder(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        upcast_to_CollisionRecorder(const CollisionVisualizer self)
        
        upcast from CollisionVisualizer to CollisionRecorder
        """
        pass

    def upcastToPandaNode(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        upcast_to_PandaNode(const CollisionVisualizer self)
        
        upcast from CollisionVisualizer to PandaNode
        """
        pass

    def upcast_to_CollisionRecorder(self, const_CollisionVisualizer_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        upcast_to_CollisionRecorder(const CollisionVisualizer self)
        
        upcast from CollisionVisualizer to CollisionRecorder
        """
        pass

    def upcast_to_PandaNode(self, const_CollisionVisualizer_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        upcast_to_PandaNode(const CollisionVisualizer self)
        
        upcast from CollisionVisualizer to PandaNode
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

    normal_scale = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    point_scale = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.core.CollisionVisualizer' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.core.CollisionVisualizer' objects>"
        '__doc__': '/**\n * This class is used to help debug the work the collisions system is doing.\n * It shows the polygons that are detected as collisions, as well as those\n * that are simply considered for collisions.\n *\n * It may be parented anywhere in the scene graph where it will be rendered to\n * achieve this.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.CollisionVisualizer' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE2D0900>'
        'clear': None, # (!) real value is "<method 'clear' of 'panda3d.core.CollisionVisualizer' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE2D0900>)>'
        'getNormalScale': None, # (!) real value is "<method 'getNormalScale' of 'panda3d.core.CollisionVisualizer' objects>"
        'getPointScale': None, # (!) real value is "<method 'getPointScale' of 'panda3d.core.CollisionVisualizer' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE2D0900>)>'
        'get_normal_scale': None, # (!) real value is "<method 'get_normal_scale' of 'panda3d.core.CollisionVisualizer' objects>"
        'get_point_scale': None, # (!) real value is "<method 'get_point_scale' of 'panda3d.core.CollisionVisualizer' objects>"
        'normal_scale': None, # (!) real value is "<attribute 'normal_scale' of 'panda3d.core.CollisionVisualizer' objects>"
        'point_scale': None, # (!) real value is "<attribute 'point_scale' of 'panda3d.core.CollisionVisualizer' objects>"
        'setNormalScale': None, # (!) real value is "<method 'setNormalScale' of 'panda3d.core.CollisionVisualizer' objects>"
        'setPointScale': None, # (!) real value is "<method 'setPointScale' of 'panda3d.core.CollisionVisualizer' objects>"
        'set_normal_scale': None, # (!) real value is "<method 'set_normal_scale' of 'panda3d.core.CollisionVisualizer' objects>"
        'set_point_scale': None, # (!) real value is "<method 'set_point_scale' of 'panda3d.core.CollisionVisualizer' objects>"
        'upcastToCollisionRecorder': None, # (!) real value is "<method 'upcastToCollisionRecorder' of 'panda3d.core.CollisionVisualizer' objects>"
        'upcastToPandaNode': None, # (!) real value is "<method 'upcastToPandaNode' of 'panda3d.core.CollisionVisualizer' objects>"
        'upcast_to_CollisionRecorder': None, # (!) real value is "<method 'upcast_to_CollisionRecorder' of 'panda3d.core.CollisionVisualizer' objects>"
        'upcast_to_PandaNode': None, # (!) real value is "<method 'upcast_to_PandaNode' of 'panda3d.core.CollisionVisualizer' objects>"
    }


