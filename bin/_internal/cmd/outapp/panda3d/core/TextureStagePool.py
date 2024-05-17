# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


class TextureStagePool(__dtoolconfig.DTOOL_SUPER_BASE):
    """
    /**
     * The TextureStagePool (there is only one in the universe) serves to unify
     * different pointers to the same TextureStage, mainly to help developers use
     * a common pointer to access things that are loaded from different model
     * files.
     *
     * It runs in one of three different modes, according to set_mode().  See that
     * method for more information.
     */
    """
    def garbageCollect(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        garbage_collect()
        
        /**
         * Releases only those TextureStages in the pool that have a reference count
         * of exactly 1; i.e.  only those TextureStages that are not being used
         * outside of the pool.  Returns the number of TextureStages released.
         */
        """
        pass

    def garbage_collect(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        garbage_collect()
        
        /**
         * Releases only those TextureStages in the pool that have a reference count
         * of exactly 1; i.e.  only those TextureStages that are not being used
         * outside of the pool.  Returns the number of TextureStages released.
         */
        """
        pass

    def getMode(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_mode()
        
        /**
         * Returns the fundamental operating mode of the TextureStagePool.  See
         * set_mode().
         */
        """
        pass

    def getStage(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_stage(TextureStage temp)
        
        /**
         * Returns a TextureStage pointer that represents the same TextureStage
         * described by temp, except that it is a shared pointer.
         *
         * Each call to get_stage() passing an equivalent TextureStage pointer will
         * return the same shared pointer.
         *
         * If you modify the shared pointer, it will automatically disassociate it
         * from the pool.
         *
         * Also, the return value may be a different pointer than that passed in, or
         * it may be the same pointer.  In either case, the passed in pointer has now
         * been sacrificed to the greater good and should not be used again (like any
         * other PointerTo, it will be freed when the last reference count is
         * removed).
         */
        """
        pass

    def get_mode(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_mode()
        
        /**
         * Returns the fundamental operating mode of the TextureStagePool.  See
         * set_mode().
         */
        """
        pass

    def get_stage(self, TextureStage_temp): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_stage(TextureStage temp)
        
        /**
         * Returns a TextureStage pointer that represents the same TextureStage
         * described by temp, except that it is a shared pointer.
         *
         * Each call to get_stage() passing an equivalent TextureStage pointer will
         * return the same shared pointer.
         *
         * If you modify the shared pointer, it will automatically disassociate it
         * from the pool.
         *
         * Also, the return value may be a different pointer than that passed in, or
         * it may be the same pointer.  In either case, the passed in pointer has now
         * been sacrificed to the greater good and should not be used again (like any
         * other PointerTo, it will be freed when the last reference count is
         * removed).
         */
        """
        pass

    def listContents(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        list_contents(ostream out)
        
        /**
         * Lists the contents of the TextureStage pool to the indicated output stream.
         */
        """
        pass

    def list_contents(self, ostream_out): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        list_contents(ostream out)
        
        /**
         * Lists the contents of the TextureStage pool to the indicated output stream.
         */
        """
        pass

    def releaseAllStages(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        release_all_stages()
        
        /**
         * Releases all TextureStages in the pool and restores the pool to the empty
         * state.
         */
        """
        pass

    def releaseStage(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        release_stage(TextureStage temp)
        
        /**
         * Removes the indicated TextureStage from the pool.
         */
        """
        pass

    def release_all_stages(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        release_all_stages()
        
        /**
         * Releases all TextureStages in the pool and restores the pool to the empty
         * state.
         */
        """
        pass

    def release_stage(self, TextureStage_temp): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        release_stage(TextureStage temp)
        
        /**
         * Removes the indicated TextureStage from the pool.
         */
        """
        pass

    def setMode(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_mode(int mode)
        
        /**
         * Specifies the fundamental operating mode of the TextureStagePool.
         *
         * If this is M_none, each call to get_stage() returns the same TextureStage
         * pointer that was passed in (the pool is effectively disabled).  If this is
         * M_name, each call to get_stage() returns the last TextureStage passed in
         * with the same name, whether it has different properties or not.  If this is
         * M_unique, then each call to get_stage() returns only TextureStages with
         * identical properties.
         */
        """
        pass

    def set_mode(self, int_mode): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_mode(int mode)
        
        /**
         * Specifies the fundamental operating mode of the TextureStagePool.
         *
         * If this is M_none, each call to get_stage() returns the same TextureStage
         * pointer that was passed in (the pool is effectively disabled).  If this is
         * M_name, each call to get_stage() returns the last TextureStage passed in
         * with the same name, whether it has different properties or not.  If this is
         * M_unique, then each call to get_stage() returns only TextureStages with
         * identical properties.
         */
        """
        pass

    def write(self, ostream_out): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        write(ostream out)
        
        /**
         * Lists the contents of the TextureStage pool to the indicated output stream.
         */
        """
        pass

    def __init__(self, there_is_only_one_in_the_universe): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        'MName': 1,
        'MNone': 0,
        'MUnique': 2,
        'M_name': 1,
        'M_none': 0,
        'M_unique': 2,
        '__doc__': '/**\n * The TextureStagePool (there is only one in the universe) serves to unify\n * different pointers to the same TextureStage, mainly to help developers use\n * a common pointer to access things that are loaded from different model\n * files.\n *\n * It runs in one of three different modes, according to set_mode().  See that\n * method for more information.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.TextureStagePool' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE3016F0>'
        '__str__': None, # (!) real value is "<slot wrapper '__str__' of 'panda3d.core.TextureStagePool' objects>"
        'garbageCollect': None, # (!) real value is '<staticmethod(<built-in method garbageCollect of type object at 0x00007FFCFE3016F0>)>'
        'garbage_collect': None, # (!) real value is '<staticmethod(<built-in method garbage_collect of type object at 0x00007FFCFE3016F0>)>'
        'getMode': None, # (!) real value is '<staticmethod(<built-in method getMode of type object at 0x00007FFCFE3016F0>)>'
        'getStage': None, # (!) real value is '<staticmethod(<built-in method getStage of type object at 0x00007FFCFE3016F0>)>'
        'get_mode': None, # (!) real value is '<staticmethod(<built-in method get_mode of type object at 0x00007FFCFE3016F0>)>'
        'get_stage': None, # (!) real value is '<staticmethod(<built-in method get_stage of type object at 0x00007FFCFE3016F0>)>'
        'listContents': None, # (!) real value is '<staticmethod(<built-in method listContents of type object at 0x00007FFCFE3016F0>)>'
        'list_contents': None, # (!) real value is '<staticmethod(<built-in method list_contents of type object at 0x00007FFCFE3016F0>)>'
        'mode': None, # (!) real value is "<attribute 'mode' of 'panda3d.core.TextureStagePool'>"
        'releaseAllStages': None, # (!) real value is '<staticmethod(<built-in method releaseAllStages of type object at 0x00007FFCFE3016F0>)>'
        'releaseStage': None, # (!) real value is '<staticmethod(<built-in method releaseStage of type object at 0x00007FFCFE3016F0>)>'
        'release_all_stages': None, # (!) real value is '<staticmethod(<built-in method release_all_stages of type object at 0x00007FFCFE3016F0>)>'
        'release_stage': None, # (!) real value is '<staticmethod(<built-in method release_stage of type object at 0x00007FFCFE3016F0>)>'
        'setMode': None, # (!) real value is '<staticmethod(<built-in method setMode of type object at 0x00007FFCFE3016F0>)>'
        'set_mode': None, # (!) real value is '<staticmethod(<built-in method set_mode of type object at 0x00007FFCFE3016F0>)>'
        'write': None, # (!) real value is '<staticmethod(<built-in method write of type object at 0x00007FFCFE3016F0>)>'
    }
    MName = 1
    MNone = 0
    mode = 0
    MUnique = 2
    M_name = 1
    M_none = 0
    M_unique = 2


