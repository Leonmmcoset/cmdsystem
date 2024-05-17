# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .TypedReferenceCount import TypedReferenceCount

class AsyncFuture(TypedReferenceCount):
    """
    /**
     * This class represents a thread-safe handle to a promised future result of
     * an asynchronous operation, providing methods to query its status and result
     * as well as register callbacks for this future's completion.
     *
     * An AsyncFuture can be awaited from within a coroutine or task.  It keeps
     * track of tasks waiting for this future and automatically reactivates them
     * upon this future's completion.
     *
     * A task itself is also a subclass of AsyncFuture.  Other subclasses are
     * not generally necessary, except to override the function of `cancel()`.
     *
     * Until the future is done, it is "owned" by the resolver thread, though it's
     * still legal for other threads to query its state.  When the resolver thread
     * resolves this future using `set_result()`, or any thread calls `cancel()`,
     * it instantly enters the "done" state, after which the result becomes a
     * read-only field that all threads can access.
     *
     * When the future returns true for done(), a thread can use cancelled() to
     * determine whether the future was cancelled or get_result() to access the
     * result of the operation.  Not all operations define a meaningful result
     * value, so some will always return nullptr.
     *
     * In Python, the `cancelled()`, `wait()` and `get_result()` methods are
     * wrapped up into a single `result()` method which waits for the future to
     * complete before either returning the result or throwing an exception if the
     * future was cancelled.
     * However, it is preferable to use the `await` keyword when running from a
     * coroutine, which only suspends the current task and not the entire thread.
     *
     * This API aims to mirror and be compatible with Python's Future class.
     *
     * @since 1.10.0
     */
    """
    def addDoneCallback(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_done_callback(const AsyncFuture self, object fn)
        """
        pass

    def add_done_callback(self, const_AsyncFuture_self, object_fn): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_done_callback(const AsyncFuture self, object fn)
        """
        pass

    def cancel(self, const_AsyncFuture_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        cancel(const AsyncFuture self)
        
        /**
         * Cancels the future.  Returns true if it was cancelled, or false if the
         * future was already done.  Either way, done() will return true after this
         * call returns.
         *
         * In the case of a task, this is equivalent to remove().
         */
        """
        pass

    def cancelled(self, AsyncFuture_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        cancelled(AsyncFuture self)
        
        /**
         * Returns true if the future was cancelled.  It is always safe to call this.
         */
        """
        pass

    def done(self, AsyncFuture_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        done(AsyncFuture self)
        
        /**
         * Returns true if the future is done or has been cancelled.  It is always
         * safe to call this.
         */
        """
        pass

    def gather(self, *args, **kwargs): # real signature unknown
        """
        /**
         * Creates a new future that returns `done()` when all of the contained
         * futures are done.
         *
         * Calling `cancel()` on the returned future will result in all contained
         * futures that have not yet finished to be cancelled.
         */
        """
        pass

    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getDoneEvent(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_done_event(AsyncFuture self)
        
        /**
         * Returns the event name that will be triggered when the future finishes.
         * See set_done_event().
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_done_event(self, AsyncFuture_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_done_event(AsyncFuture self)
        
        /**
         * Returns the event name that will be triggered when the future finishes.
         * See set_done_event().
         */
        """
        pass

    def output(self, AsyncFuture_self, ostream_out): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        output(AsyncFuture self, ostream out)
        
        /**
         *
         */
        """
        pass

    def result(self, AsyncFuture_self, object_timeout): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        result(AsyncFuture self, object timeout)
        """
        pass

    def setDoneEvent(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_done_event(const AsyncFuture self, str done_event)
        
        /**
         * Sets the event name that will be triggered when the future finishes.  Will
         * not be triggered if the future is cancelled, but it will be triggered for
         * a coroutine task that exits with an exception.
         */
        """
        pass

    def setResult(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_result(const AsyncFuture self, object param0)
        
        /**
         * Sets this future's result.  Can only be called if done() returns false.
         */
        
        /**
         * Sets this future's result.  Can only be done while the future is not done.
         * Calling this marks the future as done and schedules the done callbacks.
         *
         * This variant takes two pointers; the second one is only set if this object
         * inherits from ReferenceCount, so that a reference can be held.
         *
         * Assumes the manager's lock is *not* held.
         */
        """
        pass

    def set_done_event(self, const_AsyncFuture_self, str_done_event): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_done_event(const AsyncFuture self, str done_event)
        
        /**
         * Sets the event name that will be triggered when the future finishes.  Will
         * not be triggered if the future is cancelled, but it will be triggered for
         * a coroutine task that exits with an exception.
         */
        """
        pass

    def set_result(self, const_AsyncFuture_self, object_param0): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_result(const AsyncFuture self, object param0)
        
        /**
         * Sets this future's result.  Can only be called if done() returns false.
         */
        
        /**
         * Sets this future's result.  Can only be done while the future is not done.
         * Calling this marks the future as done and schedules the done callbacks.
         *
         * This variant takes two pointers; the second one is only set if this object
         * inherits from ReferenceCount, so that a reference can be held.
         *
         * Assumes the manager's lock is *not* held.
         */
        """
        pass

    def wait(self, const_AsyncFuture_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        wait(const AsyncFuture self)
        wait(const AsyncFuture self, double timeout)
        
        /**
         * Waits until the future is done.
         */
        
        /**
         * Waits until the future is done, or until the timeout is reached.
         */
        """
        pass

    def __await__(self, *args, **kwargs): # real signature unknown
        """ Return an iterator to be used in await expression. """
        pass

    def __copy__(self, *args, **kwargs): # real signature unknown
        pass

    def __deepcopy__(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __iter__(self, *args, **kwargs): # real signature unknown
        """ Implement iter(self). """
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

    done_event = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__await__': None, # (!) real value is "<slot wrapper '__await__' of 'panda3d.core.AsyncFuture' objects>"
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.core.AsyncFuture' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.core.AsyncFuture' objects>"
        '__doc__': '/**\n * This class represents a thread-safe handle to a promised future result of\n * an asynchronous operation, providing methods to query its status and result\n * as well as register callbacks for this future\'s completion.\n *\n * An AsyncFuture can be awaited from within a coroutine or task.  It keeps\n * track of tasks waiting for this future and automatically reactivates them\n * upon this future\'s completion.\n *\n * A task itself is also a subclass of AsyncFuture.  Other subclasses are\n * not generally necessary, except to override the function of `cancel()`.\n *\n * Until the future is done, it is "owned" by the resolver thread, though it\'s\n * still legal for other threads to query its state.  When the resolver thread\n * resolves this future using `set_result()`, or any thread calls `cancel()`,\n * it instantly enters the "done" state, after which the result becomes a\n * read-only field that all threads can access.\n *\n * When the future returns true for done(), a thread can use cancelled() to\n * determine whether the future was cancelled or get_result() to access the\n * result of the operation.  Not all operations define a meaningful result\n * value, so some will always return nullptr.\n *\n * In Python, the `cancelled()`, `wait()` and `get_result()` methods are\n * wrapped up into a single `result()` method which waits for the future to\n * complete before either returning the result or throwing an exception if the\n * future was cancelled.\n * However, it is preferable to use the `await` keyword when running from a\n * coroutine, which only suspends the current task and not the entire thread.\n *\n * This API aims to mirror and be compatible with Python\'s Future class.\n *\n * @since 1.10.0\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.AsyncFuture' objects>"
        '__iter__': None, # (!) real value is "<slot wrapper '__iter__' of 'panda3d.core.AsyncFuture' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE2EF6B0>'
        '__repr__': None, # (!) real value is "<slot wrapper '__repr__' of 'panda3d.core.AsyncFuture' objects>"
        '__str__': None, # (!) real value is "<slot wrapper '__str__' of 'panda3d.core.AsyncFuture' objects>"
        'addDoneCallback': None, # (!) real value is "<method 'addDoneCallback' of 'panda3d.core.AsyncFuture' objects>"
        'add_done_callback': None, # (!) real value is "<method 'add_done_callback' of 'panda3d.core.AsyncFuture' objects>"
        'cancel': None, # (!) real value is "<method 'cancel' of 'panda3d.core.AsyncFuture' objects>"
        'cancelled': None, # (!) real value is "<method 'cancelled' of 'panda3d.core.AsyncFuture' objects>"
        'done': None, # (!) real value is "<method 'done' of 'panda3d.core.AsyncFuture' objects>"
        'done_event': None, # (!) real value is "<attribute 'done_event' of 'panda3d.core.AsyncFuture' objects>"
        'gather': None, # (!) real value is '<staticmethod(<built-in method gather of type object at 0x00007FFCFE2EF6B0>)>'
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE2EF6B0>)>'
        'getDoneEvent': None, # (!) real value is "<method 'getDoneEvent' of 'panda3d.core.AsyncFuture' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE2EF6B0>)>'
        'get_done_event': None, # (!) real value is "<method 'get_done_event' of 'panda3d.core.AsyncFuture' objects>"
        'output': None, # (!) real value is "<method 'output' of 'panda3d.core.AsyncFuture' objects>"
        'result': None, # (!) real value is "<method 'result' of 'panda3d.core.AsyncFuture' objects>"
        'setDoneEvent': None, # (!) real value is "<method 'setDoneEvent' of 'panda3d.core.AsyncFuture' objects>"
        'setResult': None, # (!) real value is "<method 'setResult' of 'panda3d.core.AsyncFuture' objects>"
        'set_done_event': None, # (!) real value is "<method 'set_done_event' of 'panda3d.core.AsyncFuture' objects>"
        'set_result': None, # (!) real value is "<method 'set_result' of 'panda3d.core.AsyncFuture' objects>"
        'wait': None, # (!) real value is "<method 'wait' of 'panda3d.core.AsyncFuture' objects>"
    }


