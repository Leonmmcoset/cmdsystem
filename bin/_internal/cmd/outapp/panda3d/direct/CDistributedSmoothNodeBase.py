# encoding: utf-8
# module panda3d.direct
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\direct.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import panda3d.core as __panda3d_core


class CDistributedSmoothNodeBase(__dtoolconfig.DTOOL_SUPER_BASE):
    """
    /**
     * This class defines some basic methods of DistributedSmoothNodeBase which
     * have been moved into C++ as a performance optimization.
     */
    """
    def broadcastPosHprFull(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        broadcast_pos_hpr_full(const CDistributedSmoothNodeBase self)
        
        /**
         * Examines the complete pos/hpr information to see which of the six elements
         * have changed, and broadcasts the appropriate messages.
         */
        """
        pass

    def broadcastPosHprXy(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        broadcast_pos_hpr_xy(const CDistributedSmoothNodeBase self)
        
        /**
         * Examines only X and Y of the pos/hpr information, and broadcasts the
         * appropriate messages.
         */
        """
        pass

    def broadcastPosHprXyh(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        broadcast_pos_hpr_xyh(const CDistributedSmoothNodeBase self)
        
        /**
         * Examines only X, Y, and H of the pos/hpr information, and broadcasts the
         * appropriate messages.
         */
        """
        pass

    def broadcast_pos_hpr_full(self, const_CDistributedSmoothNodeBase_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        broadcast_pos_hpr_full(const CDistributedSmoothNodeBase self)
        
        /**
         * Examines the complete pos/hpr information to see which of the six elements
         * have changed, and broadcasts the appropriate messages.
         */
        """
        pass

    def broadcast_pos_hpr_xy(self, const_CDistributedSmoothNodeBase_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        broadcast_pos_hpr_xy(const CDistributedSmoothNodeBase self)
        
        /**
         * Examines only X and Y of the pos/hpr information, and broadcasts the
         * appropriate messages.
         */
        """
        pass

    def broadcast_pos_hpr_xyh(self, const_CDistributedSmoothNodeBase_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        broadcast_pos_hpr_xyh(const CDistributedSmoothNodeBase self)
        
        /**
         * Examines only X, Y, and H of the pos/hpr information, and broadcasts the
         * appropriate messages.
         */
        """
        pass

    def initialize(self, const_CDistributedSmoothNodeBase_self, const_NodePath_node_path, DCClass_dclass, long_do_id): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        initialize(const CDistributedSmoothNodeBase self, const NodePath node_path, DCClass dclass, long do_id)
        
        /**
         * Initializes the internal structures from some constructs that are normally
         * stored only in Python.  Also reads the current node's pos & hpr values in
         * preparation for transmitting them via one of the broadcast_pos_hpr_*()
         * methods.
         */
        """
        pass

    def printCurrL(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        print_curr_l(const CDistributedSmoothNodeBase self)
        """
        pass

    def print_curr_l(self, const_CDistributedSmoothNodeBase_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        print_curr_l(const CDistributedSmoothNodeBase self)
        """
        pass

    def sendEverything(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        send_everything(const CDistributedSmoothNodeBase self)
        
        /**
         * Broadcasts the current pos/hpr in its complete form.
         */
        """
        pass

    def send_everything(self, const_CDistributedSmoothNodeBase_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        send_everything(const CDistributedSmoothNodeBase self)
        
        /**
         * Broadcasts the current pos/hpr in its complete form.
         */
        """
        pass

    def setClockDelta(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_clock_delta(const CDistributedSmoothNodeBase self, object clock_delta)
        
        /**
         * Tells the C++ instance definition about the global ClockDelta object.
         */
        """
        pass

    def setCurrL(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_curr_l(const CDistributedSmoothNodeBase self, long l)
        
        /**
         * Appends the timestamp and sends the update.
         */
        """
        pass

    def setRepository(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_repository(const CDistributedSmoothNodeBase self, CConnectionRepository repository, bool is_ai, long ai_id)
        
        /**
         * Tells the C++ instance definition about the AI or Client repository, used
         * for sending datagrams.
         */
        """
        pass

    def set_clock_delta(self, const_CDistributedSmoothNodeBase_self, object_clock_delta): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_clock_delta(const CDistributedSmoothNodeBase self, object clock_delta)
        
        /**
         * Tells the C++ instance definition about the global ClockDelta object.
         */
        """
        pass

    def set_curr_l(self, const_CDistributedSmoothNodeBase_self, long_l): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_curr_l(const CDistributedSmoothNodeBase self, long l)
        
        /**
         * Appends the timestamp and sends the update.
         */
        """
        pass

    def set_repository(self, const_CDistributedSmoothNodeBase_self, CConnectionRepository_repository, bool_is_ai, long_ai_id): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_repository(const CDistributedSmoothNodeBase self, CConnectionRepository repository, bool is_ai, long ai_id)
        
        /**
         * Tells the C++ instance definition about the AI or Client repository, used
         * for sending datagrams.
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
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.direct.CDistributedSmoothNodeBase' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.direct.CDistributedSmoothNodeBase' objects>"
        '__doc__': '/**\n * This class defines some basic methods of DistributedSmoothNodeBase which\n * have been moved into C++ as a performance optimization.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.direct.CDistributedSmoothNodeBase' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFDC68EA440>'
        'broadcastPosHprFull': None, # (!) real value is "<method 'broadcastPosHprFull' of 'panda3d.direct.CDistributedSmoothNodeBase' objects>"
        'broadcastPosHprXy': None, # (!) real value is "<method 'broadcastPosHprXy' of 'panda3d.direct.CDistributedSmoothNodeBase' objects>"
        'broadcastPosHprXyh': None, # (!) real value is "<method 'broadcastPosHprXyh' of 'panda3d.direct.CDistributedSmoothNodeBase' objects>"
        'broadcast_pos_hpr_full': None, # (!) real value is "<method 'broadcast_pos_hpr_full' of 'panda3d.direct.CDistributedSmoothNodeBase' objects>"
        'broadcast_pos_hpr_xy': None, # (!) real value is "<method 'broadcast_pos_hpr_xy' of 'panda3d.direct.CDistributedSmoothNodeBase' objects>"
        'broadcast_pos_hpr_xyh': None, # (!) real value is "<method 'broadcast_pos_hpr_xyh' of 'panda3d.direct.CDistributedSmoothNodeBase' objects>"
        'initialize': None, # (!) real value is "<method 'initialize' of 'panda3d.direct.CDistributedSmoothNodeBase' objects>"
        'printCurrL': None, # (!) real value is "<method 'printCurrL' of 'panda3d.direct.CDistributedSmoothNodeBase' objects>"
        'print_curr_l': None, # (!) real value is "<method 'print_curr_l' of 'panda3d.direct.CDistributedSmoothNodeBase' objects>"
        'sendEverything': None, # (!) real value is "<method 'sendEverything' of 'panda3d.direct.CDistributedSmoothNodeBase' objects>"
        'send_everything': None, # (!) real value is "<method 'send_everything' of 'panda3d.direct.CDistributedSmoothNodeBase' objects>"
        'setClockDelta': None, # (!) real value is "<method 'setClockDelta' of 'panda3d.direct.CDistributedSmoothNodeBase' objects>"
        'setCurrL': None, # (!) real value is "<method 'setCurrL' of 'panda3d.direct.CDistributedSmoothNodeBase' objects>"
        'setRepository': None, # (!) real value is "<method 'setRepository' of 'panda3d.direct.CDistributedSmoothNodeBase' objects>"
        'set_clock_delta': None, # (!) real value is "<method 'set_clock_delta' of 'panda3d.direct.CDistributedSmoothNodeBase' objects>"
        'set_curr_l': None, # (!) real value is "<method 'set_curr_l' of 'panda3d.direct.CDistributedSmoothNodeBase' objects>"
        'set_repository': None, # (!) real value is "<method 'set_repository' of 'panda3d.direct.CDistributedSmoothNodeBase' objects>"
    }


