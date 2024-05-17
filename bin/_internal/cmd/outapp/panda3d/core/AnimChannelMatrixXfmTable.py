# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .AnimChannel_ACMatrixSwitchType import AnimChannel_ACMatrixSwitchType

class AnimChannelMatrixXfmTable(AnimChannel_ACMatrixSwitchType):
    """
    /**
     * An animation channel that issues a matrix each frame, read from a table
     * such as might have been read from an egg file.  The table actually consists
     * of nine sub-tables, each representing one component of the transform:
     * scale, rotate, translate.
     */
    """
    def clearAllTables(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_all_tables(const AnimChannelMatrixXfmTable self)
        
        /**
         * Removes all the tables from the channel, and resets it to its initial
         * state.
         */
        """
        pass

    def clearTable(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_table(const AnimChannelMatrixXfmTable self, char table_id)
        
        /**
         * Removes the indicated table from the definition.
         */
        """
        pass

    def clear_all_tables(self, const_AnimChannelMatrixXfmTable_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_all_tables(const AnimChannelMatrixXfmTable self)
        
        /**
         * Removes all the tables from the channel, and resets it to its initial
         * state.
         */
        """
        pass

    def clear_table(self, const_AnimChannelMatrixXfmTable_self, char_table_id): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_table(const AnimChannelMatrixXfmTable self, char table_id)
        
        /**
         * Removes the indicated table from the definition.
         */
        """
        pass

    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getTable(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_table(AnimChannelMatrixXfmTable self, char table_id)
        
        /**
         * Returns a pointer to the indicated subtable's data, if it exists, or NULL
         * if it does not.
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_table(self, AnimChannelMatrixXfmTable_self, char_table_id): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_table(AnimChannelMatrixXfmTable self, char table_id)
        
        /**
         * Returns a pointer to the indicated subtable's data, if it exists, or NULL
         * if it does not.
         */
        """
        pass

    def hasTable(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_table(AnimChannelMatrixXfmTable self, char table_id)
        
        /**
         * Returns true if the indicated subtable has been assigned.
         */
        """
        pass

    def has_table(self, AnimChannelMatrixXfmTable_self, char_table_id): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_table(AnimChannelMatrixXfmTable self, char table_id)
        
        /**
         * Returns true if the indicated subtable has been assigned.
         */
        """
        pass

    def isValidId(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_valid_id(char table_id)
        
        /**
         * Returns true if the given letter is one of the nine valid table id's.
         */
        """
        pass

    def is_valid_id(self, char_table_id): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_valid_id(char table_id)
        
        /**
         * Returns true if the given letter is one of the nine valid table id's.
         */
        """
        pass

    def setTable(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_table(const AnimChannelMatrixXfmTable self, char table_id, const ConstPointerToArray table)
        
        /**
         * Assigns the indicated table.  table_id is one of 'i', 'j', 'k', for scale,
         * 'a', 'b', 'c' for shear, 'h', 'p', 'r', for rotation, and 'x', 'y', 'z',
         * for translation.  The new table must have either zero, one, or
         * get_num_frames() frames.
         */
        """
        pass

    def set_table(self, const_AnimChannelMatrixXfmTable_self, char_table_id, const_ConstPointerToArray_table): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_table(const AnimChannelMatrixXfmTable self, char table_id, const ConstPointerToArray table)
        
        /**
         * Assigns the indicated table.  table_id is one of 'i', 'j', 'k', for scale,
         * 'a', 'b', 'c' for shear, 'h', 'p', 'r', for rotation, and 'x', 'y', 'z',
         * for translation.  The new table must have either zero, one, or
         * get_num_frames() frames.
         */
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    tables = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__doc__': '/**\n * An animation channel that issues a matrix each frame, read from a table\n * such as might have been read from an egg file.  The table actually consists\n * of nine sub-tables, each representing one component of the transform:\n * scale, rotate, translate.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.AnimChannelMatrixXfmTable' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE2C3AC0>'
        'clearAllTables': None, # (!) real value is "<method 'clearAllTables' of 'panda3d.core.AnimChannelMatrixXfmTable' objects>"
        'clearTable': None, # (!) real value is "<method 'clearTable' of 'panda3d.core.AnimChannelMatrixXfmTable' objects>"
        'clear_all_tables': None, # (!) real value is "<method 'clear_all_tables' of 'panda3d.core.AnimChannelMatrixXfmTable' objects>"
        'clear_table': None, # (!) real value is "<method 'clear_table' of 'panda3d.core.AnimChannelMatrixXfmTable' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE2C3AC0>)>'
        'getTable': None, # (!) real value is "<method 'getTable' of 'panda3d.core.AnimChannelMatrixXfmTable' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE2C3AC0>)>'
        'get_table': None, # (!) real value is "<method 'get_table' of 'panda3d.core.AnimChannelMatrixXfmTable' objects>"
        'hasTable': None, # (!) real value is "<method 'hasTable' of 'panda3d.core.AnimChannelMatrixXfmTable' objects>"
        'has_table': None, # (!) real value is "<method 'has_table' of 'panda3d.core.AnimChannelMatrixXfmTable' objects>"
        'isValidId': None, # (!) real value is '<staticmethod(<built-in method isValidId of type object at 0x00007FFCFE2C3AC0>)>'
        'is_valid_id': None, # (!) real value is '<staticmethod(<built-in method is_valid_id of type object at 0x00007FFCFE2C3AC0>)>'
        'setTable': None, # (!) real value is "<method 'setTable' of 'panda3d.core.AnimChannelMatrixXfmTable' objects>"
        'set_table': None, # (!) real value is "<method 'set_table' of 'panda3d.core.AnimChannelMatrixXfmTable' objects>"
        'tables': None, # (!) real value is "<attribute 'tables' of 'panda3d.core.AnimChannelMatrixXfmTable' objects>"
    }


