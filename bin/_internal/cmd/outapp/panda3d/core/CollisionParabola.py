# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .CollisionSolid import CollisionSolid

class CollisionParabola(CollisionSolid):
    """
    /**
     * This defines a parabolic arc, or subset of an arc, similar to the path of a
     * projectile or falling object.  It is finite, having a specific beginning
     * and end, but it is infinitely thin.
     *
     * Think of it as a wire bending from point t1 to point t2 along the path of a
     * pre-defined parabola.
     */
    """
    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getParabola(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_parabola(CollisionParabola self)
        
        /**
         * Returns the parabola specified by this solid.
         */
        """
        pass

    def getT1(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_t1(CollisionParabola self)
        
        /**
         * Returns the starting point on the parabola.
         */
        """
        pass

    def getT2(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_t2(CollisionParabola self)
        
        /**
         * Returns the ending point on the parabola.
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_parabola(self, CollisionParabola_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_parabola(CollisionParabola self)
        
        /**
         * Returns the parabola specified by this solid.
         */
        """
        pass

    def get_t1(self, CollisionParabola_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_t1(CollisionParabola self)
        
        /**
         * Returns the starting point on the parabola.
         */
        """
        pass

    def get_t2(self, CollisionParabola_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_t2(CollisionParabola self)
        
        /**
         * Returns the ending point on the parabola.
         */
        """
        pass

    def setParabola(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_parabola(const CollisionParabola self, const LParabolaf parabola)
        
        /**
         * Replaces the parabola specified by this solid.
         */
        """
        pass

    def setT1(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_t1(const CollisionParabola self, float t1)
        
        /**
         * Changes the starting point on the parabola.
         */
        """
        pass

    def setT2(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_t2(const CollisionParabola self, float t2)
        
        /**
         * Changes the ending point on the parabola.
         */
        """
        pass

    def set_parabola(self, const_CollisionParabola_self, const_LParabolaf_parabola): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_parabola(const CollisionParabola self, const LParabolaf parabola)
        
        /**
         * Replaces the parabola specified by this solid.
         */
        """
        pass

    def set_t1(self, const_CollisionParabola_self, float_t1): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_t1(const CollisionParabola self, float t1)
        
        /**
         * Changes the starting point on the parabola.
         */
        """
        pass

    def set_t2(self, const_CollisionParabola_self, float_t2): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_t2(const CollisionParabola self, float t2)
        
        /**
         * Changes the ending point on the parabola.
         */
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    parabola = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    t1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    t2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__doc__': '/**\n * This defines a parabolic arc, or subset of an arc, similar to the path of a\n * projectile or falling object.  It is finite, having a specific beginning\n * and end, but it is infinitely thin.\n *\n * Think of it as a wire bending from point t1 to point t2 along the path of a\n * pre-defined parabola.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.CollisionParabola' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE2D0560>'
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE2D0560>)>'
        'getParabola': None, # (!) real value is "<method 'getParabola' of 'panda3d.core.CollisionParabola' objects>"
        'getT1': None, # (!) real value is "<method 'getT1' of 'panda3d.core.CollisionParabola' objects>"
        'getT2': None, # (!) real value is "<method 'getT2' of 'panda3d.core.CollisionParabola' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE2D0560>)>'
        'get_parabola': None, # (!) real value is "<method 'get_parabola' of 'panda3d.core.CollisionParabola' objects>"
        'get_t1': None, # (!) real value is "<method 'get_t1' of 'panda3d.core.CollisionParabola' objects>"
        'get_t2': None, # (!) real value is "<method 'get_t2' of 'panda3d.core.CollisionParabola' objects>"
        'parabola': None, # (!) real value is "<attribute 'parabola' of 'panda3d.core.CollisionParabola' objects>"
        'setParabola': None, # (!) real value is "<method 'setParabola' of 'panda3d.core.CollisionParabola' objects>"
        'setT1': None, # (!) real value is "<method 'setT1' of 'panda3d.core.CollisionParabola' objects>"
        'setT2': None, # (!) real value is "<method 'setT2' of 'panda3d.core.CollisionParabola' objects>"
        'set_parabola': None, # (!) real value is "<method 'set_parabola' of 'panda3d.core.CollisionParabola' objects>"
        'set_t1': None, # (!) real value is "<method 'set_t1' of 'panda3d.core.CollisionParabola' objects>"
        'set_t2': None, # (!) real value is "<method 'set_t2' of 'panda3d.core.CollisionParabola' objects>"
        't1': None, # (!) real value is "<attribute 't1' of 'panda3d.core.CollisionParabola' objects>"
        't2': None, # (!) real value is "<attribute 't2' of 'panda3d.core.CollisionParabola' objects>"
    }


