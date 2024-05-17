# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


class PerlinNoise(__dtoolconfig.DTOOL_SUPER_BASE):
    """
    /**
     * This is the base class for PerlinNoise2 and PerlinNoise3, different
     * dimensions of Perlin noise implementation.  The base class just collects
     * the common functionality.
     */
    """
    def getSeed(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_seed(const PerlinNoise self)
        
        /**
         * Returns a unique seed value based on the seed value passed to this
         * PerlinNoise object (and on its current state).
         */
        """
        pass

    def get_seed(self, const_PerlinNoise_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_seed(const PerlinNoise self)
        
        /**
         * Returns a unique seed value based on the seed value passed to this
         * PerlinNoise object (and on its current state).
         */
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
        '__doc__': '/**\n * This is the base class for PerlinNoise2 and PerlinNoise3, different\n * dimensions of Perlin noise implementation.  The base class just collects\n * the common functionality.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.PerlinNoise' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE342CA0>'
        'getSeed': None, # (!) real value is "<method 'getSeed' of 'panda3d.core.PerlinNoise' objects>"
        'get_seed': None, # (!) real value is "<method 'get_seed' of 'panda3d.core.PerlinNoise' objects>"
    }


