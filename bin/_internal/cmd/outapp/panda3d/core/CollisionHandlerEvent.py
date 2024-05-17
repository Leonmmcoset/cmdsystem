# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .CollisionHandler import CollisionHandler

class CollisionHandlerEvent(CollisionHandler):
    """
    /**
     * A specialized kind of CollisionHandler that throws an event for each
     * collision detected.  The event thrown may be based on the name of the
     * moving object or the struck object, or both.  The first parameter of the
     * event will be a pointer to the CollisionEntry that triggered it.
     */
    """
    def addAgainPattern(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_again_pattern(const CollisionHandlerEvent self, str again_pattern)
        
        /**
         * Adds the pattern string that indicates how the event names are generated
         * when a collision between two particular nodes is *still* detected.  This
         * event is thrown each consecutive time a collision between two particular
         * nodes is detected, starting with the second time.
         *
         * In general, the in_pattern event is thrown on the first detection of a
         * collision between two particular nodes.  In subsequent passes, as long as a
         * collision between those two nodes continues to be detected each frame, the
         * again_pattern is thrown.  The first frame in which the collision is no
         * longer detected, the out_pattern event is thrown.
         */
        """
        pass

    def addInPattern(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_in_pattern(const CollisionHandlerEvent self, str in_pattern)
        
        /**
         * Adds a pattern string to the list of events that will be generated in
         * response to a collision.  The pattern string describes how the event name
         * will be composed.  It is a string that may contain any of the following:
         *
         * %fn  - the name of the "from" object's node %in  - the name of the "into"
         * object's node %fs  - 't' if "from" is tangible, 'i' if intangible %is  -
         * 't' if "into" is tangible, 'i' if intangible %ig  - 'c' if the collision is
         * into a CollisionNode, 'g' if it is a geom.
         *
         * %(tag)fh - generate event only if "from" node has the indicated net tag.
         * %(tag)fx - generate event only if "from" node does not have the indicated
         * net tag.  %(tag)ih - generate event only if "into" node has the indicated
         * net tag.  %(tag)ix - generate event only if "into" node does not have the
         * indicated net tag.  %(tag)ft - the indicated net tag value of the "from"
         * node.  %(tag)it - the indicated net tag value of the "into" node.
         *
         * Parentheses in the above are literal and should be included in the actual
         * pattern.
         *
         * The event name will be based on the in_pattern string specified here, with
         * all occurrences of the above strings replaced with the corresponding
         * values.
         *
         * In general, the in_pattern event is thrown on the first detection of a
         * collision between two particular nodes.  In subsequent passes, as long as a
         * collision between those two nodes continues to be detected each frame, the
         * again_pattern is thrown.  The first frame in which the collision is no
         * longer detected, the out_pattern event is thrown.
         */
        """
        pass

    def addOutPattern(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_out_pattern(const CollisionHandlerEvent self, str out_pattern)
        
        /**
         * Adds the pattern string that indicates how the event names are generated
         * when a collision between two particular nodes is *no longer* detected.
         *
         * In general, the in_pattern event is thrown on the first detection of a
         * collision between two particular nodes.  In subsequent passes, as long as a
         * collision between those two nodes continues to be detected each frame, the
         * again_pattern is thrown.  The first frame in which the collision is no
         * longer detected, the out_pattern event is thrown.
         */
        """
        pass

    def add_again_pattern(self, const_CollisionHandlerEvent_self, str_again_pattern): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_again_pattern(const CollisionHandlerEvent self, str again_pattern)
        
        /**
         * Adds the pattern string that indicates how the event names are generated
         * when a collision between two particular nodes is *still* detected.  This
         * event is thrown each consecutive time a collision between two particular
         * nodes is detected, starting with the second time.
         *
         * In general, the in_pattern event is thrown on the first detection of a
         * collision between two particular nodes.  In subsequent passes, as long as a
         * collision between those two nodes continues to be detected each frame, the
         * again_pattern is thrown.  The first frame in which the collision is no
         * longer detected, the out_pattern event is thrown.
         */
        """
        pass

    def add_in_pattern(self, const_CollisionHandlerEvent_self, str_in_pattern): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_in_pattern(const CollisionHandlerEvent self, str in_pattern)
        
        /**
         * Adds a pattern string to the list of events that will be generated in
         * response to a collision.  The pattern string describes how the event name
         * will be composed.  It is a string that may contain any of the following:
         *
         * %fn  - the name of the "from" object's node %in  - the name of the "into"
         * object's node %fs  - 't' if "from" is tangible, 'i' if intangible %is  -
         * 't' if "into" is tangible, 'i' if intangible %ig  - 'c' if the collision is
         * into a CollisionNode, 'g' if it is a geom.
         *
         * %(tag)fh - generate event only if "from" node has the indicated net tag.
         * %(tag)fx - generate event only if "from" node does not have the indicated
         * net tag.  %(tag)ih - generate event only if "into" node has the indicated
         * net tag.  %(tag)ix - generate event only if "into" node does not have the
         * indicated net tag.  %(tag)ft - the indicated net tag value of the "from"
         * node.  %(tag)it - the indicated net tag value of the "into" node.
         *
         * Parentheses in the above are literal and should be included in the actual
         * pattern.
         *
         * The event name will be based on the in_pattern string specified here, with
         * all occurrences of the above strings replaced with the corresponding
         * values.
         *
         * In general, the in_pattern event is thrown on the first detection of a
         * collision between two particular nodes.  In subsequent passes, as long as a
         * collision between those two nodes continues to be detected each frame, the
         * again_pattern is thrown.  The first frame in which the collision is no
         * longer detected, the out_pattern event is thrown.
         */
        """
        pass

    def add_out_pattern(self, const_CollisionHandlerEvent_self, str_out_pattern): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_out_pattern(const CollisionHandlerEvent self, str out_pattern)
        
        /**
         * Adds the pattern string that indicates how the event names are generated
         * when a collision between two particular nodes is *no longer* detected.
         *
         * In general, the in_pattern event is thrown on the first detection of a
         * collision between two particular nodes.  In subsequent passes, as long as a
         * collision between those two nodes continues to be detected each frame, the
         * again_pattern is thrown.  The first frame in which the collision is no
         * longer detected, the out_pattern event is thrown.
         */
        """
        pass

    def clear(self, const_CollisionHandlerEvent_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear(const CollisionHandlerEvent self)
        
        /**
         * Empties the list of elements that all colliders are known to be colliding
         * with.  No "out" events will be thrown; if the same collision is detected
         * next frame, a new "in" event will be thrown for each collision.
         *
         * This can be called each frame to defeat the persistent "in" event
         * mechanism, which prevents the same "in" event from being thrown repeatedly.
         * However, also see add_again_pattern(), which can be used to set the event
         * that is thrown when a collision is detected for two or more consecutive
         * frames.
         */
        """
        pass

    def clearAgainPatterns(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_again_patterns(const CollisionHandlerEvent self)
        
        /**
         * Removes all of the previously-added in patterns.  See add_again_pattern.
         */
        """
        pass

    def clearInPatterns(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_in_patterns(const CollisionHandlerEvent self)
        
        /**
         * Removes all of the previously-added in patterns.  See add_in_pattern.
         */
        """
        pass

    def clearOutPatterns(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_out_patterns(const CollisionHandlerEvent self)
        
        /**
         * Removes all of the previously-added in patterns.  See add_out_pattern.
         */
        """
        pass

    def clear_again_patterns(self, const_CollisionHandlerEvent_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_again_patterns(const CollisionHandlerEvent self)
        
        /**
         * Removes all of the previously-added in patterns.  See add_again_pattern.
         */
        """
        pass

    def clear_in_patterns(self, const_CollisionHandlerEvent_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_in_patterns(const CollisionHandlerEvent self)
        
        /**
         * Removes all of the previously-added in patterns.  See add_in_pattern.
         */
        """
        pass

    def clear_out_patterns(self, const_CollisionHandlerEvent_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_out_patterns(const CollisionHandlerEvent self)
        
        /**
         * Removes all of the previously-added in patterns.  See add_out_pattern.
         */
        """
        pass

    def flush(self, const_CollisionHandlerEvent_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        flush(const CollisionHandlerEvent self)
        
        /**
         * Same as clear() except "out" events are thrown.
         */
        """
        pass

    def getAgainPattern(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_again_pattern(CollisionHandlerEvent self, int n)
        
        /**
         * Returns the nth pattern string that indicates how the event names are
         * generated for each collision detected.  See add_again_pattern().
         */
        """
        pass

    def getAgainPatterns(self, *args, **kwargs): # real signature unknown
        pass

    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getInPattern(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_in_pattern(CollisionHandlerEvent self, int n)
        
        /**
         * Returns the nth pattern string that indicates how the event names are
         * generated for each collision detected.  See add_in_pattern().
         */
        """
        pass

    def getInPatterns(self, *args, **kwargs): # real signature unknown
        pass

    def getNumAgainPatterns(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_again_patterns(CollisionHandlerEvent self)
        
        /**
         * Returns the number of in pattern strings that have been added.
         */
        """
        pass

    def getNumInPatterns(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_in_patterns(CollisionHandlerEvent self)
        
        /**
         * Returns the number of in pattern strings that have been added.
         */
        """
        pass

    def getNumOutPatterns(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_out_patterns(CollisionHandlerEvent self)
        
        /**
         * Returns the number of in pattern strings that have been added.
         */
        """
        pass

    def getOutPattern(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_out_pattern(CollisionHandlerEvent self, int n)
        
        /**
         * Returns the nth pattern string that indicates how the event names are
         * generated for each collision detected.  See add_out_pattern().
         */
        """
        pass

    def getOutPatterns(self, *args, **kwargs): # real signature unknown
        pass

    def get_again_pattern(self, CollisionHandlerEvent_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_again_pattern(CollisionHandlerEvent self, int n)
        
        /**
         * Returns the nth pattern string that indicates how the event names are
         * generated for each collision detected.  See add_again_pattern().
         */
        """
        pass

    def get_again_patterns(self, *args, **kwargs): # real signature unknown
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_in_pattern(self, CollisionHandlerEvent_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_in_pattern(CollisionHandlerEvent self, int n)
        
        /**
         * Returns the nth pattern string that indicates how the event names are
         * generated for each collision detected.  See add_in_pattern().
         */
        """
        pass

    def get_in_patterns(self, *args, **kwargs): # real signature unknown
        pass

    def get_num_again_patterns(self, CollisionHandlerEvent_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_again_patterns(CollisionHandlerEvent self)
        
        /**
         * Returns the number of in pattern strings that have been added.
         */
        """
        pass

    def get_num_in_patterns(self, CollisionHandlerEvent_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_in_patterns(CollisionHandlerEvent self)
        
        /**
         * Returns the number of in pattern strings that have been added.
         */
        """
        pass

    def get_num_out_patterns(self, CollisionHandlerEvent_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_out_patterns(CollisionHandlerEvent self)
        
        /**
         * Returns the number of in pattern strings that have been added.
         */
        """
        pass

    def get_out_pattern(self, CollisionHandlerEvent_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_out_pattern(CollisionHandlerEvent self, int n)
        
        /**
         * Returns the nth pattern string that indicates how the event names are
         * generated for each collision detected.  See add_out_pattern().
         */
        """
        pass

    def get_out_patterns(self, *args, **kwargs): # real signature unknown
        pass

    def readDatagram(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        read_datagram(const CollisionHandlerEvent self, DatagramIterator source)
        
        /**
         * Restores the object state from the given datagram, previously obtained using
         * __getstate__.
         */
        """
        pass

    def read_datagram(self, const_CollisionHandlerEvent_self, DatagramIterator_source): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        read_datagram(const CollisionHandlerEvent self, DatagramIterator source)
        
        /**
         * Restores the object state from the given datagram, previously obtained using
         * __getstate__.
         */
        """
        pass

    def setAgainPattern(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_again_pattern(const CollisionHandlerEvent self, str again_pattern)
        
        /**
         * This method is deprecated; it completely replaces all the in patterns that
         * have previously been set with the indicated pattern.
         *
         * @deprecated Use add_again_pattern() instead.
         */
        """
        pass

    def setInPattern(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_in_pattern(const CollisionHandlerEvent self, str in_pattern)
        
        /**
         * This method is deprecated; it completely replaces all the in patterns that
         * have previously been set with the indicated pattern.
         *
         * @deprecated Use add_in_pattern() instead.
         */
        """
        pass

    def setOutPattern(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_out_pattern(const CollisionHandlerEvent self, str out_pattern)
        
        /**
         * This method is deprecated; it completely replaces all the in patterns that
         * have previously been set with the indicated pattern.
         *
         * @deprecated Use add_out_pattern() instead.
         */
        """
        pass

    def set_again_pattern(self, const_CollisionHandlerEvent_self, str_again_pattern): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_again_pattern(const CollisionHandlerEvent self, str again_pattern)
        
        /**
         * This method is deprecated; it completely replaces all the in patterns that
         * have previously been set with the indicated pattern.
         *
         * @deprecated Use add_again_pattern() instead.
         */
        """
        pass

    def set_in_pattern(self, const_CollisionHandlerEvent_self, str_in_pattern): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_in_pattern(const CollisionHandlerEvent self, str in_pattern)
        
        /**
         * This method is deprecated; it completely replaces all the in patterns that
         * have previously been set with the indicated pattern.
         *
         * @deprecated Use add_in_pattern() instead.
         */
        """
        pass

    def set_out_pattern(self, const_CollisionHandlerEvent_self, str_out_pattern): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_out_pattern(const CollisionHandlerEvent self, str out_pattern)
        
        /**
         * This method is deprecated; it completely replaces all the in patterns that
         * have previously been set with the indicated pattern.
         *
         * @deprecated Use add_out_pattern() instead.
         */
        """
        pass

    def writeDatagram(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        write_datagram(CollisionHandlerEvent self, Datagram destination)
        
        /**
         * Serializes this object, to implement pickle support.
         */
        """
        pass

    def write_datagram(self, CollisionHandlerEvent_self, Datagram_destination): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        write_datagram(CollisionHandlerEvent self, Datagram destination)
        
        /**
         * Serializes this object, to implement pickle support.
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

    def __reduce__(self, CollisionHandlerEvent_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        __reduce__(CollisionHandlerEvent self)
        
        // These help implement Python pickle support.
        """
        pass

    def __setstate__(self, const_CollisionHandlerEvent_self, bytes_data): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        __setstate__(const CollisionHandlerEvent self, bytes data)
        """
        pass

    again_patterns = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    in_patterns = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    out_patterns = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.core.CollisionHandlerEvent' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.core.CollisionHandlerEvent' objects>"
        '__doc__': '/**\n * A specialized kind of CollisionHandler that throws an event for each\n * collision detected.  The event thrown may be based on the name of the\n * moving object or the struck object, or both.  The first parameter of the\n * event will be a pointer to the CollisionEntry that triggered it.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.CollisionHandlerEvent' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE2CEFA0>'
        '__reduce__': None, # (!) real value is "<method '__reduce__' of 'panda3d.core.CollisionHandlerEvent' objects>"
        '__setstate__': None, # (!) real value is "<method '__setstate__' of 'panda3d.core.CollisionHandlerEvent' objects>"
        'addAgainPattern': None, # (!) real value is "<method 'addAgainPattern' of 'panda3d.core.CollisionHandlerEvent' objects>"
        'addInPattern': None, # (!) real value is "<method 'addInPattern' of 'panda3d.core.CollisionHandlerEvent' objects>"
        'addOutPattern': None, # (!) real value is "<method 'addOutPattern' of 'panda3d.core.CollisionHandlerEvent' objects>"
        'add_again_pattern': None, # (!) real value is "<method 'add_again_pattern' of 'panda3d.core.CollisionHandlerEvent' objects>"
        'add_in_pattern': None, # (!) real value is "<method 'add_in_pattern' of 'panda3d.core.CollisionHandlerEvent' objects>"
        'add_out_pattern': None, # (!) real value is "<method 'add_out_pattern' of 'panda3d.core.CollisionHandlerEvent' objects>"
        'again_patterns': None, # (!) real value is "<attribute 'again_patterns' of 'panda3d.core.CollisionHandlerEvent' objects>"
        'clear': None, # (!) real value is "<method 'clear' of 'panda3d.core.CollisionHandlerEvent' objects>"
        'clearAgainPatterns': None, # (!) real value is "<method 'clearAgainPatterns' of 'panda3d.core.CollisionHandlerEvent' objects>"
        'clearInPatterns': None, # (!) real value is "<method 'clearInPatterns' of 'panda3d.core.CollisionHandlerEvent' objects>"
        'clearOutPatterns': None, # (!) real value is "<method 'clearOutPatterns' of 'panda3d.core.CollisionHandlerEvent' objects>"
        'clear_again_patterns': None, # (!) real value is "<method 'clear_again_patterns' of 'panda3d.core.CollisionHandlerEvent' objects>"
        'clear_in_patterns': None, # (!) real value is "<method 'clear_in_patterns' of 'panda3d.core.CollisionHandlerEvent' objects>"
        'clear_out_patterns': None, # (!) real value is "<method 'clear_out_patterns' of 'panda3d.core.CollisionHandlerEvent' objects>"
        'flush': None, # (!) real value is "<method 'flush' of 'panda3d.core.CollisionHandlerEvent' objects>"
        'getAgainPattern': None, # (!) real value is "<method 'getAgainPattern' of 'panda3d.core.CollisionHandlerEvent' objects>"
        'getAgainPatterns': None, # (!) real value is "<method 'getAgainPatterns' of 'panda3d.core.CollisionHandlerEvent' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE2CEFA0>)>'
        'getInPattern': None, # (!) real value is "<method 'getInPattern' of 'panda3d.core.CollisionHandlerEvent' objects>"
        'getInPatterns': None, # (!) real value is "<method 'getInPatterns' of 'panda3d.core.CollisionHandlerEvent' objects>"
        'getNumAgainPatterns': None, # (!) real value is "<method 'getNumAgainPatterns' of 'panda3d.core.CollisionHandlerEvent' objects>"
        'getNumInPatterns': None, # (!) real value is "<method 'getNumInPatterns' of 'panda3d.core.CollisionHandlerEvent' objects>"
        'getNumOutPatterns': None, # (!) real value is "<method 'getNumOutPatterns' of 'panda3d.core.CollisionHandlerEvent' objects>"
        'getOutPattern': None, # (!) real value is "<method 'getOutPattern' of 'panda3d.core.CollisionHandlerEvent' objects>"
        'getOutPatterns': None, # (!) real value is "<method 'getOutPatterns' of 'panda3d.core.CollisionHandlerEvent' objects>"
        'get_again_pattern': None, # (!) real value is "<method 'get_again_pattern' of 'panda3d.core.CollisionHandlerEvent' objects>"
        'get_again_patterns': None, # (!) real value is "<method 'get_again_patterns' of 'panda3d.core.CollisionHandlerEvent' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE2CEFA0>)>'
        'get_in_pattern': None, # (!) real value is "<method 'get_in_pattern' of 'panda3d.core.CollisionHandlerEvent' objects>"
        'get_in_patterns': None, # (!) real value is "<method 'get_in_patterns' of 'panda3d.core.CollisionHandlerEvent' objects>"
        'get_num_again_patterns': None, # (!) real value is "<method 'get_num_again_patterns' of 'panda3d.core.CollisionHandlerEvent' objects>"
        'get_num_in_patterns': None, # (!) real value is "<method 'get_num_in_patterns' of 'panda3d.core.CollisionHandlerEvent' objects>"
        'get_num_out_patterns': None, # (!) real value is "<method 'get_num_out_patterns' of 'panda3d.core.CollisionHandlerEvent' objects>"
        'get_out_pattern': None, # (!) real value is "<method 'get_out_pattern' of 'panda3d.core.CollisionHandlerEvent' objects>"
        'get_out_patterns': None, # (!) real value is "<method 'get_out_patterns' of 'panda3d.core.CollisionHandlerEvent' objects>"
        'in_patterns': None, # (!) real value is "<attribute 'in_patterns' of 'panda3d.core.CollisionHandlerEvent' objects>"
        'out_patterns': None, # (!) real value is "<attribute 'out_patterns' of 'panda3d.core.CollisionHandlerEvent' objects>"
        'readDatagram': None, # (!) real value is "<method 'readDatagram' of 'panda3d.core.CollisionHandlerEvent' objects>"
        'read_datagram': None, # (!) real value is "<method 'read_datagram' of 'panda3d.core.CollisionHandlerEvent' objects>"
        'setAgainPattern': None, # (!) real value is "<method 'setAgainPattern' of 'panda3d.core.CollisionHandlerEvent' objects>"
        'setInPattern': None, # (!) real value is "<method 'setInPattern' of 'panda3d.core.CollisionHandlerEvent' objects>"
        'setOutPattern': None, # (!) real value is "<method 'setOutPattern' of 'panda3d.core.CollisionHandlerEvent' objects>"
        'set_again_pattern': None, # (!) real value is "<method 'set_again_pattern' of 'panda3d.core.CollisionHandlerEvent' objects>"
        'set_in_pattern': None, # (!) real value is "<method 'set_in_pattern' of 'panda3d.core.CollisionHandlerEvent' objects>"
        'set_out_pattern': None, # (!) real value is "<method 'set_out_pattern' of 'panda3d.core.CollisionHandlerEvent' objects>"
        'writeDatagram': None, # (!) real value is "<method 'writeDatagram' of 'panda3d.core.CollisionHandlerEvent' objects>"
        'write_datagram': None, # (!) real value is "<method 'write_datagram' of 'panda3d.core.CollisionHandlerEvent' objects>"
    }


