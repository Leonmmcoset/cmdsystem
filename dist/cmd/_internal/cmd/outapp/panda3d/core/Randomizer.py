# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


class Randomizer(__dtoolconfig.DTOOL_SUPER_BASE):
    """
    /**
     * A handy class to return random numbers.
     */
    """
    def assign(self, const_Randomizer_self, const_Randomizer_copy): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        assign(const Randomizer self, const Randomizer copy)
        """
        pass

    def getNextSeed(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_next_seed()
        
        /**
         * Returns a random seed value for the next global Randomizer object.
         */
        """
        pass

    def getSeed(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_seed(const Randomizer self)
        
        /**
         * Returns a unique seed value based on the seed value passed to this
         * Randomizer object (and on its current state).
         */
        """
        pass

    def get_next_seed(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_next_seed()
        
        /**
         * Returns a random seed value for the next global Randomizer object.
         */
        """
        pass

    def get_seed(self, const_Randomizer_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_seed(const Randomizer self)
        
        /**
         * Returns a unique seed value based on the seed value passed to this
         * Randomizer object (and on its current state).
         */
        """
        pass

    def randomInt(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        random_int(const Randomizer self, int range)
        
        /**
         * Returns a random integer in the range [0, range).
         */
        """
        pass

    def randomReal(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        random_real(const Randomizer self, double range)
        
        /**
         * Returns a random double in the range [0, range).
         */
        """
        pass

    def randomRealUnit(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        random_real_unit(const Randomizer self)
        
        /**
         * Returns a random double in the range [-0.5, 0.5).
         */
        """
        pass

    def random_int(self, const_Randomizer_self, int_range): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        random_int(const Randomizer self, int range)
        
        /**
         * Returns a random integer in the range [0, range).
         */
        """
        pass

    def random_real(self, const_Randomizer_self, double_range): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        random_real(const Randomizer self, double range)
        
        /**
         * Returns a random double in the range [0, range).
         */
        """
        pass

    def random_real_unit(self, const_Randomizer_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        random_real_unit(const Randomizer self)
        
        /**
         * Returns a random double in the range [-0.5, 0.5).
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

    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.core.Randomizer' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.core.Randomizer' objects>"
        '__doc__': '/**\n * A handy class to return random numbers.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.Randomizer' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE342AD0>'
        'assign': None, # (!) real value is "<method 'assign' of 'panda3d.core.Randomizer' objects>"
        'getNextSeed': None, # (!) real value is '<staticmethod(<built-in method getNextSeed of type object at 0x00007FFCFE342AD0>)>'
        'getSeed': None, # (!) real value is "<method 'getSeed' of 'panda3d.core.Randomizer' objects>"
        'get_next_seed': None, # (!) real value is '<staticmethod(<built-in method get_next_seed of type object at 0x00007FFCFE342AD0>)>'
        'get_seed': None, # (!) real value is "<method 'get_seed' of 'panda3d.core.Randomizer' objects>"
        'randomInt': None, # (!) real value is "<method 'randomInt' of 'panda3d.core.Randomizer' objects>"
        'randomReal': None, # (!) real value is "<method 'randomReal' of 'panda3d.core.Randomizer' objects>"
        'randomRealUnit': None, # (!) real value is "<method 'randomRealUnit' of 'panda3d.core.Randomizer' objects>"
        'random_int': None, # (!) real value is "<method 'random_int' of 'panda3d.core.Randomizer' objects>"
        'random_real': None, # (!) real value is "<method 'random_real' of 'panda3d.core.Randomizer' objects>"
        'random_real_unit': None, # (!) real value is "<method 'random_real_unit' of 'panda3d.core.Randomizer' objects>"
    }


