# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


class RecorderBase(__dtoolconfig.DTOOL_SUPER_BASE):
    """
    /**
     * This is the base class to a number of objects that record particular kinds
     * of user input (like a MouseRecorder) to use in conjunction with a
     * RecorderController to record the user's inputs for a session.
     *
     * Note that RecorderBase does not actually inherit from TypedObject, even
     * though it defines get_type().  The assumption is that the classes that
     * derive from RecorderBase might also inherit independently from TypedObject.
     *
     * It also does not inherit from TypedWritable, but it defines a method called
     * write_recorder() which is very similar to a TypedWritable's
     * write_datagram(). Classes that derive from RecorderBase and also inherit
     * from TypedWritable may choose to remap write_recorder() to do exactly the
     * same thing as write_datagram(), or they may choose to write something
     * slightly different.
     *
     * Most types of recorders should derive from Recorder, as it derives from
     * ReferenceCount, except for MouseRecorder, which would otherwise doubly
     * inherit from ReferenceCount.
     */
    """
    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def isPlaying(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_playing(RecorderBase self)
        
        /**
         * Returns true if this recorder is presently playing back data from session
         * file, false otherwise.  If this is true, play_data() will be called from
         * time to time.
         */
        """
        pass

    def isRecording(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_recording(RecorderBase self)
        
        /**
         * Returns true if this recorder is presently recording data for saving to a
         * session file, false otherwise.  If this is true, record_data() will be
         * called from time to time.
         */
        """
        pass

    def is_playing(self, RecorderBase_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_playing(RecorderBase self)
        
        /**
         * Returns true if this recorder is presently playing back data from session
         * file, false otherwise.  If this is true, play_data() will be called from
         * time to time.
         */
        """
        pass

    def is_recording(self, RecorderBase_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_recording(RecorderBase self)
        
        /**
         * Returns true if this recorder is presently recording data for saving to a
         * session file, false otherwise.  If this is true, record_data() will be
         * called from time to time.
         */
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__doc__': "/**\n * This is the base class to a number of objects that record particular kinds\n * of user input (like a MouseRecorder) to use in conjunction with a\n * RecorderController to record the user's inputs for a session.\n *\n * Note that RecorderBase does not actually inherit from TypedObject, even\n * though it defines get_type().  The assumption is that the classes that\n * derive from RecorderBase might also inherit independently from TypedObject.\n *\n * It also does not inherit from TypedWritable, but it defines a method called\n * write_recorder() which is very similar to a TypedWritable's\n * write_datagram(). Classes that derive from RecorderBase and also inherit\n * from TypedWritable may choose to remap write_recorder() to do exactly the\n * same thing as write_datagram(), or they may choose to write something\n * slightly different.\n *\n * Most types of recorders should derive from Recorder, as it derives from\n * ReferenceCount, except for MouseRecorder, which would otherwise doubly\n * inherit from ReferenceCount.\n */",
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.RecorderBase' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE284E50>'
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE284E50>)>'
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE284E50>)>'
        'isPlaying': None, # (!) real value is "<method 'isPlaying' of 'panda3d.core.RecorderBase' objects>"
        'isRecording': None, # (!) real value is "<method 'isRecording' of 'panda3d.core.RecorderBase' objects>"
        'is_playing': None, # (!) real value is "<method 'is_playing' of 'panda3d.core.RecorderBase' objects>"
        'is_recording': None, # (!) real value is "<method 'is_recording' of 'panda3d.core.RecorderBase' objects>"
    }


