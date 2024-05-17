# encoding: utf-8
# module panda3d.physics
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\physics.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import panda3d.core as __panda3d_core


from .LinearForce import LinearForce

class LinearDistanceForce(LinearForce):
    """
    /**
     * Pure virtual class for sinks and sources
     */
    """
    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getFalloffType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_falloff_type(LinearDistanceForce self)
        
        /**
         * falloff_type query
         */
        """
        pass

    def getForceCenter(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_force_center(LinearDistanceForce self)
        
        /**
         * force_center query
         */
        """
        pass

    def getRadius(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_radius(LinearDistanceForce self)
        
        /**
         * radius query
         */
        """
        pass

    def getScalarTerm(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_scalar_term(LinearDistanceForce self)
        
        /**
         * calculate the term based on falloff
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_falloff_type(self, LinearDistanceForce_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_falloff_type(LinearDistanceForce self)
        
        /**
         * falloff_type query
         */
        """
        pass

    def get_force_center(self, LinearDistanceForce_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_force_center(LinearDistanceForce self)
        
        /**
         * force_center query
         */
        """
        pass

    def get_radius(self, LinearDistanceForce_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_radius(LinearDistanceForce self)
        
        /**
         * radius query
         */
        """
        pass

    def get_scalar_term(self, LinearDistanceForce_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_scalar_term(LinearDistanceForce self)
        
        /**
         * calculate the term based on falloff
         */
        """
        pass

    def setFalloffType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_falloff_type(const LinearDistanceForce self, int ft)
        
        /**
         * falloff_type encapsulating wrap
         */
        """
        pass

    def setForceCenter(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_force_center(const LinearDistanceForce self, const LPoint3f p)
        
        /**
         * set the force center
         */
        """
        pass

    def setRadius(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_radius(const LinearDistanceForce self, float r)
        
        /**
         * set the radius
         */
        """
        pass

    def set_falloff_type(self, const_LinearDistanceForce_self, int_ft): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_falloff_type(const LinearDistanceForce self, int ft)
        
        /**
         * falloff_type encapsulating wrap
         */
        """
        pass

    def set_force_center(self, const_LinearDistanceForce_self, const_LPoint3f_p): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_force_center(const LinearDistanceForce self, const LPoint3f p)
        
        /**
         * set the force center
         */
        """
        pass

    def set_radius(self, const_LinearDistanceForce_self, float_r): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_radius(const LinearDistanceForce self, float r)
        
        /**
         * set the radius
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
        'FTONEOVERR': 0,
        'FTONEOVERRCUBED': 2,
        'FTONEOVERRSQUARED': 1,
        'FT_ONE_OVER_R': 0,
        'FT_ONE_OVER_R_CUBED': 2,
        'FT_ONE_OVER_R_SQUARED': 1,
        '__doc__': '/**\n * Pure virtual class for sinks and sources\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.physics.LinearDistanceForce' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFDC9DECF10>'
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFDC9DECF10>)>'
        'getFalloffType': None, # (!) real value is "<method 'getFalloffType' of 'panda3d.physics.LinearDistanceForce' objects>"
        'getForceCenter': None, # (!) real value is "<method 'getForceCenter' of 'panda3d.physics.LinearDistanceForce' objects>"
        'getRadius': None, # (!) real value is "<method 'getRadius' of 'panda3d.physics.LinearDistanceForce' objects>"
        'getScalarTerm': None, # (!) real value is "<method 'getScalarTerm' of 'panda3d.physics.LinearDistanceForce' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFDC9DECF10>)>'
        'get_falloff_type': None, # (!) real value is "<method 'get_falloff_type' of 'panda3d.physics.LinearDistanceForce' objects>"
        'get_force_center': None, # (!) real value is "<method 'get_force_center' of 'panda3d.physics.LinearDistanceForce' objects>"
        'get_radius': None, # (!) real value is "<method 'get_radius' of 'panda3d.physics.LinearDistanceForce' objects>"
        'get_scalar_term': None, # (!) real value is "<method 'get_scalar_term' of 'panda3d.physics.LinearDistanceForce' objects>"
        'setFalloffType': None, # (!) real value is "<method 'setFalloffType' of 'panda3d.physics.LinearDistanceForce' objects>"
        'setForceCenter': None, # (!) real value is "<method 'setForceCenter' of 'panda3d.physics.LinearDistanceForce' objects>"
        'setRadius': None, # (!) real value is "<method 'setRadius' of 'panda3d.physics.LinearDistanceForce' objects>"
        'set_falloff_type': None, # (!) real value is "<method 'set_falloff_type' of 'panda3d.physics.LinearDistanceForce' objects>"
        'set_force_center': None, # (!) real value is "<method 'set_force_center' of 'panda3d.physics.LinearDistanceForce' objects>"
        'set_radius': None, # (!) real value is "<method 'set_radius' of 'panda3d.physics.LinearDistanceForce' objects>"
    }
    FTONEOVERR = 0
    FTONEOVERRCUBED = 2
    FTONEOVERRSQUARED = 1
    FT_ONE_OVER_R = 0
    FT_ONE_OVER_R_CUBED = 2
    FT_ONE_OVER_R_SQUARED = 1


