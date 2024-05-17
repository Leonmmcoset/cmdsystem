# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .PandaNode import PandaNode

class CollisionNode(PandaNode):
    """
    /**
     * A node in the scene graph that can hold any number of CollisionSolids.
     * This may either represent a bit of static geometry in the scene that things
     * will collide with, or an animated object twirling around in the world and
     * running into things.
     */
    """
    def addSolid(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_solid(const CollisionNode self, const CollisionSolid solid)
        
        /**
         * Adds the indicated solid to the node.  Returns the index of the new solid
         * within the node's list of solids.
         */
        """
        pass

    def add_solid(self, const_CollisionNode_self, const_CollisionSolid_solid): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_solid(const CollisionNode self, const CollisionSolid solid)
        
        /**
         * Adds the indicated solid to the node.  Returns the index of the new solid
         * within the node's list of solids.
         */
        """
        pass

    def clearSolids(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_solids(const CollisionNode self)
        
        /**
         * Removes all solids from the node.
         */
        """
        pass

    def clear_solids(self, const_CollisionNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_solids(const CollisionNode self)
        
        /**
         * Removes all solids from the node.
         */
        """
        pass

    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getColliderSort(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_collider_sort(CollisionNode self)
        
        /**
         * Returns the collider_sort value that has been set for this particular node.
         * See set_collider_sort().
         */
        """
        pass

    def getDefaultCollideMask(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_default_collide_mask()
        
        /**
         * Returns the default into_collide_mask assigned to new CollisionNodes.
         */
        """
        pass

    def getFromCollideMask(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_from_collide_mask(CollisionNode self)
        
        /**
         * Returns the current "from" CollideMask.  In order for a collision to be
         * detected from this object into another object, the intersection of this
         * object's "from" mask and the other object's "into" mask must be nonzero.
         */
        """
        pass

    def getIntoCollideMask(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_into_collide_mask(CollisionNode self)
        
        /**
         * Returns the current "into" CollideMask.  In order for a collision to be
         * detected from another object into this object, the intersection of the
         * other object's "from" mask and this object's "into" mask must be nonzero.
         */
        """
        pass

    def getNumSolids(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_solids(CollisionNode self)
        
        /**
         *
         */
        """
        pass

    def getSolid(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_solid(CollisionNode self, int n)
        
        /**
         *
         */
        """
        pass

    def getSolids(self, *args, **kwargs): # real signature unknown
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_collider_sort(self, CollisionNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_collider_sort(CollisionNode self)
        
        /**
         * Returns the collider_sort value that has been set for this particular node.
         * See set_collider_sort().
         */
        """
        pass

    def get_default_collide_mask(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_default_collide_mask()
        
        /**
         * Returns the default into_collide_mask assigned to new CollisionNodes.
         */
        """
        pass

    def get_from_collide_mask(self, CollisionNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_from_collide_mask(CollisionNode self)
        
        /**
         * Returns the current "from" CollideMask.  In order for a collision to be
         * detected from this object into another object, the intersection of this
         * object's "from" mask and the other object's "into" mask must be nonzero.
         */
        """
        pass

    def get_into_collide_mask(self, CollisionNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_into_collide_mask(CollisionNode self)
        
        /**
         * Returns the current "into" CollideMask.  In order for a collision to be
         * detected from another object into this object, the intersection of the
         * other object's "from" mask and this object's "into" mask must be nonzero.
         */
        """
        pass

    def get_num_solids(self, CollisionNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_solids(CollisionNode self)
        
        /**
         *
         */
        """
        pass

    def get_solid(self, CollisionNode_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_solid(CollisionNode self, int n)
        
        /**
         *
         */
        """
        pass

    def get_solids(self, *args, **kwargs): # real signature unknown
        pass

    def insertSolid(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        insert_solid(const CollisionNode self, int n, const CollisionSolid solid)
        
        /**
         * Inserts the indicated solid to the node at the indicated position.
         */
        """
        pass

    def insert_solid(self, const_CollisionNode_self, int_n, const_CollisionSolid_solid): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        insert_solid(const CollisionNode self, int n, const CollisionSolid solid)
        
        /**
         * Inserts the indicated solid to the node at the indicated position.
         */
        """
        pass

    def modifySolid(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        modify_solid(const CollisionNode self, int n)
        
        /**
         *
         */
        """
        pass

    def modify_solid(self, const_CollisionNode_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        modify_solid(const CollisionNode self, int n)
        
        /**
         *
         */
        """
        pass

    def removeSolid(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        remove_solid(const CollisionNode self, int n)
        
        /**
         * Removes the solid with the indicated index.  This will shift all subsequent
         * indices down by one.
         */
        """
        pass

    def remove_solid(self, const_CollisionNode_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        remove_solid(const CollisionNode self, int n)
        
        /**
         * Removes the solid with the indicated index.  This will shift all subsequent
         * indices down by one.
         */
        """
        pass

    def setCollideMask(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_collide_mask(const CollisionNode self, BitMask mask)
        
        /**
         * Simultaneously sets both the "from" and "into" CollideMask values to the
         * same thing.
         */
        """
        pass

    def setColliderSort(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_collider_sort(const CollisionNode self, int sort)
        
        /**
         * Sets a particular collider_sort value on this node.  This controls the
         * order in which colliders (that is, "from nodes") are grouped together for
         * the collision traversal.
         *
         * If there are 32 or fewer colliders added to any particular
         * CollisionTraverser, then this value has no meaning.  It is only useful if
         * there are many colliders, which may force the CollisionTraverser to make
         * multiple passes through the data; in that case, it may be a useful
         * optimization to group colliders that have similar bounding volumes together
         * (by giving them similar sort values).
         */
        """
        pass

    def setFromCollideMask(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_from_collide_mask(const CollisionNode self, BitMask mask)
        
        /**
         * Sets the "from" CollideMask.  In order for a collision to be detected from
         * this object into another object, the intersection of this object's "from"
         * mask and the other object's "into" mask must be nonzero.
         */
        """
        pass

    def setIntoCollideMask(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_into_collide_mask(const CollisionNode self, BitMask mask)
        
        /**
         * Sets the "into" CollideMask.  In order for a collision to be detected from
         * another object into this object, the intersection of the other object's
         * "from" mask and this object's "into" mask must be nonzero.
         */
        """
        pass

    def setSolid(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_solid(const CollisionNode self, int n, CollisionSolid solid)
        
        /**
         * Replaces the solid with the indicated index.
         */
        """
        pass

    def set_collider_sort(self, const_CollisionNode_self, int_sort): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_collider_sort(const CollisionNode self, int sort)
        
        /**
         * Sets a particular collider_sort value on this node.  This controls the
         * order in which colliders (that is, "from nodes") are grouped together for
         * the collision traversal.
         *
         * If there are 32 or fewer colliders added to any particular
         * CollisionTraverser, then this value has no meaning.  It is only useful if
         * there are many colliders, which may force the CollisionTraverser to make
         * multiple passes through the data; in that case, it may be a useful
         * optimization to group colliders that have similar bounding volumes together
         * (by giving them similar sort values).
         */
        """
        pass

    def set_collide_mask(self, const_CollisionNode_self, BitMask_mask): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_collide_mask(const CollisionNode self, BitMask mask)
        
        /**
         * Simultaneously sets both the "from" and "into" CollideMask values to the
         * same thing.
         */
        """
        pass

    def set_from_collide_mask(self, const_CollisionNode_self, BitMask_mask): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_from_collide_mask(const CollisionNode self, BitMask mask)
        
        /**
         * Sets the "from" CollideMask.  In order for a collision to be detected from
         * this object into another object, the intersection of this object's "from"
         * mask and the other object's "into" mask must be nonzero.
         */
        """
        pass

    def set_into_collide_mask(self, const_CollisionNode_self, BitMask_mask): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_into_collide_mask(const CollisionNode self, BitMask mask)
        
        /**
         * Sets the "into" CollideMask.  In order for a collision to be detected from
         * another object into this object, the intersection of the other object's
         * "from" mask and this object's "into" mask must be nonzero.
         */
        """
        pass

    def set_solid(self, const_CollisionNode_self, int_n, CollisionSolid_solid): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_solid(const CollisionNode self, int n, CollisionSolid solid)
        
        /**
         * Replaces the solid with the indicated index.
         */
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    collider_sort = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    from_collide_mask = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    into_collide_mask = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    solids = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    default_collide_mask = None # (!) real value is ' 0000 0000 0000 1111 1111 1111 1111 1111'
    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__doc__': '/**\n * A node in the scene graph that can hold any number of CollisionSolids.\n * This may either represent a bit of static geometry in the scene that things\n * will collide with, or an animated object twirling around in the world and\n * running into things.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.CollisionNode' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE2CE2F0>'
        'addSolid': None, # (!) real value is "<method 'addSolid' of 'panda3d.core.CollisionNode' objects>"
        'add_solid': None, # (!) real value is "<method 'add_solid' of 'panda3d.core.CollisionNode' objects>"
        'clearSolids': None, # (!) real value is "<method 'clearSolids' of 'panda3d.core.CollisionNode' objects>"
        'clear_solids': None, # (!) real value is "<method 'clear_solids' of 'panda3d.core.CollisionNode' objects>"
        'collider_sort': None, # (!) real value is "<attribute 'collider_sort' of 'panda3d.core.CollisionNode' objects>"
        'default_collide_mask': None, # (!) real value is "<attribute 'default_collide_mask' of 'panda3d.core.CollisionNode'>"
        'from_collide_mask': None, # (!) real value is "<attribute 'from_collide_mask' of 'panda3d.core.CollisionNode' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE2CE2F0>)>'
        'getColliderSort': None, # (!) real value is "<method 'getColliderSort' of 'panda3d.core.CollisionNode' objects>"
        'getDefaultCollideMask': None, # (!) real value is '<staticmethod(<built-in method getDefaultCollideMask of type object at 0x00007FFCFE2CE2F0>)>'
        'getFromCollideMask': None, # (!) real value is "<method 'getFromCollideMask' of 'panda3d.core.CollisionNode' objects>"
        'getIntoCollideMask': None, # (!) real value is "<method 'getIntoCollideMask' of 'panda3d.core.CollisionNode' objects>"
        'getNumSolids': None, # (!) real value is "<method 'getNumSolids' of 'panda3d.core.CollisionNode' objects>"
        'getSolid': None, # (!) real value is "<method 'getSolid' of 'panda3d.core.CollisionNode' objects>"
        'getSolids': None, # (!) real value is "<method 'getSolids' of 'panda3d.core.CollisionNode' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE2CE2F0>)>'
        'get_collider_sort': None, # (!) real value is "<method 'get_collider_sort' of 'panda3d.core.CollisionNode' objects>"
        'get_default_collide_mask': None, # (!) real value is '<staticmethod(<built-in method get_default_collide_mask of type object at 0x00007FFCFE2CE2F0>)>'
        'get_from_collide_mask': None, # (!) real value is "<method 'get_from_collide_mask' of 'panda3d.core.CollisionNode' objects>"
        'get_into_collide_mask': None, # (!) real value is "<method 'get_into_collide_mask' of 'panda3d.core.CollisionNode' objects>"
        'get_num_solids': None, # (!) real value is "<method 'get_num_solids' of 'panda3d.core.CollisionNode' objects>"
        'get_solid': None, # (!) real value is "<method 'get_solid' of 'panda3d.core.CollisionNode' objects>"
        'get_solids': None, # (!) real value is "<method 'get_solids' of 'panda3d.core.CollisionNode' objects>"
        'insertSolid': None, # (!) real value is "<method 'insertSolid' of 'panda3d.core.CollisionNode' objects>"
        'insert_solid': None, # (!) real value is "<method 'insert_solid' of 'panda3d.core.CollisionNode' objects>"
        'into_collide_mask': None, # (!) real value is "<attribute 'into_collide_mask' of 'panda3d.core.CollisionNode' objects>"
        'modifySolid': None, # (!) real value is "<method 'modifySolid' of 'panda3d.core.CollisionNode' objects>"
        'modify_solid': None, # (!) real value is "<method 'modify_solid' of 'panda3d.core.CollisionNode' objects>"
        'removeSolid': None, # (!) real value is "<method 'removeSolid' of 'panda3d.core.CollisionNode' objects>"
        'remove_solid': None, # (!) real value is "<method 'remove_solid' of 'panda3d.core.CollisionNode' objects>"
        'setCollideMask': None, # (!) real value is "<method 'setCollideMask' of 'panda3d.core.CollisionNode' objects>"
        'setColliderSort': None, # (!) real value is "<method 'setColliderSort' of 'panda3d.core.CollisionNode' objects>"
        'setFromCollideMask': None, # (!) real value is "<method 'setFromCollideMask' of 'panda3d.core.CollisionNode' objects>"
        'setIntoCollideMask': None, # (!) real value is "<method 'setIntoCollideMask' of 'panda3d.core.CollisionNode' objects>"
        'setSolid': None, # (!) real value is "<method 'setSolid' of 'panda3d.core.CollisionNode' objects>"
        'set_collide_mask': None, # (!) real value is "<method 'set_collide_mask' of 'panda3d.core.CollisionNode' objects>"
        'set_collider_sort': None, # (!) real value is "<method 'set_collider_sort' of 'panda3d.core.CollisionNode' objects>"
        'set_from_collide_mask': None, # (!) real value is "<method 'set_from_collide_mask' of 'panda3d.core.CollisionNode' objects>"
        'set_into_collide_mask': None, # (!) real value is "<method 'set_into_collide_mask' of 'panda3d.core.CollisionNode' objects>"
        'set_solid': None, # (!) real value is "<method 'set_solid' of 'panda3d.core.CollisionNode' objects>"
        'solids': None, # (!) real value is "<attribute 'solids' of 'panda3d.core.CollisionNode' objects>"
    }


