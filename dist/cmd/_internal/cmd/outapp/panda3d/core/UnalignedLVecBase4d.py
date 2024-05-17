# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


class UnalignedLVecBase4d(__dtoolconfig.DTOOL_SUPER_BASE):
    """
    /**
     * This is an "unaligned" LVecBase4.  It has no functionality other than to
     * store numbers, and it will pack them in as tightly as possible, avoiding
     * any SSE2 alignment requirements shared by the primary LVecBase4 class.
     *
     * Use it only when you need to pack numbers tightly without respect to
     * alignment, and then copy it to a proper LVecBase4 to get actual use from
     * it.
     */
    """
    def fill(self, const_UnalignedLVecBase4d_self, double_fill_value): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        fill(const UnalignedLVecBase4d self, double fill_value)
        
        /**
         * Sets each element of the vector to the indicated fill_value.  This is
         * particularly useful for initializing to zero.
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
        get_num_components()
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_num_components(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_components()
        """
        pass

    def set(self, const_UnalignedLVecBase4d_self, double_x, double_y, double_z, double_w): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set(const UnalignedLVecBase4d self, double x, double y, double z, double w)
        
        /**
         *
         */
        """
        pass

    def __copy__(self, *args, **kwargs): # real signature unknown
        pass

    def __deepcopy__(self, *args, **kwargs): # real signature unknown
        pass

    def __delitem__(self, *args, **kwargs): # real signature unknown
        """ Delete self[key]. """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __getitem__(self, *args, **kwargs): # real signature unknown
        """ Return self[key]. """
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

    def __len__(self, *args, **kwargs): # real signature unknown
        """ Return len(self). """
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

    def __setitem__(self, *args, **kwargs): # real signature unknown
        """ Set self[key] to value. """
        pass

    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.core.UnalignedLVecBase4d' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.core.UnalignedLVecBase4d' objects>"
        '__delitem__': None, # (!) real value is "<slot wrapper '__delitem__' of 'panda3d.core.UnalignedLVecBase4d' objects>"
        '__doc__': '/**\n * This is an "unaligned" LVecBase4.  It has no functionality other than to\n * store numbers, and it will pack them in as tightly as possible, avoiding\n * any SSE2 alignment requirements shared by the primary LVecBase4 class.\n *\n * Use it only when you need to pack numbers tightly without respect to\n * alignment, and then copy it to a proper LVecBase4 to get actual use from\n * it.\n */',
        '__eq__': None, # (!) real value is "<slot wrapper '__eq__' of 'panda3d.core.UnalignedLVecBase4d' objects>"
        '__ge__': None, # (!) real value is "<slot wrapper '__ge__' of 'panda3d.core.UnalignedLVecBase4d' objects>"
        '__getitem__': None, # (!) real value is "<slot wrapper '__getitem__' of 'panda3d.core.UnalignedLVecBase4d' objects>"
        '__gt__': None, # (!) real value is "<slot wrapper '__gt__' of 'panda3d.core.UnalignedLVecBase4d' objects>"
        '__hash__': None, # (!) real value is "<slot wrapper '__hash__' of 'panda3d.core.UnalignedLVecBase4d' objects>"
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.UnalignedLVecBase4d' objects>"
        '__le__': None, # (!) real value is "<slot wrapper '__le__' of 'panda3d.core.UnalignedLVecBase4d' objects>"
        '__len__': None, # (!) real value is "<slot wrapper '__len__' of 'panda3d.core.UnalignedLVecBase4d' objects>"
        '__lt__': None, # (!) real value is "<slot wrapper '__lt__' of 'panda3d.core.UnalignedLVecBase4d' objects>"
        '__ne__': None, # (!) real value is "<slot wrapper '__ne__' of 'panda3d.core.UnalignedLVecBase4d' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE322CE0>'
        '__setitem__': None, # (!) real value is "<slot wrapper '__setitem__' of 'panda3d.core.UnalignedLVecBase4d' objects>"
        'fill': None, # (!) real value is "<method 'fill' of 'panda3d.core.UnalignedLVecBase4d' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE322CE0>)>'
        'getNumComponents': None, # (!) real value is '<staticmethod(<built-in method getNumComponents of type object at 0x00007FFCFE322CE0>)>'
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE322CE0>)>'
        'get_num_components': None, # (!) real value is '<staticmethod(<built-in method get_num_components of type object at 0x00007FFCFE322CE0>)>'
        'is_int': 0,
        'num_components': 4,
        'set': None, # (!) real value is "<method 'set' of 'panda3d.core.UnalignedLVecBase4d' objects>"
    }
    is_int = 0
    num_components = 4


