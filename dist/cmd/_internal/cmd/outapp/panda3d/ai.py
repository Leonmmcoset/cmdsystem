# encoding: utf-8
# module panda3d.ai
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\ai.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import panda3d.core as __panda3d_core


# Variables with simple values

Dtool_PyNativeInterface = 1

# functions

def Dtool_BorrowThisReference(*args, **kwargs): # real signature unknown
    """
    Used to borrow 'this' pointer (to, from)
    Assumes no ownership.
    """
    pass

# classes

class AIBehaviors(__dtoolconfig.DTOOL_SUPER_BASE):
    """
    /**
     * This class implements all the steering behaviors of the AI framework, such
     * as seek, flee, pursue, evade, wander and flock.  Each steering behavior has
     * a weight which is used when more than one type of steering behavior is
     * acting on the same ai character.  The weight decides the contribution of
     * each type of steering behavior.  The AICharacter class has a handle to an
     * object of this class and this allows to invoke the steering behaviors via
     * the AICharacter.  This class also provides functionality such as pausing,
     * resuming and removing the AI behaviors of an AI character at anytime.
     */
    """
    def addDynamicObstacle(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_dynamic_obstacle(const AIBehaviors self, NodePath obstacle)
        
        /**
         * This function starts the pathfinding obstacle navigation for the passed in
         * obstacle.
         */
        """
        pass

    def addStaticObstacle(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_static_obstacle(const AIBehaviors self, NodePath obstacle)
        
        /**
         * This function allows the user to dynamically add obstacles to the game
         * environment.  The function will update the nodes within the bounding volume
         * of the obstacle as non-traversable.  Hence will not be considered by the
         * pathfinding algorithm.
         */
        """
        pass

    def addToPath(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_to_path(const AIBehaviors self, LVecBase3f pos)
        
        /**
         * This function adds positions to the path to follow.
         */
        """
        pass

    def add_dynamic_obstacle(self, const_AIBehaviors_self, NodePath_obstacle): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_dynamic_obstacle(const AIBehaviors self, NodePath obstacle)
        
        /**
         * This function starts the pathfinding obstacle navigation for the passed in
         * obstacle.
         */
        """
        pass

    def add_static_obstacle(self, const_AIBehaviors_self, NodePath_obstacle): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_static_obstacle(const AIBehaviors self, NodePath obstacle)
        
        /**
         * This function allows the user to dynamically add obstacles to the game
         * environment.  The function will update the nodes within the bounding volume
         * of the obstacle as non-traversable.  Hence will not be considered by the
         * pathfinding algorithm.
         */
        """
        pass

    def add_to_path(self, const_AIBehaviors_self, LVecBase3f_pos): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_to_path(const AIBehaviors self, LVecBase3f pos)
        
        /**
         * This function adds positions to the path to follow.
         */
        """
        pass

    def arrival(self, const_AIBehaviors_self, double_distance): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        arrival(const AIBehaviors self, double distance)
        
        /**
         * This function activates arrival.  This is the function we want the user to
         * call for arrival to be done.
         */
        """
        pass

    def behaviorStatus(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        behavior_status(const AIBehaviors self, str ai_type)
        
        /**
         * This function returns the status of an AI Type whether it is active, paused
         * or disabled.  It returns -1 if an invalid string is passed.
         */
        """
        pass

    def behavior_status(self, const_AIBehaviors_self, str_ai_type): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        behavior_status(const AIBehaviors self, str ai_type)
        
        /**
         * This function returns the status of an AI Type whether it is active, paused
         * or disabled.  It returns -1 if an invalid string is passed.
         */
        """
        pass

    def evade(self, const_AIBehaviors_self, NodePath_target_object, double_panic_distance, double_relax_distance, float_evade_wt): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        evade(const AIBehaviors self, NodePath target_object, double panic_distance, double relax_distance, float evade_wt)
        
        /**
         * This function activates evade_activate.
         */
        """
        pass

    def flee(self, const_AIBehaviors_self, LVecBase3f_pos, double_panic_distance, double_relax_distance, float_flee_wt): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        flee(const AIBehaviors self, LVecBase3f pos, double panic_distance, double relax_distance, float flee_wt)
        flee(const AIBehaviors self, NodePath target_object, double panic_distance, double relax_distance, float flee_wt)
        
        /**
         * This function activates flee_activate and creates an object of the Flee
         * class.  This function is overloaded to accept a NodePath or an LVecBase3.
         */
        """
        pass

    def flock(self, const_AIBehaviors_self, float_flock_wt): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        flock(const AIBehaviors self, float flock_wt)
        
        /**
         * This function activates flock.  This is the function we want the user to
         * call for flock to be done.
         */
        """
        pass

    def initPathFind(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        init_path_find(const AIBehaviors self, str navmesh_filename)
        
        // should have different function names.
        
        /**
         * This function activates path finding in the character.  This function
         * accepts the meshdata in .csv format.
         *
         */
        """
        pass

    def init_path_find(self, const_AIBehaviors_self, str_navmesh_filename): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        init_path_find(const AIBehaviors self, str navmesh_filename)
        
        // should have different function names.
        
        /**
         * This function activates path finding in the character.  This function
         * accepts the meshdata in .csv format.
         *
         */
        """
        pass

    def obstacleAvoidance(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        obstacle_avoidance(const AIBehaviors self, float feeler_length)
        
        /**
         * This function activates obstacle avoidance for a given character.  This is
         * the function we want the user to call for obstacle avoidance to be
         * performed.
         */
        """
        pass

    def obstacle_avoidance(self, const_AIBehaviors_self, float_feeler_length): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        obstacle_avoidance(const AIBehaviors self, float feeler_length)
        
        /**
         * This function activates obstacle avoidance for a given character.  This is
         * the function we want the user to call for obstacle avoidance to be
         * performed.
         */
        """
        pass

    def pathFindTo(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        path_find_to(const AIBehaviors self, NodePath target, str type)
        
        /**
         * This function checks for the source and target in the navigation mesh for
         * its availability and then finds the best path via the A* algorithm Then it
         * calls the path follower to make the object follow the path.
         */
        
        /**
         * This function checks for the source and target in the navigation mesh for
         * its availability and then finds the best path via the A* algorithm Then it
         * calls the path follower to make the object follow the path.
         */
        """
        pass

    def pathFollow(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        path_follow(const AIBehaviors self, float follow_wt)
        
        /**
         * This function activates path following.  This is the function we want the
         * user to call for path following.
         */
        """
        pass

    def path_find_to(self, const_AIBehaviors_self, NodePath_target, str_type): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        path_find_to(const AIBehaviors self, NodePath target, str type)
        
        /**
         * This function checks for the source and target in the navigation mesh for
         * its availability and then finds the best path via the A* algorithm Then it
         * calls the path follower to make the object follow the path.
         */
        
        /**
         * This function checks for the source and target in the navigation mesh for
         * its availability and then finds the best path via the A* algorithm Then it
         * calls the path follower to make the object follow the path.
         */
        """
        pass

    def path_follow(self, const_AIBehaviors_self, float_follow_wt): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        path_follow(const AIBehaviors self, float follow_wt)
        
        /**
         * This function activates path following.  This is the function we want the
         * user to call for path following.
         */
        """
        pass

    def pauseAi(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        pause_ai(const AIBehaviors self, str ai_type)
        
        /**
         * This function pauses individual or all the AIs.
         */
        """
        pass

    def pause_ai(self, const_AIBehaviors_self, str_ai_type): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        pause_ai(const AIBehaviors self, str ai_type)
        
        /**
         * This function pauses individual or all the AIs.
         */
        """
        pass

    def pursue(self, const_AIBehaviors_self, NodePath_target_object, float_pursue_wt): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        pursue(const AIBehaviors self, NodePath target_object, float pursue_wt)
        
        /**
         * This function activates pursue.  This is the function we want the user to
         * call for pursue to be done.
         */
        """
        pass

    def removeAi(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        remove_ai(const AIBehaviors self, str ai_type)
        
        /**
         * This function removes individual or all the AIs.
         */
        """
        pass

    def remove_ai(self, const_AIBehaviors_self, str_ai_type): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        remove_ai(const AIBehaviors self, str ai_type)
        
        /**
         * This function removes individual or all the AIs.
         */
        """
        pass

    def resumeAi(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        resume_ai(const AIBehaviors self, str ai_type)
        
        /**
         * This function resumes individual or all the AIs
         */
        """
        pass

    def resume_ai(self, const_AIBehaviors_self, str_ai_type): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        resume_ai(const AIBehaviors self, str ai_type)
        
        /**
         * This function resumes individual or all the AIs
         */
        """
        pass

    def seek(self, const_AIBehaviors_self, NodePath_target_object, float_seek_wt): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        seek(const AIBehaviors self, NodePath target_object, float seek_wt)
        
        /**
         * This function activates seek and makes an object of the Seek class.  This
         * is the function we want the user to call for seek to be done.  This
         * function is overloaded to accept a NodePath or an LVecBase3.
         */
        """
        pass

    def startFollow(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        start_follow(const AIBehaviors self, str type)
        """
        pass

    def start_follow(self, const_AIBehaviors_self, str_type): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        start_follow(const AIBehaviors self, str type)
        """
        pass

    def wander(self, const_AIBehaviors_self, double_wander_radius, int_flag, double_aoe, float_wander_weight): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        wander(const AIBehaviors self, double wander_radius, int flag, double aoe, float wander_weight)
        
        /**
         * This function activates wander.  This is the function we want the user to
         * call for flock to be done.
         */
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
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.ai.AIBehaviors' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.ai.AIBehaviors' objects>"
        '__doc__': '/**\n * This class implements all the steering behaviors of the AI framework, such\n * as seek, flee, pursue, evade, wander and flock.  Each steering behavior has\n * a weight which is used when more than one type of steering behavior is\n * acting on the same ai character.  The weight decides the contribution of\n * each type of steering behavior.  The AICharacter class has a handle to an\n * object of this class and this allows to invoke the steering behaviors via\n * the AICharacter.  This class also provides functionality such as pausing,\n * resuming and removing the AI behaviors of an AI character at anytime.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.ai.AIBehaviors' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFDE5664580>'
        'addDynamicObstacle': None, # (!) real value is "<method 'addDynamicObstacle' of 'panda3d.ai.AIBehaviors' objects>"
        'addStaticObstacle': None, # (!) real value is "<method 'addStaticObstacle' of 'panda3d.ai.AIBehaviors' objects>"
        'addToPath': None, # (!) real value is "<method 'addToPath' of 'panda3d.ai.AIBehaviors' objects>"
        'add_dynamic_obstacle': None, # (!) real value is "<method 'add_dynamic_obstacle' of 'panda3d.ai.AIBehaviors' objects>"
        'add_static_obstacle': None, # (!) real value is "<method 'add_static_obstacle' of 'panda3d.ai.AIBehaviors' objects>"
        'add_to_path': None, # (!) real value is "<method 'add_to_path' of 'panda3d.ai.AIBehaviors' objects>"
        'arrival': None, # (!) real value is "<method 'arrival' of 'panda3d.ai.AIBehaviors' objects>"
        'behaviorStatus': None, # (!) real value is "<method 'behaviorStatus' of 'panda3d.ai.AIBehaviors' objects>"
        'behavior_status': None, # (!) real value is "<method 'behavior_status' of 'panda3d.ai.AIBehaviors' objects>"
        'evade': None, # (!) real value is "<method 'evade' of 'panda3d.ai.AIBehaviors' objects>"
        'flee': None, # (!) real value is "<method 'flee' of 'panda3d.ai.AIBehaviors' objects>"
        'flock': None, # (!) real value is "<method 'flock' of 'panda3d.ai.AIBehaviors' objects>"
        'initPathFind': None, # (!) real value is "<method 'initPathFind' of 'panda3d.ai.AIBehaviors' objects>"
        'init_path_find': None, # (!) real value is "<method 'init_path_find' of 'panda3d.ai.AIBehaviors' objects>"
        'obstacleAvoidance': None, # (!) real value is "<method 'obstacleAvoidance' of 'panda3d.ai.AIBehaviors' objects>"
        'obstacle_avoidance': None, # (!) real value is "<method 'obstacle_avoidance' of 'panda3d.ai.AIBehaviors' objects>"
        'pathFindTo': None, # (!) real value is "<method 'pathFindTo' of 'panda3d.ai.AIBehaviors' objects>"
        'pathFollow': None, # (!) real value is "<method 'pathFollow' of 'panda3d.ai.AIBehaviors' objects>"
        'path_find_to': None, # (!) real value is "<method 'path_find_to' of 'panda3d.ai.AIBehaviors' objects>"
        'path_follow': None, # (!) real value is "<method 'path_follow' of 'panda3d.ai.AIBehaviors' objects>"
        'pauseAi': None, # (!) real value is "<method 'pauseAi' of 'panda3d.ai.AIBehaviors' objects>"
        'pause_ai': None, # (!) real value is "<method 'pause_ai' of 'panda3d.ai.AIBehaviors' objects>"
        'pursue': None, # (!) real value is "<method 'pursue' of 'panda3d.ai.AIBehaviors' objects>"
        'removeAi': None, # (!) real value is "<method 'removeAi' of 'panda3d.ai.AIBehaviors' objects>"
        'remove_ai': None, # (!) real value is "<method 'remove_ai' of 'panda3d.ai.AIBehaviors' objects>"
        'resumeAi': None, # (!) real value is "<method 'resumeAi' of 'panda3d.ai.AIBehaviors' objects>"
        'resume_ai': None, # (!) real value is "<method 'resume_ai' of 'panda3d.ai.AIBehaviors' objects>"
        'seek': None, # (!) real value is "<method 'seek' of 'panda3d.ai.AIBehaviors' objects>"
        'startFollow': None, # (!) real value is "<method 'startFollow' of 'panda3d.ai.AIBehaviors' objects>"
        'start_follow': None, # (!) real value is "<method 'start_follow' of 'panda3d.ai.AIBehaviors' objects>"
        'wander': None, # (!) real value is "<method 'wander' of 'panda3d.ai.AIBehaviors' objects>"
    }


class AICharacter(__panda3d_core.ReferenceCount):
    # no doc
    def getAiBehaviors(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_ai_behaviors(const AICharacter self)
        """
        pass

    def getMass(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_mass(const AICharacter self)
        """
        pass

    def getMaxForce(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_max_force(const AICharacter self)
        """
        pass

    def getNodePath(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_node_path(const AICharacter self)
        """
        pass

    def getVelocity(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_velocity(const AICharacter self)
        """
        pass

    def get_ai_behaviors(self, const_AICharacter_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_ai_behaviors(const AICharacter self)
        """
        pass

    def get_mass(self, const_AICharacter_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_mass(const AICharacter self)
        """
        pass

    def get_max_force(self, const_AICharacter_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_max_force(const AICharacter self)
        """
        pass

    def get_node_path(self, const_AICharacter_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_node_path(const AICharacter self)
        """
        pass

    def get_velocity(self, const_AICharacter_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_velocity(const AICharacter self)
        """
        pass

    def setMass(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_mass(const AICharacter self, double m)
        """
        pass

    def setMaxForce(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_max_force(const AICharacter self, double max_force)
        """
        pass

    def setNodePath(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_node_path(const AICharacter self, NodePath np)
        """
        pass

    def setPfGuide(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_pf_guide(const AICharacter self, bool pf_guide)
        
        // This function is used to enable or disable the guides for path finding.
        """
        pass

    def set_mass(self, const_AICharacter_self, double_m): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_mass(const AICharacter self, double m)
        """
        pass

    def set_max_force(self, const_AICharacter_self, double_max_force): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_max_force(const AICharacter self, double max_force)
        """
        pass

    def set_node_path(self, const_AICharacter_self, NodePath_np): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_node_path(const AICharacter self, NodePath np)
        """
        pass

    def set_pf_guide(self, const_AICharacter_self, bool_pf_guide): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_pf_guide(const AICharacter self, bool pf_guide)
        
        // This function is used to enable or disable the guides for path finding.
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

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.ai.AICharacter' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.ai.AICharacter' objects>"
        '__doc__': None,
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.ai.AICharacter' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFDE5664760>'
        'getAiBehaviors': None, # (!) real value is "<method 'getAiBehaviors' of 'panda3d.ai.AICharacter' objects>"
        'getMass': None, # (!) real value is "<method 'getMass' of 'panda3d.ai.AICharacter' objects>"
        'getMaxForce': None, # (!) real value is "<method 'getMaxForce' of 'panda3d.ai.AICharacter' objects>"
        'getNodePath': None, # (!) real value is "<method 'getNodePath' of 'panda3d.ai.AICharacter' objects>"
        'getVelocity': None, # (!) real value is "<method 'getVelocity' of 'panda3d.ai.AICharacter' objects>"
        'get_ai_behaviors': None, # (!) real value is "<method 'get_ai_behaviors' of 'panda3d.ai.AICharacter' objects>"
        'get_mass': None, # (!) real value is "<method 'get_mass' of 'panda3d.ai.AICharacter' objects>"
        'get_max_force': None, # (!) real value is "<method 'get_max_force' of 'panda3d.ai.AICharacter' objects>"
        'get_node_path': None, # (!) real value is "<method 'get_node_path' of 'panda3d.ai.AICharacter' objects>"
        'get_velocity': None, # (!) real value is "<method 'get_velocity' of 'panda3d.ai.AICharacter' objects>"
        'name': None, # (!) real value is "<attribute 'name' of 'panda3d.ai.AICharacter' objects>"
        'setMass': None, # (!) real value is "<method 'setMass' of 'panda3d.ai.AICharacter' objects>"
        'setMaxForce': None, # (!) real value is "<method 'setMaxForce' of 'panda3d.ai.AICharacter' objects>"
        'setNodePath': None, # (!) real value is "<method 'setNodePath' of 'panda3d.ai.AICharacter' objects>"
        'setPfGuide': None, # (!) real value is "<method 'setPfGuide' of 'panda3d.ai.AICharacter' objects>"
        'set_mass': None, # (!) real value is "<method 'set_mass' of 'panda3d.ai.AICharacter' objects>"
        'set_max_force': None, # (!) real value is "<method 'set_max_force' of 'panda3d.ai.AICharacter' objects>"
        'set_node_path': None, # (!) real value is "<method 'set_node_path' of 'panda3d.ai.AICharacter' objects>"
        'set_pf_guide': None, # (!) real value is "<method 'set_pf_guide' of 'panda3d.ai.AICharacter' objects>"
    }


class AINode(__dtoolconfig.DTOOL_SUPER_BASE):
    """
    /**
     * This class is used to assign the nodes on the mesh.  It holds all the data
     * necessary to compute A* algorithm.  It also maintains a lot of vital
     * information such as the neighbor nodes of each node and also its position
     * on the mesh.  Note: The Mesh Generator which is a standalone tool makes use
     * of this class to generate the nodes on the mesh.
     */
    """
    def contains(self, const_AINode_self, float_x, float_y): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        contains(const AINode self, float x, float y)
        
        /**
         * This is a handy function which returns true if the passed position is
         * within the node's dimensions.
         */
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
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.ai.AINode' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.ai.AINode' objects>"
        '__doc__': '/**\n * This class is used to assign the nodes on the mesh.  It holds all the data\n * necessary to compute A* algorithm.  It also maintains a lot of vital\n * information such as the neighbor nodes of each node and also its position\n * on the mesh.  Note: The Mesh Generator which is a standalone tool makes use\n * of this class to generate the nodes on the mesh.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.ai.AINode' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFDE5664930>'
        'contains': None, # (!) real value is "<method 'contains' of 'panda3d.ai.AINode' objects>"
    }


class AIWorld(__dtoolconfig.DTOOL_SUPER_BASE):
    """
    /**
     * A class that implements the virtual AI world which keeps track of the AI
     * characters active at any given time.  It contains a linked list of AI
     * characters, obstactle data and unique name for each character.  It also
     * updates each characters state.  The AI characters can also be added to the
     * world as flocks.
     */
    """
    def addAiChar(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_ai_char(const AIWorld self, AICharacter ai_ch)
        """
        pass

    def addFlock(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_flock(const AIWorld self, Flock flock)
        
        /**
         * This function adds all the AI characters in the Flock object to the
         * AICharPool.  This function allows adding the AI characetrs as part of a
         * flock.
         */
        """
        pass

    def addObstacle(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_obstacle(const AIWorld self, NodePath obstacle)
        
        /**
         * This function adds the nodepath as an obstacle that is needed by the
         * obstacle avoidance behavior.
         */
        """
        pass

    def add_ai_char(self, const_AIWorld_self, AICharacter_ai_ch): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_ai_char(const AIWorld self, AICharacter ai_ch)
        """
        pass

    def add_flock(self, const_AIWorld_self, Flock_flock): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_flock(const AIWorld self, Flock flock)
        
        /**
         * This function adds all the AI characters in the Flock object to the
         * AICharPool.  This function allows adding the AI characetrs as part of a
         * flock.
         */
        """
        pass

    def add_obstacle(self, const_AIWorld_self, NodePath_obstacle): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_obstacle(const AIWorld self, NodePath obstacle)
        
        /**
         * This function adds the nodepath as an obstacle that is needed by the
         * obstacle avoidance behavior.
         */
        """
        pass

    def flockOff(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        flock_off(const AIWorld self, int flock_id)
        
        /**
         * This function turns off the flock behavior temporarily.  Similar to pausing
         * the behavior.
         */
        """
        pass

    def flockOn(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        flock_on(const AIWorld self, int flock_id)
        
        /**
         * This function turns on the flock behavior.
         */
        """
        pass

    def flock_off(self, const_AIWorld_self, int_flock_id): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        flock_off(const AIWorld self, int flock_id)
        
        /**
         * This function turns off the flock behavior temporarily.  Similar to pausing
         * the behavior.
         */
        """
        pass

    def flock_on(self, const_AIWorld_self, int_flock_id): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        flock_on(const AIWorld self, int flock_id)
        
        /**
         * This function turns on the flock behavior.
         */
        """
        pass

    def getFlock(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_flock(const AIWorld self, int flock_id)
        
        /**
         * This function returns a handle to the Flock whose id is passed.
         */
        """
        pass

    def get_flock(self, const_AIWorld_self, int_flock_id): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_flock(const AIWorld self, int flock_id)
        
        /**
         * This function returns a handle to the Flock whose id is passed.
         */
        """
        pass

    def printList(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        print_list(const AIWorld self)
        
        /**
         * This function prints the names of the AI characters that have been added to
         * the AIWorld.  Useful for debugging purposes.
         */
        """
        pass

    def print_list(self, const_AIWorld_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        print_list(const AIWorld self)
        
        /**
         * This function prints the names of the AI characters that have been added to
         * the AIWorld.  Useful for debugging purposes.
         */
        """
        pass

    def removeAiChar(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        remove_ai_char(const AIWorld self, str name)
        """
        pass

    def removeFlock(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        remove_flock(const AIWorld self, int flock_id)
        
        /**
         * This function removes the flock behavior completely.
         */
        """
        pass

    def removeObstacle(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        remove_obstacle(const AIWorld self, NodePath obstacle)
        
        /**
         * This function removes the nodepath from the obstacles list that is needed
         * by the obstacle avoidance behavior.
         */
        """
        pass

    def remove_ai_char(self, const_AIWorld_self, str_name): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        remove_ai_char(const AIWorld self, str name)
        """
        pass

    def remove_flock(self, const_AIWorld_self, int_flock_id): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        remove_flock(const AIWorld self, int flock_id)
        
        /**
         * This function removes the flock behavior completely.
         */
        """
        pass

    def remove_obstacle(self, const_AIWorld_self, NodePath_obstacle): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        remove_obstacle(const AIWorld self, NodePath obstacle)
        
        /**
         * This function removes the nodepath from the obstacles list that is needed
         * by the obstacle avoidance behavior.
         */
        """
        pass

    def update(self, const_AIWorld_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        update(const AIWorld self)
        
        /**
         * The AIWorld update function calls the update function of all the AI
         * characters which have been added to the AIWorld.
         */
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
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.ai.AIWorld' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.ai.AIWorld' objects>"
        '__doc__': '/**\n * A class that implements the virtual AI world which keeps track of the AI\n * characters active at any given time.  It contains a linked list of AI\n * characters, obstactle data and unique name for each character.  It also\n * updates each characters state.  The AI characters can also be added to the\n * world as flocks.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.ai.AIWorld' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFDE5664CD0>'
        'addAiChar': None, # (!) real value is "<method 'addAiChar' of 'panda3d.ai.AIWorld' objects>"
        'addFlock': None, # (!) real value is "<method 'addFlock' of 'panda3d.ai.AIWorld' objects>"
        'addObstacle': None, # (!) real value is "<method 'addObstacle' of 'panda3d.ai.AIWorld' objects>"
        'add_ai_char': None, # (!) real value is "<method 'add_ai_char' of 'panda3d.ai.AIWorld' objects>"
        'add_flock': None, # (!) real value is "<method 'add_flock' of 'panda3d.ai.AIWorld' objects>"
        'add_obstacle': None, # (!) real value is "<method 'add_obstacle' of 'panda3d.ai.AIWorld' objects>"
        'flockOff': None, # (!) real value is "<method 'flockOff' of 'panda3d.ai.AIWorld' objects>"
        'flockOn': None, # (!) real value is "<method 'flockOn' of 'panda3d.ai.AIWorld' objects>"
        'flock_off': None, # (!) real value is "<method 'flock_off' of 'panda3d.ai.AIWorld' objects>"
        'flock_on': None, # (!) real value is "<method 'flock_on' of 'panda3d.ai.AIWorld' objects>"
        'getFlock': None, # (!) real value is "<method 'getFlock' of 'panda3d.ai.AIWorld' objects>"
        'get_flock': None, # (!) real value is "<method 'get_flock' of 'panda3d.ai.AIWorld' objects>"
        'printList': None, # (!) real value is "<method 'printList' of 'panda3d.ai.AIWorld' objects>"
        'print_list': None, # (!) real value is "<method 'print_list' of 'panda3d.ai.AIWorld' objects>"
        'removeAiChar': None, # (!) real value is "<method 'removeAiChar' of 'panda3d.ai.AIWorld' objects>"
        'removeFlock': None, # (!) real value is "<method 'removeFlock' of 'panda3d.ai.AIWorld' objects>"
        'removeObstacle': None, # (!) real value is "<method 'removeObstacle' of 'panda3d.ai.AIWorld' objects>"
        'remove_ai_char': None, # (!) real value is "<method 'remove_ai_char' of 'panda3d.ai.AIWorld' objects>"
        'remove_flock': None, # (!) real value is "<method 'remove_flock' of 'panda3d.ai.AIWorld' objects>"
        'remove_obstacle': None, # (!) real value is "<method 'remove_obstacle' of 'panda3d.ai.AIWorld' objects>"
        'update': None, # (!) real value is "<method 'update' of 'panda3d.ai.AIWorld' objects>"
    }


class Flock(__dtoolconfig.DTOOL_SUPER_BASE):
    """
    /**
     * This class is used to define the flock attributes and the AI characters
     * which are part of the flock.
     */
    """
    def addAiChar(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_ai_char(const Flock self, AICharacter ai_char)
        
        // Function to add the ai characters to _ai_char_list.
        
        /**
         * This function adds AI characters to the flock.
         */
        """
        pass

    def add_ai_char(self, const_Flock_self, AICharacter_ai_char): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_ai_char(const Flock self, AICharacter ai_char)
        
        // Function to add the ai characters to _ai_char_list.
        
        /**
         * This function adds AI characters to the flock.
         */
        """
        pass

    def getId(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_id(const Flock self)
        
        // Function to access the private member flock_id.
        """
        pass

    def get_id(self, const_Flock_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_id(const Flock self)
        
        // Function to access the private member flock_id.
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
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.ai.Flock' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.ai.Flock' objects>"
        '__doc__': '/**\n * This class is used to define the flock attributes and the AI characters\n * which are part of the flock.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.ai.Flock' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFDE5664B00>'
        'addAiChar': None, # (!) real value is "<method 'addAiChar' of 'panda3d.ai.Flock' objects>"
        'add_ai_char': None, # (!) real value is "<method 'add_ai_char' of 'panda3d.ai.Flock' objects>"
        'getId': None, # (!) real value is "<method 'getId' of 'panda3d.ai.Flock' objects>"
        'get_id': None, # (!) real value is "<method 'get_id' of 'panda3d.ai.Flock' objects>"
    }


# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x0000026D02029A90>'

__spec__ = None # (!) real value is "ModuleSpec(name='panda3d.ai', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x0000026D02029A90>, origin='C:\\\\Users\\\\leonm\\\\PycharmProjects\\\\LeonRandomPlus\\\\venv\\\\Lib\\\\site-packages\\\\panda3d\\\\ai.cp311-win_amd64.pyd')"

