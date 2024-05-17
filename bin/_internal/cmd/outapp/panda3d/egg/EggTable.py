# encoding: utf-8
# module panda3d.egg
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\egg.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import panda3d.core as __panda3d_core


from .EggGroupNode import EggGroupNode

class EggTable(EggGroupNode):
    """
    /**
     * This corresponds to a <Table> or a <Bundle> entry.  As such, it doesn't
     * actually contain a table of numbers, but it may be a parent to an
     * EggSAnimData or an EggXfmAnimData, which do.  It may also be a parent to
     * another <Table> or <Bundle>, establishing a hierarchy of tables.
     */
    """
    def assign(self, const_EggTable_self, const_EggTable_copy): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        assign(const EggTable self, const EggTable copy)
        
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

    def getTableType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_table_type(EggTable self)
        
        /**
         *
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_table_type(self, EggTable_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_table_type(EggTable self)
        
        /**
         *
         */
        """
        pass

    def hasTransform(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_transform(EggTable self)
        
        /**
         * Returns true if the table contains a transform description, false
         * otherwise.
         */
        """
        pass

    def has_transform(self, EggTable_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_transform(EggTable self)
        
        /**
         * Returns true if the table contains a transform description, false
         * otherwise.
         */
        """
        pass

    def setTableType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_table_type(const EggTable self, int type)
        
        /**
         *
         */
        """
        pass

    def set_table_type(self, const_EggTable_self, int_type): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_table_type(const EggTable self, int type)
        
        /**
         *
         */
        """
        pass

    def stringTableType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        string_table_type(str string)
        
        /**
         * Returns the TableType value associated with the given string
         * representation, or TT_invalid if the string does not match any known
         * TableType value.
         */
        """
        pass

    def string_table_type(self, str_string): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        string_table_type(str string)
        
        /**
         * Returns the TableType value associated with the given string
         * representation, or TT_invalid if the string does not match any known
         * TableType value.
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
        'TTBundle': 2,
        'TTInvalid': 0,
        'TTTable': 1,
        'TT_bundle': 2,
        'TT_invalid': 0,
        'TT_table': 1,
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.egg.EggTable' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.egg.EggTable' objects>"
        '__doc__': "/**\n * This corresponds to a <Table> or a <Bundle> entry.  As such, it doesn't\n * actually contain a table of numbers, but it may be a parent to an\n * EggSAnimData or an EggXfmAnimData, which do.  It may also be a parent to\n * another <Table> or <Bundle>, establishing a hierarchy of tables.\n */",
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.egg.EggTable' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFDC68D11D0>'
        'assign': None, # (!) real value is "<method 'assign' of 'panda3d.egg.EggTable' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFDC68D11D0>)>'
        'getTableType': None, # (!) real value is "<method 'getTableType' of 'panda3d.egg.EggTable' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFDC68D11D0>)>'
        'get_table_type': None, # (!) real value is "<method 'get_table_type' of 'panda3d.egg.EggTable' objects>"
        'hasTransform': None, # (!) real value is "<method 'hasTransform' of 'panda3d.egg.EggTable' objects>"
        'has_transform': None, # (!) real value is "<method 'has_transform' of 'panda3d.egg.EggTable' objects>"
        'setTableType': None, # (!) real value is "<method 'setTableType' of 'panda3d.egg.EggTable' objects>"
        'set_table_type': None, # (!) real value is "<method 'set_table_type' of 'panda3d.egg.EggTable' objects>"
        'stringTableType': None, # (!) real value is '<staticmethod(<built-in method stringTableType of type object at 0x00007FFDC68D11D0>)>'
        'string_table_type': None, # (!) real value is '<staticmethod(<built-in method string_table_type of type object at 0x00007FFDC68D11D0>)>'
    }
    TTBundle = 2
    TTInvalid = 0
    TTTable = 1
    TT_bundle = 2
    TT_invalid = 0
    TT_table = 1


