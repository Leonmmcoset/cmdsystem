# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .TypedReferenceCount import TypedReferenceCount

class AuxSceneData(TypedReferenceCount):
    """
    /**
     * This is a base class for a generic data structure that can be attached per-
     * instance to the camera, to store per-instance data that must be preserved
     * over multiple frames.
     *
     * In particular, this is used to implement the FadeLODNode, which must
     * remember during traversal at what point it is in the fade, separately for
     * each instance and for each camera.
     */
    """
    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getDuration(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_duration(AuxSceneData self)
        
        /**
         * Returns the minimum length in time, in seconds, to keep this AuxSceneData
         * object around in the scene graph after the last time it was rendered.
         */
        """
        pass

    def getExpirationTime(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_expiration_time(AuxSceneData self)
        
        /**
         * Returns the frame_time at which this AuxSceneData object is currently
         * scheduled to be removed from the scene graph.
         */
        """
        pass

    def getLastRenderTime(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_last_render_time(AuxSceneData self)
        
        /**
         * Returns the last time this object was used during traversal (according to
         * set_last_render_time()).
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_duration(self, AuxSceneData_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_duration(AuxSceneData self)
        
        /**
         * Returns the minimum length in time, in seconds, to keep this AuxSceneData
         * object around in the scene graph after the last time it was rendered.
         */
        """
        pass

    def get_expiration_time(self, AuxSceneData_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_expiration_time(AuxSceneData self)
        
        /**
         * Returns the frame_time at which this AuxSceneData object is currently
         * scheduled to be removed from the scene graph.
         */
        """
        pass

    def get_last_render_time(self, AuxSceneData_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_last_render_time(AuxSceneData self)
        
        /**
         * Returns the last time this object was used during traversal (according to
         * set_last_render_time()).
         */
        """
        pass

    def output(self, AuxSceneData_self, ostream_out): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        output(AuxSceneData self, ostream out)
        
        /**
         *
         */
        """
        pass

    def setDuration(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_duration(const AuxSceneData self, double duration)
        
        /**
         * Specifies the minimum length in time, in seconds, to keep this AuxSceneData
         * object around in the scene graph after the last time it was rendered.
         */
        """
        pass

    def setLastRenderTime(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_last_render_time(const AuxSceneData self, double render_time)
        
        /**
         * Should be called with the current frame_time each time the AuxSceneData is
         * used during traversal.
         */
        """
        pass

    def set_duration(self, const_AuxSceneData_self, double_duration): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_duration(const AuxSceneData self, double duration)
        
        /**
         * Specifies the minimum length in time, in seconds, to keep this AuxSceneData
         * object around in the scene graph after the last time it was rendered.
         */
        """
        pass

    def set_last_render_time(self, const_AuxSceneData_self, double_render_time): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_last_render_time(const AuxSceneData self, double render_time)
        
        /**
         * Should be called with the current frame_time each time the AuxSceneData is
         * used during traversal.
         */
        """
        pass

    def write(self, AuxSceneData_self, ostream_out, int_indent_level): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        write(AuxSceneData self, ostream out, int indent_level)
        
        /**
         *
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

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.core.AuxSceneData' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.core.AuxSceneData' objects>"
        '__doc__': '/**\n * This is a base class for a generic data structure that can be attached per-\n * instance to the camera, to store per-instance data that must be preserved\n * over multiple frames.\n *\n * In particular, this is used to implement the FadeLODNode, which must\n * remember during traversal at what point it is in the fade, separately for\n * each instance and for each camera.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.AuxSceneData' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE294380>'
        '__repr__': None, # (!) real value is "<slot wrapper '__repr__' of 'panda3d.core.AuxSceneData' objects>"
        '__str__': None, # (!) real value is "<slot wrapper '__str__' of 'panda3d.core.AuxSceneData' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE294380>)>'
        'getDuration': None, # (!) real value is "<method 'getDuration' of 'panda3d.core.AuxSceneData' objects>"
        'getExpirationTime': None, # (!) real value is "<method 'getExpirationTime' of 'panda3d.core.AuxSceneData' objects>"
        'getLastRenderTime': None, # (!) real value is "<method 'getLastRenderTime' of 'panda3d.core.AuxSceneData' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE294380>)>'
        'get_duration': None, # (!) real value is "<method 'get_duration' of 'panda3d.core.AuxSceneData' objects>"
        'get_expiration_time': None, # (!) real value is "<method 'get_expiration_time' of 'panda3d.core.AuxSceneData' objects>"
        'get_last_render_time': None, # (!) real value is "<method 'get_last_render_time' of 'panda3d.core.AuxSceneData' objects>"
        'output': None, # (!) real value is "<method 'output' of 'panda3d.core.AuxSceneData' objects>"
        'setDuration': None, # (!) real value is "<method 'setDuration' of 'panda3d.core.AuxSceneData' objects>"
        'setLastRenderTime': None, # (!) real value is "<method 'setLastRenderTime' of 'panda3d.core.AuxSceneData' objects>"
        'set_duration': None, # (!) real value is "<method 'set_duration' of 'panda3d.core.AuxSceneData' objects>"
        'set_last_render_time': None, # (!) real value is "<method 'set_last_render_time' of 'panda3d.core.AuxSceneData' objects>"
        'write': None, # (!) real value is "<method 'write' of 'panda3d.core.AuxSceneData' objects>"
    }


