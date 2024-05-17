# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .AnimChannel_ACScalarSwitchType import AnimChannel_ACScalarSwitchType

class AnimChannelScalarTable(AnimChannel_ACScalarSwitchType):
    """
    /**
     * An animation channel that issues a scalar each frame, read from a table
     * such as might have been read from an egg file.
     */
    """
    def clearTable(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_table(const AnimChannelScalarTable self)
        
        /**
         * Empties the data table.
         */
        """
        pass

    def clear_table(self, const_AnimChannelScalarTable_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_table(const AnimChannelScalarTable self)
        
        /**
         * Empties the data table.
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
        get_table(AnimChannelScalarTable self)
        
        /**
         * Returns a pointer to the table's data, if it exists, or NULL if it does
         * not.
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_table(self, AnimChannelScalarTable_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_table(AnimChannelScalarTable self)
        
        /**
         * Returns a pointer to the table's data, if it exists, or NULL if it does
         * not.
         */
        """
        pass

    def hasTable(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_table(AnimChannelScalarTable self)
        
        /**
         * Returns true if the data table has been assigned.
         */
        """
        pass

    def has_table(self, AnimChannelScalarTable_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_table(AnimChannelScalarTable self)
        
        /**
         * Returns true if the data table has been assigned.
         */
        """
        pass

    def setTable(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_table(const AnimChannelScalarTable self, const ConstPointerToArray table)
        
        /**
         * Assigns the data table.
         */
        """
        pass

    def set_table(self, const_AnimChannelScalarTable_self, const_ConstPointerToArray_table): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_table(const AnimChannelScalarTable self, const ConstPointerToArray table)
        
        /**
         * Assigns the data table.
         */
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    table = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__doc__': '/**\n * An animation channel that issues a scalar each frame, read from a table\n * such as might have been read from an egg file.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.AnimChannelScalarTable' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE2C3E60>'
        'clearTable': None, # (!) real value is "<method 'clearTable' of 'panda3d.core.AnimChannelScalarTable' objects>"
        'clear_table': None, # (!) real value is "<method 'clear_table' of 'panda3d.core.AnimChannelScalarTable' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE2C3E60>)>'
        'getTable': None, # (!) real value is "<method 'getTable' of 'panda3d.core.AnimChannelScalarTable' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE2C3E60>)>'
        'get_table': None, # (!) real value is "<method 'get_table' of 'panda3d.core.AnimChannelScalarTable' objects>"
        'hasTable': None, # (!) real value is "<method 'hasTable' of 'panda3d.core.AnimChannelScalarTable' objects>"
        'has_table': None, # (!) real value is "<method 'has_table' of 'panda3d.core.AnimChannelScalarTable' objects>"
        'setTable': None, # (!) real value is "<method 'setTable' of 'panda3d.core.AnimChannelScalarTable' objects>"
        'set_table': None, # (!) real value is "<method 'set_table' of 'panda3d.core.AnimChannelScalarTable' objects>"
        'table': None, # (!) real value is "<attribute 'table' of 'panda3d.core.AnimChannelScalarTable' objects>"
    }


