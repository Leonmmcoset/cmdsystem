# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .RenderAttrib import RenderAttrib

class ClipPlaneAttrib(RenderAttrib):
    """
    /**
     * This functions similarly to a LightAttrib.  It indicates the set of
     * clipping planes that modify the geometry at this level and below.  A
     * ClipPlaneAttrib can either add planes or remove planes from the total set
     * of clipping planes in effect.
     */
    """
    def addOffPlane(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_off_plane(ClipPlaneAttrib self, const NodePath plane)
        
        /**
         * Returns a new ClipPlaneAttrib, just like this one, but with the indicated
         * plane added to the list of planes disabled by this attrib.
         */
        """
        pass

    def addOnPlane(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_on_plane(ClipPlaneAttrib self, const NodePath plane)
        
        /**
         * Returns a new ClipPlaneAttrib, just like this one, but with the indicated
         * plane added to the list of planes enabled by this attrib.
         */
        """
        pass

    def addPlane(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_plane(ClipPlaneAttrib self, PlaneNode plane)
        
        /**
         * Returns a new ClipPlaneAttrib, just like this one, but with the indicated
         * plane added to the list of planes.
         *
         * @deprecated Use add_on_plane() or add_off_plane() instead.
         */
        """
        pass

    def add_off_plane(self, ClipPlaneAttrib_self, const_NodePath_plane): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_off_plane(ClipPlaneAttrib self, const NodePath plane)
        
        /**
         * Returns a new ClipPlaneAttrib, just like this one, but with the indicated
         * plane added to the list of planes disabled by this attrib.
         */
        """
        pass

    def add_on_plane(self, ClipPlaneAttrib_self, const_NodePath_plane): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_on_plane(ClipPlaneAttrib self, const NodePath plane)
        
        /**
         * Returns a new ClipPlaneAttrib, just like this one, but with the indicated
         * plane added to the list of planes enabled by this attrib.
         */
        """
        pass

    def add_plane(self, ClipPlaneAttrib_self, PlaneNode_plane): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_plane(ClipPlaneAttrib self, PlaneNode plane)
        
        /**
         * Returns a new ClipPlaneAttrib, just like this one, but with the indicated
         * plane added to the list of planes.
         *
         * @deprecated Use add_on_plane() or add_off_plane() instead.
         */
        """
        pass

    def filterToMax(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        filter_to_max(ClipPlaneAttrib self, int max_clip_planes)
        
        /**
         * Returns a new ClipPlaneAttrib, very much like this one, but with the number
         * of on_planes reduced to be no more than max_clip_planes.  The number of
         * off_planes in the new ClipPlaneAttrib is undefined.
         */
        """
        pass

    def filter_to_max(self, ClipPlaneAttrib_self, int_max_clip_planes): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        filter_to_max(ClipPlaneAttrib self, int max_clip_planes)
        
        /**
         * Returns a new ClipPlaneAttrib, very much like this one, but with the number
         * of on_planes reduced to be no more than max_clip_planes.  The number of
         * off_planes in the new ClipPlaneAttrib is undefined.
         */
        """
        pass

    def getClassSlot(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_slot()
        """
        pass

    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getNumOffPlanes(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_off_planes(ClipPlaneAttrib self)
        
        /**
         * Returns the number of planes that are disabled by the attribute.
         */
        """
        pass

    def getNumOnPlanes(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_on_planes(ClipPlaneAttrib self)
        
        /**
         * Returns the number of planes that are enabled by the attribute.
         */
        """
        pass

    def getNumPlanes(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_planes(ClipPlaneAttrib self)
        
        /**
         * Returns the number of planes listed in the attribute.
         *
         * @deprecated ClipPlaneAttribs nowadays have a separate list of on_planes and
         * off_planes, so this method no longer makes sense.  Query the lists
         * independently.
         */
        """
        pass

    def getOffPlane(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_off_plane(ClipPlaneAttrib self, int n)
        
        /**
         * Returns the nth plane disabled by the attribute, sorted in arbitrary
         * (pointer) order.
         */
        """
        pass

    def getOffPlanes(self, *args, **kwargs): # real signature unknown
        pass

    def getOnPlane(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_on_plane(ClipPlaneAttrib self, int n)
        
        /**
         * Returns the nth plane enabled by the attribute, sorted in render order.
         */
        """
        pass

    def getOnPlanes(self, *args, **kwargs): # real signature unknown
        pass

    def getOperation(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_operation(ClipPlaneAttrib self)
        
        /**
         * Returns the basic operation type of the ClipPlaneAttrib.  If this is O_set,
         * the planes listed here completely replace any planes that were already on.
         * If this is O_add, the planes here are added to the set of planes that
         * were already on, and if O_remove, the planes here are removed from the set
         * of planes that were on.
         *
         * @deprecated ClipPlaneAttribs nowadays have a separate list of on_planes and
         * off_planes, so this method no longer makes sense.  Query the lists
         * independently.
         */
        """
        pass

    def getPlane(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_plane(ClipPlaneAttrib self, int n)
        
        /**
         * Returns the nth plane listed in the attribute.
         *
         * @deprecated ClipPlaneAttribs nowadays have a separate list of on_planes and
         * off_planes, so this method no longer makes sense.  Query the lists
         * independently.
         */
        """
        pass

    def get_class_slot(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_slot()
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_num_off_planes(self, ClipPlaneAttrib_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_off_planes(ClipPlaneAttrib self)
        
        /**
         * Returns the number of planes that are disabled by the attribute.
         */
        """
        pass

    def get_num_on_planes(self, ClipPlaneAttrib_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_on_planes(ClipPlaneAttrib self)
        
        /**
         * Returns the number of planes that are enabled by the attribute.
         */
        """
        pass

    def get_num_planes(self, ClipPlaneAttrib_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_planes(ClipPlaneAttrib self)
        
        /**
         * Returns the number of planes listed in the attribute.
         *
         * @deprecated ClipPlaneAttribs nowadays have a separate list of on_planes and
         * off_planes, so this method no longer makes sense.  Query the lists
         * independently.
         */
        """
        pass

    def get_off_plane(self, ClipPlaneAttrib_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_off_plane(ClipPlaneAttrib self, int n)
        
        /**
         * Returns the nth plane disabled by the attribute, sorted in arbitrary
         * (pointer) order.
         */
        """
        pass

    def get_off_planes(self, *args, **kwargs): # real signature unknown
        pass

    def get_on_plane(self, ClipPlaneAttrib_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_on_plane(ClipPlaneAttrib self, int n)
        
        /**
         * Returns the nth plane enabled by the attribute, sorted in render order.
         */
        """
        pass

    def get_on_planes(self, *args, **kwargs): # real signature unknown
        pass

    def get_operation(self, ClipPlaneAttrib_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_operation(ClipPlaneAttrib self)
        
        /**
         * Returns the basic operation type of the ClipPlaneAttrib.  If this is O_set,
         * the planes listed here completely replace any planes that were already on.
         * If this is O_add, the planes here are added to the set of planes that
         * were already on, and if O_remove, the planes here are removed from the set
         * of planes that were on.
         *
         * @deprecated ClipPlaneAttribs nowadays have a separate list of on_planes and
         * off_planes, so this method no longer makes sense.  Query the lists
         * independently.
         */
        """
        pass

    def get_plane(self, ClipPlaneAttrib_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_plane(ClipPlaneAttrib self, int n)
        
        /**
         * Returns the nth plane listed in the attribute.
         *
         * @deprecated ClipPlaneAttribs nowadays have a separate list of on_planes and
         * off_planes, so this method no longer makes sense.  Query the lists
         * independently.
         */
        """
        pass

    def hasAllOff(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_all_off(ClipPlaneAttrib self)
        
        /**
         * Returns true if this attrib disables all planes (although it may also
         * enable some).
         */
        """
        pass

    def hasOffPlane(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_off_plane(ClipPlaneAttrib self, const NodePath plane)
        
        /**
         * Returns true if the indicated plane is disabled by the attrib, false
         * otherwise.
         */
        """
        pass

    def hasOnPlane(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_on_plane(ClipPlaneAttrib self, const NodePath plane)
        
        /**
         * Returns true if the indicated plane is enabled by the attrib, false
         * otherwise.
         */
        """
        pass

    def hasPlane(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_plane(ClipPlaneAttrib self, PlaneNode plane)
        
        /**
         * Returns true if the indicated plane is listed in the attrib, false
         * otherwise.
         *
         * @deprecated ClipPlaneAttribs nowadays have a separate list of on_planes and
         * off_planes, so this method no longer makes sense.  Query the lists
         * independently.
         */
        """
        pass

    def has_all_off(self, ClipPlaneAttrib_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_all_off(ClipPlaneAttrib self)
        
        /**
         * Returns true if this attrib disables all planes (although it may also
         * enable some).
         */
        """
        pass

    def has_off_plane(self, ClipPlaneAttrib_self, const_NodePath_plane): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_off_plane(ClipPlaneAttrib self, const NodePath plane)
        
        /**
         * Returns true if the indicated plane is disabled by the attrib, false
         * otherwise.
         */
        """
        pass

    def has_on_plane(self, ClipPlaneAttrib_self, const_NodePath_plane): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_on_plane(ClipPlaneAttrib self, const NodePath plane)
        
        /**
         * Returns true if the indicated plane is enabled by the attrib, false
         * otherwise.
         */
        """
        pass

    def has_plane(self, ClipPlaneAttrib_self, PlaneNode_plane): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_plane(ClipPlaneAttrib self, PlaneNode plane)
        
        /**
         * Returns true if the indicated plane is listed in the attrib, false
         * otherwise.
         *
         * @deprecated ClipPlaneAttribs nowadays have a separate list of on_planes and
         * off_planes, so this method no longer makes sense.  Query the lists
         * independently.
         */
        """
        pass

    def isIdentity(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_identity(ClipPlaneAttrib self)
        
        /**
         * Returns true if this is an identity attrib: it does not change the set of
         * planes in use.
         */
        """
        pass

    def is_identity(self, ClipPlaneAttrib_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_identity(ClipPlaneAttrib self)
        
        /**
         * Returns true if this is an identity attrib: it does not change the set of
         * planes in use.
         */
        """
        pass

    def make(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        make()
        make(int op, PlaneNode plane)
        make(int op, PlaneNode plane1, PlaneNode plane2)
        make(int op, PlaneNode plane1, PlaneNode plane2, PlaneNode plane3)
        make(int op, PlaneNode plane1, PlaneNode plane2, PlaneNode plane3, PlaneNode plane4)
        
        // The following is the new, more general interface to the ClipPlaneAttrib.
        
        /**
         * Constructs a new ClipPlaneAttrib object that enables (or disables,
         * according to op) the indicated plane(s).
         *
         * @deprecated Use add_on_plane() or add_off_plane() instead.
         */
        
        /**
         * Constructs a new ClipPlaneAttrib object that turns on (or off, according to
         * op) the indicate plane(s).
         *
         * @deprecated Use add_on_plane() or add_off_plane() instead.
         */
        
        /**
         * Constructs a new ClipPlaneAttrib object that turns on (or off, according to
         * op) the indicate plane(s).
         *
         * @deprecated Use add_on_plane() or add_off_plane() instead.
         */
        
        /**
         * Constructs a new ClipPlaneAttrib object that turns on (or off, according to
         * op) the indicate plane(s).
         *
         * @deprecated Use add_on_plane() or add_off_plane() instead.
         */
        
        /**
         * Constructs a new ClipPlaneAttrib object that does nothing.
         */
        """
        pass

    def makeAllOff(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        make_all_off()
        
        /**
         * Constructs a new ClipPlaneAttrib object that disables all planes (and hence
         * disables clipping).
         */
        """
        pass

    def makeDefault(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        make_default()
        
        /**
         * Returns a RenderAttrib that corresponds to whatever the standard default
         * properties for render attributes of this type ought to be.
         */
        """
        pass

    def make_all_off(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        make_all_off()
        
        /**
         * Constructs a new ClipPlaneAttrib object that disables all planes (and hence
         * disables clipping).
         */
        """
        pass

    def make_default(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        make_default()
        
        /**
         * Returns a RenderAttrib that corresponds to whatever the standard default
         * properties for render attributes of this type ought to be.
         */
        """
        pass

    def removeOffPlane(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        remove_off_plane(ClipPlaneAttrib self, const NodePath plane)
        
        /**
         * Returns a new ClipPlaneAttrib, just like this one, but with the indicated
         * plane removed from the list of planes disabled by this attrib.
         */
        """
        pass

    def removeOnPlane(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        remove_on_plane(ClipPlaneAttrib self, const NodePath plane)
        
        /**
         * Returns a new ClipPlaneAttrib, just like this one, but with the indicated
         * plane removed from the list of planes enabled by this attrib.
         */
        """
        pass

    def removePlane(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        remove_plane(ClipPlaneAttrib self, PlaneNode plane)
        
        /**
         * Returns a new ClipPlaneAttrib, just like this one, but with the indicated
         * plane removed from the list of planes.
         *
         * @deprecated Use remove_on_plane() or remove_off_plane() instead.
         */
        """
        pass

    def remove_off_plane(self, ClipPlaneAttrib_self, const_NodePath_plane): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        remove_off_plane(ClipPlaneAttrib self, const NodePath plane)
        
        /**
         * Returns a new ClipPlaneAttrib, just like this one, but with the indicated
         * plane removed from the list of planes disabled by this attrib.
         */
        """
        pass

    def remove_on_plane(self, ClipPlaneAttrib_self, const_NodePath_plane): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        remove_on_plane(ClipPlaneAttrib self, const NodePath plane)
        
        /**
         * Returns a new ClipPlaneAttrib, just like this one, but with the indicated
         * plane removed from the list of planes enabled by this attrib.
         */
        """
        pass

    def remove_plane(self, ClipPlaneAttrib_self, PlaneNode_plane): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        remove_plane(ClipPlaneAttrib self, PlaneNode plane)
        
        /**
         * Returns a new ClipPlaneAttrib, just like this one, but with the indicated
         * plane removed from the list of planes.
         *
         * @deprecated Use remove_on_plane() or remove_off_plane() instead.
         */
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    class_slot = 5
    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        'OAdd': 1,
        'ORemove': 2,
        'OSet': 0,
        'O_add': 1,
        'O_remove': 2,
        'O_set': 0,
        '__doc__': '/**\n * This functions similarly to a LightAttrib.  It indicates the set of\n * clipping planes that modify the geometry at this level and below.  A\n * ClipPlaneAttrib can either add planes or remove planes from the total set\n * of clipping planes in effect.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.ClipPlaneAttrib' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE295030>'
        'addOffPlane': None, # (!) real value is "<method 'addOffPlane' of 'panda3d.core.ClipPlaneAttrib' objects>"
        'addOnPlane': None, # (!) real value is "<method 'addOnPlane' of 'panda3d.core.ClipPlaneAttrib' objects>"
        'addPlane': None, # (!) real value is "<method 'addPlane' of 'panda3d.core.ClipPlaneAttrib' objects>"
        'add_off_plane': None, # (!) real value is "<method 'add_off_plane' of 'panda3d.core.ClipPlaneAttrib' objects>"
        'add_on_plane': None, # (!) real value is "<method 'add_on_plane' of 'panda3d.core.ClipPlaneAttrib' objects>"
        'add_plane': None, # (!) real value is "<method 'add_plane' of 'panda3d.core.ClipPlaneAttrib' objects>"
        'class_slot': None, # (!) real value is "<attribute 'class_slot' of 'panda3d.core.ClipPlaneAttrib'>"
        'filterToMax': None, # (!) real value is "<method 'filterToMax' of 'panda3d.core.ClipPlaneAttrib' objects>"
        'filter_to_max': None, # (!) real value is "<method 'filter_to_max' of 'panda3d.core.ClipPlaneAttrib' objects>"
        'getClassSlot': None, # (!) real value is '<staticmethod(<built-in method getClassSlot of type object at 0x00007FFCFE295030>)>'
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE295030>)>'
        'getNumOffPlanes': None, # (!) real value is "<method 'getNumOffPlanes' of 'panda3d.core.ClipPlaneAttrib' objects>"
        'getNumOnPlanes': None, # (!) real value is "<method 'getNumOnPlanes' of 'panda3d.core.ClipPlaneAttrib' objects>"
        'getNumPlanes': None, # (!) real value is "<method 'getNumPlanes' of 'panda3d.core.ClipPlaneAttrib' objects>"
        'getOffPlane': None, # (!) real value is "<method 'getOffPlane' of 'panda3d.core.ClipPlaneAttrib' objects>"
        'getOffPlanes': None, # (!) real value is "<method 'getOffPlanes' of 'panda3d.core.ClipPlaneAttrib' objects>"
        'getOnPlane': None, # (!) real value is "<method 'getOnPlane' of 'panda3d.core.ClipPlaneAttrib' objects>"
        'getOnPlanes': None, # (!) real value is "<method 'getOnPlanes' of 'panda3d.core.ClipPlaneAttrib' objects>"
        'getOperation': None, # (!) real value is "<method 'getOperation' of 'panda3d.core.ClipPlaneAttrib' objects>"
        'getPlane': None, # (!) real value is "<method 'getPlane' of 'panda3d.core.ClipPlaneAttrib' objects>"
        'get_class_slot': None, # (!) real value is '<staticmethod(<built-in method get_class_slot of type object at 0x00007FFCFE295030>)>'
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE295030>)>'
        'get_num_off_planes': None, # (!) real value is "<method 'get_num_off_planes' of 'panda3d.core.ClipPlaneAttrib' objects>"
        'get_num_on_planes': None, # (!) real value is "<method 'get_num_on_planes' of 'panda3d.core.ClipPlaneAttrib' objects>"
        'get_num_planes': None, # (!) real value is "<method 'get_num_planes' of 'panda3d.core.ClipPlaneAttrib' objects>"
        'get_off_plane': None, # (!) real value is "<method 'get_off_plane' of 'panda3d.core.ClipPlaneAttrib' objects>"
        'get_off_planes': None, # (!) real value is "<method 'get_off_planes' of 'panda3d.core.ClipPlaneAttrib' objects>"
        'get_on_plane': None, # (!) real value is "<method 'get_on_plane' of 'panda3d.core.ClipPlaneAttrib' objects>"
        'get_on_planes': None, # (!) real value is "<method 'get_on_planes' of 'panda3d.core.ClipPlaneAttrib' objects>"
        'get_operation': None, # (!) real value is "<method 'get_operation' of 'panda3d.core.ClipPlaneAttrib' objects>"
        'get_plane': None, # (!) real value is "<method 'get_plane' of 'panda3d.core.ClipPlaneAttrib' objects>"
        'hasAllOff': None, # (!) real value is "<method 'hasAllOff' of 'panda3d.core.ClipPlaneAttrib' objects>"
        'hasOffPlane': None, # (!) real value is "<method 'hasOffPlane' of 'panda3d.core.ClipPlaneAttrib' objects>"
        'hasOnPlane': None, # (!) real value is "<method 'hasOnPlane' of 'panda3d.core.ClipPlaneAttrib' objects>"
        'hasPlane': None, # (!) real value is "<method 'hasPlane' of 'panda3d.core.ClipPlaneAttrib' objects>"
        'has_all_off': None, # (!) real value is "<method 'has_all_off' of 'panda3d.core.ClipPlaneAttrib' objects>"
        'has_off_plane': None, # (!) real value is "<method 'has_off_plane' of 'panda3d.core.ClipPlaneAttrib' objects>"
        'has_on_plane': None, # (!) real value is "<method 'has_on_plane' of 'panda3d.core.ClipPlaneAttrib' objects>"
        'has_plane': None, # (!) real value is "<method 'has_plane' of 'panda3d.core.ClipPlaneAttrib' objects>"
        'isIdentity': None, # (!) real value is "<method 'isIdentity' of 'panda3d.core.ClipPlaneAttrib' objects>"
        'is_identity': None, # (!) real value is "<method 'is_identity' of 'panda3d.core.ClipPlaneAttrib' objects>"
        'make': None, # (!) real value is '<staticmethod(<built-in method make of type object at 0x00007FFCFE295030>)>'
        'makeAllOff': None, # (!) real value is '<staticmethod(<built-in method makeAllOff of type object at 0x00007FFCFE295030>)>'
        'makeDefault': None, # (!) real value is '<staticmethod(<built-in method makeDefault of type object at 0x00007FFCFE295030>)>'
        'make_all_off': None, # (!) real value is '<staticmethod(<built-in method make_all_off of type object at 0x00007FFCFE295030>)>'
        'make_default': None, # (!) real value is '<staticmethod(<built-in method make_default of type object at 0x00007FFCFE295030>)>'
        'removeOffPlane': None, # (!) real value is "<method 'removeOffPlane' of 'panda3d.core.ClipPlaneAttrib' objects>"
        'removeOnPlane': None, # (!) real value is "<method 'removeOnPlane' of 'panda3d.core.ClipPlaneAttrib' objects>"
        'removePlane': None, # (!) real value is "<method 'removePlane' of 'panda3d.core.ClipPlaneAttrib' objects>"
        'remove_off_plane': None, # (!) real value is "<method 'remove_off_plane' of 'panda3d.core.ClipPlaneAttrib' objects>"
        'remove_on_plane': None, # (!) real value is "<method 'remove_on_plane' of 'panda3d.core.ClipPlaneAttrib' objects>"
        'remove_plane': None, # (!) real value is "<method 'remove_plane' of 'panda3d.core.ClipPlaneAttrib' objects>"
    }
    OAdd = 1
    ORemove = 2
    OSet = 0
    O_add = 1
    O_remove = 2
    O_set = 0


