# encoding: utf-8
# module panda3d.egg
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\egg.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import panda3d.core as __panda3d_core


from .EggNode import EggNode

class EggAnimData(EggNode):
    """
    /**
     * A base class for EggSAnimData and EggXfmAnimData, which contain rows and
     * columns of numbers.
     */
    """
    def addData(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_data(const EggAnimData self, double value)
        
        /**
         * Adds a single element to the table.
         */
        """
        pass

    def add_data(self, const_EggAnimData_self, double_value): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_data(const EggAnimData self, double value)
        
        /**
         * Adds a single element to the table.
         */
        """
        pass

    def assign(self, const_EggAnimData_self, const_EggAnimData_copy): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        assign(const EggAnimData self, const EggAnimData copy)
        
        /**
         *
         */
        """
        pass

    def clearData(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_data(const EggAnimData self)
        
        /**
         * Removes all data and empties the table.
         */
        """
        pass

    def clearFps(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_fps(const EggAnimData self)
        
        /**
         *
         */
        """
        pass

    def clear_data(self, const_EggAnimData_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_data(const EggAnimData self)
        
        /**
         * Removes all data and empties the table.
         */
        """
        pass

    def clear_fps(self, const_EggAnimData_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_fps(const EggAnimData self)
        
        /**
         *
         */
        """
        pass

    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getFps(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_fps(EggAnimData self)
        
        /**
         * This is only valid if has_fps() returns true.
         */
        """
        pass

    def getSize(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_size(EggAnimData self)
        
        /**
         * Returns the number of elements in the table.
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_fps(self, EggAnimData_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_fps(EggAnimData self)
        
        /**
         * This is only valid if has_fps() returns true.
         */
        """
        pass

    def get_size(self, EggAnimData_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_size(EggAnimData self)
        
        /**
         * Returns the number of elements in the table.
         */
        """
        pass

    def hasFps(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_fps(EggAnimData self)
        
        /**
         *
         */
        """
        pass

    def has_fps(self, EggAnimData_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_fps(EggAnimData self)
        
        /**
         *
         */
        """
        pass

    def quantize(self, const_EggAnimData_self, double_quantum): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        quantize(const EggAnimData self, double quantum)
        
        /**
         * Rounds each element of the table to the nearest multiple of quantum.
         */
        """
        pass

    def setFps(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_fps(const EggAnimData self, double type)
        
        /**
         *
         */
        """
        pass

    def set_fps(self, const_EggAnimData_self, double_type): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_fps(const EggAnimData self, double type)
        
        /**
         *
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
        '__doc__': '/**\n * A base class for EggSAnimData and EggXfmAnimData, which contain rows and\n * columns of numbers.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.egg.EggAnimData' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFDC68CCEC0>'
        'addData': None, # (!) real value is "<method 'addData' of 'panda3d.egg.EggAnimData' objects>"
        'add_data': None, # (!) real value is "<method 'add_data' of 'panda3d.egg.EggAnimData' objects>"
        'assign': None, # (!) real value is "<method 'assign' of 'panda3d.egg.EggAnimData' objects>"
        'clearData': None, # (!) real value is "<method 'clearData' of 'panda3d.egg.EggAnimData' objects>"
        'clearFps': None, # (!) real value is "<method 'clearFps' of 'panda3d.egg.EggAnimData' objects>"
        'clear_data': None, # (!) real value is "<method 'clear_data' of 'panda3d.egg.EggAnimData' objects>"
        'clear_fps': None, # (!) real value is "<method 'clear_fps' of 'panda3d.egg.EggAnimData' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFDC68CCEC0>)>'
        'getFps': None, # (!) real value is "<method 'getFps' of 'panda3d.egg.EggAnimData' objects>"
        'getSize': None, # (!) real value is "<method 'getSize' of 'panda3d.egg.EggAnimData' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFDC68CCEC0>)>'
        'get_fps': None, # (!) real value is "<method 'get_fps' of 'panda3d.egg.EggAnimData' objects>"
        'get_size': None, # (!) real value is "<method 'get_size' of 'panda3d.egg.EggAnimData' objects>"
        'hasFps': None, # (!) real value is "<method 'hasFps' of 'panda3d.egg.EggAnimData' objects>"
        'has_fps': None, # (!) real value is "<method 'has_fps' of 'panda3d.egg.EggAnimData' objects>"
        'quantize': None, # (!) real value is "<method 'quantize' of 'panda3d.egg.EggAnimData' objects>"
        'setFps': None, # (!) real value is "<method 'setFps' of 'panda3d.egg.EggAnimData' objects>"
        'set_fps': None, # (!) real value is "<method 'set_fps' of 'panda3d.egg.EggAnimData' objects>"
    }


