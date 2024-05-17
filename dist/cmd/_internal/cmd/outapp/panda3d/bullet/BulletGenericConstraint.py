# encoding: utf-8
# module panda3d.bullet
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\bullet.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import panda3d.core as __panda3d_core


from .BulletConstraint import BulletConstraint

class BulletGenericConstraint(BulletConstraint):
    """
    /**
     *
     */
    """
    def getAngle(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_angle(BulletGenericConstraint self, int axis)
        
        /**
         *
         */
        """
        pass

    def getAxis(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_axis(BulletGenericConstraint self, int axis)
        
        // Geometry
        
        /**
         *
         */
        """
        pass

    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getFrameA(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_frame_a(BulletGenericConstraint self)
        
        /**
         *
         */
        """
        pass

    def getFrameB(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_frame_b(BulletGenericConstraint self)
        
        /**
         *
         */
        """
        pass

    def getPivot(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_pivot(BulletGenericConstraint self, int axis)
        
        /**
         *
         */
        """
        pass

    def getRotationalLimitMotor(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_rotational_limit_motor(const BulletGenericConstraint self, int axis)
        
        // Motors
        
        /**
         *
         */
        """
        pass

    def getTranslationalLimitMotor(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_translational_limit_motor(const BulletGenericConstraint self)
        
        /**
         *
         */
        """
        pass

    def get_angle(self, BulletGenericConstraint_self, int_axis): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_angle(BulletGenericConstraint self, int axis)
        
        /**
         *
         */
        """
        pass

    def get_axis(self, BulletGenericConstraint_self, int_axis): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_axis(BulletGenericConstraint self, int axis)
        
        // Geometry
        
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

    def get_frame_a(self, BulletGenericConstraint_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_frame_a(BulletGenericConstraint self)
        
        /**
         *
         */
        """
        pass

    def get_frame_b(self, BulletGenericConstraint_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_frame_b(BulletGenericConstraint self)
        
        /**
         *
         */
        """
        pass

    def get_pivot(self, BulletGenericConstraint_self, int_axis): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_pivot(BulletGenericConstraint self, int axis)
        
        /**
         *
         */
        """
        pass

    def get_rotational_limit_motor(self, const_BulletGenericConstraint_self, int_axis): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_rotational_limit_motor(const BulletGenericConstraint self, int axis)
        
        // Motors
        
        /**
         *
         */
        """
        pass

    def get_translational_limit_motor(self, const_BulletGenericConstraint_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_translational_limit_motor(const BulletGenericConstraint self)
        
        /**
         *
         */
        """
        pass

    def setAngularLimit(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_angular_limit(const BulletGenericConstraint self, int axis, float low, float high)
        
        /**
         *
         */
        """
        pass

    def setFrames(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_frames(const BulletGenericConstraint self, const TransformState ts_a, const TransformState ts_b)
        
        // Frames
        
        /**
         *
         */
        """
        pass

    def setLinearLimit(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_linear_limit(const BulletGenericConstraint self, int axis, float low, float high)
        
        // Limit
        
        /**
         *
         */
        """
        pass

    def set_angular_limit(self, const_BulletGenericConstraint_self, int_axis, float_low, float_high): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_angular_limit(const BulletGenericConstraint self, int axis, float low, float high)
        
        /**
         *
         */
        """
        pass

    def set_frames(self, const_BulletGenericConstraint_self, const_TransformState_ts_a, const_TransformState_ts_b): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_frames(const BulletGenericConstraint self, const TransformState ts_a, const TransformState ts_b)
        
        // Frames
        
        /**
         *
         */
        """
        pass

    def set_linear_limit(self, const_BulletGenericConstraint_self, int_axis, float_low, float_high): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_linear_limit(const BulletGenericConstraint self, int axis, float low, float high)
        
        // Limit
        
        /**
         *
         */
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    frame_a = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    frame_b = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    translational_limit_motor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__doc__': '/**\n *\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.bullet.BulletGenericConstraint' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFDC68D0570>'
        'frame_a': None, # (!) real value is "<attribute 'frame_a' of 'panda3d.bullet.BulletGenericConstraint' objects>"
        'frame_b': None, # (!) real value is "<attribute 'frame_b' of 'panda3d.bullet.BulletGenericConstraint' objects>"
        'getAngle': None, # (!) real value is "<method 'getAngle' of 'panda3d.bullet.BulletGenericConstraint' objects>"
        'getAxis': None, # (!) real value is "<method 'getAxis' of 'panda3d.bullet.BulletGenericConstraint' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFDC68D0570>)>'
        'getFrameA': None, # (!) real value is "<method 'getFrameA' of 'panda3d.bullet.BulletGenericConstraint' objects>"
        'getFrameB': None, # (!) real value is "<method 'getFrameB' of 'panda3d.bullet.BulletGenericConstraint' objects>"
        'getPivot': None, # (!) real value is "<method 'getPivot' of 'panda3d.bullet.BulletGenericConstraint' objects>"
        'getRotationalLimitMotor': None, # (!) real value is "<method 'getRotationalLimitMotor' of 'panda3d.bullet.BulletGenericConstraint' objects>"
        'getTranslationalLimitMotor': None, # (!) real value is "<method 'getTranslationalLimitMotor' of 'panda3d.bullet.BulletGenericConstraint' objects>"
        'get_angle': None, # (!) real value is "<method 'get_angle' of 'panda3d.bullet.BulletGenericConstraint' objects>"
        'get_axis': None, # (!) real value is "<method 'get_axis' of 'panda3d.bullet.BulletGenericConstraint' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFDC68D0570>)>'
        'get_frame_a': None, # (!) real value is "<method 'get_frame_a' of 'panda3d.bullet.BulletGenericConstraint' objects>"
        'get_frame_b': None, # (!) real value is "<method 'get_frame_b' of 'panda3d.bullet.BulletGenericConstraint' objects>"
        'get_pivot': None, # (!) real value is "<method 'get_pivot' of 'panda3d.bullet.BulletGenericConstraint' objects>"
        'get_rotational_limit_motor': None, # (!) real value is "<method 'get_rotational_limit_motor' of 'panda3d.bullet.BulletGenericConstraint' objects>"
        'get_translational_limit_motor': None, # (!) real value is "<method 'get_translational_limit_motor' of 'panda3d.bullet.BulletGenericConstraint' objects>"
        'setAngularLimit': None, # (!) real value is "<method 'setAngularLimit' of 'panda3d.bullet.BulletGenericConstraint' objects>"
        'setFrames': None, # (!) real value is "<method 'setFrames' of 'panda3d.bullet.BulletGenericConstraint' objects>"
        'setLinearLimit': None, # (!) real value is "<method 'setLinearLimit' of 'panda3d.bullet.BulletGenericConstraint' objects>"
        'set_angular_limit': None, # (!) real value is "<method 'set_angular_limit' of 'panda3d.bullet.BulletGenericConstraint' objects>"
        'set_frames': None, # (!) real value is "<method 'set_frames' of 'panda3d.bullet.BulletGenericConstraint' objects>"
        'set_linear_limit': None, # (!) real value is "<method 'set_linear_limit' of 'panda3d.bullet.BulletGenericConstraint' objects>"
        'translational_limit_motor': None, # (!) real value is "<attribute 'translational_limit_motor' of 'panda3d.bullet.BulletGenericConstraint' objects>"
    }


