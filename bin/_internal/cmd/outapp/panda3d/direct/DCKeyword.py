# encoding: utf-8
# module panda3d.direct
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\direct.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import panda3d.core as __panda3d_core


from .DCDeclaration import DCDeclaration

class DCKeyword(DCDeclaration):
    """
    /**
     * This represents a single keyword declaration in the dc file.  It is used to
     * define a communication property associated with a field, for instance
     * "broadcast" or "airecv".
     */
    """
    def getName(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_name(DCKeyword self)
        
        /**
         * Returns the name of this keyword.
         */
        """
        pass

    def get_name(self, DCKeyword_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_name(DCKeyword self)
        
        /**
         * Returns the name of this keyword.
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
        '__doc__': '/**\n * This represents a single keyword declaration in the dc file.  It is used to\n * define a communication property associated with a field, for instance\n * "broadcast" or "airecv".\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.direct.DCKeyword' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFDC68DED40>'
        'getName': None, # (!) real value is "<method 'getName' of 'panda3d.direct.DCKeyword' objects>"
        'get_name': None, # (!) real value is "<method 'get_name' of 'panda3d.direct.DCKeyword' objects>"
    }


