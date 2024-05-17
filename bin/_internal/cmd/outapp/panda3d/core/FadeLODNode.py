# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .LODNode import LODNode

class FadeLODNode(LODNode):
    """
    /**
     * A Level-of-Detail node with alpha based switching.
     */
    """
    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getFadeBinDrawOrder(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_fade_bin_draw_order(FadeLODNode self)
        
        /**
         * Returns the draw order that is assigned (along with the bin name) to the
         * fading part of the geometry during a transition.
         */
        """
        pass

    def getFadeBinName(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_fade_bin_name(FadeLODNode self)
        
        /**
         * Returns the cull bin that is assigned to the fading part of the geometry
         * during a transition.
         */
        """
        pass

    def getFadeStateOverride(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_fade_state_override(FadeLODNode self)
        
        /**
         * Returns the override value that is applied to the state changes necessary
         * to apply the fade effect.  This should be larger than any attrib overrides
         * on the fading geometry.
         */
        """
        pass

    def getFadeTime(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_fade_time(FadeLODNode self)
        
        /**
         * get the time taken to complete an LOD switch
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_fade_bin_draw_order(self, FadeLODNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_fade_bin_draw_order(FadeLODNode self)
        
        /**
         * Returns the draw order that is assigned (along with the bin name) to the
         * fading part of the geometry during a transition.
         */
        """
        pass

    def get_fade_bin_name(self, FadeLODNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_fade_bin_name(FadeLODNode self)
        
        /**
         * Returns the cull bin that is assigned to the fading part of the geometry
         * during a transition.
         */
        """
        pass

    def get_fade_state_override(self, FadeLODNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_fade_state_override(FadeLODNode self)
        
        /**
         * Returns the override value that is applied to the state changes necessary
         * to apply the fade effect.  This should be larger than any attrib overrides
         * on the fading geometry.
         */
        """
        pass

    def get_fade_time(self, FadeLODNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_fade_time(FadeLODNode self)
        
        /**
         * get the time taken to complete an LOD switch
         */
        """
        pass

    def setFadeBin(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_fade_bin(const FadeLODNode self, str name, int draw_order)
        
        /**
         * Specifies the cull bin and draw order that is assigned to the fading part
         * of the geometry during a transition.
         */
        """
        pass

    def setFadeStateOverride(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_fade_state_override(const FadeLODNode self, int override)
        
        /**
         * Specifies the override value that is applied to the state changes necessary
         * to apply the fade effect.  This should be larger than any attrib overrides
         * on the fading geometry.
         */
        """
        pass

    def setFadeTime(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_fade_time(const FadeLODNode self, float t)
        
        /**
         * set the time taken to complete an LOD switch
         */
        """
        pass

    def set_fade_bin(self, const_FadeLODNode_self, str_name, int_draw_order): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_fade_bin(const FadeLODNode self, str name, int draw_order)
        
        /**
         * Specifies the cull bin and draw order that is assigned to the fading part
         * of the geometry during a transition.
         */
        """
        pass

    def set_fade_state_override(self, const_FadeLODNode_self, int_override): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_fade_state_override(const FadeLODNode self, int override)
        
        /**
         * Specifies the override value that is applied to the state changes necessary
         * to apply the fade effect.  This should be larger than any attrib overrides
         * on the fading geometry.
         */
        """
        pass

    def set_fade_time(self, const_FadeLODNode_self, float_t): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_fade_time(const FadeLODNode self, float t)
        
        /**
         * set the time taken to complete an LOD switch
         */
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    fade_bin_draw_order = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    fade_bin_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    fade_state_override = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    fade_time = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__doc__': '/**\n * A Level-of-Detail node with alpha based switching.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.FadeLODNode' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE287AA0>'
        'fade_bin_draw_order': None, # (!) real value is "<attribute 'fade_bin_draw_order' of 'panda3d.core.FadeLODNode' objects>"
        'fade_bin_name': None, # (!) real value is "<attribute 'fade_bin_name' of 'panda3d.core.FadeLODNode' objects>"
        'fade_state_override': None, # (!) real value is "<attribute 'fade_state_override' of 'panda3d.core.FadeLODNode' objects>"
        'fade_time': None, # (!) real value is "<attribute 'fade_time' of 'panda3d.core.FadeLODNode' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE287AA0>)>'
        'getFadeBinDrawOrder': None, # (!) real value is "<method 'getFadeBinDrawOrder' of 'panda3d.core.FadeLODNode' objects>"
        'getFadeBinName': None, # (!) real value is "<method 'getFadeBinName' of 'panda3d.core.FadeLODNode' objects>"
        'getFadeStateOverride': None, # (!) real value is "<method 'getFadeStateOverride' of 'panda3d.core.FadeLODNode' objects>"
        'getFadeTime': None, # (!) real value is "<method 'getFadeTime' of 'panda3d.core.FadeLODNode' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE287AA0>)>'
        'get_fade_bin_draw_order': None, # (!) real value is "<method 'get_fade_bin_draw_order' of 'panda3d.core.FadeLODNode' objects>"
        'get_fade_bin_name': None, # (!) real value is "<method 'get_fade_bin_name' of 'panda3d.core.FadeLODNode' objects>"
        'get_fade_state_override': None, # (!) real value is "<method 'get_fade_state_override' of 'panda3d.core.FadeLODNode' objects>"
        'get_fade_time': None, # (!) real value is "<method 'get_fade_time' of 'panda3d.core.FadeLODNode' objects>"
        'setFadeBin': None, # (!) real value is "<method 'setFadeBin' of 'panda3d.core.FadeLODNode' objects>"
        'setFadeStateOverride': None, # (!) real value is "<method 'setFadeStateOverride' of 'panda3d.core.FadeLODNode' objects>"
        'setFadeTime': None, # (!) real value is "<method 'setFadeTime' of 'panda3d.core.FadeLODNode' objects>"
        'set_fade_bin': None, # (!) real value is "<method 'set_fade_bin' of 'panda3d.core.FadeLODNode' objects>"
        'set_fade_state_override': None, # (!) real value is "<method 'set_fade_state_override' of 'panda3d.core.FadeLODNode' objects>"
        'set_fade_time': None, # (!) real value is "<method 'set_fade_time' of 'panda3d.core.FadeLODNode' objects>"
    }


