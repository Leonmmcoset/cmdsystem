# encoding: utf-8
# module panda3d.bullet
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\bullet.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import panda3d.core as __panda3d_core


from .BulletConstraint import BulletConstraint

class BulletSphericalConstraint(BulletConstraint):
    """
    /**
     * A constraint between two rigid bodies, each with a pivot point.  The pivot
     * points are described in the body's local space.  The constraint limits
     * movement of the two rigid bodies in such a way that the pivot points match
     * in global space.  The spherical constraint can be seen as a "ball and
     * socket" joint.
     */
    """
    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getPivotInA(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_pivot_in_a(BulletSphericalConstraint self)
        
        /**
         *
         */
        """
        pass

    def getPivotInB(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_pivot_in_b(BulletSphericalConstraint self)
        
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

    def get_pivot_in_a(self, BulletSphericalConstraint_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_pivot_in_a(BulletSphericalConstraint self)
        
        /**
         *
         */
        """
        pass

    def get_pivot_in_b(self, BulletSphericalConstraint_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_pivot_in_b(BulletSphericalConstraint self)
        
        /**
         *
         */
        """
        pass

    def setPivotA(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_pivot_a(const BulletSphericalConstraint self, const LPoint3f pivot_a)
        
        // Pivots
        
        // Pivots
        
        /**
         *
         */
        """
        pass

    def setPivotB(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_pivot_b(const BulletSphericalConstraint self, const LPoint3f pivot_b)
        
        /**
         *
         */
        """
        pass

    def set_pivot_a(self, const_BulletSphericalConstraint_self, const_LPoint3f_pivot_a): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_pivot_a(const BulletSphericalConstraint self, const LPoint3f pivot_a)
        
        // Pivots
        
        // Pivots
        
        /**
         *
         */
        """
        pass

    def set_pivot_b(self, const_BulletSphericalConstraint_self, const_LPoint3f_pivot_b): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_pivot_b(const BulletSphericalConstraint self, const LPoint3f pivot_b)
        
        /**
         *
         */
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    pivot_a = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pivot_b = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__doc__': '/**\n * A constraint between two rigid bodies, each with a pivot point.  The pivot\n * points are described in the body\'s local space.  The constraint limits\n * movement of the two rigid bodies in such a way that the pivot points match\n * in global space.  The spherical constraint can be seen as a "ball and\n * socket" joint.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.bullet.BulletSphericalConstraint' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFDC68D1960>'
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFDC68D1960>)>'
        'getPivotInA': None, # (!) real value is "<method 'getPivotInA' of 'panda3d.bullet.BulletSphericalConstraint' objects>"
        'getPivotInB': None, # (!) real value is "<method 'getPivotInB' of 'panda3d.bullet.BulletSphericalConstraint' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFDC68D1960>)>'
        'get_pivot_in_a': None, # (!) real value is "<method 'get_pivot_in_a' of 'panda3d.bullet.BulletSphericalConstraint' objects>"
        'get_pivot_in_b': None, # (!) real value is "<method 'get_pivot_in_b' of 'panda3d.bullet.BulletSphericalConstraint' objects>"
        'pivot_a': None, # (!) real value is "<attribute 'pivot_a' of 'panda3d.bullet.BulletSphericalConstraint' objects>"
        'pivot_b': None, # (!) real value is "<attribute 'pivot_b' of 'panda3d.bullet.BulletSphericalConstraint' objects>"
        'setPivotA': None, # (!) real value is "<method 'setPivotA' of 'panda3d.bullet.BulletSphericalConstraint' objects>"
        'setPivotB': None, # (!) real value is "<method 'setPivotB' of 'panda3d.bullet.BulletSphericalConstraint' objects>"
        'set_pivot_a': None, # (!) real value is "<method 'set_pivot_a' of 'panda3d.bullet.BulletSphericalConstraint' objects>"
        'set_pivot_b': None, # (!) real value is "<method 'set_pivot_b' of 'panda3d.bullet.BulletSphericalConstraint' objects>"
    }


