# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .TypedWritableReferenceCount import TypedWritableReferenceCount

class RenderAttrib(TypedWritableReferenceCount):
    """
    /**
     * This is the base class for a number of render attributes (other than
     * transform) that may be set on scene graph nodes to control the appearance
     * of geometry.  This includes TextureAttrib, ColorAttrib, etc.
     *
     * RenderAttrib represents render attributes that always propagate down to the
     * leaves without regard to the particular node they are assigned to.  A
     * RenderAttrib will have the same effect on a leaf node whether it is
     * assigned to the graph at the leaf or several nodes above.  This is
     * different from RenderEffect, which represents a particular render property
     * that is applied immediately to the node on which it is encountered, like
     * billboarding or decaling.
     *
     * You should not attempt to create or modify a RenderAttrib directly;
     * instead, use the make() method of the appropriate kind of attrib you want.
     * This will allocate and return a new RenderAttrib of the appropriate type,
     * and it may share pointers if possible.  Do not modify the new RenderAttrib
     * if you wish to change its properties; instead, create a new one.
     */
    """
    def compareTo(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        compare_to(RenderAttrib self, const RenderAttrib other)
        
        /**
         * Provides an arbitrary ordering among all unique RenderAttribs, so we can
         * store the essentially different ones in a big set and throw away the rest.
         *
         * This method is not needed outside of the RenderAttrib class because all
         * equivalent RenderAttrib objects are guaranteed to share the same pointer;
         * thus, a pointer comparison is always sufficient.
         */
        """
        pass

    def compare_to(self, RenderAttrib_self, const_RenderAttrib_other): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        compare_to(RenderAttrib self, const RenderAttrib other)
        
        /**
         * Provides an arbitrary ordering among all unique RenderAttribs, so we can
         * store the essentially different ones in a big set and throw away the rest.
         *
         * This method is not needed outside of the RenderAttrib class because all
         * equivalent RenderAttrib objects are guaranteed to share the same pointer;
         * thus, a pointer comparison is always sufficient.
         */
        """
        pass

    def compose(self, RenderAttrib_self, const_RenderAttrib_other): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        compose(RenderAttrib self, const RenderAttrib other)
        
        /**
         * Returns a new RenderAttrib object that represents the composition of this
         * attrib with the other attrib.  In most cases, this is the same as the other
         * attrib; a compose b produces b.  Some kinds of attributes, like a
         * TextureTransform, for instance, might produce a new result: a compose b
         * produces c.
         */
        """
        pass

    def garbageCollect(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        garbage_collect()
        
        /**
         * Performs a garbage-collection cycle.  This is called automatically from
         * RenderState::garbage_collect(); see that method for more information.
         */
        """
        pass

    def garbage_collect(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        garbage_collect()
        
        /**
         * Performs a garbage-collection cycle.  This is called automatically from
         * RenderState::garbage_collect(); see that method for more information.
         */
        """
        pass

    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getHash(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_hash(RenderAttrib self)
        
        /**
         * Returns a suitable hash value for phash_map.
         */
        """
        pass

    def getNumAttribs(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_attribs()
        
        /**
         * Returns the total number of unique RenderAttrib objects allocated in the
         * world.  This will go up and down during normal operations.
         */
        """
        pass

    def getSlot(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_slot(RenderAttrib self)
        """
        pass

    def getUnique(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_unique(RenderAttrib self)
        
        /**
         * Returns the pointer to the unique RenderAttrib in the cache that is
         * equivalent to this one.  This may be the same pointer as this object, or it
         * may be a different pointer; but it will be an equivalent object, and it
         * will be a shared pointer.  This may be called from time to time to improve
         * cache benefits.
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_hash(self, RenderAttrib_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_hash(RenderAttrib self)
        
        /**
         * Returns a suitable hash value for phash_map.
         */
        """
        pass

    def get_num_attribs(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_attribs()
        
        /**
         * Returns the total number of unique RenderAttrib objects allocated in the
         * world.  This will go up and down during normal operations.
         */
        """
        pass

    def get_slot(self, RenderAttrib_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_slot(RenderAttrib self)
        """
        pass

    def get_unique(self, RenderAttrib_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_unique(RenderAttrib self)
        
        /**
         * Returns the pointer to the unique RenderAttrib in the cache that is
         * equivalent to this one.  This may be the same pointer as this object, or it
         * may be a different pointer; but it will be an equivalent object, and it
         * will be a shared pointer.  This may be called from time to time to improve
         * cache benefits.
         */
        """
        pass

    def invertCompose(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        invert_compose(RenderAttrib self, const RenderAttrib other)
        
        /**
         * Returns a new RenderAttrib object that represents the composition of the
         * inverse of this attrib with the other attrib.  In most cases, this is the
         * same as the other attrib; !a compose b produces b.  Some kinds of
         * attributes, like a TextureTransform, for instance, might produce a new
         * result: !a compose b produces c.
         *
         * This is similar to compose() except that the source attrib is inverted
         * first.  This is used to compute the relative attribute for one node as
         * viewed from some other node, which is especially useful for transform-type
         * attributes.
         */
        """
        pass

    def invert_compose(self, RenderAttrib_self, const_RenderAttrib_other): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        invert_compose(RenderAttrib self, const RenderAttrib other)
        
        /**
         * Returns a new RenderAttrib object that represents the composition of the
         * inverse of this attrib with the other attrib.  In most cases, this is the
         * same as the other attrib; !a compose b produces b.  Some kinds of
         * attributes, like a TextureTransform, for instance, might produce a new
         * result: !a compose b produces c.
         *
         * This is similar to compose() except that the source attrib is inverted
         * first.  This is used to compute the relative attribute for one node as
         * viewed from some other node, which is especially useful for transform-type
         * attributes.
         */
        """
        pass

    def listAttribs(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        list_attribs(ostream out)
        
        /**
         * Lists all of the RenderAttribs in the cache to the output stream, one per
         * line.  This can be quite a lot of output if the cache is large, so be
         * prepared.
         */
        """
        pass

    def list_attribs(self, ostream_out): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        list_attribs(ostream out)
        
        /**
         * Lists all of the RenderAttribs in the cache to the output stream, one per
         * line.  This can be quite a lot of output if the cache is large, so be
         * prepared.
         */
        """
        pass

    def lowerAttribCanOverride(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        lower_attrib_can_override(RenderAttrib self)
        
        /**
         * Intended to be overridden by derived RenderAttrib types to specify how two
         * consecutive RenderAttrib objects of the same type interact.
         *
         * This should return false if a RenderAttrib on a higher node will compose
         * into a RenderAttrib on a lower node that has a higher override value, or
         * true if the lower RenderAttrib will completely replace the state.
         *
         * The default behavior is false: normally, a RenderAttrib in the graph cannot
         * completely override a RenderAttrib above it, regardless of its override
         * value--instead, the two attribs are composed.  But for some kinds of
         * RenderAttribs, it is useful to allow this kind of override.
         *
         * This method only handles the one special case of a lower RenderAttrib with
         * a higher override value.  If the higher RenderAttrib has a higher override
         * value, it always completely overrides.  And if both RenderAttribs have the
         * same override value, they are always composed.
         */
        """
        pass

    def lower_attrib_can_override(self, RenderAttrib_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        lower_attrib_can_override(RenderAttrib self)
        
        /**
         * Intended to be overridden by derived RenderAttrib types to specify how two
         * consecutive RenderAttrib objects of the same type interact.
         *
         * This should return false if a RenderAttrib on a higher node will compose
         * into a RenderAttrib on a lower node that has a higher override value, or
         * true if the lower RenderAttrib will completely replace the state.
         *
         * The default behavior is false: normally, a RenderAttrib in the graph cannot
         * completely override a RenderAttrib above it, regardless of its override
         * value--instead, the two attribs are composed.  But for some kinds of
         * RenderAttribs, it is useful to allow this kind of override.
         *
         * This method only handles the one special case of a lower RenderAttrib with
         * a higher override value.  If the higher RenderAttrib has a higher override
         * value, it always completely overrides.  And if both RenderAttribs have the
         * same override value, they are always composed.
         */
        """
        pass

    def output(self, RenderAttrib_self, ostream_out): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        output(RenderAttrib self, ostream out)
        
        /**
         *
         */
        """
        pass

    def validateAttribs(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        validate_attribs()
        
        /**
         * Ensures that the cache is still stored in sorted order.  Returns true if
         * so, false if there is a problem (which implies someone has modified one of
         * the supposedly-const RenderAttrib objects).
         */
        """
        pass

    def validate_attribs(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        validate_attribs()
        
        /**
         * Ensures that the cache is still stored in sorted order.  Returns true if
         * so, false if there is a problem (which implies someone has modified one of
         * the supposedly-const RenderAttrib objects).
         */
        """
        pass

    def write(self, RenderAttrib_self, ostream_out, int_indent_level): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        write(RenderAttrib self, ostream out, int indent_level)
        
        /**
         *
         */
        """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __hash__(self, *args, **kwargs): # real signature unknown
        """ Return hash(self). """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    slot = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        'MAlways': 8,
        'MConstant': 11,
        'MEqual': 3,
        'MEyeCubeMap': 3,
        'MEyeNormal': 5,
        'MEyePosition': 8,
        'MEyeSphereMap': 1,
        'MGreater': 5,
        'MGreaterEqual': 7,
        'MLess': 2,
        'MLessEqual': 4,
        'MNever': 1,
        'MNone': 0,
        'MNotEqual': 6,
        'MOff': 0,
        'MPointSprite': 9,
        'MUnused': 7,
        'MUnused2': 10,
        'MWorldCubeMap': 2,
        'MWorldNormal': 4,
        'MWorldPosition': 6,
        'M_always': 8,
        'M_constant': 11,
        'M_equal': 3,
        'M_eye_cube_map': 3,
        'M_eye_normal': 5,
        'M_eye_position': 8,
        'M_eye_sphere_map': 1,
        'M_greater': 5,
        'M_greater_equal': 7,
        'M_less': 2,
        'M_less_equal': 4,
        'M_never': 1,
        'M_none': 0,
        'M_not_equal': 6,
        'M_off': 0,
        'M_point_sprite': 9,
        'M_unused': 7,
        'M_unused2': 10,
        'M_world_cube_map': 2,
        'M_world_normal': 4,
        'M_world_position': 6,
        '__doc__': '/**\n * This is the base class for a number of render attributes (other than\n * transform) that may be set on scene graph nodes to control the appearance\n * of geometry.  This includes TextureAttrib, ColorAttrib, etc.\n *\n * RenderAttrib represents render attributes that always propagate down to the\n * leaves without regard to the particular node they are assigned to.  A\n * RenderAttrib will have the same effect on a leaf node whether it is\n * assigned to the graph at the leaf or several nodes above.  This is\n * different from RenderEffect, which represents a particular render property\n * that is applied immediately to the node on which it is encountered, like\n * billboarding or decaling.\n *\n * You should not attempt to create or modify a RenderAttrib directly;\n * instead, use the make() method of the appropriate kind of attrib you want.\n * This will allocate and return a new RenderAttrib of the appropriate type,\n * and it may share pointers if possible.  Do not modify the new RenderAttrib\n * if you wish to change its properties; instead, create a new one.\n */',
        '__eq__': None, # (!) real value is "<slot wrapper '__eq__' of 'panda3d.core.RenderAttrib' objects>"
        '__ge__': None, # (!) real value is "<slot wrapper '__ge__' of 'panda3d.core.RenderAttrib' objects>"
        '__gt__': None, # (!) real value is "<slot wrapper '__gt__' of 'panda3d.core.RenderAttrib' objects>"
        '__hash__': None, # (!) real value is "<slot wrapper '__hash__' of 'panda3d.core.RenderAttrib' objects>"
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.RenderAttrib' objects>"
        '__le__': None, # (!) real value is "<slot wrapper '__le__' of 'panda3d.core.RenderAttrib' objects>"
        '__lt__': None, # (!) real value is "<slot wrapper '__lt__' of 'panda3d.core.RenderAttrib' objects>"
        '__ne__': None, # (!) real value is "<slot wrapper '__ne__' of 'panda3d.core.RenderAttrib' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE2919D0>'
        '__repr__': None, # (!) real value is "<slot wrapper '__repr__' of 'panda3d.core.RenderAttrib' objects>"
        '__str__': None, # (!) real value is "<slot wrapper '__str__' of 'panda3d.core.RenderAttrib' objects>"
        'compareTo': None, # (!) real value is "<method 'compareTo' of 'panda3d.core.RenderAttrib' objects>"
        'compare_to': None, # (!) real value is "<method 'compare_to' of 'panda3d.core.RenderAttrib' objects>"
        'compose': None, # (!) real value is "<method 'compose' of 'panda3d.core.RenderAttrib' objects>"
        'garbageCollect': None, # (!) real value is '<staticmethod(<built-in method garbageCollect of type object at 0x00007FFCFE2919D0>)>'
        'garbage_collect': None, # (!) real value is '<staticmethod(<built-in method garbage_collect of type object at 0x00007FFCFE2919D0>)>'
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE2919D0>)>'
        'getHash': None, # (!) real value is "<method 'getHash' of 'panda3d.core.RenderAttrib' objects>"
        'getNumAttribs': None, # (!) real value is '<staticmethod(<built-in method getNumAttribs of type object at 0x00007FFCFE2919D0>)>'
        'getSlot': None, # (!) real value is "<method 'getSlot' of 'panda3d.core.RenderAttrib' objects>"
        'getUnique': None, # (!) real value is "<method 'getUnique' of 'panda3d.core.RenderAttrib' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE2919D0>)>'
        'get_hash': None, # (!) real value is "<method 'get_hash' of 'panda3d.core.RenderAttrib' objects>"
        'get_num_attribs': None, # (!) real value is '<staticmethod(<built-in method get_num_attribs of type object at 0x00007FFCFE2919D0>)>'
        'get_slot': None, # (!) real value is "<method 'get_slot' of 'panda3d.core.RenderAttrib' objects>"
        'get_unique': None, # (!) real value is "<method 'get_unique' of 'panda3d.core.RenderAttrib' objects>"
        'invertCompose': None, # (!) real value is "<method 'invertCompose' of 'panda3d.core.RenderAttrib' objects>"
        'invert_compose': None, # (!) real value is "<method 'invert_compose' of 'panda3d.core.RenderAttrib' objects>"
        'listAttribs': None, # (!) real value is '<staticmethod(<built-in method listAttribs of type object at 0x00007FFCFE2919D0>)>'
        'list_attribs': None, # (!) real value is '<staticmethod(<built-in method list_attribs of type object at 0x00007FFCFE2919D0>)>'
        'lowerAttribCanOverride': None, # (!) real value is "<method 'lowerAttribCanOverride' of 'panda3d.core.RenderAttrib' objects>"
        'lower_attrib_can_override': None, # (!) real value is "<method 'lower_attrib_can_override' of 'panda3d.core.RenderAttrib' objects>"
        'output': None, # (!) real value is "<method 'output' of 'panda3d.core.RenderAttrib' objects>"
        'slot': None, # (!) real value is "<attribute 'slot' of 'panda3d.core.RenderAttrib' objects>"
        'validateAttribs': None, # (!) real value is '<staticmethod(<built-in method validateAttribs of type object at 0x00007FFCFE2919D0>)>'
        'validate_attribs': None, # (!) real value is '<staticmethod(<built-in method validate_attribs of type object at 0x00007FFCFE2919D0>)>'
        'write': None, # (!) real value is "<method 'write' of 'panda3d.core.RenderAttrib' objects>"
    }
    MAlways = 8
    MConstant = 11
    MEqual = 3
    MEyeCubeMap = 3
    MEyeNormal = 5
    MEyePosition = 8
    MEyeSphereMap = 1
    MGreater = 5
    MGreaterEqual = 7
    MLess = 2
    MLessEqual = 4
    MNever = 1
    MNone = 0
    MNotEqual = 6
    MOff = 0
    MPointSprite = 9
    MUnused = 7
    MUnused2 = 10
    MWorldCubeMap = 2
    MWorldNormal = 4
    MWorldPosition = 6
    M_always = 8
    M_constant = 11
    M_equal = 3
    M_eye_cube_map = 3
    M_eye_normal = 5
    M_eye_position = 8
    M_eye_sphere_map = 1
    M_greater = 5
    M_greater_equal = 7
    M_less = 2
    M_less_equal = 4
    M_never = 1
    M_none = 0
    M_not_equal = 6
    M_off = 0
    M_point_sprite = 9
    M_unused = 7
    M_unused2 = 10
    M_world_cube_map = 2
    M_world_normal = 4
    M_world_position = 6


