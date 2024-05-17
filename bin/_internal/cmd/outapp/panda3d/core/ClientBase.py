# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .TypedReferenceCount import TypedReferenceCount

class ClientBase(TypedReferenceCount):
    """
    /**
     * An abstract base class for a family of client device interfaces--including
     * trackers, buttons, dials, and other analog inputs.
     *
     * This provides a common interface to connect to such devices and extract
     * their data; it is used by TrackerNode etc.  to put these devices in the
     * data graph.
     */
    """
    def forkAsynchronousThread(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        fork_asynchronous_thread(const ClientBase self, double poll_time)
        
        /**
         * Forks a separate thread to do all the polling of connected devices.  The
         * forked thread will poll after every poll_time seconds has elapsed.  Returns
         * true if the fork was successful, or false otherwise (for instance, because
         * we were already forked, or because asynchronous threads are disabled).
         */
        """
        pass

    def fork_asynchronous_thread(self, const_ClientBase_self, double_poll_time): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        fork_asynchronous_thread(const ClientBase self, double poll_time)
        
        /**
         * Forks a separate thread to do all the polling of connected devices.  The
         * forked thread will poll after every poll_time seconds has elapsed.  Returns
         * true if the fork was successful, or false otherwise (for instance, because
         * we were already forked, or because asynchronous threads are disabled).
         */
        """
        pass

    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getCoordinateSystem(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_coordinate_system(ClientBase self)
        
        /**
         * Returns the coordinate system that all devices associated with this client
         * will operate in.  Normally, this is CS_default.
         */
        """
        pass

    def getLastPollTime(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_last_poll_time(ClientBase self)
        
        /**
         * Returns the time (according to the global ClockObject's get_real_time()
         * method) of the last device poll.
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_coordinate_system(self, ClientBase_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_coordinate_system(ClientBase self)
        
        /**
         * Returns the coordinate system that all devices associated with this client
         * will operate in.  Normally, this is CS_default.
         */
        """
        pass

    def get_last_poll_time(self, ClientBase_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_last_poll_time(ClientBase self)
        
        /**
         * Returns the time (according to the global ClockObject's get_real_time()
         * method) of the last device poll.
         */
        """
        pass

    def isForked(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_forked(ClientBase self)
        
        /**
         * Returns true if the ClientBase has been forked (and, therefore, poll() does
         * not need to be called), false otherwise.
         */
        """
        pass

    def is_forked(self, ClientBase_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_forked(ClientBase self)
        
        /**
         * Returns true if the ClientBase has been forked (and, therefore, poll() does
         * not need to be called), false otherwise.
         */
        """
        pass

    def poll(self, const_ClientBase_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        poll(const ClientBase self)
        
        /**
         * Initiates a poll of the client devices, if we are not forked and if we have
         * not already polled this frame.  Returns true if the poll occurred, or false
         * if it did not.
         */
        """
        pass

    def setCoordinateSystem(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_coordinate_system(const ClientBase self, int cs)
        
        /**
         * Specifies the coordinate system that all devices associated with this
         * client will operate in.  Normally, this is CS_default.
         */
        """
        pass

    def set_coordinate_system(self, const_ClientBase_self, int_cs): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_coordinate_system(const ClientBase self, int cs)
        
        /**
         * Specifies the coordinate system that all devices associated with this
         * client will operate in.  Normally, this is CS_default.
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
        '__doc__': '/**\n * An abstract base class for a family of client device interfaces--including\n * trackers, buttons, dials, and other analog inputs.\n *\n * This provides a common interface to connect to such devices and extract\n * their data; it is used by TrackerNode etc.  to put these devices in the\n * data graph.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.ClientBase' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE2D6840>'
        'forkAsynchronousThread': None, # (!) real value is "<method 'forkAsynchronousThread' of 'panda3d.core.ClientBase' objects>"
        'fork_asynchronous_thread': None, # (!) real value is "<method 'fork_asynchronous_thread' of 'panda3d.core.ClientBase' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE2D6840>)>'
        'getCoordinateSystem': None, # (!) real value is "<method 'getCoordinateSystem' of 'panda3d.core.ClientBase' objects>"
        'getLastPollTime': None, # (!) real value is "<method 'getLastPollTime' of 'panda3d.core.ClientBase' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE2D6840>)>'
        'get_coordinate_system': None, # (!) real value is "<method 'get_coordinate_system' of 'panda3d.core.ClientBase' objects>"
        'get_last_poll_time': None, # (!) real value is "<method 'get_last_poll_time' of 'panda3d.core.ClientBase' objects>"
        'isForked': None, # (!) real value is "<method 'isForked' of 'panda3d.core.ClientBase' objects>"
        'is_forked': None, # (!) real value is "<method 'is_forked' of 'panda3d.core.ClientBase' objects>"
        'poll': None, # (!) real value is "<method 'poll' of 'panda3d.core.ClientBase' objects>"
        'setCoordinateSystem': None, # (!) real value is "<method 'setCoordinateSystem' of 'panda3d.core.ClientBase' objects>"
        'set_coordinate_system': None, # (!) real value is "<method 'set_coordinate_system' of 'panda3d.core.ClientBase' objects>"
    }


