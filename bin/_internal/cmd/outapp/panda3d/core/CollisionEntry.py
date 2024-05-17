# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .TypedWritableReferenceCount import TypedWritableReferenceCount

class CollisionEntry(TypedWritableReferenceCount):
    """
    /**
     * Defines a single collision event.  One of these is created for each
     * collision detected by a CollisionTraverser, to be dealt with by the
     * CollisionHandler.
     *
     * A CollisionEntry provides slots for a number of data values (such as
     * intersection point and normal) that might or might not be known for each
     * collision.  It is up to the handler to determine what information is known
     * and to do the right thing with it.
     */
    """
    def collided(self, CollisionEntry_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        collided(CollisionEntry self)
        
        /**
         * returns true if this represents an actual collision as opposed to a
         * potential collision, needed for iterative collision resolution where path
         * of collider changes mid-frame
         */
        """
        pass

    def getAll(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_all(CollisionEntry self, const NodePath space, LPoint3f surface_point, LVector3f surface_normal, LPoint3f interior_point)
        
        /**
         * Simultaneously transforms the surface point, surface normal, and interior
         * point of the collision into the indicated coordinate space.
         *
         * Returns true if all three properties are available, or false if any one of
         * them is not.
         */
        """
        pass

    def getAllContactInfo(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_all_contact_info(CollisionEntry self, const NodePath space, LPoint3f contact_pos, LVector3f contact_normal)
        
        /**
         * Simultaneously transforms the contact position and contact normal of the
         * collision into the indicated coordinate space.
         *
         * Returns true if all three properties are available, or false if any one of
         * them is not.
         */
        """
        pass

    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getContactNormal(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_contact_normal(CollisionEntry self, const NodePath space)
        
        /**
         * Returns the surface normal of the "into" object at the contact position.
         *
         * The normal will be converted into whichever coordinate space the caller
         * specifies.
         */
        """
        pass

    def getContactPos(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_contact_pos(CollisionEntry self, const NodePath space)
        
        /**
         * Returns the position of the "from" object at the instant that a collision
         * is first detected.
         *
         * The position will be converted into whichever coordinate space the caller
         * specifies.
         */
        """
        pass

    def getFrom(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_from(CollisionEntry self)
        
        /**
         * Returns the CollisionSolid pointer for the particular solid that triggered
         * this collision.
         */
        """
        pass

    def getFromNode(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_from_node(CollisionEntry self)
        
        /**
         * Returns the node that contains the CollisionSolid that triggered this
         * collision.  This will be a node that has been added to a CollisionTraverser
         * via add_collider().
         */
        """
        pass

    def getFromNodePath(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_from_node_path(CollisionEntry self)
        
        /**
         * Returns the NodePath that represents the CollisionNode that contains the
         * CollisionSolid that triggered this collision.  This will be a NodePath that
         * has been added to a CollisionTraverser via add_collider().
         */
        """
        pass

    def getInteriorPoint(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_interior_point(CollisionEntry self, const NodePath space)
        
        /**
         * Returns the point, within the interior of the "into" object, which
         * represents the depth to which the "from" object has penetrated.  This can
         * also be described as the intersection point on the surface of the "from"
         * object (which is inside the "into" object).  It can be thought of as the
         * deepest point of intersection.
         *
         * The point will be converted into whichever coordinate space the caller
         * specifies.
         */
        """
        pass

    def getInto(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_into(CollisionEntry self)
        
        /**
         * Returns the CollisionSolid pointer for the particular solid was collided
         * into.  This pointer might be NULL if the collision was into a piece of
         * visible geometry, instead of a normal CollisionSolid collision; see
         * has_into().
         */
        """
        pass

    def getIntoNode(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_into_node(CollisionEntry self)
        
        /**
         * Returns the node that contains the CollisionSolid that was collided into.
         * This returns a PandaNode pointer instead of something more specific,
         * because it might be either a CollisionNode or a GeomNode.
         *
         * Also see get_into_node_path().
         */
        """
        pass

    def getIntoNodePath(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_into_node_path(CollisionEntry self)
        
        /**
         * Returns the NodePath that represents the specific CollisionNode or GeomNode
         * instance that was collided into.  This is the same node returned by
         * get_into_node(), represented as a NodePath; however, it may be more useful
         * because the NodePath can resolve the particular instance of the node, if
         * there is more than one.
         */
        """
        pass

    def getRespectPrevTransform(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_respect_prev_transform(CollisionEntry self)
        
        /**
         * Returns true if the collision was detected by a CollisionTraverser whose
         * respect_prev_transform flag was set true, meaning we should consider motion
         * significant in evaluating collisions.
         */
        """
        pass

    def getSurfaceNormal(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_surface_normal(CollisionEntry self, const NodePath space)
        
        /**
         * Returns the surface normal of the "into" object at the point at which a
         * collision is detected.
         *
         * The normal will be converted into whichever coordinate space the caller
         * specifies.
         */
        """
        pass

    def getSurfacePoint(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_surface_point(CollisionEntry self, const NodePath space)
        
        /**
         * Returns the point, on the surface of the "into" object, at which a
         * collision is detected.  This can be thought of as the first point of
         * intersection.  However the contact point is the actual first point of
         * intersection.
         *
         * The point will be converted into whichever coordinate space the caller
         * specifies.
         */
        """
        pass

    def getT(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_t(CollisionEntry self)
        
        /**
         * returns time value for this collision relative to other CollisionEntries
         */
        """
        pass

    def get_all(self, CollisionEntry_self, const_NodePath_space, LPoint3f_surface_point, LVector3f_surface_normal, LPoint3f_interior_point): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_all(CollisionEntry self, const NodePath space, LPoint3f surface_point, LVector3f surface_normal, LPoint3f interior_point)
        
        /**
         * Simultaneously transforms the surface point, surface normal, and interior
         * point of the collision into the indicated coordinate space.
         *
         * Returns true if all three properties are available, or false if any one of
         * them is not.
         */
        """
        pass

    def get_all_contact_info(self, CollisionEntry_self, const_NodePath_space, LPoint3f_contact_pos, LVector3f_contact_normal): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_all_contact_info(CollisionEntry self, const NodePath space, LPoint3f contact_pos, LVector3f contact_normal)
        
        /**
         * Simultaneously transforms the contact position and contact normal of the
         * collision into the indicated coordinate space.
         *
         * Returns true if all three properties are available, or false if any one of
         * them is not.
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_contact_normal(self, CollisionEntry_self, const_NodePath_space): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_contact_normal(CollisionEntry self, const NodePath space)
        
        /**
         * Returns the surface normal of the "into" object at the contact position.
         *
         * The normal will be converted into whichever coordinate space the caller
         * specifies.
         */
        """
        pass

    def get_contact_pos(self, CollisionEntry_self, const_NodePath_space): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_contact_pos(CollisionEntry self, const NodePath space)
        
        /**
         * Returns the position of the "from" object at the instant that a collision
         * is first detected.
         *
         * The position will be converted into whichever coordinate space the caller
         * specifies.
         */
        """
        pass

    def get_from(self, CollisionEntry_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_from(CollisionEntry self)
        
        /**
         * Returns the CollisionSolid pointer for the particular solid that triggered
         * this collision.
         */
        """
        pass

    def get_from_node(self, CollisionEntry_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_from_node(CollisionEntry self)
        
        /**
         * Returns the node that contains the CollisionSolid that triggered this
         * collision.  This will be a node that has been added to a CollisionTraverser
         * via add_collider().
         */
        """
        pass

    def get_from_node_path(self, CollisionEntry_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_from_node_path(CollisionEntry self)
        
        /**
         * Returns the NodePath that represents the CollisionNode that contains the
         * CollisionSolid that triggered this collision.  This will be a NodePath that
         * has been added to a CollisionTraverser via add_collider().
         */
        """
        pass

    def get_interior_point(self, CollisionEntry_self, const_NodePath_space): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_interior_point(CollisionEntry self, const NodePath space)
        
        /**
         * Returns the point, within the interior of the "into" object, which
         * represents the depth to which the "from" object has penetrated.  This can
         * also be described as the intersection point on the surface of the "from"
         * object (which is inside the "into" object).  It can be thought of as the
         * deepest point of intersection.
         *
         * The point will be converted into whichever coordinate space the caller
         * specifies.
         */
        """
        pass

    def get_into(self, CollisionEntry_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_into(CollisionEntry self)
        
        /**
         * Returns the CollisionSolid pointer for the particular solid was collided
         * into.  This pointer might be NULL if the collision was into a piece of
         * visible geometry, instead of a normal CollisionSolid collision; see
         * has_into().
         */
        """
        pass

    def get_into_node(self, CollisionEntry_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_into_node(CollisionEntry self)
        
        /**
         * Returns the node that contains the CollisionSolid that was collided into.
         * This returns a PandaNode pointer instead of something more specific,
         * because it might be either a CollisionNode or a GeomNode.
         *
         * Also see get_into_node_path().
         */
        """
        pass

    def get_into_node_path(self, CollisionEntry_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_into_node_path(CollisionEntry self)
        
        /**
         * Returns the NodePath that represents the specific CollisionNode or GeomNode
         * instance that was collided into.  This is the same node returned by
         * get_into_node(), represented as a NodePath; however, it may be more useful
         * because the NodePath can resolve the particular instance of the node, if
         * there is more than one.
         */
        """
        pass

    def get_respect_prev_transform(self, CollisionEntry_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_respect_prev_transform(CollisionEntry self)
        
        /**
         * Returns true if the collision was detected by a CollisionTraverser whose
         * respect_prev_transform flag was set true, meaning we should consider motion
         * significant in evaluating collisions.
         */
        """
        pass

    def get_surface_normal(self, CollisionEntry_self, const_NodePath_space): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_surface_normal(CollisionEntry self, const NodePath space)
        
        /**
         * Returns the surface normal of the "into" object at the point at which a
         * collision is detected.
         *
         * The normal will be converted into whichever coordinate space the caller
         * specifies.
         */
        """
        pass

    def get_surface_point(self, CollisionEntry_self, const_NodePath_space): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_surface_point(CollisionEntry self, const NodePath space)
        
        /**
         * Returns the point, on the surface of the "into" object, at which a
         * collision is detected.  This can be thought of as the first point of
         * intersection.  However the contact point is the actual first point of
         * intersection.
         *
         * The point will be converted into whichever coordinate space the caller
         * specifies.
         */
        """
        pass

    def get_t(self, CollisionEntry_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_t(CollisionEntry self)
        
        /**
         * returns time value for this collision relative to other CollisionEntries
         */
        """
        pass

    def hasContactNormal(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_contact_normal(CollisionEntry self)
        
        /**
         * Returns true if the contact normal has been specified, false otherwise.
         * See get_contact_normal().  Some types of collisions may not compute the
         * contact normal.
         */
        """
        pass

    def hasContactPos(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_contact_pos(CollisionEntry self)
        
        /**
         * Returns true if the contact position has been specified, false otherwise.
         * See get_contact_pos().  Some types of collisions may not compute the
         * contact pos.
         */
        """
        pass

    def hasInteriorPoint(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_interior_point(CollisionEntry self)
        
        /**
         * Returns true if the interior point has been specified, false otherwise.
         * See get_interior_point().  Some types of collisions may not compute the
         * interior point.
         */
        """
        pass

    def hasInto(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_into(CollisionEntry self)
        
        /**
         * Returns true if the "into" solid is, in fact, a CollisionSolid, and its
         * pointer is known (in which case get_into() may be called to retrieve it).
         * If this returns false, the collision was detected into a GeomNode, and
         * there is no CollisionSolid pointer to be retrieved.
         */
        """
        pass

    def hasSurfaceNormal(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_surface_normal(CollisionEntry self)
        
        /**
         * Returns true if the surface normal has been specified, false otherwise.
         * See get_surface_normal().  Some types of collisions may not compute the
         * surface normal.
         */
        """
        pass

    def hasSurfacePoint(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_surface_point(CollisionEntry self)
        
        /**
         * Returns true if the surface point has been specified, false otherwise.  See
         * get_surface_point().  Some types of collisions may not compute the surface
         * point.
         */
        """
        pass

    def has_contact_normal(self, CollisionEntry_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_contact_normal(CollisionEntry self)
        
        /**
         * Returns true if the contact normal has been specified, false otherwise.
         * See get_contact_normal().  Some types of collisions may not compute the
         * contact normal.
         */
        """
        pass

    def has_contact_pos(self, CollisionEntry_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_contact_pos(CollisionEntry self)
        
        /**
         * Returns true if the contact position has been specified, false otherwise.
         * See get_contact_pos().  Some types of collisions may not compute the
         * contact pos.
         */
        """
        pass

    def has_interior_point(self, CollisionEntry_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_interior_point(CollisionEntry self)
        
        /**
         * Returns true if the interior point has been specified, false otherwise.
         * See get_interior_point().  Some types of collisions may not compute the
         * interior point.
         */
        """
        pass

    def has_into(self, CollisionEntry_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_into(CollisionEntry self)
        
        /**
         * Returns true if the "into" solid is, in fact, a CollisionSolid, and its
         * pointer is known (in which case get_into() may be called to retrieve it).
         * If this returns false, the collision was detected into a GeomNode, and
         * there is no CollisionSolid pointer to be retrieved.
         */
        """
        pass

    def has_surface_normal(self, CollisionEntry_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_surface_normal(CollisionEntry self)
        
        /**
         * Returns true if the surface normal has been specified, false otherwise.
         * See get_surface_normal().  Some types of collisions may not compute the
         * surface normal.
         */
        """
        pass

    def has_surface_point(self, CollisionEntry_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_surface_point(CollisionEntry self)
        
        /**
         * Returns true if the surface point has been specified, false otherwise.  See
         * get_surface_point().  Some types of collisions may not compute the surface
         * point.
         */
        """
        pass

    def output(self, CollisionEntry_self, ostream_out): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        output(CollisionEntry self, ostream out)
        
        /**
         *
         */
        """
        pass

    def resetCollided(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        reset_collided(const CollisionEntry self)
        
        /**
         * prepare for another collision test
         */
        """
        pass

    def reset_collided(self, const_CollisionEntry_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        reset_collided(const CollisionEntry self)
        
        /**
         * prepare for another collision test
         */
        """
        pass

    def setContactNormal(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_contact_normal(const CollisionEntry self, const LVector3f normal)
        
        /**
         * Stores the surface normal of the "into" object at the contact pos.
         *
         * This normal is specified in the coordinate space of the "into" object.
         */
        """
        pass

    def setContactPos(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_contact_pos(const CollisionEntry self, const LPoint3f pos)
        
        /**
         * Stores the position of the "from" object at the instant at which the
         * collision is first detected.
         *
         * This position is specified in the coordinate space of the "into" object.
         */
        """
        pass

    def setInteriorPoint(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_interior_point(const CollisionEntry self, const LPoint3f point)
        
        /**
         * Stores the point, within the interior of the "into" object, which
         * represents the depth to which the "from" object has penetrated.  This can
         * also be described as the intersection point on the surface of the "from"
         * object (which is inside the "into" object).
         *
         * This point is specified in the coordinate space of the "into" object.
         */
        """
        pass

    def setSurfaceNormal(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_surface_normal(const CollisionEntry self, const LVector3f normal)
        
        /**
         * Stores the surface normal of the "into" object at the point of the
         * intersection.
         *
         * This normal is specified in the coordinate space of the "into" object.
         */
        """
        pass

    def setSurfacePoint(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_surface_point(const CollisionEntry self, const LPoint3f point)
        
        /**
         * Stores the point, on the surface of the "into" object, at which a collision
         * is detected.
         *
         * This point is specified in the coordinate space of the "into" object.
         */
        """
        pass

    def setT(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_t(const CollisionEntry self, float t)
        
        /**
         * Sets a time value for this collision relative to other CollisionEntries
         */
        """
        pass

    def set_contact_normal(self, const_CollisionEntry_self, const_LVector3f_normal): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_contact_normal(const CollisionEntry self, const LVector3f normal)
        
        /**
         * Stores the surface normal of the "into" object at the contact pos.
         *
         * This normal is specified in the coordinate space of the "into" object.
         */
        """
        pass

    def set_contact_pos(self, const_CollisionEntry_self, const_LPoint3f_pos): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_contact_pos(const CollisionEntry self, const LPoint3f pos)
        
        /**
         * Stores the position of the "from" object at the instant at which the
         * collision is first detected.
         *
         * This position is specified in the coordinate space of the "into" object.
         */
        """
        pass

    def set_interior_point(self, const_CollisionEntry_self, const_LPoint3f_point): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_interior_point(const CollisionEntry self, const LPoint3f point)
        
        /**
         * Stores the point, within the interior of the "into" object, which
         * represents the depth to which the "from" object has penetrated.  This can
         * also be described as the intersection point on the surface of the "from"
         * object (which is inside the "into" object).
         *
         * This point is specified in the coordinate space of the "into" object.
         */
        """
        pass

    def set_surface_normal(self, const_CollisionEntry_self, const_LVector3f_normal): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_surface_normal(const CollisionEntry self, const LVector3f normal)
        
        /**
         * Stores the surface normal of the "into" object at the point of the
         * intersection.
         *
         * This normal is specified in the coordinate space of the "into" object.
         */
        """
        pass

    def set_surface_point(self, const_CollisionEntry_self, const_LPoint3f_point): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_surface_point(const CollisionEntry self, const LPoint3f point)
        
        /**
         * Stores the point, on the surface of the "into" object, at which a collision
         * is detected.
         *
         * This point is specified in the coordinate space of the "into" object.
         */
        """
        pass

    def set_t(self, const_CollisionEntry_self, float_t): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_t(const CollisionEntry self, float t)
        
        /**
         * Sets a time value for this collision relative to other CollisionEntries
         */
        """
        pass

    def write(self, CollisionEntry_self, ostream_out, int_indent_level): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        write(CollisionEntry self, ostream out, int indent_level)
        
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

    from_node = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    from_node_path = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    from_solid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    into_node = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    into_node_path = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    into_solid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    respect_prev_transform = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    t = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__doc__': '/**\n * Defines a single collision event.  One of these is created for each\n * collision detected by a CollisionTraverser, to be dealt with by the\n * CollisionHandler.\n *\n * A CollisionEntry provides slots for a number of data values (such as\n * intersection point and normal) that might or might not be known for each\n * collision.  It is up to the handler to determine what information is known\n * and to do the right thing with it.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.CollisionEntry' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE2CE860>'
        '__repr__': None, # (!) real value is "<slot wrapper '__repr__' of 'panda3d.core.CollisionEntry' objects>"
        '__str__': None, # (!) real value is "<slot wrapper '__str__' of 'panda3d.core.CollisionEntry' objects>"
        'collided': None, # (!) real value is "<method 'collided' of 'panda3d.core.CollisionEntry' objects>"
        'from_node': None, # (!) real value is "<attribute 'from_node' of 'panda3d.core.CollisionEntry' objects>"
        'from_node_path': None, # (!) real value is "<attribute 'from_node_path' of 'panda3d.core.CollisionEntry' objects>"
        'from_solid': None, # (!) real value is "<attribute 'from_solid' of 'panda3d.core.CollisionEntry' objects>"
        'getAll': None, # (!) real value is "<method 'getAll' of 'panda3d.core.CollisionEntry' objects>"
        'getAllContactInfo': None, # (!) real value is "<method 'getAllContactInfo' of 'panda3d.core.CollisionEntry' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE2CE860>)>'
        'getContactNormal': None, # (!) real value is "<method 'getContactNormal' of 'panda3d.core.CollisionEntry' objects>"
        'getContactPos': None, # (!) real value is "<method 'getContactPos' of 'panda3d.core.CollisionEntry' objects>"
        'getFrom': None, # (!) real value is "<method 'getFrom' of 'panda3d.core.CollisionEntry' objects>"
        'getFromNode': None, # (!) real value is "<method 'getFromNode' of 'panda3d.core.CollisionEntry' objects>"
        'getFromNodePath': None, # (!) real value is "<method 'getFromNodePath' of 'panda3d.core.CollisionEntry' objects>"
        'getInteriorPoint': None, # (!) real value is "<method 'getInteriorPoint' of 'panda3d.core.CollisionEntry' objects>"
        'getInto': None, # (!) real value is "<method 'getInto' of 'panda3d.core.CollisionEntry' objects>"
        'getIntoNode': None, # (!) real value is "<method 'getIntoNode' of 'panda3d.core.CollisionEntry' objects>"
        'getIntoNodePath': None, # (!) real value is "<method 'getIntoNodePath' of 'panda3d.core.CollisionEntry' objects>"
        'getRespectPrevTransform': None, # (!) real value is "<method 'getRespectPrevTransform' of 'panda3d.core.CollisionEntry' objects>"
        'getSurfaceNormal': None, # (!) real value is "<method 'getSurfaceNormal' of 'panda3d.core.CollisionEntry' objects>"
        'getSurfacePoint': None, # (!) real value is "<method 'getSurfacePoint' of 'panda3d.core.CollisionEntry' objects>"
        'getT': None, # (!) real value is "<method 'getT' of 'panda3d.core.CollisionEntry' objects>"
        'get_all': None, # (!) real value is "<method 'get_all' of 'panda3d.core.CollisionEntry' objects>"
        'get_all_contact_info': None, # (!) real value is "<method 'get_all_contact_info' of 'panda3d.core.CollisionEntry' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE2CE860>)>'
        'get_contact_normal': None, # (!) real value is "<method 'get_contact_normal' of 'panda3d.core.CollisionEntry' objects>"
        'get_contact_pos': None, # (!) real value is "<method 'get_contact_pos' of 'panda3d.core.CollisionEntry' objects>"
        'get_from': None, # (!) real value is "<method 'get_from' of 'panda3d.core.CollisionEntry' objects>"
        'get_from_node': None, # (!) real value is "<method 'get_from_node' of 'panda3d.core.CollisionEntry' objects>"
        'get_from_node_path': None, # (!) real value is "<method 'get_from_node_path' of 'panda3d.core.CollisionEntry' objects>"
        'get_interior_point': None, # (!) real value is "<method 'get_interior_point' of 'panda3d.core.CollisionEntry' objects>"
        'get_into': None, # (!) real value is "<method 'get_into' of 'panda3d.core.CollisionEntry' objects>"
        'get_into_node': None, # (!) real value is "<method 'get_into_node' of 'panda3d.core.CollisionEntry' objects>"
        'get_into_node_path': None, # (!) real value is "<method 'get_into_node_path' of 'panda3d.core.CollisionEntry' objects>"
        'get_respect_prev_transform': None, # (!) real value is "<method 'get_respect_prev_transform' of 'panda3d.core.CollisionEntry' objects>"
        'get_surface_normal': None, # (!) real value is "<method 'get_surface_normal' of 'panda3d.core.CollisionEntry' objects>"
        'get_surface_point': None, # (!) real value is "<method 'get_surface_point' of 'panda3d.core.CollisionEntry' objects>"
        'get_t': None, # (!) real value is "<method 'get_t' of 'panda3d.core.CollisionEntry' objects>"
        'hasContactNormal': None, # (!) real value is "<method 'hasContactNormal' of 'panda3d.core.CollisionEntry' objects>"
        'hasContactPos': None, # (!) real value is "<method 'hasContactPos' of 'panda3d.core.CollisionEntry' objects>"
        'hasInteriorPoint': None, # (!) real value is "<method 'hasInteriorPoint' of 'panda3d.core.CollisionEntry' objects>"
        'hasInto': None, # (!) real value is "<method 'hasInto' of 'panda3d.core.CollisionEntry' objects>"
        'hasSurfaceNormal': None, # (!) real value is "<method 'hasSurfaceNormal' of 'panda3d.core.CollisionEntry' objects>"
        'hasSurfacePoint': None, # (!) real value is "<method 'hasSurfacePoint' of 'panda3d.core.CollisionEntry' objects>"
        'has_contact_normal': None, # (!) real value is "<method 'has_contact_normal' of 'panda3d.core.CollisionEntry' objects>"
        'has_contact_pos': None, # (!) real value is "<method 'has_contact_pos' of 'panda3d.core.CollisionEntry' objects>"
        'has_interior_point': None, # (!) real value is "<method 'has_interior_point' of 'panda3d.core.CollisionEntry' objects>"
        'has_into': None, # (!) real value is "<method 'has_into' of 'panda3d.core.CollisionEntry' objects>"
        'has_surface_normal': None, # (!) real value is "<method 'has_surface_normal' of 'panda3d.core.CollisionEntry' objects>"
        'has_surface_point': None, # (!) real value is "<method 'has_surface_point' of 'panda3d.core.CollisionEntry' objects>"
        'into_node': None, # (!) real value is "<attribute 'into_node' of 'panda3d.core.CollisionEntry' objects>"
        'into_node_path': None, # (!) real value is "<attribute 'into_node_path' of 'panda3d.core.CollisionEntry' objects>"
        'into_solid': None, # (!) real value is "<attribute 'into_solid' of 'panda3d.core.CollisionEntry' objects>"
        'output': None, # (!) real value is "<method 'output' of 'panda3d.core.CollisionEntry' objects>"
        'resetCollided': None, # (!) real value is "<method 'resetCollided' of 'panda3d.core.CollisionEntry' objects>"
        'reset_collided': None, # (!) real value is "<method 'reset_collided' of 'panda3d.core.CollisionEntry' objects>"
        'respect_prev_transform': None, # (!) real value is "<attribute 'respect_prev_transform' of 'panda3d.core.CollisionEntry' objects>"
        'setContactNormal': None, # (!) real value is "<method 'setContactNormal' of 'panda3d.core.CollisionEntry' objects>"
        'setContactPos': None, # (!) real value is "<method 'setContactPos' of 'panda3d.core.CollisionEntry' objects>"
        'setInteriorPoint': None, # (!) real value is "<method 'setInteriorPoint' of 'panda3d.core.CollisionEntry' objects>"
        'setSurfaceNormal': None, # (!) real value is "<method 'setSurfaceNormal' of 'panda3d.core.CollisionEntry' objects>"
        'setSurfacePoint': None, # (!) real value is "<method 'setSurfacePoint' of 'panda3d.core.CollisionEntry' objects>"
        'setT': None, # (!) real value is "<method 'setT' of 'panda3d.core.CollisionEntry' objects>"
        'set_contact_normal': None, # (!) real value is "<method 'set_contact_normal' of 'panda3d.core.CollisionEntry' objects>"
        'set_contact_pos': None, # (!) real value is "<method 'set_contact_pos' of 'panda3d.core.CollisionEntry' objects>"
        'set_interior_point': None, # (!) real value is "<method 'set_interior_point' of 'panda3d.core.CollisionEntry' objects>"
        'set_surface_normal': None, # (!) real value is "<method 'set_surface_normal' of 'panda3d.core.CollisionEntry' objects>"
        'set_surface_point': None, # (!) real value is "<method 'set_surface_point' of 'panda3d.core.CollisionEntry' objects>"
        'set_t': None, # (!) real value is "<method 'set_t' of 'panda3d.core.CollisionEntry' objects>"
        't': None, # (!) real value is "<attribute 't' of 'panda3d.core.CollisionEntry' objects>"
        'write': None, # (!) real value is "<method 'write' of 'panda3d.core.CollisionEntry' objects>"
    }


