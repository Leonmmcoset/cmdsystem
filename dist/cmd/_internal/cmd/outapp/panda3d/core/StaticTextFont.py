# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .TextFont import TextFont

class StaticTextFont(TextFont):
    """
    /**
     * A StaticTextFont is loaded up from a model that was previously generated
     * via egg-mkfont, and contains all of its glyphs already generated and
     * available for use.  It doesn't require linking with any external libraries
     * like FreeType.
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

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__doc__': "/**\n * A StaticTextFont is loaded up from a model that was previously generated\n * via egg-mkfont, and contains all of its glyphs already generated and\n * available for use.  It doesn't require linking with any external libraries\n * like FreeType.\n */",
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.StaticTextFont' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE35EAC0>'
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE35EAC0>)>'
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE35EAC0>)>'
    }


