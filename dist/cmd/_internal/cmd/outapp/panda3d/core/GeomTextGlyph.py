# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .Geom import Geom

class GeomTextGlyph(Geom):
    """
    /**
     * This is a specialization on Geom for containing a primitive intended to
     * represent a TextGlyph.  Its sole purpose is to maintain the geom count on
     * the glyph, so we can determine the actual usage count on a dynamic glyph
     * (and thus know when it is safe to recycle the glyph).
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
        '__doc__': '/**\n * This is a specialization on Geom for containing a primitive intended to\n * represent a TextGlyph.  Its sole purpose is to maintain the geom count on\n * the glyph, so we can determine the actual usage count on a dynamic glyph\n * (and thus know when it is safe to recycle the glyph).\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.GeomTextGlyph' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE35E8F0>'
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE35E8F0>)>'
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE35E8F0>)>'
    }


