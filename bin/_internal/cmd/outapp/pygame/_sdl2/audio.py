# encoding: utf-8
# module pygame._sdl2.audio
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\pygame\_sdl2\audio.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import traceback as traceback # C:\Users\leonm\AppData\Local\Programs\Python\Python311\Lib\traceback.py
from pygame._sdl2.sdl2 import error


# Variables with simple values

AUDIO_ALLOW_ANY_CHANGE = 15

AUDIO_ALLOW_CHANNELS_CHANGE = 4

AUDIO_ALLOW_FORMAT_CHANGE = 2

AUDIO_ALLOW_FREQUENCY_CHANGE = 1

AUDIO_F32 = 33056
AUDIO_F32LSB = 33056
AUDIO_F32MSB = 37152
AUDIO_S16 = 32784
AUDIO_S16LSB = 32784
AUDIO_S16MSB = 36880
AUDIO_S32 = 32800
AUDIO_S32LSB = 32800
AUDIO_S32MSB = 36896
AUDIO_S8 = 32776
AUDIO_U16 = 16
AUDIO_U16LSB = 16
AUDIO_U16MSB = 4112
AUDIO_U8 = 8

# functions

def get_audio_device_names(*args, **kwargs): # real signature unknown
    """
    Returns a list of unique devicenames for each available audio device.
    
        :param bool iscapture: If False return devices available for playback.
                               If True return devices available for capture.
    
        :return: list of devicenames.
        :rtype: List[string]
    """
    pass

def __pyx_unpickle_Enum(*args, **kwargs): # real signature unknown
    pass

def __reduce_cython__(*args, **kwargs): # real signature unknown
    pass

def __setstate_cython__(*args, **kwargs): # real signature unknown
    pass

# classes

class AudioDevice(object):
    # no doc
    def close(self, *args, **kwargs): # real signature unknown
        """ Use this to pause and unpause audio playback on this device. """
        pass

    def pause(self, *args, **kwargs): # real signature unknown
        """
        Use this to pause and unpause audio playback on this device.
        
                :param int pause_on:
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        """
        An AudioDevice is for sound playback and capture of 'sound cards'.
        
                :param string devicename: One of the device names from get_audio_device_names.
                                         If None is passed in, it uses the default audio device.
                :param int frequency: Number of samples per second. 44100, 22050, ...
                :param int audioformat: AUDIO_F32SYS, AUDIO_F32SYS, AUDIO_U16SYS, AUDIO_S16SYS, ...
                :param int numchannels: 2 if stereo, 1 if mono.
                :param int chunksize: number of samples buffered.
        
                :param allowed_changes: some drivers don't support all possible requested formats.
                                        So you can tell it which ones yours support.
                    * AUDIO_ALLOW_FREQUENCY_CHANGE
                    * AUDIO_ALLOW_FORMAT_CHANGE
                    * AUDIO_ALLOW_CHANNELS_CHANGE
                    * AUDIO_ALLOW_ANY_CHANGE
        
                    If your application can only handle one specific data format,
                    pass a zero for allowed_changes and let SDL transparently handle any differences.
        
                :callback: a function which gets called with (audiodevice, memoryview).
                           memoryview is the audio data.
                           Use audiodevice.iscapture to see if it is incoming audio or outgoing.
                           The audiodevice also has the format of the memory.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    audioformat = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """ AUDIO_F32SYS, AUDIO_F32SYS, AUDIO_U16SYS, AUDIO_S16SYS, ...
        """

    callback = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """ called in the sound thread with (audiodevice, memoryview)
        """

    chunksize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """ number of samples buffered.
        """

    deviceid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """ deviceid of the audio device relative to the devicename list.
        """

    devicename = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """ devicename of the audio device from the devicename list.
        """

    frequency = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """ Number of samples per second. 44100, 22050, ...
        """

    iscapture = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """ is the AudioDevice for capturing audio?
        """

    numchannels = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """ 2 if stereo, 1 if mono.
        """



# variables with complex values

_audio_format_str = {
    8: 'AUDIO_U8',
    16: 'AUDIO_U16',
    4112: 'AUDIO_U16MSB',
    32776: 'AUDIO_S8',
    32784: 'AUDIO_S16',
    32800: 'AUDIO_S32',
    33056: 'AUDIO_F32',
    36880: 'AUDIO_S16MSB',
    36896: 'AUDIO_S32MSB',
    37152: 'AUDIO_F32MSB',
}

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x000001F6CD585FD0>'

__spec__ = None # (!) real value is "ModuleSpec(name='pygame._sdl2.audio', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x000001F6CD585FD0>, origin='C:\\\\Users\\\\leonm\\\\PycharmProjects\\\\leonsystem\\\\venv\\\\Lib\\\\site-packages\\\\pygame\\\\_sdl2\\\\audio.cp311-win_amd64.pyd')"

__test__ = {}

