# encoding: utf-8
# module panda3d.direct
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\direct.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import panda3d.core as __panda3d_core


from .DCParameter import DCParameter

class DCClassParameter(DCParameter):
    """
    /**
     * This represents a class (or struct) object used as a parameter itself.
     * This means that all the fields of the class get packed into the message.
     */
    """
    def getClass(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class(DCClassParameter self)
        
        /**
         * Returns the class object this parameter represents.
         */
        """
        pass

    def get_class(self, DCClassParameter_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class(DCClassParameter self)
        
        /**
         * Returns the class object this parameter represents.
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
        '__doc__': '/**\n * This represents a class (or struct) object used as a parameter itself.\n * This means that all the fields of the class get packed into the message.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.direct.DCClassParameter' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFDC68DE9A0>'
        'getClass': None, # (!) real value is "<method 'getClass' of 'panda3d.direct.DCClassParameter' objects>"
        'get_class': None, # (!) real value is "<method 'get_class' of 'panda3d.direct.DCClassParameter' objects>"
    }


