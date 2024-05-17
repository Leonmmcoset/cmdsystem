# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .MovieAudio import MovieAudio

class UserDataAudio(MovieAudio):
    """
    /**
     * A UserDataAudio is a way for the user to manually supply raw audio samples.
     * remove_after_read means the data will be removed if read once.  Else data
     * will be stored (enable looping and seeking). Expects data as 16 bit signed
     * (word); Example for stereo: 1.word = 1.channel,2.word = 2.channel, 3.word =
     * 1.channel,4.word = 2.channel, etc.
     */
    """
    def append(self, const_UserDataAudio_self, DatagramIterator_src, int_len): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        append(const UserDataAudio self, DatagramIterator src, int len)
        append(const UserDataAudio self, str str)
        
        /**
         * Appends audio samples to the buffer.
         */
        
        /**
         * Appends audio samples to the buffer from a datagram.  This is intended to
         * make it easy to send streaming raw audio over a network.
         */
        
        /**
         * Appends audio samples to the buffer from a string.  The samples must be
         * stored little-endian in the string.  This is not particularly efficient,
         * but it may be convenient to deal with samples in python.
         */
        """
        pass

    def done(self, const_UserDataAudio_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        done(const UserDataAudio self)
        
        // A promise not to write any more samples.
        
        /**
         * Promises not to append any more samples, ie, this marks the end of the
         * audio stream.
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
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.core.UserDataAudio' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.core.UserDataAudio' objects>"
        '__doc__': '/**\n * A UserDataAudio is a way for the user to manually supply raw audio samples.\n * remove_after_read means the data will be removed if read once.  Else data\n * will be stored (enable looping and seeking). Expects data as 16 bit signed\n * (word); Example for stereo: 1.word = 1.channel,2.word = 2.channel, 3.word =\n * 1.channel,4.word = 2.channel, etc.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.UserDataAudio' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE2B9170>'
        'append': None, # (!) real value is "<method 'append' of 'panda3d.core.UserDataAudio' objects>"
        'done': None, # (!) real value is "<method 'done' of 'panda3d.core.UserDataAudio' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE2B9170>)>'
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE2B9170>)>'
    }


