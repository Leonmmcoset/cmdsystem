# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .CollisionHandlerEvent import CollisionHandlerEvent

class CollisionHandlerPhysical(CollisionHandlerEvent):
    """
    /**
     * The abstract base class for a number of CollisionHandlers that have some
     * physical effect on their moving bodies: they need to update the nodes'
     * positions based on the effects of the collision.
     */
    """
    def addCollider(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_collider(const CollisionHandlerPhysical self, const NodePath collider, const NodePath target)
        add_collider(const CollisionHandlerPhysical self, const NodePath collider, const NodePath target, DriveInterface drive_interface)
        
        /**
         * Adds a new collider to the list with a NodePath that will be updated with
         * the collider's new position, or updates the existing collider with a new
         * NodePath object.
         */
        
        /**
         * Adds a new collider to the list with a NodePath that will be updated with
         * the collider's new position, or updates the existing collider with a new
         * NodePath object.
         *
         * The indicated DriveInterface will also be updated with the target's new
         * transform each frame.  This method should be used when the target is
         * directly controlled by a DriveInterface.
         */
        """
        pass

    def add_collider(self, const_CollisionHandlerPhysical_self, const_NodePath_collider, const_NodePath_target): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_collider(const CollisionHandlerPhysical self, const NodePath collider, const NodePath target)
        add_collider(const CollisionHandlerPhysical self, const NodePath collider, const NodePath target, DriveInterface drive_interface)
        
        /**
         * Adds a new collider to the list with a NodePath that will be updated with
         * the collider's new position, or updates the existing collider with a new
         * NodePath object.
         */
        
        /**
         * Adds a new collider to the list with a NodePath that will be updated with
         * the collider's new position, or updates the existing collider with a new
         * NodePath object.
         *
         * The indicated DriveInterface will also be updated with the target's new
         * transform each frame.  This method should be used when the target is
         * directly controlled by a DriveInterface.
         */
        """
        pass

    def clearCenter(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_center(const CollisionHandlerPhysical self)
        
        /**
         * Clears the center NodePath specified with set_center.
         */
        """
        pass

    def clearColliders(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_colliders(const CollisionHandlerPhysical self)
        
        /**
         * Completely empties the list of colliders this handler knows about.
         */
        """
        pass

    def clear_center(self, const_CollisionHandlerPhysical_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_center(const CollisionHandlerPhysical self)
        
        /**
         * Clears the center NodePath specified with set_center.
         */
        """
        pass

    def clear_colliders(self, const_CollisionHandlerPhysical_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_colliders(const CollisionHandlerPhysical self)
        
        /**
         * Completely empties the list of colliders this handler knows about.
         */
        """
        pass

    def getCenter(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_center(CollisionHandlerPhysical self)
        
        /**
         * Returns the NodePath specified with set_center, or the empty NodePath if
         * nothing has been specified.
         */
        """
        pass

    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_center(self, CollisionHandlerPhysical_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_center(CollisionHandlerPhysical self)
        
        /**
         * Returns the NodePath specified with set_center, or the empty NodePath if
         * nothing has been specified.
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def hasCenter(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_center(CollisionHandlerPhysical self)
        
        /**
         * Returns true if a NodePath has been specified with set_center(), false
         * otherwise.
         */
        """
        pass

    def hasCollider(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_collider(CollisionHandlerPhysical self, const NodePath collider)
        
        /**
         * Returns true if the handler knows about the indicated collider, false
         * otherwise.
         */
        """
        pass

    def hasContact(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_contact(CollisionHandlerPhysical self)
        
        /**
         * Did the handler make any contacts with anything on the last collision pass?
         * Depending on how your world is setup, this can be used to tell if the
         * handler is out of the world (i.e.  out of bounds). That is the original use
         * of this call.
         */
        """
        pass

    def has_center(self, CollisionHandlerPhysical_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_center(CollisionHandlerPhysical self)
        
        /**
         * Returns true if a NodePath has been specified with set_center(), false
         * otherwise.
         */
        """
        pass

    def has_collider(self, CollisionHandlerPhysical_self, const_NodePath_collider): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_collider(CollisionHandlerPhysical self, const NodePath collider)
        
        /**
         * Returns true if the handler knows about the indicated collider, false
         * otherwise.
         */
        """
        pass

    def has_contact(self, CollisionHandlerPhysical_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_contact(CollisionHandlerPhysical self)
        
        /**
         * Did the handler make any contacts with anything on the last collision pass?
         * Depending on how your world is setup, this can be used to tell if the
         * handler is out of the world (i.e.  out of bounds). That is the original use
         * of this call.
         */
        """
        pass

    def removeCollider(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        remove_collider(const CollisionHandlerPhysical self, const NodePath collider)
        
        /**
         * Removes the collider from the list of colliders that this handler knows
         * about.
         */
        """
        pass

    def remove_collider(self, const_CollisionHandlerPhysical_self, const_NodePath_collider): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        remove_collider(const CollisionHandlerPhysical self, const NodePath collider)
        
        /**
         * Removes the collider from the list of colliders that this handler knows
         * about.
         */
        """
        pass

    def setCenter(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_center(const CollisionHandlerPhysical self, const NodePath center)
        
        /**
         * Specifies an arbitrary NodePath that the handler is always considered to be
         * facing.  It does not detect collisions with surfaces that appear to be
         * facing away from this NodePath.  This works best when the collision
         * surfaces in question are polygons.
         */
        """
        pass

    def set_center(self, const_CollisionHandlerPhysical_self, const_NodePath_center): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_center(const CollisionHandlerPhysical self, const NodePath center)
        
        /**
         * Specifies an arbitrary NodePath that the handler is always considered to be
         * facing.  It does not detect collisions with surfaces that appear to be
         * facing away from this NodePath.  This works best when the collision
         * surfaces in question are polygons.
         */
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, CollisionHandlerPhysical_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        __reduce__(CollisionHandlerPhysical self)
        """
        pass

    def __setstate__(self, const_CollisionHandlerPhysical_self, bytes_data, object_nodepaths): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        __setstate__(const CollisionHandlerPhysical self, bytes data, object nodepaths)
        """
        pass

    center = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__doc__': "/**\n * The abstract base class for a number of CollisionHandlers that have some\n * physical effect on their moving bodies: they need to update the nodes'\n * positions based on the effects of the collision.\n */",
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.CollisionHandlerPhysical' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE2CF170>'
        '__reduce__': None, # (!) real value is "<method '__reduce__' of 'panda3d.core.CollisionHandlerPhysical' objects>"
        '__setstate__': None, # (!) real value is "<method '__setstate__' of 'panda3d.core.CollisionHandlerPhysical' objects>"
        'addCollider': None, # (!) real value is "<method 'addCollider' of 'panda3d.core.CollisionHandlerPhysical' objects>"
        'add_collider': None, # (!) real value is "<method 'add_collider' of 'panda3d.core.CollisionHandlerPhysical' objects>"
        'center': None, # (!) real value is "<attribute 'center' of 'panda3d.core.CollisionHandlerPhysical' objects>"
        'clearCenter': None, # (!) real value is "<method 'clearCenter' of 'panda3d.core.CollisionHandlerPhysical' objects>"
        'clearColliders': None, # (!) real value is "<method 'clearColliders' of 'panda3d.core.CollisionHandlerPhysical' objects>"
        'clear_center': None, # (!) real value is "<method 'clear_center' of 'panda3d.core.CollisionHandlerPhysical' objects>"
        'clear_colliders': None, # (!) real value is "<method 'clear_colliders' of 'panda3d.core.CollisionHandlerPhysical' objects>"
        'getCenter': None, # (!) real value is "<method 'getCenter' of 'panda3d.core.CollisionHandlerPhysical' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE2CF170>)>'
        'get_center': None, # (!) real value is "<method 'get_center' of 'panda3d.core.CollisionHandlerPhysical' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE2CF170>)>'
        'hasCenter': None, # (!) real value is "<method 'hasCenter' of 'panda3d.core.CollisionHandlerPhysical' objects>"
        'hasCollider': None, # (!) real value is "<method 'hasCollider' of 'panda3d.core.CollisionHandlerPhysical' objects>"
        'hasContact': None, # (!) real value is "<method 'hasContact' of 'panda3d.core.CollisionHandlerPhysical' objects>"
        'has_center': None, # (!) real value is "<method 'has_center' of 'panda3d.core.CollisionHandlerPhysical' objects>"
        'has_collider': None, # (!) real value is "<method 'has_collider' of 'panda3d.core.CollisionHandlerPhysical' objects>"
        'has_contact': None, # (!) real value is "<method 'has_contact' of 'panda3d.core.CollisionHandlerPhysical' objects>"
        'removeCollider': None, # (!) real value is "<method 'removeCollider' of 'panda3d.core.CollisionHandlerPhysical' objects>"
        'remove_collider': None, # (!) real value is "<method 'remove_collider' of 'panda3d.core.CollisionHandlerPhysical' objects>"
        'setCenter': None, # (!) real value is "<method 'setCenter' of 'panda3d.core.CollisionHandlerPhysical' objects>"
        'set_center': None, # (!) real value is "<method 'set_center' of 'panda3d.core.CollisionHandlerPhysical' objects>"
    }


