# encoding: utf-8
# module panda3d.ode
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\ode.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import panda3d.core as __panda3d_core


class OdeSpace(__panda3d_core.TypedObject):
    """
    /**
     *
     */
    """
    def add(self, const_OdeSpace_self, OdeSpace_space): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add(const OdeSpace self, OdeSpace space)
        add(const OdeSpace self, OdeGeom geom)
        """
        pass

    def autoCollide(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        auto_collide(const OdeSpace self)
        """
        pass

    def auto_collide(self, const_OdeSpace_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        auto_collide(const OdeSpace self)
        """
        pass

    def clean(self, const_OdeSpace_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clean(const OdeSpace self)
        """
        pass

    def collide(self, const_OdeSpace_self, object_arg, object_near_callback): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        collide(const OdeSpace self, object arg, object near_callback)
        """
        pass

    def convert(self, OdeSpace_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        convert(OdeSpace self)
        """
        pass

    def convertToHashSpace(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        convert_to_hash_space(OdeSpace self)
        """
        pass

    def convertToQuadTreeSpace(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        convert_to_quad_tree_space(OdeSpace self)
        """
        pass

    def convertToSimpleSpace(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        convert_to_simple_space(OdeSpace self)
        """
        pass

    def convert_to_hash_space(self, OdeSpace_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        convert_to_hash_space(OdeSpace self)
        """
        pass

    def convert_to_quad_tree_space(self, OdeSpace_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        convert_to_quad_tree_space(OdeSpace self)
        """
        pass

    def convert_to_simple_space(self, OdeSpace_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        convert_to_simple_space(OdeSpace self)
        """
        pass

    def destroy(self, const_OdeSpace_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        destroy(const OdeSpace self)
        """
        pass

    def disable(self, const_OdeSpace_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        disable(const OdeSpace self)
        """
        pass

    def enable(self, const_OdeSpace_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        enable(const OdeSpace self)
        """
        pass

    def getAABB(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_AABB(OdeSpace self, LVecBase3f min, LVecBase3f max)
        """
        pass

    def getAABounds(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_AA_bounds(OdeSpace self)
        """
        pass

    def getCategoryBits(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_category_bits(const OdeSpace self)
        """
        pass

    def getClass(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class(OdeSpace self)
        """
        pass

    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getCleanup(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_cleanup(OdeSpace self)
        """
        pass

    def getCollideBits(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_collide_bits(const OdeSpace self)
        """
        pass

    def getCollideId(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_collide_id(const OdeSpace self, OdeGeom geom)
        get_collide_id(const OdeSpace self, dxGeom o1)
        """
        pass

    def getCollisionEvent(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_collision_event(const OdeSpace self)
        """
        pass

    def getConvertedGeom(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_converted_geom(OdeSpace self, int i)
        """
        pass

    def getConvertedSpace(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_converted_space(OdeSpace self)
        """
        pass

    def getGeom(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_geom(const OdeSpace self, int i)
        """
        pass

    def getNumGeoms(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_geoms(OdeSpace self)
        """
        pass

    def getSpace(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_space(OdeSpace self)
        """
        pass

    def getSurfaceType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_surface_type(const OdeSpace self, OdeGeom geom)
        get_surface_type(const OdeSpace self, dxGeom o1)
        """
        pass

    def get_AABB(self, OdeSpace_self, LVecBase3f_min, LVecBase3f_max): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_AABB(OdeSpace self, LVecBase3f min, LVecBase3f max)
        """
        pass

    def get_AA_bounds(self, OdeSpace_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_AA_bounds(OdeSpace self)
        """
        pass

    def get_category_bits(self, const_OdeSpace_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_category_bits(const OdeSpace self)
        """
        pass

    def get_class(self, OdeSpace_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class(OdeSpace self)
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_cleanup(self, OdeSpace_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_cleanup(OdeSpace self)
        """
        pass

    def get_collide_bits(self, const_OdeSpace_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_collide_bits(const OdeSpace self)
        """
        pass

    def get_collide_id(self, const_OdeSpace_self, OdeGeom_geom): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_collide_id(const OdeSpace self, OdeGeom geom)
        get_collide_id(const OdeSpace self, dxGeom o1)
        """
        pass

    def get_collision_event(self, const_OdeSpace_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_collision_event(const OdeSpace self)
        """
        pass

    def get_converted_geom(self, OdeSpace_self, int_i): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_converted_geom(OdeSpace self, int i)
        """
        pass

    def get_converted_space(self, OdeSpace_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_converted_space(OdeSpace self)
        """
        pass

    def get_geom(self, const_OdeSpace_self, int_i): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_geom(const OdeSpace self, int i)
        """
        pass

    def get_num_geoms(self, OdeSpace_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_geoms(OdeSpace self)
        """
        pass

    def get_space(self, OdeSpace_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_space(OdeSpace self)
        """
        pass

    def get_surface_type(self, const_OdeSpace_self, OdeGeom_geom): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_surface_type(const OdeSpace self, OdeGeom geom)
        get_surface_type(const OdeSpace self, dxGeom o1)
        """
        pass

    def isEmpty(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_empty(OdeSpace self)
        
        /**
         * Returns true if the ID is 0, meaning the OdeSpace does not point to a valid
         * space.  It is an error to call a method on an empty space.  Note that an
         * empty OdeSpace also evaluates to False.
         */
        """
        pass

    def isEnabled(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_enabled(const OdeSpace self)
        """
        pass

    def isSpace(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_space(const OdeSpace self)
        """
        pass

    def is_empty(self, OdeSpace_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_empty(OdeSpace self)
        
        /**
         * Returns true if the ID is 0, meaning the OdeSpace does not point to a valid
         * space.  It is an error to call a method on an empty space.  Note that an
         * empty OdeSpace also evaluates to False.
         */
        """
        pass

    def is_enabled(self, const_OdeSpace_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_enabled(const OdeSpace self)
        """
        pass

    def is_space(self, const_OdeSpace_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_space(const OdeSpace self)
        """
        pass

    def query(self, OdeSpace_self, const_OdeGeom_geom): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        query(OdeSpace self, const OdeGeom geom)
        query(OdeSpace self, const OdeSpace space)
        """
        pass

    def remove(self, const_OdeSpace_self, OdeSpace_space): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        remove(const OdeSpace self, OdeSpace space)
        remove(const OdeSpace self, OdeGeom geom)
        """
        pass

    def setAutoCollideJointGroup(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_auto_collide_joint_group(const OdeSpace self, OdeJointGroup param0)
        """
        pass

    def setAutoCollideWorld(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_auto_collide_world(const OdeSpace self, OdeWorld param0)
        """
        pass

    def setCategoryBits(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_category_bits(const OdeSpace self, const BitMask bits)
        """
        pass

    def setCleanup(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_cleanup(const OdeSpace self, int mode)
        """
        pass

    def setCollideBits(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_collide_bits(const OdeSpace self, const BitMask bits)
        """
        pass

    def setCollideId(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_collide_id(const OdeSpace self, OdeGeom geom, int collide_id)
        set_collide_id(const OdeSpace self, int collide_id, dxGeom id)
        """
        pass

    def setCollisionEvent(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_collision_event(const OdeSpace self, str event_name)
        """
        pass

    def setSurfaceType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_surface_type(const OdeSpace self, OdeGeom geom, int surface_type)
        set_surface_type(const OdeSpace self, int surface_type, dxGeom id)
        """
        pass

    def set_auto_collide_joint_group(self, const_OdeSpace_self, OdeJointGroup_param0): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_auto_collide_joint_group(const OdeSpace self, OdeJointGroup param0)
        """
        pass

    def set_auto_collide_world(self, const_OdeSpace_self, OdeWorld_param0): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_auto_collide_world(const OdeSpace self, OdeWorld param0)
        """
        pass

    def set_category_bits(self, const_OdeSpace_self, const_BitMask_bits): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_category_bits(const OdeSpace self, const BitMask bits)
        """
        pass

    def set_cleanup(self, const_OdeSpace_self, int_mode): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_cleanup(const OdeSpace self, int mode)
        """
        pass

    def set_collide_bits(self, const_OdeSpace_self, const_BitMask_bits): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_collide_bits(const OdeSpace self, const BitMask bits)
        """
        pass

    def set_collide_id(self, const_OdeSpace_self, OdeGeom_geom, int_collide_id): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_collide_id(const OdeSpace self, OdeGeom geom, int collide_id)
        set_collide_id(const OdeSpace self, int collide_id, dxGeom id)
        """
        pass

    def set_collision_event(self, const_OdeSpace_self, str_event_name): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_collision_event(const OdeSpace self, str event_name)
        """
        pass

    def set_surface_type(self, const_OdeSpace_self, OdeGeom_geom, int_surface_type): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_surface_type(const OdeSpace self, OdeGeom geom, int surface_type)
        set_surface_type(const OdeSpace self, int surface_type, dxGeom id)
        """
        pass

    def write(self, OdeSpace_self, ostream_out, int_indent): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        write(OdeSpace self, ostream out, int indent)
        """
        pass

    def __bool__(self, *args, **kwargs): # real signature unknown
        """ True if self else False """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__bool__': None, # (!) real value is "<slot wrapper '__bool__' of 'panda3d.ode.OdeSpace' objects>"
        '__doc__': '/**\n *\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.ode.OdeSpace' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFDC9DEBAD0>'
        '__str__': None, # (!) real value is "<slot wrapper '__str__' of 'panda3d.ode.OdeSpace' objects>"
        'add': None, # (!) real value is "<method 'add' of 'panda3d.ode.OdeSpace' objects>"
        'autoCollide': None, # (!) real value is "<method 'autoCollide' of 'panda3d.ode.OdeSpace' objects>"
        'auto_collide': None, # (!) real value is "<method 'auto_collide' of 'panda3d.ode.OdeSpace' objects>"
        'clean': None, # (!) real value is "<method 'clean' of 'panda3d.ode.OdeSpace' objects>"
        'collide': None, # (!) real value is "<method 'collide' of 'panda3d.ode.OdeSpace' objects>"
        'convert': None, # (!) real value is "<method 'convert' of 'panda3d.ode.OdeSpace' objects>"
        'convertToHashSpace': None, # (!) real value is "<method 'convertToHashSpace' of 'panda3d.ode.OdeSpace' objects>"
        'convertToQuadTreeSpace': None, # (!) real value is "<method 'convertToQuadTreeSpace' of 'panda3d.ode.OdeSpace' objects>"
        'convertToSimpleSpace': None, # (!) real value is "<method 'convertToSimpleSpace' of 'panda3d.ode.OdeSpace' objects>"
        'convert_to_hash_space': None, # (!) real value is "<method 'convert_to_hash_space' of 'panda3d.ode.OdeSpace' objects>"
        'convert_to_quad_tree_space': None, # (!) real value is "<method 'convert_to_quad_tree_space' of 'panda3d.ode.OdeSpace' objects>"
        'convert_to_simple_space': None, # (!) real value is "<method 'convert_to_simple_space' of 'panda3d.ode.OdeSpace' objects>"
        'destroy': None, # (!) real value is "<method 'destroy' of 'panda3d.ode.OdeSpace' objects>"
        'disable': None, # (!) real value is "<method 'disable' of 'panda3d.ode.OdeSpace' objects>"
        'enable': None, # (!) real value is "<method 'enable' of 'panda3d.ode.OdeSpace' objects>"
        'getAABB': None, # (!) real value is "<method 'getAABB' of 'panda3d.ode.OdeSpace' objects>"
        'getAABounds': None, # (!) real value is "<method 'getAABounds' of 'panda3d.ode.OdeSpace' objects>"
        'getCategoryBits': None, # (!) real value is "<method 'getCategoryBits' of 'panda3d.ode.OdeSpace' objects>"
        'getClass': None, # (!) real value is "<method 'getClass' of 'panda3d.ode.OdeSpace' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFDC9DEBAD0>)>'
        'getCleanup': None, # (!) real value is "<method 'getCleanup' of 'panda3d.ode.OdeSpace' objects>"
        'getCollideBits': None, # (!) real value is "<method 'getCollideBits' of 'panda3d.ode.OdeSpace' objects>"
        'getCollideId': None, # (!) real value is "<method 'getCollideId' of 'panda3d.ode.OdeSpace' objects>"
        'getCollisionEvent': None, # (!) real value is "<method 'getCollisionEvent' of 'panda3d.ode.OdeSpace' objects>"
        'getConvertedGeom': None, # (!) real value is "<method 'getConvertedGeom' of 'panda3d.ode.OdeSpace' objects>"
        'getConvertedSpace': None, # (!) real value is "<method 'getConvertedSpace' of 'panda3d.ode.OdeSpace' objects>"
        'getGeom': None, # (!) real value is "<method 'getGeom' of 'panda3d.ode.OdeSpace' objects>"
        'getNumGeoms': None, # (!) real value is "<method 'getNumGeoms' of 'panda3d.ode.OdeSpace' objects>"
        'getSpace': None, # (!) real value is "<method 'getSpace' of 'panda3d.ode.OdeSpace' objects>"
        'getSurfaceType': None, # (!) real value is "<method 'getSurfaceType' of 'panda3d.ode.OdeSpace' objects>"
        'get_AABB': None, # (!) real value is "<method 'get_AABB' of 'panda3d.ode.OdeSpace' objects>"
        'get_AA_bounds': None, # (!) real value is "<method 'get_AA_bounds' of 'panda3d.ode.OdeSpace' objects>"
        'get_category_bits': None, # (!) real value is "<method 'get_category_bits' of 'panda3d.ode.OdeSpace' objects>"
        'get_class': None, # (!) real value is "<method 'get_class' of 'panda3d.ode.OdeSpace' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFDC9DEBAD0>)>'
        'get_cleanup': None, # (!) real value is "<method 'get_cleanup' of 'panda3d.ode.OdeSpace' objects>"
        'get_collide_bits': None, # (!) real value is "<method 'get_collide_bits' of 'panda3d.ode.OdeSpace' objects>"
        'get_collide_id': None, # (!) real value is "<method 'get_collide_id' of 'panda3d.ode.OdeSpace' objects>"
        'get_collision_event': None, # (!) real value is "<method 'get_collision_event' of 'panda3d.ode.OdeSpace' objects>"
        'get_converted_geom': None, # (!) real value is "<method 'get_converted_geom' of 'panda3d.ode.OdeSpace' objects>"
        'get_converted_space': None, # (!) real value is "<method 'get_converted_space' of 'panda3d.ode.OdeSpace' objects>"
        'get_geom': None, # (!) real value is "<method 'get_geom' of 'panda3d.ode.OdeSpace' objects>"
        'get_num_geoms': None, # (!) real value is "<method 'get_num_geoms' of 'panda3d.ode.OdeSpace' objects>"
        'get_space': None, # (!) real value is "<method 'get_space' of 'panda3d.ode.OdeSpace' objects>"
        'get_surface_type': None, # (!) real value is "<method 'get_surface_type' of 'panda3d.ode.OdeSpace' objects>"
        'isEmpty': None, # (!) real value is "<method 'isEmpty' of 'panda3d.ode.OdeSpace' objects>"
        'isEnabled': None, # (!) real value is "<method 'isEnabled' of 'panda3d.ode.OdeSpace' objects>"
        'isSpace': None, # (!) real value is "<method 'isSpace' of 'panda3d.ode.OdeSpace' objects>"
        'is_empty': None, # (!) real value is "<method 'is_empty' of 'panda3d.ode.OdeSpace' objects>"
        'is_enabled': None, # (!) real value is "<method 'is_enabled' of 'panda3d.ode.OdeSpace' objects>"
        'is_space': None, # (!) real value is "<method 'is_space' of 'panda3d.ode.OdeSpace' objects>"
        'query': None, # (!) real value is "<method 'query' of 'panda3d.ode.OdeSpace' objects>"
        'remove': None, # (!) real value is "<method 'remove' of 'panda3d.ode.OdeSpace' objects>"
        'setAutoCollideJointGroup': None, # (!) real value is "<method 'setAutoCollideJointGroup' of 'panda3d.ode.OdeSpace' objects>"
        'setAutoCollideWorld': None, # (!) real value is "<method 'setAutoCollideWorld' of 'panda3d.ode.OdeSpace' objects>"
        'setCategoryBits': None, # (!) real value is "<method 'setCategoryBits' of 'panda3d.ode.OdeSpace' objects>"
        'setCleanup': None, # (!) real value is "<method 'setCleanup' of 'panda3d.ode.OdeSpace' objects>"
        'setCollideBits': None, # (!) real value is "<method 'setCollideBits' of 'panda3d.ode.OdeSpace' objects>"
        'setCollideId': None, # (!) real value is "<method 'setCollideId' of 'panda3d.ode.OdeSpace' objects>"
        'setCollisionEvent': None, # (!) real value is "<method 'setCollisionEvent' of 'panda3d.ode.OdeSpace' objects>"
        'setSurfaceType': None, # (!) real value is "<method 'setSurfaceType' of 'panda3d.ode.OdeSpace' objects>"
        'set_auto_collide_joint_group': None, # (!) real value is "<method 'set_auto_collide_joint_group' of 'panda3d.ode.OdeSpace' objects>"
        'set_auto_collide_world': None, # (!) real value is "<method 'set_auto_collide_world' of 'panda3d.ode.OdeSpace' objects>"
        'set_category_bits': None, # (!) real value is "<method 'set_category_bits' of 'panda3d.ode.OdeSpace' objects>"
        'set_cleanup': None, # (!) real value is "<method 'set_cleanup' of 'panda3d.ode.OdeSpace' objects>"
        'set_collide_bits': None, # (!) real value is "<method 'set_collide_bits' of 'panda3d.ode.OdeSpace' objects>"
        'set_collide_id': None, # (!) real value is "<method 'set_collide_id' of 'panda3d.ode.OdeSpace' objects>"
        'set_collision_event': None, # (!) real value is "<method 'set_collision_event' of 'panda3d.ode.OdeSpace' objects>"
        'set_surface_type': None, # (!) real value is "<method 'set_surface_type' of 'panda3d.ode.OdeSpace' objects>"
        'write': None, # (!) real value is "<method 'write' of 'panda3d.ode.OdeSpace' objects>"
    }


