# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


class HTTPDate(__dtoolconfig.DTOOL_SUPER_BASE):
    """
    /**
     * A container for an HTTP-legal time/date indication.  This can accept a
     * string from an HTTP header and will decode it into a C time_t value;
     * conversely, it can accept a time_t value and encode it for output as a
     * string.
     */
    """
    def assign(self, const_HTTPDate_self, const_HTTPDate_copy): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        assign(const HTTPDate self, const HTTPDate copy)
        """
        pass

    def compareTo(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        compare_to(HTTPDate self, const HTTPDate other)
        
        /**
         * Returns a number less than zero if this HTTPDate sorts before the other
         * one, greater than zero if it sorts after, or zero if they are equivalent.
         */
        """
        pass

    def compare_to(self, HTTPDate_self, const_HTTPDate_other): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        compare_to(HTTPDate self, const HTTPDate other)
        
        /**
         * Returns a number less than zero if this HTTPDate sorts before the other
         * one, greater than zero if it sorts after, or zero if they are equivalent.
         */
        """
        pass

    def getString(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_string(HTTPDate self)
        
        /**
         *
         */
        """
        pass

    def getTime(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_time(HTTPDate self)
        
        /**
         * Returns the date as a C time_t value.
         */
        """
        pass

    def get_string(self, HTTPDate_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_string(HTTPDate self)
        
        /**
         *
         */
        """
        pass

    def get_time(self, HTTPDate_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_time(HTTPDate self)
        
        /**
         * Returns the date as a C time_t value.
         */
        """
        pass

    def input(self, const_HTTPDate_self, istream_in): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        input(const HTTPDate self, istream in)
        
        /**
         *
         */
        """
        pass

    def isValid(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_valid(HTTPDate self)
        
        /**
         * Returns true if the date is meaningful, or false if it is -1 (which
         * generally indicates the source string could not be parsed.)
         */
        """
        pass

    def is_valid(self, HTTPDate_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_valid(HTTPDate self)
        
        /**
         * Returns true if the date is meaningful, or false if it is -1 (which
         * generally indicates the source string could not be parsed.)
         */
        """
        pass

    def now(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        now()
        
        /**
         * Returns an HTTPDate that represents the current time and date.
         */
        """
        pass

    def output(self, HTTPDate_self, ostream_out): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        output(HTTPDate self, ostream out)
        
        /**
         *
         */
        """
        pass

    def __add__(self, *args, **kwargs): # real signature unknown
        """ Return self+value. """
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

    def __iadd__(self, *args, **kwargs): # real signature unknown
        """ Return self+=value. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __isub__(self, *args, **kwargs): # real signature unknown
        """ Return self-=value. """
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

    def __radd__(self, *args, **kwargs): # real signature unknown
        """ Return value+self. """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __rsub__(self, *args, **kwargs): # real signature unknown
        """ Return value-self. """
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    def __sub__(self, *args, **kwargs): # real signature unknown
        """ Return self-value. """
        pass

    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__add__': None, # (!) real value is "<slot wrapper '__add__' of 'panda3d.core.HTTPDate' objects>"
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.core.HTTPDate' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.core.HTTPDate' objects>"
        '__doc__': '/**\n * A container for an HTTP-legal time/date indication.  This can accept a\n * string from an HTTP header and will decode it into a C time_t value;\n * conversely, it can accept a time_t value and encode it for output as a\n * string.\n */',
        '__eq__': None, # (!) real value is "<slot wrapper '__eq__' of 'panda3d.core.HTTPDate' objects>"
        '__ge__': None, # (!) real value is "<slot wrapper '__ge__' of 'panda3d.core.HTTPDate' objects>"
        '__gt__': None, # (!) real value is "<slot wrapper '__gt__' of 'panda3d.core.HTTPDate' objects>"
        '__hash__': None, # (!) real value is "<slot wrapper '__hash__' of 'panda3d.core.HTTPDate' objects>"
        '__iadd__': None, # (!) real value is "<slot wrapper '__iadd__' of 'panda3d.core.HTTPDate' objects>"
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.HTTPDate' objects>"
        '__isub__': None, # (!) real value is "<slot wrapper '__isub__' of 'panda3d.core.HTTPDate' objects>"
        '__le__': None, # (!) real value is "<slot wrapper '__le__' of 'panda3d.core.HTTPDate' objects>"
        '__lt__': None, # (!) real value is "<slot wrapper '__lt__' of 'panda3d.core.HTTPDate' objects>"
        '__ne__': None, # (!) real value is "<slot wrapper '__ne__' of 'panda3d.core.HTTPDate' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE26C570>'
        '__radd__': None, # (!) real value is "<slot wrapper '__radd__' of 'panda3d.core.HTTPDate' objects>"
        '__repr__': None, # (!) real value is "<slot wrapper '__repr__' of 'panda3d.core.HTTPDate' objects>"
        '__rsub__': None, # (!) real value is "<slot wrapper '__rsub__' of 'panda3d.core.HTTPDate' objects>"
        '__str__': None, # (!) real value is "<slot wrapper '__str__' of 'panda3d.core.HTTPDate' objects>"
        '__sub__': None, # (!) real value is "<slot wrapper '__sub__' of 'panda3d.core.HTTPDate' objects>"
        'assign': None, # (!) real value is "<method 'assign' of 'panda3d.core.HTTPDate' objects>"
        'compareTo': None, # (!) real value is "<method 'compareTo' of 'panda3d.core.HTTPDate' objects>"
        'compare_to': None, # (!) real value is "<method 'compare_to' of 'panda3d.core.HTTPDate' objects>"
        'getString': None, # (!) real value is "<method 'getString' of 'panda3d.core.HTTPDate' objects>"
        'getTime': None, # (!) real value is "<method 'getTime' of 'panda3d.core.HTTPDate' objects>"
        'get_string': None, # (!) real value is "<method 'get_string' of 'panda3d.core.HTTPDate' objects>"
        'get_time': None, # (!) real value is "<method 'get_time' of 'panda3d.core.HTTPDate' objects>"
        'input': None, # (!) real value is "<method 'input' of 'panda3d.core.HTTPDate' objects>"
        'isValid': None, # (!) real value is "<method 'isValid' of 'panda3d.core.HTTPDate' objects>"
        'is_valid': None, # (!) real value is "<method 'is_valid' of 'panda3d.core.HTTPDate' objects>"
        'now': None, # (!) real value is '<staticmethod(<built-in method now of type object at 0x00007FFCFE26C570>)>'
        'output': None, # (!) real value is "<method 'output' of 'panda3d.core.HTTPDate' objects>"
    }


