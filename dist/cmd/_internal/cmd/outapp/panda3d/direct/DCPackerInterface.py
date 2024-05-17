# encoding: utf-8
# module panda3d.direct
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\direct.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import panda3d.core as __panda3d_core


class DCPackerInterface(__dtoolconfig.DTOOL_SUPER_BASE):
    """
    /**
     * This defines the internal interface for packing values into a DCField.  The
     * various different DC objects inherit from this.
     *
     * Normally these methods are called only by the DCPacker object; the user
     * wouldn't normally call these directly.
     */
    """
    def asClassParameter(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        as_class_parameter(const DCPackerInterface self)
        as_class_parameter(DCPackerInterface self)
        
        /**
         *
         */
        
        /**
         *
         */
        """
        pass

    def asField(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        as_field(const DCPackerInterface self)
        as_field(DCPackerInterface self)
        
        /**
         *
         */
        
        /**
         *
         */
        """
        pass

    def asSwitchParameter(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        as_switch_parameter(const DCPackerInterface self)
        as_switch_parameter(DCPackerInterface self)
        
        /**
         *
         */
        
        /**
         *
         */
        """
        pass

    def as_class_parameter(self, const_DCPackerInterface_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        as_class_parameter(const DCPackerInterface self)
        as_class_parameter(DCPackerInterface self)
        
        /**
         *
         */
        
        /**
         *
         */
        """
        pass

    def as_field(self, const_DCPackerInterface_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        as_field(const DCPackerInterface self)
        as_field(DCPackerInterface self)
        
        /**
         *
         */
        
        /**
         *
         */
        """
        pass

    def as_switch_parameter(self, const_DCPackerInterface_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        as_switch_parameter(const DCPackerInterface self)
        as_switch_parameter(DCPackerInterface self)
        
        /**
         *
         */
        
        /**
         *
         */
        """
        pass

    def checkMatch(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        check_match(DCPackerInterface self, str description, DCFile dcfile)
        check_match(DCPackerInterface self, const DCPackerInterface other)
        
        /**
         * Returns true if the other interface is bitwise the same as this one--that
         * is, a uint32 only matches a uint32, etc.  Names of components, and range
         * limits, are not compared.
         */
        
        /**
         * Returns true if this interface is bitwise the same as the interface
         * described with the indicated formatted string, e.g.  "(uint8, uint8,
         * int16)", or false otherwise.
         *
         * If DCFile is not NULL, it specifies the DCFile that was previously loaded,
         * from which some predefined structs and typedefs may be referenced in the
         * description string.
         */
        """
        pass

    def check_match(self, DCPackerInterface_self, str_description, DCFile_dcfile): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        check_match(DCPackerInterface self, str description, DCFile dcfile)
        check_match(DCPackerInterface self, const DCPackerInterface other)
        
        /**
         * Returns true if the other interface is bitwise the same as this one--that
         * is, a uint32 only matches a uint32, etc.  Names of components, and range
         * limits, are not compared.
         */
        
        /**
         * Returns true if this interface is bitwise the same as the interface
         * described with the indicated formatted string, e.g.  "(uint8, uint8,
         * int16)", or false otherwise.
         *
         * If DCFile is not NULL, it specifies the DCFile that was previously loaded,
         * from which some predefined structs and typedefs may be referenced in the
         * description string.
         */
        """
        pass

    def findSeekIndex(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        find_seek_index(DCPackerInterface self, str name)
        
        /**
         * Returns the index number to be passed to a future call to DCPacker::seek()
         * to seek directly to the named field without having to look up the field
         * name in a table later, or -1 if the named field cannot be found.
         *
         * If the named field is nested within a switch or some similar dynamic
         * structure that reveals different fields based on the contents of the data,
         * this mechanism cannot be used to pre-fetch the field index number--you must
         * seek for the field by name.
         */
        """
        pass

    def find_seek_index(self, DCPackerInterface_self, str_name): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        find_seek_index(DCPackerInterface self, str name)
        
        /**
         * Returns the index number to be passed to a future call to DCPacker::seek()
         * to seek directly to the named field without having to look up the field
         * name in a table later, or -1 if the named field cannot be found.
         *
         * If the named field is nested within a switch or some similar dynamic
         * structure that reveals different fields based on the contents of the data,
         * this mechanism cannot be used to pre-fetch the field index number--you must
         * seek for the field by name.
         */
        """
        pass

    def getName(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_name(DCPackerInterface self)
        
        /**
         * Returns the name of this field, or empty string if the field is unnamed.
         */
        """
        pass

    def get_name(self, DCPackerInterface_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_name(DCPackerInterface self)
        
        /**
         * Returns the name of this field, or empty string if the field is unnamed.
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
        '__doc__': "/**\n * This defines the internal interface for packing values into a DCField.  The\n * various different DC objects inherit from this.\n *\n * Normally these methods are called only by the DCPacker object; the user\n * wouldn't normally call these directly.\n */",
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.direct.DCPackerInterface' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFDC68DD770>'
        'asClassParameter': None, # (!) real value is "<method 'asClassParameter' of 'panda3d.direct.DCPackerInterface' objects>"
        'asField': None, # (!) real value is "<method 'asField' of 'panda3d.direct.DCPackerInterface' objects>"
        'asSwitchParameter': None, # (!) real value is "<method 'asSwitchParameter' of 'panda3d.direct.DCPackerInterface' objects>"
        'as_class_parameter': None, # (!) real value is "<method 'as_class_parameter' of 'panda3d.direct.DCPackerInterface' objects>"
        'as_field': None, # (!) real value is "<method 'as_field' of 'panda3d.direct.DCPackerInterface' objects>"
        'as_switch_parameter': None, # (!) real value is "<method 'as_switch_parameter' of 'panda3d.direct.DCPackerInterface' objects>"
        'checkMatch': None, # (!) real value is "<method 'checkMatch' of 'panda3d.direct.DCPackerInterface' objects>"
        'check_match': None, # (!) real value is "<method 'check_match' of 'panda3d.direct.DCPackerInterface' objects>"
        'findSeekIndex': None, # (!) real value is "<method 'findSeekIndex' of 'panda3d.direct.DCPackerInterface' objects>"
        'find_seek_index': None, # (!) real value is "<method 'find_seek_index' of 'panda3d.direct.DCPackerInterface' objects>"
        'getName': None, # (!) real value is "<method 'getName' of 'panda3d.direct.DCPackerInterface' objects>"
        'get_name': None, # (!) real value is "<method 'get_name' of 'panda3d.direct.DCPackerInterface' objects>"
    }


