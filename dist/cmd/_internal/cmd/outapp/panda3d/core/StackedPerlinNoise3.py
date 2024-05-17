# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


class StackedPerlinNoise3(__dtoolconfig.DTOOL_SUPER_BASE):
    """
    /**
     * Implements a multi-layer PerlinNoise, with one or more high-frequency noise
     * functions added to a lower-frequency base noise function.
     */
    """
    def addLevel(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_level(const StackedPerlinNoise3 self, const PerlinNoise3 level, double amp)
        
        /**
         * Adds an arbitrary PerlinNoise3 object, and an associated amplitude, to the
         * stack.
         */
        """
        pass

    def add_level(self, const_StackedPerlinNoise3_self, const_PerlinNoise3_level, double_amp): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_level(const StackedPerlinNoise3 self, const PerlinNoise3 level, double amp)
        
        /**
         * Adds an arbitrary PerlinNoise3 object, and an associated amplitude, to the
         * stack.
         */
        """
        pass

    def assign(self, const_StackedPerlinNoise3_self, const_StackedPerlinNoise3_copy): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        assign(const StackedPerlinNoise3 self, const StackedPerlinNoise3 copy)
        """
        pass

    def clear(self, const_StackedPerlinNoise3_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear(const StackedPerlinNoise3 self)
        
        /**
         * Removes all levels from the stack.  You must call add_level() again to
         * restore them.
         */
        """
        pass

    def noise(self, const_StackedPerlinNoise3_self, const_LVecBase3f_value): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        noise(const StackedPerlinNoise3 self, const LVecBase3f value)
        noise(const StackedPerlinNoise3 self, const LVecBase3d value)
        noise(const StackedPerlinNoise3 self, double x, double y, double z)
        
        /**
         * Returns the noise function of the three inputs.
         */
        
        /**
         * Returns the noise function of the three inputs.
         */
        
        /**
         * Returns the noise function of the three inputs.
         */
        """
        pass

    def __call__(self, *args, **kwargs): # real signature unknown
        """ Call self as a function. """
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
        '__call__': None, # (!) real value is "<slot wrapper '__call__' of 'panda3d.core.StackedPerlinNoise3' objects>"
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.core.StackedPerlinNoise3' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.core.StackedPerlinNoise3' objects>"
        '__doc__': '/**\n * Implements a multi-layer PerlinNoise, with one or more high-frequency noise\n * functions added to a lower-frequency base noise function.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.StackedPerlinNoise3' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE3433E0>'
        'addLevel': None, # (!) real value is "<method 'addLevel' of 'panda3d.core.StackedPerlinNoise3' objects>"
        'add_level': None, # (!) real value is "<method 'add_level' of 'panda3d.core.StackedPerlinNoise3' objects>"
        'assign': None, # (!) real value is "<method 'assign' of 'panda3d.core.StackedPerlinNoise3' objects>"
        'clear': None, # (!) real value is "<method 'clear' of 'panda3d.core.StackedPerlinNoise3' objects>"
        'noise': None, # (!) real value is "<method 'noise' of 'panda3d.core.StackedPerlinNoise3' objects>"
    }


