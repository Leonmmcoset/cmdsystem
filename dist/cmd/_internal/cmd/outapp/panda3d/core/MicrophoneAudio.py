# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .MovieAudio import MovieAudio

class MicrophoneAudio(MovieAudio):
    """
    /**
     * Class MicrophoneAudio provides the means to read raw audio samples from a
     * microphone.
     */
    """
    def getChannels(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_channels(MicrophoneAudio self)
        
        /**
         * Returns the number of channels.
         */
        """
        pass

    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getNumOptions(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_options()
        
        /**
         * Returns the number of microphone options.  An "option" consists of a device
         * plus a set of configuration parameters.  For example, "Soundblaster Audigy
         * Line in at 44,100 samples/sec" would be an option.
         */
        """
        pass

    def getOption(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_option(int n)
        
        /**
         * Returns the nth microphone option.
         */
        """
        pass

    def getOptions(self, *args, **kwargs): # real signature unknown
        pass

    def getRate(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_rate(MicrophoneAudio self)
        
        /**
         * Returns the sample rate.
         */
        """
        pass

    def get_channels(self, MicrophoneAudio_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_channels(MicrophoneAudio self)
        
        /**
         * Returns the number of channels.
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_num_options(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_options()
        
        /**
         * Returns the number of microphone options.  An "option" consists of a device
         * plus a set of configuration parameters.  For example, "Soundblaster Audigy
         * Line in at 44,100 samples/sec" would be an option.
         */
        """
        pass

    def get_option(self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_option(int n)
        
        /**
         * Returns the nth microphone option.
         */
        """
        pass

    def get_options(self, *args, **kwargs): # real signature unknown
        pass

    def get_rate(self, MicrophoneAudio_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_rate(MicrophoneAudio self)
        
        /**
         * Returns the sample rate.
         */
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    channels = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    rate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__doc__': '/**\n * Class MicrophoneAudio provides the means to read raw audio samples from a\n * microphone.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.MicrophoneAudio' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE2B8C00>'
        'channels': None, # (!) real value is "<attribute 'channels' of 'panda3d.core.MicrophoneAudio' objects>"
        'getChannels': None, # (!) real value is "<method 'getChannels' of 'panda3d.core.MicrophoneAudio' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE2B8C00>)>'
        'getNumOptions': None, # (!) real value is '<staticmethod(<built-in method getNumOptions of type object at 0x00007FFCFE2B8C00>)>'
        'getOption': None, # (!) real value is '<staticmethod(<built-in method getOption of type object at 0x00007FFCFE2B8C00>)>'
        'getOptions': None, # (!) real value is '<staticmethod(<built-in method getOptions of type object at 0x00007FFCFE2B8C00>)>'
        'getRate': None, # (!) real value is "<method 'getRate' of 'panda3d.core.MicrophoneAudio' objects>"
        'get_channels': None, # (!) real value is "<method 'get_channels' of 'panda3d.core.MicrophoneAudio' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE2B8C00>)>'
        'get_num_options': None, # (!) real value is '<staticmethod(<built-in method get_num_options of type object at 0x00007FFCFE2B8C00>)>'
        'get_option': None, # (!) real value is '<staticmethod(<built-in method get_option of type object at 0x00007FFCFE2B8C00>)>'
        'get_options': None, # (!) real value is '<staticmethod(<built-in method get_options of type object at 0x00007FFCFE2B8C00>)>'
        'get_rate': None, # (!) real value is "<method 'get_rate' of 'panda3d.core.MicrophoneAudio' objects>"
        'options': None, # (!) real value is "<attribute 'options' of 'panda3d.core.MicrophoneAudio'>"
        'rate': None, # (!) real value is "<attribute 'rate' of 'panda3d.core.MicrophoneAudio' objects>"
    }
    options = None # (!) real value is '<MicrophoneAudio.options[0] of <NULL>>'


