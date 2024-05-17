# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .Lens import Lens

class OrthographicLens(Lens):
    """
    /**
     * An orthographic lens.  Although this kind of lens is linear, like a
     * PerspectiveLens, it doesn't respect field-of-view or focal length
     * parameters, and adjusting these will have no effect.  Instead, its field of
     * view is controlled by adjusting the film_size; the orthographic lens
     * represents a planar projection onto its imaginary film of the specified
     * size, hanging in space.
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
        '__doc__': "/**\n * An orthographic lens.  Although this kind of lens is linear, like a\n * PerspectiveLens, it doesn't respect field-of-view or focal length\n * parameters, and adjusting these will have no effect.  Instead, its field of\n * view is controlled by adjusting the film_size; the orthographic lens\n * represents a planar projection onto its imaginary film of the specified\n * size, hanging in space.\n */",
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.OrthographicLens' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE2FFD90>'
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE2FFD90>)>'
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE2FFD90>)>'
    }


