# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .RenderEffect import RenderEffect

class BillboardEffect(RenderEffect):
    """
    /**
     * Indicates that geometry at this node should automatically rotate to face
     * the camera, or any other arbitrary node.
     */
    """
    def getAxialRotate(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_axial_rotate(BillboardEffect self)
        
        /**
         * Returns true if this billboard rotates only around the axis of the up
         * vector, or false if it rotates freely in three dimensions.
         */
        """
        pass

    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getEyeRelative(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_eye_relative(BillboardEffect self)
        
        /**
         * Returns true if this billboard interprets the up vector relative to the
         * camera, or false if it is relative to the world.
         */
        """
        pass

    def getFixedDepth(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_fixed_depth(BillboardEffect self)
        
        /**
         * Returns true if this billboard always appears at a fixed distance from the
         * camera.
         */
        """
        pass

    def getLookAt(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_look_at(BillboardEffect self)
        
        /**
         * Returns the node this billboard will rotate to look towards.  If this is
         * empty, it means the billboard will rotate towards the current camera node,
         * wherever that might be.
         */
        """
        pass

    def getLookAtPoint(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_look_at_point(BillboardEffect self)
        
        /**
         * Returns the point, relative to the look_at node, towards which the
         * billboard will rotate.  Normally this is (0, 0, 0).
         */
        """
        pass

    def getOffset(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_offset(BillboardEffect self)
        
        /**
         * Returns the distance toward the camera (or the look_at_point) the billboard
         * is moved towards, after rotating.  This can be used to ensure the billboard
         * is not obscured by nearby geometry.
         */
        """
        pass

    def getUpVector(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_up_vector(BillboardEffect self)
        
        /**
         * Returns the up vector in effect for this billboard.
         */
        """
        pass

    def get_axial_rotate(self, BillboardEffect_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_axial_rotate(BillboardEffect self)
        
        /**
         * Returns true if this billboard rotates only around the axis of the up
         * vector, or false if it rotates freely in three dimensions.
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_eye_relative(self, BillboardEffect_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_eye_relative(BillboardEffect self)
        
        /**
         * Returns true if this billboard interprets the up vector relative to the
         * camera, or false if it is relative to the world.
         */
        """
        pass

    def get_fixed_depth(self, BillboardEffect_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_fixed_depth(BillboardEffect self)
        
        /**
         * Returns true if this billboard always appears at a fixed distance from the
         * camera.
         */
        """
        pass

    def get_look_at(self, BillboardEffect_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_look_at(BillboardEffect self)
        
        /**
         * Returns the node this billboard will rotate to look towards.  If this is
         * empty, it means the billboard will rotate towards the current camera node,
         * wherever that might be.
         */
        """
        pass

    def get_look_at_point(self, BillboardEffect_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_look_at_point(BillboardEffect self)
        
        /**
         * Returns the point, relative to the look_at node, towards which the
         * billboard will rotate.  Normally this is (0, 0, 0).
         */
        """
        pass

    def get_offset(self, BillboardEffect_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_offset(BillboardEffect self)
        
        /**
         * Returns the distance toward the camera (or the look_at_point) the billboard
         * is moved towards, after rotating.  This can be used to ensure the billboard
         * is not obscured by nearby geometry.
         */
        """
        pass

    def get_up_vector(self, BillboardEffect_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_up_vector(BillboardEffect self)
        
        /**
         * Returns the up vector in effect for this billboard.
         */
        """
        pass

    def isOff(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_off(BillboardEffect self)
        
        /**
         * Returns true if the BillboardEffect is an 'off' BillboardEffect, indicating
         * that it does not enable billboarding.  This kind of BillboardEffect isn't
         * particularly useful and isn't normally created or stored in the graph; it
         * might be implicitly discovered as the result of a
         * NodePath::get_rel_state().
         */
        """
        pass

    def is_off(self, BillboardEffect_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_off(BillboardEffect self)
        
        /**
         * Returns true if the BillboardEffect is an 'off' BillboardEffect, indicating
         * that it does not enable billboarding.  This kind of BillboardEffect isn't
         * particularly useful and isn't normally created or stored in the graph; it
         * might be implicitly discovered as the result of a
         * NodePath::get_rel_state().
         */
        """
        pass

    def make(self, const_LVector3f_up_vector, bool_eye_relative, bool_axial_rotate, float_offset, const_NodePath_look_at, const_LPoint3f_look_at_point, bool_fixed_depth): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        make(const LVector3f up_vector, bool eye_relative, bool axial_rotate, float offset, const NodePath look_at, const LPoint3f look_at_point, bool fixed_depth)
        
        /**
         * Constructs a new BillboardEffect object with the indicated properties.
         */
        """
        pass

    def makeAxis(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        make_axis()
        
        /**
         * A convenience function to make a typical axis-rotating billboard.
         */
        """
        pass

    def makePointEye(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        make_point_eye()
        
        /**
         * A convenience function to make a typical eye-relative point-rotating
         * billboard.
         */
        """
        pass

    def makePointWorld(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        make_point_world()
        
        /**
         * A convenience function to make a typical world-relative point-rotating
         * billboard.
         */
        """
        pass

    def make_axis(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        make_axis()
        
        /**
         * A convenience function to make a typical axis-rotating billboard.
         */
        """
        pass

    def make_point_eye(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        make_point_eye()
        
        /**
         * A convenience function to make a typical eye-relative point-rotating
         * billboard.
         */
        """
        pass

    def make_point_world(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        make_point_world()
        
        /**
         * A convenience function to make a typical world-relative point-rotating
         * billboard.
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
        '__doc__': '/**\n * Indicates that geometry at this node should automatically rotate to face\n * the camera, or any other arbitrary node.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.BillboardEffect' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE294720>'
        'getAxialRotate': None, # (!) real value is "<method 'getAxialRotate' of 'panda3d.core.BillboardEffect' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE294720>)>'
        'getEyeRelative': None, # (!) real value is "<method 'getEyeRelative' of 'panda3d.core.BillboardEffect' objects>"
        'getFixedDepth': None, # (!) real value is "<method 'getFixedDepth' of 'panda3d.core.BillboardEffect' objects>"
        'getLookAt': None, # (!) real value is "<method 'getLookAt' of 'panda3d.core.BillboardEffect' objects>"
        'getLookAtPoint': None, # (!) real value is "<method 'getLookAtPoint' of 'panda3d.core.BillboardEffect' objects>"
        'getOffset': None, # (!) real value is "<method 'getOffset' of 'panda3d.core.BillboardEffect' objects>"
        'getUpVector': None, # (!) real value is "<method 'getUpVector' of 'panda3d.core.BillboardEffect' objects>"
        'get_axial_rotate': None, # (!) real value is "<method 'get_axial_rotate' of 'panda3d.core.BillboardEffect' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE294720>)>'
        'get_eye_relative': None, # (!) real value is "<method 'get_eye_relative' of 'panda3d.core.BillboardEffect' objects>"
        'get_fixed_depth': None, # (!) real value is "<method 'get_fixed_depth' of 'panda3d.core.BillboardEffect' objects>"
        'get_look_at': None, # (!) real value is "<method 'get_look_at' of 'panda3d.core.BillboardEffect' objects>"
        'get_look_at_point': None, # (!) real value is "<method 'get_look_at_point' of 'panda3d.core.BillboardEffect' objects>"
        'get_offset': None, # (!) real value is "<method 'get_offset' of 'panda3d.core.BillboardEffect' objects>"
        'get_up_vector': None, # (!) real value is "<method 'get_up_vector' of 'panda3d.core.BillboardEffect' objects>"
        'isOff': None, # (!) real value is "<method 'isOff' of 'panda3d.core.BillboardEffect' objects>"
        'is_off': None, # (!) real value is "<method 'is_off' of 'panda3d.core.BillboardEffect' objects>"
        'make': None, # (!) real value is '<staticmethod(<built-in method make of type object at 0x00007FFCFE294720>)>'
        'makeAxis': None, # (!) real value is '<staticmethod(<built-in method makeAxis of type object at 0x00007FFCFE294720>)>'
        'makePointEye': None, # (!) real value is '<staticmethod(<built-in method makePointEye of type object at 0x00007FFCFE294720>)>'
        'makePointWorld': None, # (!) real value is '<staticmethod(<built-in method makePointWorld of type object at 0x00007FFCFE294720>)>'
        'make_axis': None, # (!) real value is '<staticmethod(<built-in method make_axis of type object at 0x00007FFCFE294720>)>'
        'make_point_eye': None, # (!) real value is '<staticmethod(<built-in method make_point_eye of type object at 0x00007FFCFE294720>)>'
        'make_point_world': None, # (!) real value is '<staticmethod(<built-in method make_point_world of type object at 0x00007FFCFE294720>)>'
    }


