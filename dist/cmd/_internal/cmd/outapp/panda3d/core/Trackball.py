# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .MouseInterfaceNode import MouseInterfaceNode

class Trackball(MouseInterfaceNode):
    """
    /**
     * Trackball acts like Performer in trackball mode.  It can either spin around
     * a piece of geometry directly, or it can spin around a camera with the
     * inverse transform to make it appear that the whole world is spinning.
     *
     * The Trackball object actually just places a transform in the data graph;
     * parent a Transform2SG node under it to actually transform objects (or
     * cameras) in the world.
     */
    """
    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getControlMode(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_control_mode(Trackball self)
        
        /**
         * Returns the control mode.  See set_control_mode().
         */
        """
        pass

    def getCoordinateSystem(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_coordinate_system(Trackball self)
        
        /**
         * Returns the coordinate system of the Trackball.  See
         * set_coordinate_system().
         */
        """
        pass

    def getForwardScale(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_forward_scale(Trackball self)
        
        /**
         * Returns the scale factor applied to forward and backward motion.  See
         * set_forward_scale().
         */
        """
        pass

    def getH(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_h(Trackball self)
        """
        pass

    def getHpr(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_hpr(Trackball self)
        
        /**
         * Return the trackball's orientation.
         */
        """
        pass

    def getInvert(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_invert(Trackball self)
        
        /**
         * Returns the invert flag.  When this is set, the inverse matrix is
         * generated, suitable for joining to a camera, instead of parenting the scene
         * under it.
         */
        """
        pass

    def getMat(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_mat(Trackball self)
        
        /**
         * Returns the matrix represented by the trackball rotation.
         */
        """
        pass

    def getOrigin(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_origin(Trackball self)
        
        /**
         * Returns the current center of rotation.
         */
        """
        pass

    def getP(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_p(Trackball self)
        """
        pass

    def getPos(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_pos(Trackball self)
        
        /**
         * Return the offset from the center of rotation.
         */
        """
        pass

    def getR(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_r(Trackball self)
        """
        pass

    def getRelTo(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_rel_to(Trackball self)
        
        /**
         * Returns the NodePath that all trackball manipulations are relative to, or
         * the empty path.
         */
        """
        pass

    def getTransMat(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_trans_mat(Trackball self)
        
        /**
         * Returns the actual transform that will be applied to the scene graph.  This
         * is the same as get_mat(), unless invert is in effect.
         */
        """
        pass

    def getX(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_x(Trackball self)
        """
        pass

    def getY(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_y(Trackball self)
        """
        pass

    def getZ(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_z(Trackball self)
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_control_mode(self, Trackball_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_control_mode(Trackball self)
        
        /**
         * Returns the control mode.  See set_control_mode().
         */
        """
        pass

    def get_coordinate_system(self, Trackball_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_coordinate_system(Trackball self)
        
        /**
         * Returns the coordinate system of the Trackball.  See
         * set_coordinate_system().
         */
        """
        pass

    def get_forward_scale(self, Trackball_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_forward_scale(Trackball self)
        
        /**
         * Returns the scale factor applied to forward and backward motion.  See
         * set_forward_scale().
         */
        """
        pass

    def get_h(self, Trackball_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_h(Trackball self)
        """
        pass

    def get_hpr(self, Trackball_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_hpr(Trackball self)
        
        /**
         * Return the trackball's orientation.
         */
        """
        pass

    def get_invert(self, Trackball_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_invert(Trackball self)
        
        /**
         * Returns the invert flag.  When this is set, the inverse matrix is
         * generated, suitable for joining to a camera, instead of parenting the scene
         * under it.
         */
        """
        pass

    def get_mat(self, Trackball_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_mat(Trackball self)
        
        /**
         * Returns the matrix represented by the trackball rotation.
         */
        """
        pass

    def get_origin(self, Trackball_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_origin(Trackball self)
        
        /**
         * Returns the current center of rotation.
         */
        """
        pass

    def get_p(self, Trackball_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_p(Trackball self)
        """
        pass

    def get_pos(self, Trackball_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_pos(Trackball self)
        
        /**
         * Return the offset from the center of rotation.
         */
        """
        pass

    def get_r(self, Trackball_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_r(Trackball self)
        """
        pass

    def get_rel_to(self, Trackball_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_rel_to(Trackball self)
        
        /**
         * Returns the NodePath that all trackball manipulations are relative to, or
         * the empty path.
         */
        """
        pass

    def get_trans_mat(self, Trackball_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_trans_mat(Trackball self)
        
        /**
         * Returns the actual transform that will be applied to the scene graph.  This
         * is the same as get_mat(), unless invert is in effect.
         */
        """
        pass

    def get_x(self, Trackball_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_x(Trackball self)
        """
        pass

    def get_y(self, Trackball_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_y(Trackball self)
        """
        pass

    def get_z(self, Trackball_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_z(Trackball self)
        """
        pass

    def moveOrigin(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        move_origin(const Trackball self, float x, float y, float z)
        
        /**
         * Moves the center of rotation by the given amount.
         */
        """
        pass

    def move_origin(self, const_Trackball_self, float_x, float_y, float_z): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        move_origin(const Trackball self, float x, float y, float z)
        
        /**
         * Moves the center of rotation by the given amount.
         */
        """
        pass

    def reset(self, const_Trackball_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        reset(const Trackball self)
        
        /**
         * Reinitializes all transforms to identity.
         */
        """
        pass

    def resetOriginHere(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        reset_origin_here(const Trackball self)
        
        /**
         * Reposition the center of rotation to coincide with the current translation
         * offset.  Future rotations will be about the current origin.
         */
        """
        pass

    def reset_origin_here(self, const_Trackball_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        reset_origin_here(const Trackball self)
        
        /**
         * Reposition the center of rotation to coincide with the current translation
         * offset.  Future rotations will be about the current origin.
         */
        """
        pass

    def setControlMode(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_control_mode(const Trackball self, int control_mode)
        
        /**
         * Sets the control mode.  Normally this is CM_default, which means each mouse
         * button serves its normal function.  When it is CM_truck, CM_pan, CM_dolly,
         * or CM_roll, all of the mouse buttons serve the indicated function instead
         * of their normal function.  This can be used in conjunction with some
         * external way of changing modes.
         */
        """
        pass

    def setCoordinateSystem(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_coordinate_system(const Trackball self, int cs)
        
        /**
         * Sets the coordinate system of the Trackball.  Normally, this is the default
         * coordinate system.  This changes the axes the Trackball manipulates so that
         * the user interface remains consistent across different coordinate systems.
         */
        """
        pass

    def setForwardScale(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_forward_scale(const Trackball self, float fwdscale)
        
        /**
         * Changes the scale factor applied to forward and backward motion.  The
         * larger this number, the faster the model will move in response to dollying
         * in and out.
         */
        """
        pass

    def setH(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_h(const Trackball self, float h)
        """
        pass

    def setHpr(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_hpr(const Trackball self, const LVecBase3f hpr)
        set_hpr(const Trackball self, float h, float p, float r)
        
        /**
         * Directly set the mover's orientation.
         */
        """
        pass

    def setInvert(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_invert(const Trackball self, bool flag)
        
        /**
         * Sets the invert flag.  When this is set, the inverse matrix is generated,
         * suitable for joining to a camera, instead of parenting the scene under it.
         */
        """
        pass

    def setMat(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_mat(const Trackball self, const LMatrix4f mat)
        
        /**
         * Stores the indicated transform in the trackball.  This is a transform in
         * global space, regardless of the rel_to node.
         */
        """
        pass

    def setOrigin(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_origin(const Trackball self, const LVecBase3f origin)
        
        /**
         * Directly sets the center of rotation.
         */
        """
        pass

    def setP(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_p(const Trackball self, float p)
        """
        pass

    def setPos(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_pos(const Trackball self, const LVecBase3f vec)
        set_pos(const Trackball self, float x, float y, float z)
        
        /**
         * Directly set the offset from the rotational origin.
         */
        """
        pass

    def setR(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_r(const Trackball self, float r)
        """
        pass

    def setRelTo(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_rel_to(const Trackball self, const NodePath rel_to)
        
        /**
         * Sets the NodePath that all trackball manipulations are to be assumed to be
         * relative to.  For instance, set your camera node here to make the trackball
         * motion camera relative.  The default is the empty path, which means
         * trackball motion is in global space.
         */
        """
        pass

    def setX(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_x(const Trackball self, float x)
        """
        pass

    def setY(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_y(const Trackball self, float y)
        """
        pass

    def setZ(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_z(const Trackball self, float z)
        """
        pass

    def set_control_mode(self, const_Trackball_self, int_control_mode): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_control_mode(const Trackball self, int control_mode)
        
        /**
         * Sets the control mode.  Normally this is CM_default, which means each mouse
         * button serves its normal function.  When it is CM_truck, CM_pan, CM_dolly,
         * or CM_roll, all of the mouse buttons serve the indicated function instead
         * of their normal function.  This can be used in conjunction with some
         * external way of changing modes.
         */
        """
        pass

    def set_coordinate_system(self, const_Trackball_self, int_cs): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_coordinate_system(const Trackball self, int cs)
        
        /**
         * Sets the coordinate system of the Trackball.  Normally, this is the default
         * coordinate system.  This changes the axes the Trackball manipulates so that
         * the user interface remains consistent across different coordinate systems.
         */
        """
        pass

    def set_forward_scale(self, const_Trackball_self, float_fwdscale): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_forward_scale(const Trackball self, float fwdscale)
        
        /**
         * Changes the scale factor applied to forward and backward motion.  The
         * larger this number, the faster the model will move in response to dollying
         * in and out.
         */
        """
        pass

    def set_h(self, const_Trackball_self, float_h): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_h(const Trackball self, float h)
        """
        pass

    def set_hpr(self, const_Trackball_self, const_LVecBase3f_hpr): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_hpr(const Trackball self, const LVecBase3f hpr)
        set_hpr(const Trackball self, float h, float p, float r)
        
        /**
         * Directly set the mover's orientation.
         */
        """
        pass

    def set_invert(self, const_Trackball_self, bool_flag): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_invert(const Trackball self, bool flag)
        
        /**
         * Sets the invert flag.  When this is set, the inverse matrix is generated,
         * suitable for joining to a camera, instead of parenting the scene under it.
         */
        """
        pass

    def set_mat(self, const_Trackball_self, const_LMatrix4f_mat): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_mat(const Trackball self, const LMatrix4f mat)
        
        /**
         * Stores the indicated transform in the trackball.  This is a transform in
         * global space, regardless of the rel_to node.
         */
        """
        pass

    def set_origin(self, const_Trackball_self, const_LVecBase3f_origin): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_origin(const Trackball self, const LVecBase3f origin)
        
        /**
         * Directly sets the center of rotation.
         */
        """
        pass

    def set_p(self, const_Trackball_self, float_p): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_p(const Trackball self, float p)
        """
        pass

    def set_pos(self, const_Trackball_self, const_LVecBase3f_vec): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_pos(const Trackball self, const LVecBase3f vec)
        set_pos(const Trackball self, float x, float y, float z)
        
        /**
         * Directly set the offset from the rotational origin.
         */
        """
        pass

    def set_r(self, const_Trackball_self, float_r): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_r(const Trackball self, float r)
        """
        pass

    def set_rel_to(self, const_Trackball_self, const_NodePath_rel_to): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_rel_to(const Trackball self, const NodePath rel_to)
        
        /**
         * Sets the NodePath that all trackball manipulations are to be assumed to be
         * relative to.  For instance, set your camera node here to make the trackball
         * motion camera relative.  The default is the empty path, which means
         * trackball motion is in global space.
         */
        """
        pass

    def set_x(self, const_Trackball_self, float_x): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_x(const Trackball self, float x)
        """
        pass

    def set_y(self, const_Trackball_self, float_y): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_y(const Trackball self, float y)
        """
        pass

    def set_z(self, const_Trackball_self, float_z): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_z(const Trackball self, float z)
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

    CMDefault = 0
    CMDolly = 3
    CMPan = 2
    CMRoll = 4
    CMTruck = 1
    CM_default = 0
    CM_dolly = 3
    CM_pan = 2
    CM_roll = 4
    CM_truck = 1
    DtoolClassDict = {
        'CMDefault': 0,
        'CMDolly': 3,
        'CMPan': 2,
        'CMRoll': 4,
        'CMTruck': 1,
        'CM_default': 0,
        'CM_dolly': 3,
        'CM_pan': 2,
        'CM_roll': 4,
        'CM_truck': 1,
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.core.Trackball' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.core.Trackball' objects>"
        '__doc__': '/**\n * Trackball acts like Performer in trackball mode.  It can either spin around\n * a piece of geometry directly, or it can spin around a camera with the\n * inverse transform to make it appear that the whole world is spinning.\n *\n * The Trackball object actually just places a transform in the data graph;\n * parent a Transform2SG node under it to actually transform objects (or\n * cameras) in the world.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.Trackball' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE366F50>'
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE366F50>)>'
        'getControlMode': None, # (!) real value is "<method 'getControlMode' of 'panda3d.core.Trackball' objects>"
        'getCoordinateSystem': None, # (!) real value is "<method 'getCoordinateSystem' of 'panda3d.core.Trackball' objects>"
        'getForwardScale': None, # (!) real value is "<method 'getForwardScale' of 'panda3d.core.Trackball' objects>"
        'getH': None, # (!) real value is "<method 'getH' of 'panda3d.core.Trackball' objects>"
        'getHpr': None, # (!) real value is "<method 'getHpr' of 'panda3d.core.Trackball' objects>"
        'getInvert': None, # (!) real value is "<method 'getInvert' of 'panda3d.core.Trackball' objects>"
        'getMat': None, # (!) real value is "<method 'getMat' of 'panda3d.core.Trackball' objects>"
        'getOrigin': None, # (!) real value is "<method 'getOrigin' of 'panda3d.core.Trackball' objects>"
        'getP': None, # (!) real value is "<method 'getP' of 'panda3d.core.Trackball' objects>"
        'getPos': None, # (!) real value is "<method 'getPos' of 'panda3d.core.Trackball' objects>"
        'getR': None, # (!) real value is "<method 'getR' of 'panda3d.core.Trackball' objects>"
        'getRelTo': None, # (!) real value is "<method 'getRelTo' of 'panda3d.core.Trackball' objects>"
        'getTransMat': None, # (!) real value is "<method 'getTransMat' of 'panda3d.core.Trackball' objects>"
        'getX': None, # (!) real value is "<method 'getX' of 'panda3d.core.Trackball' objects>"
        'getY': None, # (!) real value is "<method 'getY' of 'panda3d.core.Trackball' objects>"
        'getZ': None, # (!) real value is "<method 'getZ' of 'panda3d.core.Trackball' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE366F50>)>'
        'get_control_mode': None, # (!) real value is "<method 'get_control_mode' of 'panda3d.core.Trackball' objects>"
        'get_coordinate_system': None, # (!) real value is "<method 'get_coordinate_system' of 'panda3d.core.Trackball' objects>"
        'get_forward_scale': None, # (!) real value is "<method 'get_forward_scale' of 'panda3d.core.Trackball' objects>"
        'get_h': None, # (!) real value is "<method 'get_h' of 'panda3d.core.Trackball' objects>"
        'get_hpr': None, # (!) real value is "<method 'get_hpr' of 'panda3d.core.Trackball' objects>"
        'get_invert': None, # (!) real value is "<method 'get_invert' of 'panda3d.core.Trackball' objects>"
        'get_mat': None, # (!) real value is "<method 'get_mat' of 'panda3d.core.Trackball' objects>"
        'get_origin': None, # (!) real value is "<method 'get_origin' of 'panda3d.core.Trackball' objects>"
        'get_p': None, # (!) real value is "<method 'get_p' of 'panda3d.core.Trackball' objects>"
        'get_pos': None, # (!) real value is "<method 'get_pos' of 'panda3d.core.Trackball' objects>"
        'get_r': None, # (!) real value is "<method 'get_r' of 'panda3d.core.Trackball' objects>"
        'get_rel_to': None, # (!) real value is "<method 'get_rel_to' of 'panda3d.core.Trackball' objects>"
        'get_trans_mat': None, # (!) real value is "<method 'get_trans_mat' of 'panda3d.core.Trackball' objects>"
        'get_x': None, # (!) real value is "<method 'get_x' of 'panda3d.core.Trackball' objects>"
        'get_y': None, # (!) real value is "<method 'get_y' of 'panda3d.core.Trackball' objects>"
        'get_z': None, # (!) real value is "<method 'get_z' of 'panda3d.core.Trackball' objects>"
        'moveOrigin': None, # (!) real value is "<method 'moveOrigin' of 'panda3d.core.Trackball' objects>"
        'move_origin': None, # (!) real value is "<method 'move_origin' of 'panda3d.core.Trackball' objects>"
        'reset': None, # (!) real value is "<method 'reset' of 'panda3d.core.Trackball' objects>"
        'resetOriginHere': None, # (!) real value is "<method 'resetOriginHere' of 'panda3d.core.Trackball' objects>"
        'reset_origin_here': None, # (!) real value is "<method 'reset_origin_here' of 'panda3d.core.Trackball' objects>"
        'setControlMode': None, # (!) real value is "<method 'setControlMode' of 'panda3d.core.Trackball' objects>"
        'setCoordinateSystem': None, # (!) real value is "<method 'setCoordinateSystem' of 'panda3d.core.Trackball' objects>"
        'setForwardScale': None, # (!) real value is "<method 'setForwardScale' of 'panda3d.core.Trackball' objects>"
        'setH': None, # (!) real value is "<method 'setH' of 'panda3d.core.Trackball' objects>"
        'setHpr': None, # (!) real value is "<method 'setHpr' of 'panda3d.core.Trackball' objects>"
        'setInvert': None, # (!) real value is "<method 'setInvert' of 'panda3d.core.Trackball' objects>"
        'setMat': None, # (!) real value is "<method 'setMat' of 'panda3d.core.Trackball' objects>"
        'setOrigin': None, # (!) real value is "<method 'setOrigin' of 'panda3d.core.Trackball' objects>"
        'setP': None, # (!) real value is "<method 'setP' of 'panda3d.core.Trackball' objects>"
        'setPos': None, # (!) real value is "<method 'setPos' of 'panda3d.core.Trackball' objects>"
        'setR': None, # (!) real value is "<method 'setR' of 'panda3d.core.Trackball' objects>"
        'setRelTo': None, # (!) real value is "<method 'setRelTo' of 'panda3d.core.Trackball' objects>"
        'setX': None, # (!) real value is "<method 'setX' of 'panda3d.core.Trackball' objects>"
        'setY': None, # (!) real value is "<method 'setY' of 'panda3d.core.Trackball' objects>"
        'setZ': None, # (!) real value is "<method 'setZ' of 'panda3d.core.Trackball' objects>"
        'set_control_mode': None, # (!) real value is "<method 'set_control_mode' of 'panda3d.core.Trackball' objects>"
        'set_coordinate_system': None, # (!) real value is "<method 'set_coordinate_system' of 'panda3d.core.Trackball' objects>"
        'set_forward_scale': None, # (!) real value is "<method 'set_forward_scale' of 'panda3d.core.Trackball' objects>"
        'set_h': None, # (!) real value is "<method 'set_h' of 'panda3d.core.Trackball' objects>"
        'set_hpr': None, # (!) real value is "<method 'set_hpr' of 'panda3d.core.Trackball' objects>"
        'set_invert': None, # (!) real value is "<method 'set_invert' of 'panda3d.core.Trackball' objects>"
        'set_mat': None, # (!) real value is "<method 'set_mat' of 'panda3d.core.Trackball' objects>"
        'set_origin': None, # (!) real value is "<method 'set_origin' of 'panda3d.core.Trackball' objects>"
        'set_p': None, # (!) real value is "<method 'set_p' of 'panda3d.core.Trackball' objects>"
        'set_pos': None, # (!) real value is "<method 'set_pos' of 'panda3d.core.Trackball' objects>"
        'set_r': None, # (!) real value is "<method 'set_r' of 'panda3d.core.Trackball' objects>"
        'set_rel_to': None, # (!) real value is "<method 'set_rel_to' of 'panda3d.core.Trackball' objects>"
        'set_x': None, # (!) real value is "<method 'set_x' of 'panda3d.core.Trackball' objects>"
        'set_y': None, # (!) real value is "<method 'set_y' of 'panda3d.core.Trackball' objects>"
        'set_z': None, # (!) real value is "<method 'set_z' of 'panda3d.core.Trackball' objects>"
    }


