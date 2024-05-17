# encoding: utf-8
# module panda3d.physics
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\physics.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import panda3d.core as __panda3d_core


from .LinearForce import LinearForce

class LinearVectorForce(LinearForce):
    """
    /**
     * Simple directed vector force.  Suitable for gravity, non-turbulent wind,
     * etc...
     */
    """
    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getLocalVector(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_local_vector(LinearVectorForce self)
        
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

    def get_local_vector(self, LinearVectorForce_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_local_vector(LinearVectorForce self)
        
        /**
         *
         */
        """
        pass

    def setVector(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_vector(const LinearVectorForce self, const LVector3f v)
        set_vector(const LinearVectorForce self, float x, float y, float z)
        
        /**
         * encapsulating wrapper
         */
        
        /**
         * piecewise encapsulating wrapper
         */
        """
        pass

    def set_vector(self, const_LinearVectorForce_self, const_LVector3f_v): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_vector(const LinearVectorForce self, const LVector3f v)
        set_vector(const LinearVectorForce self, float x, float y, float z)
        
        /**
         * encapsulating wrapper
         */
        
        /**
         * piecewise encapsulating wrapper
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
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.physics.LinearVectorForce' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.physics.LinearVectorForce' objects>"
        '__doc__': '/**\n * Simple directed vector force.  Suitable for gravity, non-turbulent wind,\n * etc...\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.physics.LinearVectorForce' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFDC9DEE130>'
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFDC9DEE130>)>'
        'getLocalVector': None, # (!) real value is "<method 'getLocalVector' of 'panda3d.physics.LinearVectorForce' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFDC9DEE130>)>'
        'get_local_vector': None, # (!) real value is "<method 'get_local_vector' of 'panda3d.physics.LinearVectorForce' objects>"
        'setVector': None, # (!) real value is "<method 'setVector' of 'panda3d.physics.LinearVectorForce' objects>"
        'set_vector': None, # (!) real value is "<method 'set_vector' of 'panda3d.physics.LinearVectorForce' objects>"
    }


