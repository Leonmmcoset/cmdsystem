# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .PandaNode import PandaNode

class PlaneNode(PandaNode):
    """
    /**
     * A node that contains a plane.  This is most often used as a clipping plane,
     * but it can serve other purposes as well; whenever a plane is needed to be
     * defined in some coordinate space in the world.
     */
    """
    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getClipEffect(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_clip_effect(PlaneNode self)
        
        /**
         * Returns the clip_effect bits for this clip plane.  See set_clip_effect().
         */
        """
        pass

    def getPlane(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_plane(PlaneNode self)
        
        /**
         * Returns the plane represented by the PlaneNode.
         */
        """
        pass

    def getPriority(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_priority(PlaneNode self)
        
        /**
         * Returns the priority associated with this clip plane.  See set_priority().
         */
        """
        pass

    def getVizScale(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_viz_scale(PlaneNode self)
        
        /**
         * Returns the size of the visual representation of the plane that is drawn if
         * the PlaneNode is shown.
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_clip_effect(self, PlaneNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_clip_effect(PlaneNode self)
        
        /**
         * Returns the clip_effect bits for this clip plane.  See set_clip_effect().
         */
        """
        pass

    def get_plane(self, PlaneNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_plane(PlaneNode self)
        
        /**
         * Returns the plane represented by the PlaneNode.
         */
        """
        pass

    def get_priority(self, PlaneNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_priority(PlaneNode self)
        
        /**
         * Returns the priority associated with this clip plane.  See set_priority().
         */
        """
        pass

    def get_viz_scale(self, PlaneNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_viz_scale(PlaneNode self)
        
        /**
         * Returns the size of the visual representation of the plane that is drawn if
         * the PlaneNode is shown.
         */
        """
        pass

    def setClipEffect(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_clip_effect(const PlaneNode self, int clip_effect)
        
        /**
         * Specifies the sort of things this plane will actually clip (when it is used
         * as a clip plane).  This is a bitmask union of ClipEffect values.  If it
         * includes CE_visible, then it will clip visible geometry; if it includes
         * CE_collision, then it will clip collision polygons.  If it includes neither
         * bit, it will still affect culling, but objects will either be wholly behind
         * the clipping plane, or wholly present.
         */
        """
        pass

    def setPlane(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_plane(const PlaneNode self, const LPlanef plane)
        
        /**
         * Sets the particular plane represented by the PlaneNode.
         */
        """
        pass

    def setPriority(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_priority(const PlaneNode self, int priority)
        
        /**
         * Changes the relative importance of this PlaneNode (when it is used as a
         * clip plane) relative to the other clip planes that are applied
         * simultaneously.
         *
         * The priority number is used to decide which of the requested clip planes
         * are to be activated when more clip planes are requested than the hardware
         * will support.  The highest-priority n planes are selected for rendering.
         *
         * This is similar to TextureStage::set_priority().
         */
        """
        pass

    def setVizScale(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_viz_scale(const PlaneNode self, float viz_scale)
        
        /**
         * Specifies the size of the visual representation of the plane that is drawn
         * if the PlaneNode is shown.
         */
        """
        pass

    def set_clip_effect(self, const_PlaneNode_self, int_clip_effect): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_clip_effect(const PlaneNode self, int clip_effect)
        
        /**
         * Specifies the sort of things this plane will actually clip (when it is used
         * as a clip plane).  This is a bitmask union of ClipEffect values.  If it
         * includes CE_visible, then it will clip visible geometry; if it includes
         * CE_collision, then it will clip collision polygons.  If it includes neither
         * bit, it will still affect culling, but objects will either be wholly behind
         * the clipping plane, or wholly present.
         */
        """
        pass

    def set_plane(self, const_PlaneNode_self, const_LPlanef_plane): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_plane(const PlaneNode self, const LPlanef plane)
        
        /**
         * Sets the particular plane represented by the PlaneNode.
         */
        """
        pass

    def set_priority(self, const_PlaneNode_self, int_priority): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_priority(const PlaneNode self, int priority)
        
        /**
         * Changes the relative importance of this PlaneNode (when it is used as a
         * clip plane) relative to the other clip planes that are applied
         * simultaneously.
         *
         * The priority number is used to decide which of the requested clip planes
         * are to be activated when more clip planes are requested than the hardware
         * will support.  The highest-priority n planes are selected for rendering.
         *
         * This is similar to TextureStage::set_priority().
         */
        """
        pass

    def set_viz_scale(self, const_PlaneNode_self, float_viz_scale): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_viz_scale(const PlaneNode self, float viz_scale)
        
        /**
         * Specifies the size of the visual representation of the plane that is drawn
         * if the PlaneNode is shown.
         */
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    clip_effect = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    plane = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    priority = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    viz_scale = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    CECollision = 2
    CEVisible = 1
    CE_collision = 2
    CE_visible = 1
    DtoolClassDict = {
        'CECollision': 2,
        'CEVisible': 1,
        'CE_collision': 2,
        'CE_visible': 1,
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__doc__': '/**\n * A node that contains a plane.  This is most often used as a clipping plane,\n * but it can serve other purposes as well; whenever a plane is needed to be\n * defined in some coordinate space in the world.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.PlaneNode' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE294E60>'
        'clip_effect': None, # (!) real value is "<attribute 'clip_effect' of 'panda3d.core.PlaneNode' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE294E60>)>'
        'getClipEffect': None, # (!) real value is "<method 'getClipEffect' of 'panda3d.core.PlaneNode' objects>"
        'getPlane': None, # (!) real value is "<method 'getPlane' of 'panda3d.core.PlaneNode' objects>"
        'getPriority': None, # (!) real value is "<method 'getPriority' of 'panda3d.core.PlaneNode' objects>"
        'getVizScale': None, # (!) real value is "<method 'getVizScale' of 'panda3d.core.PlaneNode' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE294E60>)>'
        'get_clip_effect': None, # (!) real value is "<method 'get_clip_effect' of 'panda3d.core.PlaneNode' objects>"
        'get_plane': None, # (!) real value is "<method 'get_plane' of 'panda3d.core.PlaneNode' objects>"
        'get_priority': None, # (!) real value is "<method 'get_priority' of 'panda3d.core.PlaneNode' objects>"
        'get_viz_scale': None, # (!) real value is "<method 'get_viz_scale' of 'panda3d.core.PlaneNode' objects>"
        'plane': None, # (!) real value is "<attribute 'plane' of 'panda3d.core.PlaneNode' objects>"
        'priority': None, # (!) real value is "<attribute 'priority' of 'panda3d.core.PlaneNode' objects>"
        'setClipEffect': None, # (!) real value is "<method 'setClipEffect' of 'panda3d.core.PlaneNode' objects>"
        'setPlane': None, # (!) real value is "<method 'setPlane' of 'panda3d.core.PlaneNode' objects>"
        'setPriority': None, # (!) real value is "<method 'setPriority' of 'panda3d.core.PlaneNode' objects>"
        'setVizScale': None, # (!) real value is "<method 'setVizScale' of 'panda3d.core.PlaneNode' objects>"
        'set_clip_effect': None, # (!) real value is "<method 'set_clip_effect' of 'panda3d.core.PlaneNode' objects>"
        'set_plane': None, # (!) real value is "<method 'set_plane' of 'panda3d.core.PlaneNode' objects>"
        'set_priority': None, # (!) real value is "<method 'set_priority' of 'panda3d.core.PlaneNode' objects>"
        'set_viz_scale': None, # (!) real value is "<method 'set_viz_scale' of 'panda3d.core.PlaneNode' objects>"
        'viz_scale': None, # (!) real value is "<attribute 'viz_scale' of 'panda3d.core.PlaneNode' objects>"
    }


