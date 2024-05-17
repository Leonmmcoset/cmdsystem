# encoding: utf-8
# module panda3d.egg
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\egg.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import panda3d.core as __panda3d_core


from .EggPrimitive import EggPrimitive

class EggSurface(EggPrimitive):
    """
    /**
     * A parametric surface of some kind.  See EggNurbsSurface.
     */
    """
    def assign(self, const_EggSurface_self, const_EggSurface_copy): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        assign(const EggSurface self, const EggSurface copy)
        
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

    def getUSubdiv(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_u_subdiv(EggSurface self)
        
        /**
         * Returns the requested number of subdivisions in the U direction, or 0 if no
         * particular subdivisions have been requested.
         */
        """
        pass

    def getVSubdiv(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_v_subdiv(EggSurface self)
        
        /**
         * Returns the requested number of subdivisions in the U direction, or 0 if no
         * particular subdivisions have been requested.
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_u_subdiv(self, EggSurface_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_u_subdiv(EggSurface self)
        
        /**
         * Returns the requested number of subdivisions in the U direction, or 0 if no
         * particular subdivisions have been requested.
         */
        """
        pass

    def get_v_subdiv(self, EggSurface_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_v_subdiv(EggSurface self)
        
        /**
         * Returns the requested number of subdivisions in the U direction, or 0 if no
         * particular subdivisions have been requested.
         */
        """
        pass

    def setUSubdiv(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_u_subdiv(const EggSurface self, int subdiv)
        
        /**
         * Sets the number of subdivisions in the U direction that will be requested
         * across the surface.  (This doesn't necessary guarantee that this number of
         * subdivisions will be made; it's just a hint to any surface renderer or
         * quick tesselator.)  Set the number to 0 to disable the hint.
         */
        """
        pass

    def setVSubdiv(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_v_subdiv(const EggSurface self, int subdiv)
        
        /**
         * Sets the number of subdivisions in the U direction that will be requested
         * across the surface.  (This doesn't necessary guarantee that this number of
         * subdivisions will be made; it's just a hint to any surface renderer or
         * quick tesselator.)  Set the number to 0 to disable the hint.
         */
        """
        pass

    def set_u_subdiv(self, const_EggSurface_self, int_subdiv): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_u_subdiv(const EggSurface self, int subdiv)
        
        /**
         * Sets the number of subdivisions in the U direction that will be requested
         * across the surface.  (This doesn't necessary guarantee that this number of
         * subdivisions will be made; it's just a hint to any surface renderer or
         * quick tesselator.)  Set the number to 0 to disable the hint.
         */
        """
        pass

    def set_v_subdiv(self, const_EggSurface_self, int_subdiv): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_v_subdiv(const EggSurface self, int subdiv)
        
        /**
         * Sets the number of subdivisions in the U direction that will be requested
         * across the surface.  (This doesn't necessary guarantee that this number of
         * subdivisions will be made; it's just a hint to any surface renderer or
         * quick tesselator.)  Set the number to 0 to disable the hint.
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
        '__doc__': '/**\n * A parametric surface of some kind.  See EggNurbsSurface.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.egg.EggSurface' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFDC68D0520>'
        'assign': None, # (!) real value is "<method 'assign' of 'panda3d.egg.EggSurface' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFDC68D0520>)>'
        'getUSubdiv': None, # (!) real value is "<method 'getUSubdiv' of 'panda3d.egg.EggSurface' objects>"
        'getVSubdiv': None, # (!) real value is "<method 'getVSubdiv' of 'panda3d.egg.EggSurface' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFDC68D0520>)>'
        'get_u_subdiv': None, # (!) real value is "<method 'get_u_subdiv' of 'panda3d.egg.EggSurface' objects>"
        'get_v_subdiv': None, # (!) real value is "<method 'get_v_subdiv' of 'panda3d.egg.EggSurface' objects>"
        'setUSubdiv': None, # (!) real value is "<method 'setUSubdiv' of 'panda3d.egg.EggSurface' objects>"
        'setVSubdiv': None, # (!) real value is "<method 'setVSubdiv' of 'panda3d.egg.EggSurface' objects>"
        'set_u_subdiv': None, # (!) real value is "<method 'set_u_subdiv' of 'panda3d.egg.EggSurface' objects>"
        'set_v_subdiv': None, # (!) real value is "<method 'set_v_subdiv' of 'panda3d.egg.EggSurface' objects>"
    }


