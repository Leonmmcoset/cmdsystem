# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


class HTTPCookie(__dtoolconfig.DTOOL_SUPER_BASE):
    """
    /**
     * A cookie sent from an HTTP server to be stored on the client and returned
     * when the path and/or domain matches.
     */
    """
    def clearExpires(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_expires(const HTTPCookie self)
        
        /**
         * Removes the expiration date on the cookie.
         */
        """
        pass

    def clear_expires(self, const_HTTPCookie_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_expires(const HTTPCookie self)
        
        /**
         * Removes the expiration date on the cookie.
         */
        """
        pass

    def getDomain(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_domain(HTTPCookie self)
        
        /**
         *
         */
        """
        pass

    def getExpires(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_expires(HTTPCookie self)
        
        /**
         * Returns the expiration date of the cookie if it is set, or an invalid date
         * if it is not.
         */
        """
        pass

    def getName(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_name(HTTPCookie self)
        
        /**
         * Returns the name of the cookie.  This is the key value specified by the
         * server.
         */
        """
        pass

    def getPath(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_path(HTTPCookie self)
        
        /**
         * Returns the prefix of the URL paths on the server for which this cookie
         * will be sent.
         */
        """
        pass

    def getSecure(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_secure(HTTPCookie self)
        
        /**
         * Returns true if the server has indicated this is a "secure" cookie which
         * should only be sent over an HTTPS channel.
         */
        """
        pass

    def getValue(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_value(HTTPCookie self)
        
        /**
         * Returns the value of the cookie.  This is the arbitrary string associated
         * with the cookie's name, as specified by the server.
         */
        """
        pass

    def get_domain(self, HTTPCookie_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_domain(HTTPCookie self)
        
        /**
         *
         */
        """
        pass

    def get_expires(self, HTTPCookie_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_expires(HTTPCookie self)
        
        /**
         * Returns the expiration date of the cookie if it is set, or an invalid date
         * if it is not.
         */
        """
        pass

    def get_name(self, HTTPCookie_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_name(HTTPCookie self)
        
        /**
         * Returns the name of the cookie.  This is the key value specified by the
         * server.
         */
        """
        pass

    def get_path(self, HTTPCookie_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_path(HTTPCookie self)
        
        /**
         * Returns the prefix of the URL paths on the server for which this cookie
         * will be sent.
         */
        """
        pass

    def get_secure(self, HTTPCookie_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_secure(HTTPCookie self)
        
        /**
         * Returns true if the server has indicated this is a "secure" cookie which
         * should only be sent over an HTTPS channel.
         */
        """
        pass

    def get_value(self, HTTPCookie_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_value(HTTPCookie self)
        
        /**
         * Returns the value of the cookie.  This is the arbitrary string associated
         * with the cookie's name, as specified by the server.
         */
        """
        pass

    def hasExpires(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_expires(HTTPCookie self)
        
        /**
         * Returns true if the cookie has an expiration date, false otherwise.
         */
        """
        pass

    def has_expires(self, HTTPCookie_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_expires(HTTPCookie self)
        
        /**
         * Returns true if the cookie has an expiration date, false otherwise.
         */
        """
        pass

    def isExpired(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_expired(HTTPCookie self, const HTTPDate now)
        
        /**
         * Returns true if the cookie's expiration date is before the indicated date,
         * false otherwise.
         */
        """
        pass

    def is_expired(self, HTTPCookie_self, const_HTTPDate_now): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_expired(HTTPCookie self, const HTTPDate now)
        
        /**
         * Returns true if the cookie's expiration date is before the indicated date,
         * false otherwise.
         */
        """
        pass

    def matchesUrl(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        matches_url(HTTPCookie self, const URLSpec url)
        
        /**
         * Returns true if the cookie is appropriate to send with the indicated URL
         * request, false otherwise.
         */
        """
        pass

    def matches_url(self, HTTPCookie_self, const_URLSpec_url): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        matches_url(HTTPCookie self, const URLSpec url)
        
        /**
         * Returns true if the cookie is appropriate to send with the indicated URL
         * request, false otherwise.
         */
        """
        pass

    def output(self, HTTPCookie_self, ostream_out): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        output(HTTPCookie self, ostream out)
        
        /**
         *
         */
        """
        pass

    def parseSetCookie(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        parse_set_cookie(const HTTPCookie self, str format, const URLSpec url)
        
        /**
         * Separates out the parameter/value pairs of the Set-Cookie header and
         * assigns the values of the cookie appropriate.  Returns true if the header
         * is parsed correctly, false if something is not understood.
         */
        """
        pass

    def parse_set_cookie(self, const_HTTPCookie_self, str_format, const_URLSpec_url): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        parse_set_cookie(const HTTPCookie self, str format, const URLSpec url)
        
        /**
         * Separates out the parameter/value pairs of the Set-Cookie header and
         * assigns the values of the cookie appropriate.  Returns true if the header
         * is parsed correctly, false if something is not understood.
         */
        """
        pass

    def setDomain(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_domain(const HTTPCookie self, str domain)
        
        /**
         *
         */
        """
        pass

    def setExpires(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_expires(const HTTPCookie self, const HTTPDate expires)
        
        /**
         *
         */
        """
        pass

    def setName(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_name(const HTTPCookie self, str name)
        
        /**
         *
         */
        """
        pass

    def setPath(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_path(const HTTPCookie self, str path)
        
        /**
         *
         */
        """
        pass

    def setSecure(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_secure(const HTTPCookie self, bool flag)
        
        /**
         *
         */
        """
        pass

    def setValue(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_value(const HTTPCookie self, str value)
        
        /**
         *
         */
        """
        pass

    def set_domain(self, const_HTTPCookie_self, str_domain): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_domain(const HTTPCookie self, str domain)
        
        /**
         *
         */
        """
        pass

    def set_expires(self, const_HTTPCookie_self, const_HTTPDate_expires): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_expires(const HTTPCookie self, const HTTPDate expires)
        
        /**
         *
         */
        """
        pass

    def set_name(self, const_HTTPCookie_self, str_name): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_name(const HTTPCookie self, str name)
        
        /**
         *
         */
        """
        pass

    def set_path(self, const_HTTPCookie_self, str_path): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_path(const HTTPCookie self, str path)
        
        /**
         *
         */
        """
        pass

    def set_secure(self, const_HTTPCookie_self, bool_flag): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_secure(const HTTPCookie self, bool flag)
        
        /**
         *
         */
        """
        pass

    def set_value(self, const_HTTPCookie_self, str_value): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_value(const HTTPCookie self, str value)
        
        /**
         *
         */
        """
        pass

    def updateFrom(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        update_from(const HTTPCookie self, const HTTPCookie other)
        
        /**
         * Assuming the operator < method, above, has already evaluated these two
         * cookies as equal, then assign the remaining values (value, expiration date,
         * secure flag) from the indicated cookie.  This is guaranteed not to change
         * the ordering of the cookie in a set, and so can be used to update an
         * existing cookie within a set with new values.
         */
        """
        pass

    def update_from(self, const_HTTPCookie_self, const_HTTPCookie_other): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        update_from(const HTTPCookie self, const HTTPCookie other)
        
        /**
         * Assuming the operator < method, above, has already evaluated these two
         * cookies as equal, then assign the remaining values (value, expiration date,
         * secure flag) from the indicated cookie.  This is guaranteed not to change
         * the ordering of the cookie in a set, and so can be used to update an
         * existing cookie within a set with new values.
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

    domain = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    expires = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    path = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    secure = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.core.HTTPCookie' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.core.HTTPCookie' objects>"
        '__doc__': '/**\n * A cookie sent from an HTTP server to be stored on the client and returned\n * when the path and/or domain matches.\n */',
        '__eq__': None, # (!) real value is "<slot wrapper '__eq__' of 'panda3d.core.HTTPCookie' objects>"
        '__ge__': None, # (!) real value is "<slot wrapper '__ge__' of 'panda3d.core.HTTPCookie' objects>"
        '__gt__': None, # (!) real value is "<slot wrapper '__gt__' of 'panda3d.core.HTTPCookie' objects>"
        '__hash__': None, # (!) real value is "<slot wrapper '__hash__' of 'panda3d.core.HTTPCookie' objects>"
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.HTTPCookie' objects>"
        '__le__': None, # (!) real value is "<slot wrapper '__le__' of 'panda3d.core.HTTPCookie' objects>"
        '__lt__': None, # (!) real value is "<slot wrapper '__lt__' of 'panda3d.core.HTTPCookie' objects>"
        '__ne__': None, # (!) real value is "<slot wrapper '__ne__' of 'panda3d.core.HTTPCookie' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE26C740>'
        '__repr__': None, # (!) real value is "<slot wrapper '__repr__' of 'panda3d.core.HTTPCookie' objects>"
        '__str__': None, # (!) real value is "<slot wrapper '__str__' of 'panda3d.core.HTTPCookie' objects>"
        'clearExpires': None, # (!) real value is "<method 'clearExpires' of 'panda3d.core.HTTPCookie' objects>"
        'clear_expires': None, # (!) real value is "<method 'clear_expires' of 'panda3d.core.HTTPCookie' objects>"
        'domain': None, # (!) real value is "<attribute 'domain' of 'panda3d.core.HTTPCookie' objects>"
        'expires': None, # (!) real value is "<attribute 'expires' of 'panda3d.core.HTTPCookie' objects>"
        'getDomain': None, # (!) real value is "<method 'getDomain' of 'panda3d.core.HTTPCookie' objects>"
        'getExpires': None, # (!) real value is "<method 'getExpires' of 'panda3d.core.HTTPCookie' objects>"
        'getName': None, # (!) real value is "<method 'getName' of 'panda3d.core.HTTPCookie' objects>"
        'getPath': None, # (!) real value is "<method 'getPath' of 'panda3d.core.HTTPCookie' objects>"
        'getSecure': None, # (!) real value is "<method 'getSecure' of 'panda3d.core.HTTPCookie' objects>"
        'getValue': None, # (!) real value is "<method 'getValue' of 'panda3d.core.HTTPCookie' objects>"
        'get_domain': None, # (!) real value is "<method 'get_domain' of 'panda3d.core.HTTPCookie' objects>"
        'get_expires': None, # (!) real value is "<method 'get_expires' of 'panda3d.core.HTTPCookie' objects>"
        'get_name': None, # (!) real value is "<method 'get_name' of 'panda3d.core.HTTPCookie' objects>"
        'get_path': None, # (!) real value is "<method 'get_path' of 'panda3d.core.HTTPCookie' objects>"
        'get_secure': None, # (!) real value is "<method 'get_secure' of 'panda3d.core.HTTPCookie' objects>"
        'get_value': None, # (!) real value is "<method 'get_value' of 'panda3d.core.HTTPCookie' objects>"
        'hasExpires': None, # (!) real value is "<method 'hasExpires' of 'panda3d.core.HTTPCookie' objects>"
        'has_expires': None, # (!) real value is "<method 'has_expires' of 'panda3d.core.HTTPCookie' objects>"
        'isExpired': None, # (!) real value is "<method 'isExpired' of 'panda3d.core.HTTPCookie' objects>"
        'is_expired': None, # (!) real value is "<method 'is_expired' of 'panda3d.core.HTTPCookie' objects>"
        'matchesUrl': None, # (!) real value is "<method 'matchesUrl' of 'panda3d.core.HTTPCookie' objects>"
        'matches_url': None, # (!) real value is "<method 'matches_url' of 'panda3d.core.HTTPCookie' objects>"
        'name': None, # (!) real value is "<attribute 'name' of 'panda3d.core.HTTPCookie' objects>"
        'output': None, # (!) real value is "<method 'output' of 'panda3d.core.HTTPCookie' objects>"
        'parseSetCookie': None, # (!) real value is "<method 'parseSetCookie' of 'panda3d.core.HTTPCookie' objects>"
        'parse_set_cookie': None, # (!) real value is "<method 'parse_set_cookie' of 'panda3d.core.HTTPCookie' objects>"
        'path': None, # (!) real value is "<attribute 'path' of 'panda3d.core.HTTPCookie' objects>"
        'secure': None, # (!) real value is "<attribute 'secure' of 'panda3d.core.HTTPCookie' objects>"
        'setDomain': None, # (!) real value is "<method 'setDomain' of 'panda3d.core.HTTPCookie' objects>"
        'setExpires': None, # (!) real value is "<method 'setExpires' of 'panda3d.core.HTTPCookie' objects>"
        'setName': None, # (!) real value is "<method 'setName' of 'panda3d.core.HTTPCookie' objects>"
        'setPath': None, # (!) real value is "<method 'setPath' of 'panda3d.core.HTTPCookie' objects>"
        'setSecure': None, # (!) real value is "<method 'setSecure' of 'panda3d.core.HTTPCookie' objects>"
        'setValue': None, # (!) real value is "<method 'setValue' of 'panda3d.core.HTTPCookie' objects>"
        'set_domain': None, # (!) real value is "<method 'set_domain' of 'panda3d.core.HTTPCookie' objects>"
        'set_expires': None, # (!) real value is "<method 'set_expires' of 'panda3d.core.HTTPCookie' objects>"
        'set_name': None, # (!) real value is "<method 'set_name' of 'panda3d.core.HTTPCookie' objects>"
        'set_path': None, # (!) real value is "<method 'set_path' of 'panda3d.core.HTTPCookie' objects>"
        'set_secure': None, # (!) real value is "<method 'set_secure' of 'panda3d.core.HTTPCookie' objects>"
        'set_value': None, # (!) real value is "<method 'set_value' of 'panda3d.core.HTTPCookie' objects>"
        'updateFrom': None, # (!) real value is "<method 'updateFrom' of 'panda3d.core.HTTPCookie' objects>"
        'update_from': None, # (!) real value is "<method 'update_from' of 'panda3d.core.HTTPCookie' objects>"
        'value': None, # (!) real value is "<attribute 'value' of 'panda3d.core.HTTPCookie' objects>"
    }


