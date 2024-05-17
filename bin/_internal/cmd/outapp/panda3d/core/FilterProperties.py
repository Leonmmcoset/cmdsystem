# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .TypedReferenceCount import TypedReferenceCount

class FilterProperties(TypedReferenceCount):
    # no doc
    def addChorus(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_chorus(const FilterProperties self, float drymix, float wet1, float wet2, float wet3, float delay, float rate, float depth)
        
        /**
         * Add a chorus filter to the end of the DSP chain.
         */
        """
        pass

    def addCompress(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_compress(const FilterProperties self, float threshold, float attack, float release, float gainmakeup)
        
        /**
         * Add a compress filter to the end of the DSP chain.
         */
        """
        pass

    def addDistort(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_distort(const FilterProperties self, float level)
        
        /**
         * Add a distort filter to the end of the DSP chain.
         */
        """
        pass

    def addEcho(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_echo(const FilterProperties self, float drymix, float wetmix, float delay, float decayratio)
        
        /**
         * Add a echo filter to the end of the DSP chain.
         */
        """
        pass

    def addFlange(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_flange(const FilterProperties self, float drymix, float wetmix, float depth, float rate)
        
        /**
         * Add a flange filter to the end of the DSP chain.
         */
        """
        pass

    def addHighpass(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_highpass(const FilterProperties self, float cutoff_freq, float resonance_q)
        
        /**
         * Add a highpass filter to the end of the DSP chain.
         */
        """
        pass

    def addLowpass(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_lowpass(const FilterProperties self, float cutoff_freq, float resonance_q)
        
        /**
         * Add a lowpass filter to the end of the DSP chain.
         */
        """
        pass

    def addNormalize(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_normalize(const FilterProperties self, float fadetime, float threshold, float maxamp)
        
        /**
         * Add a normalize filter to the end of the DSP chain.
         */
        """
        pass

    def addParameq(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_parameq(const FilterProperties self, float center_freq, float bandwidth, float gain)
        
        /**
         * Add a parameq filter to the end of the DSP chain.
         */
        """
        pass

    def addPitchshift(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_pitchshift(const FilterProperties self, float pitch, float fftsize, float overlap)
        
        /**
         * Add a pitchshift filter to the end of the DSP chain.
         */
        """
        pass

    def addSfxreverb(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_sfxreverb(const FilterProperties self, float drylevel, float room, float roomhf, float decaytime, float decayhfratio, float reflectionslevel, float reflectionsdelay, float reverblevel, float reverbdelay, float diffusion, float density, float hfreference, float roomlf, float lfreference)
        
        /**
         * Add a reverb filter to the end of the DSP chain.
         */
        """
        pass

    def add_chorus(self, const_FilterProperties_self, float_drymix, float_wet1, float_wet2, float_wet3, float_delay, float_rate, float_depth): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_chorus(const FilterProperties self, float drymix, float wet1, float wet2, float wet3, float delay, float rate, float depth)
        
        /**
         * Add a chorus filter to the end of the DSP chain.
         */
        """
        pass

    def add_compress(self, const_FilterProperties_self, float_threshold, float_attack, float_release, float_gainmakeup): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_compress(const FilterProperties self, float threshold, float attack, float release, float gainmakeup)
        
        /**
         * Add a compress filter to the end of the DSP chain.
         */
        """
        pass

    def add_distort(self, const_FilterProperties_self, float_level): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_distort(const FilterProperties self, float level)
        
        /**
         * Add a distort filter to the end of the DSP chain.
         */
        """
        pass

    def add_echo(self, const_FilterProperties_self, float_drymix, float_wetmix, float_delay, float_decayratio): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_echo(const FilterProperties self, float drymix, float wetmix, float delay, float decayratio)
        
        /**
         * Add a echo filter to the end of the DSP chain.
         */
        """
        pass

    def add_flange(self, const_FilterProperties_self, float_drymix, float_wetmix, float_depth, float_rate): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_flange(const FilterProperties self, float drymix, float wetmix, float depth, float rate)
        
        /**
         * Add a flange filter to the end of the DSP chain.
         */
        """
        pass

    def add_highpass(self, const_FilterProperties_self, float_cutoff_freq, float_resonance_q): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_highpass(const FilterProperties self, float cutoff_freq, float resonance_q)
        
        /**
         * Add a highpass filter to the end of the DSP chain.
         */
        """
        pass

    def add_lowpass(self, const_FilterProperties_self, float_cutoff_freq, float_resonance_q): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_lowpass(const FilterProperties self, float cutoff_freq, float resonance_q)
        
        /**
         * Add a lowpass filter to the end of the DSP chain.
         */
        """
        pass

    def add_normalize(self, const_FilterProperties_self, float_fadetime, float_threshold, float_maxamp): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_normalize(const FilterProperties self, float fadetime, float threshold, float maxamp)
        
        /**
         * Add a normalize filter to the end of the DSP chain.
         */
        """
        pass

    def add_parameq(self, const_FilterProperties_self, float_center_freq, float_bandwidth, float_gain): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_parameq(const FilterProperties self, float center_freq, float bandwidth, float gain)
        
        /**
         * Add a parameq filter to the end of the DSP chain.
         */
        """
        pass

    def add_pitchshift(self, const_FilterProperties_self, float_pitch, float_fftsize, float_overlap): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_pitchshift(const FilterProperties self, float pitch, float fftsize, float overlap)
        
        /**
         * Add a pitchshift filter to the end of the DSP chain.
         */
        """
        pass

    def add_sfxreverb(self, const_FilterProperties_self, float_drylevel, float_room, float_roomhf, float_decaytime, float_decayhfratio, float_reflectionslevel, float_reflectionsdelay, float_reverblevel, float_reverbdelay, float_diffusion, float_density, float_hfreference, float_roomlf, float_lfreference): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_sfxreverb(const FilterProperties self, float drylevel, float room, float roomhf, float decaytime, float decayhfratio, float reflectionslevel, float reflectionsdelay, float reverblevel, float reverbdelay, float diffusion, float density, float hfreference, float roomlf, float lfreference)
        
        /**
         * Add a reverb filter to the end of the DSP chain.
         */
        """
        pass

    def clear(self, const_FilterProperties_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear(const FilterProperties self)
        
        /**
         * Removes all DSP postprocessing.
         */
        """
        pass

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
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.core.FilterProperties' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.core.FilterProperties' objects>"
        '__doc__': None,
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.FilterProperties' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE381480>'
        'addChorus': None, # (!) real value is "<method 'addChorus' of 'panda3d.core.FilterProperties' objects>"
        'addCompress': None, # (!) real value is "<method 'addCompress' of 'panda3d.core.FilterProperties' objects>"
        'addDistort': None, # (!) real value is "<method 'addDistort' of 'panda3d.core.FilterProperties' objects>"
        'addEcho': None, # (!) real value is "<method 'addEcho' of 'panda3d.core.FilterProperties' objects>"
        'addFlange': None, # (!) real value is "<method 'addFlange' of 'panda3d.core.FilterProperties' objects>"
        'addHighpass': None, # (!) real value is "<method 'addHighpass' of 'panda3d.core.FilterProperties' objects>"
        'addLowpass': None, # (!) real value is "<method 'addLowpass' of 'panda3d.core.FilterProperties' objects>"
        'addNormalize': None, # (!) real value is "<method 'addNormalize' of 'panda3d.core.FilterProperties' objects>"
        'addParameq': None, # (!) real value is "<method 'addParameq' of 'panda3d.core.FilterProperties' objects>"
        'addPitchshift': None, # (!) real value is "<method 'addPitchshift' of 'panda3d.core.FilterProperties' objects>"
        'addSfxreverb': None, # (!) real value is "<method 'addSfxreverb' of 'panda3d.core.FilterProperties' objects>"
        'add_chorus': None, # (!) real value is "<method 'add_chorus' of 'panda3d.core.FilterProperties' objects>"
        'add_compress': None, # (!) real value is "<method 'add_compress' of 'panda3d.core.FilterProperties' objects>"
        'add_distort': None, # (!) real value is "<method 'add_distort' of 'panda3d.core.FilterProperties' objects>"
        'add_echo': None, # (!) real value is "<method 'add_echo' of 'panda3d.core.FilterProperties' objects>"
        'add_flange': None, # (!) real value is "<method 'add_flange' of 'panda3d.core.FilterProperties' objects>"
        'add_highpass': None, # (!) real value is "<method 'add_highpass' of 'panda3d.core.FilterProperties' objects>"
        'add_lowpass': None, # (!) real value is "<method 'add_lowpass' of 'panda3d.core.FilterProperties' objects>"
        'add_normalize': None, # (!) real value is "<method 'add_normalize' of 'panda3d.core.FilterProperties' objects>"
        'add_parameq': None, # (!) real value is "<method 'add_parameq' of 'panda3d.core.FilterProperties' objects>"
        'add_pitchshift': None, # (!) real value is "<method 'add_pitchshift' of 'panda3d.core.FilterProperties' objects>"
        'add_sfxreverb': None, # (!) real value is "<method 'add_sfxreverb' of 'panda3d.core.FilterProperties' objects>"
        'clear': None, # (!) real value is "<method 'clear' of 'panda3d.core.FilterProperties' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE381480>)>'
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE381480>)>'
    }


