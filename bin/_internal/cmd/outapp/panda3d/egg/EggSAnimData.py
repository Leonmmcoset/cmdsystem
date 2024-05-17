# encoding: utf-8
# module panda3d.egg
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\egg.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import panda3d.core as __panda3d_core


from .EggAnimData import EggAnimData

class EggSAnimData(EggAnimData):
    """
    /**
     * Corresponding to an <S$Anim> entry, this stores a single column of numbers,
     * for instance for a morph target, or as one column in an EggXfmSAnim.
     */
    """
    def assign(self, const_EggSAnimData_self, const_EggSAnimData_copy): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        assign(const EggSAnimData self, const EggSAnimData copy)
        
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

    def getNumRows(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_rows(EggSAnimData self)
        
        /**
         * Returns the number of rows in the table.  For an SAnim table, each row has
         * one column.
         */
        """
        pass

    def getValue(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_value(EggSAnimData self, int row)
        
        /**
         * Returns the value at the indicated row.  Row must be in the range 0 <= row
         * < get_num_rows().
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_num_rows(self, EggSAnimData_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_rows(EggSAnimData self)
        
        /**
         * Returns the number of rows in the table.  For an SAnim table, each row has
         * one column.
         */
        """
        pass

    def get_value(self, EggSAnimData_self, int_row): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_value(EggSAnimData self, int row)
        
        /**
         * Returns the value at the indicated row.  Row must be in the range 0 <= row
         * < get_num_rows().
         */
        """
        pass

    def optimize(self, const_EggSAnimData_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        optimize(const EggSAnimData self)
        
        /**
         * Optimizes the data by collapsing a long table of duplicate values into a
         * single value.
         */
        """
        pass

    def setValue(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_value(const EggSAnimData self, int row, double value)
        
        /**
         * Changes the value at the indicated row.  Row must be in the range 0 <= row
         * < get_num_rows().
         */
        """
        pass

    def set_value(self, const_EggSAnimData_self, int_row, double_value): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_value(const EggSAnimData self, int row, double value)
        
        /**
         * Changes the value at the indicated row.  Row must be in the range 0 <= row
         * < get_num_rows().
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
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.egg.EggSAnimData' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.egg.EggSAnimData' objects>"
        '__doc__': '/**\n * Corresponding to an <S$Anim> entry, this stores a single column of numbers,\n * for instance for a morph target, or as one column in an EggXfmSAnim.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.egg.EggSAnimData' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFDC68D1000>'
        'assign': None, # (!) real value is "<method 'assign' of 'panda3d.egg.EggSAnimData' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFDC68D1000>)>'
        'getNumRows': None, # (!) real value is "<method 'getNumRows' of 'panda3d.egg.EggSAnimData' objects>"
        'getValue': None, # (!) real value is "<method 'getValue' of 'panda3d.egg.EggSAnimData' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFDC68D1000>)>'
        'get_num_rows': None, # (!) real value is "<method 'get_num_rows' of 'panda3d.egg.EggSAnimData' objects>"
        'get_value': None, # (!) real value is "<method 'get_value' of 'panda3d.egg.EggSAnimData' objects>"
        'optimize': None, # (!) real value is "<method 'optimize' of 'panda3d.egg.EggSAnimData' objects>"
        'setValue': None, # (!) real value is "<method 'setValue' of 'panda3d.egg.EggSAnimData' objects>"
        'set_value': None, # (!) real value is "<method 'set_value' of 'panda3d.egg.EggSAnimData' objects>"
    }


