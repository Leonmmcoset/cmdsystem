# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .ParamValueBase import ParamValueBase

class PointerEventList(ParamValueBase):
    """
    /**
     * Records a set of pointer events that happened recently.  This class is
     * usually used only in the data graph, to transmit the recent pointer
     * presses, but it may be used anywhere a list of PointerEvents is desired.
     */
    """
    def addEvent(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_event(const PointerEventList self, const PointerData data, int seq, double time)
        add_event(const PointerEventList self, bool in_win, int xpos, int ypos, int seq, double time)
        add_event(const PointerEventList self, bool in_win, int xpos, int ypos, double xdelta, double ydelta, int seq, double time)
        
        /**
         * Adds a new event from the given PointerData object.
         */
        
        /**
         * Adds a new event to the end of the list.  Automatically calculates the dx,
         * dy, length, direction, and rotation for all but the first event.
         */
        
        /**
         * Adds a new event to the end of the list based on the given mouse movement.
         */
        """
        pass

    def add_event(self, const_PointerEventList_self, const_PointerData_data, int_seq, double_time): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_event(const PointerEventList self, const PointerData data, int seq, double time)
        add_event(const PointerEventList self, bool in_win, int xpos, int ypos, int seq, double time)
        add_event(const PointerEventList self, bool in_win, int xpos, int ypos, double xdelta, double ydelta, int seq, double time)
        
        /**
         * Adds a new event from the given PointerData object.
         */
        
        /**
         * Adds a new event to the end of the list.  Automatically calculates the dx,
         * dy, length, direction, and rotation for all but the first event.
         */
        
        /**
         * Adds a new event to the end of the list based on the given mouse movement.
         */
        """
        pass

    def clear(self, const_PointerEventList_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear(const PointerEventList self)
        
        /**
         * Empties all the events from the list.
         */
        """
        pass

    def encircles(self, PointerEventList_self, int_x, int_y): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        encircles(PointerEventList self, int x, int y)
        
        /**
         * Returns true if the trail loops around the specified point.
         */
        """
        pass

    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getDirection(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_direction(PointerEventList self, int n)
        
        /**
         * Get the direction of the nth event.
         */
        """
        pass

    def getDx(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_dx(PointerEventList self, int n)
        
        /**
         * Get the x-delta of the nth event.
         */
        """
        pass

    def getDy(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_dy(PointerEventList self, int n)
        
        /**
         * Get the y-delta of the nth event.
         */
        """
        pass

    def getInWindow(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_in_window(PointerEventList self, int n)
        
        /**
         * Get the in-window flag of the nth event.
         */
        """
        pass

    def getLength(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_length(PointerEventList self, int n)
        
        /**
         * Get the length of the nth event.
         */
        """
        pass

    def getNumEvents(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_events(PointerEventList self)
        
        /**
         * Returns the number of events in the list.
         */
        """
        pass

    def getRotation(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_rotation(PointerEventList self, int n)
        
        /**
         * Get the rotation of the nth event.
         */
        """
        pass

    def getSequence(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_sequence(PointerEventList self, int n)
        
        /**
         * Get the sequence number of the nth event.
         */
        """
        pass

    def getTime(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_time(PointerEventList self, int n)
        
        /**
         * Get the timestamp of the nth event.
         */
        """
        pass

    def getXpos(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_xpos(PointerEventList self, int n)
        
        /**
         * Get the x-coordinate of the nth event.
         */
        """
        pass

    def getYpos(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_ypos(PointerEventList self, int n)
        
        /**
         * Get the y-coordinate of the nth event.
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_direction(self, PointerEventList_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_direction(PointerEventList self, int n)
        
        /**
         * Get the direction of the nth event.
         */
        """
        pass

    def get_dx(self, PointerEventList_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_dx(PointerEventList self, int n)
        
        /**
         * Get the x-delta of the nth event.
         */
        """
        pass

    def get_dy(self, PointerEventList_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_dy(PointerEventList self, int n)
        
        /**
         * Get the y-delta of the nth event.
         */
        """
        pass

    def get_in_window(self, PointerEventList_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_in_window(PointerEventList self, int n)
        
        /**
         * Get the in-window flag of the nth event.
         */
        """
        pass

    def get_length(self, PointerEventList_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_length(PointerEventList self, int n)
        
        /**
         * Get the length of the nth event.
         */
        """
        pass

    def get_num_events(self, PointerEventList_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_events(PointerEventList self)
        
        /**
         * Returns the number of events in the list.
         */
        """
        pass

    def get_rotation(self, PointerEventList_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_rotation(PointerEventList self, int n)
        
        /**
         * Get the rotation of the nth event.
         */
        """
        pass

    def get_sequence(self, PointerEventList_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_sequence(PointerEventList self, int n)
        
        /**
         * Get the sequence number of the nth event.
         */
        """
        pass

    def get_time(self, PointerEventList_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_time(PointerEventList self, int n)
        
        /**
         * Get the timestamp of the nth event.
         */
        """
        pass

    def get_xpos(self, PointerEventList_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_xpos(PointerEventList self, int n)
        
        /**
         * Get the x-coordinate of the nth event.
         */
        """
        pass

    def get_ypos(self, PointerEventList_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_ypos(PointerEventList self, int n)
        
        /**
         * Get the y-coordinate of the nth event.
         */
        """
        pass

    def matchPattern(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        match_pattern(const PointerEventList self, str pattern, double rot, double seglen)
        
        /**
         * This function is not implemented yet.  It is a work in progress.  The
         * intent is as follows:
         *
         * Returns a nonzero value if the mouse movements match the specified pattern.
         * The higher the value, the better the match.  The pattern is a sequence of
         * compass directions (ie, "E", "NE", etc) separated by spaces.  If rot is
         * nonzero, then the pattern is rotated counterclockwise by the specified
         * amount before testing.  Seglen is the minimum length a mouse movement needs
         * to be in order to be considered significant.
         */
        """
        pass

    def match_pattern(self, const_PointerEventList_self, str_pattern, double_rot, double_seglen): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        match_pattern(const PointerEventList self, str pattern, double rot, double seglen)
        
        /**
         * This function is not implemented yet.  It is a work in progress.  The
         * intent is as follows:
         *
         * Returns a nonzero value if the mouse movements match the specified pattern.
         * The higher the value, the better the match.  The pattern is a sequence of
         * compass directions (ie, "E", "NE", etc) separated by spaces.  If rot is
         * nonzero, then the pattern is rotated counterclockwise by the specified
         * amount before testing.  Seglen is the minimum length a mouse movement needs
         * to be in order to be considered significant.
         */
        """
        pass

    def popFront(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        pop_front(const PointerEventList self)
        
        /**
         * Discards the first event on the list.
         */
        """
        pass

    def pop_front(self, const_PointerEventList_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        pop_front(const PointerEventList self)
        
        /**
         * Discards the first event on the list.
         */
        """
        pass

    def totalTurns(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        total_turns(PointerEventList self, double sec)
        
        /**
         * returns the total angular deviation that the trail has made in the
         * specified time period.  A small number means that the trail is moving in a
         * relatively straight line, a large number means that the trail is zig-
         * zagging or spinning.  The result is in degrees.
         */
        """
        pass

    def total_turns(self, PointerEventList_self, double_sec): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        total_turns(PointerEventList self, double sec)
        
        /**
         * returns the total angular deviation that the trail has made in the
         * specified time period.  A small number means that the trail is moving in a
         * relatively straight line, a large number means that the trail is zig-
         * zagging or spinning.  The result is in degrees.
         */
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__doc__': '/**\n * Records a set of pointer events that happened recently.  This class is\n * usually used only in the data graph, to transmit the recent pointer\n * presses, but it may be used anywhere a list of PointerEvents is desired.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.PointerEventList' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE2F0C70>'
        'addEvent': None, # (!) real value is "<method 'addEvent' of 'panda3d.core.PointerEventList' objects>"
        'add_event': None, # (!) real value is "<method 'add_event' of 'panda3d.core.PointerEventList' objects>"
        'clear': None, # (!) real value is "<method 'clear' of 'panda3d.core.PointerEventList' objects>"
        'encircles': None, # (!) real value is "<method 'encircles' of 'panda3d.core.PointerEventList' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE2F0C70>)>'
        'getDirection': None, # (!) real value is "<method 'getDirection' of 'panda3d.core.PointerEventList' objects>"
        'getDx': None, # (!) real value is "<method 'getDx' of 'panda3d.core.PointerEventList' objects>"
        'getDy': None, # (!) real value is "<method 'getDy' of 'panda3d.core.PointerEventList' objects>"
        'getInWindow': None, # (!) real value is "<method 'getInWindow' of 'panda3d.core.PointerEventList' objects>"
        'getLength': None, # (!) real value is "<method 'getLength' of 'panda3d.core.PointerEventList' objects>"
        'getNumEvents': None, # (!) real value is "<method 'getNumEvents' of 'panda3d.core.PointerEventList' objects>"
        'getRotation': None, # (!) real value is "<method 'getRotation' of 'panda3d.core.PointerEventList' objects>"
        'getSequence': None, # (!) real value is "<method 'getSequence' of 'panda3d.core.PointerEventList' objects>"
        'getTime': None, # (!) real value is "<method 'getTime' of 'panda3d.core.PointerEventList' objects>"
        'getXpos': None, # (!) real value is "<method 'getXpos' of 'panda3d.core.PointerEventList' objects>"
        'getYpos': None, # (!) real value is "<method 'getYpos' of 'panda3d.core.PointerEventList' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE2F0C70>)>'
        'get_direction': None, # (!) real value is "<method 'get_direction' of 'panda3d.core.PointerEventList' objects>"
        'get_dx': None, # (!) real value is "<method 'get_dx' of 'panda3d.core.PointerEventList' objects>"
        'get_dy': None, # (!) real value is "<method 'get_dy' of 'panda3d.core.PointerEventList' objects>"
        'get_in_window': None, # (!) real value is "<method 'get_in_window' of 'panda3d.core.PointerEventList' objects>"
        'get_length': None, # (!) real value is "<method 'get_length' of 'panda3d.core.PointerEventList' objects>"
        'get_num_events': None, # (!) real value is "<method 'get_num_events' of 'panda3d.core.PointerEventList' objects>"
        'get_rotation': None, # (!) real value is "<method 'get_rotation' of 'panda3d.core.PointerEventList' objects>"
        'get_sequence': None, # (!) real value is "<method 'get_sequence' of 'panda3d.core.PointerEventList' objects>"
        'get_time': None, # (!) real value is "<method 'get_time' of 'panda3d.core.PointerEventList' objects>"
        'get_xpos': None, # (!) real value is "<method 'get_xpos' of 'panda3d.core.PointerEventList' objects>"
        'get_ypos': None, # (!) real value is "<method 'get_ypos' of 'panda3d.core.PointerEventList' objects>"
        'matchPattern': None, # (!) real value is "<method 'matchPattern' of 'panda3d.core.PointerEventList' objects>"
        'match_pattern': None, # (!) real value is "<method 'match_pattern' of 'panda3d.core.PointerEventList' objects>"
        'popFront': None, # (!) real value is "<method 'popFront' of 'panda3d.core.PointerEventList' objects>"
        'pop_front': None, # (!) real value is "<method 'pop_front' of 'panda3d.core.PointerEventList' objects>"
        'totalTurns': None, # (!) real value is "<method 'totalTurns' of 'panda3d.core.PointerEventList' objects>"
        'total_turns': None, # (!) real value is "<method 'total_turns' of 'panda3d.core.PointerEventList' objects>"
    }


