# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .TiXmlNode import TiXmlNode

class TiXmlDeclaration(TiXmlNode):
    """
    /** In correct XML the declaration is the first entry in the file.
        @verbatim
            <?xml version="1.0" standalone="yes"?>
        @endverbatim
    
        TinyXml will happily read or write files without a declaration,
        however. There are 3 possible attributes to the declaration:
        version, encoding, and standalone.
    
        Note: In this version of the code, the attributes are
        handled as special cases, not generic attributes, simply
        because there can only be at most 3 and they are always the same.
    */
    """
    def assign(self, const_TiXmlDeclaration_self, const_TiXmlDeclaration_copy): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        assign(const TiXmlDeclaration self, const TiXmlDeclaration copy)
        """
        pass

    def Encoding(self, TiXmlDeclaration_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        Encoding(TiXmlDeclaration self)
        
        /// Encoding. Will return an empty string if none was found.
        """
        pass

    def Standalone(self, TiXmlDeclaration_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        Standalone(TiXmlDeclaration self)
        
        /// Is this a standalone document?
        """
        pass

    def Version(self, TiXmlDeclaration_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        Version(TiXmlDeclaration self)
        
        /// Version. Will return an empty string if none was found.
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
        'Encoding': None, # (!) real value is "<method 'Encoding' of 'panda3d.core.TiXmlDeclaration' objects>"
        'Standalone': None, # (!) real value is "<method 'Standalone' of 'panda3d.core.TiXmlDeclaration' objects>"
        'Version': None, # (!) real value is "<method 'Version' of 'panda3d.core.TiXmlDeclaration' objects>"
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.core.TiXmlDeclaration' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.core.TiXmlDeclaration' objects>"
        '__doc__': '/** In correct XML the declaration is the first entry in the file.\n    @verbatim\n        <?xml version="1.0" standalone="yes"?>\n    @endverbatim\n\n    TinyXml will happily read or write files without a declaration,\n    however. There are 3 possible attributes to the declaration:\n    version, encoding, and standalone.\n\n    Note: In this version of the code, the attributes are\n    handled as special cases, not generic attributes, simply\n    because there can only be at most 3 and they are always the same.\n*/',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.TiXmlDeclaration' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE3908C0>'
        'assign': None, # (!) real value is "<method 'assign' of 'panda3d.core.TiXmlDeclaration' objects>"
    }


