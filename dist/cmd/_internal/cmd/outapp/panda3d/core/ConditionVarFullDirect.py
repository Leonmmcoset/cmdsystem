# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


class ConditionVarFullDirect(__dtoolconfig.DTOOL_SUPER_BASE):
    """
    /**
     * A condition variable, usually used to communicate information about
     * changing state to a thread that is waiting for something to happen.  A
     * condition variable can be used to "wake up" a thread when some arbitrary
     * condition has changed.
     *
     * A condition variable is associated with a single mutex, and several
     * condition variables may share the same mutex.
     */
    """
    def getMutex(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_mutex(ConditionVarFullDirect self)
        
        /**
         * Returns the mutex associated with this condition variable.
         */
        """
        pass

    def get_mutex(self, ConditionVarFullDirect_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_mutex(ConditionVarFullDirect self)
        
        /**
         * Returns the mutex associated with this condition variable.
         */
        """
        pass

    def notify(self, const_ConditionVarFullDirect_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        notify(const ConditionVarFullDirect self)
        
        /**
         * Informs one of the other threads who are currently blocked on wait() that
         * the relevant condition has changed.  If multiple threads are currently
         * waiting, at least one of them will be woken up, although there is no way to
         * predict which one.  It is possible that more than one thread will be woken
         * up.
         *
         * The caller must be holding the mutex associated with the condition variable
         * before making this call, which will not release the mutex.
         *
         * If no threads are waiting, this is a no-op: the notify is lost.
         */
        """
        pass

    def notifyAll(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        notify_all(const ConditionVarFullDirect self)
        
        /**
         * Informs all of the other threads who are currently blocked on wait() that
         * the relevant condition has changed.
         *
         * The caller must be holding the mutex associated with the condition variable
         * before making this call, which will not release the mutex.
         *
         * If no threads are waiting, this is a no-op: the notify event is lost.
         */
        """
        pass

    def notify_all(self, const_ConditionVarFullDirect_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        notify_all(const ConditionVarFullDirect self)
        
        /**
         * Informs all of the other threads who are currently blocked on wait() that
         * the relevant condition has changed.
         *
         * The caller must be holding the mutex associated with the condition variable
         * before making this call, which will not release the mutex.
         *
         * If no threads are waiting, this is a no-op: the notify event is lost.
         */
        """
        pass

    def output(self, ConditionVarFullDirect_self, ostream_out): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        output(ConditionVarFullDirect self, ostream out)
        
        /**
         * This method is declared virtual in ConditionVarFullDebug, but non-virtual
         * in ConditionVarFullDirect.
         */
        """
        pass

    def wait(self, const_ConditionVarFullDirect_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        wait(const ConditionVarFullDirect self)
        wait(const ConditionVarFullDirect self, double timeout)
        
        /**
         * Waits on the condition.  The caller must already be holding the lock
         * associated with the condition variable before calling this function.
         *
         * wait() will release the lock, then go to sleep until some other thread
         * calls notify() on this condition variable.  At that time at least one
         * thread waiting on the same ConditionVarFullDirect will grab the lock again,
         * and then return from wait().
         *
         * It is possible that wait() will return even if no one has called notify().
         * It is the responsibility of the calling process to verify the condition on
         * return from wait, and possibly loop back to wait again if necessary.
         *
         * Note the semantics of a condition variable: the mutex must be held before
         * wait() is called, and it will still be held when wait() returns.  However,
         * it will be temporarily released during the wait() call itself.
         */
        
        /**
         * Waits on the condition, with a timeout.  The function will return when the
         * condition variable is notified, or the timeout occurs.  There is no way to
         * directly tell which happened, and it is possible that neither in fact
         * happened (spurious wakeups are possible).
         *
         * See wait() with no parameters for more.
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
        '__doc__': '/**\n * A condition variable, usually used to communicate information about\n * changing state to a thread that is waiting for something to happen.  A\n * condition variable can be used to "wake up" a thread when some arbitrary\n * condition has changed.\n *\n * A condition variable is associated with a single mutex, and several\n * condition variables may share the same mutex.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.ConditionVarFullDirect' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE2EBA70>'
        '__repr__': None, # (!) real value is "<slot wrapper '__repr__' of 'panda3d.core.ConditionVarFullDirect' objects>"
        '__str__': None, # (!) real value is "<slot wrapper '__str__' of 'panda3d.core.ConditionVarFullDirect' objects>"
        'getMutex': None, # (!) real value is "<method 'getMutex' of 'panda3d.core.ConditionVarFullDirect' objects>"
        'get_mutex': None, # (!) real value is "<method 'get_mutex' of 'panda3d.core.ConditionVarFullDirect' objects>"
        'notify': None, # (!) real value is "<method 'notify' of 'panda3d.core.ConditionVarFullDirect' objects>"
        'notifyAll': None, # (!) real value is "<method 'notifyAll' of 'panda3d.core.ConditionVarFullDirect' objects>"
        'notify_all': None, # (!) real value is "<method 'notify_all' of 'panda3d.core.ConditionVarFullDirect' objects>"
        'output': None, # (!) real value is "<method 'output' of 'panda3d.core.ConditionVarFullDirect' objects>"
        'wait': None, # (!) real value is "<method 'wait' of 'panda3d.core.ConditionVarFullDirect' objects>"
    }


