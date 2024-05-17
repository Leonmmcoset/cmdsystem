# encoding: utf-8
# module panda3d.ode
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\ode.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import panda3d.core as __panda3d_core


from .OdeGeom import OdeGeom

class OdeRayGeom(OdeGeom):
    """
    /**
     *
     */
    """
    def get(self, OdeRayGeom_self, LVecBase3f_start, LVecBase3f_dir): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get(OdeRayGeom self, LVecBase3f start, LVecBase3f dir)
        """
        pass

    def getBackfaceCull(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_backface_cull(OdeRayGeom self)
        """
        pass

    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getClosestHit(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_closest_hit(const OdeRayGeom self)
        """
        pass

    def getDirection(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_direction(OdeRayGeom self)
        """
        pass

    def getFirstContact(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_first_contact(OdeRayGeom self)
        """
        pass

    def getLength(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_length(const OdeRayGeom self)
        """
        pass

    def getStart(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_start(OdeRayGeom self)
        """
        pass

    def get_backface_cull(self, OdeRayGeom_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_backface_cull(OdeRayGeom self)
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_closest_hit(self, const_OdeRayGeom_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_closest_hit(const OdeRayGeom self)
        """
        pass

    def get_direction(self, OdeRayGeom_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_direction(OdeRayGeom self)
        """
        pass

    def get_first_contact(self, OdeRayGeom_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_first_contact(OdeRayGeom self)
        """
        pass

    def get_length(self, const_OdeRayGeom_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_length(const OdeRayGeom self)
        """
        pass

    def get_start(self, OdeRayGeom_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_start(OdeRayGeom self)
        """
        pass

    def set(self, const_OdeRayGeom_self, const_LVecBase3f_start, const_LVecBase3f_dir): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set(const OdeRayGeom self, const LVecBase3f start, const LVecBase3f dir)
        set(const OdeRayGeom self, float px, float py, float pz, float dx, float dy, float dz)
        """
        pass

    def setClosestHit(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_closest_hit(const OdeRayGeom self, int closest_hit)
        """
        pass

    def setLength(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_length(const OdeRayGeom self, float length)
        """
        pass

    def setParams(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_params(const OdeRayGeom self, int first_contact, int backface_cull)
        """
        pass

    def set_closest_hit(self, const_OdeRayGeom_self, int_closest_hit): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_closest_hit(const OdeRayGeom self, int closest_hit)
        """
        pass

    def set_length(self, const_OdeRayGeom_self, float_length): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_length(const OdeRayGeom self, float length)
        """
        pass

    def set_params(self, const_OdeRayGeom_self, int_first_contact, int_backface_cull): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_params(const OdeRayGeom self, int first_contact, int backface_cull)
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
        '__doc__': '/**\n *\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.ode.OdeRayGeom' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFDC9DEDF10>'
        'get': None, # (!) real value is "<method 'get' of 'panda3d.ode.OdeRayGeom' objects>"
        'getBackfaceCull': None, # (!) real value is "<method 'getBackfaceCull' of 'panda3d.ode.OdeRayGeom' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFDC9DEDF10>)>'
        'getClosestHit': None, # (!) real value is "<method 'getClosestHit' of 'panda3d.ode.OdeRayGeom' objects>"
        'getDirection': None, # (!) real value is "<method 'getDirection' of 'panda3d.ode.OdeRayGeom' objects>"
        'getFirstContact': None, # (!) real value is "<method 'getFirstContact' of 'panda3d.ode.OdeRayGeom' objects>"
        'getLength': None, # (!) real value is "<method 'getLength' of 'panda3d.ode.OdeRayGeom' objects>"
        'getStart': None, # (!) real value is "<method 'getStart' of 'panda3d.ode.OdeRayGeom' objects>"
        'get_backface_cull': None, # (!) real value is "<method 'get_backface_cull' of 'panda3d.ode.OdeRayGeom' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFDC9DEDF10>)>'
        'get_closest_hit': None, # (!) real value is "<method 'get_closest_hit' of 'panda3d.ode.OdeRayGeom' objects>"
        'get_direction': None, # (!) real value is "<method 'get_direction' of 'panda3d.ode.OdeRayGeom' objects>"
        'get_first_contact': None, # (!) real value is "<method 'get_first_contact' of 'panda3d.ode.OdeRayGeom' objects>"
        'get_length': None, # (!) real value is "<method 'get_length' of 'panda3d.ode.OdeRayGeom' objects>"
        'get_start': None, # (!) real value is "<method 'get_start' of 'panda3d.ode.OdeRayGeom' objects>"
        'set': None, # (!) real value is "<method 'set' of 'panda3d.ode.OdeRayGeom' objects>"
        'setClosestHit': None, # (!) real value is "<method 'setClosestHit' of 'panda3d.ode.OdeRayGeom' objects>"
        'setLength': None, # (!) real value is "<method 'setLength' of 'panda3d.ode.OdeRayGeom' objects>"
        'setParams': None, # (!) real value is "<method 'setParams' of 'panda3d.ode.OdeRayGeom' objects>"
        'set_closest_hit': None, # (!) real value is "<method 'set_closest_hit' of 'panda3d.ode.OdeRayGeom' objects>"
        'set_length': None, # (!) real value is "<method 'set_length' of 'panda3d.ode.OdeRayGeom' objects>"
        'set_params': None, # (!) real value is "<method 'set_params' of 'panda3d.ode.OdeRayGeom' objects>"
    }


