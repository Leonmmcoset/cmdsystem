# encoding: utf-8
# module panda3d.egg
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\egg.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import panda3d.core as __panda3d_core


class EggUserData(__panda3d_core.TypedReferenceCount):
    """
    /**
     * This is a base class for a user-defined data type to extend egg structures
     * in processing code.  The user of the egg library may derive from
     * EggUserData to associate any arbitrary data with various egg objects.
     *
     * However, this data will not be written out to the disk when the egg file is
     * written; it is an in-memory object only.
     */
    """
    def assign(self, const_EggUserData_self, const_EggUserData_copy): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        assign(const EggUserData self, const EggUserData copy)
        
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

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
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
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.egg.EggUserData' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.egg.EggUserData' objects>"
        '__doc__': '/**\n * This is a base class for a user-defined data type to extend egg structures\n * in processing code.  The user of the egg library may derive from\n * EggUserData to associate any arbitrary data with various egg objects.\n *\n * However, this data will not be written out to the disk when the egg file is\n * written; it is an in-memory object only.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.egg.EggUserData' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFDC68CC5B0>'
        'assign': None, # (!) real value is "<method 'assign' of 'panda3d.egg.EggUserData' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFDC68CC5B0>)>'
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFDC68CC5B0>)>'
    }


