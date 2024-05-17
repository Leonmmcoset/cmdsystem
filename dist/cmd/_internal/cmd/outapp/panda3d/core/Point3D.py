# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .LVecBase3d import LVecBase3d

class Point3D(LVecBase3d):
    """
    /**
     * This is a three-component point in space (as opposed to a three-component
     * vector, which represents a direction and a distance).  Some of the methods
     * are slightly different between LPoint3 and LVector3; in particular,
     * subtraction of two points yields a vector, while addition of a vector and a
     * point yields a point.
     */
    """
    def cross(self, LPoint3d_self, const_LVecBase3d_other): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        cross(LPoint3d self, const LVecBase3d other)
        
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

    def getXy(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_xy(LPoint3d self)
        
        /**
         * Returns a 2-component vector that shares just the first two components of
         * this vector.
         */
        """
        pass

    def getXz(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_xz(LPoint3d self)
        
        /**
         * Returns a 2-component vector that shares just the first and last components
         * of this vector.
         */
        """
        pass

    def getYz(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_yz(LPoint3d self)
        
        /**
         * Returns a 2-component vector that shares just the last two components of
         * this vector.
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_xy(self, LPoint3d_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_xy(LPoint3d self)
        
        /**
         * Returns a 2-component vector that shares just the first two components of
         * this vector.
         */
        """
        pass

    def get_xz(self, LPoint3d_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_xz(LPoint3d self)
        
        /**
         * Returns a 2-component vector that shares just the first and last components
         * of this vector.
         */
        """
        pass

    def get_yz(self, LPoint3d_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_yz(LPoint3d self)
        
        /**
         * Returns a 2-component vector that shares just the last two components of
         * this vector.
         */
        """
        pass

    def normalized(self, LPoint3d_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        normalized(LPoint3d self)
        
        /**
         * Normalizes the vector and returns the normalized vector as a copy.  If the
         * vector was a zero-length vector, a zero length vector will be returned.
         */
        """
        pass

    def origin(self, int_cs): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        origin(int cs)
        
        /**
         * Returns the origin of the indicated coordinate system.  This is always 0,
         * 0, 0 with all of our existing coordinate systems; it's hard to imagine it
         * ever being different.
         */
        """
        pass

    def project(self, LPoint3d_self, const_LVecBase3d_onto): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        project(LPoint3d self, const LVecBase3d onto)
        
        /**
         * Returns a new vector representing the projection of this vector onto
         * another one.  The resulting vector will be a scalar multiple of onto.
         */
        """
        pass

    def rfu(self, double_right, double_fwd, double_up, int_cs): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        rfu(double right, double fwd, double up, int cs)
        
        /**
         * Returns a point described by right, forward, up displacements from the
         * origin, wherever that maps to in the given coordinate system.
         */
        """
        pass

    def unitX(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        unit_x()
        
        /**
         * Returns a unit X point.
         */
        """
        pass

    def unitY(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        unit_y()
        
        /**
         * Returns a unit Y point.
         */
        """
        pass

    def unitZ(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        unit_z()
        
        /**
         * Returns a unit Z point.
         */
        """
        pass

    def unit_x(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        unit_x()
        
        /**
         * Returns a unit X point.
         */
        """
        pass

    def unit_y(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        unit_y()
        
        /**
         * Returns a unit Y point.
         */
        """
        pass

    def unit_z(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        unit_z()
        
        /**
         * Returns a unit Z point.
         */
        """
        pass

    def zero(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        zero()
        
        /**
         * Returns a zero-length point.
         */
        """
        pass

    def __add__(self, *args, **kwargs): # real signature unknown
        """ Return self+value. """
        pass

    def __copy__(self, *args, **kwargs): # real signature unknown
        pass

    def __deepcopy__(self, *args, **kwargs): # real signature unknown
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __mul__(self, *args, **kwargs): # real signature unknown
        """ Return self*value. """
        pass

    def __neg__(self, *args, **kwargs): # real signature unknown
        """ -self """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __radd__(self, *args, **kwargs): # real signature unknown
        """ Return value+self. """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __rmul__(self, *args, **kwargs): # real signature unknown
        """ Return value*self. """
        pass

    def __rsub__(self, *args, **kwargs): # real signature unknown
        """ Return value-self. """
        pass

    def __rtruediv__(self, *args, **kwargs): # real signature unknown
        """ Return value/self. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    def __sub__(self, *args, **kwargs): # real signature unknown
        """ Return self-value. """
        pass

    def __truediv__(self, *args, **kwargs): # real signature unknown
        """ Return self/value. """
        pass

    xy = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    xz = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    yz = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__add__': None, # (!) real value is "<slot wrapper '__add__' of 'panda3d.core.LPoint3d' objects>"
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.core.LPoint3d' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.core.LPoint3d' objects>"
        '__delattr__': None, # (!) real value is "<slot wrapper '__delattr__' of 'panda3d.core.LPoint3d' objects>"
        '__doc__': '/**\n * This is a three-component point in space (as opposed to a three-component\n * vector, which represents a direction and a distance).  Some of the methods\n * are slightly different between LPoint3 and LVector3; in particular,\n * subtraction of two points yields a vector, while addition of a vector and a\n * point yields a point.\n */',
        '__getattribute__': None, # (!) real value is "<slot wrapper '__getattribute__' of 'panda3d.core.LPoint3d' objects>"
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.LPoint3d' objects>"
        '__mul__': None, # (!) real value is "<slot wrapper '__mul__' of 'panda3d.core.LPoint3d' objects>"
        '__neg__': None, # (!) real value is "<slot wrapper '__neg__' of 'panda3d.core.LPoint3d' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE3223D0>'
        '__radd__': None, # (!) real value is "<slot wrapper '__radd__' of 'panda3d.core.LPoint3d' objects>"
        '__repr__': None, # (!) real value is "<slot wrapper '__repr__' of 'panda3d.core.LPoint3d' objects>"
        '__rmul__': None, # (!) real value is "<slot wrapper '__rmul__' of 'panda3d.core.LPoint3d' objects>"
        '__rsub__': None, # (!) real value is "<slot wrapper '__rsub__' of 'panda3d.core.LPoint3d' objects>"
        '__rtruediv__': None, # (!) real value is "<slot wrapper '__rtruediv__' of 'panda3d.core.LPoint3d' objects>"
        '__setattr__': None, # (!) real value is "<slot wrapper '__setattr__' of 'panda3d.core.LPoint3d' objects>"
        '__sub__': None, # (!) real value is "<slot wrapper '__sub__' of 'panda3d.core.LPoint3d' objects>"
        '__truediv__': None, # (!) real value is "<slot wrapper '__truediv__' of 'panda3d.core.LPoint3d' objects>"
        'cross': None, # (!) real value is "<method 'cross' of 'panda3d.core.LPoint3d' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE3223D0>)>'
        'getXy': None, # (!) real value is "<method 'getXy' of 'panda3d.core.LPoint3d' objects>"
        'getXz': None, # (!) real value is "<method 'getXz' of 'panda3d.core.LPoint3d' objects>"
        'getYz': None, # (!) real value is "<method 'getYz' of 'panda3d.core.LPoint3d' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE3223D0>)>'
        'get_xy': None, # (!) real value is "<method 'get_xy' of 'panda3d.core.LPoint3d' objects>"
        'get_xz': None, # (!) real value is "<method 'get_xz' of 'panda3d.core.LPoint3d' objects>"
        'get_yz': None, # (!) real value is "<method 'get_yz' of 'panda3d.core.LPoint3d' objects>"
        'normalized': None, # (!) real value is "<method 'normalized' of 'panda3d.core.LPoint3d' objects>"
        'origin': None, # (!) real value is '<staticmethod(<built-in method origin of type object at 0x00007FFCFE3223D0>)>'
        'project': None, # (!) real value is "<method 'project' of 'panda3d.core.LPoint3d' objects>"
        'rfu': None, # (!) real value is '<staticmethod(<built-in method rfu of type object at 0x00007FFCFE3223D0>)>'
        'unitX': None, # (!) real value is '<staticmethod(<built-in method unitX of type object at 0x00007FFCFE3223D0>)>'
        'unitY': None, # (!) real value is '<staticmethod(<built-in method unitY of type object at 0x00007FFCFE3223D0>)>'
        'unitZ': None, # (!) real value is '<staticmethod(<built-in method unitZ of type object at 0x00007FFCFE3223D0>)>'
        'unit_x': None, # (!) real value is '<staticmethod(<built-in method unit_x of type object at 0x00007FFCFE3223D0>)>'
        'unit_y': None, # (!) real value is '<staticmethod(<built-in method unit_y of type object at 0x00007FFCFE3223D0>)>'
        'unit_z': None, # (!) real value is '<staticmethod(<built-in method unit_z of type object at 0x00007FFCFE3223D0>)>'
        'xy': None, # (!) real value is "<attribute 'xy' of 'panda3d.core.LPoint3d' objects>"
        'xz': None, # (!) real value is "<attribute 'xz' of 'panda3d.core.LPoint3d' objects>"
        'yz': None, # (!) real value is "<attribute 'yz' of 'panda3d.core.LPoint3d' objects>"
        'zero': None, # (!) real value is '<staticmethod(<built-in method zero of type object at 0x00007FFCFE3223D0>)>'
    }


