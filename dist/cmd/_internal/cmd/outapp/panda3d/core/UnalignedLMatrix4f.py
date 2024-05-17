# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


class UnalignedLMatrix4f(__dtoolconfig.DTOOL_SUPER_BASE):
    """
    /**
     * This is an "unaligned" LMatrix4.  It has no functionality other than to
     * store numbers, and it will pack them in as tightly as possible, avoiding
     * any SSE2 alignment requirements shared by the primary LMatrix4 class.
     *
     * Use it only when you need to pack numbers tightly without respect to
     * alignment, and then copy it to a proper LMatrix4 to get actual use from it.
     */
    """
    def assign(self, const_UnalignedLMatrix4f_self, const_LMatrix4f_copy): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        assign(const UnalignedLMatrix4f self, const LMatrix4f copy)
        assign(const UnalignedLMatrix4f self, const UnalignedLMatrix4f copy)
        
        /**
         *
         */
        
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

    def getNumComponents(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_components(UnalignedLMatrix4f self)
        
        /**
         * Returns the number of elements in the matrix, sixteen.
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_num_components(self, UnalignedLMatrix4f_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_components(UnalignedLMatrix4f self)
        
        /**
         * Returns the number of elements in the matrix, sixteen.
         */
        """
        pass

    def set(self, const_UnalignedLMatrix4f_self, float_e00, float_e01, float_e02, float_e03, float_e10, float_e11, float_e12, float_e13, float_e20, float_e21, float_e22, float_e23, float_e30, float_e31, float_e32, float_e33): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set(const UnalignedLMatrix4f self, float e00, float e01, float e02, float e03, float e10, float e11, float e12, float e13, float e20, float e21, float e22, float e23, float e30, float e31, float e32, float e33)
        
        /**
         *
         */
        """
        pass

    def __call__(self, *args, **kwargs): # real signature unknown
        """ Call self as a function. """
        pass

    def __copy__(self, *args, **kwargs): # real signature unknown
        pass

    def __deepcopy__(self, *args, **kwargs): # real signature unknown
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __hash__(self, *args, **kwargs): # real signature unknown
        """ Return hash(self). """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__call__': None, # (!) real value is "<slot wrapper '__call__' of 'panda3d.core.UnalignedLMatrix4f' objects>"
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.core.UnalignedLMatrix4f' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.core.UnalignedLMatrix4f' objects>"
        '__doc__': '/**\n * This is an "unaligned" LMatrix4.  It has no functionality other than to\n * store numbers, and it will pack them in as tightly as possible, avoiding\n * any SSE2 alignment requirements shared by the primary LMatrix4 class.\n *\n * Use it only when you need to pack numbers tightly without respect to\n * alignment, and then copy it to a proper LMatrix4 to get actual use from it.\n */',
        '__eq__': None, # (!) real value is "<slot wrapper '__eq__' of 'panda3d.core.UnalignedLMatrix4f' objects>"
        '__ge__': None, # (!) real value is "<slot wrapper '__ge__' of 'panda3d.core.UnalignedLMatrix4f' objects>"
        '__gt__': None, # (!) real value is "<slot wrapper '__gt__' of 'panda3d.core.UnalignedLMatrix4f' objects>"
        '__hash__': None, # (!) real value is "<slot wrapper '__hash__' of 'panda3d.core.UnalignedLMatrix4f' objects>"
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.UnalignedLMatrix4f' objects>"
        '__le__': None, # (!) real value is "<slot wrapper '__le__' of 'panda3d.core.UnalignedLMatrix4f' objects>"
        '__lt__': None, # (!) real value is "<slot wrapper '__lt__' of 'panda3d.core.UnalignedLMatrix4f' objects>"
        '__ne__': None, # (!) real value is "<slot wrapper '__ne__' of 'panda3d.core.UnalignedLMatrix4f' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE324810>'
        'assign': None, # (!) real value is "<method 'assign' of 'panda3d.core.UnalignedLMatrix4f' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE324810>)>'
        'getNumComponents': None, # (!) real value is "<method 'getNumComponents' of 'panda3d.core.UnalignedLMatrix4f' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE324810>)>'
        'get_num_components': None, # (!) real value is "<method 'get_num_components' of 'panda3d.core.UnalignedLMatrix4f' objects>"
        'num_components': 16,
        'set': None, # (!) real value is "<method 'set' of 'panda3d.core.UnalignedLMatrix4f' objects>"
    }
    num_components = 16


