# encoding: utf-8
# module panda3d.ode
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\ode.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import panda3d.core as __panda3d_core


class OdeCollisionEntry(__panda3d_core.TypedReferenceCount):
    """
    /**
     * A class used to hold information about a collision that has occurred.
     */
    """
    def getBody1(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_body1(OdeCollisionEntry self)
        
        /**
         * Returns the first body in the collision.
         */
        """
        pass

    def getBody2(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_body2(OdeCollisionEntry self)
        
        /**
         * Returns the second body in the collision.
         */
        """
        pass

    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getContactGeom(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_contact_geom(OdeCollisionEntry self, int n)
        
        /**
         * Returns the nth contact geom in the collision.
         */
        """
        pass

    def getContactGeoms(self, *args, **kwargs): # real signature unknown
        pass

    def getContactPoint(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_contact_point(OdeCollisionEntry self, int n)
        
        /**
         * Returns the nth contact point in the collision.  This does exactly the same
         * as get_contact_geom(n).get_pos().
         */
        """
        pass

    def getContactPoints(self, *args, **kwargs): # real signature unknown
        pass

    def getGeom1(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_geom1(OdeCollisionEntry self)
        
        /**
         * Returns the first geom in the collision.
         */
        """
        pass

    def getGeom2(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_geom2(OdeCollisionEntry self)
        
        /**
         * Returns the second geom in the collision.
         */
        """
        pass

    def getNumContacts(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_contacts(OdeCollisionEntry self)
        
        /**
         * Returns the number of contacts in the collision.
         */
        """
        pass

    def get_body1(self, OdeCollisionEntry_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_body1(OdeCollisionEntry self)
        
        /**
         * Returns the first body in the collision.
         */
        """
        pass

    def get_body2(self, OdeCollisionEntry_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_body2(OdeCollisionEntry self)
        
        /**
         * Returns the second body in the collision.
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_contact_geom(self, OdeCollisionEntry_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_contact_geom(OdeCollisionEntry self, int n)
        
        /**
         * Returns the nth contact geom in the collision.
         */
        """
        pass

    def get_contact_geoms(self, *args, **kwargs): # real signature unknown
        pass

    def get_contact_point(self, OdeCollisionEntry_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_contact_point(OdeCollisionEntry self, int n)
        
        /**
         * Returns the nth contact point in the collision.  This does exactly the same
         * as get_contact_geom(n).get_pos().
         */
        """
        pass

    def get_contact_points(self, *args, **kwargs): # real signature unknown
        pass

    def get_geom1(self, OdeCollisionEntry_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_geom1(OdeCollisionEntry self)
        
        /**
         * Returns the first geom in the collision.
         */
        """
        pass

    def get_geom2(self, OdeCollisionEntry_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_geom2(OdeCollisionEntry self)
        
        /**
         * Returns the second geom in the collision.
         */
        """
        pass

    def get_num_contacts(self, OdeCollisionEntry_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_contacts(OdeCollisionEntry self)
        
        /**
         * Returns the number of contacts in the collision.
         */
        """
        pass

    def isEmpty(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_empty(OdeCollisionEntry self)
        
        /**
         * Returns true if the entry holds no contacts.
         */
        """
        pass

    def is_empty(self, OdeCollisionEntry_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_empty(OdeCollisionEntry self)
        
        /**
         * Returns true if the entry holds no contacts.
         */
        """
        pass

    def __bool__(self, *args, **kwargs): # real signature unknown
        """ True if self else False """
        pass

    def __copy__(self, *args, **kwargs): # real signature unknown
        pass

    def __deepcopy__(self, *args, **kwargs): # real signature unknown
        pass

    def __getitem__(self, *args, **kwargs): # real signature unknown
        """ Return self[key]. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__bool__': None, # (!) real value is "<slot wrapper '__bool__' of 'panda3d.ode.OdeCollisionEntry' objects>"
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.ode.OdeCollisionEntry' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.ode.OdeCollisionEntry' objects>"
        '__doc__': '/**\n * A class used to hold information about a collision that has occurred.\n */',
        '__getitem__': None, # (!) real value is "<slot wrapper '__getitem__' of 'panda3d.ode.OdeCollisionEntry' objects>"
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.ode.OdeCollisionEntry' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFDC9DEC3E0>'
        'getBody1': None, # (!) real value is "<method 'getBody1' of 'panda3d.ode.OdeCollisionEntry' objects>"
        'getBody2': None, # (!) real value is "<method 'getBody2' of 'panda3d.ode.OdeCollisionEntry' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFDC9DEC3E0>)>'
        'getContactGeom': None, # (!) real value is "<method 'getContactGeom' of 'panda3d.ode.OdeCollisionEntry' objects>"
        'getContactGeoms': None, # (!) real value is "<method 'getContactGeoms' of 'panda3d.ode.OdeCollisionEntry' objects>"
        'getContactPoint': None, # (!) real value is "<method 'getContactPoint' of 'panda3d.ode.OdeCollisionEntry' objects>"
        'getContactPoints': None, # (!) real value is "<method 'getContactPoints' of 'panda3d.ode.OdeCollisionEntry' objects>"
        'getGeom1': None, # (!) real value is "<method 'getGeom1' of 'panda3d.ode.OdeCollisionEntry' objects>"
        'getGeom2': None, # (!) real value is "<method 'getGeom2' of 'panda3d.ode.OdeCollisionEntry' objects>"
        'getNumContacts': None, # (!) real value is "<method 'getNumContacts' of 'panda3d.ode.OdeCollisionEntry' objects>"
        'get_body1': None, # (!) real value is "<method 'get_body1' of 'panda3d.ode.OdeCollisionEntry' objects>"
        'get_body2': None, # (!) real value is "<method 'get_body2' of 'panda3d.ode.OdeCollisionEntry' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFDC9DEC3E0>)>'
        'get_contact_geom': None, # (!) real value is "<method 'get_contact_geom' of 'panda3d.ode.OdeCollisionEntry' objects>"
        'get_contact_geoms': None, # (!) real value is "<method 'get_contact_geoms' of 'panda3d.ode.OdeCollisionEntry' objects>"
        'get_contact_point': None, # (!) real value is "<method 'get_contact_point' of 'panda3d.ode.OdeCollisionEntry' objects>"
        'get_contact_points': None, # (!) real value is "<method 'get_contact_points' of 'panda3d.ode.OdeCollisionEntry' objects>"
        'get_geom1': None, # (!) real value is "<method 'get_geom1' of 'panda3d.ode.OdeCollisionEntry' objects>"
        'get_geom2': None, # (!) real value is "<method 'get_geom2' of 'panda3d.ode.OdeCollisionEntry' objects>"
        'get_num_contacts': None, # (!) real value is "<method 'get_num_contacts' of 'panda3d.ode.OdeCollisionEntry' objects>"
        'isEmpty': None, # (!) real value is "<method 'isEmpty' of 'panda3d.ode.OdeCollisionEntry' objects>"
        'is_empty': None, # (!) real value is "<method 'is_empty' of 'panda3d.ode.OdeCollisionEntry' objects>"
    }


