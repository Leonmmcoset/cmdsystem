# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


class UnalignedLMatrix4d(__dtoolconfig.DTOOL_SUPER_BASE):
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
    def assign(self, const_UnalignedLMatrix4d_self, const_LMatrix4d_copy): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        assign(const UnalignedLMatrix4d self, const LMatrix4d copy)
        assign(const UnalignedLMatrix4d self, const UnalignedLMatrix4d copy)
        
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
        get_num_components(UnalignedLMatrix4d self)
        
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

    def get_num_components(self, UnalignedLMatrix4d_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_components(UnalignedLMatrix4d self)
        
        /**
         * Returns the number of elements in the matrix, sixteen.
         */
        """
        pass

    def set(self, const_UnalignedLMatrix4d_self, double_e00, double_e01, double_e02, double_e03, double_e10, double_e11, double_e12, double_e13, double_e20, double_e21, double_e22, double_e23, double_e30, double_e31, double_e32, double_e33): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set(const UnalignedLMatrix4d self, double e00, double e01, double e02, double e03, double e10, double e11, double e12, double e13, double e20, double e21, double e22, double e23, double e30, double e31, double e32, double e33)
        
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
        '__call__': None, # (!) real value is "<slot wrapper '__call__' of 'panda3d.core.UnalignedLMatrix4d' objects>"
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.core.UnalignedLMatrix4d' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.core.UnalignedLMatrix4d' objects>"
        '__doc__': '/**\n * This is an "unaligned" LMatrix4.  It has no functionality other than to\n * store numbers, and it will pack them in as tightly as possible, avoiding\n * any SSE2 alignment requirements shared by the primary LMatrix4 class.\n *\n * Use it only when you need to pack numbers tightly without respect to\n * alignment, and then copy it to a proper LMatrix4 to get actual use from it.\n */',
        '__eq__': None, # (!) real value is "<slot wrapper '__eq__' of 'panda3d.core.UnalignedLMatrix4d' objects>"
        '__ge__': None, # (!) real value is "<slot wrapper '__ge__' of 'panda3d.core.UnalignedLMatrix4d' objects>"
        '__gt__': None, # (!) real value is "<slot wrapper '__gt__' of 'panda3d.core.UnalignedLMatrix4d' objects>"
        '__hash__': None, # (!) real value is "<slot wrapper '__hash__' of 'panda3d.core.UnalignedLMatrix4d' objects>"
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.UnalignedLMatrix4d' objects>"
        '__le__': None, # (!) real value is "<slot wrapper '__le__' of 'panda3d.core.UnalignedLMatrix4d' objects>"
        '__lt__': None, # (!) real value is "<slot wrapper '__lt__' of 'panda3d.core.UnalignedLMatrix4d' objects>"
        '__ne__': None, # (!) real value is "<slot wrapper '__ne__' of 'panda3d.core.UnalignedLMatrix4d' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE3254C0>'
        'assign': None, # (!) real value is "<method 'assign' of 'panda3d.core.UnalignedLMatrix4d' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE3254C0>)>'
        'getNumComponents': None, # (!) real value is "<method 'getNumComponents' of 'panda3d.core.UnalignedLMatrix4d' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE3254C0>)>'
        'get_num_components': None, # (!) real value is "<method 'get_num_components' of 'panda3d.core.UnalignedLMatrix4d' objects>"
        'num_components': 16,
        'set': None, # (!) real value is "<method 'set' of 'panda3d.core.UnalignedLMatrix4d' objects>"
    }
    num_components = 16


