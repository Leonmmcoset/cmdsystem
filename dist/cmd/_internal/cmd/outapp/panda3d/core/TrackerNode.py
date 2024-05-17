# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .DataNode import DataNode

class TrackerNode(DataNode):
    """
    /**
     * This class reads the position and orientation information from a tracker
     * device and makes it available as a transformation on the data graph.
     * It is also the primary interface to a Tracker object associated with a
     * ClientBase.
     */
    """
    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getGraphCoordinateSystem(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_graph_coordinate_system(TrackerNode self)
        
        /**
         * Returns the coordinate system that the TrackerNode will convert its
         * transform into for passing down the data graph.  Normally, this is
         * CS_default.
         */
        """
        pass

    def getOrient(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_orient(TrackerNode self)
        
        /**
         * Returns the current orientation of the tracker, if it is available.
         */
        """
        pass

    def getPos(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_pos(TrackerNode self)
        
        /**
         * Returns the current position of the tracker, if it is available.
         */
        """
        pass

    def getTime(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_time(TrackerNode self)
        
        /**
         * Returns the time of the tracker's last update.
         */
        """
        pass

    def getTrackerCoordinateSystem(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_tracker_coordinate_system(TrackerNode self)
        
        /**
         * Returns the coordinate system that the tracker associated with this node
         * will operate in.
         */
        """
        pass

    def getTransform(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_transform(TrackerNode self)
        
        /**
         * Returns the current position and orientation of the tracker, as a combined
         * matrix.
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_graph_coordinate_system(self, TrackerNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_graph_coordinate_system(TrackerNode self)
        
        /**
         * Returns the coordinate system that the TrackerNode will convert its
         * transform into for passing down the data graph.  Normally, this is
         * CS_default.
         */
        """
        pass

    def get_orient(self, TrackerNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_orient(TrackerNode self)
        
        /**
         * Returns the current orientation of the tracker, if it is available.
         */
        """
        pass

    def get_pos(self, TrackerNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_pos(TrackerNode self)
        
        /**
         * Returns the current position of the tracker, if it is available.
         */
        """
        pass

    def get_time(self, TrackerNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_time(TrackerNode self)
        
        /**
         * Returns the time of the tracker's last update.
         */
        """
        pass

    def get_tracker_coordinate_system(self, TrackerNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_tracker_coordinate_system(TrackerNode self)
        
        /**
         * Returns the coordinate system that the tracker associated with this node
         * will operate in.
         */
        """
        pass

    def get_transform(self, TrackerNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_transform(TrackerNode self)
        
        /**
         * Returns the current position and orientation of the tracker, as a combined
         * matrix.
         */
        """
        pass

    def hasTime(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_time(TrackerNode self)
        
        /**
         * True if this data comes with timestamps.
         */
        """
        pass

    def has_time(self, TrackerNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_time(TrackerNode self)
        
        /**
         * True if this data comes with timestamps.
         */
        """
        pass

    def isValid(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_valid(TrackerNode self)
        
        /**
         * Returns true if the TrackerNode is valid and connected to a server, false
         * otherwise.
         */
        """
        pass

    def is_valid(self, TrackerNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_valid(TrackerNode self)
        
        /**
         * Returns true if the TrackerNode is valid and connected to a server, false
         * otherwise.
         */
        """
        pass

    def setGraphCoordinateSystem(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_graph_coordinate_system(const TrackerNode self, int cs)
        
        /**
         * Specifies the coordinate system that the TrackerNode will convert its
         * transform into for passing down the data graph.  Normally, this is
         * CS_default.
         */
        """
        pass

    def setTrackerCoordinateSystem(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_tracker_coordinate_system(const TrackerNode self, int cs)
        
        /**
         * Specifies the coordinate system that the tracker associated with this node
         * will operate in.  Normally, this is set from the ClientBase that's used to
         * create the TrackerNode, so it should not need to be set on an individual
         * tracker basis.
         */
        """
        pass

    def set_graph_coordinate_system(self, const_TrackerNode_self, int_cs): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_graph_coordinate_system(const TrackerNode self, int cs)
        
        /**
         * Specifies the coordinate system that the TrackerNode will convert its
         * transform into for passing down the data graph.  Normally, this is
         * CS_default.
         */
        """
        pass

    def set_tracker_coordinate_system(self, const_TrackerNode_self, int_cs): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_tracker_coordinate_system(const TrackerNode self, int cs)
        
        /**
         * Specifies the coordinate system that the tracker associated with this node
         * will operate in.  Normally, this is set from the ClientBase that's used to
         * create the TrackerNode, so it should not need to be set on an individual
         * tracker basis.
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
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.core.TrackerNode' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.core.TrackerNode' objects>"
        '__doc__': '/**\n * This class reads the position and orientation information from a tracker\n * device and makes it available as a transformation on the data graph.\n * It is also the primary interface to a Tracker object associated with a\n * ClientBase.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.TrackerNode' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE2D74F0>'
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE2D74F0>)>'
        'getGraphCoordinateSystem': None, # (!) real value is "<method 'getGraphCoordinateSystem' of 'panda3d.core.TrackerNode' objects>"
        'getOrient': None, # (!) real value is "<method 'getOrient' of 'panda3d.core.TrackerNode' objects>"
        'getPos': None, # (!) real value is "<method 'getPos' of 'panda3d.core.TrackerNode' objects>"
        'getTime': None, # (!) real value is "<method 'getTime' of 'panda3d.core.TrackerNode' objects>"
        'getTrackerCoordinateSystem': None, # (!) real value is "<method 'getTrackerCoordinateSystem' of 'panda3d.core.TrackerNode' objects>"
        'getTransform': None, # (!) real value is "<method 'getTransform' of 'panda3d.core.TrackerNode' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE2D74F0>)>'
        'get_graph_coordinate_system': None, # (!) real value is "<method 'get_graph_coordinate_system' of 'panda3d.core.TrackerNode' objects>"
        'get_orient': None, # (!) real value is "<method 'get_orient' of 'panda3d.core.TrackerNode' objects>"
        'get_pos': None, # (!) real value is "<method 'get_pos' of 'panda3d.core.TrackerNode' objects>"
        'get_time': None, # (!) real value is "<method 'get_time' of 'panda3d.core.TrackerNode' objects>"
        'get_tracker_coordinate_system': None, # (!) real value is "<method 'get_tracker_coordinate_system' of 'panda3d.core.TrackerNode' objects>"
        'get_transform': None, # (!) real value is "<method 'get_transform' of 'panda3d.core.TrackerNode' objects>"
        'hasTime': None, # (!) real value is "<method 'hasTime' of 'panda3d.core.TrackerNode' objects>"
        'has_time': None, # (!) real value is "<method 'has_time' of 'panda3d.core.TrackerNode' objects>"
        'isValid': None, # (!) real value is "<method 'isValid' of 'panda3d.core.TrackerNode' objects>"
        'is_valid': None, # (!) real value is "<method 'is_valid' of 'panda3d.core.TrackerNode' objects>"
        'setGraphCoordinateSystem': None, # (!) real value is "<method 'setGraphCoordinateSystem' of 'panda3d.core.TrackerNode' objects>"
        'setTrackerCoordinateSystem': None, # (!) real value is "<method 'setTrackerCoordinateSystem' of 'panda3d.core.TrackerNode' objects>"
        'set_graph_coordinate_system': None, # (!) real value is "<method 'set_graph_coordinate_system' of 'panda3d.core.TrackerNode' objects>"
        'set_tracker_coordinate_system': None, # (!) real value is "<method 'set_tracker_coordinate_system' of 'panda3d.core.TrackerNode' objects>"
    }


