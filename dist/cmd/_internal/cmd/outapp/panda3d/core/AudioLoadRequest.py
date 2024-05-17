# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .AsyncTask import AsyncTask

class AudioLoadRequest(AsyncTask):
    """
    /**
     * A class object that manages a single asynchronous audio load request.  This
     * works in conjunction with the Loader class defined in pgraph, or really
     * with any AsyncTaskManager.  Create a new AudioLoadRequest, and add it to
     * the loader via load_async(), to begin an asynchronous load.
     */
    """
    def getAudioManager(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_audio_manager(AudioLoadRequest self)
        
        /**
         * Returns the AudioManager that will serve this asynchronous
         * AudioLoadRequest.
         */
        """
        pass

    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getFilename(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_filename(AudioLoadRequest self)
        
        /**
         * Returns the filename associated with this asynchronous AudioLoadRequest.
         */
        """
        pass

    def getPositional(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_positional(AudioLoadRequest self)
        
        /**
         * Returns the positional flag associated with this asynchronous
         * AudioLoadRequest.
         */
        """
        pass

    def getSound(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_sound(AudioLoadRequest self)
        
        /**
         * Returns the sound that was loaded asynchronously, if any, or nullptr if
         * there was an error.  It is an error to call this unless done() returns
         * true.
         * @deprecated Use result() instead.
         */
        """
        pass

    def get_audio_manager(self, AudioLoadRequest_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_audio_manager(AudioLoadRequest self)
        
        /**
         * Returns the AudioManager that will serve this asynchronous
         * AudioLoadRequest.
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_filename(self, AudioLoadRequest_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_filename(AudioLoadRequest self)
        
        /**
         * Returns the filename associated with this asynchronous AudioLoadRequest.
         */
        """
        pass

    def get_positional(self, AudioLoadRequest_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_positional(AudioLoadRequest self)
        
        /**
         * Returns the positional flag associated with this asynchronous
         * AudioLoadRequest.
         */
        """
        pass

    def get_sound(self, AudioLoadRequest_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_sound(AudioLoadRequest self)
        
        /**
         * Returns the sound that was loaded asynchronously, if any, or nullptr if
         * there was an error.  It is an error to call this unless done() returns
         * true.
         * @deprecated Use result() instead.
         */
        """
        pass

    def isReady(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_ready(AudioLoadRequest self)
        
        /**
         * Returns true if this request has completed, false if it is still pending.
         * When this returns true, you may retrieve the sound loaded by calling
         * get_sound().
         * Equivalent to `req.done() and not req.cancelled()`.
         * @see done()
         */
        """
        pass

    def is_ready(self, AudioLoadRequest_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_ready(AudioLoadRequest self)
        
        /**
         * Returns true if this request has completed, false if it is still pending.
         * When this returns true, you may retrieve the sound loaded by calling
         * get_sound().
         * Equivalent to `req.done() and not req.cancelled()`.
         * @see done()
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

    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.core.AudioLoadRequest' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.core.AudioLoadRequest' objects>"
        '__doc__': '/**\n * A class object that manages a single asynchronous audio load request.  This\n * works in conjunction with the Loader class defined in pgraph, or really\n * with any AsyncTaskManager.  Create a new AudioLoadRequest, and add it to\n * the loader via load_async(), to begin an asynchronous load.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.AudioLoadRequest' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE381A00>'
        'getAudioManager': None, # (!) real value is "<method 'getAudioManager' of 'panda3d.core.AudioLoadRequest' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE381A00>)>'
        'getFilename': None, # (!) real value is "<method 'getFilename' of 'panda3d.core.AudioLoadRequest' objects>"
        'getPositional': None, # (!) real value is "<method 'getPositional' of 'panda3d.core.AudioLoadRequest' objects>"
        'getSound': None, # (!) real value is "<method 'getSound' of 'panda3d.core.AudioLoadRequest' objects>"
        'get_audio_manager': None, # (!) real value is "<method 'get_audio_manager' of 'panda3d.core.AudioLoadRequest' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE381A00>)>'
        'get_filename': None, # (!) real value is "<method 'get_filename' of 'panda3d.core.AudioLoadRequest' objects>"
        'get_positional': None, # (!) real value is "<method 'get_positional' of 'panda3d.core.AudioLoadRequest' objects>"
        'get_sound': None, # (!) real value is "<method 'get_sound' of 'panda3d.core.AudioLoadRequest' objects>"
        'isReady': None, # (!) real value is "<method 'isReady' of 'panda3d.core.AudioLoadRequest' objects>"
        'is_ready': None, # (!) real value is "<method 'is_ready' of 'panda3d.core.AudioLoadRequest' objects>"
    }


