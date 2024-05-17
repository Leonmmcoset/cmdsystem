# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


class HTTPEntityTag(__dtoolconfig.DTOOL_SUPER_BASE):
    """
    /**
     * A container for an "entity tag" from an HTTP server.  This is used to
     * identify a particular version of a document or resource, particularly
     * useful for verifying caches.
     */
    """
    def assign(self, const_HTTPEntityTag_self, const_HTTPEntityTag_copy): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        assign(const HTTPEntityTag self, const HTTPEntityTag copy)
        """
        pass

    def compareTo(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        compare_to(HTTPEntityTag self, const HTTPEntityTag other)
        
        /**
         * Returns a number less than zero if this HTTPEntityTag sorts before the
         * other one, greater than zero if it sorts after, or zero if they are
         * equivalent.
         */
        """
        pass

    def compare_to(self, HTTPEntityTag_self, const_HTTPEntityTag_other): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        compare_to(HTTPEntityTag self, const HTTPEntityTag other)
        
        /**
         * Returns a number less than zero if this HTTPEntityTag sorts before the
         * other one, greater than zero if it sorts after, or zero if they are
         * equivalent.
         */
        """
        pass

    def getString(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_string(HTTPEntityTag self)
        
        /**
         * Returns the entity tag formatted for sending to an HTTP server (the tag is
         * quoted, with a conditional W prefix).
         */
        """
        pass

    def getTag(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_tag(HTTPEntityTag self)
        
        /**
         * Returns the tag as a literal string.
         */
        """
        pass

    def get_string(self, HTTPEntityTag_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_string(HTTPEntityTag self)
        
        /**
         * Returns the entity tag formatted for sending to an HTTP server (the tag is
         * quoted, with a conditional W prefix).
         */
        """
        pass

    def get_tag(self, HTTPEntityTag_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_tag(HTTPEntityTag self)
        
        /**
         * Returns the tag as a literal string.
         */
        """
        pass

    def isWeak(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_weak(HTTPEntityTag self)
        
        /**
         * Returns true if the entity tag is marked as "weak". A consistent weak
         * entity tag does not guarantee that its resource has not changed in any way,
         * but it does promise that the resource has not changed in any semantically
         * meaningful way.
         */
        """
        pass

    def is_weak(self, HTTPEntityTag_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_weak(HTTPEntityTag self)
        
        /**
         * Returns true if the entity tag is marked as "weak". A consistent weak
         * entity tag does not guarantee that its resource has not changed in any way,
         * but it does promise that the resource has not changed in any semantically
         * meaningful way.
         */
        """
        pass

    def output(self, HTTPEntityTag_self, ostream_out): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        output(HTTPEntityTag self, ostream out)
        
        /**
         *
         */
        """
        pass

    def strongEquiv(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        strong_equiv(HTTPEntityTag self, const HTTPEntityTag other)
        
        /**
         * Returns true if the two tags have "strong" equivalence: they are the same
         * tag, and both are "strong".
         */
        """
        pass

    def strong_equiv(self, HTTPEntityTag_self, const_HTTPEntityTag_other): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        strong_equiv(HTTPEntityTag self, const HTTPEntityTag other)
        
        /**
         * Returns true if the two tags have "strong" equivalence: they are the same
         * tag, and both are "strong".
         */
        """
        pass

    def weakEquiv(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        weak_equiv(HTTPEntityTag self, const HTTPEntityTag other)
        
        /**
         * Returns true if the two tags have "weak" equivalence: they are the same
         * tag, and one or both may be "weak".
         */
        """
        pass

    def weak_equiv(self, HTTPEntityTag_self, const_HTTPEntityTag_other): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        weak_equiv(HTTPEntityTag self, const HTTPEntityTag other)
        
        /**
         * Returns true if the two tags have "weak" equivalence: they are the same
         * tag, and one or both may be "weak".
         */
        """
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

    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.core.HTTPEntityTag' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.core.HTTPEntityTag' objects>"
        '__doc__': '/**\n * A container for an "entity tag" from an HTTP server.  This is used to\n * identify a particular version of a document or resource, particularly\n * useful for verifying caches.\n */',
        '__eq__': None, # (!) real value is "<slot wrapper '__eq__' of 'panda3d.core.HTTPEntityTag' objects>"
        '__ge__': None, # (!) real value is "<slot wrapper '__ge__' of 'panda3d.core.HTTPEntityTag' objects>"
        '__gt__': None, # (!) real value is "<slot wrapper '__gt__' of 'panda3d.core.HTTPEntityTag' objects>"
        '__hash__': None, # (!) real value is "<slot wrapper '__hash__' of 'panda3d.core.HTTPEntityTag' objects>"
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.HTTPEntityTag' objects>"
        '__le__': None, # (!) real value is "<slot wrapper '__le__' of 'panda3d.core.HTTPEntityTag' objects>"
        '__lt__': None, # (!) real value is "<slot wrapper '__lt__' of 'panda3d.core.HTTPEntityTag' objects>"
        '__ne__': None, # (!) real value is "<slot wrapper '__ne__' of 'panda3d.core.HTTPEntityTag' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE26CAE0>'
        '__repr__': None, # (!) real value is "<slot wrapper '__repr__' of 'panda3d.core.HTTPEntityTag' objects>"
        '__str__': None, # (!) real value is "<slot wrapper '__str__' of 'panda3d.core.HTTPEntityTag' objects>"
        'assign': None, # (!) real value is "<method 'assign' of 'panda3d.core.HTTPEntityTag' objects>"
        'compareTo': None, # (!) real value is "<method 'compareTo' of 'panda3d.core.HTTPEntityTag' objects>"
        'compare_to': None, # (!) real value is "<method 'compare_to' of 'panda3d.core.HTTPEntityTag' objects>"
        'getString': None, # (!) real value is "<method 'getString' of 'panda3d.core.HTTPEntityTag' objects>"
        'getTag': None, # (!) real value is "<method 'getTag' of 'panda3d.core.HTTPEntityTag' objects>"
        'get_string': None, # (!) real value is "<method 'get_string' of 'panda3d.core.HTTPEntityTag' objects>"
        'get_tag': None, # (!) real value is "<method 'get_tag' of 'panda3d.core.HTTPEntityTag' objects>"
        'isWeak': None, # (!) real value is "<method 'isWeak' of 'panda3d.core.HTTPEntityTag' objects>"
        'is_weak': None, # (!) real value is "<method 'is_weak' of 'panda3d.core.HTTPEntityTag' objects>"
        'output': None, # (!) real value is "<method 'output' of 'panda3d.core.HTTPEntityTag' objects>"
        'strongEquiv': None, # (!) real value is "<method 'strongEquiv' of 'panda3d.core.HTTPEntityTag' objects>"
        'strong_equiv': None, # (!) real value is "<method 'strong_equiv' of 'panda3d.core.HTTPEntityTag' objects>"
        'weakEquiv': None, # (!) real value is "<method 'weakEquiv' of 'panda3d.core.HTTPEntityTag' objects>"
        'weak_equiv': None, # (!) real value is "<method 'weak_equiv' of 'panda3d.core.HTTPEntityTag' objects>"
    }


