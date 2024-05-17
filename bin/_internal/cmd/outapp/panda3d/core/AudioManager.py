# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .TypedReferenceCount import TypedReferenceCount

class AudioManager(TypedReferenceCount):
    # no doc
    def audio3dGetDistanceFactor(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        audio_3d_get_distance_factor(AudioManager self)
        """
        pass

    def audio3dGetDopplerFactor(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        audio_3d_get_doppler_factor(AudioManager self)
        """
        pass

    def audio3dGetDropOffFactor(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        audio_3d_get_drop_off_factor(AudioManager self)
        """
        pass

    def audio3dSetDistanceFactor(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        audio_3d_set_distance_factor(const AudioManager self, float factor)
        
        // Control the "relative scale that sets the distance factor" units for 3D
        // spacialized audio. This is a float in units-per-meter. Default value is
        // 1.0, which means that Panda units are understood as meters; for e.g.
        // feet, set 3.28. This factor is applied only to Fmod and OpenAL at the
        // moment.
        """
        pass

    def audio3dSetDopplerFactor(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        audio_3d_set_doppler_factor(const AudioManager self, float factor)
        
        // Control the presence of the Doppler effect.  Default is 1.0 Exaggerated
        // Doppler, use >1.0 Diminshed Doppler, use <1.0
        """
        pass

    def audio3dSetDropOffFactor(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        audio_3d_set_drop_off_factor(const AudioManager self, float factor)
        
        // Exaggerate or diminish the effect of distance on sound.  Default is 1.0
        // Valid range is 0 to 10 Faster drop off, use >1.0 Slower drop off, use
        // <1.0
        """
        pass

    def audio3dSetListenerAttributes(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        audio_3d_set_listener_attributes(const AudioManager self, float px, float py, float pz, float vx, float vy, float vz, float fx, float fy, float fz, float ux, float uy, float uz)
        
        // This controls the "set of ears" that listens to 3D spacialized sound px,
        // py, pz are position coordinates.  vx, vy, vz are a velocity vector in
        // UNITS PER SECOND (default: meters). fx, fy and fz are the respective
        // components of a unit forward-vector ux, uy and uz are the respective
        // components of a unit up-vector
        """
        pass

    def audio_3d_get_distance_factor(self, AudioManager_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        audio_3d_get_distance_factor(AudioManager self)
        """
        pass

    def audio_3d_get_doppler_factor(self, AudioManager_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        audio_3d_get_doppler_factor(AudioManager self)
        """
        pass

    def audio_3d_get_drop_off_factor(self, AudioManager_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        audio_3d_get_drop_off_factor(AudioManager self)
        """
        pass

    def audio_3d_set_distance_factor(self, const_AudioManager_self, float_factor): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        audio_3d_set_distance_factor(const AudioManager self, float factor)
        
        // Control the "relative scale that sets the distance factor" units for 3D
        // spacialized audio. This is a float in units-per-meter. Default value is
        // 1.0, which means that Panda units are understood as meters; for e.g.
        // feet, set 3.28. This factor is applied only to Fmod and OpenAL at the
        // moment.
        """
        pass

    def audio_3d_set_doppler_factor(self, const_AudioManager_self, float_factor): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        audio_3d_set_doppler_factor(const AudioManager self, float factor)
        
        // Control the presence of the Doppler effect.  Default is 1.0 Exaggerated
        // Doppler, use >1.0 Diminshed Doppler, use <1.0
        """
        pass

    def audio_3d_set_drop_off_factor(self, const_AudioManager_self, float_factor): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        audio_3d_set_drop_off_factor(const AudioManager self, float factor)
        
        // Exaggerate or diminish the effect of distance on sound.  Default is 1.0
        // Valid range is 0 to 10 Faster drop off, use >1.0 Slower drop off, use
        // <1.0
        """
        pass

    def audio_3d_set_listener_attributes(self, const_AudioManager_self, float_px, float_py, float_pz, float_vx, float_vy, float_vz, float_fx, float_fy, float_fz, float_ux, float_uy, float_uz): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        audio_3d_set_listener_attributes(const AudioManager self, float px, float py, float pz, float vx, float vy, float vz, float fx, float fy, float fz, float ux, float uy, float uz)
        
        // This controls the "set of ears" that listens to 3D spacialized sound px,
        // py, pz are position coordinates.  vx, vy, vz are a velocity vector in
        // UNITS PER SECOND (default: meters). fx, fy and fz are the respective
        // components of a unit forward-vector ux, uy and uz are the respective
        // components of a unit up-vector
        """
        pass

    def clearCache(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_cache(const AudioManager self)
        """
        pass

    def clear_cache(self, const_AudioManager_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_cache(const AudioManager self)
        """
        pass

    def configureFilters(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        configure_filters(const AudioManager self, FilterProperties config)
        """
        pass

    def configure_filters(self, const_AudioManager_self, FilterProperties_config): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        configure_filters(const AudioManager self, FilterProperties config)
        """
        pass

    def createAudioManager(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        create_AudioManager()
        """
        pass

    def create_AudioManager(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        create_AudioManager()
        """
        pass

    def getActive(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_active(AudioManager self)
        """
        pass

    def getCacheLimit(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_cache_limit(AudioManager self)
        """
        pass

    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getConcurrentSoundLimit(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_concurrent_sound_limit(AudioManager self)
        """
        pass

    def getDlsPathname(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_dls_pathname()
        """
        pass

    def getNullSound(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_null_sound(const AudioManager self)
        """
        pass

    def getSound(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_sound(const AudioManager self, MovieAudio source, bool positional, int mode)
        
        // Get a sound:
        """
        pass

    def getSpeakerSetup(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_speaker_setup(const AudioManager self)
        """
        pass

    def getVolume(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_volume(AudioManager self)
        """
        pass

    def get_active(self, AudioManager_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_active(AudioManager self)
        """
        pass

    def get_cache_limit(self, AudioManager_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_cache_limit(AudioManager self)
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_concurrent_sound_limit(self, AudioManager_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_concurrent_sound_limit(AudioManager self)
        """
        pass

    def get_dls_pathname(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_dls_pathname()
        """
        pass

    def get_null_sound(self, const_AudioManager_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_null_sound(const AudioManager self)
        """
        pass

    def get_sound(self, const_AudioManager_self, MovieAudio_source, bool_positional, int_mode): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_sound(const AudioManager self, MovieAudio source, bool positional, int mode)
        
        // Get a sound:
        """
        pass

    def get_speaker_setup(self, const_AudioManager_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_speaker_setup(const AudioManager self)
        """
        pass

    def get_volume(self, AudioManager_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_volume(AudioManager self)
        """
        pass

    def isValid(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_valid(const AudioManager self)
        
        // If you're interested in knowing whether this audio manager is valid,
        // here's the call to do it.  It is not necessary to check whether the audio
        // manager is valid before making other calls.  You are free to use an
        // invalid sound manager, you may get silent sounds from it though.  The
        // sound manager and the sounds it creates should not crash the application
        // even when the objects are not valid.
        """
        pass

    def is_valid(self, const_AudioManager_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_valid(const AudioManager self)
        
        // If you're interested in knowing whether this audio manager is valid,
        // here's the call to do it.  It is not necessary to check whether the audio
        // manager is valid before making other calls.  You are free to use an
        // invalid sound manager, you may get silent sounds from it though.  The
        // sound manager and the sounds it creates should not crash the application
        // even when the objects are not valid.
        """
        pass

    def output(self, AudioManager_self, ostream_out): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        output(AudioManager self, ostream out)
        """
        pass

    def reduceSoundsPlayingTo(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        reduce_sounds_playing_to(const AudioManager self, int count)
        
        // This is likely to be a utility function for the concurrent_sound_limit
        // options.  It is exposed as an API, because it's reasonable that it may be
        // useful to be here.  It reduces the number of concurrently playing sounds
        // to count by some implementation specific means.  If the number of sounds
        // currently playing is at or below count then there is no effect.
        """
        pass

    def reduce_sounds_playing_to(self, const_AudioManager_self, int_count): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        reduce_sounds_playing_to(const AudioManager self, int count)
        
        // This is likely to be a utility function for the concurrent_sound_limit
        // options.  It is exposed as an API, because it's reasonable that it may be
        // useful to be here.  It reduces the number of concurrently playing sounds
        // to count by some implementation specific means.  If the number of sounds
        // currently playing is at or below count then there is no effect.
        """
        pass

    def setActive(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_active(const AudioManager self, bool flag)
        
        // Turn the manager on or off.  If you play a sound while the manager is
        // inactive, it won't start.  If you deactivate the manager while sounds are
        // playing, they'll stop.  If you activate the manager while looping sounds
        // are playing (those that have a loop_count of zero), they will start
        // playing from the beginning of their loop.  Defaults to true.
        """
        pass

    def setCacheLimit(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_cache_limit(const AudioManager self, int count)
        """
        pass

    def setConcurrentSoundLimit(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_concurrent_sound_limit(const AudioManager self, int limit)
        
        // This controls the number of sounds that you allow at once.  This is more
        // of a user choice -- it avoids talk over and the creation of a cacophony.
        // It can also be used to help performance.  0 == unlimited.  1 == mutually
        // exclusive (one sound at a time).  Which is an example of: n == allow n
        // sounds to be playing at the same time.
        """
        pass

    def setSpeakerConfiguration(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_speaker_configuration(const AudioManager self, LVecBase3f speaker1, LVecBase3f speaker2, LVecBase3f speaker3, LVecBase3f speaker4, LVecBase3f speaker5, LVecBase3f speaker6, LVecBase3f speaker7, LVecBase3f speaker8, LVecBase3f speaker9)
        
        // set_speaker_configuration is a Miles only method.
        """
        pass

    def setSpeakerSetup(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_speaker_setup(const AudioManager self, int cat)
        """
        pass

    def setVolume(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_volume(const AudioManager self, float volume)
        
        // Control volume: FYI: If you start a sound with the volume off and turn
        // the volume up later, you'll hear the sound playing at that late point.  0
        // = minimum; 1.0 = maximum.  inits to 1.0.
        """
        pass

    def set_active(self, const_AudioManager_self, bool_flag): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_active(const AudioManager self, bool flag)
        
        // Turn the manager on or off.  If you play a sound while the manager is
        // inactive, it won't start.  If you deactivate the manager while sounds are
        // playing, they'll stop.  If you activate the manager while looping sounds
        // are playing (those that have a loop_count of zero), they will start
        // playing from the beginning of their loop.  Defaults to true.
        """
        pass

    def set_cache_limit(self, const_AudioManager_self, int_count): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_cache_limit(const AudioManager self, int count)
        """
        pass

    def set_concurrent_sound_limit(self, const_AudioManager_self, int_limit): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_concurrent_sound_limit(const AudioManager self, int limit)
        
        // This controls the number of sounds that you allow at once.  This is more
        // of a user choice -- it avoids talk over and the creation of a cacophony.
        // It can also be used to help performance.  0 == unlimited.  1 == mutually
        // exclusive (one sound at a time).  Which is an example of: n == allow n
        // sounds to be playing at the same time.
        """
        pass

    def set_speaker_configuration(self, const_AudioManager_self, LVecBase3f_speaker1, LVecBase3f_speaker2, LVecBase3f_speaker3, LVecBase3f_speaker4, LVecBase3f_speaker5, LVecBase3f_speaker6, LVecBase3f_speaker7, LVecBase3f_speaker8, LVecBase3f_speaker9): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_speaker_configuration(const AudioManager self, LVecBase3f speaker1, LVecBase3f speaker2, LVecBase3f speaker3, LVecBase3f speaker4, LVecBase3f speaker5, LVecBase3f speaker6, LVecBase3f speaker7, LVecBase3f speaker8, LVecBase3f speaker9)
        
        // set_speaker_configuration is a Miles only method.
        """
        pass

    def set_speaker_setup(self, const_AudioManager_self, int_cat): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_speaker_setup(const AudioManager self, int cat)
        """
        pass

    def set_volume(self, const_AudioManager_self, float_volume): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_volume(const AudioManager self, float volume)
        
        // Control volume: FYI: If you start a sound with the volume off and turn
        // the volume up later, you'll hear the sound playing at that late point.  0
        // = minimum; 1.0 = maximum.  inits to 1.0.
        """
        pass

    def shutdown(self, const_AudioManager_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        shutdown(const AudioManager self)
        """
        pass

    def stopAllSounds(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        stop_all_sounds(const AudioManager self)
        
        // Stop playback on all sounds managed by this manager.  This is effectively
        // the same as reduce_sounds_playing_to(0), but this call may be for
        // efficient on some implementations.
        """
        pass

    def stop_all_sounds(self, const_AudioManager_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        stop_all_sounds(const AudioManager self)
        
        // Stop playback on all sounds managed by this manager.  This is effectively
        // the same as reduce_sounds_playing_to(0), but this call may be for
        // efficient on some implementations.
        """
        pass

    def uncacheSound(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        uncache_sound(const AudioManager self, const Filename file_name)
        
        // Tell the AudioManager there is no need to keep this one cached.  This
        // doesn't break any connection between AudioSounds that have already given
        // by get_sound() from this manager.  It's only affecting whether the
        // AudioManager keeps a copy of the sound in its poolcache.
        """
        pass

    def uncache_sound(self, const_AudioManager_self, const_Filename_file_name): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        uncache_sound(const AudioManager self, const Filename file_name)
        
        // Tell the AudioManager there is no need to keep this one cached.  This
        // doesn't break any connection between AudioSounds that have already given
        // by get_sound() from this manager.  It's only affecting whether the
        // AudioManager keeps a copy of the sound in its poolcache.
        """
        pass

    def update(self, const_AudioManager_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        update(const AudioManager self)
        
        // This should be called every frame.  Failure to call could cause problems.
        """
        pass

    def write(self, AudioManager_self, ostream_out): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        write(AudioManager self, ostream out)
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

    dls_pathname = Filename('/c/Windows/System32/drivers/gm.dls')
    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        'SMHeuristic': 0,
        'SMSample': 1,
        'SMStream': 2,
        'SM_heuristic': 0,
        'SM_sample': 1,
        'SM_stream': 2,
        'SPEAKERMODE5point1': 5,
        'SPEAKERMODE7point1': 6,
        'SPEAKERMODECOUNT': 8,
        'SPEAKERMODEMax': 7,
        'SPEAKERMODEMono': 1,
        'SPEAKERMODEQuad': 3,
        'SPEAKERMODERaw': 0,
        'SPEAKERMODEStereo': 2,
        'SPEAKERMODESurround': 4,
        'SPEAKERMODE_5point1': 5,
        'SPEAKERMODE_7point1': 6,
        'SPEAKERMODE_COUNT': 8,
        'SPEAKERMODE_max': 7,
        'SPEAKERMODE_mono': 1,
        'SPEAKERMODE_quad': 3,
        'SPEAKERMODE_raw': 0,
        'SPEAKERMODE_stereo': 2,
        'SPEAKERMODE_surround': 4,
        'SPKBackleft': 5,
        'SPKBackright': 6,
        'SPKCOUNT': 9,
        'SPKCenter': 3,
        'SPKFrontleft': 1,
        'SPKFrontright': 2,
        'SPKNone': 0,
        'SPKSideleft': 7,
        'SPKSideright': 8,
        'SPKSub': 4,
        'SPK_COUNT': 9,
        'SPK_backleft': 5,
        'SPK_backright': 6,
        'SPK_center': 3,
        'SPK_frontleft': 1,
        'SPK_frontright': 2,
        'SPK_none': 0,
        'SPK_sideleft': 7,
        'SPK_sideright': 8,
        'SPK_sub': 4,
        '__doc__': None,
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.AudioManager' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE381830>'
        '__repr__': None, # (!) real value is "<slot wrapper '__repr__' of 'panda3d.core.AudioManager' objects>"
        '__str__': None, # (!) real value is "<slot wrapper '__str__' of 'panda3d.core.AudioManager' objects>"
        'audio3dGetDistanceFactor': None, # (!) real value is "<method 'audio3dGetDistanceFactor' of 'panda3d.core.AudioManager' objects>"
        'audio3dGetDopplerFactor': None, # (!) real value is "<method 'audio3dGetDopplerFactor' of 'panda3d.core.AudioManager' objects>"
        'audio3dGetDropOffFactor': None, # (!) real value is "<method 'audio3dGetDropOffFactor' of 'panda3d.core.AudioManager' objects>"
        'audio3dSetDistanceFactor': None, # (!) real value is "<method 'audio3dSetDistanceFactor' of 'panda3d.core.AudioManager' objects>"
        'audio3dSetDopplerFactor': None, # (!) real value is "<method 'audio3dSetDopplerFactor' of 'panda3d.core.AudioManager' objects>"
        'audio3dSetDropOffFactor': None, # (!) real value is "<method 'audio3dSetDropOffFactor' of 'panda3d.core.AudioManager' objects>"
        'audio3dSetListenerAttributes': None, # (!) real value is "<method 'audio3dSetListenerAttributes' of 'panda3d.core.AudioManager' objects>"
        'audio_3d_get_distance_factor': None, # (!) real value is "<method 'audio_3d_get_distance_factor' of 'panda3d.core.AudioManager' objects>"
        'audio_3d_get_doppler_factor': None, # (!) real value is "<method 'audio_3d_get_doppler_factor' of 'panda3d.core.AudioManager' objects>"
        'audio_3d_get_drop_off_factor': None, # (!) real value is "<method 'audio_3d_get_drop_off_factor' of 'panda3d.core.AudioManager' objects>"
        'audio_3d_set_distance_factor': None, # (!) real value is "<method 'audio_3d_set_distance_factor' of 'panda3d.core.AudioManager' objects>"
        'audio_3d_set_doppler_factor': None, # (!) real value is "<method 'audio_3d_set_doppler_factor' of 'panda3d.core.AudioManager' objects>"
        'audio_3d_set_drop_off_factor': None, # (!) real value is "<method 'audio_3d_set_drop_off_factor' of 'panda3d.core.AudioManager' objects>"
        'audio_3d_set_listener_attributes': None, # (!) real value is "<method 'audio_3d_set_listener_attributes' of 'panda3d.core.AudioManager' objects>"
        'clearCache': None, # (!) real value is "<method 'clearCache' of 'panda3d.core.AudioManager' objects>"
        'clear_cache': None, # (!) real value is "<method 'clear_cache' of 'panda3d.core.AudioManager' objects>"
        'configureFilters': None, # (!) real value is "<method 'configureFilters' of 'panda3d.core.AudioManager' objects>"
        'configure_filters': None, # (!) real value is "<method 'configure_filters' of 'panda3d.core.AudioManager' objects>"
        'createAudioManager': None, # (!) real value is '<staticmethod(<built-in method createAudioManager of type object at 0x00007FFCFE381830>)>'
        'create_AudioManager': None, # (!) real value is '<staticmethod(<built-in method create_AudioManager of type object at 0x00007FFCFE381830>)>'
        'dls_pathname': None, # (!) real value is "<attribute 'dls_pathname' of 'panda3d.core.AudioManager'>"
        'getActive': None, # (!) real value is "<method 'getActive' of 'panda3d.core.AudioManager' objects>"
        'getCacheLimit': None, # (!) real value is "<method 'getCacheLimit' of 'panda3d.core.AudioManager' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE381830>)>'
        'getConcurrentSoundLimit': None, # (!) real value is "<method 'getConcurrentSoundLimit' of 'panda3d.core.AudioManager' objects>"
        'getDlsPathname': None, # (!) real value is '<staticmethod(<built-in method getDlsPathname of type object at 0x00007FFCFE381830>)>'
        'getNullSound': None, # (!) real value is "<method 'getNullSound' of 'panda3d.core.AudioManager' objects>"
        'getSound': None, # (!) real value is "<method 'getSound' of 'panda3d.core.AudioManager' objects>"
        'getSpeakerSetup': None, # (!) real value is "<method 'getSpeakerSetup' of 'panda3d.core.AudioManager' objects>"
        'getVolume': None, # (!) real value is "<method 'getVolume' of 'panda3d.core.AudioManager' objects>"
        'get_active': None, # (!) real value is "<method 'get_active' of 'panda3d.core.AudioManager' objects>"
        'get_cache_limit': None, # (!) real value is "<method 'get_cache_limit' of 'panda3d.core.AudioManager' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE381830>)>'
        'get_concurrent_sound_limit': None, # (!) real value is "<method 'get_concurrent_sound_limit' of 'panda3d.core.AudioManager' objects>"
        'get_dls_pathname': None, # (!) real value is '<staticmethod(<built-in method get_dls_pathname of type object at 0x00007FFCFE381830>)>'
        'get_null_sound': None, # (!) real value is "<method 'get_null_sound' of 'panda3d.core.AudioManager' objects>"
        'get_sound': None, # (!) real value is "<method 'get_sound' of 'panda3d.core.AudioManager' objects>"
        'get_speaker_setup': None, # (!) real value is "<method 'get_speaker_setup' of 'panda3d.core.AudioManager' objects>"
        'get_volume': None, # (!) real value is "<method 'get_volume' of 'panda3d.core.AudioManager' objects>"
        'isValid': None, # (!) real value is "<method 'isValid' of 'panda3d.core.AudioManager' objects>"
        'is_valid': None, # (!) real value is "<method 'is_valid' of 'panda3d.core.AudioManager' objects>"
        'output': None, # (!) real value is "<method 'output' of 'panda3d.core.AudioManager' objects>"
        'reduceSoundsPlayingTo': None, # (!) real value is "<method 'reduceSoundsPlayingTo' of 'panda3d.core.AudioManager' objects>"
        'reduce_sounds_playing_to': None, # (!) real value is "<method 'reduce_sounds_playing_to' of 'panda3d.core.AudioManager' objects>"
        'setActive': None, # (!) real value is "<method 'setActive' of 'panda3d.core.AudioManager' objects>"
        'setCacheLimit': None, # (!) real value is "<method 'setCacheLimit' of 'panda3d.core.AudioManager' objects>"
        'setConcurrentSoundLimit': None, # (!) real value is "<method 'setConcurrentSoundLimit' of 'panda3d.core.AudioManager' objects>"
        'setSpeakerConfiguration': None, # (!) real value is "<method 'setSpeakerConfiguration' of 'panda3d.core.AudioManager' objects>"
        'setSpeakerSetup': None, # (!) real value is "<method 'setSpeakerSetup' of 'panda3d.core.AudioManager' objects>"
        'setVolume': None, # (!) real value is "<method 'setVolume' of 'panda3d.core.AudioManager' objects>"
        'set_active': None, # (!) real value is "<method 'set_active' of 'panda3d.core.AudioManager' objects>"
        'set_cache_limit': None, # (!) real value is "<method 'set_cache_limit' of 'panda3d.core.AudioManager' objects>"
        'set_concurrent_sound_limit': None, # (!) real value is "<method 'set_concurrent_sound_limit' of 'panda3d.core.AudioManager' objects>"
        'set_speaker_configuration': None, # (!) real value is "<method 'set_speaker_configuration' of 'panda3d.core.AudioManager' objects>"
        'set_speaker_setup': None, # (!) real value is "<method 'set_speaker_setup' of 'panda3d.core.AudioManager' objects>"
        'set_volume': None, # (!) real value is "<method 'set_volume' of 'panda3d.core.AudioManager' objects>"
        'shutdown': None, # (!) real value is "<method 'shutdown' of 'panda3d.core.AudioManager' objects>"
        'stopAllSounds': None, # (!) real value is "<method 'stopAllSounds' of 'panda3d.core.AudioManager' objects>"
        'stop_all_sounds': None, # (!) real value is "<method 'stop_all_sounds' of 'panda3d.core.AudioManager' objects>"
        'uncacheSound': None, # (!) real value is "<method 'uncacheSound' of 'panda3d.core.AudioManager' objects>"
        'uncache_sound': None, # (!) real value is "<method 'uncache_sound' of 'panda3d.core.AudioManager' objects>"
        'update': None, # (!) real value is "<method 'update' of 'panda3d.core.AudioManager' objects>"
        'write': None, # (!) real value is "<method 'write' of 'panda3d.core.AudioManager' objects>"
    }
    SMHeuristic = 0
    SMSample = 1
    SMStream = 2
    SM_heuristic = 0
    SM_sample = 1
    SM_stream = 2
    SPEAKERMODE5point1 = 5
    SPEAKERMODE7point1 = 6
    SPEAKERMODECOUNT = 8
    SPEAKERMODEMax = 7
    SPEAKERMODEMono = 1
    SPEAKERMODEQuad = 3
    SPEAKERMODERaw = 0
    SPEAKERMODEStereo = 2
    SPEAKERMODESurround = 4
    SPEAKERMODE_5point1 = 5
    SPEAKERMODE_7point1 = 6
    SPEAKERMODE_COUNT = 8
    SPEAKERMODE_max = 7
    SPEAKERMODE_mono = 1
    SPEAKERMODE_quad = 3
    SPEAKERMODE_raw = 0
    SPEAKERMODE_stereo = 2
    SPEAKERMODE_surround = 4
    SPKBackleft = 5
    SPKBackright = 6
    SPKCenter = 3
    SPKCOUNT = 9
    SPKFrontleft = 1
    SPKFrontright = 2
    SPKNone = 0
    SPKSideleft = 7
    SPKSideright = 8
    SPKSub = 4
    SPK_backleft = 5
    SPK_backright = 6
    SPK_center = 3
    SPK_COUNT = 9
    SPK_frontleft = 1
    SPK_frontright = 2
    SPK_none = 0
    SPK_sideleft = 7
    SPK_sideright = 8
    SPK_sub = 4


