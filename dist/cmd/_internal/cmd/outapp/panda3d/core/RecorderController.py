# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .TypedReferenceCount import TypedReferenceCount

class RecorderController(TypedReferenceCount):
    """
    /**
     * This object manages the process of recording the user's runtime inputs to a
     * bam file so that the session can be recreated later.
     */
    """
    def addRecorder(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_recorder(const RecorderController self, str name, RecorderBase recorder)
        
        /**
         * Adds the named recorder to the set of recorders that are in use.
         *
         * If the controller is in recording mode, the named recorder will begin
         * recording its status to the session file.  If the controller is in playback
         * mode and the name and type matches a recorder in the session file, the
         * recorder will begin receiving data.
         */
        """
        pass

    def add_recorder(self, const_RecorderController_self, str_name, RecorderBase_recorder): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_recorder(const RecorderController self, str name, RecorderBase recorder)
        
        /**
         * Adds the named recorder to the set of recorders that are in use.
         *
         * If the controller is in recording mode, the named recorder will begin
         * recording its status to the session file.  If the controller is in playback
         * mode and the name and type matches a recorder in the session file, the
         * recorder will begin receiving data.
         */
        """
        pass

    def beginPlayback(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        begin_playback(const RecorderController self, const Filename filename)
        
        /**
         * Begins playing back data from the indicated filename.  All of the recorders
         * in use should already have been added, although this may define additional
         * recorders if they are present in the file (these new recorders will not be
         * used).  This may also undefine recorders that were previously added but are
         * not present in the file.
         */
        """
        pass

    def beginRecord(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        begin_record(const RecorderController self, const Filename filename)
        
        /**
         * Begins recording data to the indicated filename.  All of the recorders in
         * use should already have been added.
         */
        """
        pass

    def begin_playback(self, const_RecorderController_self, const_Filename_filename): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        begin_playback(const RecorderController self, const Filename filename)
        
        /**
         * Begins playing back data from the indicated filename.  All of the recorders
         * in use should already have been added, although this may define additional
         * recorders if they are present in the file (these new recorders will not be
         * used).  This may also undefine recorders that were previously added but are
         * not present in the file.
         */
        """
        pass

    def begin_record(self, const_RecorderController_self, const_Filename_filename): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        begin_record(const RecorderController self, const Filename filename)
        
        /**
         * Begins recording data to the indicated filename.  All of the recorders in
         * use should already have been added.
         */
        """
        pass

    def close(self, const_RecorderController_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        close(const RecorderController self)
        
        /**
         * Finishes recording data to the indicated filename.
         */
        """
        pass

    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getClockOffset(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_clock_offset(RecorderController self)
        
        /**
         * Returns the delta offset between the actual frame time and the frame time
         * written to the log.  This is essentially the time at which the recording
         * (or playback) started.
         */
        """
        pass

    def getFilename(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_filename(RecorderController self)
        
        /**
         * Returns the filename that was passed to the most recent call to
         * begin_record() or begin_playback().
         */
        """
        pass

    def getFrameOffset(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_frame_offset(RecorderController self)
        
        /**
         * Returns the delta offset between the actual frame count and the frame count
         * written to the log.  This is essentially the frame number at which the
         * recording (or playback) started.
         */
        """
        pass

    def getFrameTie(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_frame_tie(RecorderController self)
        
        /**
         * See set_frame_tie().
         */
        """
        pass

    def getRandomSeed(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_random_seed(RecorderController self)
        
        /**
         * Returns the random seed that was set by a previous call to
         * set_random_seed(), or the number read from the session file after
         * begin_playback() has been called.
         */
        """
        pass

    def getRecorder(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_recorder(RecorderController self, str name)
        
        /**
         * Returns the recorder with the indicated name, or NULL if there is no such
         * recorder.
         *
         * If the controller is in playback mode, this may return the recorder
         * matching the indicated name as read from the session file, even if it was
         * never added to the table by the user.  In this case, has_recorder() may
         * return false, but get_recorder() will return a non-NULL value.
         */
        """
        pass

    def getStartTime(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_start_time(RecorderController self)
        
        /**
         * Returns the time (and date) at which the current session was originally
         * recorded (or, in recording mode, the time at which the current session
         * began).
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_clock_offset(self, RecorderController_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_clock_offset(RecorderController self)
        
        /**
         * Returns the delta offset between the actual frame time and the frame time
         * written to the log.  This is essentially the time at which the recording
         * (or playback) started.
         */
        """
        pass

    def get_filename(self, RecorderController_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_filename(RecorderController self)
        
        /**
         * Returns the filename that was passed to the most recent call to
         * begin_record() or begin_playback().
         */
        """
        pass

    def get_frame_offset(self, RecorderController_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_frame_offset(RecorderController self)
        
        /**
         * Returns the delta offset between the actual frame count and the frame count
         * written to the log.  This is essentially the frame number at which the
         * recording (or playback) started.
         */
        """
        pass

    def get_frame_tie(self, RecorderController_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_frame_tie(RecorderController self)
        
        /**
         * See set_frame_tie().
         */
        """
        pass

    def get_random_seed(self, RecorderController_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_random_seed(RecorderController self)
        
        /**
         * Returns the random seed that was set by a previous call to
         * set_random_seed(), or the number read from the session file after
         * begin_playback() has been called.
         */
        """
        pass

    def get_recorder(self, RecorderController_self, str_name): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_recorder(RecorderController self, str name)
        
        /**
         * Returns the recorder with the indicated name, or NULL if there is no such
         * recorder.
         *
         * If the controller is in playback mode, this may return the recorder
         * matching the indicated name as read from the session file, even if it was
         * never added to the table by the user.  In this case, has_recorder() may
         * return false, but get_recorder() will return a non-NULL value.
         */
        """
        pass

    def get_start_time(self, RecorderController_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_start_time(RecorderController self)
        
        /**
         * Returns the time (and date) at which the current session was originally
         * recorded (or, in recording mode, the time at which the current session
         * began).
         */
        """
        pass

    def hasRecorder(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_recorder(RecorderController self, str name)
        
        /**
         * Returns true if the named recorder has been added to the table by a
         * previous call to add_recorder(), false otherwise.
         *
         * If the controller is in playback mode, this will also return false for a
         * recorder that was found in the session file but was never explicitly added
         * via add_recorder(); see get_recorder().
         */
        """
        pass

    def has_recorder(self, RecorderController_self, str_name): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_recorder(RecorderController self, str name)
        
        /**
         * Returns true if the named recorder has been added to the table by a
         * previous call to add_recorder(), false otherwise.
         *
         * If the controller is in playback mode, this will also return false for a
         * recorder that was found in the session file but was never explicitly added
         * via add_recorder(); see get_recorder().
         */
        """
        pass

    def isError(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_error(const RecorderController self)
        
        /**
         * Returns true if the controller has been opened for input or output output
         * and there is an error on the stream, or false if the controller is closed
         * or if there is no problem.
         */
        """
        pass

    def isOpen(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_open(RecorderController self)
        
        /**
         * Returns true if the controller has been opened for either input or output,
         * false otherwise.
         */
        """
        pass

    def isPlaying(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_playing(RecorderController self)
        
        /**
         * Returns true if the controller has been opened for input, false otherwise.
         */
        """
        pass

    def isRecording(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_recording(RecorderController self)
        
        /**
         * Returns true if the controller has been opened for output, false otherwise.
         */
        """
        pass

    def is_error(self, const_RecorderController_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_error(const RecorderController self)
        
        /**
         * Returns true if the controller has been opened for input or output output
         * and there is an error on the stream, or false if the controller is closed
         * or if there is no problem.
         */
        """
        pass

    def is_open(self, RecorderController_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_open(RecorderController self)
        
        /**
         * Returns true if the controller has been opened for either input or output,
         * false otherwise.
         */
        """
        pass

    def is_playing(self, RecorderController_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_playing(RecorderController self)
        
        /**
         * Returns true if the controller has been opened for input, false otherwise.
         */
        """
        pass

    def is_recording(self, RecorderController_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_recording(RecorderController self)
        
        /**
         * Returns true if the controller has been opened for output, false otherwise.
         */
        """
        pass

    def playFrame(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        play_frame(const RecorderController self)
        
        /**
         * Gets the next frame of data from all of the active recorders and adds it to
         * the output file.
         */
        """
        pass

    def play_frame(self, const_RecorderController_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        play_frame(const RecorderController self)
        
        /**
         * Gets the next frame of data from all of the active recorders and adds it to
         * the output file.
         */
        """
        pass

    def recordFrame(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        record_frame(const RecorderController self)
        
        /**
         * Gets the next frame of data from all of the active recorders and adds it to
         * the output file.
         */
        """
        pass

    def record_frame(self, const_RecorderController_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        record_frame(const RecorderController self)
        
        /**
         * Gets the next frame of data from all of the active recorders and adds it to
         * the output file.
         */
        """
        pass

    def removeRecorder(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        remove_recorder(const RecorderController self, str name)
        
        /**
         * Removes the named recorder from the table.  Returns true if successful,
         * false if there was no such recorder.
         *
         * If the controller is in recording mode, the named recorder will stop
         * recording.  If the controller is in playback mode, the named recorder will
         * disassociate itself from the session file (but if the session file still
         * has data for this name, a default recorder will take its place to decode
         * the data from the session file).
         */
        """
        pass

    def remove_recorder(self, const_RecorderController_self, str_name): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        remove_recorder(const RecorderController self, str name)
        
        /**
         * Removes the named recorder from the table.  Returns true if successful,
         * false if there was no such recorder.
         *
         * If the controller is in recording mode, the named recorder will stop
         * recording.  If the controller is in playback mode, the named recorder will
         * disassociate itself from the session file (but if the session file still
         * has data for this name, a default recorder will take its place to decode
         * the data from the session file).
         */
        """
        pass

    def setFrameTie(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_frame_tie(const RecorderController self, bool frame_tie)
        
        /**
         * Sets the frame_tie flag.
         *
         * When this is true, sessions are played back frame-for-frame, based on the
         * frame count of the recorded session.  This gives the most accurate
         * playback, but the playback rate will vary according to the frame rate of
         * the playback machine.
         *
         * When this is false, sessions are played back at real time, based on the
         * clock of the recorded session.  This may introduce playback discrepencies
         * if the frames do not fall at exactly the same times as they did in the
         * original.
         */
        """
        pass

    def setRandomSeed(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_random_seed(const RecorderController self, int random_seed)
        
        /**
         * Indicates an arbitrary number to be recorded in the session file as a
         * random seed, should the application wish to take advantage of it.  This
         * must be set before begin_record() is called.
         */
        """
        pass

    def set_frame_tie(self, const_RecorderController_self, bool_frame_tie): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_frame_tie(const RecorderController self, bool frame_tie)
        
        /**
         * Sets the frame_tie flag.
         *
         * When this is true, sessions are played back frame-for-frame, based on the
         * frame count of the recorded session.  This gives the most accurate
         * playback, but the playback rate will vary according to the frame rate of
         * the playback machine.
         *
         * When this is false, sessions are played back at real time, based on the
         * clock of the recorded session.  This may introduce playback discrepencies
         * if the frames do not fall at exactly the same times as they did in the
         * original.
         */
        """
        pass

    def set_random_seed(self, const_RecorderController_self, int_random_seed): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_random_seed(const RecorderController self, int random_seed)
        
        /**
         * Indicates an arbitrary number to be recorded in the session file as a
         * random seed, should the application wish to take advantage of it.  This
         * must be set before begin_record() is called.
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
        '__doc__': "/**\n * This object manages the process of recording the user's runtime inputs to a\n * bam file so that the session can be recreated later.\n */",
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.RecorderController' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE2851F0>'
        'addRecorder': None, # (!) real value is "<method 'addRecorder' of 'panda3d.core.RecorderController' objects>"
        'add_recorder': None, # (!) real value is "<method 'add_recorder' of 'panda3d.core.RecorderController' objects>"
        'beginPlayback': None, # (!) real value is "<method 'beginPlayback' of 'panda3d.core.RecorderController' objects>"
        'beginRecord': None, # (!) real value is "<method 'beginRecord' of 'panda3d.core.RecorderController' objects>"
        'begin_playback': None, # (!) real value is "<method 'begin_playback' of 'panda3d.core.RecorderController' objects>"
        'begin_record': None, # (!) real value is "<method 'begin_record' of 'panda3d.core.RecorderController' objects>"
        'close': None, # (!) real value is "<method 'close' of 'panda3d.core.RecorderController' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE2851F0>)>'
        'getClockOffset': None, # (!) real value is "<method 'getClockOffset' of 'panda3d.core.RecorderController' objects>"
        'getFilename': None, # (!) real value is "<method 'getFilename' of 'panda3d.core.RecorderController' objects>"
        'getFrameOffset': None, # (!) real value is "<method 'getFrameOffset' of 'panda3d.core.RecorderController' objects>"
        'getFrameTie': None, # (!) real value is "<method 'getFrameTie' of 'panda3d.core.RecorderController' objects>"
        'getRandomSeed': None, # (!) real value is "<method 'getRandomSeed' of 'panda3d.core.RecorderController' objects>"
        'getRecorder': None, # (!) real value is "<method 'getRecorder' of 'panda3d.core.RecorderController' objects>"
        'getStartTime': None, # (!) real value is "<method 'getStartTime' of 'panda3d.core.RecorderController' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE2851F0>)>'
        'get_clock_offset': None, # (!) real value is "<method 'get_clock_offset' of 'panda3d.core.RecorderController' objects>"
        'get_filename': None, # (!) real value is "<method 'get_filename' of 'panda3d.core.RecorderController' objects>"
        'get_frame_offset': None, # (!) real value is "<method 'get_frame_offset' of 'panda3d.core.RecorderController' objects>"
        'get_frame_tie': None, # (!) real value is "<method 'get_frame_tie' of 'panda3d.core.RecorderController' objects>"
        'get_random_seed': None, # (!) real value is "<method 'get_random_seed' of 'panda3d.core.RecorderController' objects>"
        'get_recorder': None, # (!) real value is "<method 'get_recorder' of 'panda3d.core.RecorderController' objects>"
        'get_start_time': None, # (!) real value is "<method 'get_start_time' of 'panda3d.core.RecorderController' objects>"
        'hasRecorder': None, # (!) real value is "<method 'hasRecorder' of 'panda3d.core.RecorderController' objects>"
        'has_recorder': None, # (!) real value is "<method 'has_recorder' of 'panda3d.core.RecorderController' objects>"
        'isError': None, # (!) real value is "<method 'isError' of 'panda3d.core.RecorderController' objects>"
        'isOpen': None, # (!) real value is "<method 'isOpen' of 'panda3d.core.RecorderController' objects>"
        'isPlaying': None, # (!) real value is "<method 'isPlaying' of 'panda3d.core.RecorderController' objects>"
        'isRecording': None, # (!) real value is "<method 'isRecording' of 'panda3d.core.RecorderController' objects>"
        'is_error': None, # (!) real value is "<method 'is_error' of 'panda3d.core.RecorderController' objects>"
        'is_open': None, # (!) real value is "<method 'is_open' of 'panda3d.core.RecorderController' objects>"
        'is_playing': None, # (!) real value is "<method 'is_playing' of 'panda3d.core.RecorderController' objects>"
        'is_recording': None, # (!) real value is "<method 'is_recording' of 'panda3d.core.RecorderController' objects>"
        'playFrame': None, # (!) real value is "<method 'playFrame' of 'panda3d.core.RecorderController' objects>"
        'play_frame': None, # (!) real value is "<method 'play_frame' of 'panda3d.core.RecorderController' objects>"
        'recordFrame': None, # (!) real value is "<method 'recordFrame' of 'panda3d.core.RecorderController' objects>"
        'record_frame': None, # (!) real value is "<method 'record_frame' of 'panda3d.core.RecorderController' objects>"
        'removeRecorder': None, # (!) real value is "<method 'removeRecorder' of 'panda3d.core.RecorderController' objects>"
        'remove_recorder': None, # (!) real value is "<method 'remove_recorder' of 'panda3d.core.RecorderController' objects>"
        'setFrameTie': None, # (!) real value is "<method 'setFrameTie' of 'panda3d.core.RecorderController' objects>"
        'setRandomSeed': None, # (!) real value is "<method 'setRandomSeed' of 'panda3d.core.RecorderController' objects>"
        'set_frame_tie': None, # (!) real value is "<method 'set_frame_tie' of 'panda3d.core.RecorderController' objects>"
        'set_random_seed': None, # (!) real value is "<method 'set_random_seed' of 'panda3d.core.RecorderController' objects>"
    }


