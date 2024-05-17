# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


class ButtonHandle(__dtoolconfig.DTOOL_SUPER_BASE):
    """
    /**
     * A ButtonHandle represents a single button from any device, including
     * keyboard buttons and mouse buttons (but see KeyboardButton and
     * MouseButton).
     */
    """
    def compareTo(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        compare_to(ButtonHandle self, const ButtonHandle other)
        
        /**
         * Sorts ButtonHandles arbitrarily (according to <, >, etc.).  Returns a
         * number less than 0 if this type sorts before the other one, greater than
         * zero if it sorts after, 0 if they are equivalent.
         */
        """
        pass

    def compare_to(self, ButtonHandle_self, const_ButtonHandle_other): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        compare_to(ButtonHandle self, const ButtonHandle other)
        
        /**
         * Sorts ButtonHandles arbitrarily (according to <, >, etc.).  Returns a
         * number less than 0 if this type sorts before the other one, greater than
         * zero if it sorts after, 0 if they are equivalent.
         */
        """
        pass

    def getAlias(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_alias(ButtonHandle self)
        
        /**
         * Returns the alias (alternate name) associated with the button, if any, or
         * ButtonHandle::none() if the button has no alias.
         *
         * Each button is allowed to have one alias, and multiple different buttons
         * can refer to the same alias.  The alias should be the more general name for
         * the button, for instance, shift is an alias for lshift, but not vice-versa.
         */
        """
        pass

    def getAsciiEquivalent(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_ascii_equivalent(ButtonHandle self)
        
        /**
         * Returns the character code associated with the button, or '\0' if no ASCII
         * code was associated.
         */
        """
        pass

    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getHash(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_hash(ButtonHandle self)
        
        /**
         * Returns a hash code suitable for phash_map.
         */
        """
        pass

    def getIndex(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_index(ButtonHandle self)
        
        /**
         * Returns the integer index associated with this ButtonHandle.  Each
         * different ButtonHandle will have a different index.  However, you probably
         * shouldn't be using this method; you should just treat the ButtonHandles as
         * opaque classes.  This is provided for the convenience of non-C++ scripting
         * languages to build a hashtable of ButtonHandles.
         */
        """
        pass

    def getName(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_name(ButtonHandle self)
        
        /**
         * Returns the name of the button.
         */
        """
        pass

    def get_alias(self, ButtonHandle_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_alias(ButtonHandle self)
        
        /**
         * Returns the alias (alternate name) associated with the button, if any, or
         * ButtonHandle::none() if the button has no alias.
         *
         * Each button is allowed to have one alias, and multiple different buttons
         * can refer to the same alias.  The alias should be the more general name for
         * the button, for instance, shift is an alias for lshift, but not vice-versa.
         */
        """
        pass

    def get_ascii_equivalent(self, ButtonHandle_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_ascii_equivalent(ButtonHandle self)
        
        /**
         * Returns the character code associated with the button, or '\0' if no ASCII
         * code was associated.
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_hash(self, ButtonHandle_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_hash(ButtonHandle self)
        
        /**
         * Returns a hash code suitable for phash_map.
         */
        """
        pass

    def get_index(self, ButtonHandle_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_index(ButtonHandle self)
        
        /**
         * Returns the integer index associated with this ButtonHandle.  Each
         * different ButtonHandle will have a different index.  However, you probably
         * shouldn't be using this method; you should just treat the ButtonHandles as
         * opaque classes.  This is provided for the convenience of non-C++ scripting
         * languages to build a hashtable of ButtonHandles.
         */
        """
        pass

    def get_name(self, ButtonHandle_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_name(ButtonHandle self)
        
        /**
         * Returns the name of the button.
         */
        """
        pass

    def hasAsciiEquivalent(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_ascii_equivalent(ButtonHandle self)
        
        /**
         * Returns true if the button was created with an ASCII equivalent code (e.g.
         * for a standard keyboard button).
         */
        """
        pass

    def has_ascii_equivalent(self, ButtonHandle_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_ascii_equivalent(ButtonHandle self)
        
        /**
         * Returns true if the button was created with an ASCII equivalent code (e.g.
         * for a standard keyboard button).
         */
        """
        pass

    def matches(self, ButtonHandle_self, const_ButtonHandle_other): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        matches(ButtonHandle self, const ButtonHandle other)
        
        /**
         * Returns true if this ButtonHandle is the same as the other one, or if the
         * other one is an alias for this one.  (Does not return true if this button
         * is an alias for the other one, however.)
         *
         * This is a more general comparison than operator ==.
         */
        """
        pass

    def none(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        none()
        """
        pass

    def output(self, ButtonHandle_self, ostream_out): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        output(ButtonHandle self, ostream out)
        
        /**
         *
         */
        """
        pass

    def __bool__(self, *args, **kwargs): # real signature unknown
        """ True if self else False """
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

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    alias = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ascii_equivalent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    index = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__bool__': None, # (!) real value is "<slot wrapper '__bool__' of 'panda3d.core.ButtonHandle' objects>"
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.core.ButtonHandle' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.core.ButtonHandle' objects>"
        '__doc__': '/**\n * A ButtonHandle represents a single button from any device, including\n * keyboard buttons and mouse buttons (but see KeyboardButton and\n * MouseButton).\n */',
        '__eq__': None, # (!) real value is "<slot wrapper '__eq__' of 'panda3d.core.ButtonHandle' objects>"
        '__ge__': None, # (!) real value is "<slot wrapper '__ge__' of 'panda3d.core.ButtonHandle' objects>"
        '__gt__': None, # (!) real value is "<slot wrapper '__gt__' of 'panda3d.core.ButtonHandle' objects>"
        '__hash__': None, # (!) real value is "<slot wrapper '__hash__' of 'panda3d.core.ButtonHandle' objects>"
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.ButtonHandle' objects>"
        '__le__': None, # (!) real value is "<slot wrapper '__le__' of 'panda3d.core.ButtonHandle' objects>"
        '__lt__': None, # (!) real value is "<slot wrapper '__lt__' of 'panda3d.core.ButtonHandle' objects>"
        '__ne__': None, # (!) real value is "<slot wrapper '__ne__' of 'panda3d.core.ButtonHandle' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE370AF0>'
        '__repr__': None, # (!) real value is "<slot wrapper '__repr__' of 'panda3d.core.ButtonHandle' objects>"
        '__str__': None, # (!) real value is "<slot wrapper '__str__' of 'panda3d.core.ButtonHandle' objects>"
        'alias': None, # (!) real value is "<attribute 'alias' of 'panda3d.core.ButtonHandle' objects>"
        'ascii_equivalent': None, # (!) real value is "<attribute 'ascii_equivalent' of 'panda3d.core.ButtonHandle' objects>"
        'compareTo': None, # (!) real value is "<method 'compareTo' of 'panda3d.core.ButtonHandle' objects>"
        'compare_to': None, # (!) real value is "<method 'compare_to' of 'panda3d.core.ButtonHandle' objects>"
        'getAlias': None, # (!) real value is "<method 'getAlias' of 'panda3d.core.ButtonHandle' objects>"
        'getAsciiEquivalent': None, # (!) real value is "<method 'getAsciiEquivalent' of 'panda3d.core.ButtonHandle' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE370AF0>)>'
        'getHash': None, # (!) real value is "<method 'getHash' of 'panda3d.core.ButtonHandle' objects>"
        'getIndex': None, # (!) real value is "<method 'getIndex' of 'panda3d.core.ButtonHandle' objects>"
        'getName': None, # (!) real value is "<method 'getName' of 'panda3d.core.ButtonHandle' objects>"
        'get_alias': None, # (!) real value is "<method 'get_alias' of 'panda3d.core.ButtonHandle' objects>"
        'get_ascii_equivalent': None, # (!) real value is "<method 'get_ascii_equivalent' of 'panda3d.core.ButtonHandle' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE370AF0>)>'
        'get_hash': None, # (!) real value is "<method 'get_hash' of 'panda3d.core.ButtonHandle' objects>"
        'get_index': None, # (!) real value is "<method 'get_index' of 'panda3d.core.ButtonHandle' objects>"
        'get_name': None, # (!) real value is "<method 'get_name' of 'panda3d.core.ButtonHandle' objects>"
        'hasAsciiEquivalent': None, # (!) real value is "<method 'hasAsciiEquivalent' of 'panda3d.core.ButtonHandle' objects>"
        'has_ascii_equivalent': None, # (!) real value is "<method 'has_ascii_equivalent' of 'panda3d.core.ButtonHandle' objects>"
        'index': None, # (!) real value is "<attribute 'index' of 'panda3d.core.ButtonHandle' objects>"
        'matches': None, # (!) real value is "<method 'matches' of 'panda3d.core.ButtonHandle' objects>"
        'name': None, # (!) real value is "<attribute 'name' of 'panda3d.core.ButtonHandle' objects>"
        'none': None, # (!) real value is '<staticmethod(<built-in method none of type object at 0x00007FFCFE370AF0>)>'
        'output': None, # (!) real value is "<method 'output' of 'panda3d.core.ButtonHandle' objects>"
    }


