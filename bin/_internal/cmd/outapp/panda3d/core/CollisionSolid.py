# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .CopyOnWriteObject import CopyOnWriteObject

class CollisionSolid(CopyOnWriteObject):
    """
    /**
     * The abstract base class for all things that can collide with other things
     * in the world, and all the things they can collide with (except geometry).
     *
     * This class and its derivatives really work very similarly to the way
     * BoundingVolume and all of its derivatives work.  There's a different
     * subclass for each basic shape of solid, and double-dispatch function calls
     * handle the subset of the N*N intersection tests that we care about.
     */
    """
    def clearEffectiveNormal(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_effective_normal(const CollisionSolid self)
        
        /**
         * Removes the normal previously set by set_effective_normal().
         */
        """
        pass

    def clear_effective_normal(self, const_CollisionSolid_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_effective_normal(const CollisionSolid self)
        
        /**
         * Removes the normal previously set by set_effective_normal().
         */
        """
        pass

    def getBounds(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_bounds(CollisionSolid self)
        
        /**
         * Returns the solid's bounding volume.
         */
        """
        pass

    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getCollisionOrigin(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_collision_origin(CollisionSolid self)
        """
        pass

    def getEffectiveNormal(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_effective_normal(CollisionSolid self)
        
        /**
         * Returns the normal that was set by set_effective_normal().  It is an error
         * to call this unless has_effective_normal() returns true.
         */
        """
        pass

    def getRespectEffectiveNormal(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_respect_effective_normal(CollisionSolid self)
        
        /**
         * See set_respect_effective_normal().
         */
        """
        pass

    def get_bounds(self, CollisionSolid_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_bounds(CollisionSolid self)
        
        /**
         * Returns the solid's bounding volume.
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_collision_origin(self, CollisionSolid_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_collision_origin(CollisionSolid self)
        """
        pass

    def get_effective_normal(self, CollisionSolid_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_effective_normal(CollisionSolid self)
        
        /**
         * Returns the normal that was set by set_effective_normal().  It is an error
         * to call this unless has_effective_normal() returns true.
         */
        """
        pass

    def get_respect_effective_normal(self, CollisionSolid_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_respect_effective_normal(CollisionSolid self)
        
        /**
         * See set_respect_effective_normal().
         */
        """
        pass

    def hasEffectiveNormal(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_effective_normal(CollisionSolid self)
        
        /**
         * Returns true if a special normal was set by set_effective_normal(), false
         * otherwise.
         */
        """
        pass

    def has_effective_normal(self, CollisionSolid_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_effective_normal(CollisionSolid self)
        
        /**
         * Returns true if a special normal was set by set_effective_normal(), false
         * otherwise.
         */
        """
        pass

    def isTangible(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_tangible(CollisionSolid self)
        
        /**
         * Returns whether the solid is considered 'tangible' or not.  An intangible
         * solid has no effect in a CollisionHandlerPusher (except to throw an event);
         * it's useful for defining 'trigger' planes and spheres, that cause an effect
         * when passed through.
         */
        """
        pass

    def is_tangible(self, CollisionSolid_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_tangible(CollisionSolid self)
        
        /**
         * Returns whether the solid is considered 'tangible' or not.  An intangible
         * solid has no effect in a CollisionHandlerPusher (except to throw an event);
         * it's useful for defining 'trigger' planes and spheres, that cause an effect
         * when passed through.
         */
        """
        pass

    def output(self, CollisionSolid_self, ostream_out): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        output(CollisionSolid self, ostream out)
        
        /**
         *
         */
        """
        pass

    def setBounds(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_bounds(const CollisionSolid self, const BoundingVolume bounding_volume)
        
        /**
         * Returns the solid's bounding volume.
         */
        """
        pass

    def setEffectiveNormal(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_effective_normal(const CollisionSolid self, const LVector3f effective_normal)
        
        /**
         * Records a false normal for this CollisionSolid that will be reported by the
         * collision system with all collisions into it, instead of its actual normal.
         * This is useful as a workaround for the problem of an avatar wanting to
         * stand on a sloping ground; by storing a false normal, the ground appears to
         * be perfectly level, and the avatar does not tend to slide down it.
         */
        """
        pass

    def setRespectEffectiveNormal(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_respect_effective_normal(const CollisionSolid self, bool respect_effective_normal)
        
        /**
         * This is only meaningful for CollisionSolids that will be added to a
         * traverser as colliders.  It is normally true, but if set false, it means
         * that this particular solid does not care about the "effective" normal of
         * other solids it meets, but rather always uses the true normal.
         */
        """
        pass

    def setTangible(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_tangible(const CollisionSolid self, bool tangible)
        
        /**
         * Sets the current state of the 'tangible' flag.  Set this true to make the
         * solid tangible, so that a CollisionHandlerPusher will not allow another
         * object to intersect it, or false to make it intangible, so that a
         * CollisionHandlerPusher will ignore it except to throw an event.
         */
        """
        pass

    def set_bounds(self, const_CollisionSolid_self, const_BoundingVolume_bounding_volume): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_bounds(const CollisionSolid self, const BoundingVolume bounding_volume)
        
        /**
         * Returns the solid's bounding volume.
         */
        """
        pass

    def set_effective_normal(self, const_CollisionSolid_self, const_LVector3f_effective_normal): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_effective_normal(const CollisionSolid self, const LVector3f effective_normal)
        
        /**
         * Records a false normal for this CollisionSolid that will be reported by the
         * collision system with all collisions into it, instead of its actual normal.
         * This is useful as a workaround for the problem of an avatar wanting to
         * stand on a sloping ground; by storing a false normal, the ground appears to
         * be perfectly level, and the avatar does not tend to slide down it.
         */
        """
        pass

    def set_respect_effective_normal(self, const_CollisionSolid_self, bool_respect_effective_normal): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_respect_effective_normal(const CollisionSolid self, bool respect_effective_normal)
        
        /**
         * This is only meaningful for CollisionSolids that will be added to a
         * traverser as colliders.  It is normally true, but if set false, it means
         * that this particular solid does not care about the "effective" normal of
         * other solids it meets, but rather always uses the true normal.
         */
        """
        pass

    def set_tangible(self, const_CollisionSolid_self, bool_tangible): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_tangible(const CollisionSolid self, bool tangible)
        
        /**
         * Sets the current state of the 'tangible' flag.  Set this true to make the
         * solid tangible, so that a CollisionHandlerPusher will not allow another
         * object to intersect it, or false to make it intangible, so that a
         * CollisionHandlerPusher will ignore it except to throw an event.
         */
        """
        pass

    def write(self, CollisionSolid_self, ostream_out, int_indent_level): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        write(CollisionSolid self, ostream out, int indent_level)
        
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

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    bounds = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    collision_origin = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    respect_effective_normal = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tangible = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__doc__': "/**\n * The abstract base class for all things that can collide with other things\n * in the world, and all the things they can collide with (except geometry).\n *\n * This class and its derivatives really work very similarly to the way\n * BoundingVolume and all of its derivatives work.  There's a different\n * subclass for each basic shape of solid, and double-dispatch function calls\n * handle the subset of the N*N intersection tests that we care about.\n */",
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.CollisionSolid' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE2CDBA0>'
        '__repr__': None, # (!) real value is "<slot wrapper '__repr__' of 'panda3d.core.CollisionSolid' objects>"
        '__str__': None, # (!) real value is "<slot wrapper '__str__' of 'panda3d.core.CollisionSolid' objects>"
        'bounds': None, # (!) real value is "<attribute 'bounds' of 'panda3d.core.CollisionSolid' objects>"
        'clearEffectiveNormal': None, # (!) real value is "<method 'clearEffectiveNormal' of 'panda3d.core.CollisionSolid' objects>"
        'clear_effective_normal': None, # (!) real value is "<method 'clear_effective_normal' of 'panda3d.core.CollisionSolid' objects>"
        'collision_origin': None, # (!) real value is "<attribute 'collision_origin' of 'panda3d.core.CollisionSolid' objects>"
        'getBounds': None, # (!) real value is "<method 'getBounds' of 'panda3d.core.CollisionSolid' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE2CDBA0>)>'
        'getCollisionOrigin': None, # (!) real value is "<method 'getCollisionOrigin' of 'panda3d.core.CollisionSolid' objects>"
        'getEffectiveNormal': None, # (!) real value is "<method 'getEffectiveNormal' of 'panda3d.core.CollisionSolid' objects>"
        'getRespectEffectiveNormal': None, # (!) real value is "<method 'getRespectEffectiveNormal' of 'panda3d.core.CollisionSolid' objects>"
        'get_bounds': None, # (!) real value is "<method 'get_bounds' of 'panda3d.core.CollisionSolid' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE2CDBA0>)>'
        'get_collision_origin': None, # (!) real value is "<method 'get_collision_origin' of 'panda3d.core.CollisionSolid' objects>"
        'get_effective_normal': None, # (!) real value is "<method 'get_effective_normal' of 'panda3d.core.CollisionSolid' objects>"
        'get_respect_effective_normal': None, # (!) real value is "<method 'get_respect_effective_normal' of 'panda3d.core.CollisionSolid' objects>"
        'hasEffectiveNormal': None, # (!) real value is "<method 'hasEffectiveNormal' of 'panda3d.core.CollisionSolid' objects>"
        'has_effective_normal': None, # (!) real value is "<method 'has_effective_normal' of 'panda3d.core.CollisionSolid' objects>"
        'isTangible': None, # (!) real value is "<method 'isTangible' of 'panda3d.core.CollisionSolid' objects>"
        'is_tangible': None, # (!) real value is "<method 'is_tangible' of 'panda3d.core.CollisionSolid' objects>"
        'output': None, # (!) real value is "<method 'output' of 'panda3d.core.CollisionSolid' objects>"
        'respect_effective_normal': None, # (!) real value is "<attribute 'respect_effective_normal' of 'panda3d.core.CollisionSolid' objects>"
        'setBounds': None, # (!) real value is "<method 'setBounds' of 'panda3d.core.CollisionSolid' objects>"
        'setEffectiveNormal': None, # (!) real value is "<method 'setEffectiveNormal' of 'panda3d.core.CollisionSolid' objects>"
        'setRespectEffectiveNormal': None, # (!) real value is "<method 'setRespectEffectiveNormal' of 'panda3d.core.CollisionSolid' objects>"
        'setTangible': None, # (!) real value is "<method 'setTangible' of 'panda3d.core.CollisionSolid' objects>"
        'set_bounds': None, # (!) real value is "<method 'set_bounds' of 'panda3d.core.CollisionSolid' objects>"
        'set_effective_normal': None, # (!) real value is "<method 'set_effective_normal' of 'panda3d.core.CollisionSolid' objects>"
        'set_respect_effective_normal': None, # (!) real value is "<method 'set_respect_effective_normal' of 'panda3d.core.CollisionSolid' objects>"
        'set_tangible': None, # (!) real value is "<method 'set_tangible' of 'panda3d.core.CollisionSolid' objects>"
        'tangible': None, # (!) real value is "<attribute 'tangible' of 'panda3d.core.CollisionSolid' objects>"
        'write': None, # (!) real value is "<method 'write' of 'panda3d.core.CollisionSolid' objects>"
    }


