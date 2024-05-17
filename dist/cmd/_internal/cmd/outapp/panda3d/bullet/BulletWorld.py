# encoding: utf-8
# module panda3d.bullet
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\bullet.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import panda3d.core as __panda3d_core


class BulletWorld(__panda3d_core.TypedReferenceCount):
    """
    /**
     *
     */
    """
    def attach(self, const_BulletWorld_self, TypedObject_object): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        attach(const BulletWorld self, TypedObject object)
        
        // AttachRemove
        
        /**
         *
         */
        """
        pass

    def attachCharacter(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        attach_character(const BulletWorld self, BulletBaseCharacterControllerNode node)
        
        /**
         * @deprecated Please use BulletWorld::attach
         */
        """
        pass

    def attachConstraint(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        attach_constraint(const BulletWorld self, BulletConstraint constraint, bool linked_collision)
        
        /**
         * Attaches a single constraint to a world.  Collision checks between the
         * linked objects will be disabled if the second parameter is set to TRUE.
         */
        """
        pass

    def attachGhost(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        attach_ghost(const BulletWorld self, BulletGhostNode node)
        
        // Deprecated methods, will be removed soon
        
        /**
         * @deprecated Please use BulletWorld::attach
         */
        """
        pass

    def attachRigidBody(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        attach_rigid_body(const BulletWorld self, BulletRigidBodyNode node)
        
        /**
         * @deprecated Please use BulletWorld::attach
         */
        """
        pass

    def attachSoftBody(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        attach_soft_body(const BulletWorld self, BulletSoftBodyNode node)
        
        /**
         * @deprecated Please use BulletWorld::attach
         */
        """
        pass

    def attachVehicle(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        attach_vehicle(const BulletWorld self, BulletVehicle vehicle)
        
        /**
         * @deprecated Please use BulletWorld::attach
         */
        """
        pass

    def attach_character(self, const_BulletWorld_self, BulletBaseCharacterControllerNode_node): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        attach_character(const BulletWorld self, BulletBaseCharacterControllerNode node)
        
        /**
         * @deprecated Please use BulletWorld::attach
         */
        """
        pass

    def attach_constraint(self, const_BulletWorld_self, BulletConstraint_constraint, bool_linked_collision): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        attach_constraint(const BulletWorld self, BulletConstraint constraint, bool linked_collision)
        
        /**
         * Attaches a single constraint to a world.  Collision checks between the
         * linked objects will be disabled if the second parameter is set to TRUE.
         */
        """
        pass

    def attach_ghost(self, const_BulletWorld_self, BulletGhostNode_node): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        attach_ghost(const BulletWorld self, BulletGhostNode node)
        
        // Deprecated methods, will be removed soon
        
        /**
         * @deprecated Please use BulletWorld::attach
         */
        """
        pass

    def attach_rigid_body(self, const_BulletWorld_self, BulletRigidBodyNode_node): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        attach_rigid_body(const BulletWorld self, BulletRigidBodyNode node)
        
        /**
         * @deprecated Please use BulletWorld::attach
         */
        """
        pass

    def attach_soft_body(self, const_BulletWorld_self, BulletSoftBodyNode_node): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        attach_soft_body(const BulletWorld self, BulletSoftBodyNode node)
        
        /**
         * @deprecated Please use BulletWorld::attach
         */
        """
        pass

    def attach_vehicle(self, const_BulletWorld_self, BulletVehicle_vehicle): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        attach_vehicle(const BulletWorld self, BulletVehicle vehicle)
        
        /**
         * @deprecated Please use BulletWorld::attach
         */
        """
        pass

    def clearContactAddedCallback(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_contact_added_callback(const BulletWorld self)
        
        /**
         *
         */
        """
        pass

    def clearDebugNode(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_debug_node(const BulletWorld self)
        
        /**
         * Removes a debug node that has been assigned to this BulletWorld.
         */
        """
        pass

    def clearFilterCallback(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_filter_callback(const BulletWorld self)
        
        /**
         *
         */
        """
        pass

    def clearTickCallback(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_tick_callback(const BulletWorld self)
        
        /**
         *
         */
        """
        pass

    def clear_contact_added_callback(self, const_BulletWorld_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_contact_added_callback(const BulletWorld self)
        
        /**
         *
         */
        """
        pass

    def clear_debug_node(self, const_BulletWorld_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_debug_node(const BulletWorld self)
        
        /**
         * Removes a debug node that has been assigned to this BulletWorld.
         */
        """
        pass

    def clear_filter_callback(self, const_BulletWorld_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_filter_callback(const BulletWorld self)
        
        /**
         *
         */
        """
        pass

    def clear_tick_callback(self, const_BulletWorld_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_tick_callback(const BulletWorld self)
        
        /**
         *
         */
        """
        pass

    def contactTest(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        contact_test(BulletWorld self, PandaNode node, bool use_filter)
        
        /**
         * Performas a test for all bodies which are currently in contact with the
         * given body.  The test returns a BulletContactResult object which may
         * contain zero, one or more contacts.
         *
         * If the optional parameter use_filter is set to TRUE this test will consider
         * filter settings.  Otherwise all objects in contact are reported, no matter
         * if they would collide or not.
         */
        """
        pass

    def contactTestPair(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        contact_test_pair(BulletWorld self, PandaNode node0, PandaNode node1)
        
        /**
         * Performas a test if the two bodies given as parameters are in contact or
         * not.  The test returns a BulletContactResult object which may contain zero
         * or one contacts.
         */
        """
        pass

    def contact_test(self, BulletWorld_self, PandaNode_node, bool_use_filter): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        contact_test(BulletWorld self, PandaNode node, bool use_filter)
        
        /**
         * Performas a test for all bodies which are currently in contact with the
         * given body.  The test returns a BulletContactResult object which may
         * contain zero, one or more contacts.
         *
         * If the optional parameter use_filter is set to TRUE this test will consider
         * filter settings.  Otherwise all objects in contact are reported, no matter
         * if they would collide or not.
         */
        """
        pass

    def contact_test_pair(self, BulletWorld_self, PandaNode_node0, PandaNode_node1): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        contact_test_pair(BulletWorld self, PandaNode node0, PandaNode node1)
        
        /**
         * Performas a test if the two bodies given as parameters are in contact or
         * not.  The test returns a BulletContactResult object which may contain zero
         * or one contacts.
         */
        """
        pass

    def doPhysics(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        do_physics(const BulletWorld self, float dt, int max_substeps, float stepsize)
        
        /**
         *
         */
        """
        pass

    def do_physics(self, const_BulletWorld_self, float_dt, int_max_substeps, float_stepsize): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        do_physics(const BulletWorld self, float dt, int max_substeps, float stepsize)
        
        /**
         *
         */
        """
        pass

    def filterTest(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        filter_test(BulletWorld self, PandaNode node0, PandaNode node1)
        
        /**
         * Performs a test if two bodies should collide or not, based on the collision
         * filter setting.
         */
        """
        pass

    def filter_test(self, BulletWorld_self, PandaNode_node0, PandaNode_node1): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        filter_test(BulletWorld self, PandaNode node0, PandaNode node1)
        
        /**
         * Performs a test if two bodies should collide or not, based on the collision
         * filter setting.
         */
        """
        pass

    def getCharacter(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_character(BulletWorld self, int idx)
        
        /**
         *
         */
        """
        pass

    def getCharacters(self, *args, **kwargs): # real signature unknown
        pass

    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getConstraint(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_constraint(BulletWorld self, int idx)
        
        /**
         *
         */
        """
        pass

    def getConstraints(self, *args, **kwargs): # real signature unknown
        pass

    def getDebugNode(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_debug_node(BulletWorld self)
        
        /**
         *
         */
        """
        pass

    def getForceUpdateAllAabbs(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_force_update_all_aabbs(BulletWorld self)
        
        /**
         *
         */
        """
        pass

    def getGhost(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_ghost(BulletWorld self, int idx)
        
        /**
         *
         */
        """
        pass

    def getGhosts(self, *args, **kwargs): # real signature unknown
        pass

    def getGravity(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_gravity(BulletWorld self)
        
        /**
         *
         */
        """
        pass

    def getGroupCollisionFlag(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_group_collision_flag(BulletWorld self, int group1, int group2)
        
        /**
         *
         */
        """
        pass

    def getManifold(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_manifold(BulletWorld self, int idx)
        
        /**
         *
         */
        """
        pass

    def GetManifold(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        __get_manifold(BulletWorld self, int idx)
        
        /**
         *
         */
        """
        pass

    def getManifolds(self, *args, **kwargs): # real signature unknown
        pass

    def getNumCharacters(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_characters(BulletWorld self)
        
        // Character controller
        
        // Character controller
        
        // Character controller
        
        /**
         *
         */
        """
        pass

    def getNumConstraints(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_constraints(BulletWorld self)
        
        // Constraint
        
        // Constraint
        
        // Constraint
        
        /**
         *
         */
        """
        pass

    def getNumGhosts(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_ghosts(BulletWorld self)
        
        // Ghost object
        
        // Ghost object
        
        // Ghost object
        
        /**
         *
         */
        """
        pass

    def getNumManifolds(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_manifolds(BulletWorld self)
        
        // Manifolds
        
        // Manifolds
        
        // Manifolds
        
        /**
         *
         */
        """
        pass

    def getNumRigidBodies(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_rigid_bodies(BulletWorld self)
        
        // Rigid body
        
        // Rigid body
        
        // Rigid body
        
        /**
         *
         */
        """
        pass

    def getNumSoftBodies(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_soft_bodies(BulletWorld self)
        
        // Soft body
        
        // Soft body
        
        // Soft body
        
        /**
         *
         */
        """
        pass

    def getNumVehicles(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_vehicles(BulletWorld self)
        
        /**
         *
         */
        """
        pass

    def getRigidBodies(self, *args, **kwargs): # real signature unknown
        pass

    def getRigidBody(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_rigid_body(BulletWorld self, int idx)
        
        /**
         *
         */
        """
        pass

    def getSoftBodies(self, *args, **kwargs): # real signature unknown
        pass

    def getSoftBody(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_soft_body(BulletWorld self, int idx)
        
        /**
         *
         */
        """
        pass

    def getVehicle(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_vehicle(BulletWorld self, int idx)
        
        /**
         *
         */
        """
        pass

    def getVehicles(self, *args, **kwargs): # real signature unknown
        pass

    def getWorldInfo(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_world_info(const BulletWorld self)
        
        /**
         *
         */
        """
        pass

    def get_character(self, BulletWorld_self, int_idx): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_character(BulletWorld self, int idx)
        
        /**
         *
         */
        """
        pass

    def get_characters(self, *args, **kwargs): # real signature unknown
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_constraint(self, BulletWorld_self, int_idx): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_constraint(BulletWorld self, int idx)
        
        /**
         *
         */
        """
        pass

    def get_constraints(self, *args, **kwargs): # real signature unknown
        pass

    def get_debug_node(self, BulletWorld_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_debug_node(BulletWorld self)
        
        /**
         *
         */
        """
        pass

    def get_force_update_all_aabbs(self, BulletWorld_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_force_update_all_aabbs(BulletWorld self)
        
        /**
         *
         */
        """
        pass

    def get_ghost(self, BulletWorld_self, int_idx): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_ghost(BulletWorld self, int idx)
        
        /**
         *
         */
        """
        pass

    def get_ghosts(self, *args, **kwargs): # real signature unknown
        pass

    def get_gravity(self, BulletWorld_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_gravity(BulletWorld self)
        
        /**
         *
         */
        """
        pass

    def get_group_collision_flag(self, BulletWorld_self, int_group1, int_group2): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_group_collision_flag(BulletWorld self, int group1, int group2)
        
        /**
         *
         */
        """
        pass

    def get_manifold(self, BulletWorld_self, int_idx): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_manifold(BulletWorld self, int idx)
        
        /**
         *
         */
        """
        pass

    def get_manifolds(self, *args, **kwargs): # real signature unknown
        pass

    def get_num_characters(self, BulletWorld_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_characters(BulletWorld self)
        
        // Character controller
        
        // Character controller
        
        // Character controller
        
        /**
         *
         */
        """
        pass

    def get_num_constraints(self, BulletWorld_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_constraints(BulletWorld self)
        
        // Constraint
        
        // Constraint
        
        // Constraint
        
        /**
         *
         */
        """
        pass

    def get_num_ghosts(self, BulletWorld_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_ghosts(BulletWorld self)
        
        // Ghost object
        
        // Ghost object
        
        // Ghost object
        
        /**
         *
         */
        """
        pass

    def get_num_manifolds(self, BulletWorld_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_manifolds(BulletWorld self)
        
        // Manifolds
        
        // Manifolds
        
        // Manifolds
        
        /**
         *
         */
        """
        pass

    def get_num_rigid_bodies(self, BulletWorld_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_rigid_bodies(BulletWorld self)
        
        // Rigid body
        
        // Rigid body
        
        // Rigid body
        
        /**
         *
         */
        """
        pass

    def get_num_soft_bodies(self, BulletWorld_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_soft_bodies(BulletWorld self)
        
        // Soft body
        
        // Soft body
        
        // Soft body
        
        /**
         *
         */
        """
        pass

    def get_num_vehicles(self, BulletWorld_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_vehicles(BulletWorld self)
        
        /**
         *
         */
        """
        pass

    def get_rigid_bodies(self, *args, **kwargs): # real signature unknown
        pass

    def get_rigid_body(self, BulletWorld_self, int_idx): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_rigid_body(BulletWorld self, int idx)
        
        /**
         *
         */
        """
        pass

    def get_soft_bodies(self, *args, **kwargs): # real signature unknown
        pass

    def get_soft_body(self, BulletWorld_self, int_idx): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_soft_body(BulletWorld self, int idx)
        
        /**
         *
         */
        """
        pass

    def get_vehicle(self, BulletWorld_self, int_idx): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_vehicle(BulletWorld self, int idx)
        
        /**
         *
         */
        """
        pass

    def get_vehicles(self, *args, **kwargs): # real signature unknown
        pass

    def get_world_info(self, const_BulletWorld_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_world_info(const BulletWorld self)
        
        /**
         *
         */
        """
        pass

    def hasDebugNode(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_debug_node(BulletWorld self)
        
        /**
         *
         */
        """
        pass

    def has_debug_node(self, BulletWorld_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_debug_node(BulletWorld self)
        
        /**
         *
         */
        """
        pass

    def rayTestAll(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        ray_test_all(BulletWorld self, const LPoint3f from_pos, const LPoint3f to_pos, const BitMask mask)
        
        /**
         *
         */
        """
        pass

    def rayTestClosest(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        ray_test_closest(BulletWorld self, const LPoint3f from_pos, const LPoint3f to_pos, const BitMask mask)
        
        // Raycast and other queries
        
        /**
         *
         */
        """
        pass

    def ray_test_all(self, BulletWorld_self, const_LPoint3f_from_pos, const_LPoint3f_to_pos, const_BitMask_mask): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        ray_test_all(BulletWorld self, const LPoint3f from_pos, const LPoint3f to_pos, const BitMask mask)
        
        /**
         *
         */
        """
        pass

    def ray_test_closest(self, BulletWorld_self, const_LPoint3f_from_pos, const_LPoint3f_to_pos, const_BitMask_mask): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        ray_test_closest(BulletWorld self, const LPoint3f from_pos, const LPoint3f to_pos, const BitMask mask)
        
        // Raycast and other queries
        
        /**
         *
         */
        """
        pass

    def remove(self, const_BulletWorld_self, TypedObject_object): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        remove(const BulletWorld self, TypedObject object)
        
        /**
         *
         */
        """
        pass

    def removeCharacter(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        remove_character(const BulletWorld self, BulletBaseCharacterControllerNode node)
        
        /**
         * @deprecated Please use BulletWorld::remove
         */
        """
        pass

    def removeConstraint(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        remove_constraint(const BulletWorld self, BulletConstraint constraint)
        
        /**
         * @deprecated Please use BulletWorld::remove
         */
        """
        pass

    def removeGhost(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        remove_ghost(const BulletWorld self, BulletGhostNode node)
        
        /**
         * @deprecated Please use BulletWorld::remove
         */
        """
        pass

    def removeRigidBody(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        remove_rigid_body(const BulletWorld self, BulletRigidBodyNode node)
        
        /**
         * @deprecated Please use BulletWorld::remove
         */
        """
        pass

    def removeSoftBody(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        remove_soft_body(const BulletWorld self, BulletSoftBodyNode node)
        
        /**
         * @deprecated Please use BulletWorld::remove
         */
        """
        pass

    def removeVehicle(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        remove_vehicle(const BulletWorld self, BulletVehicle vehicle)
        
        /**
         * @deprecated Please use BulletWorld::remove
         */
        """
        pass

    def remove_character(self, const_BulletWorld_self, BulletBaseCharacterControllerNode_node): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        remove_character(const BulletWorld self, BulletBaseCharacterControllerNode node)
        
        /**
         * @deprecated Please use BulletWorld::remove
         */
        """
        pass

    def remove_constraint(self, const_BulletWorld_self, BulletConstraint_constraint): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        remove_constraint(const BulletWorld self, BulletConstraint constraint)
        
        /**
         * @deprecated Please use BulletWorld::remove
         */
        """
        pass

    def remove_ghost(self, const_BulletWorld_self, BulletGhostNode_node): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        remove_ghost(const BulletWorld self, BulletGhostNode node)
        
        /**
         * @deprecated Please use BulletWorld::remove
         */
        """
        pass

    def remove_rigid_body(self, const_BulletWorld_self, BulletRigidBodyNode_node): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        remove_rigid_body(const BulletWorld self, BulletRigidBodyNode node)
        
        /**
         * @deprecated Please use BulletWorld::remove
         */
        """
        pass

    def remove_soft_body(self, const_BulletWorld_self, BulletSoftBodyNode_node): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        remove_soft_body(const BulletWorld self, BulletSoftBodyNode node)
        
        /**
         * @deprecated Please use BulletWorld::remove
         */
        """
        pass

    def remove_vehicle(self, const_BulletWorld_self, BulletVehicle_vehicle): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        remove_vehicle(const BulletWorld self, BulletVehicle vehicle)
        
        /**
         * @deprecated Please use BulletWorld::remove
         */
        """
        pass

    def setContactAddedCallback(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_contact_added_callback(const BulletWorld self, CallbackObject obj)
        
        // Callbacks
        
        /**
         *
         */
        """
        pass

    def setDebugNode(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_debug_node(const BulletWorld self, BulletDebugNode node)
        
        // Debug
        
        // Debug
        
        /**
         *
         */
        """
        pass

    def setFilterCallback(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_filter_callback(const BulletWorld self, CallbackObject obj)
        
        /**
         *
         */
        """
        pass

    def setForceUpdateAllAabbs(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_force_update_all_aabbs(const BulletWorld self, bool force)
        
        /**
         *
         */
        """
        pass

    def setGravity(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_gravity(const BulletWorld self, const LVector3f gravity)
        set_gravity(const BulletWorld self, float gx, float gy, float gz)
        
        /**
         *
         */
        
        /**
         *
         */
        """
        pass

    def setGroupCollisionFlag(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_group_collision_flag(const BulletWorld self, int group1, int group2, bool enable)
        
        // Collision filtering
        
        /**
         *
         */
        """
        pass

    def setTickCallback(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_tick_callback(const BulletWorld self, CallbackObject obj, bool is_pretick)
        
        /**
         *
         */
        """
        pass

    def set_contact_added_callback(self, const_BulletWorld_self, CallbackObject_obj): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_contact_added_callback(const BulletWorld self, CallbackObject obj)
        
        // Callbacks
        
        /**
         *
         */
        """
        pass

    def set_debug_node(self, const_BulletWorld_self, BulletDebugNode_node): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_debug_node(const BulletWorld self, BulletDebugNode node)
        
        // Debug
        
        // Debug
        
        /**
         *
         */
        """
        pass

    def set_filter_callback(self, const_BulletWorld_self, CallbackObject_obj): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_filter_callback(const BulletWorld self, CallbackObject obj)
        
        /**
         *
         */
        """
        pass

    def set_force_update_all_aabbs(self, const_BulletWorld_self, bool_force): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_force_update_all_aabbs(const BulletWorld self, bool force)
        
        /**
         *
         */
        """
        pass

    def set_gravity(self, const_BulletWorld_self, const_LVector3f_gravity): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_gravity(const BulletWorld self, const LVector3f gravity)
        set_gravity(const BulletWorld self, float gx, float gy, float gz)
        
        /**
         *
         */
        
        /**
         *
         */
        """
        pass

    def set_group_collision_flag(self, const_BulletWorld_self, int_group1, int_group2, bool_enable): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_group_collision_flag(const BulletWorld self, int group1, int group2, bool enable)
        
        // Collision filtering
        
        /**
         *
         */
        """
        pass

    def set_tick_callback(self, const_BulletWorld_self, CallbackObject_obj, bool_is_pretick): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_tick_callback(const BulletWorld self, CallbackObject obj, bool is_pretick)
        
        /**
         *
         */
        """
        pass

    def sweepTestClosest(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        sweep_test_closest(BulletWorld self, BulletShape shape, const TransformState from_ts, const TransformState to_ts, const BitMask mask, float penetration)
        
        /**
         * Performs a sweep test against all other shapes that match the given group
         * mask.  The provided shape must be a convex shape; it is an error to invoke
         * this method using a non-convex shape.
         */
        """
        pass

    def sweep_test_closest(self, BulletWorld_self, BulletShape_shape, const_TransformState_from_ts, const_TransformState_to_ts, const_BitMask_mask, float_penetration): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        sweep_test_closest(BulletWorld self, BulletShape shape, const TransformState from_ts, const TransformState to_ts, const BitMask mask, float penetration)
        
        /**
         * Performs a sweep test against all other shapes that match the given group
         * mask.  The provided shape must be a convex shape; it is an error to invoke
         * this method using a non-convex shape.
         */
        """
        pass

    def __get_manifold(self, BulletWorld_self, int_idx): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        __get_manifold(BulletWorld self, int idx)
        
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

    characters = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    constraints = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    debug_node = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    force_update_all_aabbs = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ghosts = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    gravity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    manifolds = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    rigid_bodies = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    soft_bodies = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    vehicles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    world_info = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    BADynamicAabbTree = 1
    BASweepAndPrune = 0
    BA_dynamic_aabb_tree = 1
    BA_sweep_and_prune = 0
    DtoolClassDict = {
        'BADynamicAabbTree': 1,
        'BASweepAndPrune': 0,
        'BA_dynamic_aabb_tree': 1,
        'BA_sweep_and_prune': 0,
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        'FACallback': 2,
        'FAGroupsMask': 1,
        'FAMask': 0,
        'FA_callback': 2,
        'FA_groups_mask': 1,
        'FA_mask': 0,
        'GetManifold': None, # (!) real value is "<method 'GetManifold' of 'panda3d.bullet.BulletWorld' objects>"
        '__doc__': '/**\n *\n */',
        '__get_manifold': None, # (!) real value is "<method '__get_manifold' of 'panda3d.bullet.BulletWorld' objects>"
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.bullet.BulletWorld' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFDC68CF6F0>'
        'attach': None, # (!) real value is "<method 'attach' of 'panda3d.bullet.BulletWorld' objects>"
        'attachCharacter': None, # (!) real value is "<method 'attachCharacter' of 'panda3d.bullet.BulletWorld' objects>"
        'attachConstraint': None, # (!) real value is "<method 'attachConstraint' of 'panda3d.bullet.BulletWorld' objects>"
        'attachGhost': None, # (!) real value is "<method 'attachGhost' of 'panda3d.bullet.BulletWorld' objects>"
        'attachRigidBody': None, # (!) real value is "<method 'attachRigidBody' of 'panda3d.bullet.BulletWorld' objects>"
        'attachSoftBody': None, # (!) real value is "<method 'attachSoftBody' of 'panda3d.bullet.BulletWorld' objects>"
        'attachVehicle': None, # (!) real value is "<method 'attachVehicle' of 'panda3d.bullet.BulletWorld' objects>"
        'attach_character': None, # (!) real value is "<method 'attach_character' of 'panda3d.bullet.BulletWorld' objects>"
        'attach_constraint': None, # (!) real value is "<method 'attach_constraint' of 'panda3d.bullet.BulletWorld' objects>"
        'attach_ghost': None, # (!) real value is "<method 'attach_ghost' of 'panda3d.bullet.BulletWorld' objects>"
        'attach_rigid_body': None, # (!) real value is "<method 'attach_rigid_body' of 'panda3d.bullet.BulletWorld' objects>"
        'attach_soft_body': None, # (!) real value is "<method 'attach_soft_body' of 'panda3d.bullet.BulletWorld' objects>"
        'attach_vehicle': None, # (!) real value is "<method 'attach_vehicle' of 'panda3d.bullet.BulletWorld' objects>"
        'characters': None, # (!) real value is "<attribute 'characters' of 'panda3d.bullet.BulletWorld' objects>"
        'clearContactAddedCallback': None, # (!) real value is "<method 'clearContactAddedCallback' of 'panda3d.bullet.BulletWorld' objects>"
        'clearDebugNode': None, # (!) real value is "<method 'clearDebugNode' of 'panda3d.bullet.BulletWorld' objects>"
        'clearFilterCallback': None, # (!) real value is "<method 'clearFilterCallback' of 'panda3d.bullet.BulletWorld' objects>"
        'clearTickCallback': None, # (!) real value is "<method 'clearTickCallback' of 'panda3d.bullet.BulletWorld' objects>"
        'clear_contact_added_callback': None, # (!) real value is "<method 'clear_contact_added_callback' of 'panda3d.bullet.BulletWorld' objects>"
        'clear_debug_node': None, # (!) real value is "<method 'clear_debug_node' of 'panda3d.bullet.BulletWorld' objects>"
        'clear_filter_callback': None, # (!) real value is "<method 'clear_filter_callback' of 'panda3d.bullet.BulletWorld' objects>"
        'clear_tick_callback': None, # (!) real value is "<method 'clear_tick_callback' of 'panda3d.bullet.BulletWorld' objects>"
        'constraints': None, # (!) real value is "<attribute 'constraints' of 'panda3d.bullet.BulletWorld' objects>"
        'contactTest': None, # (!) real value is "<method 'contactTest' of 'panda3d.bullet.BulletWorld' objects>"
        'contactTestPair': None, # (!) real value is "<method 'contactTestPair' of 'panda3d.bullet.BulletWorld' objects>"
        'contact_test': None, # (!) real value is "<method 'contact_test' of 'panda3d.bullet.BulletWorld' objects>"
        'contact_test_pair': None, # (!) real value is "<method 'contact_test_pair' of 'panda3d.bullet.BulletWorld' objects>"
        'debug_node': None, # (!) real value is "<attribute 'debug_node' of 'panda3d.bullet.BulletWorld' objects>"
        'doPhysics': None, # (!) real value is "<method 'doPhysics' of 'panda3d.bullet.BulletWorld' objects>"
        'do_physics': None, # (!) real value is "<method 'do_physics' of 'panda3d.bullet.BulletWorld' objects>"
        'filterTest': None, # (!) real value is "<method 'filterTest' of 'panda3d.bullet.BulletWorld' objects>"
        'filter_test': None, # (!) real value is "<method 'filter_test' of 'panda3d.bullet.BulletWorld' objects>"
        'force_update_all_aabbs': None, # (!) real value is "<attribute 'force_update_all_aabbs' of 'panda3d.bullet.BulletWorld' objects>"
        'getCharacter': None, # (!) real value is "<method 'getCharacter' of 'panda3d.bullet.BulletWorld' objects>"
        'getCharacters': None, # (!) real value is "<method 'getCharacters' of 'panda3d.bullet.BulletWorld' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFDC68CF6F0>)>'
        'getConstraint': None, # (!) real value is "<method 'getConstraint' of 'panda3d.bullet.BulletWorld' objects>"
        'getConstraints': None, # (!) real value is "<method 'getConstraints' of 'panda3d.bullet.BulletWorld' objects>"
        'getDebugNode': None, # (!) real value is "<method 'getDebugNode' of 'panda3d.bullet.BulletWorld' objects>"
        'getForceUpdateAllAabbs': None, # (!) real value is "<method 'getForceUpdateAllAabbs' of 'panda3d.bullet.BulletWorld' objects>"
        'getGhost': None, # (!) real value is "<method 'getGhost' of 'panda3d.bullet.BulletWorld' objects>"
        'getGhosts': None, # (!) real value is "<method 'getGhosts' of 'panda3d.bullet.BulletWorld' objects>"
        'getGravity': None, # (!) real value is "<method 'getGravity' of 'panda3d.bullet.BulletWorld' objects>"
        'getGroupCollisionFlag': None, # (!) real value is "<method 'getGroupCollisionFlag' of 'panda3d.bullet.BulletWorld' objects>"
        'getManifold': None, # (!) real value is "<method 'getManifold' of 'panda3d.bullet.BulletWorld' objects>"
        'getManifolds': None, # (!) real value is "<method 'getManifolds' of 'panda3d.bullet.BulletWorld' objects>"
        'getNumCharacters': None, # (!) real value is "<method 'getNumCharacters' of 'panda3d.bullet.BulletWorld' objects>"
        'getNumConstraints': None, # (!) real value is "<method 'getNumConstraints' of 'panda3d.bullet.BulletWorld' objects>"
        'getNumGhosts': None, # (!) real value is "<method 'getNumGhosts' of 'panda3d.bullet.BulletWorld' objects>"
        'getNumManifolds': None, # (!) real value is "<method 'getNumManifolds' of 'panda3d.bullet.BulletWorld' objects>"
        'getNumRigidBodies': None, # (!) real value is "<method 'getNumRigidBodies' of 'panda3d.bullet.BulletWorld' objects>"
        'getNumSoftBodies': None, # (!) real value is "<method 'getNumSoftBodies' of 'panda3d.bullet.BulletWorld' objects>"
        'getNumVehicles': None, # (!) real value is "<method 'getNumVehicles' of 'panda3d.bullet.BulletWorld' objects>"
        'getRigidBodies': None, # (!) real value is "<method 'getRigidBodies' of 'panda3d.bullet.BulletWorld' objects>"
        'getRigidBody': None, # (!) real value is "<method 'getRigidBody' of 'panda3d.bullet.BulletWorld' objects>"
        'getSoftBodies': None, # (!) real value is "<method 'getSoftBodies' of 'panda3d.bullet.BulletWorld' objects>"
        'getSoftBody': None, # (!) real value is "<method 'getSoftBody' of 'panda3d.bullet.BulletWorld' objects>"
        'getVehicle': None, # (!) real value is "<method 'getVehicle' of 'panda3d.bullet.BulletWorld' objects>"
        'getVehicles': None, # (!) real value is "<method 'getVehicles' of 'panda3d.bullet.BulletWorld' objects>"
        'getWorldInfo': None, # (!) real value is "<method 'getWorldInfo' of 'panda3d.bullet.BulletWorld' objects>"
        'get_character': None, # (!) real value is "<method 'get_character' of 'panda3d.bullet.BulletWorld' objects>"
        'get_characters': None, # (!) real value is "<method 'get_characters' of 'panda3d.bullet.BulletWorld' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFDC68CF6F0>)>'
        'get_constraint': None, # (!) real value is "<method 'get_constraint' of 'panda3d.bullet.BulletWorld' objects>"
        'get_constraints': None, # (!) real value is "<method 'get_constraints' of 'panda3d.bullet.BulletWorld' objects>"
        'get_debug_node': None, # (!) real value is "<method 'get_debug_node' of 'panda3d.bullet.BulletWorld' objects>"
        'get_force_update_all_aabbs': None, # (!) real value is "<method 'get_force_update_all_aabbs' of 'panda3d.bullet.BulletWorld' objects>"
        'get_ghost': None, # (!) real value is "<method 'get_ghost' of 'panda3d.bullet.BulletWorld' objects>"
        'get_ghosts': None, # (!) real value is "<method 'get_ghosts' of 'panda3d.bullet.BulletWorld' objects>"
        'get_gravity': None, # (!) real value is "<method 'get_gravity' of 'panda3d.bullet.BulletWorld' objects>"
        'get_group_collision_flag': None, # (!) real value is "<method 'get_group_collision_flag' of 'panda3d.bullet.BulletWorld' objects>"
        'get_manifold': None, # (!) real value is "<method 'get_manifold' of 'panda3d.bullet.BulletWorld' objects>"
        'get_manifolds': None, # (!) real value is "<method 'get_manifolds' of 'panda3d.bullet.BulletWorld' objects>"
        'get_num_characters': None, # (!) real value is "<method 'get_num_characters' of 'panda3d.bullet.BulletWorld' objects>"
        'get_num_constraints': None, # (!) real value is "<method 'get_num_constraints' of 'panda3d.bullet.BulletWorld' objects>"
        'get_num_ghosts': None, # (!) real value is "<method 'get_num_ghosts' of 'panda3d.bullet.BulletWorld' objects>"
        'get_num_manifolds': None, # (!) real value is "<method 'get_num_manifolds' of 'panda3d.bullet.BulletWorld' objects>"
        'get_num_rigid_bodies': None, # (!) real value is "<method 'get_num_rigid_bodies' of 'panda3d.bullet.BulletWorld' objects>"
        'get_num_soft_bodies': None, # (!) real value is "<method 'get_num_soft_bodies' of 'panda3d.bullet.BulletWorld' objects>"
        'get_num_vehicles': None, # (!) real value is "<method 'get_num_vehicles' of 'panda3d.bullet.BulletWorld' objects>"
        'get_rigid_bodies': None, # (!) real value is "<method 'get_rigid_bodies' of 'panda3d.bullet.BulletWorld' objects>"
        'get_rigid_body': None, # (!) real value is "<method 'get_rigid_body' of 'panda3d.bullet.BulletWorld' objects>"
        'get_soft_bodies': None, # (!) real value is "<method 'get_soft_bodies' of 'panda3d.bullet.BulletWorld' objects>"
        'get_soft_body': None, # (!) real value is "<method 'get_soft_body' of 'panda3d.bullet.BulletWorld' objects>"
        'get_vehicle': None, # (!) real value is "<method 'get_vehicle' of 'panda3d.bullet.BulletWorld' objects>"
        'get_vehicles': None, # (!) real value is "<method 'get_vehicles' of 'panda3d.bullet.BulletWorld' objects>"
        'get_world_info': None, # (!) real value is "<method 'get_world_info' of 'panda3d.bullet.BulletWorld' objects>"
        'ghosts': None, # (!) real value is "<attribute 'ghosts' of 'panda3d.bullet.BulletWorld' objects>"
        'gravity': None, # (!) real value is "<attribute 'gravity' of 'panda3d.bullet.BulletWorld' objects>"
        'hasDebugNode': None, # (!) real value is "<method 'hasDebugNode' of 'panda3d.bullet.BulletWorld' objects>"
        'has_debug_node': None, # (!) real value is "<method 'has_debug_node' of 'panda3d.bullet.BulletWorld' objects>"
        'manifolds': None, # (!) real value is "<attribute 'manifolds' of 'panda3d.bullet.BulletWorld' objects>"
        'rayTestAll': None, # (!) real value is "<method 'rayTestAll' of 'panda3d.bullet.BulletWorld' objects>"
        'rayTestClosest': None, # (!) real value is "<method 'rayTestClosest' of 'panda3d.bullet.BulletWorld' objects>"
        'ray_test_all': None, # (!) real value is "<method 'ray_test_all' of 'panda3d.bullet.BulletWorld' objects>"
        'ray_test_closest': None, # (!) real value is "<method 'ray_test_closest' of 'panda3d.bullet.BulletWorld' objects>"
        'remove': None, # (!) real value is "<method 'remove' of 'panda3d.bullet.BulletWorld' objects>"
        'removeCharacter': None, # (!) real value is "<method 'removeCharacter' of 'panda3d.bullet.BulletWorld' objects>"
        'removeConstraint': None, # (!) real value is "<method 'removeConstraint' of 'panda3d.bullet.BulletWorld' objects>"
        'removeGhost': None, # (!) real value is "<method 'removeGhost' of 'panda3d.bullet.BulletWorld' objects>"
        'removeRigidBody': None, # (!) real value is "<method 'removeRigidBody' of 'panda3d.bullet.BulletWorld' objects>"
        'removeSoftBody': None, # (!) real value is "<method 'removeSoftBody' of 'panda3d.bullet.BulletWorld' objects>"
        'removeVehicle': None, # (!) real value is "<method 'removeVehicle' of 'panda3d.bullet.BulletWorld' objects>"
        'remove_character': None, # (!) real value is "<method 'remove_character' of 'panda3d.bullet.BulletWorld' objects>"
        'remove_constraint': None, # (!) real value is "<method 'remove_constraint' of 'panda3d.bullet.BulletWorld' objects>"
        'remove_ghost': None, # (!) real value is "<method 'remove_ghost' of 'panda3d.bullet.BulletWorld' objects>"
        'remove_rigid_body': None, # (!) real value is "<method 'remove_rigid_body' of 'panda3d.bullet.BulletWorld' objects>"
        'remove_soft_body': None, # (!) real value is "<method 'remove_soft_body' of 'panda3d.bullet.BulletWorld' objects>"
        'remove_vehicle': None, # (!) real value is "<method 'remove_vehicle' of 'panda3d.bullet.BulletWorld' objects>"
        'rigid_bodies': None, # (!) real value is "<attribute 'rigid_bodies' of 'panda3d.bullet.BulletWorld' objects>"
        'setContactAddedCallback': None, # (!) real value is "<method 'setContactAddedCallback' of 'panda3d.bullet.BulletWorld' objects>"
        'setDebugNode': None, # (!) real value is "<method 'setDebugNode' of 'panda3d.bullet.BulletWorld' objects>"
        'setFilterCallback': None, # (!) real value is "<method 'setFilterCallback' of 'panda3d.bullet.BulletWorld' objects>"
        'setForceUpdateAllAabbs': None, # (!) real value is "<method 'setForceUpdateAllAabbs' of 'panda3d.bullet.BulletWorld' objects>"
        'setGravity': None, # (!) real value is "<method 'setGravity' of 'panda3d.bullet.BulletWorld' objects>"
        'setGroupCollisionFlag': None, # (!) real value is "<method 'setGroupCollisionFlag' of 'panda3d.bullet.BulletWorld' objects>"
        'setTickCallback': None, # (!) real value is "<method 'setTickCallback' of 'panda3d.bullet.BulletWorld' objects>"
        'set_contact_added_callback': None, # (!) real value is "<method 'set_contact_added_callback' of 'panda3d.bullet.BulletWorld' objects>"
        'set_debug_node': None, # (!) real value is "<method 'set_debug_node' of 'panda3d.bullet.BulletWorld' objects>"
        'set_filter_callback': None, # (!) real value is "<method 'set_filter_callback' of 'panda3d.bullet.BulletWorld' objects>"
        'set_force_update_all_aabbs': None, # (!) real value is "<method 'set_force_update_all_aabbs' of 'panda3d.bullet.BulletWorld' objects>"
        'set_gravity': None, # (!) real value is "<method 'set_gravity' of 'panda3d.bullet.BulletWorld' objects>"
        'set_group_collision_flag': None, # (!) real value is "<method 'set_group_collision_flag' of 'panda3d.bullet.BulletWorld' objects>"
        'set_tick_callback': None, # (!) real value is "<method 'set_tick_callback' of 'panda3d.bullet.BulletWorld' objects>"
        'soft_bodies': None, # (!) real value is "<attribute 'soft_bodies' of 'panda3d.bullet.BulletWorld' objects>"
        'sweepTestClosest': None, # (!) real value is "<method 'sweepTestClosest' of 'panda3d.bullet.BulletWorld' objects>"
        'sweep_test_closest': None, # (!) real value is "<method 'sweep_test_closest' of 'panda3d.bullet.BulletWorld' objects>"
        'vehicles': None, # (!) real value is "<attribute 'vehicles' of 'panda3d.bullet.BulletWorld' objects>"
        'world_info': None, # (!) real value is "<attribute 'world_info' of 'panda3d.bullet.BulletWorld' objects>"
    }
    FACallback = 2
    FAGroupsMask = 1
    FAMask = 0
    FA_callback = 2
    FA_groups_mask = 1
    FA_mask = 0


