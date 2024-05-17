# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .LVecBase3i import LVecBase3i

class LVector3i(LVecBase3i):
    """
    /**
     * This is a three-component vector distance (as opposed to a three-component
     * point, which represents a particular point in space).  Some of the methods
     * are slightly different between LPoint3 and LVector3; in particular,
     * subtraction of two points yields a vector, while addition of a vector and a
     * point yields a point.
     */
    """
    def back(self, int_cs): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        back(int cs)
        
        /**
         * Returns the back vector for the given coordinate system.
         */
        """
        pass

    def cross(self, LVector3i_self, const_LVecBase3i_other): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        cross(LVector3i self, const LVecBase3i other)
        
        /**
         *
         */
        """
        pass

    def down(self, int_cs): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        down(int cs)
        
        /**
         * Returns the down vector for the given coordinate system.
         */
        """
        pass

    def forward(self, int_cs): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        forward(int cs)
        
        /**
         * Returns the forward vector for the given coordinate system.
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
        get_xy(LVector3i self)
        
        /**
         * Returns a 2-component vector that shares just the first two components of
         * this vector.
         */
        """
        pass

    def getXz(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_xz(LVector3i self)
        
        /**
         * Returns a 2-component vector that shares just the first and last components
         * of this vector.
         */
        """
        pass

    def getYz(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_yz(LVector3i self)
        
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

    def get_xy(self, LVector3i_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_xy(LVector3i self)
        
        /**
         * Returns a 2-component vector that shares just the first two components of
         * this vector.
         */
        """
        pass

    def get_xz(self, LVector3i_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_xz(LVector3i self)
        
        /**
         * Returns a 2-component vector that shares just the first and last components
         * of this vector.
         */
        """
        pass

    def get_yz(self, LVector3i_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_yz(LVector3i self)
        
        /**
         * Returns a 2-component vector that shares just the last two components of
         * this vector.
         */
        """
        pass

    def left(self, int_cs): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        left(int cs)
        
        /**
         * Returns the left vector for the given coordinate system.
         */
        """
        pass

    def rfu(self, int_right, int_fwd, int_up, int_cs): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        rfu(int right, int fwd, int up, int cs)
        
        // INLINE_LINMATH static FLOATNAME(LVector3) & rfu(FLOATTYPE right,
        
        /**
         * Returns a vector that is described by its right, forward, and up
         * components, in whatever way the coordinate system represents that vector.
         */
        """
        pass

    def right(self, int_cs): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        right(int cs)
        
        /**
         * Returns the right vector for the given coordinate system.
         */
        """
        pass

    def unitX(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        unit_x()
        
        /**
         * Returns a unit X vector.
         */
        """
        pass

    def unitY(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        unit_y()
        
        /**
         * Returns a unit Y vector.
         */
        """
        pass

    def unitZ(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        unit_z()
        
        /**
         * Returns a unit Z vector.
         */
        """
        pass

    def unit_x(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        unit_x()
        
        /**
         * Returns a unit X vector.
         */
        """
        pass

    def unit_y(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        unit_y()
        
        /**
         * Returns a unit Y vector.
         */
        """
        pass

    def unit_z(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        unit_z()
        
        /**
         * Returns a unit Z vector.
         */
        """
        pass

    def up(self, int_cs): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        up(int cs)
        
        /**
         * Returns the up vector for the given coordinate system.
         */
        """
        pass

    def zero(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        zero()
        
        /**
         * Returns a zero-length vector.
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

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    def __sub__(self, *args, **kwargs): # real signature unknown
        """ Return self-value. """
        pass

    xy = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    xz = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    yz = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__add__': None, # (!) real value is "<slot wrapper '__add__' of 'panda3d.core.LVector3i' objects>"
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.core.LVector3i' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.core.LVector3i' objects>"
        '__delattr__': None, # (!) real value is "<slot wrapper '__delattr__' of 'panda3d.core.LVector3i' objects>"
        '__doc__': '/**\n * This is a three-component vector distance (as opposed to a three-component\n * point, which represents a particular point in space).  Some of the methods\n * are slightly different between LPoint3 and LVector3; in particular,\n * subtraction of two points yields a vector, while addition of a vector and a\n * point yields a point.\n */',
        '__getattribute__': None, # (!) real value is "<slot wrapper '__getattribute__' of 'panda3d.core.LVector3i' objects>"
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.LVector3i' objects>"
        '__mul__': None, # (!) real value is "<slot wrapper '__mul__' of 'panda3d.core.LVector3i' objects>"
        '__neg__': None, # (!) real value is "<slot wrapper '__neg__' of 'panda3d.core.LVector3i' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE322030>'
        '__radd__': None, # (!) real value is "<slot wrapper '__radd__' of 'panda3d.core.LVector3i' objects>"
        '__repr__': None, # (!) real value is "<slot wrapper '__repr__' of 'panda3d.core.LVector3i' objects>"
        '__rmul__': None, # (!) real value is "<slot wrapper '__rmul__' of 'panda3d.core.LVector3i' objects>"
        '__rsub__': None, # (!) real value is "<slot wrapper '__rsub__' of 'panda3d.core.LVector3i' objects>"
        '__setattr__': None, # (!) real value is "<slot wrapper '__setattr__' of 'panda3d.core.LVector3i' objects>"
        '__sub__': None, # (!) real value is "<slot wrapper '__sub__' of 'panda3d.core.LVector3i' objects>"
        'back': None, # (!) real value is '<staticmethod(<built-in method back of type object at 0x00007FFCFE322030>)>'
        'cross': None, # (!) real value is "<method 'cross' of 'panda3d.core.LVector3i' objects>"
        'down': None, # (!) real value is '<staticmethod(<built-in method down of type object at 0x00007FFCFE322030>)>'
        'forward': None, # (!) real value is '<staticmethod(<built-in method forward of type object at 0x00007FFCFE322030>)>'
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE322030>)>'
        'getXy': None, # (!) real value is "<method 'getXy' of 'panda3d.core.LVector3i' objects>"
        'getXz': None, # (!) real value is "<method 'getXz' of 'panda3d.core.LVector3i' objects>"
        'getYz': None, # (!) real value is "<method 'getYz' of 'panda3d.core.LVector3i' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE322030>)>'
        'get_xy': None, # (!) real value is "<method 'get_xy' of 'panda3d.core.LVector3i' objects>"
        'get_xz': None, # (!) real value is "<method 'get_xz' of 'panda3d.core.LVector3i' objects>"
        'get_yz': None, # (!) real value is "<method 'get_yz' of 'panda3d.core.LVector3i' objects>"
        'left': None, # (!) real value is '<staticmethod(<built-in method left of type object at 0x00007FFCFE322030>)>'
        'rfu': None, # (!) real value is '<staticmethod(<built-in method rfu of type object at 0x00007FFCFE322030>)>'
        'right': None, # (!) real value is '<staticmethod(<built-in method right of type object at 0x00007FFCFE322030>)>'
        'unitX': None, # (!) real value is '<staticmethod(<built-in method unitX of type object at 0x00007FFCFE322030>)>'
        'unitY': None, # (!) real value is '<staticmethod(<built-in method unitY of type object at 0x00007FFCFE322030>)>'
        'unitZ': None, # (!) real value is '<staticmethod(<built-in method unitZ of type object at 0x00007FFCFE322030>)>'
        'unit_x': None, # (!) real value is '<staticmethod(<built-in method unit_x of type object at 0x00007FFCFE322030>)>'
        'unit_y': None, # (!) real value is '<staticmethod(<built-in method unit_y of type object at 0x00007FFCFE322030>)>'
        'unit_z': None, # (!) real value is '<staticmethod(<built-in method unit_z of type object at 0x00007FFCFE322030>)>'
        'up': None, # (!) real value is '<staticmethod(<built-in method up of type object at 0x00007FFCFE322030>)>'
        'xy': None, # (!) real value is "<attribute 'xy' of 'panda3d.core.LVector3i' objects>"
        'xz': None, # (!) real value is "<attribute 'xz' of 'panda3d.core.LVector3i' objects>"
        'yz': None, # (!) real value is "<attribute 'yz' of 'panda3d.core.LVector3i' objects>"
        'zero': None, # (!) real value is '<staticmethod(<built-in method zero of type object at 0x00007FFCFE322030>)>'
    }


