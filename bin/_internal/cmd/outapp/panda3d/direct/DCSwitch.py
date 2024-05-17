# encoding: utf-8
# module panda3d.direct
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\direct.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import panda3d.core as __panda3d_core


from .DCDeclaration import DCDeclaration

class DCSwitch(DCDeclaration):
    """
    /**
     * This represents a switch statement, which can appear inside a class body
     * and represents two or more alternative unpacking schemes based on the first
     * field read.
     */
    """
    def getCase(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_case(DCSwitch self, int n)
        
        /**
         * Returns the DCPackerInterface that packs the nth case.
         */
        """
        pass

    def getCaseByValue(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_case_by_value(DCSwitch self, bytes case_value)
        
        /**
         * Returns the index number of the case with the indicated packed value, or -1
         * if no case has this value.
         */
        """
        pass

    def getDefaultCase(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_default_case(DCSwitch self)
        
        /**
         * Returns the DCPackerInterface that packs the default case, or NULL if there
         * is no default case.
         */
        """
        pass

    def getField(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_field(DCSwitch self, int case_index, int n)
        
        /**
         * Returns the nth field in the indicated case.
         */
        """
        pass

    def getFieldByName(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_field_by_name(DCSwitch self, int case_index, str name)
        
        /**
         * Returns the field with the given name from the indicated case, or NULL if
         * no field has this name.
         */
        """
        pass

    def getKeyParameter(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_key_parameter(DCSwitch self)
        
        /**
         * Returns the key parameter on which the switch is based.  The value of this
         * parameter in the record determines which one of the several cases within
         * the switch will be used.
         */
        """
        pass

    def getName(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_name(DCSwitch self)
        
        /**
         * Returns the name of this switch.
         */
        """
        pass

    def getNumCases(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_cases(DCSwitch self)
        
        /**
         * Returns the number of different cases within the switch.  The legal values
         * for case_index range from 0 to get_num_cases() - 1.
         */
        """
        pass

    def getNumFields(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_fields(DCSwitch self, int case_index)
        
        /**
         * Returns the number of fields in the indicated case.
         */
        """
        pass

    def getValue(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_value(DCSwitch self, int case_index)
        
        /**
         * Returns the packed value associated with the indicated case.
         */
        """
        pass

    def get_case(self, DCSwitch_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_case(DCSwitch self, int n)
        
        /**
         * Returns the DCPackerInterface that packs the nth case.
         */
        """
        pass

    def get_case_by_value(self, DCSwitch_self, bytes_case_value): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_case_by_value(DCSwitch self, bytes case_value)
        
        /**
         * Returns the index number of the case with the indicated packed value, or -1
         * if no case has this value.
         */
        """
        pass

    def get_default_case(self, DCSwitch_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_default_case(DCSwitch self)
        
        /**
         * Returns the DCPackerInterface that packs the default case, or NULL if there
         * is no default case.
         */
        """
        pass

    def get_field(self, DCSwitch_self, int_case_index, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_field(DCSwitch self, int case_index, int n)
        
        /**
         * Returns the nth field in the indicated case.
         */
        """
        pass

    def get_field_by_name(self, DCSwitch_self, int_case_index, str_name): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_field_by_name(DCSwitch self, int case_index, str name)
        
        /**
         * Returns the field with the given name from the indicated case, or NULL if
         * no field has this name.
         */
        """
        pass

    def get_key_parameter(self, DCSwitch_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_key_parameter(DCSwitch self)
        
        /**
         * Returns the key parameter on which the switch is based.  The value of this
         * parameter in the record determines which one of the several cases within
         * the switch will be used.
         */
        """
        pass

    def get_name(self, DCSwitch_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_name(DCSwitch self)
        
        /**
         * Returns the name of this switch.
         */
        """
        pass

    def get_num_cases(self, DCSwitch_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_cases(DCSwitch self)
        
        /**
         * Returns the number of different cases within the switch.  The legal values
         * for case_index range from 0 to get_num_cases() - 1.
         */
        """
        pass

    def get_num_fields(self, DCSwitch_self, int_case_index): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_fields(DCSwitch self, int case_index)
        
        /**
         * Returns the number of fields in the indicated case.
         */
        """
        pass

    def get_value(self, DCSwitch_self, int_case_index): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_value(DCSwitch self, int case_index)
        
        /**
         * Returns the packed value associated with the indicated case.
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
        '__doc__': '/**\n * This represents a switch statement, which can appear inside a class body\n * and represents two or more alternative unpacking schemes based on the first\n * field read.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.direct.DCSwitch' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFDC68DF2B0>'
        'getCase': None, # (!) real value is "<method 'getCase' of 'panda3d.direct.DCSwitch' objects>"
        'getCaseByValue': None, # (!) real value is "<method 'getCaseByValue' of 'panda3d.direct.DCSwitch' objects>"
        'getDefaultCase': None, # (!) real value is "<method 'getDefaultCase' of 'panda3d.direct.DCSwitch' objects>"
        'getField': None, # (!) real value is "<method 'getField' of 'panda3d.direct.DCSwitch' objects>"
        'getFieldByName': None, # (!) real value is "<method 'getFieldByName' of 'panda3d.direct.DCSwitch' objects>"
        'getKeyParameter': None, # (!) real value is "<method 'getKeyParameter' of 'panda3d.direct.DCSwitch' objects>"
        'getName': None, # (!) real value is "<method 'getName' of 'panda3d.direct.DCSwitch' objects>"
        'getNumCases': None, # (!) real value is "<method 'getNumCases' of 'panda3d.direct.DCSwitch' objects>"
        'getNumFields': None, # (!) real value is "<method 'getNumFields' of 'panda3d.direct.DCSwitch' objects>"
        'getValue': None, # (!) real value is "<method 'getValue' of 'panda3d.direct.DCSwitch' objects>"
        'get_case': None, # (!) real value is "<method 'get_case' of 'panda3d.direct.DCSwitch' objects>"
        'get_case_by_value': None, # (!) real value is "<method 'get_case_by_value' of 'panda3d.direct.DCSwitch' objects>"
        'get_default_case': None, # (!) real value is "<method 'get_default_case' of 'panda3d.direct.DCSwitch' objects>"
        'get_field': None, # (!) real value is "<method 'get_field' of 'panda3d.direct.DCSwitch' objects>"
        'get_field_by_name': None, # (!) real value is "<method 'get_field_by_name' of 'panda3d.direct.DCSwitch' objects>"
        'get_key_parameter': None, # (!) real value is "<method 'get_key_parameter' of 'panda3d.direct.DCSwitch' objects>"
        'get_name': None, # (!) real value is "<method 'get_name' of 'panda3d.direct.DCSwitch' objects>"
        'get_num_cases': None, # (!) real value is "<method 'get_num_cases' of 'panda3d.direct.DCSwitch' objects>"
        'get_num_fields': None, # (!) real value is "<method 'get_num_fields' of 'panda3d.direct.DCSwitch' objects>"
        'get_value': None, # (!) real value is "<method 'get_value' of 'panda3d.direct.DCSwitch' objects>"
    }


