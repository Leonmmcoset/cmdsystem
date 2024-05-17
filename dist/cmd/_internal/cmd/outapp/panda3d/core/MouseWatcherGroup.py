# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .MouseWatcherBase import MouseWatcherBase

from .ReferenceCount import ReferenceCount

class MouseWatcherGroup(MouseWatcherBase, ReferenceCount):
    """
    /**
     * This represents a collection of MouseWatcherRegions that may be managed as
     * a group.  The implementation for this is in MouseWatcherBase; this class
     * exists so that we can inherit from ReferenceCount.
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

    def upcastToMouseWatcherBase(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        upcast_to_MouseWatcherBase(const MouseWatcherGroup self)
        
        upcast from MouseWatcherGroup to MouseWatcherBase
        """
        pass

    def upcastToReferenceCount(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        upcast_to_ReferenceCount(const MouseWatcherGroup self)
        
        upcast from MouseWatcherGroup to ReferenceCount
        """
        pass

    def upcast_to_MouseWatcherBase(self, const_MouseWatcherGroup_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        upcast_to_MouseWatcherBase(const MouseWatcherGroup self)
        
        upcast from MouseWatcherGroup to MouseWatcherBase
        """
        pass

    def upcast_to_ReferenceCount(self, const_MouseWatcherGroup_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        upcast_to_ReferenceCount(const MouseWatcherGroup self)
        
        upcast from MouseWatcherGroup to ReferenceCount
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
        '__doc__': '/**\n * This represents a collection of MouseWatcherRegions that may be managed as\n * a group.  The implementation for this is in MouseWatcherBase; this class\n * exists so that we can inherit from ReferenceCount.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.MouseWatcherGroup' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE3669E0>'
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE3669E0>)>'
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE3669E0>)>'
        'upcastToMouseWatcherBase': None, # (!) real value is "<method 'upcastToMouseWatcherBase' of 'panda3d.core.MouseWatcherGroup' objects>"
        'upcastToReferenceCount': None, # (!) real value is "<method 'upcastToReferenceCount' of 'panda3d.core.MouseWatcherGroup' objects>"
        'upcast_to_MouseWatcherBase': None, # (!) real value is "<method 'upcast_to_MouseWatcherBase' of 'panda3d.core.MouseWatcherGroup' objects>"
        'upcast_to_ReferenceCount': None, # (!) real value is "<method 'upcast_to_ReferenceCount' of 'panda3d.core.MouseWatcherGroup' objects>"
    }


