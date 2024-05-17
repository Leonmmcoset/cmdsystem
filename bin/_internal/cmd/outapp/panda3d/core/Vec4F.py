# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .LVecBase4f import LVecBase4f

class Vec4F(LVecBase4f):
    """
    /**
     * This is a four-component vector distance.
     */
    """
    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getXy(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_xy(LVector4f self)
        
        /**
         * Returns the x and y component of this vector
         */
        """
        pass

    def getXyz(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_xyz(LVector4f self)
        
        /**
         * Returns the x, y and z component of this vector
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_xy(self, LVector4f_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_xy(LVector4f self)
        
        /**
         * Returns the x and y component of this vector
         */
        """
        pass

    def get_xyz(self, LVector4f_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_xyz(LVector4f self)
        
        /**
         * Returns the x, y and z component of this vector
         */
        """
        pass

    def normalized(self, LVector4f_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        normalized(LVector4f self)
        
        /**
         * Normalizes the vector and returns the normalized vector as a copy.  If the
         * vector was a zero-length vector, a zero length vector will be returned.
         */
        """
        pass

    def project(self, LVector4f_self, const_LVecBase4f_onto): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        project(LVector4f self, const LVecBase4f onto)
        
        /**
         * Returns a new vector representing the projection of this vector onto
         * another one.  The resulting vector will be a scalar multiple of onto.
         */
        """
        pass

    def unitW(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        unit_w()
        
        /**
         * Returns a unit W vector.
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

    def unit_w(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        unit_w()
        
        /**
         * Returns a unit W vector.
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

    xyz = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__add__': None, # (!) real value is "<slot wrapper '__add__' of 'panda3d.core.LVector4f' objects>"
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.core.LVector4f' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.core.LVector4f' objects>"
        '__delattr__': None, # (!) real value is "<slot wrapper '__delattr__' of 'panda3d.core.LVector4f' objects>"
        '__doc__': '/**\n * This is a four-component vector distance.\n */',
        '__getattribute__': None, # (!) real value is "<slot wrapper '__getattribute__' of 'panda3d.core.LVector4f' objects>"
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.LVector4f' objects>"
        '__mul__': None, # (!) real value is "<slot wrapper '__mul__' of 'panda3d.core.LVector4f' objects>"
        '__neg__': None, # (!) real value is "<slot wrapper '__neg__' of 'panda3d.core.LVector4f' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE323250>'
        '__radd__': None, # (!) real value is "<slot wrapper '__radd__' of 'panda3d.core.LVector4f' objects>"
        '__repr__': None, # (!) real value is "<slot wrapper '__repr__' of 'panda3d.core.LVector4f' objects>"
        '__rmul__': None, # (!) real value is "<slot wrapper '__rmul__' of 'panda3d.core.LVector4f' objects>"
        '__rsub__': None, # (!) real value is "<slot wrapper '__rsub__' of 'panda3d.core.LVector4f' objects>"
        '__rtruediv__': None, # (!) real value is "<slot wrapper '__rtruediv__' of 'panda3d.core.LVector4f' objects>"
        '__setattr__': None, # (!) real value is "<slot wrapper '__setattr__' of 'panda3d.core.LVector4f' objects>"
        '__sub__': None, # (!) real value is "<slot wrapper '__sub__' of 'panda3d.core.LVector4f' objects>"
        '__truediv__': None, # (!) real value is "<slot wrapper '__truediv__' of 'panda3d.core.LVector4f' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE323250>)>'
        'getXy': None, # (!) real value is "<method 'getXy' of 'panda3d.core.LVector4f' objects>"
        'getXyz': None, # (!) real value is "<method 'getXyz' of 'panda3d.core.LVector4f' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE323250>)>'
        'get_xy': None, # (!) real value is "<method 'get_xy' of 'panda3d.core.LVector4f' objects>"
        'get_xyz': None, # (!) real value is "<method 'get_xyz' of 'panda3d.core.LVector4f' objects>"
        'normalized': None, # (!) real value is "<method 'normalized' of 'panda3d.core.LVector4f' objects>"
        'project': None, # (!) real value is "<method 'project' of 'panda3d.core.LVector4f' objects>"
        'unitW': None, # (!) real value is '<staticmethod(<built-in method unitW of type object at 0x00007FFCFE323250>)>'
        'unitX': None, # (!) real value is '<staticmethod(<built-in method unitX of type object at 0x00007FFCFE323250>)>'
        'unitY': None, # (!) real value is '<staticmethod(<built-in method unitY of type object at 0x00007FFCFE323250>)>'
        'unitZ': None, # (!) real value is '<staticmethod(<built-in method unitZ of type object at 0x00007FFCFE323250>)>'
        'unit_w': None, # (!) real value is '<staticmethod(<built-in method unit_w of type object at 0x00007FFCFE323250>)>'
        'unit_x': None, # (!) real value is '<staticmethod(<built-in method unit_x of type object at 0x00007FFCFE323250>)>'
        'unit_y': None, # (!) real value is '<staticmethod(<built-in method unit_y of type object at 0x00007FFCFE323250>)>'
        'unit_z': None, # (!) real value is '<staticmethod(<built-in method unit_z of type object at 0x00007FFCFE323250>)>'
        'xy': None, # (!) real value is "<attribute 'xy' of 'panda3d.core.LVector4f' objects>"
        'xyz': None, # (!) real value is "<attribute 'xyz' of 'panda3d.core.LVector4f' objects>"
        'zero': None, # (!) real value is '<staticmethod(<built-in method zero of type object at 0x00007FFCFE323250>)>'
    }


