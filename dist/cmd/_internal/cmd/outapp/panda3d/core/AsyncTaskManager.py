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

class AsyncTaskManager(TypedReferenceCount, Namable):
    """
    /**
     * A class to manage a loose queue of isolated tasks, which can be performed
     * either synchronously (in the foreground thread) or asynchronously (by a
     * background thread).
     *
     * The AsyncTaskManager is actually a collection of AsyncTaskChains, each of
     * which maintains a list of tasks.  Each chain can be either foreground or
     * background (it may run only in the main thread, or it may be serviced by
     * one or more background threads). See AsyncTaskChain for more information.
     *
     * If you do not require background processing, it is perfectly acceptable to
     * create only one AsyncTaskChain, which runs in the main thread.  This is a
     * common configuration.
     */
    """
    def add(self, const_AsyncTaskManager_self, AsyncTask_task): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add(const AsyncTaskManager self, AsyncTask task)
        
        /**
         * Adds the indicated task to the active queue.  It is an error if the task is
         * already added to this or any other active queue.
         */
        """
        pass

    def cleanup(self, const_AsyncTaskManager_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        cleanup(const AsyncTaskManager self)
        
        /**
         * Stops all threads and messily empties the task list.  This is intended to
         * be called on destruction only.
         */
        """
        pass

    def findTask(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        find_task(AsyncTaskManager self, str name)
        
        /**
         * Returns the first task found with the indicated name, or NULL if there is
         * no task with the indicated name.
         *
         * If there are multiple tasks with the same name, returns one of them
         * arbitrarily.
         */
        """
        pass

    def findTaskChain(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        find_task_chain(const AsyncTaskManager self, str name)
        
        /**
         * Searches a new AsyncTaskChain of the indicated name and returns it if it
         * exists, or NULL otherwise.
         */
        """
        pass

    def findTasks(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        find_tasks(AsyncTaskManager self, str name)
        
        /**
         * Returns the list of tasks found with the indicated name.
         */
        """
        pass

    def findTasksMatching(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        find_tasks_matching(AsyncTaskManager self, const GlobPattern pattern)
        
        /**
         * Returns the list of tasks found whose name matches the indicated glob
         * pattern, e.g.  "my_task_*".
         */
        """
        pass

    def find_task(self, AsyncTaskManager_self, str_name): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        find_task(AsyncTaskManager self, str name)
        
        /**
         * Returns the first task found with the indicated name, or NULL if there is
         * no task with the indicated name.
         *
         * If there are multiple tasks with the same name, returns one of them
         * arbitrarily.
         */
        """
        pass

    def find_tasks(self, AsyncTaskManager_self, str_name): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        find_tasks(AsyncTaskManager self, str name)
        
        /**
         * Returns the list of tasks found with the indicated name.
         */
        """
        pass

    def find_tasks_matching(self, AsyncTaskManager_self, const_GlobPattern_pattern): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        find_tasks_matching(AsyncTaskManager self, const GlobPattern pattern)
        
        /**
         * Returns the list of tasks found whose name matches the indicated glob
         * pattern, e.g.  "my_task_*".
         */
        """
        pass

    def find_task_chain(self, const_AsyncTaskManager_self, str_name): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        find_task_chain(const AsyncTaskManager self, str name)
        
        /**
         * Searches a new AsyncTaskChain of the indicated name and returns it if it
         * exists, or NULL otherwise.
         */
        """
        pass

    def getActiveTasks(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_active_tasks(AsyncTaskManager self)
        
        /**
         * Returns the set of tasks that are active (and not sleeping) on the task
         * manager, at the time of the call.
         */
        """
        pass

    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getClock(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_clock(const AsyncTaskManager self)
        
        /**
         * Returns the clock pointer used within the AsyncTaskManager.  See
         * set_clock().
         */
        """
        pass

    def getGlobalPtr(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_global_ptr()
        
        /**
         * Returns a pointer to the global AsyncTaskManager.  This is the
         * AsyncTaskManager that most code should use for queueing tasks and suchlike.
         */
        """
        pass

    def getNextWakeTime(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_next_wake_time(AsyncTaskManager self)
        
        /**
         * Returns the scheduled time (on the manager's clock) of the next sleeping
         * task, on any task chain, to awaken.  Returns -1 if there are no sleeping
         * tasks.
         */
        """
        pass

    def getNumTaskChains(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_task_chains(AsyncTaskManager self)
        
        /**
         * Returns the number of different task chains.
         */
        """
        pass

    def getNumTasks(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_tasks(AsyncTaskManager self)
        
        /**
         * Returns the number of tasks that are currently active or sleeping within
         * the task manager.
         */
        """
        pass

    def getSleepingTasks(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_sleeping_tasks(AsyncTaskManager self)
        
        /**
         * Returns the set of tasks that are sleeping (and not active) on the task
         * manager, at the time of the call.
         */
        """
        pass

    def getTaskChain(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_task_chain(AsyncTaskManager self, int n)
        
        /**
         * Returns the nth task chain.
         */
        """
        pass

    def getTaskChains(self, *args, **kwargs): # real signature unknown
        pass

    def getTasks(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_tasks(AsyncTaskManager self)
        
        /**
         * Returns the set of tasks that are active or sleeping on the task manager,
         * at the time of the call.
         */
        """
        pass

    def get_active_tasks(self, AsyncTaskManager_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_active_tasks(AsyncTaskManager self)
        
        /**
         * Returns the set of tasks that are active (and not sleeping) on the task
         * manager, at the time of the call.
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_clock(self, const_AsyncTaskManager_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_clock(const AsyncTaskManager self)
        
        /**
         * Returns the clock pointer used within the AsyncTaskManager.  See
         * set_clock().
         */
        """
        pass

    def get_global_ptr(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_global_ptr()
        
        /**
         * Returns a pointer to the global AsyncTaskManager.  This is the
         * AsyncTaskManager that most code should use for queueing tasks and suchlike.
         */
        """
        pass

    def get_next_wake_time(self, AsyncTaskManager_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_next_wake_time(AsyncTaskManager self)
        
        /**
         * Returns the scheduled time (on the manager's clock) of the next sleeping
         * task, on any task chain, to awaken.  Returns -1 if there are no sleeping
         * tasks.
         */
        """
        pass

    def get_num_tasks(self, AsyncTaskManager_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_tasks(AsyncTaskManager self)
        
        /**
         * Returns the number of tasks that are currently active or sleeping within
         * the task manager.
         */
        """
        pass

    def get_num_task_chains(self, AsyncTaskManager_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_task_chains(AsyncTaskManager self)
        
        /**
         * Returns the number of different task chains.
         */
        """
        pass

    def get_sleeping_tasks(self, AsyncTaskManager_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_sleeping_tasks(AsyncTaskManager self)
        
        /**
         * Returns the set of tasks that are sleeping (and not active) on the task
         * manager, at the time of the call.
         */
        """
        pass

    def get_tasks(self, AsyncTaskManager_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_tasks(AsyncTaskManager self)
        
        /**
         * Returns the set of tasks that are active or sleeping on the task manager,
         * at the time of the call.
         */
        """
        pass

    def get_task_chain(self, AsyncTaskManager_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_task_chain(AsyncTaskManager self, int n)
        
        /**
         * Returns the nth task chain.
         */
        """
        pass

    def get_task_chains(self, *args, **kwargs): # real signature unknown
        pass

    def hasTask(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_task(AsyncTaskManager self, AsyncTask task)
        
        /**
         * Returns true if the indicated task has been added to this AsyncTaskManager,
         * false otherwise.
         */
        """
        pass

    def has_task(self, AsyncTaskManager_self, AsyncTask_task): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_task(AsyncTaskManager self, AsyncTask task)
        
        /**
         * Returns true if the indicated task has been added to this AsyncTaskManager,
         * false otherwise.
         */
        """
        pass

    def makeTaskChain(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        make_task_chain(const AsyncTaskManager self, str name)
        
        /**
         * Creates a new AsyncTaskChain of the indicated name and stores it within the
         * AsyncTaskManager.  If a task chain with this name already exists, returns
         * it instead.
         */
        """
        pass

    def make_task_chain(self, const_AsyncTaskManager_self, str_name): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        make_task_chain(const AsyncTaskManager self, str name)
        
        /**
         * Creates a new AsyncTaskChain of the indicated name and stores it within the
         * AsyncTaskManager.  If a task chain with this name already exists, returns
         * it instead.
         */
        """
        pass

    def output(self, AsyncTaskManager_self, ostream_out): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        output(AsyncTaskManager self, ostream out)
        
        /**
         *
         */
        """
        pass

    def poll(self, const_AsyncTaskManager_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        poll(const AsyncTaskManager self)
        
        /**
         * Runs through all the tasks in the task list, once, if the task manager is
         * running in single-threaded mode (no threads available).  This method does
         * nothing in threaded mode, so it may safely be called in either case.
         */
        """
        pass

    def remove(self, const_AsyncTaskManager_self, AsyncTask_task): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        remove(const AsyncTaskManager self, AsyncTask task)
        remove(const AsyncTaskManager self, const AsyncTaskCollection tasks)
        
        /**
         * Removes the indicated task from the active queue.  Returns true if the task
         * is successfully removed, or false if it wasn't there.
         */
        
        /**
         * Removes all of the tasks in the AsyncTaskCollection.  Returns the number of
         * tasks removed.
         */
        """
        pass

    def removeTaskChain(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        remove_task_chain(const AsyncTaskManager self, str name)
        
        /**
         * Removes the AsyncTaskChain of the indicated name.  If the chain still has
         * tasks, this will block until all tasks are finished.
         *
         * Returns true if successful, or false if the chain did not exist.
         */
        """
        pass

    def remove_task_chain(self, const_AsyncTaskManager_self, str_name): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        remove_task_chain(const AsyncTaskManager self, str name)
        
        /**
         * Removes the AsyncTaskChain of the indicated name.  If the chain still has
         * tasks, this will block until all tasks are finished.
         *
         * Returns true if successful, or false if the chain did not exist.
         */
        """
        pass

    def setClock(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_clock(const AsyncTaskManager self, ClockObject clock)
        
        /**
         * Replaces the clock pointer used within the AsyncTaskManager.  This is used
         * to control when tasks with a set_delay() specified will be scheduled.  It
         * can also be ticked automatically each epoch, if set_tick_clock() is true.
         *
         * The default is the global clock pointer.
         */
        """
        pass

    def set_clock(self, const_AsyncTaskManager_self, ClockObject_clock): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_clock(const AsyncTaskManager self, ClockObject clock)
        
        /**
         * Replaces the clock pointer used within the AsyncTaskManager.  This is used
         * to control when tasks with a set_delay() specified will be scheduled.  It
         * can also be ticked automatically each epoch, if set_tick_clock() is true.
         *
         * The default is the global clock pointer.
         */
        """
        pass

    def startThreads(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        start_threads(const AsyncTaskManager self)
        
        /**
         * Starts any requested threads to service the tasks on the queue.  This is
         * normally not necessary, since adding a task will start the threads
         * automatically.
         */
        """
        pass

    def start_threads(self, const_AsyncTaskManager_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        start_threads(const AsyncTaskManager self)
        
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
        stop_threads(const AsyncTaskManager self)
        
        /**
         * Stops any threads that are currently running.  If any tasks are still
         * pending and have not yet been picked up by a thread, they will not be
         * serviced unless poll() or start_threads() is later called.
         */
        """
        pass

    def stop_threads(self, const_AsyncTaskManager_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        stop_threads(const AsyncTaskManager self)
        
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
        upcast_to_Namable(const AsyncTaskManager self)
        
        upcast from AsyncTaskManager to Namable
        """
        pass

    def upcastToTypedReferenceCount(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        upcast_to_TypedReferenceCount(const AsyncTaskManager self)
        
        upcast from AsyncTaskManager to TypedReferenceCount
        """
        pass

    def upcast_to_Namable(self, const_AsyncTaskManager_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        upcast_to_Namable(const AsyncTaskManager self)
        
        upcast from AsyncTaskManager to Namable
        """
        pass

    def upcast_to_TypedReferenceCount(self, const_AsyncTaskManager_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        upcast_to_TypedReferenceCount(const AsyncTaskManager self)
        
        upcast from AsyncTaskManager to TypedReferenceCount
        """
        pass

    def waitForTasks(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        wait_for_tasks(const AsyncTaskManager self)
        
        /**
         * Blocks until the task list is empty.
         */
        """
        pass

    def wait_for_tasks(self, const_AsyncTaskManager_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        wait_for_tasks(const AsyncTaskManager self)
        
        /**
         * Blocks until the task list is empty.
         */
        """
        pass

    def write(self, AsyncTaskManager_self, ostream_out, int_indent_level): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        write(AsyncTaskManager self, ostream out, int indent_level)
        
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

    active_tasks = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    clock = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    next_wake_time = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    sleeping_tasks = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tasks = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__doc__': '/**\n * A class to manage a loose queue of isolated tasks, which can be performed\n * either synchronously (in the foreground thread) or asynchronously (by a\n * background thread).\n *\n * The AsyncTaskManager is actually a collection of AsyncTaskChains, each of\n * which maintains a list of tasks.  Each chain can be either foreground or\n * background (it may run only in the main thread, or it may be serviced by\n * one or more background threads). See AsyncTaskChain for more information.\n *\n * If you do not require background processing, it is perfectly acceptable to\n * create only one AsyncTaskChain, which runs in the main thread.  This is a\n * common configuration.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.AsyncTaskManager' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE2EFA50>'
        '__repr__': None, # (!) real value is "<slot wrapper '__repr__' of 'panda3d.core.AsyncTaskManager' objects>"
        '__str__': None, # (!) real value is "<slot wrapper '__str__' of 'panda3d.core.AsyncTaskManager' objects>"
        'active_tasks': None, # (!) real value is "<attribute 'active_tasks' of 'panda3d.core.AsyncTaskManager' objects>"
        'add': None, # (!) real value is "<method 'add' of 'panda3d.core.AsyncTaskManager' objects>"
        'cleanup': None, # (!) real value is "<method 'cleanup' of 'panda3d.core.AsyncTaskManager' objects>"
        'clock': None, # (!) real value is "<attribute 'clock' of 'panda3d.core.AsyncTaskManager' objects>"
        'findTask': None, # (!) real value is "<method 'findTask' of 'panda3d.core.AsyncTaskManager' objects>"
        'findTaskChain': None, # (!) real value is "<method 'findTaskChain' of 'panda3d.core.AsyncTaskManager' objects>"
        'findTasks': None, # (!) real value is "<method 'findTasks' of 'panda3d.core.AsyncTaskManager' objects>"
        'findTasksMatching': None, # (!) real value is "<method 'findTasksMatching' of 'panda3d.core.AsyncTaskManager' objects>"
        'find_task': None, # (!) real value is "<method 'find_task' of 'panda3d.core.AsyncTaskManager' objects>"
        'find_task_chain': None, # (!) real value is "<method 'find_task_chain' of 'panda3d.core.AsyncTaskManager' objects>"
        'find_tasks': None, # (!) real value is "<method 'find_tasks' of 'panda3d.core.AsyncTaskManager' objects>"
        'find_tasks_matching': None, # (!) real value is "<method 'find_tasks_matching' of 'panda3d.core.AsyncTaskManager' objects>"
        'getActiveTasks': None, # (!) real value is "<method 'getActiveTasks' of 'panda3d.core.AsyncTaskManager' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE2EFA50>)>'
        'getClock': None, # (!) real value is "<method 'getClock' of 'panda3d.core.AsyncTaskManager' objects>"
        'getGlobalPtr': None, # (!) real value is '<staticmethod(<built-in method getGlobalPtr of type object at 0x00007FFCFE2EFA50>)>'
        'getNextWakeTime': None, # (!) real value is "<method 'getNextWakeTime' of 'panda3d.core.AsyncTaskManager' objects>"
        'getNumTaskChains': None, # (!) real value is "<method 'getNumTaskChains' of 'panda3d.core.AsyncTaskManager' objects>"
        'getNumTasks': None, # (!) real value is "<method 'getNumTasks' of 'panda3d.core.AsyncTaskManager' objects>"
        'getSleepingTasks': None, # (!) real value is "<method 'getSleepingTasks' of 'panda3d.core.AsyncTaskManager' objects>"
        'getTaskChain': None, # (!) real value is "<method 'getTaskChain' of 'panda3d.core.AsyncTaskManager' objects>"
        'getTaskChains': None, # (!) real value is "<method 'getTaskChains' of 'panda3d.core.AsyncTaskManager' objects>"
        'getTasks': None, # (!) real value is "<method 'getTasks' of 'panda3d.core.AsyncTaskManager' objects>"
        'get_active_tasks': None, # (!) real value is "<method 'get_active_tasks' of 'panda3d.core.AsyncTaskManager' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE2EFA50>)>'
        'get_clock': None, # (!) real value is "<method 'get_clock' of 'panda3d.core.AsyncTaskManager' objects>"
        'get_global_ptr': None, # (!) real value is '<staticmethod(<built-in method get_global_ptr of type object at 0x00007FFCFE2EFA50>)>'
        'get_next_wake_time': None, # (!) real value is "<method 'get_next_wake_time' of 'panda3d.core.AsyncTaskManager' objects>"
        'get_num_task_chains': None, # (!) real value is "<method 'get_num_task_chains' of 'panda3d.core.AsyncTaskManager' objects>"
        'get_num_tasks': None, # (!) real value is "<method 'get_num_tasks' of 'panda3d.core.AsyncTaskManager' objects>"
        'get_sleeping_tasks': None, # (!) real value is "<method 'get_sleeping_tasks' of 'panda3d.core.AsyncTaskManager' objects>"
        'get_task_chain': None, # (!) real value is "<method 'get_task_chain' of 'panda3d.core.AsyncTaskManager' objects>"
        'get_task_chains': None, # (!) real value is "<method 'get_task_chains' of 'panda3d.core.AsyncTaskManager' objects>"
        'get_tasks': None, # (!) real value is "<method 'get_tasks' of 'panda3d.core.AsyncTaskManager' objects>"
        'hasTask': None, # (!) real value is "<method 'hasTask' of 'panda3d.core.AsyncTaskManager' objects>"
        'has_task': None, # (!) real value is "<method 'has_task' of 'panda3d.core.AsyncTaskManager' objects>"
        'makeTaskChain': None, # (!) real value is "<method 'makeTaskChain' of 'panda3d.core.AsyncTaskManager' objects>"
        'make_task_chain': None, # (!) real value is "<method 'make_task_chain' of 'panda3d.core.AsyncTaskManager' objects>"
        'next_wake_time': None, # (!) real value is "<attribute 'next_wake_time' of 'panda3d.core.AsyncTaskManager' objects>"
        'output': None, # (!) real value is "<method 'output' of 'panda3d.core.AsyncTaskManager' objects>"
        'poll': None, # (!) real value is "<method 'poll' of 'panda3d.core.AsyncTaskManager' objects>"
        'remove': None, # (!) real value is "<method 'remove' of 'panda3d.core.AsyncTaskManager' objects>"
        'removeTaskChain': None, # (!) real value is "<method 'removeTaskChain' of 'panda3d.core.AsyncTaskManager' objects>"
        'remove_task_chain': None, # (!) real value is "<method 'remove_task_chain' of 'panda3d.core.AsyncTaskManager' objects>"
        'setClock': None, # (!) real value is "<method 'setClock' of 'panda3d.core.AsyncTaskManager' objects>"
        'set_clock': None, # (!) real value is "<method 'set_clock' of 'panda3d.core.AsyncTaskManager' objects>"
        'sleeping_tasks': None, # (!) real value is "<attribute 'sleeping_tasks' of 'panda3d.core.AsyncTaskManager' objects>"
        'startThreads': None, # (!) real value is "<method 'startThreads' of 'panda3d.core.AsyncTaskManager' objects>"
        'start_threads': None, # (!) real value is "<method 'start_threads' of 'panda3d.core.AsyncTaskManager' objects>"
        'stopThreads': None, # (!) real value is "<method 'stopThreads' of 'panda3d.core.AsyncTaskManager' objects>"
        'stop_threads': None, # (!) real value is "<method 'stop_threads' of 'panda3d.core.AsyncTaskManager' objects>"
        'tasks': None, # (!) real value is "<attribute 'tasks' of 'panda3d.core.AsyncTaskManager' objects>"
        'upcastToNamable': None, # (!) real value is "<method 'upcastToNamable' of 'panda3d.core.AsyncTaskManager' objects>"
        'upcastToTypedReferenceCount': None, # (!) real value is "<method 'upcastToTypedReferenceCount' of 'panda3d.core.AsyncTaskManager' objects>"
        'upcast_to_Namable': None, # (!) real value is "<method 'upcast_to_Namable' of 'panda3d.core.AsyncTaskManager' objects>"
        'upcast_to_TypedReferenceCount': None, # (!) real value is "<method 'upcast_to_TypedReferenceCount' of 'panda3d.core.AsyncTaskManager' objects>"
        'waitForTasks': None, # (!) real value is "<method 'waitForTasks' of 'panda3d.core.AsyncTaskManager' objects>"
        'wait_for_tasks': None, # (!) real value is "<method 'wait_for_tasks' of 'panda3d.core.AsyncTaskManager' objects>"
        'write': None, # (!) real value is "<method 'write' of 'panda3d.core.AsyncTaskManager' objects>"
    }


