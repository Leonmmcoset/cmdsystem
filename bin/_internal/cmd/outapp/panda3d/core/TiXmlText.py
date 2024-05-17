# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .TiXmlNode import TiXmlNode

class TiXmlText(TiXmlNode):
    """
    /** XML text. A text node can have 2 ways to output the next. "normal" output
        and CDATA. It will default to the mode it was parsed from the XML file and
        you generally want to leave it alone, but you can change the output mode with
        SetCDATA() and query it with CDATA().
    */
    """
    def assign(self, const_TiXmlText_self, const_TiXmlText_base): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        assign(const TiXmlText self, const TiXmlText base)
        """
        pass

    def CDATA(self, TiXmlText_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        CDATA(TiXmlText self)
        
        /// Queries whether this represents text using a CDATA section.
        """
        pass

    def SetCDATA(self, const_TiXmlText_self, bool__cdata): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        SetCDATA(const TiXmlText self, bool _cdata)
        
        /// Turns on or off a CDATA representation of text.
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
        'CDATA': None, # (!) real value is "<method 'CDATA' of 'panda3d.core.TiXmlText' objects>"
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        'SetCDATA': None, # (!) real value is "<method 'SetCDATA' of 'panda3d.core.TiXmlText' objects>"
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.core.TiXmlText' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.core.TiXmlText' objects>"
        '__doc__': '/** XML text. A text node can have 2 ways to output the next. "normal" output\n    and CDATA. It will default to the mode it was parsed from the XML file and\n    you generally want to leave it alone, but you can change the output mode with\n    SetCDATA() and query it with CDATA().\n*/',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.TiXmlText' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE391910>'
        'assign': None, # (!) real value is "<method 'assign' of 'panda3d.core.TiXmlText' objects>"
    }


