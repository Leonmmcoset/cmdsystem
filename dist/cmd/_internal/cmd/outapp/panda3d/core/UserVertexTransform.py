# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .VertexTransform import VertexTransform

class UserVertexTransform(VertexTransform):
    """
    /**
     * This is a specialization on VertexTransform that allows the user to specify
     * any arbitrary transform matrix he likes.  This is rarely used except for
     * testing.
     */
    """
    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getName(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_name(UserVertexTransform self)
        
        /**
         * Returns the name passed to the constructor.  Completely arbitrary.
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_name(self, UserVertexTransform_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_name(UserVertexTransform self)
        
        /**
         * Returns the name passed to the constructor.  Completely arbitrary.
         */
        """
        pass

    def setMatrix(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_matrix(const UserVertexTransform self, const LMatrix4f matrix)
        
        /**
         * Stores the indicated matrix.
         */
        """
        pass

    def set_matrix(self, const_UserVertexTransform_self, const_LMatrix4f_matrix): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_matrix(const UserVertexTransform self, const LMatrix4f matrix)
        
        /**
         * Stores the indicated matrix.
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
        '__doc__': '/**\n * This is a specialization on VertexTransform that allows the user to specify\n * any arbitrary transform matrix he likes.  This is rarely used except for\n * testing.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.UserVertexTransform' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE300C10>'
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE300C10>)>'
        'getName': None, # (!) real value is "<method 'getName' of 'panda3d.core.UserVertexTransform' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE300C10>)>'
        'get_name': None, # (!) real value is "<method 'get_name' of 'panda3d.core.UserVertexTransform' objects>"
        'setMatrix': None, # (!) real value is "<method 'setMatrix' of 'panda3d.core.UserVertexTransform' objects>"
        'set_matrix': None, # (!) real value is "<method 'set_matrix' of 'panda3d.core.UserVertexTransform' objects>"
    }


