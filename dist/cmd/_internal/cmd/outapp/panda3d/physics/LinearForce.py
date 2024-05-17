# encoding: utf-8
# module panda3d.physics
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\physics.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import panda3d.core as __panda3d_core


from .BaseForce import BaseForce

class LinearForce(BaseForce):
    """
    /**
     * A force that acts on a PhysicsObject by way of an Integrator.  This is a
     * pure virtual base class.
     */
    """
    def getAmplitude(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_amplitude(LinearForce self)
        
        /**
        
         */
        """
        pass

    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getMassDependent(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_mass_dependent(LinearForce self)
        
        /**
        
         */
        """
        pass

    def getVector(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_vector(const LinearForce self, const PhysicsObject po)
        
        /**
        
         */
        """
        pass

    def getVectorMasks(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_vector_masks(const LinearForce self)
        
        /**
        
         */
        """
        pass

    def get_amplitude(self, LinearForce_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_amplitude(LinearForce self)
        
        /**
        
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_mass_dependent(self, LinearForce_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_mass_dependent(LinearForce self)
        
        /**
        
         */
        """
        pass

    def get_vector(self, const_LinearForce_self, const_PhysicsObject_po): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_vector(const LinearForce self, const PhysicsObject po)
        
        /**
        
         */
        """
        pass

    def get_vector_masks(self, const_LinearForce_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_vector_masks(const LinearForce self)
        
        /**
        
         */
        """
        pass

    def makeCopy(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        make_copy(const LinearForce self)
        """
        pass

    def make_copy(self, const_LinearForce_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        make_copy(const LinearForce self)
        """
        pass

    def setAmplitude(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_amplitude(const LinearForce self, float a)
        
        /**
        
         */
        """
        pass

    def setMassDependent(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_mass_dependent(const LinearForce self, bool m)
        
        /**
        
         */
        """
        pass

    def setVectorMasks(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_vector_masks(const LinearForce self, bool x, bool y, bool z)
        
        /**
        
         */
        """
        pass

    def set_amplitude(self, const_LinearForce_self, float_a): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_amplitude(const LinearForce self, float a)
        
        /**
        
         */
        """
        pass

    def set_mass_dependent(self, const_LinearForce_self, bool_m): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_mass_dependent(const LinearForce self, bool m)
        
        /**
        
         */
        """
        pass

    def set_vector_masks(self, const_LinearForce_self, bool_x, bool_y, bool_z): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_vector_masks(const LinearForce self, bool x, bool y, bool z)
        
        /**
        
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
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.physics.LinearForce' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.physics.LinearForce' objects>"
        '__doc__': '/**\n * A force that acts on a PhysicsObject by way of an Integrator.  This is a\n * pure virtual base class.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.physics.LinearForce' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFDC9DEB950>'
        'getAmplitude': None, # (!) real value is "<method 'getAmplitude' of 'panda3d.physics.LinearForce' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFDC9DEB950>)>'
        'getMassDependent': None, # (!) real value is "<method 'getMassDependent' of 'panda3d.physics.LinearForce' objects>"
        'getVector': None, # (!) real value is "<method 'getVector' of 'panda3d.physics.LinearForce' objects>"
        'getVectorMasks': None, # (!) real value is "<method 'getVectorMasks' of 'panda3d.physics.LinearForce' objects>"
        'get_amplitude': None, # (!) real value is "<method 'get_amplitude' of 'panda3d.physics.LinearForce' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFDC9DEB950>)>'
        'get_mass_dependent': None, # (!) real value is "<method 'get_mass_dependent' of 'panda3d.physics.LinearForce' objects>"
        'get_vector': None, # (!) real value is "<method 'get_vector' of 'panda3d.physics.LinearForce' objects>"
        'get_vector_masks': None, # (!) real value is "<method 'get_vector_masks' of 'panda3d.physics.LinearForce' objects>"
        'makeCopy': None, # (!) real value is "<method 'makeCopy' of 'panda3d.physics.LinearForce' objects>"
        'make_copy': None, # (!) real value is "<method 'make_copy' of 'panda3d.physics.LinearForce' objects>"
        'setAmplitude': None, # (!) real value is "<method 'setAmplitude' of 'panda3d.physics.LinearForce' objects>"
        'setMassDependent': None, # (!) real value is "<method 'setMassDependent' of 'panda3d.physics.LinearForce' objects>"
        'setVectorMasks': None, # (!) real value is "<method 'setVectorMasks' of 'panda3d.physics.LinearForce' objects>"
        'set_amplitude': None, # (!) real value is "<method 'set_amplitude' of 'panda3d.physics.LinearForce' objects>"
        'set_mass_dependent': None, # (!) real value is "<method 'set_mass_dependent' of 'panda3d.physics.LinearForce' objects>"
        'set_vector_masks': None, # (!) real value is "<method 'set_vector_masks' of 'panda3d.physics.LinearForce' objects>"
    }


