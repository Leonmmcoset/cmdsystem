# encoding: utf-8
# module panda3d.physics
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\physics.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import panda3d.core as __panda3d_core


from .BaseForce import BaseForce

class AngularForce(BaseForce):
    """
    /**
     * pure virtual parent of all quat-based forces.
     */
    """
    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getQuat(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_quat(const AngularForce self, const PhysicsObject po)
        
        /**
         * access query
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_quat(self, const_AngularForce_self, const_PhysicsObject_po): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_quat(const AngularForce self, const PhysicsObject po)
        
        /**
         * access query
         */
        """
        pass

    def makeCopy(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        make_copy(AngularForce self)
        """
        pass

    def make_copy(self, AngularForce_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        make_copy(AngularForce self)
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
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.physics.AngularForce' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.physics.AngularForce' objects>"
        '__doc__': '/**\n * pure virtual parent of all quat-based forces.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.physics.AngularForce' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFDC9DEBB20>'
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFDC9DEBB20>)>'
        'getQuat': None, # (!) real value is "<method 'getQuat' of 'panda3d.physics.AngularForce' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFDC9DEBB20>)>'
        'get_quat': None, # (!) real value is "<method 'get_quat' of 'panda3d.physics.AngularForce' objects>"
        'makeCopy': None, # (!) real value is "<method 'makeCopy' of 'panda3d.physics.AngularForce' objects>"
        'make_copy': None, # (!) real value is "<method 'make_copy' of 'panda3d.physics.AngularForce' objects>"
    }


