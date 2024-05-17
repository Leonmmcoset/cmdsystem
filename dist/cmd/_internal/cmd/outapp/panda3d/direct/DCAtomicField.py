# encoding: utf-8
# module panda3d.direct
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\direct.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import panda3d.core as __panda3d_core


from .DCField import DCField

class DCAtomicField(DCField):
    """
    /**
     * A single atomic field of a Distributed Class, as read from a .dc file.
     * This defines an interface to the Distributed Class, and is always
     * implemented as a remote procedure method.
     */
    """
    def getElement(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_element(DCAtomicField self, int n)
        
        /**
         * Returns the parameter object describing the nth element.
         */
        """
        pass

    def getElementDefault(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_element_default(DCAtomicField self, int n)
        
        // These five methods are deprecated and will be removed soon.
        
        /**
         * Returns the pre-formatted default value associated with the nth element of
         * the field.  This is only valid if has_element_default() returns true, in
         * which case this string represents the bytes that should be assigned to the
         * field as a default value.
         *
         * If the element is an array-type element, the returned value will include
         * the two-byte length preceding the array data.
         *
         * @deprecated use get_element() instead.
         */
        """
        pass

    def getElementDivisor(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_element_divisor(DCAtomicField self, int n)
        
        /**
         * Returns the divisor associated with the nth element of the field.  This
         * implements an implicit fixed-point system; floating-point values are to be
         * multiplied by this value before encoding into a packet, and divided by this
         * number after decoding.
         *
         * This method is deprecated; use get_element()->get_divisor() instead.
         */
        """
        pass

    def getElementName(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_element_name(DCAtomicField self, int n)
        
        /**
         * Returns the name of the nth element of the field.  This name is strictly
         * for documentary purposes; it does not generally affect operation.  If a
         * name is not specified, this will be the empty string.
         *
         * @deprecated use get_element()->get_name() instead.
         */
        """
        pass

    def getElementType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_element_type(DCAtomicField self, int n)
        
        /**
         * Returns the numeric type of the nth element of the field.  This method is
         * deprecated; use get_element() instead.
         */
        """
        pass

    def getNumElements(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_elements(DCAtomicField self)
        
        /**
         * Returns the number of elements (parameters) of the atomic field.
         */
        """
        pass

    def get_element(self, DCAtomicField_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_element(DCAtomicField self, int n)
        
        /**
         * Returns the parameter object describing the nth element.
         */
        """
        pass

    def get_element_default(self, DCAtomicField_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_element_default(DCAtomicField self, int n)
        
        // These five methods are deprecated and will be removed soon.
        
        /**
         * Returns the pre-formatted default value associated with the nth element of
         * the field.  This is only valid if has_element_default() returns true, in
         * which case this string represents the bytes that should be assigned to the
         * field as a default value.
         *
         * If the element is an array-type element, the returned value will include
         * the two-byte length preceding the array data.
         *
         * @deprecated use get_element() instead.
         */
        """
        pass

    def get_element_divisor(self, DCAtomicField_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_element_divisor(DCAtomicField self, int n)
        
        /**
         * Returns the divisor associated with the nth element of the field.  This
         * implements an implicit fixed-point system; floating-point values are to be
         * multiplied by this value before encoding into a packet, and divided by this
         * number after decoding.
         *
         * This method is deprecated; use get_element()->get_divisor() instead.
         */
        """
        pass

    def get_element_name(self, DCAtomicField_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_element_name(DCAtomicField self, int n)
        
        /**
         * Returns the name of the nth element of the field.  This name is strictly
         * for documentary purposes; it does not generally affect operation.  If a
         * name is not specified, this will be the empty string.
         *
         * @deprecated use get_element()->get_name() instead.
         */
        """
        pass

    def get_element_type(self, DCAtomicField_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_element_type(DCAtomicField self, int n)
        
        /**
         * Returns the numeric type of the nth element of the field.  This method is
         * deprecated; use get_element() instead.
         */
        """
        pass

    def get_num_elements(self, DCAtomicField_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_elements(DCAtomicField self)
        
        /**
         * Returns the number of elements (parameters) of the atomic field.
         */
        """
        pass

    def hasElementDefault(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_element_default(DCAtomicField self, int n)
        
        /**
         * Returns true if the nth element of the field has a default value specified,
         * false otherwise.
         *
         * @deprecated use get_element() instead.
         */
        """
        pass

    def has_element_default(self, DCAtomicField_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_element_default(DCAtomicField self, int n)
        
        /**
         * Returns true if the nth element of the field has a default value specified,
         * false otherwise.
         *
         * @deprecated use get_element() instead.
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
        '__doc__': '/**\n * A single atomic field of a Distributed Class, as read from a .dc file.\n * This defines an interface to the Distributed Class, and is always\n * implemented as a remote procedure method.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.direct.DCAtomicField' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFDC68DE430>'
        'getElement': None, # (!) real value is "<method 'getElement' of 'panda3d.direct.DCAtomicField' objects>"
        'getElementDefault': None, # (!) real value is "<method 'getElementDefault' of 'panda3d.direct.DCAtomicField' objects>"
        'getElementDivisor': None, # (!) real value is "<method 'getElementDivisor' of 'panda3d.direct.DCAtomicField' objects>"
        'getElementName': None, # (!) real value is "<method 'getElementName' of 'panda3d.direct.DCAtomicField' objects>"
        'getElementType': None, # (!) real value is "<method 'getElementType' of 'panda3d.direct.DCAtomicField' objects>"
        'getNumElements': None, # (!) real value is "<method 'getNumElements' of 'panda3d.direct.DCAtomicField' objects>"
        'get_element': None, # (!) real value is "<method 'get_element' of 'panda3d.direct.DCAtomicField' objects>"
        'get_element_default': None, # (!) real value is "<method 'get_element_default' of 'panda3d.direct.DCAtomicField' objects>"
        'get_element_divisor': None, # (!) real value is "<method 'get_element_divisor' of 'panda3d.direct.DCAtomicField' objects>"
        'get_element_name': None, # (!) real value is "<method 'get_element_name' of 'panda3d.direct.DCAtomicField' objects>"
        'get_element_type': None, # (!) real value is "<method 'get_element_type' of 'panda3d.direct.DCAtomicField' objects>"
        'get_num_elements': None, # (!) real value is "<method 'get_num_elements' of 'panda3d.direct.DCAtomicField' objects>"
        'hasElementDefault': None, # (!) real value is "<method 'hasElementDefault' of 'panda3d.direct.DCAtomicField' objects>"
        'has_element_default': None, # (!) real value is "<method 'has_element_default' of 'panda3d.direct.DCAtomicField' objects>"
    }


