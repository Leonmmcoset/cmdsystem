# encoding: utf-8
# module panda3d.direct
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\direct.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import panda3d.core as __panda3d_core


class DCDeclaration(__dtoolconfig.DTOOL_SUPER_BASE):
    """
    /**
     * This is a common interface for a declaration in a DC file.  Currently, this
     * is either a class or a typedef declaration (import declarations are still
     * collected together at the top, and don't inherit from this object).  Its
     * only purpose is so that classes and typedefs can be stored in one list
     * together so they can be ordered correctly on output.
     */
    """
    def asClass(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        as_class(const DCDeclaration self)
        as_class(DCDeclaration self)
        
        /**
         *
         */
        
        /**
         *
         */
        """
        pass

    def asSwitch(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        as_switch(const DCDeclaration self)
        as_switch(DCDeclaration self)
        
        /**
         *
         */
        
        /**
         *
         */
        """
        pass

    def as_class(self, const_DCDeclaration_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        as_class(const DCDeclaration self)
        as_class(DCDeclaration self)
        
        /**
         *
         */
        
        /**
         *
         */
        """
        pass

    def as_switch(self, const_DCDeclaration_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        as_switch(const DCDeclaration self)
        as_switch(DCDeclaration self)
        
        /**
         *
         */
        
        /**
         *
         */
        """
        pass

    def output(self, DCDeclaration_self, ostream_out): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        output(DCDeclaration self, ostream out)
        
        /**
         * Write a string representation of this instance to <out>.
         */
        """
        pass

    def write(self, DCDeclaration_self, ostream_out, int_indent_level): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        write(DCDeclaration self, ostream out, int indent_level)
        
        /**
         * Write a string representation of this instance to <out>.
         */
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__doc__': "/**\n * This is a common interface for a declaration in a DC file.  Currently, this\n * is either a class or a typedef declaration (import declarations are still\n * collected together at the top, and don't inherit from this object).  Its\n * only purpose is so that classes and typedefs can be stored in one list\n * together so they can be ordered correctly on output.\n */",
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.direct.DCDeclaration' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFDC68DE600>'
        '__repr__': None, # (!) real value is "<slot wrapper '__repr__' of 'panda3d.direct.DCDeclaration' objects>"
        '__str__': None, # (!) real value is "<slot wrapper '__str__' of 'panda3d.direct.DCDeclaration' objects>"
        'asClass': None, # (!) real value is "<method 'asClass' of 'panda3d.direct.DCDeclaration' objects>"
        'asSwitch': None, # (!) real value is "<method 'asSwitch' of 'panda3d.direct.DCDeclaration' objects>"
        'as_class': None, # (!) real value is "<method 'as_class' of 'panda3d.direct.DCDeclaration' objects>"
        'as_switch': None, # (!) real value is "<method 'as_switch' of 'panda3d.direct.DCDeclaration' objects>"
        'output': None, # (!) real value is "<method 'output' of 'panda3d.direct.DCDeclaration' objects>"
        'write': None, # (!) real value is "<method 'write' of 'panda3d.direct.DCDeclaration' objects>"
    }


