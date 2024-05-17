# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .AsyncFuture import AsyncFuture

from .Namable import Namable

class AsyncTask(AsyncFuture, Namable):
    """
    /**
     * This class represents a concrete task performed by an AsyncManager.
     * Normally, you would subclass from this class, and override do_task(), to
     * define the functionality you wish to have the task perform.
     */
    """
    def clearDelay(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_delay(const AsyncTask self)
        
        /**
         * Removes any delay specified for the task.  The next time the task is added
         * to the queue, it will run immediately.  This does not affect the task's
         * wake time if it has already been added to the queue.
         */
        """
        pass

    def clearName(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_name(const AsyncTask self)
        
        /**
         * Resets the task's name to empty.
         */
        """
        pass

    def clear_delay(self, const_AsyncTask_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_delay(const AsyncTask self)
        
        /**
         * Removes any delay specified for the task.  The next time the task is added
         * to the queue, it will run immediately.  This does not affect the task's
         * wake time if it has already been added to the queue.
         */
        """
        pass

    def clear_name(self, const_AsyncTask_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_name(const AsyncTask self)
        
        /**
         * Resets the task's name to empty.
         */
        """
        pass

    def getAverageDt(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_average_dt(AsyncTask self)
        
        /**
         * Returns the average amount of time elapsed during each of the task's
         * previous run cycles, in seconds.
         */
        """
        pass

    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getDelay(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_delay(AsyncTask self)
        
        /**
         * Returns the delay value that has been set via set_delay, if any.
         */
        """
        pass

    def getDt(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_dt(AsyncTask self)
        
        /**
         * Returns the amount of time elapsed during the task's previous run cycle, in
         * seconds.
         */
        """
        pass

    def getElapsedFrames(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_elapsed_frames(AsyncTask self)
        
        /**
         * Returns the number of frames that have elapsed since the task was started,
         * according to the task manager's clock.
         *
         * It is only valid to call this if the task's status is not S_inactive.
         */
        """
        pass

    def getElapsedTime(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_elapsed_time(AsyncTask self)
        
        /**
         * Returns the amount of time that has elapsed since the task was started,
         * according to the task manager's clock.
         *
         * It is only valid to call this if the task's status is not S_inactive.
         */
        """
        pass

    def getManager(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_manager(AsyncTask self)
        
        /**
         * Returns the AsyncTaskManager that this task is active on.  This will be
         * NULL if the state is S_inactive.
         */
        """
        pass

    def getMaxDt(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_max_dt(AsyncTask self)
        
        /**
         * Returns the maximum amount of time elapsed during any one of the task's
         * previous run cycles, in seconds.
         */
        """
        pass

    def getNamePrefix(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_name_prefix(AsyncTask self)
        
        /**
         * Returns the initial part of the name, up to but not including any trailing
         * digits following a hyphen or underscore.
         */
        """
        pass

    def getPriority(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_priority(AsyncTask self)
        
        /**
         * Returns the task's current priority value.  See set_priority().
         */
        """
        pass

    def getSort(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_sort(AsyncTask self)
        
        /**
         * Returns the task's current sort value.  See set_sort().
         */
        """
        pass

    def getStartFrame(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_start_frame(AsyncTask self)
        
        /**
         * Returns the frame number at which the task was started, according to the
         * task manager's clock.
         *
         * It is only valid to call this if the task's status is not S_inactive.
         */
        """
        pass

    def getStartTime(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_start_time(AsyncTask self)
        
        /**
         * Returns the time at which the task was started, according to the task
         * manager's clock.
         *
         * It is only valid to call this if the task's status is not S_inactive.
         */
        """
        pass

    def getState(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_state(AsyncTask self)
        
        /**
         * Returns the current state of the task.
         */
        """
        pass

    def getTaskChain(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_task_chain(AsyncTask self)
        
        /**
         * Returns the AsyncTaskChain on which this task will be running.  Each task
         * chain runs tasks independently of the others.
         */
        """
        pass

    def getTaskId(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_task_id(AsyncTask self)
        
        /**
         * Returns a number guaranteed to be unique for each different AsyncTask
         * object in the universe.
         */
        """
        pass

    def getWakeTime(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_wake_time(AsyncTask self)
        
        /**
         * If this task has been added to an AsyncTaskManager with a delay in effect,
         * this returns the time at which the task is expected to awaken.  It has no
         * meaning if the task has not yet been added to a queue, or if there was no
         * delay in effect at the time the task was added.
         *
         * If the task's status is not S_sleeping, this returns 0.0.
         */
        """
        pass

    def get_average_dt(self, AsyncTask_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_average_dt(AsyncTask self)
        
        /**
         * Returns the average amount of time elapsed during each of the task's
         * previous run cycles, in seconds.
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_delay(self, AsyncTask_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_delay(AsyncTask self)
        
        /**
         * Returns the delay value that has been set via set_delay, if any.
         */
        """
        pass

    def get_dt(self, AsyncTask_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_dt(AsyncTask self)
        
        /**
         * Returns the amount of time elapsed during the task's previous run cycle, in
         * seconds.
         */
        """
        pass

    def get_elapsed_frames(self, AsyncTask_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_elapsed_frames(AsyncTask self)
        
        /**
         * Returns the number of frames that have elapsed since the task was started,
         * according to the task manager's clock.
         *
         * It is only valid to call this if the task's status is not S_inactive.
         */
        """
        pass

    def get_elapsed_time(self, AsyncTask_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_elapsed_time(AsyncTask self)
        
        /**
         * Returns the amount of time that has elapsed since the task was started,
         * according to the task manager's clock.
         *
         * It is only valid to call this if the task's status is not S_inactive.
         */
        """
        pass

    def get_manager(self, AsyncTask_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_manager(AsyncTask self)
        
        /**
         * Returns the AsyncTaskManager that this task is active on.  This will be
         * NULL if the state is S_inactive.
         */
        """
        pass

    def get_max_dt(self, AsyncTask_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_max_dt(AsyncTask self)
        
        /**
         * Returns the maximum amount of time elapsed during any one of the task's
         * previous run cycles, in seconds.
         */
        """
        pass

    def get_name_prefix(self, AsyncTask_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_name_prefix(AsyncTask self)
        
        /**
         * Returns the initial part of the name, up to but not including any trailing
         * digits following a hyphen or underscore.
         */
        """
        pass

    def get_priority(self, AsyncTask_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_priority(AsyncTask self)
        
        /**
         * Returns the task's current priority value.  See set_priority().
         */
        """
        pass

    def get_sort(self, AsyncTask_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_sort(AsyncTask self)
        
        /**
         * Returns the task's current sort value.  See set_sort().
         */
        """
        pass

    def get_start_frame(self, AsyncTask_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_start_frame(AsyncTask self)
        
        /**
         * Returns the frame number at which the task was started, according to the
         * task manager's clock.
         *
         * It is only valid to call this if the task's status is not S_inactive.
         */
        """
        pass

    def get_start_time(self, AsyncTask_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_start_time(AsyncTask self)
        
        /**
         * Returns the time at which the task was started, according to the task
         * manager's clock.
         *
         * It is only valid to call this if the task's status is not S_inactive.
         */
        """
        pass

    def get_state(self, AsyncTask_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_state(AsyncTask self)
        
        /**
         * Returns the current state of the task.
         */
        """
        pass

    def get_task_chain(self, AsyncTask_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_task_chain(AsyncTask self)
        
        /**
         * Returns the AsyncTaskChain on which this task will be running.  Each task
         * chain runs tasks independently of the others.
         */
        """
        pass

    def get_task_id(self, AsyncTask_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_task_id(AsyncTask self)
        
        /**
         * Returns a number guaranteed to be unique for each different AsyncTask
         * object in the universe.
         */
        """
        pass

    def get_wake_time(self, AsyncTask_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_wake_time(AsyncTask self)
        
        /**
         * If this task has been added to an AsyncTaskManager with a delay in effect,
         * this returns the time at which the task is expected to awaken.  It has no
         * meaning if the task has not yet been added to a queue, or if there was no
         * delay in effect at the time the task was added.
         *
         * If the task's status is not S_sleeping, this returns 0.0.
         */
        """
        pass

    def hasDelay(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_delay(AsyncTask self)
        
        /**
         * Returns true if a delay has been set for this task via set_delay(), or
         * false otherwise.
         */
        """
        pass

    def has_delay(self, AsyncTask_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_delay(AsyncTask self)
        
        /**
         * Returns true if a delay has been set for this task via set_delay(), or
         * false otherwise.
         */
        """
        pass

    def isAlive(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_alive(AsyncTask self)
        
        /**
         * Returns true if the task is currently active or sleeping on some task
         * chain, meaning that it will be executed in its turn, or false if it is not
         * active.  If the task has recently been removed while it is in the middle of
         * execution, this will return false, because the task will not run again once
         * it finishes.
         */
        """
        pass

    def is_alive(self, AsyncTask_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_alive(AsyncTask self)
        
        /**
         * Returns true if the task is currently active or sleeping on some task
         * chain, meaning that it will be executed in its turn, or false if it is not
         * active.  If the task has recently been removed while it is in the middle of
         * execution, this will return false, because the task will not run again once
         * it finishes.
         */
        """
        pass

    def output(self, AsyncTask_self, ostream_out): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        output(AsyncTask self, ostream out)
        
        /**
         *
         */
        """
        pass

    def recalcWakeTime(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        recalc_wake_time(const AsyncTask self)
        
        /**
         * If the task is currently sleeping on a task chain, this resets its wake
         * time to the current time + get_delay().  It is as if the task had suddenly
         * returned DS_again.  The task will sleep for its current delay seconds
         * before running again.  This method may therefore be used to make the task
         * wake up sooner or later than it would have otherwise.
         *
         * If the task is not already sleeping, this method has no effect.
         */
        """
        pass

    def recalc_wake_time(self, const_AsyncTask_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        recalc_wake_time(const AsyncTask self)
        
        /**
         * If the task is currently sleeping on a task chain, this resets its wake
         * time to the current time + get_delay().  It is as if the task had suddenly
         * returned DS_again.  The task will sleep for its current delay seconds
         * before running again.  This method may therefore be used to make the task
         * wake up sooner or later than it would have otherwise.
         *
         * If the task is not already sleeping, this method has no effect.
         */
        """
        pass

    def remove(self, const_AsyncTask_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        remove(const AsyncTask self)
        
        /**
         * Removes the task from its active manager, if any, and makes the state
         * S_inactive (or possible S_servicing_removed).  This is a no-op if the state
         * is already S_inactive.
         */
        """
        pass

    def setDelay(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_delay(const AsyncTask self, double delay)
        
        /**
         * Specifies the amount of time, in seconds, by which this task will be
         * delayed after it has been added to the AsyncTaskManager.  At least the
         * specified amount of time (and possibly more) will elapse before the task
         * begins.
         *
         * You may specify a delay of 0.0 to guarantee that the task will run in the
         * next epoch following the one in which it is added.
         *
         * Setting this value after the task has already been added will not affect
         * the task's wake time; it will only affect the task if it is re-added to the
         * queue in the future, for instance if the task returns DS_again.  However,
         * see recalc_wake_time() if you wish to apply the delay effect immediately.
         */
        """
        pass

    def setDoneEvent(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_done_event(const AsyncTask self, str done_event)
        
        /**
         * Sets the event name that will be triggered when the task finishes.  This
         * should only be called before the task has been started, or after it has
         * finished and before it is about to be restarted (i.e.  when get_state()
         * returns S_inactive).
         */
        """
        pass

    def setName(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_name(const AsyncTask self, str name)
        
        /**
         *
         */
        """
        pass

    def setPriority(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_priority(const AsyncTask self, int priority)
        
        /**
         * Specifies a priority value for this task.  In general, tasks with a higher
         * priority value are executed before tasks with a lower priority value (but
         * only for tasks with the same sort value).
         *
         * Unlike the sort value, tasks with different priorities may execute at the
         * same time, if the AsyncTaskManager has more than one thread servicing
         * tasks.
         *
         * Also see AsyncTaskChain::set_timeslice_priority(), which changes the
         * meaning of this value.  In the default mode, when the timeslice_priority
         * flag is false, all tasks always run once per epoch, regardless of their
         * priority values (that is, the priority controls the order of the task
         * execution only, not the number of times it runs).  On the other hand, if
         * you set the timeslice_priority flag to true, then changing a task's
         * priority has an effect on the number of times it runs.
         */
        """
        pass

    def setSort(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_sort(const AsyncTask self, int sort)
        
        /**
         * Specifies a sort value for this task.  Within a given AsyncTaskManager, all
         * of the tasks with a given sort value are guaranteed to be completed before
         * any tasks with a higher sort value are begun.
         *
         * To put it another way, two tasks might execute in parallel with each other
         * only if they both have the same sort value.  Tasks with a lower sort value
         * are executed first.
         *
         * This is different from the priority, which makes no such exclusion
         * guarantees.
         */
        """
        pass

    def setTaskChain(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_task_chain(const AsyncTask self, str chain_name)
        
        /**
         * Specifies the AsyncTaskChain on which this task will be running.  Each task
         * chain runs tasks independently of the others.
         */
        """
        pass

    def set_delay(self, const_AsyncTask_self, double_delay): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_delay(const AsyncTask self, double delay)
        
        /**
         * Specifies the amount of time, in seconds, by which this task will be
         * delayed after it has been added to the AsyncTaskManager.  At least the
         * specified amount of time (and possibly more) will elapse before the task
         * begins.
         *
         * You may specify a delay of 0.0 to guarantee that the task will run in the
         * next epoch following the one in which it is added.
         *
         * Setting this value after the task has already been added will not affect
         * the task's wake time; it will only affect the task if it is re-added to the
         * queue in the future, for instance if the task returns DS_again.  However,
         * see recalc_wake_time() if you wish to apply the delay effect immediately.
         */
        """
        pass

    def set_done_event(self, const_AsyncTask_self, str_done_event): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_done_event(const AsyncTask self, str done_event)
        
        /**
         * Sets the event name that will be triggered when the task finishes.  This
         * should only be called before the task has been started, or after it has
         * finished and before it is about to be restarted (i.e.  when get_state()
         * returns S_inactive).
         */
        """
        pass

    def set_name(self, const_AsyncTask_self, str_name): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_name(const AsyncTask self, str name)
        
        /**
         *
         */
        """
        pass

    def set_priority(self, const_AsyncTask_self, int_priority): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_priority(const AsyncTask self, int priority)
        
        /**
         * Specifies a priority value for this task.  In general, tasks with a higher
         * priority value are executed before tasks with a lower priority value (but
         * only for tasks with the same sort value).
         *
         * Unlike the sort value, tasks with different priorities may execute at the
         * same time, if the AsyncTaskManager has more than one thread servicing
         * tasks.
         *
         * Also see AsyncTaskChain::set_timeslice_priority(), which changes the
         * meaning of this value.  In the default mode, when the timeslice_priority
         * flag is false, all tasks always run once per epoch, regardless of their
         * priority values (that is, the priority controls the order of the task
         * execution only, not the number of times it runs).  On the other hand, if
         * you set the timeslice_priority flag to true, then changing a task's
         * priority has an effect on the number of times it runs.
         */
        """
        pass

    def set_sort(self, const_AsyncTask_self, int_sort): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_sort(const AsyncTask self, int sort)
        
        /**
         * Specifies a sort value for this task.  Within a given AsyncTaskManager, all
         * of the tasks with a given sort value are guaranteed to be completed before
         * any tasks with a higher sort value are begun.
         *
         * To put it another way, two tasks might execute in parallel with each other
         * only if they both have the same sort value.  Tasks with a lower sort value
         * are executed first.
         *
         * This is different from the priority, which makes no such exclusion
         * guarantees.
         */
        """
        pass

    def set_task_chain(self, const_AsyncTask_self, str_chain_name): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_task_chain(const AsyncTask self, str chain_name)
        
        /**
         * Specifies the AsyncTaskChain on which this task will be running.  Each task
         * chain runs tasks independently of the others.
         */
        """
        pass

    def upcastToAsyncFuture(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        upcast_to_AsyncFuture(const AsyncTask self)
        
        upcast from AsyncTask to AsyncFuture
        """
        pass

    def upcastToNamable(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        upcast_to_Namable(const AsyncTask self)
        
        upcast from AsyncTask to Namable
        """
        pass

    def upcast_to_AsyncFuture(self, const_AsyncTask_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        upcast_to_AsyncFuture(const AsyncTask self)
        
        upcast from AsyncTask to AsyncFuture
        """
        pass

    def upcast_to_Namable(self, const_AsyncTask_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        upcast_to_Namable(const AsyncTask self)
        
        upcast from AsyncTask to Namable
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

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    alive = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    average_dt = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    done_event = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """/**
 * Returns the event name that will be triggered when the future finishes.
 * See set_done_event().
 */"""

    dt = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """// This is a number guaranteed to be unique for each different AsyncTask
// object in the universe."""

    manager = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    max_dt = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """// The name of this task."""

    priority = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    sort = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    state = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    task_chain = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    DSAgain = 2
    DSAwait = 7
    DSCont = 1
    DSDone = 0
    DSExit = 4
    DSInterrupt = 6
    DSPause = 5
    DSPickup = 3
    DS_again = 2
    DS_await = 7
    DS_cont = 1
    DS_done = 0
    DS_exit = 4
    DS_interrupt = 6
    DS_pause = 5
    DS_pickup = 3
    DtoolClassDict = {
        'DSAgain': 2,
        'DSAwait': 7,
        'DSCont': 1,
        'DSDone': 0,
        'DSExit': 4,
        'DSInterrupt': 6,
        'DSPause': 5,
        'DSPickup': 3,
        'DS_again': 2,
        'DS_await': 7,
        'DS_cont': 1,
        'DS_done': 0,
        'DS_exit': 4,
        'DS_interrupt': 6,
        'DS_pause': 5,
        'DS_pickup': 3,
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        'SActive': 1,
        'SActiveNested': 5,
        'SAwaiting': 6,
        'SInactive': 0,
        'SServicing': 2,
        'SServicingRemoved': 3,
        'SSleeping': 4,
        'S_active': 1,
        'S_active_nested': 5,
        'S_awaiting': 6,
        'S_inactive': 0,
        'S_servicing': 2,
        'S_servicing_removed': 3,
        'S_sleeping': 4,
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.core.AsyncTask' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.core.AsyncTask' objects>"
        '__doc__': '/**\n * This class represents a concrete task performed by an AsyncManager.\n * Normally, you would subclass from this class, and override do_task(), to\n * define the functionality you wish to have the task perform.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.AsyncTask' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE2EF880>'
        '__repr__': None, # (!) real value is "<slot wrapper '__repr__' of 'panda3d.core.AsyncTask' objects>"
        '__str__': None, # (!) real value is "<slot wrapper '__str__' of 'panda3d.core.AsyncTask' objects>"
        'alive': None, # (!) real value is "<attribute 'alive' of 'panda3d.core.AsyncTask' objects>"
        'average_dt': None, # (!) real value is "<attribute 'average_dt' of 'panda3d.core.AsyncTask' objects>"
        'clearDelay': None, # (!) real value is "<method 'clearDelay' of 'panda3d.core.AsyncTask' objects>"
        'clearName': None, # (!) real value is "<method 'clearName' of 'panda3d.core.AsyncTask' objects>"
        'clear_delay': None, # (!) real value is "<method 'clear_delay' of 'panda3d.core.AsyncTask' objects>"
        'clear_name': None, # (!) real value is "<method 'clear_name' of 'panda3d.core.AsyncTask' objects>"
        'done_event': None, # (!) real value is "<attribute 'done_event' of 'panda3d.core.AsyncTask' objects>"
        'dt': None, # (!) real value is "<attribute 'dt' of 'panda3d.core.AsyncTask' objects>"
        'getAverageDt': None, # (!) real value is "<method 'getAverageDt' of 'panda3d.core.AsyncTask' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE2EF880>)>'
        'getDelay': None, # (!) real value is "<method 'getDelay' of 'panda3d.core.AsyncTask' objects>"
        'getDt': None, # (!) real value is "<method 'getDt' of 'panda3d.core.AsyncTask' objects>"
        'getElapsedFrames': None, # (!) real value is "<method 'getElapsedFrames' of 'panda3d.core.AsyncTask' objects>"
        'getElapsedTime': None, # (!) real value is "<method 'getElapsedTime' of 'panda3d.core.AsyncTask' objects>"
        'getManager': None, # (!) real value is "<method 'getManager' of 'panda3d.core.AsyncTask' objects>"
        'getMaxDt': None, # (!) real value is "<method 'getMaxDt' of 'panda3d.core.AsyncTask' objects>"
        'getNamePrefix': None, # (!) real value is "<method 'getNamePrefix' of 'panda3d.core.AsyncTask' objects>"
        'getPriority': None, # (!) real value is "<method 'getPriority' of 'panda3d.core.AsyncTask' objects>"
        'getSort': None, # (!) real value is "<method 'getSort' of 'panda3d.core.AsyncTask' objects>"
        'getStartFrame': None, # (!) real value is "<method 'getStartFrame' of 'panda3d.core.AsyncTask' objects>"
        'getStartTime': None, # (!) real value is "<method 'getStartTime' of 'panda3d.core.AsyncTask' objects>"
        'getState': None, # (!) real value is "<method 'getState' of 'panda3d.core.AsyncTask' objects>"
        'getTaskChain': None, # (!) real value is "<method 'getTaskChain' of 'panda3d.core.AsyncTask' objects>"
        'getTaskId': None, # (!) real value is "<method 'getTaskId' of 'panda3d.core.AsyncTask' objects>"
        'getWakeTime': None, # (!) real value is "<method 'getWakeTime' of 'panda3d.core.AsyncTask' objects>"
        'get_average_dt': None, # (!) real value is "<method 'get_average_dt' of 'panda3d.core.AsyncTask' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE2EF880>)>'
        'get_delay': None, # (!) real value is "<method 'get_delay' of 'panda3d.core.AsyncTask' objects>"
        'get_dt': None, # (!) real value is "<method 'get_dt' of 'panda3d.core.AsyncTask' objects>"
        'get_elapsed_frames': None, # (!) real value is "<method 'get_elapsed_frames' of 'panda3d.core.AsyncTask' objects>"
        'get_elapsed_time': None, # (!) real value is "<method 'get_elapsed_time' of 'panda3d.core.AsyncTask' objects>"
        'get_manager': None, # (!) real value is "<method 'get_manager' of 'panda3d.core.AsyncTask' objects>"
        'get_max_dt': None, # (!) real value is "<method 'get_max_dt' of 'panda3d.core.AsyncTask' objects>"
        'get_name_prefix': None, # (!) real value is "<method 'get_name_prefix' of 'panda3d.core.AsyncTask' objects>"
        'get_priority': None, # (!) real value is "<method 'get_priority' of 'panda3d.core.AsyncTask' objects>"
        'get_sort': None, # (!) real value is "<method 'get_sort' of 'panda3d.core.AsyncTask' objects>"
        'get_start_frame': None, # (!) real value is "<method 'get_start_frame' of 'panda3d.core.AsyncTask' objects>"
        'get_start_time': None, # (!) real value is "<method 'get_start_time' of 'panda3d.core.AsyncTask' objects>"
        'get_state': None, # (!) real value is "<method 'get_state' of 'panda3d.core.AsyncTask' objects>"
        'get_task_chain': None, # (!) real value is "<method 'get_task_chain' of 'panda3d.core.AsyncTask' objects>"
        'get_task_id': None, # (!) real value is "<method 'get_task_id' of 'panda3d.core.AsyncTask' objects>"
        'get_wake_time': None, # (!) real value is "<method 'get_wake_time' of 'panda3d.core.AsyncTask' objects>"
        'hasDelay': None, # (!) real value is "<method 'hasDelay' of 'panda3d.core.AsyncTask' objects>"
        'has_delay': None, # (!) real value is "<method 'has_delay' of 'panda3d.core.AsyncTask' objects>"
        'id': None, # (!) real value is "<attribute 'id' of 'panda3d.core.AsyncTask' objects>"
        'isAlive': None, # (!) real value is "<method 'isAlive' of 'panda3d.core.AsyncTask' objects>"
        'is_alive': None, # (!) real value is "<method 'is_alive' of 'panda3d.core.AsyncTask' objects>"
        'manager': None, # (!) real value is "<attribute 'manager' of 'panda3d.core.AsyncTask' objects>"
        'max_dt': None, # (!) real value is "<attribute 'max_dt' of 'panda3d.core.AsyncTask' objects>"
        'name': None, # (!) real value is "<attribute 'name' of 'panda3d.core.AsyncTask' objects>"
        'output': None, # (!) real value is "<method 'output' of 'panda3d.core.AsyncTask' objects>"
        'priority': None, # (!) real value is "<attribute 'priority' of 'panda3d.core.AsyncTask' objects>"
        'recalcWakeTime': None, # (!) real value is "<method 'recalcWakeTime' of 'panda3d.core.AsyncTask' objects>"
        'recalc_wake_time': None, # (!) real value is "<method 'recalc_wake_time' of 'panda3d.core.AsyncTask' objects>"
        'remove': None, # (!) real value is "<method 'remove' of 'panda3d.core.AsyncTask' objects>"
        'setDelay': None, # (!) real value is "<method 'setDelay' of 'panda3d.core.AsyncTask' objects>"
        'setDoneEvent': None, # (!) real value is "<method 'setDoneEvent' of 'panda3d.core.AsyncTask' objects>"
        'setName': None, # (!) real value is "<method 'setName' of 'panda3d.core.AsyncTask' objects>"
        'setPriority': None, # (!) real value is "<method 'setPriority' of 'panda3d.core.AsyncTask' objects>"
        'setSort': None, # (!) real value is "<method 'setSort' of 'panda3d.core.AsyncTask' objects>"
        'setTaskChain': None, # (!) real value is "<method 'setTaskChain' of 'panda3d.core.AsyncTask' objects>"
        'set_delay': None, # (!) real value is "<method 'set_delay' of 'panda3d.core.AsyncTask' objects>"
        'set_done_event': None, # (!) real value is "<method 'set_done_event' of 'panda3d.core.AsyncTask' objects>"
        'set_name': None, # (!) real value is "<method 'set_name' of 'panda3d.core.AsyncTask' objects>"
        'set_priority': None, # (!) real value is "<method 'set_priority' of 'panda3d.core.AsyncTask' objects>"
        'set_sort': None, # (!) real value is "<method 'set_sort' of 'panda3d.core.AsyncTask' objects>"
        'set_task_chain': None, # (!) real value is "<method 'set_task_chain' of 'panda3d.core.AsyncTask' objects>"
        'sort': None, # (!) real value is "<attribute 'sort' of 'panda3d.core.AsyncTask' objects>"
        'state': None, # (!) real value is "<attribute 'state' of 'panda3d.core.AsyncTask' objects>"
        'task_chain': None, # (!) real value is "<attribute 'task_chain' of 'panda3d.core.AsyncTask' objects>"
        'upcastToAsyncFuture': None, # (!) real value is "<method 'upcastToAsyncFuture' of 'panda3d.core.AsyncTask' objects>"
        'upcastToNamable': None, # (!) real value is "<method 'upcastToNamable' of 'panda3d.core.AsyncTask' objects>"
        'upcast_to_AsyncFuture': None, # (!) real value is "<method 'upcast_to_AsyncFuture' of 'panda3d.core.AsyncTask' objects>"
        'upcast_to_Namable': None, # (!) real value is "<method 'upcast_to_Namable' of 'panda3d.core.AsyncTask' objects>"
    }
    SActive = 1
    SActiveNested = 5
    SAwaiting = 6
    SInactive = 0
    SServicing = 2
    SServicingRemoved = 3
    SSleeping = 4
    S_active = 1
    S_active_nested = 5
    S_awaiting = 6
    S_inactive = 0
    S_servicing = 2
    S_servicing_removed = 3
    S_sleeping = 4


