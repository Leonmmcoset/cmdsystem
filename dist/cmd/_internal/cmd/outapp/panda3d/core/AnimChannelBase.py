# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .AnimGroup import AnimGroup

class AnimChannelBase(AnimGroup):
    """
    /**
     * Parent class for all animation channels.  An AnimChannel is an arbitrary
     * function that changes over time (actually, over frames), usually defined by
     * a table read from an egg file (but possibly computed or generated in any
     * other way).
     */
    """
    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_type(AnimChannelBase self)
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_type(self, AnimChannelBase_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_type(AnimChannelBase self)
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
        '__doc__': '/**\n * Parent class for all animation channels.  An AnimChannel is an arbitrary\n * function that changes over time (actually, over frames), usually defined by\n * a table read from an egg file (but possibly computed or generated in any\n * other way).\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.AnimChannelBase' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE2C3380>'
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE2C3380>)>'
        'getType': None, # (!) real value is "<method 'getType' of 'panda3d.core.AnimChannelBase' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE2C3380>)>'
        'get_type': None, # (!) real value is "<method 'get_type' of 'panda3d.core.AnimChannelBase' objects>"
    }


