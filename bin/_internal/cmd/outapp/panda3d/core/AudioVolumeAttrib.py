# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .RenderAttrib import RenderAttrib

class AudioVolumeAttrib(RenderAttrib):
    """
    /**
     * Applies a scale to audio volume for positional sounds in the scene graph.
     */
    """
    def getClassSlot(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_slot()
        """
        pass

    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getVolume(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_volume(AudioVolumeAttrib self)
        
        /**
         * Returns the volume to be applied to sounds.
         */
        """
        pass

    def get_class_slot(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_slot()
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_volume(self, AudioVolumeAttrib_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_volume(AudioVolumeAttrib self)
        
        /**
         * Returns the volume to be applied to sounds.
         */
        """
        pass

    def hasVolume(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_volume(AudioVolumeAttrib self)
        
        /**
         * Returns true if the AudioVolumeAttrib has a non-identity volume, false
         * otherwise (in which case it might be an off attrib or an identity attrib).
         */
        """
        pass

    def has_volume(self, AudioVolumeAttrib_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_volume(AudioVolumeAttrib self)
        
        /**
         * Returns true if the AudioVolumeAttrib has a non-identity volume, false
         * otherwise (in which case it might be an off attrib or an identity attrib).
         */
        """
        pass

    def isOff(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_off(AudioVolumeAttrib self)
        
        /**
         * Returns true if the AudioVolumeAttrib will ignore any color scales
         * inherited from above, false otherwise.  This is not the same thing as
         * !has_scale(); a AudioVolumeAttrib may have the "off" flag set and also have
         * another scale specified.
         */
        """
        pass

    def is_off(self, AudioVolumeAttrib_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_off(AudioVolumeAttrib self)
        
        /**
         * Returns true if the AudioVolumeAttrib will ignore any color scales
         * inherited from above, false otherwise.  This is not the same thing as
         * !has_scale(); a AudioVolumeAttrib may have the "off" flag set and also have
         * another scale specified.
         */
        """
        pass

    def make(self, float_volume): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        make(float volume)
        
        /**
         * Constructs a new AudioVolumeAttrib object that indicates audio volume
         * should be scaled by the indicated factor.
         */
        """
        pass

    def makeDefault(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        make_default()
        
        /**
         * Returns a RenderAttrib that corresponds to whatever the standard default
         * properties for render attributes of this type ought to be.
         */
        """
        pass

    def makeIdentity(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        make_identity()
        
        /**
         * Constructs an identity audio volume attrib.
         */
        """
        pass

    def makeOff(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        make_off()
        
        /**
         * Constructs a new AudioVolumeAttrib object that ignores any
         * AudioVolumeAttrib inherited from above.  You may also specify an additional
         * volume scale to apply to geometry below (using set_volume()).
         */
        """
        pass

    def make_default(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        make_default()
        
        /**
         * Returns a RenderAttrib that corresponds to whatever the standard default
         * properties for render attributes of this type ought to be.
         */
        """
        pass

    def make_identity(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        make_identity()
        
        /**
         * Constructs an identity audio volume attrib.
         */
        """
        pass

    def make_off(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        make_off()
        
        /**
         * Constructs a new AudioVolumeAttrib object that ignores any
         * AudioVolumeAttrib inherited from above.  You may also specify an additional
         * volume scale to apply to geometry below (using set_volume()).
         */
        """
        pass

    def setVolume(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_volume(AudioVolumeAttrib self, float volume)
        
        /**
         * Returns a new AudioVolumeAttrib, just like this one, but with the volume
         * changed to the indicated value.
         */
        """
        pass

    def set_volume(self, AudioVolumeAttrib_self, float_volume): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_volume(AudioVolumeAttrib self, float volume)
        
        /**
         * Returns a new AudioVolumeAttrib, just like this one, but with the volume
         * changed to the indicated value.
         */
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    volume = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    class_slot = 3
    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__doc__': '/**\n * Applies a scale to audio volume for positional sounds in the scene graph.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.AudioVolumeAttrib' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE293FE0>'
        'class_slot': None, # (!) real value is "<attribute 'class_slot' of 'panda3d.core.AudioVolumeAttrib'>"
        'getClassSlot': None, # (!) real value is '<staticmethod(<built-in method getClassSlot of type object at 0x00007FFCFE293FE0>)>'
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE293FE0>)>'
        'getVolume': None, # (!) real value is "<method 'getVolume' of 'panda3d.core.AudioVolumeAttrib' objects>"
        'get_class_slot': None, # (!) real value is '<staticmethod(<built-in method get_class_slot of type object at 0x00007FFCFE293FE0>)>'
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE293FE0>)>'
        'get_volume': None, # (!) real value is "<method 'get_volume' of 'panda3d.core.AudioVolumeAttrib' objects>"
        'hasVolume': None, # (!) real value is "<method 'hasVolume' of 'panda3d.core.AudioVolumeAttrib' objects>"
        'has_volume': None, # (!) real value is "<method 'has_volume' of 'panda3d.core.AudioVolumeAttrib' objects>"
        'isOff': None, # (!) real value is "<method 'isOff' of 'panda3d.core.AudioVolumeAttrib' objects>"
        'is_off': None, # (!) real value is "<method 'is_off' of 'panda3d.core.AudioVolumeAttrib' objects>"
        'make': None, # (!) real value is '<staticmethod(<built-in method make of type object at 0x00007FFCFE293FE0>)>'
        'makeDefault': None, # (!) real value is '<staticmethod(<built-in method makeDefault of type object at 0x00007FFCFE293FE0>)>'
        'makeIdentity': None, # (!) real value is '<staticmethod(<built-in method makeIdentity of type object at 0x00007FFCFE293FE0>)>'
        'makeOff': None, # (!) real value is '<staticmethod(<built-in method makeOff of type object at 0x00007FFCFE293FE0>)>'
        'make_default': None, # (!) real value is '<staticmethod(<built-in method make_default of type object at 0x00007FFCFE293FE0>)>'
        'make_identity': None, # (!) real value is '<staticmethod(<built-in method make_identity of type object at 0x00007FFCFE293FE0>)>'
        'make_off': None, # (!) real value is '<staticmethod(<built-in method make_off of type object at 0x00007FFCFE293FE0>)>'
        'setVolume': None, # (!) real value is "<method 'setVolume' of 'panda3d.core.AudioVolumeAttrib' objects>"
        'set_volume': None, # (!) real value is "<method 'set_volume' of 'panda3d.core.AudioVolumeAttrib' objects>"
        'volume': None, # (!) real value is "<attribute 'volume' of 'panda3d.core.AudioVolumeAttrib' objects>"
    }


