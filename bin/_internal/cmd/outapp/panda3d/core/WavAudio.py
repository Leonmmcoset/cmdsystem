# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .MovieAudio import MovieAudio

class WavAudio(MovieAudio):
    """
    /**
     * A native PCM .wav loader.  Supported formats are linear PCM, IEEE float,
     * A-law and mu-law.
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

    def make(self, const_Filename_name): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        make(const Filename name)
        
        /**
         * Obtains a MovieAudio that references a file.
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
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.core.WavAudio' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.core.WavAudio' objects>"
        '__doc__': '/**\n * A native PCM .wav loader.  Supported formats are linear PCM, IEEE float,\n * A-law and mu-law.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.WavAudio' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE2B98B0>'
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE2B98B0>)>'
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE2B98B0>)>'
        'make': None, # (!) real value is '<staticmethod(<built-in method make of type object at 0x00007FFCFE2B98B0>)>'
    }


