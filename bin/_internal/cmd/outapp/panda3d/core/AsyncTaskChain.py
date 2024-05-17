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

class AsyncTaskChain(TypedReferenceCount, Namable):
    """
    /**
     * The AsyncTaskChain is a subset of the AsyncTaskManager.  Each chain
     * maintains a separate list of tasks, and will execute them with its own set
     * of threads.  Each chain may thereby operate independently of the other
     * chains.
     *
     * The AsyncTaskChain will spawn a specified number of threads (possibly 0) to
     * serve the tasks.  If there are no threads, you must call poll() from time
     * to time to serve the tasks in the main thread.  Normally this is done by
     * calling AsyncTaskManager::poll().
     *
     * Each task will run exactly once each epoch.  Beyond that, the tasks' sort
     * and priority values control the order in which they are run: tasks are run
     * in increasing order by sort value, and within the same sort value, they are
     * run roughly in decreasing order by priority value, with some exceptions for
     * parallelism.  Tasks with different sort values are never run in parallel
     * together, but tasks with different priority values might be (if there is
     * more than one thread).
     */
    """
    def getActiveTasks(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_active_tasks(AsyncTaskChain self)
        
        /**
         * Returns the set of tasks that are active (and not sleeping) on the task
         * chain, at the time of the call.
         */
        """
        pass

    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getFrameBudget(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_frame_budget(AsyncTaskChain self)
        
        /**
         * Returns the maximum amount of time per frame the tasks on this chain are
         * granted for execution.  See set_frame_budget().
         */
        """
        pass

    def getFrameSync(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_frame_sync(AsyncTaskChain self)
        
        /**
         * Returns the frame_sync flag.  See set_frame_sync().
         */
        """
        pass

    def getNextWakeTime(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_next_wake_time(AsyncTaskChain self)
        
        /**
         * Returns the scheduled time (on the manager's clock) of the next sleeping
         * task, on any task chain, to awaken.  Returns -1 if there are no sleeping
         * tasks.
         */
        """
        pass

    def getNumRunningThreads(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_running_threads(AsyncTaskChain self)
        
        /**
         * Returns the number of threads that have been created and are actively
         * running.  This will return 0 before the threads have been started; it will
         * also return 0 if thread support is not available.
         */
        """
        pass

    def getNumTasks(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_tasks(AsyncTaskChain self)
        
        /**
         * Returns the number of tasks that are currently active or sleeping within
         * the task chain.
         */
        """
        pass

    def getNumThreads(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_threads(AsyncTaskChain self)
        
        /**
         * Returns the number of threads that will be servicing tasks for this chain.
         * Also see get_num_running_threads().
         */
        """
        pass

    def getSleepingTasks(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_sleeping_tasks(AsyncTaskChain self)
        
        /**
         * Returns the set of tasks that are sleeping (and not active) on the task
         * chain, at the time of the call.
         */
        """
        pass

    def getTasks(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_tasks(AsyncTaskChain self)
        
        /**
         * Returns the set of tasks that are active or sleeping on the task chain, at
         * the time of the call.
         */
        """
        pass

    def getThreadPriority(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_thread_priority(AsyncTaskChain self)
        
        /**
         * Returns the priority associated with threads that serve this task chain.
         */
        """
        pass

    def getTickClock(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_tick_clock(AsyncTaskChain self)
        
        /**
         * Returns the tick_clock flag.  See set_tick_clock().
         */
        """
        pass

    def getTimeslicePriority(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_timeslice_priority(AsyncTaskChain self)
        
        /**
         * Returns the timeslice_priority flag.  This changes the interpretation of
         * priority, and the number of times per epoch each task will run.  See
         * set_timeslice_priority().
         */
        """
        pass

    def get_active_tasks(self, AsyncTaskChain_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_active_tasks(AsyncTaskChain self)
        
        /**
         * Returns the set of tasks that are active (and not sleeping) on the task
         * chain, at the time of the call.
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_frame_budget(self, AsyncTaskChain_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_frame_budget(AsyncTaskChain self)
        
        /**
         * Returns the maximum amount of time per frame the tasks on this chain are
         * granted for execution.  See set_frame_budget().
         */
        """
        pass

    def get_frame_sync(self, AsyncTaskChain_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_frame_sync(AsyncTaskChain self)
        
        /**
         * Returns the frame_sync flag.  See set_frame_sync().
         */
        """
        pass

    def get_next_wake_time(self, AsyncTaskChain_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_next_wake_time(AsyncTaskChain self)
        
        /**
         * Returns the scheduled time (on the manager's clock) of the next sleeping
         * task, on any task chain, to awaken.  Returns -1 if there are no sleeping
         * tasks.
         */
        """
        pass

    def get_num_running_threads(self, AsyncTaskChain_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_running_threads(AsyncTaskChain self)
        
        /**
         * Returns the number of threads that have been created and are actively
         * running.  This will return 0 before the threads have been started; it will
         * also return 0 if thread support is not available.
         */
        """
        pass

    def get_num_tasks(self, AsyncTaskChain_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_tasks(AsyncTaskChain self)
        
        /**
         * Returns the number of tasks that are currently active or sleeping within
         * the task chain.
         */
        """
        pass

    def get_num_threads(self, AsyncTaskChain_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_threads(AsyncTaskChain self)
        
        /**
         * Returns the number of threads that will be servicing tasks for this chain.
         * Also see get_num_running_threads().
         */
        """
        pass

    def get_sleeping_tasks(self, AsyncTaskChain_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_sleeping_tasks(AsyncTaskChain self)
        
        /**
         * Returns the set of tasks that are sleeping (and not active) on the task
         * chain, at the time of the call.
         */
        """
        pass

    def get_tasks(self, AsyncTaskChain_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_tasks(AsyncTaskChain self)
        
        /**
         * Returns the set of tasks that are active or sleeping on the task chain, at
         * the time of the call.
         */
        """
        pass

    def get_thread_priority(self, AsyncTaskChain_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_thread_priority(AsyncTaskChain self)
        
        /**
         * Returns the priority associated with threads that serve this task chain.
         */
        """
        pass

    def get_tick_clock(self, AsyncTaskChain_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_tick_clock(AsyncTaskChain self)
        
        /**
         * Returns the tick_clock flag.  See set_tick_clock().
         */
        """
        pass

    def get_timeslice_priority(self, AsyncTaskChain_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_timeslice_priority(AsyncTaskChain self)
        
        /**
         * Returns the timeslice_priority flag.  This changes the interpretation of
         * priority, and the number of times per epoch each task will run.  See
         * set_timeslice_priority().
         */
        """
        pass

    def hasTask(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_task(AsyncTaskChain self, AsyncTask task)
        
        /**
         * Returns true if the indicated task has been added to this AsyncTaskChain,
         * false otherwise.
         */
        """
        pass

    def has_task(self, AsyncTaskChain_self, AsyncTask_task): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_task(AsyncTaskChain self, AsyncTask task)
        
        /**
         * Returns true if the indicated task has been added to this AsyncTaskChain,
         * false otherwise.
         */
        """
        pass

    def isStarted(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_started(AsyncTaskChain self)
        
        /**
         * Returns true if the thread(s) have been started and are ready to service
         * requests, false otherwise.  If this is false, the next call to add() or
         * add_and_do() will automatically start the threads.
         */
        """
        pass

    def is_started(self, AsyncTaskChain_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_started(AsyncTaskChain self)
        
        /**
         * Returns true if the thread(s) have been started and are ready to service
         * requests, false otherwise.  If this is false, the next call to add() or
         * add_and_do() will automatically start the threads.
         */
        """
        pass

    def output(self, AsyncTaskChain_self, ostream_out): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        output(AsyncTaskChain self, ostream out)
        
        /**
         *
         */
        """
        pass

    def poll(self, const_AsyncTaskChain_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        poll(const AsyncTaskChain self)
        
        /**
         * Runs through all the tasks in the task list, once, if the task chain is
         * running in single-threaded mode (no threads available).  This method does
         * nothing in threaded mode, so it may safely be called in either case.
         *
         * Normally, you would not call this function directly; instead, call
         * AsyncTaskManager::poll(), which polls all of the task chains in sequence.
         */
        """
        pass

    def setFrameBudget(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_frame_budget(const AsyncTaskChain self, double frame_budget)
        
        /**
         * Sets the maximum amount of time per frame the tasks on this chain are
         * granted for execution.  If this is less than zero, there is no limit; if it
         * is >= 0, it represents a maximum amount of time (in seconds) that will be
         * used to execute tasks.  If this time is exceeded in any one frame, the task
         * chain will stop executing tasks until the next frame, as defined by the
         * TaskManager's clock.
         */
        """
        pass

    def setFrameSync(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_frame_sync(const AsyncTaskChain self, bool frame_sync)
        
        /**
         * Sets the frame_sync flag.  When this flag is true, this task chain will be
         * forced to sync with the TaskManager's clock.  It will run no faster than
         * one epoch per clock frame.
         *
         * When this flag is false, the default, the task chain will finish all of its
         * tasks and then immediately start from the first task again, regardless of
         * the clock frame.  When it is true, the task chain will finish all of its
         * tasks and then wait for the clock to tick to the next frame before resuming
         * the first task.
         *
         * This only makes sense for threaded task chains.  Non-threaded task chains
         * are automatically synchronous.
         */
        """
        pass

    def setNumThreads(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_num_threads(const AsyncTaskChain self, int num_threads)
        
        /**
         * Changes the number of threads for this task chain.  This may require
         * stopping the threads if they are already running.
         */
        """
        pass

    def setThreadPriority(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_thread_priority(const AsyncTaskChain self, int priority)
        
        /**
         * Changes the priority associated with threads that serve this task chain.
         * This may require stopping the threads if they are already running.
         */
        """
        pass

    def setTickClock(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_tick_clock(const AsyncTaskChain self, bool tick_clock)
        
        /**
         * Sets the tick_clock flag.  When this is true, get_clock()->tick() will be
         * called automatically at each task epoch.  This is false by default.
         */
        """
        pass

    def setTimeslicePriority(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_timeslice_priority(const AsyncTaskChain self, bool timeslice_priority)
        
        /**
         * Sets the timeslice_priority flag.  This changes the interpretation of
         * priority, and the number of times per epoch each task will run.
         *
         * When this flag is true, some tasks might not run in any given epoch.
         * Instead, tasks with priority higher than 1 will be given precedence, in
         * proportion to the amount of time they have already used.  This gives
         * higher-priority tasks more runtime than lower-priority tasks.  Each task
         * gets the amount of time proportional to its priority value, so a task with
         * priority 100 will get five times as much processing time as a task with
         * priority 20.  For these purposes, priority values less than 1 are deemed to
         * be equal to 1.
         *
         * When this flag is false (the default), all tasks are run exactly once each
         * epoch, round-robin style.  Priority is only used to determine which task
         * runs first within tasks of the same sort value.
         */
        """
        pass

    def set_frame_budget(self, const_AsyncTaskChain_self, double_frame_budget): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_frame_budget(const AsyncTaskChain self, double frame_budget)
        
        /**
         * Sets the maximum amount of time per frame the tasks on this chain are
         * granted for execution.  If this is less than zero, there is no limit; if it
         * is >= 0, it represents a maximum amount of time (in seconds) that will be
         * used to execute tasks.  If this time is exceeded in any one frame, the task
         * chain will stop executing tasks until the next frame, as defined by the
         * TaskManager's clock.
         */
        """
        pass

    def set_frame_sync(self, const_AsyncTaskChain_self, bool_frame_sync): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_frame_sync(const AsyncTaskChain self, bool frame_sync)
        
        /**
         * Sets the frame_sync flag.  When this flag is true, this task chain will be
         * forced to sync with the TaskManager's clock.  It will run no faster than
         * one epoch per clock frame.
         *
         * When this flag is false, the default, the task chain will finish all of its
         * tasks and then immediately start from the first task again, regardless of
         * the clock frame.  When it is true, the task chain will finish all of its
         * tasks and then wait for the clock to tick to the next frame before resuming
         * the first task.
         *
         * This only makes sense for threaded task chains.  Non-threaded task chains
         * are automatically synchronous.
         */
        """
        pass

    def set_num_threads(self, const_AsyncTaskChain_self, int_num_threads): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_num_threads(const AsyncTaskChain self, int num_threads)
        
        /**
         * Changes the number of threads for this task chain.  This may require
         * stopping the threads if they are already running.
         */
        """
        pass

    def set_thread_priority(self, const_AsyncTaskChain_self, int_priority): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_thread_priority(const AsyncTaskChain self, int priority)
        
        /**
         * Changes the priority associated with threads that serve this task chain.
         * This may require stopping the threads if they are already running.
         */
        """
        pass

    def set_tick_clock(self, const_AsyncTaskChain_self, bool_tick_clock): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_tick_clock(const AsyncTaskChain self, bool tick_clock)
        
        /**
         * Sets the tick_clock flag.  When this is true, get_clock()->tick() will be
         * called automatically at each task epoch.  This is false by default.
         */
        """
        pass

    def set_timeslice_priority(self, const_AsyncTaskChain_self, bool_timeslice_priority): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_timeslice_priority(const AsyncTaskChain self, bool timeslice_priority)
        
        /**
         * Sets the timeslice_priority flag.  This changes the interpretation of
         * priority, and the number of times per epoch each task will run.
         *
         * When this flag is true, some tasks might not run in any given epoch.
         * Instead, tasks with priority higher than 1 will be given precedence, in
         * proportion to the amount of time they have already used.  This gives
         * higher-priority tasks more runtime than lower-priority tasks.  Each task
         * gets the amount of time proportional to its priority value, so a task with
         * priority 100 will get five times as much processing time as a task with
         * priority 20.  For these purposes, priority values less than 1 are deemed to
         * be equal to 1.
         *
         * When this flag is false (the default), all tasks are run exactly once each
         * epoch, round-robin style.  Priority is only used to determine which task
         * runs first within tasks of the same sort value.
         */
        """
        pass

    def startThreads(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        start_threads(const AsyncTaskChain self)
        
        /**
         * Starts any requested threads to service the tasks on the queue.  This is
         * normally not necessary, since adding a task will start the threads
         * automatically.
         */
        """
        pass

    def start_threads(self, const_AsyncTaskChain_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        start_threads(const AsyncTaskChain self)
        
        /**
         * Starts any requested threads to service the tasks on the queue.  This is
         * normally not necessary, since adding a task will start the threads
         * automatically.
         */
        """
        pass

    def stopThreads(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        stop_threads(const AsyncTaskChain self)
        
        /**
         * Stops any threads that are currently running.  If any tasks are still
         * pending and have not yet been picked up by a thread, they will not be
         * serviced unless poll() or start_threads() is later called.
         */
        """
        pass

    def stop_threads(self, const_AsyncTaskChain_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        stop_threads(const AsyncTaskChain self)
        
        /**
         * Stops any threads that are currently running.  If any tasks are still
         * pending and have not yet been picked up by a thread, they will not be
         * serviced unless poll() or start_threads() is later called.
         */
        """
        pass

    def upcastToNamable(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        upcast_to_Namable(const AsyncTaskChain self)
        
        upcast from AsyncTaskChain to Namable
        """
        pass

    def upcastToTypedReferenceCount(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        upcast_to_TypedReferenceCount(const AsyncTaskChain self)
        
        upcast from AsyncTaskChain to TypedReferenceCount
        """
        pass

    def upcast_to_Namable(self, const_AsyncTaskChain_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        upcast_to_Namable(const AsyncTaskChain self)
        
        upcast from AsyncTaskChain to Namable
        """
        pass

    def upcast_to_TypedReferenceCount(self, const_AsyncTaskChain_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        upcast_to_TypedReferenceCount(const AsyncTaskChain self)
        
        upcast from AsyncTaskChain to TypedReferenceCount
        """
        pass

    def waitForTasks(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        wait_for_tasks(const AsyncTaskChain self)
        
        /**
         * Blocks until the task list is empty.
         */
        """
        pass

    def wait_for_tasks(self, const_AsyncTaskChain_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        wait_for_tasks(const AsyncTaskChain self)
        
        /**
         * Blocks until the task list is empty.
         */
        """
        pass

    def write(self, AsyncTaskChain_self, ostream_out, int_indent_level): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        write(AsyncTaskChain self, ostream out, int indent_level)
        
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

    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__doc__': "/**\n * The AsyncTaskChain is a subset of the AsyncTaskManager.  Each chain\n * maintains a separate list of tasks, and will execute them with its own set\n * of threads.  Each chain may thereby operate independently of the other\n * chains.\n *\n * The AsyncTaskChain will spawn a specified number of threads (possibly 0) to\n * serve the tasks.  If there are no threads, you must call poll() from time\n * to time to serve the tasks in the main thread.  Normally this is done by\n * calling AsyncTaskManager::poll().\n *\n * Each task will run exactly once each epoch.  Beyond that, the tasks' sort\n * and priority values control the order in which they are run: tasks are run\n * in increasing order by sort value, and within the same sort value, they are\n * run roughly in decreasing order by priority value, with some exceptions for\n * parallelism.  Tasks with different sort values are never run in parallel\n * together, but tasks with different priority values might be (if there is\n * more than one thread).\n */",
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.AsyncTaskChain' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE2EFDF0>'
        '__repr__': None, # (!) real value is "<slot wrapper '__repr__' of 'panda3d.core.AsyncTaskChain' objects>"
        '__str__': None, # (!) real value is "<slot wrapper '__str__' of 'panda3d.core.AsyncTaskChain' objects>"
        'getActiveTasks': None, # (!) real value is "<method 'getActiveTasks' of 'panda3d.core.AsyncTaskChain' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE2EFDF0>)>'
        'getFrameBudget': None, # (!) real value is "<method 'getFrameBudget' of 'panda3d.core.AsyncTaskChain' objects>"
        'getFrameSync': None, # (!) real value is "<method 'getFrameSync' of 'panda3d.core.AsyncTaskChain' objects>"
        'getNextWakeTime': None, # (!) real value is "<method 'getNextWakeTime' of 'panda3d.core.AsyncTaskChain' objects>"
        'getNumRunningThreads': None, # (!) real value is "<method 'getNumRunningThreads' of 'panda3d.core.AsyncTaskChain' objects>"
        'getNumTasks': None, # (!) real value is "<method 'getNumTasks' of 'panda3d.core.AsyncTaskChain' objects>"
        'getNumThreads': None, # (!) real value is "<method 'getNumThreads' of 'panda3d.core.AsyncTaskChain' objects>"
        'getSleepingTasks': None, # (!) real value is "<method 'getSleepingTasks' of 'panda3d.core.AsyncTaskChain' objects>"
        'getTasks': None, # (!) real value is "<method 'getTasks' of 'panda3d.core.AsyncTaskChain' objects>"
        'getThreadPriority': None, # (!) real value is "<method 'getThreadPriority' of 'panda3d.core.AsyncTaskChain' objects>"
        'getTickClock': None, # (!) real value is "<method 'getTickClock' of 'panda3d.core.AsyncTaskChain' objects>"
        'getTimeslicePriority': None, # (!) real value is "<method 'getTimeslicePriority' of 'panda3d.core.AsyncTaskChain' objects>"
        'get_active_tasks': None, # (!) real value is "<method 'get_active_tasks' of 'panda3d.core.AsyncTaskChain' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE2EFDF0>)>'
        'get_frame_budget': None, # (!) real value is "<method 'get_frame_budget' of 'panda3d.core.AsyncTaskChain' objects>"
        'get_frame_sync': None, # (!) real value is "<method 'get_frame_sync' of 'panda3d.core.AsyncTaskChain' objects>"
        'get_next_wake_time': None, # (!) real value is "<method 'get_next_wake_time' of 'panda3d.core.AsyncTaskChain' objects>"
        'get_num_running_threads': None, # (!) real value is "<method 'get_num_running_threads' of 'panda3d.core.AsyncTaskChain' objects>"
        'get_num_tasks': None, # (!) real value is "<method 'get_num_tasks' of 'panda3d.core.AsyncTaskChain' objects>"
        'get_num_threads': None, # (!) real value is "<method 'get_num_threads' of 'panda3d.core.AsyncTaskChain' objects>"
        'get_sleeping_tasks': None, # (!) real value is "<method 'get_sleeping_tasks' of 'panda3d.core.AsyncTaskChain' objects>"
        'get_tasks': None, # (!) real value is "<method 'get_tasks' of 'panda3d.core.AsyncTaskChain' objects>"
        'get_thread_priority': None, # (!) real value is "<method 'get_thread_priority' of 'panda3d.core.AsyncTaskChain' objects>"
        'get_tick_clock': None, # (!) real value is "<method 'get_tick_clock' of 'panda3d.core.AsyncTaskChain' objects>"
        'get_timeslice_priority': None, # (!) real value is "<method 'get_timeslice_priority' of 'panda3d.core.AsyncTaskChain' objects>"
        'hasTask': None, # (!) real value is "<method 'hasTask' of 'panda3d.core.AsyncTaskChain' objects>"
        'has_task': None, # (!) real value is "<method 'has_task' of 'panda3d.core.AsyncTaskChain' objects>"
        'isStarted': None, # (!) real value is "<method 'isStarted' of 'panda3d.core.AsyncTaskChain' objects>"
        'is_started': None, # (!) real value is "<method 'is_started' of 'panda3d.core.AsyncTaskChain' objects>"
        'output': None, # (!) real value is "<method 'output' of 'panda3d.core.AsyncTaskChain' objects>"
        'poll': None, # (!) real value is "<method 'poll' of 'panda3d.core.AsyncTaskChain' objects>"
        'setFrameBudget': None, # (!) real value is "<method 'setFrameBudget' of 'panda3d.core.AsyncTaskChain' objects>"
        'setFrameSync': None, # (!) real value is "<method 'setFrameSync' of 'panda3d.core.AsyncTaskChain' objects>"
        'setNumThreads': None, # (!) real value is "<method 'setNumThreads' of 'panda3d.core.AsyncTaskChain' objects>"
        'setThreadPriority': None, # (!) real value is "<method 'setThreadPriority' of 'panda3d.core.AsyncTaskChain' objects>"
        'setTickClock': None, # (!) real value is "<method 'setTickClock' of 'panda3d.core.AsyncTaskChain' objects>"
        'setTimeslicePriority': None, # (!) real value is "<method 'setTimeslicePriority' of 'panda3d.core.AsyncTaskChain' objects>"
        'set_frame_budget': None, # (!) real value is "<method 'set_frame_budget' of 'panda3d.core.AsyncTaskChain' objects>"
        'set_frame_sync': None, # (!) real value is "<method 'set_frame_sync' of 'panda3d.core.AsyncTaskChain' objects>"
        'set_num_threads': None, # (!) real value is "<method 'set_num_threads' of 'panda3d.core.AsyncTaskChain' objects>"
        'set_thread_priority': None, # (!) real value is "<method 'set_thread_priority' of 'panda3d.core.AsyncTaskChain' objects>"
        'set_tick_clock': None, # (!) real value is "<method 'set_tick_clock' of 'panda3d.core.AsyncTaskChain' objects>"
        'set_timeslice_priority': None, # (!) real value is "<method 'set_timeslice_priority' of 'panda3d.core.AsyncTaskChain' objects>"
        'startThreads': None, # (!) real value is "<method 'startThreads' of 'panda3d.core.AsyncTaskChain' objects>"
        'start_threads': None, # (!) real value is "<method 'start_threads' of 'panda3d.core.AsyncTaskChain' objects>"
        'stopThreads': None, # (!) real value is "<method 'stopThreads' of 'panda3d.core.AsyncTaskChain' objects>"
        'stop_threads': None, # (!) real value is "<method 'stop_threads' of 'panda3d.core.AsyncTaskChain' objects>"
        'upcastToNamable': None, # (!) real value is "<method 'upcastToNamable' of 'panda3d.core.AsyncTaskChain' objects>"
        'upcastToTypedReferenceCount': None, # (!) real value is "<method 'upcastToTypedReferenceCount' of 'panda3d.core.AsyncTaskChain' objects>"
        'upcast_to_Namable': None, # (!) real value is "<method 'upcast_to_Namable' of 'panda3d.core.AsyncTaskChain' objects>"
        'upcast_to_TypedReferenceCount': None, # (!) real value is "<method 'upcast_to_TypedReferenceCount' of 'panda3d.core.AsyncTaskChain' objects>"
        'waitForTasks': None, # (!) real value is "<method 'waitForTasks' of 'panda3d.core.AsyncTaskChain' objects>"
        'wait_for_tasks': None, # (!) real value is "<method 'wait_for_tasks' of 'panda3d.core.AsyncTaskChain' objects>"
        'write': None, # (!) real value is "<method 'write' of 'panda3d.core.AsyncTaskChain' objects>"
    }


