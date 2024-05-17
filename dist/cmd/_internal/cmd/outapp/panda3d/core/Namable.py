# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


class Namable(__dtoolconfig.DTOOL_SUPER_BASE):
    """
    /**
     * A base class for all things which can have a name.  The name is either
     * empty or nonempty, but it is never NULL.
     */
    """
    def clearName(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_name(const Namable self)
        
        /**
         * Resets the Namable's name to empty.
         */
        """
        pass

    def clear_name(self, const_Namable_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_name(const Namable self)
        
        /**
         * Resets the Namable's name to empty.
         */
        """
        pass

    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getName(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_name(Namable self)
        
        /**
         *
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_name(self, Namable_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_name(Namable self)
        
        /**
         *
         */
        """
        pass

    def hasName(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_name(Namable self)
        
        /**
         * Returns true if the Namable has a nonempty name set, false if the name is
         * empty.
         */
        """
        pass

    def has_name(self, Namable_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_name(Namable self)
        
        /**
         * Returns true if the Namable has a nonempty name set, false if the name is
         * empty.
         */
        """
        pass

    def output(self, Namable_self, ostream_out): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        output(Namable self, ostream out)
        
        // In the absence of any definition to the contrary, outputting a Namable
        // will write out its name.
        
        /**
         * Outputs the Namable.  This function simply writes the name to the output
         * stream; most Namable derivatives will probably redefine this.
         */
        """
        pass

    def setName(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_name(const Namable self, str name)
        
        /**
         *
         */
        """
        pass

    def set_name(self, const_Namable_self, str_name): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_name(const Namable self, str name)
        
        /**
         *
         */
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

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.core.Namable' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.core.Namable' objects>"
        '__doc__': '/**\n * A base class for all things which can have a name.  The name is either\n * empty or nonempty, but it is never NULL.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.Namable' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE2790E0>'
        '__repr__': None, # (!) real value is "<slot wrapper '__repr__' of 'panda3d.core.Namable' objects>"
        '__str__': None, # (!) real value is "<slot wrapper '__str__' of 'panda3d.core.Namable' objects>"
        'clearName': None, # (!) real value is "<method 'clearName' of 'panda3d.core.Namable' objects>"
        'clear_name': None, # (!) real value is "<method 'clear_name' of 'panda3d.core.Namable' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE2790E0>)>'
        'getName': None, # (!) real value is "<method 'getName' of 'panda3d.core.Namable' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE2790E0>)>'
        'get_name': None, # (!) real value is "<method 'get_name' of 'panda3d.core.Namable' objects>"
        'hasName': None, # (!) real value is "<method 'hasName' of 'panda3d.core.Namable' objects>"
        'has_name': None, # (!) real value is "<method 'has_name' of 'panda3d.core.Namable' objects>"
        'name': None, # (!) real value is "<attribute 'name' of 'panda3d.core.Namable' objects>"
        'output': None, # (!) real value is "<method 'output' of 'panda3d.core.Namable' objects>"
        'setName': None, # (!) real value is "<method 'setName' of 'panda3d.core.Namable' objects>"
        'set_name': None, # (!) real value is "<method 'set_name' of 'panda3d.core.Namable' objects>"
    }


