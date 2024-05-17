# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .PerlinNoise import PerlinNoise

class PerlinNoise3(PerlinNoise):
    """
    /**
     * This class provides an implementation of Perlin noise for 3 variables.
     * This code is loosely based on the reference implementation at
     * http://mrl.nyu.edu/~perlin/noise/ .
     */
    """
    def assign(self, const_PerlinNoise3_self, const_PerlinNoise3_copy): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        assign(const PerlinNoise3 self, const PerlinNoise3 copy)
        """
        pass

    def noise(self, PerlinNoise3_self, const_LVecBase3d_value): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        noise(PerlinNoise3 self, const LVecBase3d value)
        noise(PerlinNoise3 self, const LVecBase3f value)
        noise(PerlinNoise3 self, double x, double y, double z)
        
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

    def setScale(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_scale(const PerlinNoise3 self, const LVecBase3f scale)
        set_scale(const PerlinNoise3 self, const LVecBase3d scale)
        set_scale(const PerlinNoise3 self, double scale)
        set_scale(const PerlinNoise3 self, double sx, double sy, double sz)
        
        /**
         * Changes the scale (frequency) of the noise.
         */
        
        /**
         * Changes the scale (frequency) of the noise.
         */
        
        /**
         * Changes the scale (frequency) of the noise.
         */
        
        /**
         * Changes the scale (frequency) of the noise.
         */
        """
        pass

    def set_scale(self, const_PerlinNoise3_self, const_LVecBase3f_scale): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_scale(const PerlinNoise3 self, const LVecBase3f scale)
        set_scale(const PerlinNoise3 self, const LVecBase3d scale)
        set_scale(const PerlinNoise3 self, double scale)
        set_scale(const PerlinNoise3 self, double sx, double sy, double sz)
        
        /**
         * Changes the scale (frequency) of the noise.
         */
        
        /**
         * Changes the scale (frequency) of the noise.
         */
        
        /**
         * Changes the scale (frequency) of the noise.
         */
        
        /**
         * Changes the scale (frequency) of the noise.
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
        '__call__': None, # (!) real value is "<slot wrapper '__call__' of 'panda3d.core.PerlinNoise3' objects>"
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.core.PerlinNoise3' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.core.PerlinNoise3' objects>"
        '__doc__': '/**\n * This class provides an implementation of Perlin noise for 3 variables.\n * This code is loosely based on the reference implementation at\n * http://mrl.nyu.edu/~perlin/noise/ .\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.PerlinNoise3' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE343040>'
        'assign': None, # (!) real value is "<method 'assign' of 'panda3d.core.PerlinNoise3' objects>"
        'noise': None, # (!) real value is "<method 'noise' of 'panda3d.core.PerlinNoise3' objects>"
        'setScale': None, # (!) real value is "<method 'setScale' of 'panda3d.core.PerlinNoise3' objects>"
        'set_scale': None, # (!) real value is "<method 'set_scale' of 'panda3d.core.PerlinNoise3' objects>"
    }


