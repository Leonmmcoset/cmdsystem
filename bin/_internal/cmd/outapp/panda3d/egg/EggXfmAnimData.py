# encoding: utf-8
# module panda3d.egg
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\egg.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import panda3d.core as __panda3d_core


from .EggAnimData import EggAnimData

class EggXfmAnimData(EggAnimData):
    """
    /**
     * Corresponding to an <Xfm$Anim> entry, this stores a two-dimensional table
     * with up to nine columns, one for each component of a transformation.  This
     * is an older syntax of egg anim table, not often used currently--it's
     * replaced by EggXfmSAnim.
     */
    """
    def assign(self, const_EggXfmAnimData_self, const_EggXfmAnimData_copy): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        assign(const EggXfmAnimData self, const EggXfmAnimData copy)
        
        /**
         *
         */
        """
        pass

    def clearContents(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_contents(const EggXfmAnimData self)
        
        /**
         *
         */
        """
        pass

    def clearOrder(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_order(const EggXfmAnimData self)
        
        /**
         *
         */
        """
        pass

    def clear_contents(self, const_EggXfmAnimData_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_contents(const EggXfmAnimData self)
        
        /**
         *
         */
        """
        pass

    def clear_order(self, const_EggXfmAnimData_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_order(const EggXfmAnimData self)
        
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

    def getContents(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_contents(EggXfmAnimData self)
        
        /**
         *
         */
        """
        pass

    def getCoordinateSystem(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_coordinate_system(EggXfmAnimData self)
        
        /**
         * Returns the coordinate system this table believes it is defined within.
         * This should always match the coordinate system of the EggData structure
         * that owns it.  It is necessary to store it here because the meaning of the
         * h, p, and r columns depends on the coordinate system.
         */
        """
        pass

    def getNumCols(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_cols(EggXfmAnimData self)
        
        /**
         * Returns the number of columns in the table.  This is set according to the
         * "contents" string, which defines the meaning of each column.
         */
        """
        pass

    def getNumRows(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_rows(EggXfmAnimData self)
        
        /**
         * Returns the number of rows in the table.
         */
        """
        pass

    def getOrder(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_order(EggXfmAnimData self)
        
        /**
         *
         */
        """
        pass

    def getStandardOrder(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_standard_order()
        
        /**
         * Returns the standard order of matrix component composition.  This is what
         * the order string must be set to in order to use set_value() or add_data()
         * successfully.
         */
        """
        pass

    def getValue(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_value(EggXfmAnimData self, int row, LMatrix4d mat)
        get_value(EggXfmAnimData self, int row, int col)
        
        /**
         * Returns the value at the indicated row.  Row must be in the range 0 <= row
         * < get_num_rows(); col must be in the range 0 <= col < get_num_cols().
         */
        
        /**
         * Returns the value of the aggregate row of the table as a matrix.  This is a
         * convenience function that treats the 2-d table as if it were a single table
         * of matrices.
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_contents(self, EggXfmAnimData_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_contents(EggXfmAnimData self)
        
        /**
         *
         */
        """
        pass

    def get_coordinate_system(self, EggXfmAnimData_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_coordinate_system(EggXfmAnimData self)
        
        /**
         * Returns the coordinate system this table believes it is defined within.
         * This should always match the coordinate system of the EggData structure
         * that owns it.  It is necessary to store it here because the meaning of the
         * h, p, and r columns depends on the coordinate system.
         */
        """
        pass

    def get_num_cols(self, EggXfmAnimData_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_cols(EggXfmAnimData self)
        
        /**
         * Returns the number of columns in the table.  This is set according to the
         * "contents" string, which defines the meaning of each column.
         */
        """
        pass

    def get_num_rows(self, EggXfmAnimData_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_rows(EggXfmAnimData self)
        
        /**
         * Returns the number of rows in the table.
         */
        """
        pass

    def get_order(self, EggXfmAnimData_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_order(EggXfmAnimData self)
        
        /**
         *
         */
        """
        pass

    def get_standard_order(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_standard_order()
        
        /**
         * Returns the standard order of matrix component composition.  This is what
         * the order string must be set to in order to use set_value() or add_data()
         * successfully.
         */
        """
        pass

    def get_value(self, EggXfmAnimData_self, int_row, LMatrix4d_mat): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_value(EggXfmAnimData self, int row, LMatrix4d mat)
        get_value(EggXfmAnimData self, int row, int col)
        
        /**
         * Returns the value at the indicated row.  Row must be in the range 0 <= row
         * < get_num_rows(); col must be in the range 0 <= col < get_num_cols().
         */
        
        /**
         * Returns the value of the aggregate row of the table as a matrix.  This is a
         * convenience function that treats the 2-d table as if it were a single table
         * of matrices.
         */
        """
        pass

    def hasContents(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_contents(EggXfmAnimData self)
        
        /**
         *
         */
        """
        pass

    def hasOrder(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_order(EggXfmAnimData self)
        
        /**
         *
         */
        """
        pass

    def has_contents(self, EggXfmAnimData_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_contents(EggXfmAnimData self)
        
        /**
         *
         */
        """
        pass

    def has_order(self, EggXfmAnimData_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_order(EggXfmAnimData self)
        
        /**
         *
         */
        """
        pass

    def setContents(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_contents(const EggXfmAnimData self, str contents)
        
        /**
         *
         */
        """
        pass

    def setOrder(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_order(const EggXfmAnimData self, str order)
        
        /**
         *
         */
        """
        pass

    def set_contents(self, const_EggXfmAnimData_self, str_contents): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_contents(const EggXfmAnimData self, str contents)
        
        /**
         *
         */
        """
        pass

    def set_order(self, const_EggXfmAnimData_self, str_order): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_order(const EggXfmAnimData self, str order)
        
        /**
         *
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
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.egg.EggXfmAnimData' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.egg.EggXfmAnimData' objects>"
        '__doc__': "/**\n * Corresponding to an <Xfm$Anim> entry, this stores a two-dimensional table\n * with up to nine columns, one for each component of a transformation.  This\n * is an older syntax of egg anim table, not often used currently--it's\n * replaced by EggXfmSAnim.\n */",
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.egg.EggXfmAnimData' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFDC68D1AE0>'
        'assign': None, # (!) real value is "<method 'assign' of 'panda3d.egg.EggXfmAnimData' objects>"
        'clearContents': None, # (!) real value is "<method 'clearContents' of 'panda3d.egg.EggXfmAnimData' objects>"
        'clearOrder': None, # (!) real value is "<method 'clearOrder' of 'panda3d.egg.EggXfmAnimData' objects>"
        'clear_contents': None, # (!) real value is "<method 'clear_contents' of 'panda3d.egg.EggXfmAnimData' objects>"
        'clear_order': None, # (!) real value is "<method 'clear_order' of 'panda3d.egg.EggXfmAnimData' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFDC68D1AE0>)>'
        'getContents': None, # (!) real value is "<method 'getContents' of 'panda3d.egg.EggXfmAnimData' objects>"
        'getCoordinateSystem': None, # (!) real value is "<method 'getCoordinateSystem' of 'panda3d.egg.EggXfmAnimData' objects>"
        'getNumCols': None, # (!) real value is "<method 'getNumCols' of 'panda3d.egg.EggXfmAnimData' objects>"
        'getNumRows': None, # (!) real value is "<method 'getNumRows' of 'panda3d.egg.EggXfmAnimData' objects>"
        'getOrder': None, # (!) real value is "<method 'getOrder' of 'panda3d.egg.EggXfmAnimData' objects>"
        'getStandardOrder': None, # (!) real value is '<staticmethod(<built-in method getStandardOrder of type object at 0x00007FFDC68D1AE0>)>'
        'getValue': None, # (!) real value is "<method 'getValue' of 'panda3d.egg.EggXfmAnimData' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFDC68D1AE0>)>'
        'get_contents': None, # (!) real value is "<method 'get_contents' of 'panda3d.egg.EggXfmAnimData' objects>"
        'get_coordinate_system': None, # (!) real value is "<method 'get_coordinate_system' of 'panda3d.egg.EggXfmAnimData' objects>"
        'get_num_cols': None, # (!) real value is "<method 'get_num_cols' of 'panda3d.egg.EggXfmAnimData' objects>"
        'get_num_rows': None, # (!) real value is "<method 'get_num_rows' of 'panda3d.egg.EggXfmAnimData' objects>"
        'get_order': None, # (!) real value is "<method 'get_order' of 'panda3d.egg.EggXfmAnimData' objects>"
        'get_standard_order': None, # (!) real value is '<staticmethod(<built-in method get_standard_order of type object at 0x00007FFDC68D1AE0>)>'
        'get_value': None, # (!) real value is "<method 'get_value' of 'panda3d.egg.EggXfmAnimData' objects>"
        'hasContents': None, # (!) real value is "<method 'hasContents' of 'panda3d.egg.EggXfmAnimData' objects>"
        'hasOrder': None, # (!) real value is "<method 'hasOrder' of 'panda3d.egg.EggXfmAnimData' objects>"
        'has_contents': None, # (!) real value is "<method 'has_contents' of 'panda3d.egg.EggXfmAnimData' objects>"
        'has_order': None, # (!) real value is "<method 'has_order' of 'panda3d.egg.EggXfmAnimData' objects>"
        'setContents': None, # (!) real value is "<method 'setContents' of 'panda3d.egg.EggXfmAnimData' objects>"
        'setOrder': None, # (!) real value is "<method 'setOrder' of 'panda3d.egg.EggXfmAnimData' objects>"
        'set_contents': None, # (!) real value is "<method 'set_contents' of 'panda3d.egg.EggXfmAnimData' objects>"
        'set_order': None, # (!) real value is "<method 'set_order' of 'panda3d.egg.EggXfmAnimData' objects>"
    }


