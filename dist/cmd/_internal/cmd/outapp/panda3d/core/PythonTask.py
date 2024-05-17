# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .AsyncTask import AsyncTask

class PythonTask(AsyncTask):
    """
    /**
     * This class exists to allow association of a Python function or coroutine
     * with the AsyncTaskManager.
     */
    """
    def getArgs(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_args(const PythonTask self)
        """
        pass

    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getFunction(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_function(const PythonTask self)
        
        /**
         * Returns the function that is called when the task runs.
         */
        """
        pass

    def getOwner(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_owner(PythonTask self)
        
        /**
         * Returns the "owner" object.  See set_owner().
         */
        """
        pass

    def getUponDeath(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_upon_death(const PythonTask self)
        
        /**
         * Returns the function that is called when the task finishes.
         */
        """
        pass

    def get_args(self, const_PythonTask_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_args(const PythonTask self)
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_function(self, const_PythonTask_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_function(const PythonTask self)
        
        /**
         * Returns the function that is called when the task runs.
         */
        """
        pass

    def get_owner(self, PythonTask_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_owner(PythonTask self)
        
        /**
         * Returns the "owner" object.  See set_owner().
         */
        """
        pass

    def get_upon_death(self, const_PythonTask_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_upon_death(const PythonTask self)
        
        /**
         * Returns the function that is called when the task finishes.
         */
        """
        pass

    def setArgs(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_args(const PythonTask self, object args, bool append_task)
        """
        pass

    def setFunction(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_function(const PythonTask self, object function)
        """
        pass

    def setOwner(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_owner(const PythonTask self, object owner)
        """
        pass

    def setResult(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_result(const PythonTask self, object result)
        
        /**
         * Sets the "result" of this task.  This is the value returned from an "await"
         * expression on this task.
         * This can only be called while the task is still alive.
         */
        """
        pass

    def setUponDeath(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_upon_death(const PythonTask self, object upon_death)
        """
        pass

    def set_args(self, const_PythonTask_self, object_args, bool_append_task): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_args(const PythonTask self, object args, bool append_task)
        """
        pass

    def set_function(self, const_PythonTask_self, object_function): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_function(const PythonTask self, object function)
        """
        pass

    def set_owner(self, const_PythonTask_self, object_owner): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_owner(const PythonTask self, object owner)
        """
        pass

    def set_result(self, const_PythonTask_self, object_result): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_result(const PythonTask self, object result)
        
        /**
         * Sets the "result" of this task.  This is the value returned from an "await"
         * expression on this task.
         * This can only be called while the task is still alive.
         */
        """
        pass

    def set_upon_death(self, const_PythonTask_self, object_upon_death): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_upon_death(const PythonTask self, object upon_death)
        """
        pass

    def __copy__(self, *args, **kwargs): # real signature unknown
        pass

    def __deepcopy__(self, *args, **kwargs): # real signature unknown
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    delayTime = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """// Alias of delay_time."""

    delay_time = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """// The delay value that has been set on this task, if any, or None."""

    frame = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """// The number of frames that have elapsed since the task was started,
// according to the task manager's clock."""

    time = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """// The amount of seconds that have elapsed since the task was started,
// according to the task manager's clock."""

    wakeTime = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """// Alias of wake_time."""

    wake_time = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """// If this task has been added to an AsyncTaskManager with a delay in
// effect, this contains the time at which the task is expected to awaken.
// It has no meaning of the task has not yet been added to a queue, or if
// there was no delay in effect at the time the task was added.  If the
// task's status is not S_sleeping, this contains 0.0."""


    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.core.PythonTask' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.core.PythonTask' objects>"
        '__delattr__': None, # (!) real value is "<slot wrapper '__delattr__' of 'panda3d.core.PythonTask' objects>"
        '__dict__': None, # (!) real value is "<attribute '__dict__' of 'panda3d.core.PythonTask' objects>"
        '__doc__': '/**\n * This class exists to allow association of a Python function or coroutine\n * with the AsyncTaskManager.\n */',
        '__getattribute__': None, # (!) real value is "<slot wrapper '__getattribute__' of 'panda3d.core.PythonTask' objects>"
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.PythonTask' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE2F0E40>'
        '__setattr__': None, # (!) real value is "<slot wrapper '__setattr__' of 'panda3d.core.PythonTask' objects>"
        'delayTime': None, # (!) real value is "<attribute 'delayTime' of 'panda3d.core.PythonTask' objects>"
        'delay_time': None, # (!) real value is "<attribute 'delay_time' of 'panda3d.core.PythonTask' objects>"
        'frame': None, # (!) real value is "<attribute 'frame' of 'panda3d.core.PythonTask' objects>"
        'getArgs': None, # (!) real value is "<method 'getArgs' of 'panda3d.core.PythonTask' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE2F0E40>)>'
        'getFunction': None, # (!) real value is "<method 'getFunction' of 'panda3d.core.PythonTask' objects>"
        'getOwner': None, # (!) real value is "<method 'getOwner' of 'panda3d.core.PythonTask' objects>"
        'getUponDeath': None, # (!) real value is "<method 'getUponDeath' of 'panda3d.core.PythonTask' objects>"
        'get_args': None, # (!) real value is "<method 'get_args' of 'panda3d.core.PythonTask' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE2F0E40>)>'
        'get_function': None, # (!) real value is "<method 'get_function' of 'panda3d.core.PythonTask' objects>"
        'get_owner': None, # (!) real value is "<method 'get_owner' of 'panda3d.core.PythonTask' objects>"
        'get_upon_death': None, # (!) real value is "<method 'get_upon_death' of 'panda3d.core.PythonTask' objects>"
        'setArgs': None, # (!) real value is "<method 'setArgs' of 'panda3d.core.PythonTask' objects>"
        'setFunction': None, # (!) real value is "<method 'setFunction' of 'panda3d.core.PythonTask' objects>"
        'setOwner': None, # (!) real value is "<method 'setOwner' of 'panda3d.core.PythonTask' objects>"
        'setResult': None, # (!) real value is "<method 'setResult' of 'panda3d.core.PythonTask' objects>"
        'setUponDeath': None, # (!) real value is "<method 'setUponDeath' of 'panda3d.core.PythonTask' objects>"
        'set_args': None, # (!) real value is "<method 'set_args' of 'panda3d.core.PythonTask' objects>"
        'set_function': None, # (!) real value is "<method 'set_function' of 'panda3d.core.PythonTask' objects>"
        'set_owner': None, # (!) real value is "<method 'set_owner' of 'panda3d.core.PythonTask' objects>"
        'set_result': None, # (!) real value is "<method 'set_result' of 'panda3d.core.PythonTask' objects>"
        'set_upon_death': None, # (!) real value is "<method 'set_upon_death' of 'panda3d.core.PythonTask' objects>"
        'time': None, # (!) real value is "<attribute 'time' of 'panda3d.core.PythonTask' objects>"
        'wakeTime': None, # (!) real value is "<attribute 'wakeTime' of 'panda3d.core.PythonTask' objects>"
        'wake_time': None, # (!) real value is "<attribute 'wake_time' of 'panda3d.core.PythonTask' objects>"
    }
    __dict__ = None # (!) real value is "mappingproxy({'DtoolClassDict': {...}, '__new__': <built-in method __new__ of type object at 0x00007FFCFE2F0E40>, '__getattribute__': <slot wrapper '__getattribute__' of 'panda3d.core.PythonTask' objects>, '__setattr__': <slot wrapper '__setattr__' of 'panda3d.core.PythonTask' objects>, '__delattr__': <slot wrapper '__delattr__' of 'panda3d.core.PythonTask' objects>, '__init__': <slot wrapper '__init__' of 'panda3d.core.PythonTask' objects>, 'set_function': <method 'set_function' of 'panda3d.core.PythonTask' objects>, 'setFunction': <method 'setFunction' of 'panda3d.core.PythonTask' objects>, 'get_function': <method 'get_function' of 'panda3d.core.PythonTask' objects>, 'getFunction': <method 'getFunction' of 'panda3d.core.PythonTask' objects>, 'set_args': <method 'set_args' of 'panda3d.core.PythonTask' objects>, 'setArgs': <method 'setArgs' of 'panda3d.core.PythonTask' objects>, 'get_args': <method 'get_args' of 'panda3d.core.PythonTask' objects>, 'getArgs': <method 'getArgs' of 'panda3d.core.PythonTask' objects>, 'set_upon_death': <method 'set_upon_death' of 'panda3d.core.PythonTask' objects>, 'setUponDeath': <method 'setUponDeath' of 'panda3d.core.PythonTask' objects>, 'get_upon_death': <method 'get_upon_death' of 'panda3d.core.PythonTask' objects>, 'getUponDeath': <method 'getUponDeath' of 'panda3d.core.PythonTask' objects>, 'set_owner': <method 'set_owner' of 'panda3d.core.PythonTask' objects>, 'setOwner': <method 'setOwner' of 'panda3d.core.PythonTask' objects>, 'get_owner': <method 'get_owner' of 'panda3d.core.PythonTask' objects>, 'getOwner': <method 'getOwner' of 'panda3d.core.PythonTask' objects>, 'set_result': <method 'set_result' of 'panda3d.core.PythonTask' objects>, 'setResult': <method 'setResult' of 'panda3d.core.PythonTask' objects>, 'get_class_type': <staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE2F0E40>)>, 'getClassType': <staticmethod(<built-in method getClassType of type object at 0x00007FFCFE2F0E40>)>, '__copy__': <method '__copy__' of 'panda3d.core.PythonTask' objects>, '__deepcopy__': <method '__deepcopy__' of 'panda3d.core.PythonTask' objects>, 'time': <attribute 'time' of 'panda3d.core.PythonTask' objects>, 'wake_time': <attribute 'wake_time' of 'panda3d.core.PythonTask' objects>, 'wakeTime': <attribute 'wakeTime' of 'panda3d.core.PythonTask' objects>, 'delay_time': <attribute 'delay_time' of 'panda3d.core.PythonTask' objects>, 'delayTime': <attribute 'delayTime' of 'panda3d.core.PythonTask' objects>, 'frame': <attribute 'frame' of 'panda3d.core.PythonTask' objects>, '__dict__': <attribute '__dict__' of 'panda3d.core.PythonTask' objects>, '__doc__': '/**\\n * This class exists to allow association of a Python function or coroutine\\n * with the AsyncTaskManager.\\n */'})"


