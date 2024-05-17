# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .Namable import Namable

class CollisionTraverser(Namable):
    """
    /**
     * This class manages the traversal through the scene graph to detect
     * collisions.  It holds ownership of a number of collider objects, each of
     * which is a CollisionNode and an associated CollisionHandler.
     *
     * When traverse() is called, it begins at the indicated root and detects all
     * collisions with any of its collider objects against nodes at or below the
     * indicated root, calling the appropriate CollisionHandler for each detected
     * collision.
     */
    """
    def addCollider(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_collider(const CollisionTraverser self, const NodePath collider, CollisionHandler handler)
        
        /**
         * Adds a new CollisionNode, representing an object that will be tested for
         * collisions into other objects, along with the handler that will serve each
         * detected collision.  Each CollisionNode may be served by only one handler
         * at a time, but a given handler may serve many CollisionNodes.
         *
         * The handler that serves a particular node may be changed from time to time
         * by calling add_collider() again on the same node.
         */
        """
        pass

    def add_collider(self, const_CollisionTraverser_self, const_NodePath_collider, CollisionHandler_handler): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_collider(const CollisionTraverser self, const NodePath collider, CollisionHandler handler)
        
        /**
         * Adds a new CollisionNode, representing an object that will be tested for
         * collisions into other objects, along with the handler that will serve each
         * detected collision.  Each CollisionNode may be served by only one handler
         * at a time, but a given handler may serve many CollisionNodes.
         *
         * The handler that serves a particular node may be changed from time to time
         * by calling add_collider() again on the same node.
         */
        """
        pass

    def clearColliders(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_colliders(const CollisionTraverser self)
        
        /**
         * Completely empties the set of collision nodes and their associated
         * handlers.
         */
        """
        pass

    def clearRecorder(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_recorder(const CollisionTraverser self)
        
        /**
         * Removes the CollisionRecorder from the traverser and restores normal low-
         * overhead operation.
         */
        """
        pass

    def clear_colliders(self, const_CollisionTraverser_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_colliders(const CollisionTraverser self)
        
        /**
         * Completely empties the set of collision nodes and their associated
         * handlers.
         */
        """
        pass

    def clear_recorder(self, const_CollisionTraverser_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_recorder(const CollisionTraverser self)
        
        /**
         * Removes the CollisionRecorder from the traverser and restores normal low-
         * overhead operation.
         */
        """
        pass

    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getCollider(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_collider(CollisionTraverser self, int n)
        
        /**
         * Returns the nth CollisionNode that has been added to the traverser via
         * add_collider().
         */
        """
        pass

    def getColliders(self, *args, **kwargs): # real signature unknown
        pass

    def getHandler(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_handler(CollisionTraverser self, const NodePath collider)
        
        /**
         * Returns the handler that is currently assigned to serve the indicated
         * collision node, or NULL if the node is not on the traverser's set of active
         * nodes.
         */
        """
        pass

    def getNumColliders(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_colliders(CollisionTraverser self)
        
        /**
         * Returns the number of CollisionNodes that have been added to the traverser
         * via add_collider().
         */
        """
        pass

    def getRecorder(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_recorder(CollisionTraverser self)
        
        /**
         * Returns the CollisionRecorder currently assigned, or NULL if no recorder is
         * assigned.
         */
        """
        pass

    def getRespectPrevTransform(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_respect_prev_transform(CollisionTraverser self)
        
        /**
         * Returns the flag that indicates whether the prev_transform stored on a node
         * is respected to calculate collisions.  See set_respect_prev_transform().
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_collider(self, CollisionTraverser_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_collider(CollisionTraverser self, int n)
        
        /**
         * Returns the nth CollisionNode that has been added to the traverser via
         * add_collider().
         */
        """
        pass

    def get_colliders(self, *args, **kwargs): # real signature unknown
        pass

    def get_handler(self, CollisionTraverser_self, const_NodePath_collider): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_handler(CollisionTraverser self, const NodePath collider)
        
        /**
         * Returns the handler that is currently assigned to serve the indicated
         * collision node, or NULL if the node is not on the traverser's set of active
         * nodes.
         */
        """
        pass

    def get_num_colliders(self, CollisionTraverser_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_colliders(CollisionTraverser self)
        
        /**
         * Returns the number of CollisionNodes that have been added to the traverser
         * via add_collider().
         */
        """
        pass

    def get_recorder(self, CollisionTraverser_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_recorder(CollisionTraverser self)
        
        /**
         * Returns the CollisionRecorder currently assigned, or NULL if no recorder is
         * assigned.
         */
        """
        pass

    def get_respect_prev_transform(self, CollisionTraverser_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_respect_prev_transform(CollisionTraverser self)
        
        /**
         * Returns the flag that indicates whether the prev_transform stored on a node
         * is respected to calculate collisions.  See set_respect_prev_transform().
         */
        """
        pass

    def hasCollider(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_collider(CollisionTraverser self, const NodePath collider)
        
        /**
         * Returns true if the indicated node is current in the set of nodes that will
         * be tested each frame for collisions into other objects.
         */
        """
        pass

    def hasRecorder(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_recorder(CollisionTraverser self)
        
        /**
         * Returns true if the CollisionTraverser has a CollisionRecorder object
         * currently assigned, false otherwise.
         */
        """
        pass

    def has_collider(self, CollisionTraverser_self, const_NodePath_collider): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_collider(CollisionTraverser self, const NodePath collider)
        
        /**
         * Returns true if the indicated node is current in the set of nodes that will
         * be tested each frame for collisions into other objects.
         */
        """
        pass

    def has_recorder(self, CollisionTraverser_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_recorder(CollisionTraverser self)
        
        /**
         * Returns true if the CollisionTraverser has a CollisionRecorder object
         * currently assigned, false otherwise.
         */
        """
        pass

    def hideCollisions(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        hide_collisions(const CollisionTraverser self)
        
        /**
         * Undoes the effect of a previous call to show_collisions().
         */
        """
        pass

    def hide_collisions(self, const_CollisionTraverser_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        hide_collisions(const CollisionTraverser self)
        
        /**
         * Undoes the effect of a previous call to show_collisions().
         */
        """
        pass

    def output(self, CollisionTraverser_self, ostream_out): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        output(CollisionTraverser self, ostream out)
        
        /**
         *
         */
        """
        pass

    def removeCollider(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        remove_collider(const CollisionTraverser self, const NodePath collider)
        
        /**
         * Removes the collider (and its associated handler) from the set of
         * CollisionNodes that will be tested each frame for collisions into other
         * objects.  Returns true if the definition was found and removed, false if it
         * wasn't present to begin with.
         */
        """
        pass

    def remove_collider(self, const_CollisionTraverser_self, const_NodePath_collider): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        remove_collider(const CollisionTraverser self, const NodePath collider)
        
        /**
         * Removes the collider (and its associated handler) from the set of
         * CollisionNodes that will be tested each frame for collisions into other
         * objects.  Returns true if the definition was found and removed, false if it
         * wasn't present to begin with.
         */
        """
        pass

    def setRecorder(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_recorder(const CollisionTraverser self, CollisionRecorder recorder)
        
        /**
         * Uses the indicated CollisionRecorder object to start recording the
         * intersection tests made by each subsequent call to traverse() on this
         * object.  A particular CollisionRecorder object can only record one
         * traverser at a time; if this object has already been assigned to another
         * traverser, that assignment is broken.
         *
         * This is intended to be used in a debugging mode to try to determine what
         * work is being performed by the collision traversal.  Usually, attaching a
         * recorder will impose significant runtime overhead.
         *
         * This does not transfer ownership of the CollisionRecorder pointer;
         * maintenance of that remains the caller's responsibility.  If the
         * CollisionRecorder is destructed, it will cleanly remove itself from the
         * traverser.
         */
        """
        pass

    def setRespectPrevTransform(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_respect_prev_transform(const CollisionTraverser self, bool flag)
        
        /**
         * Sets the flag that indicates whether the prev_transform stored on a node
         * (as updated via set_fluid_pos(), etc.) is respected to calculate
         * collisions.  If this is true, certain types of collision tests will be
         * enhanced by the information about objects in motion.  If this is false,
         * objects are always considered to be static.  The default is false.
         */
        """
        pass

    def set_recorder(self, const_CollisionTraverser_self, CollisionRecorder_recorder): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_recorder(const CollisionTraverser self, CollisionRecorder recorder)
        
        /**
         * Uses the indicated CollisionRecorder object to start recording the
         * intersection tests made by each subsequent call to traverse() on this
         * object.  A particular CollisionRecorder object can only record one
         * traverser at a time; if this object has already been assigned to another
         * traverser, that assignment is broken.
         *
         * This is intended to be used in a debugging mode to try to determine what
         * work is being performed by the collision traversal.  Usually, attaching a
         * recorder will impose significant runtime overhead.
         *
         * This does not transfer ownership of the CollisionRecorder pointer;
         * maintenance of that remains the caller's responsibility.  If the
         * CollisionRecorder is destructed, it will cleanly remove itself from the
         * traverser.
         */
        """
        pass

    def set_respect_prev_transform(self, const_CollisionTraverser_self, bool_flag): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_respect_prev_transform(const CollisionTraverser self, bool flag)
        
        /**
         * Sets the flag that indicates whether the prev_transform stored on a node
         * (as updated via set_fluid_pos(), etc.) is respected to calculate
         * collisions.  If this is true, certain types of collision tests will be
         * enhanced by the information about objects in motion.  If this is false,
         * objects are always considered to be static.  The default is false.
         */
        """
        pass

    def showCollisions(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        show_collisions(const CollisionTraverser self, const NodePath root)
        
        /**
         * This is a high-level function to create a CollisionVisualizer object to
         * render the collision tests performed by this traverser.  The supplied root
         * should be any node in the scene graph; typically, the top node (e.g.
         * render).  The CollisionVisualizer will be attached to this node.
         */
        """
        pass

    def show_collisions(self, const_CollisionTraverser_self, const_NodePath_root): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        show_collisions(const CollisionTraverser self, const NodePath root)
        
        /**
         * This is a high-level function to create a CollisionVisualizer object to
         * render the collision tests performed by this traverser.  The supplied root
         * should be any node in the scene graph; typically, the top node (e.g.
         * render).  The CollisionVisualizer will be attached to this node.
         */
        """
        pass

    def traverse(self, const_CollisionTraverser_self, const_NodePath_root): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        traverse(const CollisionTraverser self, const NodePath root)
        
        /**
         * Perform the traversal. Begins at the indicated root and detects all
         * collisions with any of its collider objects against nodes at or below the
         * indicated root, calling the appropriate CollisionHandler for each detected
         * collision.
         */
        """
        pass

    def write(self, CollisionTraverser_self, ostream_out, int_indent_level): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        write(CollisionTraverser self, ostream out, int indent_level)
        
        /**
         *
         */
        """
        pass

    def __copy__(self, *args, **kwargs): # real signature unknown
        pass

    def __deepcopy__(self, *args, **kwargs): # real signature unknown
        pass

    def __getstate__(self, CollisionTraverser_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        __getstate__(CollisionTraverser self)
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

    def __setstate__(self, const_CollisionTraverser_self, object_state): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        __setstate__(const CollisionTraverser self, object state)
        """
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    colliders = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    recorder = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    respect_preV_transform = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    respect_prev_transform = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.core.CollisionTraverser' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.core.CollisionTraverser' objects>"
        '__doc__': '/**\n * This class manages the traversal through the scene graph to detect\n * collisions.  It holds ownership of a number of collider objects, each of\n * which is a CollisionNode and an associated CollisionHandler.\n *\n * When traverse() is called, it begins at the indicated root and detects all\n * collisions with any of its collider objects against nodes at or below the\n * indicated root, calling the appropriate CollisionHandler for each detected\n * collision.\n */',
        '__getstate__': None, # (!) real value is "<method '__getstate__' of 'panda3d.core.CollisionTraverser' objects>"
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.CollisionTraverser' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE2CE4C0>'
        '__repr__': None, # (!) real value is "<slot wrapper '__repr__' of 'panda3d.core.CollisionTraverser' objects>"
        '__setstate__': None, # (!) real value is "<method '__setstate__' of 'panda3d.core.CollisionTraverser' objects>"
        '__str__': None, # (!) real value is "<slot wrapper '__str__' of 'panda3d.core.CollisionTraverser' objects>"
        'addCollider': None, # (!) real value is "<method 'addCollider' of 'panda3d.core.CollisionTraverser' objects>"
        'add_collider': None, # (!) real value is "<method 'add_collider' of 'panda3d.core.CollisionTraverser' objects>"
        'clearColliders': None, # (!) real value is "<method 'clearColliders' of 'panda3d.core.CollisionTraverser' objects>"
        'clearRecorder': None, # (!) real value is "<method 'clearRecorder' of 'panda3d.core.CollisionTraverser' objects>"
        'clear_colliders': None, # (!) real value is "<method 'clear_colliders' of 'panda3d.core.CollisionTraverser' objects>"
        'clear_recorder': None, # (!) real value is "<method 'clear_recorder' of 'panda3d.core.CollisionTraverser' objects>"
        'colliders': None, # (!) real value is "<attribute 'colliders' of 'panda3d.core.CollisionTraverser' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE2CE4C0>)>'
        'getCollider': None, # (!) real value is "<method 'getCollider' of 'panda3d.core.CollisionTraverser' objects>"
        'getColliders': None, # (!) real value is "<method 'getColliders' of 'panda3d.core.CollisionTraverser' objects>"
        'getHandler': None, # (!) real value is "<method 'getHandler' of 'panda3d.core.CollisionTraverser' objects>"
        'getNumColliders': None, # (!) real value is "<method 'getNumColliders' of 'panda3d.core.CollisionTraverser' objects>"
        'getRecorder': None, # (!) real value is "<method 'getRecorder' of 'panda3d.core.CollisionTraverser' objects>"
        'getRespectPrevTransform': None, # (!) real value is "<method 'getRespectPrevTransform' of 'panda3d.core.CollisionTraverser' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE2CE4C0>)>'
        'get_collider': None, # (!) real value is "<method 'get_collider' of 'panda3d.core.CollisionTraverser' objects>"
        'get_colliders': None, # (!) real value is "<method 'get_colliders' of 'panda3d.core.CollisionTraverser' objects>"
        'get_handler': None, # (!) real value is "<method 'get_handler' of 'panda3d.core.CollisionTraverser' objects>"
        'get_num_colliders': None, # (!) real value is "<method 'get_num_colliders' of 'panda3d.core.CollisionTraverser' objects>"
        'get_recorder': None, # (!) real value is "<method 'get_recorder' of 'panda3d.core.CollisionTraverser' objects>"
        'get_respect_prev_transform': None, # (!) real value is "<method 'get_respect_prev_transform' of 'panda3d.core.CollisionTraverser' objects>"
        'hasCollider': None, # (!) real value is "<method 'hasCollider' of 'panda3d.core.CollisionTraverser' objects>"
        'hasRecorder': None, # (!) real value is "<method 'hasRecorder' of 'panda3d.core.CollisionTraverser' objects>"
        'has_collider': None, # (!) real value is "<method 'has_collider' of 'panda3d.core.CollisionTraverser' objects>"
        'has_recorder': None, # (!) real value is "<method 'has_recorder' of 'panda3d.core.CollisionTraverser' objects>"
        'hideCollisions': None, # (!) real value is "<method 'hideCollisions' of 'panda3d.core.CollisionTraverser' objects>"
        'hide_collisions': None, # (!) real value is "<method 'hide_collisions' of 'panda3d.core.CollisionTraverser' objects>"
        'output': None, # (!) real value is "<method 'output' of 'panda3d.core.CollisionTraverser' objects>"
        'recorder': None, # (!) real value is "<attribute 'recorder' of 'panda3d.core.CollisionTraverser' objects>"
        'removeCollider': None, # (!) real value is "<method 'removeCollider' of 'panda3d.core.CollisionTraverser' objects>"
        'remove_collider': None, # (!) real value is "<method 'remove_collider' of 'panda3d.core.CollisionTraverser' objects>"
        'respect_preV_transform': None, # (!) real value is "<attribute 'respect_preV_transform' of 'panda3d.core.CollisionTraverser' objects>"
        'respect_prev_transform': None, # (!) real value is "<attribute 'respect_prev_transform' of 'panda3d.core.CollisionTraverser' objects>"
        'setRecorder': None, # (!) real value is "<method 'setRecorder' of 'panda3d.core.CollisionTraverser' objects>"
        'setRespectPrevTransform': None, # (!) real value is "<method 'setRespectPrevTransform' of 'panda3d.core.CollisionTraverser' objects>"
        'set_recorder': None, # (!) real value is "<method 'set_recorder' of 'panda3d.core.CollisionTraverser' objects>"
        'set_respect_prev_transform': None, # (!) real value is "<method 'set_respect_prev_transform' of 'panda3d.core.CollisionTraverser' objects>"
        'showCollisions': None, # (!) real value is "<method 'showCollisions' of 'panda3d.core.CollisionTraverser' objects>"
        'show_collisions': None, # (!) real value is "<method 'show_collisions' of 'panda3d.core.CollisionTraverser' objects>"
        'traverse': None, # (!) real value is "<method 'traverse' of 'panda3d.core.CollisionTraverser' objects>"
        'write': None, # (!) real value is "<method 'write' of 'panda3d.core.CollisionTraverser' objects>"
    }


