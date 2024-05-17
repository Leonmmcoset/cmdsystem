# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


class AsyncTaskCollection(__dtoolconfig.DTOOL_SUPER_BASE):
    """
    /**
     * A list of tasks, for instance as returned by some of the AsyncTaskManager
     * query functions.  This also serves to define an AsyncTaskSequence.
     *
     * TODO: None of this is thread-safe yet.
     */
    """
    def addTask(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_task(const AsyncTaskCollection self, AsyncTask task)
        
        /**
         * Adds a new AsyncTask to the collection.
         */
        """
        pass

    def addTasksFrom(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_tasks_from(const AsyncTaskCollection self, const AsyncTaskCollection other)
        
        /**
         * Adds all the AsyncTasks indicated in the other collection to this task.
         * The other tasks are simply appended to the end of the tasks in this list;
         * duplicates are not automatically removed.
         */
        """
        pass

    def add_task(self, const_AsyncTaskCollection_self, AsyncTask_task): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_task(const AsyncTaskCollection self, AsyncTask task)
        
        /**
         * Adds a new AsyncTask to the collection.
         */
        """
        pass

    def add_tasks_from(self, const_AsyncTaskCollection_self, const_AsyncTaskCollection_other): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_tasks_from(const AsyncTaskCollection self, const AsyncTaskCollection other)
        
        /**
         * Adds all the AsyncTasks indicated in the other collection to this task.
         * The other tasks are simply appended to the end of the tasks in this list;
         * duplicates are not automatically removed.
         */
        """
        pass

    def assign(self, const_AsyncTaskCollection_self, const_AsyncTaskCollection_copy): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        assign(const AsyncTaskCollection self, const AsyncTaskCollection copy)
        """
        pass

    def clear(self, const_AsyncTaskCollection_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear(const AsyncTaskCollection self)
        
        /**
         * Removes all AsyncTasks from the collection.
         */
        """
        pass

    def findTask(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        find_task(AsyncTaskCollection self, str name)
        
        /**
         * Returns the task in the collection with the indicated name, if any, or NULL
         * if no task has that name.
         */
        """
        pass

    def find_task(self, AsyncTaskCollection_self, str_name): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        find_task(AsyncTaskCollection self, str name)
        
        /**
         * Returns the task in the collection with the indicated name, if any, or NULL
         * if no task has that name.
         */
        """
        pass

    def getNumTasks(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_tasks(AsyncTaskCollection self)
        
        /**
         * Returns the number of AsyncTasks in the collection.
         */
        """
        pass

    def getTask(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_task(AsyncTaskCollection self, int index)
        
        /**
         * Returns the nth AsyncTask in the collection.
         */
        """
        pass

    def getTasks(self, *args, **kwargs): # real signature unknown
        pass

    def get_num_tasks(self, AsyncTaskCollection_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_tasks(AsyncTaskCollection self)
        
        /**
         * Returns the number of AsyncTasks in the collection.
         */
        """
        pass

    def get_task(self, AsyncTaskCollection_self, int_index): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_task(AsyncTaskCollection self, int index)
        
        /**
         * Returns the nth AsyncTask in the collection.
         */
        """
        pass

    def get_tasks(self, *args, **kwargs): # real signature unknown
        pass

    def hasTask(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_task(AsyncTaskCollection self, AsyncTask task)
        
        /**
         * Returns true if the indicated AsyncTask appears in this collection, false
         * otherwise.
         */
        """
        pass

    def has_task(self, AsyncTaskCollection_self, AsyncTask_task): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_task(AsyncTaskCollection self, AsyncTask task)
        
        /**
         * Returns true if the indicated AsyncTask appears in this collection, false
         * otherwise.
         */
        """
        pass

    def output(self, AsyncTaskCollection_self, ostream_out): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        output(AsyncTaskCollection self, ostream out)
        
        /**
         * Writes a brief one-line description of the AsyncTaskCollection to the
         * indicated output stream.
         */
        """
        pass

    def removeDuplicateTasks(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        remove_duplicate_tasks(const AsyncTaskCollection self)
        
        /**
         * Removes any duplicate entries of the same AsyncTasks on this collection.
         * If a AsyncTask appears multiple times, the first appearance is retained;
         * subsequent appearances are removed.
         */
        """
        pass

    def removeTask(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        remove_task(const AsyncTaskCollection self, AsyncTask task)
        remove_task(const AsyncTaskCollection self, int index)
        
        /**
         * Removes the indicated AsyncTask from the collection.  Returns true if the
         * task was removed, false if it was not a member of the collection.
         */
        
        /**
         * Removes the nth AsyncTask from the collection.
         */
        """
        pass

    def removeTasksFrom(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        remove_tasks_from(const AsyncTaskCollection self, const AsyncTaskCollection other)
        
        /**
         * Removes from this collection all of the AsyncTasks listed in the other
         * collection.
         */
        """
        pass

    def remove_duplicate_tasks(self, const_AsyncTaskCollection_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        remove_duplicate_tasks(const AsyncTaskCollection self)
        
        /**
         * Removes any duplicate entries of the same AsyncTasks on this collection.
         * If a AsyncTask appears multiple times, the first appearance is retained;
         * subsequent appearances are removed.
         */
        """
        pass

    def remove_task(self, const_AsyncTaskCollection_self, AsyncTask_task): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        remove_task(const AsyncTaskCollection self, AsyncTask task)
        remove_task(const AsyncTaskCollection self, int index)
        
        /**
         * Removes the indicated AsyncTask from the collection.  Returns true if the
         * task was removed, false if it was not a member of the collection.
         */
        
        /**
         * Removes the nth AsyncTask from the collection.
         */
        """
        pass

    def remove_tasks_from(self, const_AsyncTaskCollection_self, const_AsyncTaskCollection_other): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        remove_tasks_from(const AsyncTaskCollection self, const AsyncTaskCollection other)
        
        /**
         * Removes from this collection all of the AsyncTasks listed in the other
         * collection.
         */
        """
        pass

    def write(self, AsyncTaskCollection_self, ostream_out, int_indent_level): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        write(AsyncTaskCollection self, ostream out, int indent_level)
        
        /**
         * Writes a complete multi-line description of the AsyncTaskCollection to the
         * indicated output stream.
         */
        """
        pass

    def __add__(self, *args, **kwargs): # real signature unknown
        """ Return self+value. """
        pass

    def __copy__(self, *args, **kwargs): # real signature unknown
        pass

    def __deepcopy__(self, *args, **kwargs): # real signature unknown
        pass

    def __getitem__(self, *args, **kwargs): # real signature unknown
        """ Return self[key]. """
        pass

    def __iadd__(self, *args, **kwargs): # real signature unknown
        """ Return self+=value. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __len__(self, *args, **kwargs): # real signature unknown
        """ Return len(self). """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __radd__(self, *args, **kwargs): # real signature unknown
        """ Return value+self. """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__add__': None, # (!) real value is "<slot wrapper '__add__' of 'panda3d.core.AsyncTaskCollection' objects>"
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.core.AsyncTaskCollection' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.core.AsyncTaskCollection' objects>"
        '__doc__': '/**\n * A list of tasks, for instance as returned by some of the AsyncTaskManager\n * query functions.  This also serves to define an AsyncTaskSequence.\n *\n * TODO: None of this is thread-safe yet.\n */',
        '__getitem__': None, # (!) real value is "<slot wrapper '__getitem__' of 'panda3d.core.AsyncTaskCollection' objects>"
        '__iadd__': None, # (!) real value is "<slot wrapper '__iadd__' of 'panda3d.core.AsyncTaskCollection' objects>"
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.AsyncTaskCollection' objects>"
        '__len__': None, # (!) real value is "<slot wrapper '__len__' of 'panda3d.core.AsyncTaskCollection' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE2EFC20>'
        '__radd__': None, # (!) real value is "<slot wrapper '__radd__' of 'panda3d.core.AsyncTaskCollection' objects>"
        '__repr__': None, # (!) real value is "<slot wrapper '__repr__' of 'panda3d.core.AsyncTaskCollection' objects>"
        '__str__': None, # (!) real value is "<slot wrapper '__str__' of 'panda3d.core.AsyncTaskCollection' objects>"
        'addTask': None, # (!) real value is "<method 'addTask' of 'panda3d.core.AsyncTaskCollection' objects>"
        'addTasksFrom': None, # (!) real value is "<method 'addTasksFrom' of 'panda3d.core.AsyncTaskCollection' objects>"
        'add_task': None, # (!) real value is "<method 'add_task' of 'panda3d.core.AsyncTaskCollection' objects>"
        'add_tasks_from': None, # (!) real value is "<method 'add_tasks_from' of 'panda3d.core.AsyncTaskCollection' objects>"
        'assign': None, # (!) real value is "<method 'assign' of 'panda3d.core.AsyncTaskCollection' objects>"
        'clear': None, # (!) real value is "<method 'clear' of 'panda3d.core.AsyncTaskCollection' objects>"
        'findTask': None, # (!) real value is "<method 'findTask' of 'panda3d.core.AsyncTaskCollection' objects>"
        'find_task': None, # (!) real value is "<method 'find_task' of 'panda3d.core.AsyncTaskCollection' objects>"
        'getNumTasks': None, # (!) real value is "<method 'getNumTasks' of 'panda3d.core.AsyncTaskCollection' objects>"
        'getTask': None, # (!) real value is "<method 'getTask' of 'panda3d.core.AsyncTaskCollection' objects>"
        'getTasks': None, # (!) real value is "<method 'getTasks' of 'panda3d.core.AsyncTaskCollection' objects>"
        'get_num_tasks': None, # (!) real value is "<method 'get_num_tasks' of 'panda3d.core.AsyncTaskCollection' objects>"
        'get_task': None, # (!) real value is "<method 'get_task' of 'panda3d.core.AsyncTaskCollection' objects>"
        'get_tasks': None, # (!) real value is "<method 'get_tasks' of 'panda3d.core.AsyncTaskCollection' objects>"
        'hasTask': None, # (!) real value is "<method 'hasTask' of 'panda3d.core.AsyncTaskCollection' objects>"
        'has_task': None, # (!) real value is "<method 'has_task' of 'panda3d.core.AsyncTaskCollection' objects>"
        'output': None, # (!) real value is "<method 'output' of 'panda3d.core.AsyncTaskCollection' objects>"
        'removeDuplicateTasks': None, # (!) real value is "<method 'removeDuplicateTasks' of 'panda3d.core.AsyncTaskCollection' objects>"
        'removeTask': None, # (!) real value is "<method 'removeTask' of 'panda3d.core.AsyncTaskCollection' objects>"
        'removeTasksFrom': None, # (!) real value is "<method 'removeTasksFrom' of 'panda3d.core.AsyncTaskCollection' objects>"
        'remove_duplicate_tasks': None, # (!) real value is "<method 'remove_duplicate_tasks' of 'panda3d.core.AsyncTaskCollection' objects>"
        'remove_task': None, # (!) real value is "<method 'remove_task' of 'panda3d.core.AsyncTaskCollection' objects>"
        'remove_tasks_from': None, # (!) real value is "<method 'remove_tasks_from' of 'panda3d.core.AsyncTaskCollection' objects>"
        'write': None, # (!) real value is "<method 'write' of 'panda3d.core.AsyncTaskCollection' objects>"
    }


