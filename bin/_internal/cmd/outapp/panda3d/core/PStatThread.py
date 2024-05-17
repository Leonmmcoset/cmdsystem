# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


class PStatThread(__dtoolconfig.DTOOL_SUPER_BASE):
    """
    /**
     * A lightweight class that represents a single thread of execution to PStats.
     * It corresponds one-to-one with Panda's Thread instance.
     */
    """
    def assign(self, const_PStatThread_self, const_PStatThread_copy): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        assign(const PStatThread self, const PStatThread copy)
        """
        pass

    def getIndex(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_index(PStatThread self)
        
        /**
         * Returns the index number of this particular thread within the PStatClient.
         */
        """
        pass

    def getThread(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_thread(PStatThread self)
        
        /**
         * Returns the Panda Thread object associated with this particular
         * PStatThread.
         */
        """
        pass

    def get_index(self, PStatThread_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_index(PStatThread self)
        
        /**
         * Returns the index number of this particular thread within the PStatClient.
         */
        """
        pass

    def get_thread(self, PStatThread_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_thread(PStatThread self)
        
        /**
         * Returns the Panda Thread object associated with this particular
         * PStatThread.
         */
        """
        pass

    def newFrame(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        new_frame(const PStatThread self)
        
        /**
         * This must be called at the start of every "frame", whatever a frame may be
         * deemed to be, to accumulate all the stats that have collected so far for
         * the thread and ship them off to the server.
         *
         * Calling PStatClient::thread_tick() will automatically call this for any
         * threads with the indicated sync name.
         */
        """
        pass

    def new_frame(self, const_PStatThread_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        new_frame(const PStatThread self)
        
        /**
         * This must be called at the start of every "frame", whatever a frame may be
         * deemed to be, to accumulate all the stats that have collected so far for
         * the thread and ship them off to the server.
         *
         * Calling PStatClient::thread_tick() will automatically call this for any
         * threads with the indicated sync name.
         */
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

    index = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thread = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.core.PStatThread' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.core.PStatThread' objects>"
        '__doc__': "/**\n * A lightweight class that represents a single thread of execution to PStats.\n * It corresponds one-to-one with Panda's Thread instance.\n */",
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.PStatThread' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE2C9740>'
        'assign': None, # (!) real value is "<method 'assign' of 'panda3d.core.PStatThread' objects>"
        'getIndex': None, # (!) real value is "<method 'getIndex' of 'panda3d.core.PStatThread' objects>"
        'getThread': None, # (!) real value is "<method 'getThread' of 'panda3d.core.PStatThread' objects>"
        'get_index': None, # (!) real value is "<method 'get_index' of 'panda3d.core.PStatThread' objects>"
        'get_thread': None, # (!) real value is "<method 'get_thread' of 'panda3d.core.PStatThread' objects>"
        'index': None, # (!) real value is "<attribute 'index' of 'panda3d.core.PStatThread' objects>"
        'newFrame': None, # (!) real value is "<method 'newFrame' of 'panda3d.core.PStatThread' objects>"
        'new_frame': None, # (!) real value is "<method 'new_frame' of 'panda3d.core.PStatThread' objects>"
        'thread': None, # (!) real value is "<attribute 'thread' of 'panda3d.core.PStatThread' objects>"
    }


