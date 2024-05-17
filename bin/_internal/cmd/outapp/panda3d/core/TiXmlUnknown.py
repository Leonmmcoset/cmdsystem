# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .TiXmlNode import TiXmlNode

class TiXmlUnknown(TiXmlNode):
    """
    /** Any tag that tinyXml doesn't recognize is saved as an
        unknown. It is a tag of text, but should not be modified.
        It will be written back to the XML, unchanged, when the file
        is saved.
    
        DTD tags get thrown into TiXmlUnknowns.
    */
    """
    def assign(self, const_TiXmlUnknown_self, const_TiXmlUnknown_copy): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        assign(const TiXmlUnknown self, const TiXmlUnknown copy)
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
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.core.TiXmlUnknown' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.core.TiXmlUnknown' objects>"
        '__doc__': "/** Any tag that tinyXml doesn't recognize is saved as an\n    unknown. It is a tag of text, but should not be modified.\n    It will be written back to the XML, unchanged, when the file\n    is saved.\n\n    DTD tags get thrown into TiXmlUnknowns.\n*/",
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.TiXmlUnknown' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE391AE0>'
        'assign': None, # (!) real value is "<method 'assign' of 'panda3d.core.TiXmlUnknown' objects>"
    }


