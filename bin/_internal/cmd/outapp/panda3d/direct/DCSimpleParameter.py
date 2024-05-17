# encoding: utf-8
# module panda3d.direct
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\direct.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import panda3d.core as __panda3d_core


from .DCParameter import DCParameter

class DCSimpleParameter(DCParameter):
    """
    /**
     * This is the most fundamental kind of parameter type: a single number or
     * string, one of the DCSubatomicType elements.  It may also optionally have a
     * divisor, which is meaningful only for the numeric type elements (and
     * represents a fixed-point numeric convention).
     */
    """
    def getDivisor(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_divisor(DCSimpleParameter self)
        
        /**
         * Returns the divisor associated with this type.  This is 1 by default, but
         * if this is other than one it represents the scale to apply when packing and
         * unpacking numeric values (to store fixed-point values in an integer field).
         * It is only meaningful for numeric-type fields.
         */
        """
        pass

    def getModulus(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_modulus(DCSimpleParameter self)
        
        /**
         * Returns the modulus associated with this type, if any.  It is an error to
         * call this if has_modulus() returned false.
         *
         * If present, this is the modulus that is used to constrain the numeric value
         * of the field before it is packed (and range-checked).
         */
        """
        pass

    def getType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_type(DCSimpleParameter self)
        
        /**
         * Returns the particular subatomic type represented by this instance.
         */
        """
        pass

    def get_divisor(self, DCSimpleParameter_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_divisor(DCSimpleParameter self)
        
        /**
         * Returns the divisor associated with this type.  This is 1 by default, but
         * if this is other than one it represents the scale to apply when packing and
         * unpacking numeric values (to store fixed-point values in an integer field).
         * It is only meaningful for numeric-type fields.
         */
        """
        pass

    def get_modulus(self, DCSimpleParameter_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_modulus(DCSimpleParameter self)
        
        /**
         * Returns the modulus associated with this type, if any.  It is an error to
         * call this if has_modulus() returned false.
         *
         * If present, this is the modulus that is used to constrain the numeric value
         * of the field before it is packed (and range-checked).
         */
        """
        pass

    def get_type(self, DCSimpleParameter_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_type(DCSimpleParameter self)
        
        /**
         * Returns the particular subatomic type represented by this instance.
         */
        """
        pass

    def hasModulus(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_modulus(DCSimpleParameter self)
        
        /**
         * Returns true if there is a modulus associated, false otherwise.,
         */
        """
        pass

    def has_modulus(self, DCSimpleParameter_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_modulus(DCSimpleParameter self)
        
        /**
         * Returns true if there is a modulus associated, false otherwise.,
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
        '__doc__': '/**\n * This is the most fundamental kind of parameter type: a single number or\n * string, one of the DCSubatomicType elements.  It may also optionally have a\n * divisor, which is meaningful only for the numeric type elements (and\n * represents a fixed-point numeric convention).\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.direct.DCSimpleParameter' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFDC68DF0E0>'
        'getDivisor': None, # (!) real value is "<method 'getDivisor' of 'panda3d.direct.DCSimpleParameter' objects>"
        'getModulus': None, # (!) real value is "<method 'getModulus' of 'panda3d.direct.DCSimpleParameter' objects>"
        'getType': None, # (!) real value is "<method 'getType' of 'panda3d.direct.DCSimpleParameter' objects>"
        'get_divisor': None, # (!) real value is "<method 'get_divisor' of 'panda3d.direct.DCSimpleParameter' objects>"
        'get_modulus': None, # (!) real value is "<method 'get_modulus' of 'panda3d.direct.DCSimpleParameter' objects>"
        'get_type': None, # (!) real value is "<method 'get_type' of 'panda3d.direct.DCSimpleParameter' objects>"
        'hasModulus': None, # (!) real value is "<method 'hasModulus' of 'panda3d.direct.DCSimpleParameter' objects>"
        'has_modulus': None, # (!) real value is "<method 'has_modulus' of 'panda3d.direct.DCSimpleParameter' objects>"
    }


