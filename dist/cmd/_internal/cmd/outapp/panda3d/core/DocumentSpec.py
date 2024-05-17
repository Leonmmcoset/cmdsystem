# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


class DocumentSpec(__dtoolconfig.DTOOL_SUPER_BASE):
    """
    /**
     * A descriptor that refers to a particular version of a document.  This
     * includes the URL of the document and its identity tag and last-modified
     * dates.
     *
     * The DocumentSpec may also be used to request a newer document than a
     * particular one if available, for instance to refresh a cached document.
     */
    """
    def assign(self, const_DocumentSpec_self, const_DocumentSpec_copy): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        assign(const DocumentSpec self, const DocumentSpec copy)
        """
        pass

    def clearDate(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_date(const DocumentSpec self)
        
        /**
         * Removes the last-modified date associated with the DocumentSpec, if there
         * is one.
         */
        """
        pass

    def clearTag(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_tag(const DocumentSpec self)
        
        /**
         * Removes the identity tag associated with the DocumentSpec, if there is one.
         */
        """
        pass

    def clear_date(self, const_DocumentSpec_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_date(const DocumentSpec self)
        
        /**
         * Removes the last-modified date associated with the DocumentSpec, if there
         * is one.
         */
        """
        pass

    def clear_tag(self, const_DocumentSpec_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_tag(const DocumentSpec self)
        
        /**
         * Removes the identity tag associated with the DocumentSpec, if there is one.
         */
        """
        pass

    def compareTo(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        compare_to(DocumentSpec self, const DocumentSpec other)
        
        /**
         *
         */
        """
        pass

    def compare_to(self, DocumentSpec_self, const_DocumentSpec_other): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        compare_to(DocumentSpec self, const DocumentSpec other)
        
        /**
         *
         */
        """
        pass

    def getCacheControl(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_cache_control(DocumentSpec self)
        
        /**
         * Returns the request mode of this DocumentSpec.  See set_cache_control().
         */
        """
        pass

    def getDate(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_date(DocumentSpec self)
        
        /**
         * Returns the last-modified date associated with the DocumentSpec, if there
         * is one.  It is an error to call this if has_date() returns false.
         */
        """
        pass

    def getRequestMode(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_request_mode(DocumentSpec self)
        
        /**
         * Returns the request mode of this DocumentSpec.  See set_request_mode().
         */
        """
        pass

    def getTag(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_tag(DocumentSpec self)
        
        /**
         * Returns the identity tag associated with the DocumentSpec, if there is one.
         * It is an error to call this if has_tag() returns false.
         *
         * The identity tag is set by the HTTP server to uniquely refer to a
         * particular version of a document.
         */
        """
        pass

    def getUrl(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_url(DocumentSpec self)
        
        /**
         * Retrieves the URL of the DocumentSpec.
         */
        """
        pass

    def get_cache_control(self, DocumentSpec_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_cache_control(DocumentSpec self)
        
        /**
         * Returns the request mode of this DocumentSpec.  See set_cache_control().
         */
        """
        pass

    def get_date(self, DocumentSpec_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_date(DocumentSpec self)
        
        /**
         * Returns the last-modified date associated with the DocumentSpec, if there
         * is one.  It is an error to call this if has_date() returns false.
         */
        """
        pass

    def get_request_mode(self, DocumentSpec_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_request_mode(DocumentSpec self)
        
        /**
         * Returns the request mode of this DocumentSpec.  See set_request_mode().
         */
        """
        pass

    def get_tag(self, DocumentSpec_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_tag(DocumentSpec self)
        
        /**
         * Returns the identity tag associated with the DocumentSpec, if there is one.
         * It is an error to call this if has_tag() returns false.
         *
         * The identity tag is set by the HTTP server to uniquely refer to a
         * particular version of a document.
         */
        """
        pass

    def get_url(self, DocumentSpec_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_url(DocumentSpec self)
        
        /**
         * Retrieves the URL of the DocumentSpec.
         */
        """
        pass

    def hasDate(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_date(DocumentSpec self)
        
        /**
         * Returns true if a last-modified date is associated with the DocumentSpec.
         */
        """
        pass

    def hasTag(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_tag(DocumentSpec self)
        
        /**
         * Returns true if an identity tag is associated with the DocumentSpec.
         */
        """
        pass

    def has_date(self, DocumentSpec_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_date(DocumentSpec self)
        
        /**
         * Returns true if a last-modified date is associated with the DocumentSpec.
         */
        """
        pass

    def has_tag(self, DocumentSpec_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_tag(DocumentSpec self)
        
        /**
         * Returns true if an identity tag is associated with the DocumentSpec.
         */
        """
        pass

    def input(self, const_DocumentSpec_self, istream_in): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        input(const DocumentSpec self, istream in)
        
        /**
         * Can be used to read in the DocumentSpec from a stream generated either by
         * output() or write().  Returns true on success, false on failure.
         */
        """
        pass

    def output(self, DocumentSpec_self, ostream_out): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        output(DocumentSpec self, ostream out)
        
        /**
         *
         */
        """
        pass

    def setCacheControl(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_cache_control(const DocumentSpec self, int cache_control)
        
        /**
         * Specifies what kind of cached value is acceptable for this document.
         * Warning: some HTTP proxies may not respect this setting and may return a
         * cached result anyway.
         *
         * CC_allow_cache: the normal HTTP behavior; the server may return a cached
         * value if it believes it is valid.
         *
         * CC_revalidate: a proxy is forced to contact the origin server and verify
         * that is cached value is in fact still valid before it returns it.
         *
         * CC_no_cache: a proxy must not return its cached value at all, but is forced
         * to go all the way back to the origin server for the official document.
         *
         * The default mode is CC_allow_cache.
         */
        """
        pass

    def setDate(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_date(const DocumentSpec self, const HTTPDate date)
        
        /**
         * Changes the last-modified date associated with the DocumentSpec.
         */
        """
        pass

    def setRequestMode(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_request_mode(const DocumentSpec self, int request_mode)
        
        /**
         * Sets the request mode of this DocumentSpec.  This is only relevant when
         * using the DocumentSpec to generate a request (for instance, in
         * HTTPChannel).  This specifies whether the document request will ask the
         * server for a newer version than the indicated version, or the exact
         * version, neither, or either.
         *
         * The possible values are:
         *
         * RM_any: ignore date and tag (if specified), and retrieve any document that
         * matches the URL.  For a subrange request, if the document matches the
         * version indicated exactly, retrieve the subrange only; otherwise, retrieve
         * the entire document.
         *
         * RM_equal: request only the precise version of the document that matches the
         * particular date and/or tag exactly, if specified; fail if this version is
         * not available.
         *
         * RM_newer: request any document that is newer than the version indicated by
         * the particular date and/or tag; fail if only that version (or older
         * versions) are available.
         *
         * RM_newer_or_equal: request any document that matches the version indicated
         * by the particular date and/or tag, or is a newer version; fail if only
         * older versions are available.
         *
         * In any of the above, you may specify either or both of the last-modified
         * date and the identity tag, whichever is known to the client.
         *
         * The default mode is RM_any.
         */
        """
        pass

    def setTag(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_tag(const DocumentSpec self, const HTTPEntityTag tag)
        
        /**
         * Changes the identity tag associated with the DocumentSpec.
         */
        """
        pass

    def setUrl(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_url(const DocumentSpec self, const URLSpec url)
        
        /**
         * Changes the URL of the DocumentSpec without modifying its other properties.
         * Normally this would be a strange thing to do, because the tag and date are
         * usually strongly associated with the URL.  To get a DocumentSpec pointing
         * to a new URL, you would normally create a new DocumentSpec object.
         */
        """
        pass

    def set_cache_control(self, const_DocumentSpec_self, int_cache_control): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_cache_control(const DocumentSpec self, int cache_control)
        
        /**
         * Specifies what kind of cached value is acceptable for this document.
         * Warning: some HTTP proxies may not respect this setting and may return a
         * cached result anyway.
         *
         * CC_allow_cache: the normal HTTP behavior; the server may return a cached
         * value if it believes it is valid.
         *
         * CC_revalidate: a proxy is forced to contact the origin server and verify
         * that is cached value is in fact still valid before it returns it.
         *
         * CC_no_cache: a proxy must not return its cached value at all, but is forced
         * to go all the way back to the origin server for the official document.
         *
         * The default mode is CC_allow_cache.
         */
        """
        pass

    def set_date(self, const_DocumentSpec_self, const_HTTPDate_date): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_date(const DocumentSpec self, const HTTPDate date)
        
        /**
         * Changes the last-modified date associated with the DocumentSpec.
         */
        """
        pass

    def set_request_mode(self, const_DocumentSpec_self, int_request_mode): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_request_mode(const DocumentSpec self, int request_mode)
        
        /**
         * Sets the request mode of this DocumentSpec.  This is only relevant when
         * using the DocumentSpec to generate a request (for instance, in
         * HTTPChannel).  This specifies whether the document request will ask the
         * server for a newer version than the indicated version, or the exact
         * version, neither, or either.
         *
         * The possible values are:
         *
         * RM_any: ignore date and tag (if specified), and retrieve any document that
         * matches the URL.  For a subrange request, if the document matches the
         * version indicated exactly, retrieve the subrange only; otherwise, retrieve
         * the entire document.
         *
         * RM_equal: request only the precise version of the document that matches the
         * particular date and/or tag exactly, if specified; fail if this version is
         * not available.
         *
         * RM_newer: request any document that is newer than the version indicated by
         * the particular date and/or tag; fail if only that version (or older
         * versions) are available.
         *
         * RM_newer_or_equal: request any document that matches the version indicated
         * by the particular date and/or tag, or is a newer version; fail if only
         * older versions are available.
         *
         * In any of the above, you may specify either or both of the last-modified
         * date and the identity tag, whichever is known to the client.
         *
         * The default mode is RM_any.
         */
        """
        pass

    def set_tag(self, const_DocumentSpec_self, const_HTTPEntityTag_tag): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_tag(const DocumentSpec self, const HTTPEntityTag tag)
        
        /**
         * Changes the identity tag associated with the DocumentSpec.
         */
        """
        pass

    def set_url(self, const_DocumentSpec_self, const_URLSpec_url): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_url(const DocumentSpec self, const URLSpec url)
        
        /**
         * Changes the URL of the DocumentSpec without modifying its other properties.
         * Normally this would be a strange thing to do, because the tag and date are
         * usually strongly associated with the URL.  To get a DocumentSpec pointing
         * to a new URL, you would normally create a new DocumentSpec object.
         */
        """
        pass

    def write(self, DocumentSpec_self, ostream_out, int_indent_level): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        write(DocumentSpec self, ostream out, int indent_level)
        
        /**
         *
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

    cache_control = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    date = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    request_mode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tag = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    url = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    CCAllowCache = 0
    CCNoCache = 2
    CCRevalidate = 1
    CC_allow_cache = 0
    CC_no_cache = 2
    CC_revalidate = 1
    DtoolClassDict = {
        'CCAllowCache': 0,
        'CCNoCache': 2,
        'CCRevalidate': 1,
        'CC_allow_cache': 0,
        'CC_no_cache': 2,
        'CC_revalidate': 1,
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        'RMAny': 0,
        'RMEqual': 1,
        'RMEqualOrNewer': 3,
        'RMNewer': 2,
        'RM_any': 0,
        'RM_equal': 1,
        'RM_equal_or_newer': 3,
        'RM_newer': 2,
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.core.DocumentSpec' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.core.DocumentSpec' objects>"
        '__doc__': '/**\n * A descriptor that refers to a particular version of a document.  This\n * includes the URL of the document and its identity tag and last-modified\n * dates.\n *\n * The DocumentSpec may also be used to request a newer document than a\n * particular one if available, for instance to refresh a cached document.\n */',
        '__eq__': None, # (!) real value is "<slot wrapper '__eq__' of 'panda3d.core.DocumentSpec' objects>"
        '__ge__': None, # (!) real value is "<slot wrapper '__ge__' of 'panda3d.core.DocumentSpec' objects>"
        '__gt__': None, # (!) real value is "<slot wrapper '__gt__' of 'panda3d.core.DocumentSpec' objects>"
        '__hash__': None, # (!) real value is "<slot wrapper '__hash__' of 'panda3d.core.DocumentSpec' objects>"
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.DocumentSpec' objects>"
        '__le__': None, # (!) real value is "<slot wrapper '__le__' of 'panda3d.core.DocumentSpec' objects>"
        '__lt__': None, # (!) real value is "<slot wrapper '__lt__' of 'panda3d.core.DocumentSpec' objects>"
        '__ne__': None, # (!) real value is "<slot wrapper '__ne__' of 'panda3d.core.DocumentSpec' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE26CCB0>'
        '__repr__': None, # (!) real value is "<slot wrapper '__repr__' of 'panda3d.core.DocumentSpec' objects>"
        '__str__': None, # (!) real value is "<slot wrapper '__str__' of 'panda3d.core.DocumentSpec' objects>"
        'assign': None, # (!) real value is "<method 'assign' of 'panda3d.core.DocumentSpec' objects>"
        'cache_control': None, # (!) real value is "<attribute 'cache_control' of 'panda3d.core.DocumentSpec' objects>"
        'clearDate': None, # (!) real value is "<method 'clearDate' of 'panda3d.core.DocumentSpec' objects>"
        'clearTag': None, # (!) real value is "<method 'clearTag' of 'panda3d.core.DocumentSpec' objects>"
        'clear_date': None, # (!) real value is "<method 'clear_date' of 'panda3d.core.DocumentSpec' objects>"
        'clear_tag': None, # (!) real value is "<method 'clear_tag' of 'panda3d.core.DocumentSpec' objects>"
        'compareTo': None, # (!) real value is "<method 'compareTo' of 'panda3d.core.DocumentSpec' objects>"
        'compare_to': None, # (!) real value is "<method 'compare_to' of 'panda3d.core.DocumentSpec' objects>"
        'date': None, # (!) real value is "<attribute 'date' of 'panda3d.core.DocumentSpec' objects>"
        'getCacheControl': None, # (!) real value is "<method 'getCacheControl' of 'panda3d.core.DocumentSpec' objects>"
        'getDate': None, # (!) real value is "<method 'getDate' of 'panda3d.core.DocumentSpec' objects>"
        'getRequestMode': None, # (!) real value is "<method 'getRequestMode' of 'panda3d.core.DocumentSpec' objects>"
        'getTag': None, # (!) real value is "<method 'getTag' of 'panda3d.core.DocumentSpec' objects>"
        'getUrl': None, # (!) real value is "<method 'getUrl' of 'panda3d.core.DocumentSpec' objects>"
        'get_cache_control': None, # (!) real value is "<method 'get_cache_control' of 'panda3d.core.DocumentSpec' objects>"
        'get_date': None, # (!) real value is "<method 'get_date' of 'panda3d.core.DocumentSpec' objects>"
        'get_request_mode': None, # (!) real value is "<method 'get_request_mode' of 'panda3d.core.DocumentSpec' objects>"
        'get_tag': None, # (!) real value is "<method 'get_tag' of 'panda3d.core.DocumentSpec' objects>"
        'get_url': None, # (!) real value is "<method 'get_url' of 'panda3d.core.DocumentSpec' objects>"
        'hasDate': None, # (!) real value is "<method 'hasDate' of 'panda3d.core.DocumentSpec' objects>"
        'hasTag': None, # (!) real value is "<method 'hasTag' of 'panda3d.core.DocumentSpec' objects>"
        'has_date': None, # (!) real value is "<method 'has_date' of 'panda3d.core.DocumentSpec' objects>"
        'has_tag': None, # (!) real value is "<method 'has_tag' of 'panda3d.core.DocumentSpec' objects>"
        'input': None, # (!) real value is "<method 'input' of 'panda3d.core.DocumentSpec' objects>"
        'output': None, # (!) real value is "<method 'output' of 'panda3d.core.DocumentSpec' objects>"
        'request_mode': None, # (!) real value is "<attribute 'request_mode' of 'panda3d.core.DocumentSpec' objects>"
        'setCacheControl': None, # (!) real value is "<method 'setCacheControl' of 'panda3d.core.DocumentSpec' objects>"
        'setDate': None, # (!) real value is "<method 'setDate' of 'panda3d.core.DocumentSpec' objects>"
        'setRequestMode': None, # (!) real value is "<method 'setRequestMode' of 'panda3d.core.DocumentSpec' objects>"
        'setTag': None, # (!) real value is "<method 'setTag' of 'panda3d.core.DocumentSpec' objects>"
        'setUrl': None, # (!) real value is "<method 'setUrl' of 'panda3d.core.DocumentSpec' objects>"
        'set_cache_control': None, # (!) real value is "<method 'set_cache_control' of 'panda3d.core.DocumentSpec' objects>"
        'set_date': None, # (!) real value is "<method 'set_date' of 'panda3d.core.DocumentSpec' objects>"
        'set_request_mode': None, # (!) real value is "<method 'set_request_mode' of 'panda3d.core.DocumentSpec' objects>"
        'set_tag': None, # (!) real value is "<method 'set_tag' of 'panda3d.core.DocumentSpec' objects>"
        'set_url': None, # (!) real value is "<method 'set_url' of 'panda3d.core.DocumentSpec' objects>"
        'tag': None, # (!) real value is "<attribute 'tag' of 'panda3d.core.DocumentSpec' objects>"
        'url': None, # (!) real value is "<attribute 'url' of 'panda3d.core.DocumentSpec' objects>"
        'write': None, # (!) real value is "<method 'write' of 'panda3d.core.DocumentSpec' objects>"
    }
    RMAny = 0
    RMEqual = 1
    RMEqualOrNewer = 3
    RMNewer = 2
    RM_any = 0
    RM_equal = 1
    RM_equal_or_newer = 3
    RM_newer = 2


