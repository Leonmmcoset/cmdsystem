# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .LVecBase2f import LVecBase2f

class Vec2F(LVecBase2f):
    """
    /**
     * This is a two-component vector offset.
     */
    """
    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def normalized(self, LVector2f_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        normalized(LVector2f self)
        
        /**
         * Normalizes the vector and returns the normalized vector as a copy.  If the
         * vector was a zero-length vector, a zero length vector will be returned.
         */
        """
        pass

    def project(self, LVector2f_self, const_LVecBase2f_onto): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        project(LVector2f self, const LVecBase2f onto)
        
        /**
         * Returns a new vector representing the projection of this vector onto
         * another one.  The resulting vector will be a scalar multiple of onto.
         */
        """
        pass

    def signedAngleDeg(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        signed_angle_deg(LVector2f self, const LVector2f other)
        
        /**
         * returns the signed angled between two vectors.  normalization is NOT
         * necessary
         */
        """
        pass

    def signedAngleRad(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        signed_angle_rad(LVector2f self, const LVector2f other)
        
        /**
         * returns the signed angled between two vectors.  normalization is NOT
         * necessary
         */
        """
        pass

    def signed_angle_deg(self, LVector2f_self, const_LVector2f_other): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        signed_angle_deg(LVector2f self, const LVector2f other)
        
        /**
         * returns the signed angled between two vectors.  normalization is NOT
         * necessary
         */
        """
        pass

    def signed_angle_rad(self, LVector2f_self, const_LVector2f_other): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        signed_angle_rad(LVector2f self, const LVector2f other)
        
        /**
         * returns the signed angled between two vectors.  normalization is NOT
         * necessary
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

    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__add__': None, # (!) real value is "<slot wrapper '__add__' of 'panda3d.core.LVector2f' objects>"
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.core.LVector2f' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.core.LVector2f' objects>"
        '__delattr__': None, # (!) real value is "<slot wrapper '__delattr__' of 'panda3d.core.LVector2f' objects>"
        '__doc__': '/**\n * This is a two-component vector offset.\n */',
        '__getattribute__': None, # (!) real value is "<slot wrapper '__getattribute__' of 'panda3d.core.LVector2f' objects>"
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.LVector2f' objects>"
        '__mul__': None, # (!) real value is "<slot wrapper '__mul__' of 'panda3d.core.LVector2f' objects>"
        '__neg__': None, # (!) real value is "<slot wrapper '__neg__' of 'panda3d.core.LVector2f' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE320C40>'
        '__radd__': None, # (!) real value is "<slot wrapper '__radd__' of 'panda3d.core.LVector2f' objects>"
        '__repr__': None, # (!) real value is "<slot wrapper '__repr__' of 'panda3d.core.LVector2f' objects>"
        '__rmul__': None, # (!) real value is "<slot wrapper '__rmul__' of 'panda3d.core.LVector2f' objects>"
        '__rsub__': None, # (!) real value is "<slot wrapper '__rsub__' of 'panda3d.core.LVector2f' objects>"
        '__rtruediv__': None, # (!) real value is "<slot wrapper '__rtruediv__' of 'panda3d.core.LVector2f' objects>"
        '__setattr__': None, # (!) real value is "<slot wrapper '__setattr__' of 'panda3d.core.LVector2f' objects>"
        '__sub__': None, # (!) real value is "<slot wrapper '__sub__' of 'panda3d.core.LVector2f' objects>"
        '__truediv__': None, # (!) real value is "<slot wrapper '__truediv__' of 'panda3d.core.LVector2f' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE320C40>)>'
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE320C40>)>'
        'normalized': None, # (!) real value is "<method 'normalized' of 'panda3d.core.LVector2f' objects>"
        'project': None, # (!) real value is "<method 'project' of 'panda3d.core.LVector2f' objects>"
        'signedAngleDeg': None, # (!) real value is "<method 'signedAngleDeg' of 'panda3d.core.LVector2f' objects>"
        'signedAngleRad': None, # (!) real value is "<method 'signedAngleRad' of 'panda3d.core.LVector2f' objects>"
        'signed_angle_deg': None, # (!) real value is "<method 'signed_angle_deg' of 'panda3d.core.LVector2f' objects>"
        'signed_angle_rad': None, # (!) real value is "<method 'signed_angle_rad' of 'panda3d.core.LVector2f' objects>"
        'unitX': None, # (!) real value is '<staticmethod(<built-in method unitX of type object at 0x00007FFCFE320C40>)>'
        'unitY': None, # (!) real value is '<staticmethod(<built-in method unitY of type object at 0x00007FFCFE320C40>)>'
        'unit_x': None, # (!) real value is '<staticmethod(<built-in method unit_x of type object at 0x00007FFCFE320C40>)>'
        'unit_y': None, # (!) real value is '<staticmethod(<built-in method unit_y of type object at 0x00007FFCFE320C40>)>'
        'zero': None, # (!) real value is '<staticmethod(<built-in method zero of type object at 0x00007FFCFE320C40>)>'
    }


