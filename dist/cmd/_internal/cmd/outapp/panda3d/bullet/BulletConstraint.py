# encoding: utf-8
# module panda3d.bullet
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\bullet.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import panda3d.core as __panda3d_core


class BulletConstraint(__panda3d_core.TypedReferenceCount):
    """
    /**
     *
     */
    """
    def enableFeedback(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        enable_feedback(const BulletConstraint self, bool value)
        
        /**
         *
         */
        """
        pass

    def enable_feedback(self, const_BulletConstraint_self, bool_value): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        enable_feedback(const BulletConstraint self, bool value)
        
        /**
         *
         */
        """
        pass

    def getAppliedImpulse(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_applied_impulse(BulletConstraint self)
        
        /**
         *
         */
        """
        pass

    def getBreakingThreshold(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_breaking_threshold(BulletConstraint self)
        
        /**
         * Returns the applied impluse limit for breaking the constraint.
         */
        """
        pass

    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getDebugDrawSize(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_debug_draw_size(const BulletConstraint self)
        
        /**
         *
         */
        """
        pass

    def getParam(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_param(const BulletConstraint self, int num, int axis)
        
        /**
         *
         */
        """
        pass

    def getRigidBodyA(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_rigid_body_a(const BulletConstraint self)
        
        /**
         *
         */
        """
        pass

    def getRigidBodyB(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_rigid_body_b(const BulletConstraint self)
        
        /**
         *
         */
        """
        pass

    def get_applied_impulse(self, BulletConstraint_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_applied_impulse(BulletConstraint self)
        
        /**
         *
         */
        """
        pass

    def get_breaking_threshold(self, BulletConstraint_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_breaking_threshold(BulletConstraint self)
        
        /**
         * Returns the applied impluse limit for breaking the constraint.
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_debug_draw_size(self, const_BulletConstraint_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_debug_draw_size(const BulletConstraint self)
        
        /**
         *
         */
        """
        pass

    def get_param(self, const_BulletConstraint_self, int_num, int_axis): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_param(const BulletConstraint self, int num, int axis)
        
        /**
         *
         */
        """
        pass

    def get_rigid_body_a(self, const_BulletConstraint_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_rigid_body_a(const BulletConstraint self)
        
        /**
         *
         */
        """
        pass

    def get_rigid_body_b(self, const_BulletConstraint_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_rigid_body_b(const BulletConstraint self)
        
        /**
         *
         */
        """
        pass

    def isEnabled(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_enabled(BulletConstraint self)
        
        /**
         * Returns TRUE if the constraint is enabled.
         */
        """
        pass

    def is_enabled(self, BulletConstraint_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_enabled(BulletConstraint self)
        
        /**
         * Returns TRUE if the constraint is enabled.
         */
        """
        pass

    def setBreakingThreshold(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_breaking_threshold(const BulletConstraint self, float threshold)
        
        /**
         * Sets the applied impulse limit for breaking the constraint.  If the limit
         * is exceeded the constraint will be disabled.  Disabled constraints are not
         * removed from the world, and can be re-enabled.
         */
        """
        pass

    def setDebugDrawSize(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_debug_draw_size(const BulletConstraint self, float size)
        
        /**
         *
         */
        """
        pass

    def setEnabled(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_enabled(const BulletConstraint self, bool enabled)
        
        /**
         *
         */
        """
        pass

    def setParam(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_param(const BulletConstraint self, int num, float value, int axis)
        
        /**
         *
         */
        """
        pass

    def set_breaking_threshold(self, const_BulletConstraint_self, float_threshold): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_breaking_threshold(const BulletConstraint self, float threshold)
        
        /**
         * Sets the applied impulse limit for breaking the constraint.  If the limit
         * is exceeded the constraint will be disabled.  Disabled constraints are not
         * removed from the world, and can be re-enabled.
         */
        """
        pass

    def set_debug_draw_size(self, const_BulletConstraint_self, float_size): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_debug_draw_size(const BulletConstraint self, float size)
        
        /**
         *
         */
        """
        pass

    def set_enabled(self, const_BulletConstraint_self, bool_enabled): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_enabled(const BulletConstraint self, bool enabled)
        
        /**
         *
         */
        """
        pass

    def set_param(self, const_BulletConstraint_self, int_num, float_value, int_axis): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_param(const BulletConstraint self, int num, float value, int axis)
        
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

    applied_impulse = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    breaking_threshold = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    debug_draw_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    enabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    rigid_body_a = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    rigid_body_b = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    CPCfm = 3
    CPErp = 1
    CPStopCfm = 4
    CPStopErp = 2
    CP_cfm = 3
    CP_erp = 1
    CP_stop_cfm = 4
    CP_stop_erp = 2
    DtoolClassDict = {
        'CPCfm': 3,
        'CPErp': 1,
        'CPStopCfm': 4,
        'CPStopErp': 2,
        'CP_cfm': 3,
        'CP_erp': 1,
        'CP_stop_cfm': 4,
        'CP_stop_erp': 2,
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__doc__': '/**\n *\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.bullet.BulletConstraint' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFDC68CD650>'
        'applied_impulse': None, # (!) real value is "<attribute 'applied_impulse' of 'panda3d.bullet.BulletConstraint' objects>"
        'breaking_threshold': None, # (!) real value is "<attribute 'breaking_threshold' of 'panda3d.bullet.BulletConstraint' objects>"
        'debug_draw_size': None, # (!) real value is "<attribute 'debug_draw_size' of 'panda3d.bullet.BulletConstraint' objects>"
        'enableFeedback': None, # (!) real value is "<method 'enableFeedback' of 'panda3d.bullet.BulletConstraint' objects>"
        'enable_feedback': None, # (!) real value is "<method 'enable_feedback' of 'panda3d.bullet.BulletConstraint' objects>"
        'enabled': None, # (!) real value is "<attribute 'enabled' of 'panda3d.bullet.BulletConstraint' objects>"
        'getAppliedImpulse': None, # (!) real value is "<method 'getAppliedImpulse' of 'panda3d.bullet.BulletConstraint' objects>"
        'getBreakingThreshold': None, # (!) real value is "<method 'getBreakingThreshold' of 'panda3d.bullet.BulletConstraint' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFDC68CD650>)>'
        'getDebugDrawSize': None, # (!) real value is "<method 'getDebugDrawSize' of 'panda3d.bullet.BulletConstraint' objects>"
        'getParam': None, # (!) real value is "<method 'getParam' of 'panda3d.bullet.BulletConstraint' objects>"
        'getRigidBodyA': None, # (!) real value is "<method 'getRigidBodyA' of 'panda3d.bullet.BulletConstraint' objects>"
        'getRigidBodyB': None, # (!) real value is "<method 'getRigidBodyB' of 'panda3d.bullet.BulletConstraint' objects>"
        'get_applied_impulse': None, # (!) real value is "<method 'get_applied_impulse' of 'panda3d.bullet.BulletConstraint' objects>"
        'get_breaking_threshold': None, # (!) real value is "<method 'get_breaking_threshold' of 'panda3d.bullet.BulletConstraint' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFDC68CD650>)>'
        'get_debug_draw_size': None, # (!) real value is "<method 'get_debug_draw_size' of 'panda3d.bullet.BulletConstraint' objects>"
        'get_param': None, # (!) real value is "<method 'get_param' of 'panda3d.bullet.BulletConstraint' objects>"
        'get_rigid_body_a': None, # (!) real value is "<method 'get_rigid_body_a' of 'panda3d.bullet.BulletConstraint' objects>"
        'get_rigid_body_b': None, # (!) real value is "<method 'get_rigid_body_b' of 'panda3d.bullet.BulletConstraint' objects>"
        'isEnabled': None, # (!) real value is "<method 'isEnabled' of 'panda3d.bullet.BulletConstraint' objects>"
        'is_enabled': None, # (!) real value is "<method 'is_enabled' of 'panda3d.bullet.BulletConstraint' objects>"
        'rigid_body_a': None, # (!) real value is "<attribute 'rigid_body_a' of 'panda3d.bullet.BulletConstraint' objects>"
        'rigid_body_b': None, # (!) real value is "<attribute 'rigid_body_b' of 'panda3d.bullet.BulletConstraint' objects>"
        'setBreakingThreshold': None, # (!) real value is "<method 'setBreakingThreshold' of 'panda3d.bullet.BulletConstraint' objects>"
        'setDebugDrawSize': None, # (!) real value is "<method 'setDebugDrawSize' of 'panda3d.bullet.BulletConstraint' objects>"
        'setEnabled': None, # (!) real value is "<method 'setEnabled' of 'panda3d.bullet.BulletConstraint' objects>"
        'setParam': None, # (!) real value is "<method 'setParam' of 'panda3d.bullet.BulletConstraint' objects>"
        'set_breaking_threshold': None, # (!) real value is "<method 'set_breaking_threshold' of 'panda3d.bullet.BulletConstraint' objects>"
        'set_debug_draw_size': None, # (!) real value is "<method 'set_debug_draw_size' of 'panda3d.bullet.BulletConstraint' objects>"
        'set_enabled': None, # (!) real value is "<method 'set_enabled' of 'panda3d.bullet.BulletConstraint' objects>"
        'set_param': None, # (!) real value is "<method 'set_param' of 'panda3d.bullet.BulletConstraint' objects>"
    }


