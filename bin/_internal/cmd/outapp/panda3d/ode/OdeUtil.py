# encoding: utf-8
# module panda3d.ode
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\ode.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import panda3d.core as __panda3d_core


class OdeUtil(__dtoolconfig.DTOOL_SUPER_BASE):
    """
    /**
     *
     */
    """
    def areConnected(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        are_connected(const OdeBody body1, const OdeBody body2)
        
        /**
         * Returns 1 if the given bodies are connected by a joint, returns 0
         * otherwise.
         */
        """
        pass

    def areConnectedExcluding(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        are_connected_excluding(const OdeBody body1, const OdeBody body2, int joint_type)
        
        /**
         * Returns 1 if the given bodies are connected by a joint that does not match
         * the given joint_type, returns 0 otherwise.  This is useful for deciding
         * whether to add contact joints between two bodies: if they are already
         * connected by non-contact joints then it may not be appropriate to add
         * contacts, however it is okay to add more contact between bodies that
         * already have contacts.
         */
        """
        pass

    def are_connected(self, const_OdeBody_body1, const_OdeBody_body2): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        are_connected(const OdeBody body1, const OdeBody body2)
        
        /**
         * Returns 1 if the given bodies are connected by a joint, returns 0
         * otherwise.
         */
        """
        pass

    def are_connected_excluding(self, const_OdeBody_body1, const_OdeBody_body2, int_joint_type): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        are_connected_excluding(const OdeBody body1, const OdeBody body2, int joint_type)
        
        /**
         * Returns 1 if the given bodies are connected by a joint that does not match
         * the given joint_type, returns 0 otherwise.  This is useful for deciding
         * whether to add contact joints between two bodies: if they are already
         * connected by non-contact joints then it may not be appropriate to add
         * contacts, however it is okay to add more contact between bodies that
         * already have contacts.
         */
        """
        pass

    def collide(self, const_OdeGeom_geom1, const_OdeGeom_geom2, int_max_contacts): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        collide(const OdeGeom geom1, const OdeGeom geom2, int max_contacts)
        
        /**
         * Given two geometry objects that potentially touch (geom1 and geom2),
         * generate contact information for them.  Returns an OdeCollisionEntry.
         */
        """
        pass

    def collide2(self, const_OdeGeom_geom1, const_OdeGeom_geom2, object_arg, object_callback): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        collide2(const OdeGeom geom1, const OdeGeom geom2, object arg, object callback)
        """
        pass

    def getConnectingJoint(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_connecting_joint(const OdeBody body1, const OdeBody body2)
        
        /**
         * Returns the joint that connects the given bodies.
         */
        """
        pass

    def getConnectingJointList(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_connecting_joint_list(const OdeBody body1, const OdeBody body2)
        
        /**
         * Returns a collection of joints connecting the specified bodies.
         */
        """
        pass

    def getInfinity(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_infinity()
        
        // RAU we can't access OC_infinity as constants are not exposed in python
        """
        pass

    def get_connecting_joint(self, const_OdeBody_body1, const_OdeBody_body2): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_connecting_joint(const OdeBody body1, const OdeBody body2)
        
        /**
         * Returns the joint that connects the given bodies.
         */
        """
        pass

    def get_connecting_joint_list(self, const_OdeBody_body1, const_OdeBody_body2): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_connecting_joint_list(const OdeBody body1, const OdeBody body2)
        
        /**
         * Returns a collection of joints connecting the specified bodies.
         */
        """
        pass

    def get_infinity(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_infinity()
        
        // RAU we can't access OC_infinity as constants are not exposed in python
        """
        pass

    def randGetSeed(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        rand_get_seed()
        """
        pass

    def randSetSeed(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        rand_set_seed(int s)
        """
        pass

    def rand_get_seed(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        rand_get_seed()
        """
        pass

    def rand_set_seed(self, int_s): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        rand_set_seed(int s)
        """
        pass

    def spaceToGeom(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        space_to_geom(const OdeSpace space)
        """
        pass

    def space_to_geom(self, const_OdeSpace_space): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        space_to_geom(const OdeSpace space)
        """
        pass

    def __copy__(self, *args, **kwargs): # real signature unknown
        pass

    def __deepcopy__(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.ode.OdeUtil' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.ode.OdeUtil' objects>"
        '__doc__': '/**\n *\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.ode.OdeUtil' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFDC9DEEBC0>'
        'areConnected': None, # (!) real value is '<staticmethod(<built-in method areConnected of type object at 0x00007FFDC9DEEBC0>)>'
        'areConnectedExcluding': None, # (!) real value is '<staticmethod(<built-in method areConnectedExcluding of type object at 0x00007FFDC9DEEBC0>)>'
        'are_connected': None, # (!) real value is '<staticmethod(<built-in method are_connected of type object at 0x00007FFDC9DEEBC0>)>'
        'are_connected_excluding': None, # (!) real value is '<staticmethod(<built-in method are_connected_excluding of type object at 0x00007FFDC9DEEBC0>)>'
        'collide': None, # (!) real value is '<staticmethod(<built-in method collide of type object at 0x00007FFDC9DEEBC0>)>'
        'collide2': None, # (!) real value is '<staticmethod(<built-in method collide2 of type object at 0x00007FFDC9DEEBC0>)>'
        'getConnectingJoint': None, # (!) real value is '<staticmethod(<built-in method getConnectingJoint of type object at 0x00007FFDC9DEEBC0>)>'
        'getConnectingJointList': None, # (!) real value is '<staticmethod(<built-in method getConnectingJointList of type object at 0x00007FFDC9DEEBC0>)>'
        'getInfinity': None, # (!) real value is '<staticmethod(<built-in method getInfinity of type object at 0x00007FFDC9DEEBC0>)>'
        'get_connecting_joint': None, # (!) real value is '<staticmethod(<built-in method get_connecting_joint of type object at 0x00007FFDC9DEEBC0>)>'
        'get_connecting_joint_list': None, # (!) real value is '<staticmethod(<built-in method get_connecting_joint_list of type object at 0x00007FFDC9DEEBC0>)>'
        'get_infinity': None, # (!) real value is '<staticmethod(<built-in method get_infinity of type object at 0x00007FFDC9DEEBC0>)>'
        'randGetSeed': None, # (!) real value is '<staticmethod(<built-in method randGetSeed of type object at 0x00007FFDC9DEEBC0>)>'
        'randSetSeed': None, # (!) real value is '<staticmethod(<built-in method randSetSeed of type object at 0x00007FFDC9DEEBC0>)>'
        'rand_get_seed': None, # (!) real value is '<staticmethod(<built-in method rand_get_seed of type object at 0x00007FFDC9DEEBC0>)>'
        'rand_set_seed': None, # (!) real value is '<staticmethod(<built-in method rand_set_seed of type object at 0x00007FFDC9DEEBC0>)>'
        'spaceToGeom': None, # (!) real value is '<staticmethod(<built-in method spaceToGeom of type object at 0x00007FFDC9DEEBC0>)>'
        'space_to_geom': None, # (!) real value is '<staticmethod(<built-in method space_to_geom of type object at 0x00007FFDC9DEEBC0>)>'
    }


