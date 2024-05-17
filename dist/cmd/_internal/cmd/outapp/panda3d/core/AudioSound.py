# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .TypedReferenceCount import TypedReferenceCount

class AudioSound(TypedReferenceCount):
    # no doc
    def configureFilters(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        configure_filters(const AudioSound self, FilterProperties config)
        """
        pass

    def configure_filters(self, const_AudioSound_self, FilterProperties_config): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        configure_filters(const AudioSound self, FilterProperties config)
        """
        pass

    def get3dMaxDistance(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_3d_max_distance(AudioSound self)
        """
        pass

    def get3dMinDistance(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_3d_min_distance(AudioSound self)
        """
        pass

    def getActive(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_active(AudioSound self)
        """
        pass

    def getBalance(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_balance(AudioSound self)
        """
        pass

    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getFinishedEvent(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_finished_event(AudioSound self)
        """
        pass

    def getLoop(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_loop(AudioSound self)
        """
        pass

    def getLoopCount(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_loop_count(AudioSound self)
        """
        pass

    def getName(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_name(AudioSound self)
        
        // There is no set_name(), this is intentional.
        """
        pass

    def getPlayRate(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_play_rate(AudioSound self)
        """
        pass

    def getPriority(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_priority(const AudioSound self)
        """
        pass

    def getSpeakerLevel(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_speaker_level(const AudioSound self, int index)
        """
        pass

    def getSpeakerMix(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_speaker_mix(const AudioSound self, int speaker)
        
        // speaker_mix and speaker_level(s) serve the same purpose.
        // speaker_mix is for use with FMOD. speaker_level(s) is for use with
        // Miles.  Both interfaces exist because of a significant difference in the
        // two APIs.  Hopefully the difference can be reconciled into a single
        // interface at some point.
        """
        pass

    def getTime(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_time(AudioSound self)
        """
        pass

    def getVolume(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_volume(AudioSound self)
        """
        pass

    def get_3d_max_distance(self, AudioSound_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_3d_max_distance(AudioSound self)
        """
        pass

    def get_3d_min_distance(self, AudioSound_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_3d_min_distance(AudioSound self)
        """
        pass

    def get_active(self, AudioSound_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_active(AudioSound self)
        """
        pass

    def get_balance(self, AudioSound_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_balance(AudioSound self)
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_finished_event(self, AudioSound_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_finished_event(AudioSound self)
        """
        pass

    def get_loop(self, AudioSound_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_loop(AudioSound self)
        """
        pass

    def get_loop_count(self, AudioSound_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_loop_count(AudioSound self)
        """
        pass

    def get_name(self, AudioSound_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_name(AudioSound self)
        
        // There is no set_name(), this is intentional.
        """
        pass

    def get_play_rate(self, AudioSound_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_play_rate(AudioSound self)
        """
        pass

    def get_priority(self, const_AudioSound_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_priority(const AudioSound self)
        """
        pass

    def get_speaker_level(self, const_AudioSound_self, int_index): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_speaker_level(const AudioSound self, int index)
        """
        pass

    def get_speaker_mix(self, const_AudioSound_self, int_speaker): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_speaker_mix(const AudioSound self, int speaker)
        
        // speaker_mix and speaker_level(s) serve the same purpose.
        // speaker_mix is for use with FMOD. speaker_level(s) is for use with
        // Miles.  Both interfaces exist because of a significant difference in the
        // two APIs.  Hopefully the difference can be reconciled into a single
        // interface at some point.
        """
        pass

    def get_time(self, AudioSound_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_time(AudioSound self)
        """
        pass

    def get_volume(self, AudioSound_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_volume(AudioSound self)
        """
        pass

    def length(self, AudioSound_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        length(AudioSound self)
        
        // return: playing time in seconds.
        """
        pass

    def output(self, AudioSound_self, ostream_out): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        output(AudioSound self, ostream out)
        """
        pass

    def play(self, const_AudioSound_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        play(const AudioSound self)
        
        // For best compatibility, set the loop_count, volume, and balance, prior to
        // calling play().  You may set them while they're playing, but it's
        // implementation specific whether you get the results.  - Calling play() a
        // second time on the same sound before it is finished will start the sound
        // again (creating a skipping or stuttering effect).
        """
        pass

    def set3dAttributes(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_3d_attributes(const AudioSound self, float px, float py, float pz, float vx, float vy, float vz)
        
        // Controls the position of this sound's emitter.  px, py and pz are the
        // emitter's position.  vx, vy and vz are the emitter's velocity in UNITS
        // PER SECOND (default: meters).
        """
        pass

    def set3dMaxDistance(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_3d_max_distance(const AudioSound self, float dist)
        
        // Controls the maximum distance (in units) that this sound stops falling
        // off.  The sound does not stop at that point, it just doesn't get any
        // quieter.  You should rarely need to adjust this.  Default is 1000000000.0
        """
        pass

    def set3dMinDistance(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_3d_min_distance(const AudioSound self, float dist)
        
        // Controls the distance (in units) that this sound begins to fall off.
        // Also affects the rate it falls off.  Default is 1.0 CloserFaster, <1.0
        // FartherSlower, >1.0
        """
        pass

    def setActive(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_active(const AudioSound self, bool flag)
        
        // inits to manager's state.
        """
        pass

    def setBalance(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_balance(const AudioSound self, float balance_right)
        
        // -1.0 is hard left 0.0 is centered 1.0 is hard right inits to 0.0.
        """
        pass

    def setFinishedEvent(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_finished_event(const AudioSound self, str event)
        
        // Set (or clear) the event that will be thrown when the sound finishes
        // playing.  To clear the event, pass an empty string.
        """
        pass

    def setLoop(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_loop(const AudioSound self, bool loop)
        
        // loop: false = play once; true = play forever.  inits to false.
        """
        pass

    def setLoopCount(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_loop_count(const AudioSound self, int loop_count)
        
        // loop_count: 0 = forever; 1 = play once; n = play n times.  inits to 1.
        """
        pass

    def setPlayRate(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_play_rate(const AudioSound self, float play_rate)
        
        // play_rate is any positive PN_stdfloat value.  inits to 1.0.
        """
        pass

    def setPriority(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_priority(const AudioSound self, int priority)
        """
        pass

    def setSpeakerLevels(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_speaker_levels(const AudioSound self, float level1, float level2, float level3, float level4, float level5, float level6, float level7, float level8, float level9)
        """
        pass

    def setSpeakerMix(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_speaker_mix(const AudioSound self, float frontleft, float frontright, float center, float sub, float backleft, float backright, float sideleft, float sideright)
        """
        pass

    def setTime(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_time(const AudioSound self, float start_time)
        
        /**
           * Control time position within the sound, in seconds.  This is similar (in
           * concept) to the seek position within a file.  The value starts at 0.0 (the
           * default) and ends at the value given by the length() method.
           *
           * The current time position will not change while the sound is playing; you
           * must call play() again to effect the change.  To play the same sound from
           * a time offset a second time, explicitly set the time position again.  When
           * looping, the second and later loops will start from the beginning of the
           * sound.
           *
           * If a sound is playing, calling get_time() repeatedly will return different
           * results over time.  e.g.
           * @code
           * PN_stdfloat percent_complete = s.get_time() / s.length();
           * @endcode
           */
        """
        pass

    def setVolume(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_volume(const AudioSound self, float volume)
        
        // 0 = minimum; 1.0 = maximum.  inits to 1.0.
        """
        pass

    def set_3d_attributes(self, const_AudioSound_self, float_px, float_py, float_pz, float_vx, float_vy, float_vz): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_3d_attributes(const AudioSound self, float px, float py, float pz, float vx, float vy, float vz)
        
        // Controls the position of this sound's emitter.  px, py and pz are the
        // emitter's position.  vx, vy and vz are the emitter's velocity in UNITS
        // PER SECOND (default: meters).
        """
        pass

    def set_3d_max_distance(self, const_AudioSound_self, float_dist): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_3d_max_distance(const AudioSound self, float dist)
        
        // Controls the maximum distance (in units) that this sound stops falling
        // off.  The sound does not stop at that point, it just doesn't get any
        // quieter.  You should rarely need to adjust this.  Default is 1000000000.0
        """
        pass

    def set_3d_min_distance(self, const_AudioSound_self, float_dist): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_3d_min_distance(const AudioSound self, float dist)
        
        // Controls the distance (in units) that this sound begins to fall off.
        // Also affects the rate it falls off.  Default is 1.0 CloserFaster, <1.0
        // FartherSlower, >1.0
        """
        pass

    def set_active(self, const_AudioSound_self, bool_flag): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_active(const AudioSound self, bool flag)
        
        // inits to manager's state.
        """
        pass

    def set_balance(self, const_AudioSound_self, float_balance_right): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_balance(const AudioSound self, float balance_right)
        
        // -1.0 is hard left 0.0 is centered 1.0 is hard right inits to 0.0.
        """
        pass

    def set_finished_event(self, const_AudioSound_self, str_event): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_finished_event(const AudioSound self, str event)
        
        // Set (or clear) the event that will be thrown when the sound finishes
        // playing.  To clear the event, pass an empty string.
        """
        pass

    def set_loop(self, const_AudioSound_self, bool_loop): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_loop(const AudioSound self, bool loop)
        
        // loop: false = play once; true = play forever.  inits to false.
        """
        pass

    def set_loop_count(self, const_AudioSound_self, int_loop_count): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_loop_count(const AudioSound self, int loop_count)
        
        // loop_count: 0 = forever; 1 = play once; n = play n times.  inits to 1.
        """
        pass

    def set_play_rate(self, const_AudioSound_self, float_play_rate): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_play_rate(const AudioSound self, float play_rate)
        
        // play_rate is any positive PN_stdfloat value.  inits to 1.0.
        """
        pass

    def set_priority(self, const_AudioSound_self, int_priority): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_priority(const AudioSound self, int priority)
        """
        pass

    def set_speaker_levels(self, const_AudioSound_self, float_level1, float_level2, float_level3, float_level4, float_level5, float_level6, float_level7, float_level8, float_level9): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_speaker_levels(const AudioSound self, float level1, float level2, float level3, float level4, float level5, float level6, float level7, float level8, float level9)
        """
        pass

    def set_speaker_mix(self, const_AudioSound_self, float_frontleft, float_frontright, float_center, float_sub, float_backleft, float_backright, float_sideleft, float_sideright): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_speaker_mix(const AudioSound self, float frontleft, float frontright, float center, float sub, float backleft, float backright, float sideleft, float sideright)
        """
        pass

    def set_time(self, const_AudioSound_self, float_start_time): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_time(const AudioSound self, float start_time)
        
        /**
           * Control time position within the sound, in seconds.  This is similar (in
           * concept) to the seek position within a file.  The value starts at 0.0 (the
           * default) and ends at the value given by the length() method.
           *
           * The current time position will not change while the sound is playing; you
           * must call play() again to effect the change.  To play the same sound from
           * a time offset a second time, explicitly set the time position again.  When
           * looping, the second and later loops will start from the beginning of the
           * sound.
           *
           * If a sound is playing, calling get_time() repeatedly will return different
           * results over time.  e.g.
           * @code
           * PN_stdfloat percent_complete = s.get_time() / s.length();
           * @endcode
           */
        """
        pass

    def set_volume(self, const_AudioSound_self, float_volume): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_volume(const AudioSound self, float volume)
        
        // 0 = minimum; 1.0 = maximum.  inits to 1.0.
        """
        pass

    def status(self, AudioSound_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        status(AudioSound self)
        """
        pass

    def stop(self, const_AudioSound_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        stop(const AudioSound self)
        """
        pass

    def write(self, AudioSound_self, ostream_out): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        write(AudioSound self, ostream out)
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

    BAD = 0
    DtoolClassDict = {
        'BAD': 0,
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        'PLAYING': 2,
        'READY': 1,
        '__doc__': None,
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.AudioSound' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE381660>'
        '__repr__': None, # (!) real value is "<slot wrapper '__repr__' of 'panda3d.core.AudioSound' objects>"
        '__str__': None, # (!) real value is "<slot wrapper '__str__' of 'panda3d.core.AudioSound' objects>"
        'configureFilters': None, # (!) real value is "<method 'configureFilters' of 'panda3d.core.AudioSound' objects>"
        'configure_filters': None, # (!) real value is "<method 'configure_filters' of 'panda3d.core.AudioSound' objects>"
        'get3dMaxDistance': None, # (!) real value is "<method 'get3dMaxDistance' of 'panda3d.core.AudioSound' objects>"
        'get3dMinDistance': None, # (!) real value is "<method 'get3dMinDistance' of 'panda3d.core.AudioSound' objects>"
        'getActive': None, # (!) real value is "<method 'getActive' of 'panda3d.core.AudioSound' objects>"
        'getBalance': None, # (!) real value is "<method 'getBalance' of 'panda3d.core.AudioSound' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE381660>)>'
        'getFinishedEvent': None, # (!) real value is "<method 'getFinishedEvent' of 'panda3d.core.AudioSound' objects>"
        'getLoop': None, # (!) real value is "<method 'getLoop' of 'panda3d.core.AudioSound' objects>"
        'getLoopCount': None, # (!) real value is "<method 'getLoopCount' of 'panda3d.core.AudioSound' objects>"
        'getName': None, # (!) real value is "<method 'getName' of 'panda3d.core.AudioSound' objects>"
        'getPlayRate': None, # (!) real value is "<method 'getPlayRate' of 'panda3d.core.AudioSound' objects>"
        'getPriority': None, # (!) real value is "<method 'getPriority' of 'panda3d.core.AudioSound' objects>"
        'getSpeakerLevel': None, # (!) real value is "<method 'getSpeakerLevel' of 'panda3d.core.AudioSound' objects>"
        'getSpeakerMix': None, # (!) real value is "<method 'getSpeakerMix' of 'panda3d.core.AudioSound' objects>"
        'getTime': None, # (!) real value is "<method 'getTime' of 'panda3d.core.AudioSound' objects>"
        'getVolume': None, # (!) real value is "<method 'getVolume' of 'panda3d.core.AudioSound' objects>"
        'get_3d_max_distance': None, # (!) real value is "<method 'get_3d_max_distance' of 'panda3d.core.AudioSound' objects>"
        'get_3d_min_distance': None, # (!) real value is "<method 'get_3d_min_distance' of 'panda3d.core.AudioSound' objects>"
        'get_active': None, # (!) real value is "<method 'get_active' of 'panda3d.core.AudioSound' objects>"
        'get_balance': None, # (!) real value is "<method 'get_balance' of 'panda3d.core.AudioSound' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE381660>)>'
        'get_finished_event': None, # (!) real value is "<method 'get_finished_event' of 'panda3d.core.AudioSound' objects>"
        'get_loop': None, # (!) real value is "<method 'get_loop' of 'panda3d.core.AudioSound' objects>"
        'get_loop_count': None, # (!) real value is "<method 'get_loop_count' of 'panda3d.core.AudioSound' objects>"
        'get_name': None, # (!) real value is "<method 'get_name' of 'panda3d.core.AudioSound' objects>"
        'get_play_rate': None, # (!) real value is "<method 'get_play_rate' of 'panda3d.core.AudioSound' objects>"
        'get_priority': None, # (!) real value is "<method 'get_priority' of 'panda3d.core.AudioSound' objects>"
        'get_speaker_level': None, # (!) real value is "<method 'get_speaker_level' of 'panda3d.core.AudioSound' objects>"
        'get_speaker_mix': None, # (!) real value is "<method 'get_speaker_mix' of 'panda3d.core.AudioSound' objects>"
        'get_time': None, # (!) real value is "<method 'get_time' of 'panda3d.core.AudioSound' objects>"
        'get_volume': None, # (!) real value is "<method 'get_volume' of 'panda3d.core.AudioSound' objects>"
        'length': None, # (!) real value is "<method 'length' of 'panda3d.core.AudioSound' objects>"
        'output': None, # (!) real value is "<method 'output' of 'panda3d.core.AudioSound' objects>"
        'play': None, # (!) real value is "<method 'play' of 'panda3d.core.AudioSound' objects>"
        'set3dAttributes': None, # (!) real value is "<method 'set3dAttributes' of 'panda3d.core.AudioSound' objects>"
        'set3dMaxDistance': None, # (!) real value is "<method 'set3dMaxDistance' of 'panda3d.core.AudioSound' objects>"
        'set3dMinDistance': None, # (!) real value is "<method 'set3dMinDistance' of 'panda3d.core.AudioSound' objects>"
        'setActive': None, # (!) real value is "<method 'setActive' of 'panda3d.core.AudioSound' objects>"
        'setBalance': None, # (!) real value is "<method 'setBalance' of 'panda3d.core.AudioSound' objects>"
        'setFinishedEvent': None, # (!) real value is "<method 'setFinishedEvent' of 'panda3d.core.AudioSound' objects>"
        'setLoop': None, # (!) real value is "<method 'setLoop' of 'panda3d.core.AudioSound' objects>"
        'setLoopCount': None, # (!) real value is "<method 'setLoopCount' of 'panda3d.core.AudioSound' objects>"
        'setPlayRate': None, # (!) real value is "<method 'setPlayRate' of 'panda3d.core.AudioSound' objects>"
        'setPriority': None, # (!) real value is "<method 'setPriority' of 'panda3d.core.AudioSound' objects>"
        'setSpeakerLevels': None, # (!) real value is "<method 'setSpeakerLevels' of 'panda3d.core.AudioSound' objects>"
        'setSpeakerMix': None, # (!) real value is "<method 'setSpeakerMix' of 'panda3d.core.AudioSound' objects>"
        'setTime': None, # (!) real value is "<method 'setTime' of 'panda3d.core.AudioSound' objects>"
        'setVolume': None, # (!) real value is "<method 'setVolume' of 'panda3d.core.AudioSound' objects>"
        'set_3d_attributes': None, # (!) real value is "<method 'set_3d_attributes' of 'panda3d.core.AudioSound' objects>"
        'set_3d_max_distance': None, # (!) real value is "<method 'set_3d_max_distance' of 'panda3d.core.AudioSound' objects>"
        'set_3d_min_distance': None, # (!) real value is "<method 'set_3d_min_distance' of 'panda3d.core.AudioSound' objects>"
        'set_active': None, # (!) real value is "<method 'set_active' of 'panda3d.core.AudioSound' objects>"
        'set_balance': None, # (!) real value is "<method 'set_balance' of 'panda3d.core.AudioSound' objects>"
        'set_finished_event': None, # (!) real value is "<method 'set_finished_event' of 'panda3d.core.AudioSound' objects>"
        'set_loop': None, # (!) real value is "<method 'set_loop' of 'panda3d.core.AudioSound' objects>"
        'set_loop_count': None, # (!) real value is "<method 'set_loop_count' of 'panda3d.core.AudioSound' objects>"
        'set_play_rate': None, # (!) real value is "<method 'set_play_rate' of 'panda3d.core.AudioSound' objects>"
        'set_priority': None, # (!) real value is "<method 'set_priority' of 'panda3d.core.AudioSound' objects>"
        'set_speaker_levels': None, # (!) real value is "<method 'set_speaker_levels' of 'panda3d.core.AudioSound' objects>"
        'set_speaker_mix': None, # (!) real value is "<method 'set_speaker_mix' of 'panda3d.core.AudioSound' objects>"
        'set_time': None, # (!) real value is "<method 'set_time' of 'panda3d.core.AudioSound' objects>"
        'set_volume': None, # (!) real value is "<method 'set_volume' of 'panda3d.core.AudioSound' objects>"
        'status': None, # (!) real value is "<method 'status' of 'panda3d.core.AudioSound' objects>"
        'stop': None, # (!) real value is "<method 'stop' of 'panda3d.core.AudioSound' objects>"
        'write': None, # (!) real value is "<method 'write' of 'panda3d.core.AudioSound' objects>"
    }
    PLAYING = 2
    READY = 1


