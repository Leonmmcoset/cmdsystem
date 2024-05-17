# encoding: utf-8
# module panda3d.egg
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\egg.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import panda3d.core as __panda3d_core


from .EggGroupNode import EggGroupNode

class EggXfmSAnim(EggGroupNode):
    """
    /**
     * This corresponds to an <Xfm$Anim_S$> entry, which is a collection of up to
     * nine <S$Anim> entries that specify the nine components of a transformation.
     * It's implemented as a group that can contain any number of EggSAnimData
     * children.
     */
    """
    def addComponentData(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_component_data(const EggXfmSAnim self, str component_name, double value)
        add_component_data(const EggXfmSAnim self, int component, double value)
        
        /**
         * Adds a new row to the named component (one of matrix_component_letters) of
         * the table.
         */
        
        /**
         * Adds a new row to the indicated component (0-12) of the table.
         */
        """
        pass

    def addData(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_data(const EggXfmSAnim self, const LMatrix4d mat)
        
        /**
         * Adds a new matrix to the table, by adding a new row to each of the
         * subtables.
         *
         * This is a convenience function that treats the table of tables as if it
         * were a single table of matrices.  It is an error to call this if any
         * SAnimData children of this node have an improper name (e.g.  not a single
         * letter, or not one of "ijkabchprxyz").
         *
         * This function has the further requirement that all nine of the subtables
         * must exist and be of the same length.  Furthermore, the order string must
         * be the standard order string, which matches the system compose_matrix() and
         * decompose_matrix() functions.
         *
         * Thus, you probably cannot take an existing EggXfmSAnim object and start
         * adding matrices to the end; you must clear out the original data first.
         * (As a special exception, if no tables exist, they will be created.)  The
         * method normalize() will do this for you on an existing EggXfmSAnim.
         *
         * This function may fail silently if the matrix cannot be decomposed into
         * scale, shear, rotate, and translate.  In this case, the closest
         * approximation is added to the table, and false is returned.
         */
        """
        pass

    def add_component_data(self, const_EggXfmSAnim_self, str_component_name, double_value): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_component_data(const EggXfmSAnim self, str component_name, double value)
        add_component_data(const EggXfmSAnim self, int component, double value)
        
        /**
         * Adds a new row to the named component (one of matrix_component_letters) of
         * the table.
         */
        
        /**
         * Adds a new row to the indicated component (0-12) of the table.
         */
        """
        pass

    def add_data(self, const_EggXfmSAnim_self, const_LMatrix4d_mat): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_data(const EggXfmSAnim self, const LMatrix4d mat)
        
        /**
         * Adds a new matrix to the table, by adding a new row to each of the
         * subtables.
         *
         * This is a convenience function that treats the table of tables as if it
         * were a single table of matrices.  It is an error to call this if any
         * SAnimData children of this node have an improper name (e.g.  not a single
         * letter, or not one of "ijkabchprxyz").
         *
         * This function has the further requirement that all nine of the subtables
         * must exist and be of the same length.  Furthermore, the order string must
         * be the standard order string, which matches the system compose_matrix() and
         * decompose_matrix() functions.
         *
         * Thus, you probably cannot take an existing EggXfmSAnim object and start
         * adding matrices to the end; you must clear out the original data first.
         * (As a special exception, if no tables exist, they will be created.)  The
         * method normalize() will do this for you on an existing EggXfmSAnim.
         *
         * This function may fail silently if the matrix cannot be decomposed into
         * scale, shear, rotate, and translate.  In this case, the closest
         * approximation is added to the table, and false is returned.
         */
        """
        pass

    def assign(self, const_EggXfmSAnim_self, const_EggXfmSAnim_copy): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        assign(const EggXfmSAnim self, const EggXfmSAnim copy)
        
        /**
         *
         */
        """
        pass

    def clearData(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_data(const EggXfmSAnim self)
        
        /**
         * Removes all data from the table.  It does this by removing all of its
         * children.
         */
        """
        pass

    def clearFps(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_fps(const EggXfmSAnim self)
        
        /**
         *
         */
        """
        pass

    def clearOrder(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_order(const EggXfmSAnim self)
        
        /**
         *
         */
        """
        pass

    def clear_data(self, const_EggXfmSAnim_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_data(const EggXfmSAnim self)
        
        /**
         * Removes all data from the table.  It does this by removing all of its
         * children.
         */
        """
        pass

    def clear_fps(self, const_EggXfmSAnim_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_fps(const EggXfmSAnim self)
        
        /**
         *
         */
        """
        pass

    def clear_order(self, const_EggXfmSAnim_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_order(const EggXfmSAnim self)
        
        /**
         *
         */
        """
        pass

    def composeWithOrder(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        compose_with_order(LMatrix4d mat, const LVecBase3d scale, const LVecBase3d shear, const LVecBase3d hpr, const LVecBase3d trans, str order, int cs)
        
        /**
         * Composes a matrix out of the nine individual components, respecting the
         * order string.  The components will be applied in the order indicated by the
         * string.
         */
        """
        pass

    def compose_with_order(self, LMatrix4d_mat, const_LVecBase3d_scale, const_LVecBase3d_shear, const_LVecBase3d_hpr, const_LVecBase3d_trans, str_order, int_cs): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        compose_with_order(LMatrix4d mat, const LVecBase3d scale, const LVecBase3d shear, const LVecBase3d hpr, const LVecBase3d trans, str order, int cs)
        
        /**
         * Composes a matrix out of the nine individual components, respecting the
         * order string.  The components will be applied in the order indicated by the
         * string.
         */
        """
        pass

    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getCoordinateSystem(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_coordinate_system(EggXfmSAnim self)
        
        /**
         * Returns the coordinate system this table believes it is defined within.
         * This should always match the coordinate system of the EggData structure
         * that owns it.  It is necessary to store it here because the meaning of the
         * h, p, and r columns depends on the coordinate system.
         */
        """
        pass

    def getFps(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_fps(EggXfmSAnim self)
        
        /**
         * This is only valid if has_fps() returns true.
         */
        """
        pass

    def getNumRows(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_rows(EggXfmSAnim self)
        
        /**
         * Returns the effective number of rows in the table.  This is actually the
         * number of rows of the smallest subtable larger than one row.  This is a
         * convenience function that treats the table of tables as if it were a single
         * table of matrices.
         */
        """
        pass

    def getOrder(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_order(EggXfmSAnim self)
        
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
        get_value(EggXfmSAnim self, int row, LMatrix4d mat)
        
        /**
         * Returns the value of the aggregate row of the table as a matrix.  This is a
         * convenience function that treats the table of tables as if it were a single
         * table of matrices.  It is an error to call this if any SAnimData children
         * of this node have an improper name (e.g.  not a single letter, or not one
         * of "ijkabchprxyz").
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_coordinate_system(self, EggXfmSAnim_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_coordinate_system(EggXfmSAnim self)
        
        /**
         * Returns the coordinate system this table believes it is defined within.
         * This should always match the coordinate system of the EggData structure
         * that owns it.  It is necessary to store it here because the meaning of the
         * h, p, and r columns depends on the coordinate system.
         */
        """
        pass

    def get_fps(self, EggXfmSAnim_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_fps(EggXfmSAnim self)
        
        /**
         * This is only valid if has_fps() returns true.
         */
        """
        pass

    def get_num_rows(self, EggXfmSAnim_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_rows(EggXfmSAnim self)
        
        /**
         * Returns the effective number of rows in the table.  This is actually the
         * number of rows of the smallest subtable larger than one row.  This is a
         * convenience function that treats the table of tables as if it were a single
         * table of matrices.
         */
        """
        pass

    def get_order(self, EggXfmSAnim_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_order(EggXfmSAnim self)
        
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

    def get_value(self, EggXfmSAnim_self, int_row, LMatrix4d_mat): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_value(EggXfmSAnim self, int row, LMatrix4d mat)
        
        /**
         * Returns the value of the aggregate row of the table as a matrix.  This is a
         * convenience function that treats the table of tables as if it were a single
         * table of matrices.  It is an error to call this if any SAnimData children
         * of this node have an improper name (e.g.  not a single letter, or not one
         * of "ijkabchprxyz").
         */
        """
        pass

    def hasFps(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_fps(EggXfmSAnim self)
        
        /**
         *
         */
        """
        pass

    def hasOrder(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_order(EggXfmSAnim self)
        
        /**
         *
         */
        """
        pass

    def has_fps(self, EggXfmSAnim_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_fps(EggXfmSAnim self)
        
        /**
         *
         */
        """
        pass

    def has_order(self, EggXfmSAnim_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_order(EggXfmSAnim self)
        
        /**
         *
         */
        """
        pass

    def normalize(self, const_EggXfmSAnim_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        normalize(const EggXfmSAnim self)
        
        /**
         * The inverse operation of optimize(), this ensures that all the sub-tables
         * have the same length by duplicating rows as necessary.  This is needed
         * before doing operations like add_data() or set_value() on an existing
         * table.
         */
        """
        pass

    def optimize(self, const_EggXfmSAnim_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        optimize(const EggXfmSAnim self)
        
        /**
         * Optimizes the table by collapsing redundant sub-tables.
         */
        """
        pass

    def optimizeToStandardOrder(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        optimize_to_standard_order(const EggXfmSAnim self)
        
        /**
         * Optimizes the table by collapsing redundant sub-tables, and simultaneously
         * ensures that the order string is the standard order (which is the same as
         * that supported by compose_matrix() and decompose_matrix()).
         */
        """
        pass

    def optimize_to_standard_order(self, const_EggXfmSAnim_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        optimize_to_standard_order(const EggXfmSAnim self)
        
        /**
         * Optimizes the table by collapsing redundant sub-tables, and simultaneously
         * ensures that the order string is the standard order (which is the same as
         * that supported by compose_matrix() and decompose_matrix()).
         */
        """
        pass

    def setFps(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_fps(const EggXfmSAnim self, double fps)
        
        /**
         *
         */
        """
        pass

    def setOrder(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_order(const EggXfmSAnim self, str order)
        
        /**
         *
         */
        """
        pass

    def setValue(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_value(const EggXfmSAnim self, int row, const LMatrix4d mat)
        
        /**
         * Replaces the indicated row of the table with the given matrix.
         *
         * This function can only be called if all the constraints of add_data(),
         * below, are met.  Call normalize() first if you are not sure.
         *
         * The return value is true if the matrix can be decomposed and stored as
         * scale, shear, rotate, and translate, or false otherwise.  The data is set
         * in either case.
         */
        """
        pass

    def set_fps(self, const_EggXfmSAnim_self, double_fps): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_fps(const EggXfmSAnim self, double fps)
        
        /**
         *
         */
        """
        pass

    def set_order(self, const_EggXfmSAnim_self, str_order): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_order(const EggXfmSAnim self, str order)
        
        /**
         *
         */
        """
        pass

    def set_value(self, const_EggXfmSAnim_self, int_row, const_LMatrix4d_mat): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_value(const EggXfmSAnim self, int row, const LMatrix4d mat)
        
        /**
         * Replaces the indicated row of the table with the given matrix.
         *
         * This function can only be called if all the constraints of add_data(),
         * below, are met.  Call normalize() first if you are not sure.
         *
         * The return value is true if the matrix can be decomposed and stored as
         * scale, shear, rotate, and translate, or false otherwise.  The data is set
         * in either case.
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
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.egg.EggXfmSAnim' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.egg.EggXfmSAnim' objects>"
        '__doc__': "/**\n * This corresponds to an <Xfm$Anim_S$> entry, which is a collection of up to\n * nine <S$Anim> entries that specify the nine components of a transformation.\n * It's implemented as a group that can contain any number of EggSAnimData\n * children.\n */",
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.egg.EggXfmSAnim' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFDC68D1910>'
        'addComponentData': None, # (!) real value is "<method 'addComponentData' of 'panda3d.egg.EggXfmSAnim' objects>"
        'addData': None, # (!) real value is "<method 'addData' of 'panda3d.egg.EggXfmSAnim' objects>"
        'add_component_data': None, # (!) real value is "<method 'add_component_data' of 'panda3d.egg.EggXfmSAnim' objects>"
        'add_data': None, # (!) real value is "<method 'add_data' of 'panda3d.egg.EggXfmSAnim' objects>"
        'assign': None, # (!) real value is "<method 'assign' of 'panda3d.egg.EggXfmSAnim' objects>"
        'clearData': None, # (!) real value is "<method 'clearData' of 'panda3d.egg.EggXfmSAnim' objects>"
        'clearFps': None, # (!) real value is "<method 'clearFps' of 'panda3d.egg.EggXfmSAnim' objects>"
        'clearOrder': None, # (!) real value is "<method 'clearOrder' of 'panda3d.egg.EggXfmSAnim' objects>"
        'clear_data': None, # (!) real value is "<method 'clear_data' of 'panda3d.egg.EggXfmSAnim' objects>"
        'clear_fps': None, # (!) real value is "<method 'clear_fps' of 'panda3d.egg.EggXfmSAnim' objects>"
        'clear_order': None, # (!) real value is "<method 'clear_order' of 'panda3d.egg.EggXfmSAnim' objects>"
        'composeWithOrder': None, # (!) real value is '<staticmethod(<built-in method composeWithOrder of type object at 0x00007FFDC68D1910>)>'
        'compose_with_order': None, # (!) real value is '<staticmethod(<built-in method compose_with_order of type object at 0x00007FFDC68D1910>)>'
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFDC68D1910>)>'
        'getCoordinateSystem': None, # (!) real value is "<method 'getCoordinateSystem' of 'panda3d.egg.EggXfmSAnim' objects>"
        'getFps': None, # (!) real value is "<method 'getFps' of 'panda3d.egg.EggXfmSAnim' objects>"
        'getNumRows': None, # (!) real value is "<method 'getNumRows' of 'panda3d.egg.EggXfmSAnim' objects>"
        'getOrder': None, # (!) real value is "<method 'getOrder' of 'panda3d.egg.EggXfmSAnim' objects>"
        'getStandardOrder': None, # (!) real value is '<staticmethod(<built-in method getStandardOrder of type object at 0x00007FFDC68D1910>)>'
        'getValue': None, # (!) real value is "<method 'getValue' of 'panda3d.egg.EggXfmSAnim' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFDC68D1910>)>'
        'get_coordinate_system': None, # (!) real value is "<method 'get_coordinate_system' of 'panda3d.egg.EggXfmSAnim' objects>"
        'get_fps': None, # (!) real value is "<method 'get_fps' of 'panda3d.egg.EggXfmSAnim' objects>"
        'get_num_rows': None, # (!) real value is "<method 'get_num_rows' of 'panda3d.egg.EggXfmSAnim' objects>"
        'get_order': None, # (!) real value is "<method 'get_order' of 'panda3d.egg.EggXfmSAnim' objects>"
        'get_standard_order': None, # (!) real value is '<staticmethod(<built-in method get_standard_order of type object at 0x00007FFDC68D1910>)>'
        'get_value': None, # (!) real value is "<method 'get_value' of 'panda3d.egg.EggXfmSAnim' objects>"
        'hasFps': None, # (!) real value is "<method 'hasFps' of 'panda3d.egg.EggXfmSAnim' objects>"
        'hasOrder': None, # (!) real value is "<method 'hasOrder' of 'panda3d.egg.EggXfmSAnim' objects>"
        'has_fps': None, # (!) real value is "<method 'has_fps' of 'panda3d.egg.EggXfmSAnim' objects>"
        'has_order': None, # (!) real value is "<method 'has_order' of 'panda3d.egg.EggXfmSAnim' objects>"
        'normalize': None, # (!) real value is "<method 'normalize' of 'panda3d.egg.EggXfmSAnim' objects>"
        'optimize': None, # (!) real value is "<method 'optimize' of 'panda3d.egg.EggXfmSAnim' objects>"
        'optimizeToStandardOrder': None, # (!) real value is "<method 'optimizeToStandardOrder' of 'panda3d.egg.EggXfmSAnim' objects>"
        'optimize_to_standard_order': None, # (!) real value is "<method 'optimize_to_standard_order' of 'panda3d.egg.EggXfmSAnim' objects>"
        'setFps': None, # (!) real value is "<method 'setFps' of 'panda3d.egg.EggXfmSAnim' objects>"
        'setOrder': None, # (!) real value is "<method 'setOrder' of 'panda3d.egg.EggXfmSAnim' objects>"
        'setValue': None, # (!) real value is "<method 'setValue' of 'panda3d.egg.EggXfmSAnim' objects>"
        'set_fps': None, # (!) real value is "<method 'set_fps' of 'panda3d.egg.EggXfmSAnim' objects>"
        'set_order': None, # (!) real value is "<method 'set_order' of 'panda3d.egg.EggXfmSAnim' objects>"
        'set_value': None, # (!) real value is "<method 'set_value' of 'panda3d.egg.EggXfmSAnim' objects>"
    }


