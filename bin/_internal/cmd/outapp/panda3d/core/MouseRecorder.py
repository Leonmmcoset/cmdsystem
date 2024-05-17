# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .DataNode import DataNode

from .RecorderBase import RecorderBase

class MouseRecorder(DataNode, RecorderBase):
    """
    /**
     * This object records any data generated by a particular MouseAndKeyboard
     * node on the datagraph for a session for eventual playback via a
     * DataGraphPlayback (and a PlaybackController).  To use it, make it a child
     * of the node you wish to record.  It also serves as a pass-through, so that
     * additional child nodes may be parented directly to it.
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

    def upcastToDataNode(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        upcast_to_DataNode(const MouseRecorder self)
        
        upcast from MouseRecorder to DataNode
        """
        pass

    def upcastToRecorderBase(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        upcast_to_RecorderBase(const MouseRecorder self)
        
        upcast from MouseRecorder to RecorderBase
        """
        pass

    def upcast_to_DataNode(self, const_MouseRecorder_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        upcast_to_DataNode(const MouseRecorder self)
        
        upcast from MouseRecorder to DataNode
        """
        pass

    def upcast_to_RecorderBase(self, const_MouseRecorder_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        upcast_to_RecorderBase(const MouseRecorder self)
        
        upcast from MouseRecorder to RecorderBase
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
        '__doc__': '/**\n * This object records any data generated by a particular MouseAndKeyboard\n * node on the datagraph for a session for eventual playback via a\n * DataGraphPlayback (and a PlaybackController).  To use it, make it a child\n * of the node you wish to record.  It also serves as a pass-through, so that\n * additional child nodes may be parented directly to it.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.MouseRecorder' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE285020>'
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE285020>)>'
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE285020>)>'
        'upcastToDataNode': None, # (!) real value is "<method 'upcastToDataNode' of 'panda3d.core.MouseRecorder' objects>"
        'upcastToRecorderBase': None, # (!) real value is "<method 'upcastToRecorderBase' of 'panda3d.core.MouseRecorder' objects>"
        'upcast_to_DataNode': None, # (!) real value is "<method 'upcast_to_DataNode' of 'panda3d.core.MouseRecorder' objects>"
        'upcast_to_RecorderBase': None, # (!) real value is "<method 'upcast_to_RecorderBase' of 'panda3d.core.MouseRecorder' objects>"
    }

