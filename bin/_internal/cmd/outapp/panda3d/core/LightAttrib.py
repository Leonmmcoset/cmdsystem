# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .RenderAttrib import RenderAttrib

class LightAttrib(RenderAttrib):
    """
    /**
     * Indicates which set of lights should be considered "on" to illuminate
     * geometry at this level and below.  A LightAttrib can either add lights or
     * remove lights from the total set of "on" lights.
     */
    """
    def addLight(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_light(LightAttrib self, Light light)
        
        /**
         * Returns a new LightAttrib, just like this one, but with the indicated light
         * added to the list of lights.
         *
         * @deprecated Use add_on_light() or add_off_light() instead.
         */
        """
        pass

    def addOffLight(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_off_light(LightAttrib self, const NodePath light)
        
        /**
         * Returns a new LightAttrib, just like this one, but with the indicated light
         * added to the list of lights turned off by this attrib.
         */
        """
        pass

    def addOnLight(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_on_light(LightAttrib self, const NodePath light)
        
        /**
         * Returns a new LightAttrib, just like this one, but with the indicated light
         * added to the list of lights turned on by this attrib.
         */
        """
        pass

    def add_light(self, LightAttrib_self, Light_light): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_light(LightAttrib self, Light light)
        
        /**
         * Returns a new LightAttrib, just like this one, but with the indicated light
         * added to the list of lights.
         *
         * @deprecated Use add_on_light() or add_off_light() instead.
         */
        """
        pass

    def add_off_light(self, LightAttrib_self, const_NodePath_light): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_off_light(LightAttrib self, const NodePath light)
        
        /**
         * Returns a new LightAttrib, just like this one, but with the indicated light
         * added to the list of lights turned off by this attrib.
         */
        """
        pass

    def add_on_light(self, LightAttrib_self, const_NodePath_light): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_on_light(LightAttrib self, const NodePath light)
        
        /**
         * Returns a new LightAttrib, just like this one, but with the indicated light
         * added to the list of lights turned on by this attrib.
         */
        """
        pass

    def getAmbientContribution(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_ambient_contribution(LightAttrib self)
        
        /**
         * Returns the total contribution of all the ambient lights.
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

    def getLight(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_light(LightAttrib self, int n)
        
        /**
         * Returns the nth light listed in the attribute.
         *
         * @deprecated LightAttribs nowadays have a separate list of on_lights and
         * off_lights, so this method no longer makes sense.  Query the lists
         * independently.
         */
        """
        pass

    def getMostImportantLight(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_most_important_light(LightAttrib self)
        
        /**
         * Returns the most important light (that is, the light with the highest
         * priority) in the LightAttrib, excluding any ambient lights.  Returns an
         * empty NodePath if no non-ambient lights are found.
         */
        """
        pass

    def getNumLights(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_lights(LightAttrib self)
        
        /**
         * Returns the number of lights listed in the attribute.
         *
         * @deprecated LightAttribs nowadays have a separate list of on_lights and
         * off_lights, so this method no longer makes sense.  Query the lists
         * independently.
         */
        """
        pass

    def getNumNonAmbientLights(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_non_ambient_lights(LightAttrib self)
        
        /**
         * Returns the number of non-ambient lights that are turned on by this
         * attribute.
         */
        """
        pass

    def getNumOffLights(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_off_lights(LightAttrib self)
        
        /**
         * Returns the number of lights that are turned off by the attribute.
         */
        """
        pass

    def getNumOnLights(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_on_lights(LightAttrib self)
        
        /**
         * Returns the number of lights that are turned on by the attribute.
         */
        """
        pass

    def getOffLight(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_off_light(LightAttrib self, int n)
        
        /**
         * Returns the nth light turned off by the attribute, sorted in arbitrary
         * (pointer) order.
         */
        """
        pass

    def getOffLights(self, *args, **kwargs): # real signature unknown
        pass

    def getOnLight(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_on_light(LightAttrib self, int n)
        
        /**
         * Returns the nth light turned on by the attribute, sorted in render order.
         */
        """
        pass

    def getOnLights(self, *args, **kwargs): # real signature unknown
        pass

    def getOperation(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_operation(LightAttrib self)
        
        /**
         * Returns the basic operation type of the LightAttrib.  If this is O_set, the
         * lights listed here completely replace any lights that were already on.  If
         * this is O_add, the lights here are added to the set of lights that were
         * already on, and if O_remove, the lights here are removed from the set of
         * lights that were on.
         *
         * @deprecated LightAttribs nowadays have a separate list of on_lights and
         * off_lights, so this method no longer makes sense.  Query the lists
         * independently.
         */
        """
        pass

    def get_ambient_contribution(self, LightAttrib_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_ambient_contribution(LightAttrib self)
        
        /**
         * Returns the total contribution of all the ambient lights.
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

    def get_light(self, LightAttrib_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_light(LightAttrib self, int n)
        
        /**
         * Returns the nth light listed in the attribute.
         *
         * @deprecated LightAttribs nowadays have a separate list of on_lights and
         * off_lights, so this method no longer makes sense.  Query the lists
         * independently.
         */
        """
        pass

    def get_most_important_light(self, LightAttrib_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_most_important_light(LightAttrib self)
        
        /**
         * Returns the most important light (that is, the light with the highest
         * priority) in the LightAttrib, excluding any ambient lights.  Returns an
         * empty NodePath if no non-ambient lights are found.
         */
        """
        pass

    def get_num_lights(self, LightAttrib_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_lights(LightAttrib self)
        
        /**
         * Returns the number of lights listed in the attribute.
         *
         * @deprecated LightAttribs nowadays have a separate list of on_lights and
         * off_lights, so this method no longer makes sense.  Query the lists
         * independently.
         */
        """
        pass

    def get_num_non_ambient_lights(self, LightAttrib_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_non_ambient_lights(LightAttrib self)
        
        /**
         * Returns the number of non-ambient lights that are turned on by this
         * attribute.
         */
        """
        pass

    def get_num_off_lights(self, LightAttrib_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_off_lights(LightAttrib self)
        
        /**
         * Returns the number of lights that are turned off by the attribute.
         */
        """
        pass

    def get_num_on_lights(self, LightAttrib_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_on_lights(LightAttrib self)
        
        /**
         * Returns the number of lights that are turned on by the attribute.
         */
        """
        pass

    def get_off_light(self, LightAttrib_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_off_light(LightAttrib self, int n)
        
        /**
         * Returns the nth light turned off by the attribute, sorted in arbitrary
         * (pointer) order.
         */
        """
        pass

    def get_off_lights(self, *args, **kwargs): # real signature unknown
        pass

    def get_on_light(self, LightAttrib_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_on_light(LightAttrib self, int n)
        
        /**
         * Returns the nth light turned on by the attribute, sorted in render order.
         */
        """
        pass

    def get_on_lights(self, *args, **kwargs): # real signature unknown
        pass

    def get_operation(self, LightAttrib_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_operation(LightAttrib self)
        
        /**
         * Returns the basic operation type of the LightAttrib.  If this is O_set, the
         * lights listed here completely replace any lights that were already on.  If
         * this is O_add, the lights here are added to the set of lights that were
         * already on, and if O_remove, the lights here are removed from the set of
         * lights that were on.
         *
         * @deprecated LightAttribs nowadays have a separate list of on_lights and
         * off_lights, so this method no longer makes sense.  Query the lists
         * independently.
         */
        """
        pass

    def hasAllOff(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_all_off(LightAttrib self)
        
        /**
         * Returns true if this attrib turns off all lights (although it may also turn
         * some on).
         */
        """
        pass

    def hasAnyOnLight(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_any_on_light(LightAttrib self)
        
        /**
         * Returns true if any light is turned on by the attrib, false otherwise.
         */
        """
        pass

    def hasLight(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_light(LightAttrib self, Light light)
        
        /**
         * Returns true if the indicated light is listed in the attrib, false
         * otherwise.
         *
         * @deprecated LightAttribs nowadays have a separate list of on_lights and
         * off_lights, so this method no longer makes sense.  Query the lists
         * independently.
         */
        """
        pass

    def hasOffLight(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_off_light(LightAttrib self, const NodePath light)
        
        /**
         * Returns true if the indicated light is turned off by the attrib, false
         * otherwise.
         */
        """
        pass

    def hasOnLight(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_on_light(LightAttrib self, const NodePath light)
        
        /**
         * Returns true if the indicated light is turned on by the attrib, false
         * otherwise.
         */
        """
        pass

    def has_all_off(self, LightAttrib_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_all_off(LightAttrib self)
        
        /**
         * Returns true if this attrib turns off all lights (although it may also turn
         * some on).
         */
        """
        pass

    def has_any_on_light(self, LightAttrib_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_any_on_light(LightAttrib self)
        
        /**
         * Returns true if any light is turned on by the attrib, false otherwise.
         */
        """
        pass

    def has_light(self, LightAttrib_self, Light_light): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_light(LightAttrib self, Light light)
        
        /**
         * Returns true if the indicated light is listed in the attrib, false
         * otherwise.
         *
         * @deprecated LightAttribs nowadays have a separate list of on_lights and
         * off_lights, so this method no longer makes sense.  Query the lists
         * independently.
         */
        """
        pass

    def has_off_light(self, LightAttrib_self, const_NodePath_light): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_off_light(LightAttrib self, const NodePath light)
        
        /**
         * Returns true if the indicated light is turned off by the attrib, false
         * otherwise.
         */
        """
        pass

    def has_on_light(self, LightAttrib_self, const_NodePath_light): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_on_light(LightAttrib self, const NodePath light)
        
        /**
         * Returns true if the indicated light is turned on by the attrib, false
         * otherwise.
         */
        """
        pass

    def isIdentity(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_identity(LightAttrib self)
        
        /**
         * Returns true if this is an identity attrib: it does not change the set of
         * lights in use.
         */
        """
        pass

    def is_identity(self, LightAttrib_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_identity(LightAttrib self)
        
        /**
         * Returns true if this is an identity attrib: it does not change the set of
         * lights in use.
         */
        """
        pass

    def make(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        make()
        make(int op, Light light)
        make(int op, Light light1, Light light2)
        make(int op, Light light1, Light light2, Light light3)
        make(int op, Light light1, Light light2, Light light3, Light light4)
        
        // The following is the new, more general interface to the LightAttrib.
        
        /**
         * Constructs a new LightAttrib object that turns on (or off, according to op)
         * the indicated light(s).
         *
         * @deprecated Use add_on_light() or add_off_light() instead.
         */
        
        /**
         * Constructs a new LightAttrib object that turns on (or off, according to op)
         * the indicate light(s).
         *
         * @deprecated Use add_on_light() or add_off_light() instead.
         */
        
        /**
         * Constructs a new LightAttrib object that turns on (or off, according to op)
         * the indicate light(s).
         *
         * @deprecated Use add_on_light() or add_off_light() instead.
         */
        
        /**
         * Constructs a new LightAttrib object that turns on (or off, according to op)
         * the indicate light(s).
         *
         * @deprecated Use add_on_light() or add_off_light() instead.
         */
        
        /**
         * Constructs a new LightAttrib object that does nothing.
         */
        """
        pass

    def makeAllOff(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        make_all_off()
        
        /**
         * Constructs a new LightAttrib object that turns off all lights (and hence
         * disables lighting).
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
         * Constructs a new LightAttrib object that turns off all lights (and hence
         * disables lighting).
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

    def removeLight(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        remove_light(LightAttrib self, Light light)
        
        /**
         * Returns a new LightAttrib, just like this one, but with the indicated light
         * removed from the list of lights.
         *
         * @deprecated Use remove_on_light() or remove_off_light() instead.
         */
        """
        pass

    def removeOffLight(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        remove_off_light(LightAttrib self, const NodePath light)
        
        /**
         * Returns a new LightAttrib, just like this one, but with the indicated light
         * removed from the list of lights turned off by this attrib.
         */
        """
        pass

    def removeOnLight(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        remove_on_light(LightAttrib self, const NodePath light)
        
        /**
         * Returns a new LightAttrib, just like this one, but with the indicated light
         * removed from the list of lights turned on by this attrib.
         */
        """
        pass

    def remove_light(self, LightAttrib_self, Light_light): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        remove_light(LightAttrib self, Light light)
        
        /**
         * Returns a new LightAttrib, just like this one, but with the indicated light
         * removed from the list of lights.
         *
         * @deprecated Use remove_on_light() or remove_off_light() instead.
         */
        """
        pass

    def remove_off_light(self, LightAttrib_self, const_NodePath_light): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        remove_off_light(LightAttrib self, const NodePath light)
        
        /**
         * Returns a new LightAttrib, just like this one, but with the indicated light
         * removed from the list of lights turned off by this attrib.
         */
        """
        pass

    def remove_on_light(self, LightAttrib_self, const_NodePath_light): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        remove_on_light(LightAttrib self, const NodePath light)
        
        /**
         * Returns a new LightAttrib, just like this one, but with the indicated light
         * removed from the list of lights turned on by this attrib.
         */
        """
        pass

    def replaceOffLight(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        replace_off_light(LightAttrib self, const NodePath source, const NodePath dest)
        
        /**
         * Returns a new LightAttrib, just like this one, but with the indicated light
         * replaced with the given other light.
         */
        """
        pass

    def replaceOnLight(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        replace_on_light(LightAttrib self, const NodePath source, const NodePath dest)
        
        /**
         * Returns a new LightAttrib, just like this one, but with the indicated light
         * replaced with the given other light.
         */
        """
        pass

    def replace_off_light(self, LightAttrib_self, const_NodePath_source, const_NodePath_dest): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        replace_off_light(LightAttrib self, const NodePath source, const NodePath dest)
        
        /**
         * Returns a new LightAttrib, just like this one, but with the indicated light
         * replaced with the given other light.
         */
        """
        pass

    def replace_on_light(self, LightAttrib_self, const_NodePath_source, const_NodePath_dest): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        replace_on_light(LightAttrib self, const NodePath source, const NodePath dest)
        
        /**
         * Returns a new LightAttrib, just like this one, but with the indicated light
         * replaced with the given other light.
         */
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    off_lights = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    on_lights = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    class_slot = 16
    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        'OAdd': 1,
        'ORemove': 2,
        'OSet': 0,
        'O_add': 1,
        'O_remove': 2,
        'O_set': 0,
        '__doc__': '/**\n * Indicates which set of lights should be considered "on" to illuminate\n * geometry at this level and below.  A LightAttrib can either add lights or\n * remove lights from the total set of "on" lights.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.LightAttrib' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE297D80>'
        'addLight': None, # (!) real value is "<method 'addLight' of 'panda3d.core.LightAttrib' objects>"
        'addOffLight': None, # (!) real value is "<method 'addOffLight' of 'panda3d.core.LightAttrib' objects>"
        'addOnLight': None, # (!) real value is "<method 'addOnLight' of 'panda3d.core.LightAttrib' objects>"
        'add_light': None, # (!) real value is "<method 'add_light' of 'panda3d.core.LightAttrib' objects>"
        'add_off_light': None, # (!) real value is "<method 'add_off_light' of 'panda3d.core.LightAttrib' objects>"
        'add_on_light': None, # (!) real value is "<method 'add_on_light' of 'panda3d.core.LightAttrib' objects>"
        'class_slot': None, # (!) real value is "<attribute 'class_slot' of 'panda3d.core.LightAttrib'>"
        'getAmbientContribution': None, # (!) real value is "<method 'getAmbientContribution' of 'panda3d.core.LightAttrib' objects>"
        'getClassSlot': None, # (!) real value is '<staticmethod(<built-in method getClassSlot of type object at 0x00007FFCFE297D80>)>'
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE297D80>)>'
        'getLight': None, # (!) real value is "<method 'getLight' of 'panda3d.core.LightAttrib' objects>"
        'getMostImportantLight': None, # (!) real value is "<method 'getMostImportantLight' of 'panda3d.core.LightAttrib' objects>"
        'getNumLights': None, # (!) real value is "<method 'getNumLights' of 'panda3d.core.LightAttrib' objects>"
        'getNumNonAmbientLights': None, # (!) real value is "<method 'getNumNonAmbientLights' of 'panda3d.core.LightAttrib' objects>"
        'getNumOffLights': None, # (!) real value is "<method 'getNumOffLights' of 'panda3d.core.LightAttrib' objects>"
        'getNumOnLights': None, # (!) real value is "<method 'getNumOnLights' of 'panda3d.core.LightAttrib' objects>"
        'getOffLight': None, # (!) real value is "<method 'getOffLight' of 'panda3d.core.LightAttrib' objects>"
        'getOffLights': None, # (!) real value is "<method 'getOffLights' of 'panda3d.core.LightAttrib' objects>"
        'getOnLight': None, # (!) real value is "<method 'getOnLight' of 'panda3d.core.LightAttrib' objects>"
        'getOnLights': None, # (!) real value is "<method 'getOnLights' of 'panda3d.core.LightAttrib' objects>"
        'getOperation': None, # (!) real value is "<method 'getOperation' of 'panda3d.core.LightAttrib' objects>"
        'get_ambient_contribution': None, # (!) real value is "<method 'get_ambient_contribution' of 'panda3d.core.LightAttrib' objects>"
        'get_class_slot': None, # (!) real value is '<staticmethod(<built-in method get_class_slot of type object at 0x00007FFCFE297D80>)>'
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE297D80>)>'
        'get_light': None, # (!) real value is "<method 'get_light' of 'panda3d.core.LightAttrib' objects>"
        'get_most_important_light': None, # (!) real value is "<method 'get_most_important_light' of 'panda3d.core.LightAttrib' objects>"
        'get_num_lights': None, # (!) real value is "<method 'get_num_lights' of 'panda3d.core.LightAttrib' objects>"
        'get_num_non_ambient_lights': None, # (!) real value is "<method 'get_num_non_ambient_lights' of 'panda3d.core.LightAttrib' objects>"
        'get_num_off_lights': None, # (!) real value is "<method 'get_num_off_lights' of 'panda3d.core.LightAttrib' objects>"
        'get_num_on_lights': None, # (!) real value is "<method 'get_num_on_lights' of 'panda3d.core.LightAttrib' objects>"
        'get_off_light': None, # (!) real value is "<method 'get_off_light' of 'panda3d.core.LightAttrib' objects>"
        'get_off_lights': None, # (!) real value is "<method 'get_off_lights' of 'panda3d.core.LightAttrib' objects>"
        'get_on_light': None, # (!) real value is "<method 'get_on_light' of 'panda3d.core.LightAttrib' objects>"
        'get_on_lights': None, # (!) real value is "<method 'get_on_lights' of 'panda3d.core.LightAttrib' objects>"
        'get_operation': None, # (!) real value is "<method 'get_operation' of 'panda3d.core.LightAttrib' objects>"
        'hasAllOff': None, # (!) real value is "<method 'hasAllOff' of 'panda3d.core.LightAttrib' objects>"
        'hasAnyOnLight': None, # (!) real value is "<method 'hasAnyOnLight' of 'panda3d.core.LightAttrib' objects>"
        'hasLight': None, # (!) real value is "<method 'hasLight' of 'panda3d.core.LightAttrib' objects>"
        'hasOffLight': None, # (!) real value is "<method 'hasOffLight' of 'panda3d.core.LightAttrib' objects>"
        'hasOnLight': None, # (!) real value is "<method 'hasOnLight' of 'panda3d.core.LightAttrib' objects>"
        'has_all_off': None, # (!) real value is "<method 'has_all_off' of 'panda3d.core.LightAttrib' objects>"
        'has_any_on_light': None, # (!) real value is "<method 'has_any_on_light' of 'panda3d.core.LightAttrib' objects>"
        'has_light': None, # (!) real value is "<method 'has_light' of 'panda3d.core.LightAttrib' objects>"
        'has_off_light': None, # (!) real value is "<method 'has_off_light' of 'panda3d.core.LightAttrib' objects>"
        'has_on_light': None, # (!) real value is "<method 'has_on_light' of 'panda3d.core.LightAttrib' objects>"
        'isIdentity': None, # (!) real value is "<method 'isIdentity' of 'panda3d.core.LightAttrib' objects>"
        'is_identity': None, # (!) real value is "<method 'is_identity' of 'panda3d.core.LightAttrib' objects>"
        'make': None, # (!) real value is '<staticmethod(<built-in method make of type object at 0x00007FFCFE297D80>)>'
        'makeAllOff': None, # (!) real value is '<staticmethod(<built-in method makeAllOff of type object at 0x00007FFCFE297D80>)>'
        'makeDefault': None, # (!) real value is '<staticmethod(<built-in method makeDefault of type object at 0x00007FFCFE297D80>)>'
        'make_all_off': None, # (!) real value is '<staticmethod(<built-in method make_all_off of type object at 0x00007FFCFE297D80>)>'
        'make_default': None, # (!) real value is '<staticmethod(<built-in method make_default of type object at 0x00007FFCFE297D80>)>'
        'off_lights': None, # (!) real value is "<attribute 'off_lights' of 'panda3d.core.LightAttrib' objects>"
        'on_lights': None, # (!) real value is "<attribute 'on_lights' of 'panda3d.core.LightAttrib' objects>"
        'removeLight': None, # (!) real value is "<method 'removeLight' of 'panda3d.core.LightAttrib' objects>"
        'removeOffLight': None, # (!) real value is "<method 'removeOffLight' of 'panda3d.core.LightAttrib' objects>"
        'removeOnLight': None, # (!) real value is "<method 'removeOnLight' of 'panda3d.core.LightAttrib' objects>"
        'remove_light': None, # (!) real value is "<method 'remove_light' of 'panda3d.core.LightAttrib' objects>"
        'remove_off_light': None, # (!) real value is "<method 'remove_off_light' of 'panda3d.core.LightAttrib' objects>"
        'remove_on_light': None, # (!) real value is "<method 'remove_on_light' of 'panda3d.core.LightAttrib' objects>"
        'replaceOffLight': None, # (!) real value is "<method 'replaceOffLight' of 'panda3d.core.LightAttrib' objects>"
        'replaceOnLight': None, # (!) real value is "<method 'replaceOnLight' of 'panda3d.core.LightAttrib' objects>"
        'replace_off_light': None, # (!) real value is "<method 'replace_off_light' of 'panda3d.core.LightAttrib' objects>"
        'replace_on_light': None, # (!) real value is "<method 'replace_on_light' of 'panda3d.core.LightAttrib' objects>"
    }
    OAdd = 1
    ORemove = 2
    OSet = 0
    O_add = 1
    O_remove = 2
    O_set = 0


