# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .TypedReferenceCount import TypedReferenceCount

from .Namable import Namable

class Thread(TypedReferenceCount, Namable):
    """
    /**
     * A thread; that is, a lightweight process.  This is an abstract base class;
     * to use it, you must subclass from it and redefine thread_main().
     *
     * The thread itself will keep a reference count on the Thread object while it
     * is running; when the thread returns from its root function, the Thread
     * object will automatically be destructed if no other pointers are
     * referencing it.
     */
    """
    def bindThread(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        bind_thread(str name, str sync_name)
        
        /**
         * Returns a new Panda Thread object associated with the current thread (which
         * has been created externally). This can be used to bind a unique Panda
         * Thread object with an external thread, such as a new Python thread.
         *
         * It is particularly useful to bind a Panda Thread object to an external
         * thread for the purposes of PStats monitoring.  Without this call, each
         * external thread will be assigned the same global ExternalThread object,
         * which means they will all appear in the same PStats graph.
         *
         * It is the caller's responsibility to save the returned Thread pointer for
         * the lifetime of the external thread.  It is an error for the Thread pointer
         * to destruct while the external thread is still in the system.
         *
         * It is also an error to call this method from the main thread, or twice
         * within a given thread, unless it is given the same name each time (in which
         * case the same pointer will be returned each time).
         */
        """
        pass

    def bind_thread(self, str_name, str_sync_name): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        bind_thread(str name, str sync_name)
        
        /**
         * Returns a new Panda Thread object associated with the current thread (which
         * has been created externally). This can be used to bind a unique Panda
         * Thread object with an external thread, such as a new Python thread.
         *
         * It is particularly useful to bind a Panda Thread object to an external
         * thread for the purposes of PStats monitoring.  Without this call, each
         * external thread will be assigned the same global ExternalThread object,
         * which means they will all appear in the same PStats graph.
         *
         * It is the caller's responsibility to save the returned Thread pointer for
         * the lifetime of the external thread.  It is an error for the Thread pointer
         * to destruct while the external thread is still in the system.
         *
         * It is also an error to call this method from the main thread, or twice
         * within a given thread, unless it is given the same name each time (in which
         * case the same pointer will be returned each time).
         */
        """
        pass

    def considerYield(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        consider_yield()
        
        /**
         * Possibly suspends the current thread for the rest of the current epoch, if
         * it has run for enough this epoch.  This is especially important for the
         * simple thread implementation, which relies on cooperative yields like this.
         */
        """
        pass

    def consider_yield(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        consider_yield()
        
        /**
         * Possibly suspends the current thread for the rest of the current epoch, if
         * it has run for enough this epoch.  This is especially important for the
         * simple thread implementation, which relies on cooperative yields like this.
         */
        """
        pass

    def forceYield(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        force_yield()
        
        /**
         * Suspends the current thread for the rest of the current epoch.
         */
        """
        pass

    def force_yield(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        force_yield()
        
        /**
         * Suspends the current thread for the rest of the current epoch.
         */
        """
        pass

    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getCurrentPipelineStage(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_current_pipeline_stage()
        
        /**
         * Returns the integer pipeline stage associated with the current thread.
         * This is the same thing as get_current_thread()->get_pipeline_stage(), but
         * it may be faster to retrieve in some contexts.
         */
        """
        pass

    def getCurrentTask(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_current_task(Thread self)
        
        /**
         * Returns the task currently executing on this thread (via the
         * AsyncTaskManager), if any, or NULL if the thread is not currently servicing
         * a task.
         */
        """
        pass

    def getCurrentThread(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_current_thread()
        
        /**
         * Returns a pointer to the currently-executing Thread object.  If this is
         * called from the main thread, this will return the same value as
         * get_main_thread().
         *
         * This will always return some valid Thread pointer.  It will never return
         * NULL, even if the current thread was spawned outside of Panda's threading
         * system, although all non-Panda threads will return the exact same Thread
         * pointer.
         */
        """
        pass

    def getExternalThread(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_external_thread()
        
        /**
         * Returns a pointer to the "external" Thread object--this is a special Thread
         * object that corresponds to any thread spawned outside of Panda's threading
         * interface.  Note that multiple different threads may share this same
         * pointer.
         */
        """
        pass

    def getMainThread(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_main_thread()
        
        /**
         * Returns a pointer to the "main" Thread object--this is the Thread that
         * started the whole process.
         */
        """
        pass

    def getPipelineStage(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_pipeline_stage(Thread self)
        
        /**
         * Returns the Pipeline stage number associated with this thread.  The default
         * stage is 0 if no stage is specified otherwise.  See set_pipeline_stage().
         */
        """
        pass

    def getPstatsIndex(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_pstats_index(Thread self)
        
        /**
         * Returns the PStats index associated with this thread, or -1 if no index has
         * yet been associated with this thread.  This is used internally by the
         * PStatClient; you should not need to call this directly.
         */
        """
        pass

    def getPythonIndex(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_python_index(Thread self)
        
        /**
         * Returns the Python index associated with this thread, or -1 if no index has
         * yet been associated with this thread.  This is used internally by the
         * direct.stdpy.thread module; you should not need to call this directly.
         */
        """
        pass

    def getSyncName(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_sync_name(Thread self)
        
        /**
         * Returns the sync name of the thread.  This name collects threads into "sync
         * groups", which are expected to run synchronously.  This is mainly used for
         * the benefit of PStats; threads with the same sync name can be ticked all at
         * once via the thread_tick() call.
         */
        """
        pass

    def getUniqueId(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_unique_id(Thread self)
        
        /**
         * Returns a string that is guaranteed to be unique to this thread, across all
         * processes on the machine, during at least the lifetime of this process.
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_current_pipeline_stage(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_current_pipeline_stage()
        
        /**
         * Returns the integer pipeline stage associated with the current thread.
         * This is the same thing as get_current_thread()->get_pipeline_stage(), but
         * it may be faster to retrieve in some contexts.
         */
        """
        pass

    def get_current_task(self, Thread_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_current_task(Thread self)
        
        /**
         * Returns the task currently executing on this thread (via the
         * AsyncTaskManager), if any, or NULL if the thread is not currently servicing
         * a task.
         */
        """
        pass

    def get_current_thread(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_current_thread()
        
        /**
         * Returns a pointer to the currently-executing Thread object.  If this is
         * called from the main thread, this will return the same value as
         * get_main_thread().
         *
         * This will always return some valid Thread pointer.  It will never return
         * NULL, even if the current thread was spawned outside of Panda's threading
         * system, although all non-Panda threads will return the exact same Thread
         * pointer.
         */
        """
        pass

    def get_external_thread(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_external_thread()
        
        /**
         * Returns a pointer to the "external" Thread object--this is a special Thread
         * object that corresponds to any thread spawned outside of Panda's threading
         * interface.  Note that multiple different threads may share this same
         * pointer.
         */
        """
        pass

    def get_main_thread(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_main_thread()
        
        /**
         * Returns a pointer to the "main" Thread object--this is the Thread that
         * started the whole process.
         */
        """
        pass

    def get_pipeline_stage(self, Thread_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_pipeline_stage(Thread self)
        
        /**
         * Returns the Pipeline stage number associated with this thread.  The default
         * stage is 0 if no stage is specified otherwise.  See set_pipeline_stage().
         */
        """
        pass

    def get_pstats_index(self, Thread_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_pstats_index(Thread self)
        
        /**
         * Returns the PStats index associated with this thread, or -1 if no index has
         * yet been associated with this thread.  This is used internally by the
         * PStatClient; you should not need to call this directly.
         */
        """
        pass

    def get_python_index(self, Thread_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_python_index(Thread self)
        
        /**
         * Returns the Python index associated with this thread, or -1 if no index has
         * yet been associated with this thread.  This is used internally by the
         * direct.stdpy.thread module; you should not need to call this directly.
         */
        """
        pass

    def get_sync_name(self, Thread_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_sync_name(Thread self)
        
        /**
         * Returns the sync name of the thread.  This name collects threads into "sync
         * groups", which are expected to run synchronously.  This is mainly used for
         * the benefit of PStats; threads with the same sync name can be ticked all at
         * once via the thread_tick() call.
         */
        """
        pass

    def get_unique_id(self, Thread_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_unique_id(Thread self)
        
        /**
         * Returns a string that is guaranteed to be unique to this thread, across all
         * processes on the machine, during at least the lifetime of this process.
         */
        """
        pass

    def isJoinable(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_joinable(Thread self)
        
        /**
         * Returns the value of joinable that was passed to the start() call.
         */
        """
        pass

    def isSimpleThreads(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_simple_threads()
        
        /**
         * Returns true if Panda is currently compiled for "simple threads", which is
         * to say, cooperative context switching only, reducing the need for quite so
         * many critical section protections.  This is not necessarily the opposite of
         * "true threads", since one possible implementation of simple threads is via
         * true threads with mutex protection to ensure only one runs at a time.
         */
        """
        pass

    def isStarted(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_started(Thread self)
        
        /**
         * Returns true if the thread has been started, false if it has not, or if
         * join() has already been called.
         */
        """
        pass

    def isThreadingSupported(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_threading_supported()
        
        /**
         * Returns true if threading support has been compiled in and enabled, or
         * false if no threading is available (and Thread::start() will always fail).
         */
        """
        pass

    def isTrueThreads(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_true_threads()
        
        /**
         * Returns true if a real threading library is available that supports actual
         * OS-implemented threads, or false if the only threading we can provide is
         * simulated user-space threading.
         */
        """
        pass

    def is_joinable(self, Thread_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_joinable(Thread self)
        
        /**
         * Returns the value of joinable that was passed to the start() call.
         */
        """
        pass

    def is_simple_threads(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_simple_threads()
        
        /**
         * Returns true if Panda is currently compiled for "simple threads", which is
         * to say, cooperative context switching only, reducing the need for quite so
         * many critical section protections.  This is not necessarily the opposite of
         * "true threads", since one possible implementation of simple threads is via
         * true threads with mutex protection to ensure only one runs at a time.
         */
        """
        pass

    def is_started(self, Thread_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_started(Thread self)
        
        /**
         * Returns true if the thread has been started, false if it has not, or if
         * join() has already been called.
         */
        """
        pass

    def is_threading_supported(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_threading_supported()
        
        /**
         * Returns true if threading support has been compiled in and enabled, or
         * false if no threading is available (and Thread::start() will always fail).
         */
        """
        pass

    def is_true_threads(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_true_threads()
        
        /**
         * Returns true if a real threading library is available that supports actual
         * OS-implemented threads, or false if the only threading we can provide is
         * simulated user-space threading.
         */
        """
        pass

    def join(self, const_Thread_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        join(const Thread self)
        
        /**
         * Blocks the calling process until the thread terminates.  If the thread has
         * already terminated, this returns immediately.
         */
        """
        pass

    def output(self, Thread_self, ostream_out): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        output(Thread self, ostream out)
        
        /**
         *
         */
        """
        pass

    def outputBlocker(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        output_blocker(Thread self, ostream out)
        
        /**
         * Writes a description of the mutex or condition variable that this thread is
         * blocked on.  Writes nothing if there is no blocker, or if we are not in
         * DEBUG_THREADS mode.
         */
        """
        pass

    def output_blocker(self, Thread_self, ostream_out): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        output_blocker(Thread self, ostream out)
        
        /**
         * Writes a description of the mutex or condition variable that this thread is
         * blocked on.  Writes nothing if there is no blocker, or if we are not in
         * DEBUG_THREADS mode.
         */
        """
        pass

    def preempt(self, const_Thread_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        preempt(const Thread self)
        
        /**
         * Indicates that this thread should run as soon as possible, preemptying any
         * other threads that may be scheduled to run.  This may not be implemented on
         * every platform.
         */
        """
        pass

    def prepareForExit(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        prepare_for_exit()
        
        /**
         * Should be called by the main thread just before exiting the program, this
         * blocks until any remaining thread cleanup has finished.
         */
        """
        pass

    def prepare_for_exit(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        prepare_for_exit()
        
        /**
         * Should be called by the main thread just before exiting the program, this
         * blocks until any remaining thread cleanup has finished.
         */
        """
        pass

    def setMinPipelineStage(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_min_pipeline_stage(const Thread self, int min_pipeline_stage)
        
        /**
         * Sets this thread's pipeline stage number to at least the indicated value,
         * unless it is already larger.  See set_pipeline_stage().
         */
        """
        pass

    def setPipelineStage(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_pipeline_stage(const Thread self, int pipeline_stage)
        
        /**
         * Specifies the Pipeline stage number associated with this thread.  The
         * default stage is 0 if no stage is specified otherwise.
         *
         * This must be a value in the range [0 .. pipeline->get_num_stages() - 1].
         * It specifies the values that this thread observes for all pipelined data.
         * Typically, an application thread will leave this at 0, but a render thread
         * may set it to 1 or 2 (to operate on the previous frame's data, or the
         * second previous frame's data).
         */
        """
        pass

    def setPythonIndex(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_python_index(const Thread self, int index)
        
        /**
         * Stores a Python index to be associated with this thread.  This is used
         * internally by the thread module; you should not need to call this directly.
         */
        """
        pass

    def set_min_pipeline_stage(self, const_Thread_self, int_min_pipeline_stage): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_min_pipeline_stage(const Thread self, int min_pipeline_stage)
        
        /**
         * Sets this thread's pipeline stage number to at least the indicated value,
         * unless it is already larger.  See set_pipeline_stage().
         */
        """
        pass

    def set_pipeline_stage(self, const_Thread_self, int_pipeline_stage): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_pipeline_stage(const Thread self, int pipeline_stage)
        
        /**
         * Specifies the Pipeline stage number associated with this thread.  The
         * default stage is 0 if no stage is specified otherwise.
         *
         * This must be a value in the range [0 .. pipeline->get_num_stages() - 1].
         * It specifies the values that this thread observes for all pipelined data.
         * Typically, an application thread will leave this at 0, but a render thread
         * may set it to 1 or 2 (to operate on the previous frame's data, or the
         * second previous frame's data).
         */
        """
        pass

    def set_python_index(self, const_Thread_self, int_index): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_python_index(const Thread self, int index)
        
        /**
         * Stores a Python index to be associated with this thread.  This is used
         * internally by the thread module; you should not need to call this directly.
         */
        """
        pass

    def sleep(self, double_seconds): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        sleep(double seconds)
        
        /**
         * Suspends the current thread for at least the indicated amount of time.  It
         * might be suspended for longer.
         */
        """
        pass

    def start(self, const_Thread_self, int_priority, bool_joinable): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        start(const Thread self, int priority, bool joinable)
        
        /**
         * Starts the thread executing.  It is only valid to call this once.
         *
         * The thread will begin executing its thread_main() function, and will
         * terminate when thread_main() returns.
         *
         * priority is intended as a hint to the relative importance of this thread.
         * This may be ignored by the thread implementation.
         *
         * joinable should be set true if you intend to call join() to wait for the
         * thread to terminate, or false if you don't care and you will never call
         * join(). Note that the reference count on the Thread object is incremented
         * while the thread itself is running, so if you just want to fire and forget
         * a thread, you may pass joinable = false, and never store the Thread object.
         * It will automatically destruct itself when it finishes.
         *
         * The return value is true if the thread is successfully started, false
         * otherwise.
         */
        """
        pass

    def upcastToNamable(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        upcast_to_Namable(const Thread self)
        
        upcast from Thread to Namable
        """
        pass

    def upcastToTypedReferenceCount(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        upcast_to_TypedReferenceCount(const Thread self)
        
        upcast from Thread to TypedReferenceCount
        """
        pass

    def upcast_to_Namable(self, const_Thread_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        upcast_to_Namable(const Thread self)
        
        upcast from Thread to Namable
        """
        pass

    def upcast_to_TypedReferenceCount(self, const_Thread_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        upcast_to_TypedReferenceCount(const Thread self)
        
        upcast from Thread to TypedReferenceCount
        """
        pass

    def writeStatus(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        write_status(ostream out)
        
        /**
         *
         */
        """
        pass

    def write_status(self, ostream_out): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        write_status(ostream out)
        
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

    current_task = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    joinable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pipeline_stage = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pstats_index = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    python_index = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    started = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    sync_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    unique_id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    current_pipeline_stage = 0
    current_thread = None # (!) real value is 'MainThread Main'
    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__doc__': '/**\n * A thread; that is, a lightweight process.  This is an abstract base class;\n * to use it, you must subclass from it and redefine thread_main().\n *\n * The thread itself will keep a reference count on the Thread object while it\n * is running; when the thread returns from its root function, the Thread\n * object will automatically be destructed if no other pointers are\n * referencing it.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.Thread' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE2EB160>'
        '__repr__': None, # (!) real value is "<slot wrapper '__repr__' of 'panda3d.core.Thread' objects>"
        '__str__': None, # (!) real value is "<slot wrapper '__str__' of 'panda3d.core.Thread' objects>"
        'bindThread': None, # (!) real value is '<staticmethod(<built-in method bindThread of type object at 0x00007FFCFE2EB160>)>'
        'bind_thread': None, # (!) real value is '<staticmethod(<built-in method bind_thread of type object at 0x00007FFCFE2EB160>)>'
        'considerYield': None, # (!) real value is '<staticmethod(<built-in method considerYield of type object at 0x00007FFCFE2EB160>)>'
        'consider_yield': None, # (!) real value is '<staticmethod(<built-in method consider_yield of type object at 0x00007FFCFE2EB160>)>'
        'current_pipeline_stage': None, # (!) real value is "<attribute 'current_pipeline_stage' of 'panda3d.core.Thread'>"
        'current_task': None, # (!) real value is "<attribute 'current_task' of 'panda3d.core.Thread' objects>"
        'current_thread': None, # (!) real value is "<attribute 'current_thread' of 'panda3d.core.Thread'>"
        'external_thread': None, # (!) real value is "<attribute 'external_thread' of 'panda3d.core.Thread'>"
        'forceYield': None, # (!) real value is '<staticmethod(<built-in method forceYield of type object at 0x00007FFCFE2EB160>)>'
        'force_yield': None, # (!) real value is '<staticmethod(<built-in method force_yield of type object at 0x00007FFCFE2EB160>)>'
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE2EB160>)>'
        'getCurrentPipelineStage': None, # (!) real value is '<staticmethod(<built-in method getCurrentPipelineStage of type object at 0x00007FFCFE2EB160>)>'
        'getCurrentTask': None, # (!) real value is "<method 'getCurrentTask' of 'panda3d.core.Thread' objects>"
        'getCurrentThread': None, # (!) real value is '<staticmethod(<built-in method getCurrentThread of type object at 0x00007FFCFE2EB160>)>'
        'getExternalThread': None, # (!) real value is '<staticmethod(<built-in method getExternalThread of type object at 0x00007FFCFE2EB160>)>'
        'getMainThread': None, # (!) real value is '<staticmethod(<built-in method getMainThread of type object at 0x00007FFCFE2EB160>)>'
        'getPipelineStage': None, # (!) real value is "<method 'getPipelineStage' of 'panda3d.core.Thread' objects>"
        'getPstatsIndex': None, # (!) real value is "<method 'getPstatsIndex' of 'panda3d.core.Thread' objects>"
        'getPythonIndex': None, # (!) real value is "<method 'getPythonIndex' of 'panda3d.core.Thread' objects>"
        'getSyncName': None, # (!) real value is "<method 'getSyncName' of 'panda3d.core.Thread' objects>"
        'getUniqueId': None, # (!) real value is "<method 'getUniqueId' of 'panda3d.core.Thread' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE2EB160>)>'
        'get_current_pipeline_stage': None, # (!) real value is '<staticmethod(<built-in method get_current_pipeline_stage of type object at 0x00007FFCFE2EB160>)>'
        'get_current_task': None, # (!) real value is "<method 'get_current_task' of 'panda3d.core.Thread' objects>"
        'get_current_thread': None, # (!) real value is '<staticmethod(<built-in method get_current_thread of type object at 0x00007FFCFE2EB160>)>'
        'get_external_thread': None, # (!) real value is '<staticmethod(<built-in method get_external_thread of type object at 0x00007FFCFE2EB160>)>'
        'get_main_thread': None, # (!) real value is '<staticmethod(<built-in method get_main_thread of type object at 0x00007FFCFE2EB160>)>'
        'get_pipeline_stage': None, # (!) real value is "<method 'get_pipeline_stage' of 'panda3d.core.Thread' objects>"
        'get_pstats_index': None, # (!) real value is "<method 'get_pstats_index' of 'panda3d.core.Thread' objects>"
        'get_python_index': None, # (!) real value is "<method 'get_python_index' of 'panda3d.core.Thread' objects>"
        'get_sync_name': None, # (!) real value is "<method 'get_sync_name' of 'panda3d.core.Thread' objects>"
        'get_unique_id': None, # (!) real value is "<method 'get_unique_id' of 'panda3d.core.Thread' objects>"
        'isJoinable': None, # (!) real value is "<method 'isJoinable' of 'panda3d.core.Thread' objects>"
        'isSimpleThreads': None, # (!) real value is '<staticmethod(<built-in method isSimpleThreads of type object at 0x00007FFCFE2EB160>)>'
        'isStarted': None, # (!) real value is "<method 'isStarted' of 'panda3d.core.Thread' objects>"
        'isThreadingSupported': None, # (!) real value is '<staticmethod(<built-in method isThreadingSupported of type object at 0x00007FFCFE2EB160>)>'
        'isTrueThreads': None, # (!) real value is '<staticmethod(<built-in method isTrueThreads of type object at 0x00007FFCFE2EB160>)>'
        'is_joinable': None, # (!) real value is "<method 'is_joinable' of 'panda3d.core.Thread' objects>"
        'is_simple_threads': None, # (!) real value is '<staticmethod(<built-in method is_simple_threads of type object at 0x00007FFCFE2EB160>)>'
        'is_started': None, # (!) real value is "<method 'is_started' of 'panda3d.core.Thread' objects>"
        'is_threading_supported': None, # (!) real value is '<staticmethod(<built-in method is_threading_supported of type object at 0x00007FFCFE2EB160>)>'
        'is_true_threads': None, # (!) real value is '<staticmethod(<built-in method is_true_threads of type object at 0x00007FFCFE2EB160>)>'
        'join': None, # (!) real value is "<method 'join' of 'panda3d.core.Thread' objects>"
        'joinable': None, # (!) real value is "<attribute 'joinable' of 'panda3d.core.Thread' objects>"
        'main_thread': None, # (!) real value is "<attribute 'main_thread' of 'panda3d.core.Thread'>"
        'output': None, # (!) real value is "<method 'output' of 'panda3d.core.Thread' objects>"
        'outputBlocker': None, # (!) real value is "<method 'outputBlocker' of 'panda3d.core.Thread' objects>"
        'output_blocker': None, # (!) real value is "<method 'output_blocker' of 'panda3d.core.Thread' objects>"
        'pipeline_stage': None, # (!) real value is "<attribute 'pipeline_stage' of 'panda3d.core.Thread' objects>"
        'preempt': None, # (!) real value is "<method 'preempt' of 'panda3d.core.Thread' objects>"
        'prepareForExit': None, # (!) real value is '<staticmethod(<built-in method prepareForExit of type object at 0x00007FFCFE2EB160>)>'
        'prepare_for_exit': None, # (!) real value is '<staticmethod(<built-in method prepare_for_exit of type object at 0x00007FFCFE2EB160>)>'
        'pstats_index': None, # (!) real value is "<attribute 'pstats_index' of 'panda3d.core.Thread' objects>"
        'python_index': None, # (!) real value is "<attribute 'python_index' of 'panda3d.core.Thread' objects>"
        'setMinPipelineStage': None, # (!) real value is "<method 'setMinPipelineStage' of 'panda3d.core.Thread' objects>"
        'setPipelineStage': None, # (!) real value is "<method 'setPipelineStage' of 'panda3d.core.Thread' objects>"
        'setPythonIndex': None, # (!) real value is "<method 'setPythonIndex' of 'panda3d.core.Thread' objects>"
        'set_min_pipeline_stage': None, # (!) real value is "<method 'set_min_pipeline_stage' of 'panda3d.core.Thread' objects>"
        'set_pipeline_stage': None, # (!) real value is "<method 'set_pipeline_stage' of 'panda3d.core.Thread' objects>"
        'set_python_index': None, # (!) real value is "<method 'set_python_index' of 'panda3d.core.Thread' objects>"
        'simple_threads': None, # (!) real value is "<attribute 'simple_threads' of 'panda3d.core.Thread'>"
        'sleep': None, # (!) real value is '<staticmethod(<built-in method sleep of type object at 0x00007FFCFE2EB160>)>'
        'start': None, # (!) real value is "<method 'start' of 'panda3d.core.Thread' objects>"
        'started': None, # (!) real value is "<attribute 'started' of 'panda3d.core.Thread' objects>"
        'sync_name': None, # (!) real value is "<attribute 'sync_name' of 'panda3d.core.Thread' objects>"
        'threading_supported': None, # (!) real value is "<attribute 'threading_supported' of 'panda3d.core.Thread'>"
        'true_threads': None, # (!) real value is "<attribute 'true_threads' of 'panda3d.core.Thread'>"
        'unique_id': None, # (!) real value is "<attribute 'unique_id' of 'panda3d.core.Thread' objects>"
        'upcastToNamable': None, # (!) real value is "<method 'upcastToNamable' of 'panda3d.core.Thread' objects>"
        'upcastToTypedReferenceCount': None, # (!) real value is "<method 'upcastToTypedReferenceCount' of 'panda3d.core.Thread' objects>"
        'upcast_to_Namable': None, # (!) real value is "<method 'upcast_to_Namable' of 'panda3d.core.Thread' objects>"
        'upcast_to_TypedReferenceCount': None, # (!) real value is "<method 'upcast_to_TypedReferenceCount' of 'panda3d.core.Thread' objects>"
        'writeStatus': None, # (!) real value is '<staticmethod(<built-in method writeStatus of type object at 0x00007FFCFE2EB160>)>'
        'write_status': None, # (!) real value is '<staticmethod(<built-in method write_status of type object at 0x00007FFCFE2EB160>)>'
    }
    external_thread = None # (!) real value is 'ExternalThread External'
    main_thread = None # (!) real value is 'MainThread Main'
    simple_threads = False
    threading_supported = True
    true_threads = True


