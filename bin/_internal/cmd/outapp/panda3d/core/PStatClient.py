# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


class PStatClient(__dtoolconfig.DTOOL_SUPER_BASE):
    # no doc
    def clientConnect(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        client_connect(const PStatClient self, str hostname, int port)
        
        /**
         * The nonstatic implementation of connect().
         */
        """
        pass

    def clientDisconnect(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        client_disconnect(const PStatClient self)
        
        /**
         * The nonstatic implementation of disconnect().
         */
        """
        pass

    def clientIsConnected(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        client_is_connected(PStatClient self)
        
        /**
         * The nonstatic implementation of is_connected().
         */
        """
        pass

    def clientMainTick(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        client_main_tick(const PStatClient self)
        
        /**
         * A convenience function to call new_frame() on the given PStatClient's main
         * thread, and any other threads with a sync_name of "Main".
         */
        """
        pass

    def clientResumeAfterPause(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        client_resume_after_pause(const PStatClient self)
        
        /**
         * Resumes the PStatClient after the simulation has been paused for a while.
         * This allows the stats to continue exactly where it left off, instead of
         * leaving a big gap that would represent a chug.
         */
        """
        pass

    def clientThreadTick(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        client_thread_tick(const PStatClient self, str sync_name)
        
        /**
         * A convenience function to call new_frame() on all of the threads with the
         * indicated sync name.
         */
        """
        pass

    def client_connect(self, const_PStatClient_self, str_hostname, int_port): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        client_connect(const PStatClient self, str hostname, int port)
        
        /**
         * The nonstatic implementation of connect().
         */
        """
        pass

    def client_disconnect(self, const_PStatClient_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        client_disconnect(const PStatClient self)
        
        /**
         * The nonstatic implementation of disconnect().
         */
        """
        pass

    def client_is_connected(self, PStatClient_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        client_is_connected(PStatClient self)
        
        /**
         * The nonstatic implementation of is_connected().
         */
        """
        pass

    def client_main_tick(self, const_PStatClient_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        client_main_tick(const PStatClient self)
        
        /**
         * A convenience function to call new_frame() on the given PStatClient's main
         * thread, and any other threads with a sync_name of "Main".
         */
        """
        pass

    def client_resume_after_pause(self, const_PStatClient_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        client_resume_after_pause(const PStatClient self)
        
        /**
         * Resumes the PStatClient after the simulation has been paused for a while.
         * This allows the stats to continue exactly where it left off, instead of
         * leaving a big gap that would represent a chug.
         */
        """
        pass

    def client_thread_tick(self, const_PStatClient_self, str_sync_name): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        client_thread_tick(const PStatClient self, str sync_name)
        
        /**
         * A convenience function to call new_frame() on all of the threads with the
         * indicated sync name.
         */
        """
        pass

    def connect(self, str_hostname, int_port): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        connect(str hostname, int port)
        
        /**
         * Attempts to establish a connection to the indicated PStatServer.  Returns
         * true if successful, false on failure.
         */
        """
        pass

    def disconnect(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        disconnect()
        
        /**
         * Closes the connection previously established.
         */
        """
        pass

    def getClientName(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_client_name(PStatClient self)
        
        /**
         * Retrieves the name of the client as set.
         */
        """
        pass

    def getCollector(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_collector(PStatClient self, int index)
        
        /**
         * Returns the nth collector.
         */
        """
        pass

    def getCollectorFullname(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_collector_fullname(PStatClient self, int index)
        
        /**
         * Returns the "full name" of the indicated collector.  This will be the
         * concatenation of all of the collector's parents' names (except Frame) and
         * the collector's own name.
         */
        """
        pass

    def getCollectorName(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_collector_name(PStatClient self, int index)
        
        /**
         * Returns the name of the indicated collector.
         */
        """
        pass

    def getCollectors(self, *args, **kwargs): # real signature unknown
        pass

    def getCurrentThread(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_current_thread(PStatClient self)
        
        /**
         * Returns a handle to the currently-executing thread.  This is the thread
         * that PStatCollectors will be counted in if they do not specify otherwise.
         */
        """
        pass

    def getGlobalPstats(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_global_pstats()
        
        /**
         * Returns a pointer to the global PStatClient object.  It's legal to declare
         * your own PStatClient locally, but it's also convenient to have a global one
         * that everyone can register with.  This is the global one.
         */
        """
        pass

    def getMainThread(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_main_thread(PStatClient self)
        
        /**
         * Returns a handle to the client's Main thread.  This is the thread that
         * started the application.
         */
        """
        pass

    def getMaxRate(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_max_rate(PStatClient self)
        
        /**
         * Returns the maximum number of packets that will be sent to the server per
         * second, per thread.  See set_max_rate().
         */
        """
        pass

    def getNumCollectors(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_collectors(PStatClient self)
        
        /**
         * Returns the total number of collectors the Client knows about.
         */
        """
        pass

    def getNumThreads(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_threads(PStatClient self)
        
        /**
         * Returns the total number of threads the Client knows about.
         */
        """
        pass

    def getRealTime(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_real_time(PStatClient self)
        
        /**
         * Returns the time according to to the PStatClient's clock object.  It keeps
         * its own clock, instead of using the global clock object, so the stats won't
         * get mucked up if you put the global clock in non-real-time mode or
         * something.
         */
        """
        pass

    def getThread(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_thread(PStatClient self, int index)
        
        /**
         * Returns the nth thread.
         */
        """
        pass

    def getThreadName(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_thread_name(PStatClient self, int index)
        
        /**
         * Returns the name of the indicated thread.
         */
        """
        pass

    def getThreadObject(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_thread_object(PStatClient self, int index)
        
        /**
         * Returns the Panda Thread object associated with the indicated PStatThread.
         */
        """
        pass

    def getThreads(self, *args, **kwargs): # real signature unknown
        pass

    def getThreadSyncName(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_thread_sync_name(PStatClient self, int index)
        
        /**
         * Returns the sync_name of the indicated thread.
         */
        """
        pass

    def get_client_name(self, PStatClient_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_client_name(PStatClient self)
        
        /**
         * Retrieves the name of the client as set.
         */
        """
        pass

    def get_collector(self, PStatClient_self, int_index): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_collector(PStatClient self, int index)
        
        /**
         * Returns the nth collector.
         */
        """
        pass

    def get_collectors(self, *args, **kwargs): # real signature unknown
        pass

    def get_collector_fullname(self, PStatClient_self, int_index): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_collector_fullname(PStatClient self, int index)
        
        /**
         * Returns the "full name" of the indicated collector.  This will be the
         * concatenation of all of the collector's parents' names (except Frame) and
         * the collector's own name.
         */
        """
        pass

    def get_collector_name(self, PStatClient_self, int_index): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_collector_name(PStatClient self, int index)
        
        /**
         * Returns the name of the indicated collector.
         */
        """
        pass

    def get_current_thread(self, PStatClient_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_current_thread(PStatClient self)
        
        /**
         * Returns a handle to the currently-executing thread.  This is the thread
         * that PStatCollectors will be counted in if they do not specify otherwise.
         */
        """
        pass

    def get_global_pstats(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_global_pstats()
        
        /**
         * Returns a pointer to the global PStatClient object.  It's legal to declare
         * your own PStatClient locally, but it's also convenient to have a global one
         * that everyone can register with.  This is the global one.
         */
        """
        pass

    def get_main_thread(self, PStatClient_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_main_thread(PStatClient self)
        
        /**
         * Returns a handle to the client's Main thread.  This is the thread that
         * started the application.
         */
        """
        pass

    def get_max_rate(self, PStatClient_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_max_rate(PStatClient self)
        
        /**
         * Returns the maximum number of packets that will be sent to the server per
         * second, per thread.  See set_max_rate().
         */
        """
        pass

    def get_num_collectors(self, PStatClient_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_collectors(PStatClient self)
        
        /**
         * Returns the total number of collectors the Client knows about.
         */
        """
        pass

    def get_num_threads(self, PStatClient_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_threads(PStatClient self)
        
        /**
         * Returns the total number of threads the Client knows about.
         */
        """
        pass

    def get_real_time(self, PStatClient_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_real_time(PStatClient self)
        
        /**
         * Returns the time according to to the PStatClient's clock object.  It keeps
         * its own clock, instead of using the global clock object, so the stats won't
         * get mucked up if you put the global clock in non-real-time mode or
         * something.
         */
        """
        pass

    def get_thread(self, PStatClient_self, int_index): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_thread(PStatClient self, int index)
        
        /**
         * Returns the nth thread.
         */
        """
        pass

    def get_threads(self, *args, **kwargs): # real signature unknown
        pass

    def get_thread_name(self, PStatClient_self, int_index): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_thread_name(PStatClient self, int index)
        
        /**
         * Returns the name of the indicated thread.
         */
        """
        pass

    def get_thread_object(self, PStatClient_self, int_index): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_thread_object(PStatClient self, int index)
        
        /**
         * Returns the Panda Thread object associated with the indicated PStatThread.
         */
        """
        pass

    def get_thread_sync_name(self, PStatClient_self, int_index): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_thread_sync_name(PStatClient self, int index)
        
        /**
         * Returns the sync_name of the indicated thread.
         */
        """
        pass

    def isConnected(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_connected()
        
        /**
         * Returns true if the client believes it is connected to a working
         * PStatServer, false otherwise.
         */
        """
        pass

    def is_connected(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_connected()
        
        /**
         * Returns true if the client believes it is connected to a working
         * PStatServer, false otherwise.
         */
        """
        pass

    def mainTick(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        main_tick()
        
        /**
         * A convenience function to call new_frame() on the global PStatClient's main
         * thread, and any other threads with a sync_name of "Main".
         */
        """
        pass

    def main_tick(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        main_tick()
        
        /**
         * A convenience function to call new_frame() on the global PStatClient's main
         * thread, and any other threads with a sync_name of "Main".
         */
        """
        pass

    def resumeAfterPause(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        resume_after_pause()
        
        /**
         * Resumes the PStatClient after the simulation has been paused for a while.
         * This allows the stats to continue exactly where it left off, instead of
         * leaving a big gap that would represent a chug.
         */
        """
        pass

    def resume_after_pause(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        resume_after_pause()
        
        /**
         * Resumes the PStatClient after the simulation has been paused for a while.
         * This allows the stats to continue exactly where it left off, instead of
         * leaving a big gap that would represent a chug.
         */
        """
        pass

    def setClientName(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_client_name(const PStatClient self, str name)
        
        /**
         * Sets the name of the client.  This is reported to the PStatsServer, and
         * will presumably be written in the title bar or something.
         */
        """
        pass

    def setMaxRate(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_max_rate(const PStatClient self, double rate)
        
        /**
         * Controls the number of packets that will be sent to the server.  Normally,
         * one packet is sent per frame, but this can flood the server with more
         * packets than it can handle if the frame rate is especially good (e.g.  if
         * nothing is onscreen at the moment).  Set this parameter to a reasonable
         * number to prevent this from happening.
         *
         * This number specifies the maximum number of packets that will be sent to
         * the server per second, per thread.
         */
        """
        pass

    def set_client_name(self, const_PStatClient_self, str_name): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_client_name(const PStatClient self, str name)
        
        /**
         * Sets the name of the client.  This is reported to the PStatsServer, and
         * will presumably be written in the title bar or something.
         */
        """
        pass

    def set_max_rate(self, const_PStatClient_self, double_rate): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_max_rate(const PStatClient self, double rate)
        
        /**
         * Controls the number of packets that will be sent to the server.  Normally,
         * one packet is sent per frame, but this can flood the server with more
         * packets than it can handle if the frame rate is especially good (e.g.  if
         * nothing is onscreen at the moment).  Set this parameter to a reasonable
         * number to prevent this from happening.
         *
         * This number specifies the maximum number of packets that will be sent to
         * the server per second, per thread.
         */
        """
        pass

    def threadTick(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        thread_tick(str sync_name)
        
        /**
         * A convenience function to call new_frame() on any threads with the
         * indicated sync_name
         */
        """
        pass

    def thread_tick(self, str_sync_name): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        thread_tick(str sync_name)
        
        /**
         * A convenience function to call new_frame() on any threads with the
         * indicated sync_name
         */
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    client_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    collectors = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    current_thread = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    main_thread = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    max_rate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    real_time = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    threads = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__doc__': None,
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.PStatClient' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE2C93A0>'
        'clientConnect': None, # (!) real value is "<method 'clientConnect' of 'panda3d.core.PStatClient' objects>"
        'clientDisconnect': None, # (!) real value is "<method 'clientDisconnect' of 'panda3d.core.PStatClient' objects>"
        'clientIsConnected': None, # (!) real value is "<method 'clientIsConnected' of 'panda3d.core.PStatClient' objects>"
        'clientMainTick': None, # (!) real value is "<method 'clientMainTick' of 'panda3d.core.PStatClient' objects>"
        'clientResumeAfterPause': None, # (!) real value is "<method 'clientResumeAfterPause' of 'panda3d.core.PStatClient' objects>"
        'clientThreadTick': None, # (!) real value is "<method 'clientThreadTick' of 'panda3d.core.PStatClient' objects>"
        'client_connect': None, # (!) real value is "<method 'client_connect' of 'panda3d.core.PStatClient' objects>"
        'client_disconnect': None, # (!) real value is "<method 'client_disconnect' of 'panda3d.core.PStatClient' objects>"
        'client_is_connected': None, # (!) real value is "<method 'client_is_connected' of 'panda3d.core.PStatClient' objects>"
        'client_main_tick': None, # (!) real value is "<method 'client_main_tick' of 'panda3d.core.PStatClient' objects>"
        'client_name': None, # (!) real value is "<attribute 'client_name' of 'panda3d.core.PStatClient' objects>"
        'client_resume_after_pause': None, # (!) real value is "<method 'client_resume_after_pause' of 'panda3d.core.PStatClient' objects>"
        'client_thread_tick': None, # (!) real value is "<method 'client_thread_tick' of 'panda3d.core.PStatClient' objects>"
        'collectors': None, # (!) real value is "<attribute 'collectors' of 'panda3d.core.PStatClient' objects>"
        'connect': None, # (!) real value is '<staticmethod(<built-in method connect of type object at 0x00007FFCFE2C93A0>)>'
        'current_thread': None, # (!) real value is "<attribute 'current_thread' of 'panda3d.core.PStatClient' objects>"
        'disconnect': None, # (!) real value is '<staticmethod(<built-in method disconnect of type object at 0x00007FFCFE2C93A0>)>'
        'getClientName': None, # (!) real value is "<method 'getClientName' of 'panda3d.core.PStatClient' objects>"
        'getCollector': None, # (!) real value is "<method 'getCollector' of 'panda3d.core.PStatClient' objects>"
        'getCollectorFullname': None, # (!) real value is "<method 'getCollectorFullname' of 'panda3d.core.PStatClient' objects>"
        'getCollectorName': None, # (!) real value is "<method 'getCollectorName' of 'panda3d.core.PStatClient' objects>"
        'getCollectors': None, # (!) real value is "<method 'getCollectors' of 'panda3d.core.PStatClient' objects>"
        'getCurrentThread': None, # (!) real value is "<method 'getCurrentThread' of 'panda3d.core.PStatClient' objects>"
        'getGlobalPstats': None, # (!) real value is '<staticmethod(<built-in method getGlobalPstats of type object at 0x00007FFCFE2C93A0>)>'
        'getMainThread': None, # (!) real value is "<method 'getMainThread' of 'panda3d.core.PStatClient' objects>"
        'getMaxRate': None, # (!) real value is "<method 'getMaxRate' of 'panda3d.core.PStatClient' objects>"
        'getNumCollectors': None, # (!) real value is "<method 'getNumCollectors' of 'panda3d.core.PStatClient' objects>"
        'getNumThreads': None, # (!) real value is "<method 'getNumThreads' of 'panda3d.core.PStatClient' objects>"
        'getRealTime': None, # (!) real value is "<method 'getRealTime' of 'panda3d.core.PStatClient' objects>"
        'getThread': None, # (!) real value is "<method 'getThread' of 'panda3d.core.PStatClient' objects>"
        'getThreadName': None, # (!) real value is "<method 'getThreadName' of 'panda3d.core.PStatClient' objects>"
        'getThreadObject': None, # (!) real value is "<method 'getThreadObject' of 'panda3d.core.PStatClient' objects>"
        'getThreadSyncName': None, # (!) real value is "<method 'getThreadSyncName' of 'panda3d.core.PStatClient' objects>"
        'getThreads': None, # (!) real value is "<method 'getThreads' of 'panda3d.core.PStatClient' objects>"
        'get_client_name': None, # (!) real value is "<method 'get_client_name' of 'panda3d.core.PStatClient' objects>"
        'get_collector': None, # (!) real value is "<method 'get_collector' of 'panda3d.core.PStatClient' objects>"
        'get_collector_fullname': None, # (!) real value is "<method 'get_collector_fullname' of 'panda3d.core.PStatClient' objects>"
        'get_collector_name': None, # (!) real value is "<method 'get_collector_name' of 'panda3d.core.PStatClient' objects>"
        'get_collectors': None, # (!) real value is "<method 'get_collectors' of 'panda3d.core.PStatClient' objects>"
        'get_current_thread': None, # (!) real value is "<method 'get_current_thread' of 'panda3d.core.PStatClient' objects>"
        'get_global_pstats': None, # (!) real value is '<staticmethod(<built-in method get_global_pstats of type object at 0x00007FFCFE2C93A0>)>'
        'get_main_thread': None, # (!) real value is "<method 'get_main_thread' of 'panda3d.core.PStatClient' objects>"
        'get_max_rate': None, # (!) real value is "<method 'get_max_rate' of 'panda3d.core.PStatClient' objects>"
        'get_num_collectors': None, # (!) real value is "<method 'get_num_collectors' of 'panda3d.core.PStatClient' objects>"
        'get_num_threads': None, # (!) real value is "<method 'get_num_threads' of 'panda3d.core.PStatClient' objects>"
        'get_real_time': None, # (!) real value is "<method 'get_real_time' of 'panda3d.core.PStatClient' objects>"
        'get_thread': None, # (!) real value is "<method 'get_thread' of 'panda3d.core.PStatClient' objects>"
        'get_thread_name': None, # (!) real value is "<method 'get_thread_name' of 'panda3d.core.PStatClient' objects>"
        'get_thread_object': None, # (!) real value is "<method 'get_thread_object' of 'panda3d.core.PStatClient' objects>"
        'get_thread_sync_name': None, # (!) real value is "<method 'get_thread_sync_name' of 'panda3d.core.PStatClient' objects>"
        'get_threads': None, # (!) real value is "<method 'get_threads' of 'panda3d.core.PStatClient' objects>"
        'isConnected': None, # (!) real value is '<staticmethod(<built-in method isConnected of type object at 0x00007FFCFE2C93A0>)>'
        'is_connected': None, # (!) real value is '<staticmethod(<built-in method is_connected of type object at 0x00007FFCFE2C93A0>)>'
        'mainTick': None, # (!) real value is '<staticmethod(<built-in method mainTick of type object at 0x00007FFCFE2C93A0>)>'
        'main_thread': None, # (!) real value is "<attribute 'main_thread' of 'panda3d.core.PStatClient' objects>"
        'main_tick': None, # (!) real value is '<staticmethod(<built-in method main_tick of type object at 0x00007FFCFE2C93A0>)>'
        'max_rate': None, # (!) real value is "<attribute 'max_rate' of 'panda3d.core.PStatClient' objects>"
        'real_time': None, # (!) real value is "<attribute 'real_time' of 'panda3d.core.PStatClient' objects>"
        'resumeAfterPause': None, # (!) real value is '<staticmethod(<built-in method resumeAfterPause of type object at 0x00007FFCFE2C93A0>)>'
        'resume_after_pause': None, # (!) real value is '<staticmethod(<built-in method resume_after_pause of type object at 0x00007FFCFE2C93A0>)>'
        'setClientName': None, # (!) real value is "<method 'setClientName' of 'panda3d.core.PStatClient' objects>"
        'setMaxRate': None, # (!) real value is "<method 'setMaxRate' of 'panda3d.core.PStatClient' objects>"
        'set_client_name': None, # (!) real value is "<method 'set_client_name' of 'panda3d.core.PStatClient' objects>"
        'set_max_rate': None, # (!) real value is "<method 'set_max_rate' of 'panda3d.core.PStatClient' objects>"
        'threadTick': None, # (!) real value is '<staticmethod(<built-in method threadTick of type object at 0x00007FFCFE2C93A0>)>'
        'thread_tick': None, # (!) real value is '<staticmethod(<built-in method thread_tick of type object at 0x00007FFCFE2C93A0>)>'
        'threads': None, # (!) real value is "<attribute 'threads' of 'panda3d.core.PStatClient' objects>"
    }


