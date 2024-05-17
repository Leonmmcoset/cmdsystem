# encoding: utf-8
# module panda3d.direct
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\direct.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import panda3d.core as __panda3d_core


from .CLerpInterval import CLerpInterval

class CLerpAnimEffectInterval(CLerpInterval):
    """
    /**
     * This interval lerps between different amounts of control effects for
     * various AnimControls that might be playing on an actor.  It's used to
     * change the blending amount between multiple animations.
     *
     * The idea is to start all the animations playing first, then use a
     * CLerpAnimEffectInterval to adjust the degree to which each animation
     * affects the actor.
     */
    """
    def addControl(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_control(const CLerpAnimEffectInterval self, AnimControl control, str name, float begin_effect, float end_effect)
        
        /**
         * Adds another AnimControl to the list of AnimControls affected by the lerp.
         * This control will be lerped from begin_effect to end_effect over the period
         * of the lerp.
         *
         * The AnimControl name parameter is only used when formatting the interval
         * for output.
         */
        """
        pass

    def add_control(self, const_CLerpAnimEffectInterval_self, AnimControl_control, str_name, float_begin_effect, float_end_effect): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_control(const CLerpAnimEffectInterval self, AnimControl control, str name, float begin_effect, float end_effect)
        
        /**
         * Adds another AnimControl to the list of AnimControls affected by the lerp.
         * This control will be lerped from begin_effect to end_effect over the period
         * of the lerp.
         *
         * The AnimControl name parameter is only used when formatting the interval
         * for output.
         */
        """
        pass

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
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.direct.CLerpAnimEffectInterval' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.direct.CLerpAnimEffectInterval' objects>"
        '__doc__': "/**\n * This interval lerps between different amounts of control effects for\n * various AnimControls that might be playing on an actor.  It's used to\n * change the blending amount between multiple animations.\n *\n * The idea is to start all the animations playing first, then use a\n * CLerpAnimEffectInterval to adjust the degree to which each animation\n * affects the actor.\n */",
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.direct.CLerpAnimEffectInterval' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFDC68E61F0>'
        'addControl': None, # (!) real value is "<method 'addControl' of 'panda3d.direct.CLerpAnimEffectInterval' objects>"
        'add_control': None, # (!) real value is "<method 'add_control' of 'panda3d.direct.CLerpAnimEffectInterval' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFDC68E61F0>)>'
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFDC68E61F0>)>'
    }


