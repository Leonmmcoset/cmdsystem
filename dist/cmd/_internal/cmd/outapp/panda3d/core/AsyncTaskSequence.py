# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .AsyncTask import AsyncTask

from .AsyncTaskCollection import AsyncTaskCollection

class AsyncTaskSequence(AsyncTask, AsyncTaskCollection):
    """
    /**
     * A special kind of task that serves as a list of tasks internally.  Each
     * task on the list is executed in sequence, one per epoch.
     *
     * This is similar to a Sequence interval, though it has some slightly
     * different abilities.  For instance, although you can't start at any
     * arbitrary point in the sequence, you can construct a task sequence whose
     * duration changes during playback.
     */
    """
    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getCurrentTaskIndex(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_current_task_index(AsyncTaskSequence self)
        
        /**
         * Returns the index of the task within the sequence that is currently being
         * executed (or that will be executed at the next epoch).
         */
        """
        pass

    def getRepeatCount(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_repeat_count(AsyncTaskSequence self)
        
        /**
         * Returns the repeat count of the sequence.  See set_repeat_count().
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_current_task_index(self, AsyncTaskSequence_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_current_task_index(AsyncTaskSequence self)
        
        /**
         * Returns the index of the task within the sequence that is currently being
         * executed (or that will be executed at the next epoch).
         */
        """
        pass

    def get_repeat_count(self, AsyncTaskSequence_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_repeat_count(AsyncTaskSequence self)
        
        /**
         * Returns the repeat count of the sequence.  See set_repeat_count().
         */
        """
        pass

    def setRepeatCount(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_repeat_count(const AsyncTaskSequence self, int repeat_count)
        
        /**
         * Sets the repeat count of the sequence.  If the count is 0 or 1, the
         * sequence will run exactly once.  If it is greater than 0, it will run that
         * number of times.  If it is negative, it will run forever until it is
         * explicitly removed.
         */
        """
        pass

    def set_repeat_count(self, const_AsyncTaskSequence_self, int_repeat_count): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_repeat_count(const AsyncTaskSequence self, int repeat_count)
        
        /**
         * Sets the repeat count of the sequence.  If the count is 0 or 1, the
         * sequence will run exactly once.  If it is greater than 0, it will run that
         * number of times.  If it is negative, it will run forever until it is
         * explicitly removed.
         */
        """
        pass

    def upcastToAsyncTask(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        upcast_to_AsyncTask(const AsyncTaskSequence self)
        
        upcast from AsyncTaskSequence to AsyncTask
        """
        pass

    def upcastToAsyncTaskCollection(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        upcast_to_AsyncTaskCollection(const AsyncTaskSequence self)
        
        upcast from AsyncTaskSequence to AsyncTaskCollection
        """
        pass

    def upcast_to_AsyncTask(self, const_AsyncTaskSequence_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        upcast_to_AsyncTask(const AsyncTaskSequence self)
        
        upcast from AsyncTaskSequence to AsyncTask
        """
        pass

    def upcast_to_AsyncTaskCollection(self, const_AsyncTaskSequence_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        upcast_to_AsyncTaskCollection(const AsyncTaskSequence self)
        
        upcast from AsyncTaskSequence to AsyncTaskCollection
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
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.core.AsyncTaskSequence' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.core.AsyncTaskSequence' objects>"
        '__doc__': "/**\n * A special kind of task that serves as a list of tasks internally.  Each\n * task on the list is executed in sequence, one per epoch.\n *\n * This is similar to a Sequence interval, though it has some slightly\n * different abilities.  For instance, although you can't start at any\n * arbitrary point in the sequence, you can construct a task sequence whose\n * duration changes during playback.\n */",
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.AsyncTaskSequence' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE2F0190>'
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE2F0190>)>'
        'getCurrentTaskIndex': None, # (!) real value is "<method 'getCurrentTaskIndex' of 'panda3d.core.AsyncTaskSequence' objects>"
        'getRepeatCount': None, # (!) real value is "<method 'getRepeatCount' of 'panda3d.core.AsyncTaskSequence' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE2F0190>)>'
        'get_current_task_index': None, # (!) real value is "<method 'get_current_task_index' of 'panda3d.core.AsyncTaskSequence' objects>"
        'get_repeat_count': None, # (!) real value is "<method 'get_repeat_count' of 'panda3d.core.AsyncTaskSequence' objects>"
        'setRepeatCount': None, # (!) real value is "<method 'setRepeatCount' of 'panda3d.core.AsyncTaskSequence' objects>"
        'set_repeat_count': None, # (!) real value is "<method 'set_repeat_count' of 'panda3d.core.AsyncTaskSequence' objects>"
        'upcastToAsyncTask': None, # (!) real value is "<method 'upcastToAsyncTask' of 'panda3d.core.AsyncTaskSequence' objects>"
        'upcastToAsyncTaskCollection': None, # (!) real value is "<method 'upcastToAsyncTaskCollection' of 'panda3d.core.AsyncTaskSequence' objects>"
        'upcast_to_AsyncTask': None, # (!) real value is "<method 'upcast_to_AsyncTask' of 'panda3d.core.AsyncTaskSequence' objects>"
        'upcast_to_AsyncTaskCollection': None, # (!) real value is "<method 'upcast_to_AsyncTaskCollection' of 'panda3d.core.AsyncTaskSequence' objects>"
    }


