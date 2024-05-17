# encoding: utf-8
# module panda3d.direct
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\direct.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import panda3d.core as __panda3d_core


class DCPackData(__dtoolconfig.DTOOL_SUPER_BASE):
    """
    /**
     * This is a block of data that receives the results of DCPacker.
     */
    """
    def clear(self, const_DCPackData_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear(const DCPackData self)
        
        /**
         * Empties the contents of the data (without necessarily freeing its allocated
         * memory).
         */
        """
        pass

    def getLength(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_length(DCPackData self)
        
        /**
         * Returns the current length of the buffer.  This is the number of useful
         * bytes stored in the buffer, not the amount of memory it takes up.
         */
        """
        pass

    def getString(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_string(DCPackData self)
        
        /**
         * Returns the data buffer as a string.  Also see get_data().
         */
        """
        pass

    def get_length(self, DCPackData_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_length(DCPackData self)
        
        /**
         * Returns the current length of the buffer.  This is the number of useful
         * bytes stored in the buffer, not the amount of memory it takes up.
         */
        """
        pass

    def get_string(self, DCPackData_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_string(DCPackData self)
        
        /**
         * Returns the data buffer as a string.  Also see get_data().
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
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.direct.DCPackData' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.direct.DCPackData' objects>"
        '__doc__': '/**\n * This is a block of data that receives the results of DCPacker.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.direct.DCPackData' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFDC68DDCF0>'
        'clear': None, # (!) real value is "<method 'clear' of 'panda3d.direct.DCPackData' objects>"
        'getLength': None, # (!) real value is "<method 'getLength' of 'panda3d.direct.DCPackData' objects>"
        'getString': None, # (!) real value is "<method 'getString' of 'panda3d.direct.DCPackData' objects>"
        'get_length': None, # (!) real value is "<method 'get_length' of 'panda3d.direct.DCPackData' objects>"
        'get_string': None, # (!) real value is "<method 'get_string' of 'panda3d.direct.DCPackData' objects>"
    }


