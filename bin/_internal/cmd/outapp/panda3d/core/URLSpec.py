# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


class URLSpec(__dtoolconfig.DTOOL_SUPER_BASE):
    """
    /**
     * A container for a URL, e.g.  "http://server:port/path".
     *
     * The URLSpec object is similar to a Filename in that it contains logic to
     * identify the various parts of a URL and return (or modify) them separately.
     */
    """
    def assign(self, const_URLSpec_self, str_url): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        assign(const URLSpec self, str url)
        """
        pass

    def compareTo(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        compare_to(URLSpec self, const URLSpec other)
        
        /**
         * Returns a number less than zero if this URLSpec sorts before the other one,
         * greater than zero if it sorts after, or zero if they are equivalent.
         */
        """
        pass

    def compare_to(self, URLSpec_self, const_URLSpec_other): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        compare_to(URLSpec self, const URLSpec other)
        
        /**
         * Returns a number less than zero if this URLSpec sorts before the other one,
         * greater than zero if it sorts after, or zero if they are equivalent.
         */
        """
        pass

    def cStr(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        c_str(URLSpec self)
        
        /**
         *
         */
        """
        pass

    def c_str(self, URLSpec_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        c_str(URLSpec self)
        
        /**
         *
         */
        """
        pass

    def empty(self, URLSpec_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        empty(URLSpec self)
        
        /**
         * Returns false if the URLSpec is valid (not empty), or true if it is an
         * empty string.
         */
        """
        pass

    def getAuthority(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_authority(URLSpec self)
        
        /**
         * Returns the authority specified by the URL (this includes username, server,
         * and/or port), or empty string if no authority is specified.
         */
        """
        pass

    def getDefaultPortForScheme(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_default_port_for_scheme(str scheme)
        
        /**
         * Returns the default port number for the indicated scheme, or 0 if there is
         * no known default.
         */
        """
        pass

    def getHash(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_hash(URLSpec self)
        
        /**
         *
         */
        """
        pass

    def getPath(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_path(URLSpec self)
        
        /**
         * Returns the path specified by the URL, or "/" if no path is specified.
         */
        """
        pass

    def getPathAndQuery(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_path_and_query(URLSpec self)
        
        /**
         * Returns the path (or "/" if no path is specified), followed by the query if
         * it is specified.
         */
        """
        pass

    def getPort(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_port(URLSpec self)
        
        /**
         * Returns the port number specified by the URL, or the default port if not
         * specified.
         */
        """
        pass

    def getPortStr(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_port_str(URLSpec self)
        
        /**
         * Returns the port specified by the URL as a string, or the empty string if
         * no port is specified.  Compare this with get_port(), which returns a
         * default port number if no port is specified.
         */
        """
        pass

    def getQuery(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_query(URLSpec self)
        
        /**
         * Returns the query specified by the URL, or empty string if no query is
         * specified.
         */
        """
        pass

    def getScheme(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_scheme(URLSpec self)
        
        /**
         * Returns the scheme specified by the URL, or empty string if no scheme is
         * specified.
         */
        """
        pass

    def getServer(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_server(URLSpec self)
        
        /**
         * Returns the server name specified by the URL, if any.  In case of an IPv6
         * address, does not include the enclosing brackets.
         */
        """
        pass

    def getServerAndPort(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_server_and_port(URLSpec self)
        
        /**
         * Returns a string consisting of the server name, followed by a colon,
         * followed by the port number.  If the port number is not explicitly given in
         * the URL, this string will include the implicit port number.
         * If the server is an IPv6 address, it will be enclosed in square brackets.
         */
        """
        pass

    def getUrl(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_url(URLSpec self)
        
        /**
         * Returns the complete URL specification.
         */
        """
        pass

    def getUsername(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_username(URLSpec self)
        
        /**
         * Returns the username specified by the URL, if any.  This might also include
         * a password, e.g.  "username:password", although putting a password on the
         * URL is probably a bad idea.
         */
        """
        pass

    def get_authority(self, URLSpec_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_authority(URLSpec self)
        
        /**
         * Returns the authority specified by the URL (this includes username, server,
         * and/or port), or empty string if no authority is specified.
         */
        """
        pass

    def get_default_port_for_scheme(self, str_scheme): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_default_port_for_scheme(str scheme)
        
        /**
         * Returns the default port number for the indicated scheme, or 0 if there is
         * no known default.
         */
        """
        pass

    def get_hash(self, URLSpec_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_hash(URLSpec self)
        
        /**
         *
         */
        """
        pass

    def get_path(self, URLSpec_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_path(URLSpec self)
        
        /**
         * Returns the path specified by the URL, or "/" if no path is specified.
         */
        """
        pass

    def get_path_and_query(self, URLSpec_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_path_and_query(URLSpec self)
        
        /**
         * Returns the path (or "/" if no path is specified), followed by the query if
         * it is specified.
         */
        """
        pass

    def get_port(self, URLSpec_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_port(URLSpec self)
        
        /**
         * Returns the port number specified by the URL, or the default port if not
         * specified.
         */
        """
        pass

    def get_port_str(self, URLSpec_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_port_str(URLSpec self)
        
        /**
         * Returns the port specified by the URL as a string, or the empty string if
         * no port is specified.  Compare this with get_port(), which returns a
         * default port number if no port is specified.
         */
        """
        pass

    def get_query(self, URLSpec_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_query(URLSpec self)
        
        /**
         * Returns the query specified by the URL, or empty string if no query is
         * specified.
         */
        """
        pass

    def get_scheme(self, URLSpec_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_scheme(URLSpec self)
        
        /**
         * Returns the scheme specified by the URL, or empty string if no scheme is
         * specified.
         */
        """
        pass

    def get_server(self, URLSpec_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_server(URLSpec self)
        
        /**
         * Returns the server name specified by the URL, if any.  In case of an IPv6
         * address, does not include the enclosing brackets.
         */
        """
        pass

    def get_server_and_port(self, URLSpec_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_server_and_port(URLSpec self)
        
        /**
         * Returns a string consisting of the server name, followed by a colon,
         * followed by the port number.  If the port number is not explicitly given in
         * the URL, this string will include the implicit port number.
         * If the server is an IPv6 address, it will be enclosed in square brackets.
         */
        """
        pass

    def get_url(self, URLSpec_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_url(URLSpec self)
        
        /**
         * Returns the complete URL specification.
         */
        """
        pass

    def get_username(self, URLSpec_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_username(URLSpec self)
        
        /**
         * Returns the username specified by the URL, if any.  This might also include
         * a password, e.g.  "username:password", although putting a password on the
         * URL is probably a bad idea.
         */
        """
        pass

    def hasAuthority(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_authority(URLSpec self)
        
        /**
         * Returns true if the URL specifies an authority (this includes username,
         * server, and/or port), false otherwise.
         */
        """
        pass

    def hasPath(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_path(URLSpec self)
        
        /**
         * Returns true if the URL includes a path specification (that is, the
         * particular filename on the server to retrieve), false otherwise.
         */
        """
        pass

    def hasPort(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_port(URLSpec self)
        
        /**
         * Returns true if the URL specifies a port number, false otherwise.
         */
        """
        pass

    def hasQuery(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_query(URLSpec self)
        
        /**
         * Returns true if the URL includes a query specification, false otherwise.
         */
        """
        pass

    def hasScheme(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_scheme(URLSpec self)
        
        /**
         * Returns true if the URL specifies a scheme (e.g.  "http:"), false
         * otherwise.
         */
        """
        pass

    def hasServer(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_server(URLSpec self)
        
        /**
         * Returns true if the URL specifies a server name, false otherwise.
         */
        """
        pass

    def hasUsername(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_username(URLSpec self)
        
        /**
         * Returns true if the URL specifies a username (and/or password), false
         * otherwise.
         */
        """
        pass

    def has_authority(self, URLSpec_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_authority(URLSpec self)
        
        /**
         * Returns true if the URL specifies an authority (this includes username,
         * server, and/or port), false otherwise.
         */
        """
        pass

    def has_path(self, URLSpec_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_path(URLSpec self)
        
        /**
         * Returns true if the URL includes a path specification (that is, the
         * particular filename on the server to retrieve), false otherwise.
         */
        """
        pass

    def has_port(self, URLSpec_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_port(URLSpec self)
        
        /**
         * Returns true if the URL specifies a port number, false otherwise.
         */
        """
        pass

    def has_query(self, URLSpec_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_query(URLSpec self)
        
        /**
         * Returns true if the URL includes a query specification, false otherwise.
         */
        """
        pass

    def has_scheme(self, URLSpec_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_scheme(URLSpec self)
        
        /**
         * Returns true if the URL specifies a scheme (e.g.  "http:"), false
         * otherwise.
         */
        """
        pass

    def has_server(self, URLSpec_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_server(URLSpec self)
        
        /**
         * Returns true if the URL specifies a server name, false otherwise.
         */
        """
        pass

    def has_username(self, URLSpec_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_username(URLSpec self)
        
        /**
         * Returns true if the URL specifies a username (and/or password), false
         * otherwise.
         */
        """
        pass

    def input(self, const_URLSpec_self, istream_in): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        input(const URLSpec self, istream in)
        
        /**
         *
         */
        """
        pass

    def isDefaultPort(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_default_port(URLSpec self)
        
        /**
         * Returns true if the port number encoded in this URL is the default port
         * number for the scheme (or if there is no port number), or false if it is a
         * nonstandard port.
         */
        """
        pass

    def isSsl(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_ssl(URLSpec self)
        
        /**
         * Returns true if the URL's scheme specifies an SSL-secured protocol such as
         * https, or false otherwise.
         */
        """
        pass

    def is_default_port(self, URLSpec_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_default_port(URLSpec self)
        
        /**
         * Returns true if the port number encoded in this URL is the default port
         * number for the scheme (or if there is no port number), or false if it is a
         * nonstandard port.
         */
        """
        pass

    def is_ssl(self, URLSpec_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_ssl(URLSpec self)
        
        /**
         * Returns true if the URL's scheme specifies an SSL-secured protocol such as
         * https, or false otherwise.
         */
        """
        pass

    def length(self, URLSpec_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        length(URLSpec self)
        
        /**
         *
         */
        """
        pass

    def output(self, URLSpec_self, ostream_out): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        output(URLSpec self, ostream out)
        
        /**
         *
         */
        """
        pass

    def quote(self, str_source, str_safe): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        quote(str source, str safe)
        
        /**
         * Returns the source string with all "unsafe" characters quoted, making a
         * string suitable for placing in a URL.  Letters, digits, and the underscore,
         * comma, period, and hyphen characters, as well as any included in the safe
         * string, are left alone; all others are converted to hex representation.
         */
        """
        pass

    def quotePlus(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        quote_plus(str source, str safe)
        
        /**
         * Behaves like quote() with the additional behavior of replacing spaces with
         * plus signs.
         */
        """
        pass

    def quote_plus(self, str_source, str_safe): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        quote_plus(str source, str safe)
        
        /**
         * Behaves like quote() with the additional behavior of replacing spaces with
         * plus signs.
         */
        """
        pass

    def setAuthority(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_authority(const URLSpec self, str authority)
        
        /**
         * Replaces the authority part of the URL specification.  This includes the
         * username, server, and port.
         */
        """
        pass

    def setPath(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_path(const URLSpec self, str path)
        
        /**
         * Replaces the path part of the URL specification.
         */
        """
        pass

    def setPort(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_port(const URLSpec self, str port)
        set_port(const URLSpec self, int port)
        
        /**
         * Replaces the port part of the URL specification.
         */
        
        /**
         * Replaces the port part of the URL specification, given a numeric port
         * number.
         */
        """
        pass

    def setQuery(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_query(const URLSpec self, str query)
        
        /**
         * Replaces the query part of the URL specification.
         */
        """
        pass

    def setScheme(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_scheme(const URLSpec self, str scheme)
        
        /**
         * Replaces the scheme part of the URL specification.
         */
        """
        pass

    def setServer(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_server(const URLSpec self, str server)
        
        /**
         * Replaces the server part of the URL specification.
         * Unlike set_server_and_port, this method does not require IPv6 addresses to
         * be enclosed in square brackets.
         */
        """
        pass

    def setServerAndPort(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_server_and_port(const URLSpec self, str server_and_port)
        
        /**
         * Replaces the server and port parts of the URL specification simultaneously.
         * The input string should be of the form "server:port", or just "server" to
         * make the port number implicit.
         * Any IPv6 address must be enclosed in square brackets.
         */
        """
        pass

    def setUrl(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_url(const URLSpec self, str url, bool server_name_expected)
        
        /**
         * Completely replaces the URL with the indicated string.  If
         * server_name_expected is true, it is a hint that an undecorated URL is
         * probably a server name, not a local filename.
         */
        """
        pass

    def setUsername(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_username(const URLSpec self, str username)
        
        /**
         * Replaces the username part of the URL specification.
         */
        """
        pass

    def set_authority(self, const_URLSpec_self, str_authority): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_authority(const URLSpec self, str authority)
        
        /**
         * Replaces the authority part of the URL specification.  This includes the
         * username, server, and port.
         */
        """
        pass

    def set_path(self, const_URLSpec_self, str_path): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_path(const URLSpec self, str path)
        
        /**
         * Replaces the path part of the URL specification.
         */
        """
        pass

    def set_port(self, const_URLSpec_self, str_port): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_port(const URLSpec self, str port)
        set_port(const URLSpec self, int port)
        
        /**
         * Replaces the port part of the URL specification.
         */
        
        /**
         * Replaces the port part of the URL specification, given a numeric port
         * number.
         */
        """
        pass

    def set_query(self, const_URLSpec_self, str_query): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_query(const URLSpec self, str query)
        
        /**
         * Replaces the query part of the URL specification.
         */
        """
        pass

    def set_scheme(self, const_URLSpec_self, str_scheme): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_scheme(const URLSpec self, str scheme)
        
        /**
         * Replaces the scheme part of the URL specification.
         */
        """
        pass

    def set_server(self, const_URLSpec_self, str_server): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_server(const URLSpec self, str server)
        
        /**
         * Replaces the server part of the URL specification.
         * Unlike set_server_and_port, this method does not require IPv6 addresses to
         * be enclosed in square brackets.
         */
        """
        pass

    def set_server_and_port(self, const_URLSpec_self, str_server_and_port): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_server_and_port(const URLSpec self, str server_and_port)
        
        /**
         * Replaces the server and port parts of the URL specification simultaneously.
         * The input string should be of the form "server:port", or just "server" to
         * make the port number implicit.
         * Any IPv6 address must be enclosed in square brackets.
         */
        """
        pass

    def set_url(self, const_URLSpec_self, str_url, bool_server_name_expected): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_url(const URLSpec self, str url, bool server_name_expected)
        
        /**
         * Completely replaces the URL with the indicated string.  If
         * server_name_expected is true, it is a hint that an undecorated URL is
         * probably a server name, not a local filename.
         */
        """
        pass

    def set_username(self, const_URLSpec_self, str_username): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_username(const URLSpec self, str username)
        
        /**
         * Replaces the username part of the URL specification.
         */
        """
        pass

    def unquote(self, str_source): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        unquote(str source)
        
        /**
         * Reverses the operation of quote(): converts escaped characters of the form
         * "%xx" to their ascii equivalent.
         */
        """
        pass

    def unquotePlus(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        unquote_plus(str source)
        
        /**
         * Reverses the operation of quote_plus(): converts escaped characters of the
         * form "%xx" to their ascii equivalent, and also converts plus signs to
         * spaces.
         */
        """
        pass

    def unquote_plus(self, str_source): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        unquote_plus(str source)
        
        /**
         * Reverses the operation of quote_plus(): converts escaped characters of the
         * form "%xx" to their ascii equivalent, and also converts plus signs to
         * spaces.
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

    def __getitem__(self, *args, **kwargs): # real signature unknown
        """ Return self[key]. """
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

    def __len__(self, *args, **kwargs): # real signature unknown
        """ Return len(self). """
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

    authority = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    path = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    port = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    query = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    scheme = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    server = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    server_and_port = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ssl = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    username = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__bool__': None, # (!) real value is "<slot wrapper '__bool__' of 'panda3d.core.URLSpec' objects>"
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.core.URLSpec' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.core.URLSpec' objects>"
        '__doc__': '/**\n * A container for a URL, e.g.  "http://server:port/path".\n *\n * The URLSpec object is similar to a Filename in that it contains logic to\n * identify the various parts of a URL and return (or modify) them separately.\n */',
        '__eq__': None, # (!) real value is "<slot wrapper '__eq__' of 'panda3d.core.URLSpec' objects>"
        '__ge__': None, # (!) real value is "<slot wrapper '__ge__' of 'panda3d.core.URLSpec' objects>"
        '__getitem__': None, # (!) real value is "<slot wrapper '__getitem__' of 'panda3d.core.URLSpec' objects>"
        '__gt__': None, # (!) real value is "<slot wrapper '__gt__' of 'panda3d.core.URLSpec' objects>"
        '__hash__': None, # (!) real value is "<slot wrapper '__hash__' of 'panda3d.core.URLSpec' objects>"
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.URLSpec' objects>"
        '__le__': None, # (!) real value is "<slot wrapper '__le__' of 'panda3d.core.URLSpec' objects>"
        '__len__': None, # (!) real value is "<slot wrapper '__len__' of 'panda3d.core.URLSpec' objects>"
        '__lt__': None, # (!) real value is "<slot wrapper '__lt__' of 'panda3d.core.URLSpec' objects>"
        '__ne__': None, # (!) real value is "<slot wrapper '__ne__' of 'panda3d.core.URLSpec' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE26C1D0>'
        '__repr__': None, # (!) real value is "<slot wrapper '__repr__' of 'panda3d.core.URLSpec' objects>"
        '__str__': None, # (!) real value is "<slot wrapper '__str__' of 'panda3d.core.URLSpec' objects>"
        'assign': None, # (!) real value is "<method 'assign' of 'panda3d.core.URLSpec' objects>"
        'authority': None, # (!) real value is "<attribute 'authority' of 'panda3d.core.URLSpec' objects>"
        'cStr': None, # (!) real value is "<method 'cStr' of 'panda3d.core.URLSpec' objects>"
        'c_str': None, # (!) real value is "<method 'c_str' of 'panda3d.core.URLSpec' objects>"
        'compareTo': None, # (!) real value is "<method 'compareTo' of 'panda3d.core.URLSpec' objects>"
        'compare_to': None, # (!) real value is "<method 'compare_to' of 'panda3d.core.URLSpec' objects>"
        'empty': None, # (!) real value is "<method 'empty' of 'panda3d.core.URLSpec' objects>"
        'getAuthority': None, # (!) real value is "<method 'getAuthority' of 'panda3d.core.URLSpec' objects>"
        'getDefaultPortForScheme': None, # (!) real value is '<staticmethod(<built-in method getDefaultPortForScheme of type object at 0x00007FFCFE26C1D0>)>'
        'getHash': None, # (!) real value is "<method 'getHash' of 'panda3d.core.URLSpec' objects>"
        'getPath': None, # (!) real value is "<method 'getPath' of 'panda3d.core.URLSpec' objects>"
        'getPathAndQuery': None, # (!) real value is "<method 'getPathAndQuery' of 'panda3d.core.URLSpec' objects>"
        'getPort': None, # (!) real value is "<method 'getPort' of 'panda3d.core.URLSpec' objects>"
        'getPortStr': None, # (!) real value is "<method 'getPortStr' of 'panda3d.core.URLSpec' objects>"
        'getQuery': None, # (!) real value is "<method 'getQuery' of 'panda3d.core.URLSpec' objects>"
        'getScheme': None, # (!) real value is "<method 'getScheme' of 'panda3d.core.URLSpec' objects>"
        'getServer': None, # (!) real value is "<method 'getServer' of 'panda3d.core.URLSpec' objects>"
        'getServerAndPort': None, # (!) real value is "<method 'getServerAndPort' of 'panda3d.core.URLSpec' objects>"
        'getUrl': None, # (!) real value is "<method 'getUrl' of 'panda3d.core.URLSpec' objects>"
        'getUsername': None, # (!) real value is "<method 'getUsername' of 'panda3d.core.URLSpec' objects>"
        'get_authority': None, # (!) real value is "<method 'get_authority' of 'panda3d.core.URLSpec' objects>"
        'get_default_port_for_scheme': None, # (!) real value is '<staticmethod(<built-in method get_default_port_for_scheme of type object at 0x00007FFCFE26C1D0>)>'
        'get_hash': None, # (!) real value is "<method 'get_hash' of 'panda3d.core.URLSpec' objects>"
        'get_path': None, # (!) real value is "<method 'get_path' of 'panda3d.core.URLSpec' objects>"
        'get_path_and_query': None, # (!) real value is "<method 'get_path_and_query' of 'panda3d.core.URLSpec' objects>"
        'get_port': None, # (!) real value is "<method 'get_port' of 'panda3d.core.URLSpec' objects>"
        'get_port_str': None, # (!) real value is "<method 'get_port_str' of 'panda3d.core.URLSpec' objects>"
        'get_query': None, # (!) real value is "<method 'get_query' of 'panda3d.core.URLSpec' objects>"
        'get_scheme': None, # (!) real value is "<method 'get_scheme' of 'panda3d.core.URLSpec' objects>"
        'get_server': None, # (!) real value is "<method 'get_server' of 'panda3d.core.URLSpec' objects>"
        'get_server_and_port': None, # (!) real value is "<method 'get_server_and_port' of 'panda3d.core.URLSpec' objects>"
        'get_url': None, # (!) real value is "<method 'get_url' of 'panda3d.core.URLSpec' objects>"
        'get_username': None, # (!) real value is "<method 'get_username' of 'panda3d.core.URLSpec' objects>"
        'hasAuthority': None, # (!) real value is "<method 'hasAuthority' of 'panda3d.core.URLSpec' objects>"
        'hasPath': None, # (!) real value is "<method 'hasPath' of 'panda3d.core.URLSpec' objects>"
        'hasPort': None, # (!) real value is "<method 'hasPort' of 'panda3d.core.URLSpec' objects>"
        'hasQuery': None, # (!) real value is "<method 'hasQuery' of 'panda3d.core.URLSpec' objects>"
        'hasScheme': None, # (!) real value is "<method 'hasScheme' of 'panda3d.core.URLSpec' objects>"
        'hasServer': None, # (!) real value is "<method 'hasServer' of 'panda3d.core.URLSpec' objects>"
        'hasUsername': None, # (!) real value is "<method 'hasUsername' of 'panda3d.core.URLSpec' objects>"
        'has_authority': None, # (!) real value is "<method 'has_authority' of 'panda3d.core.URLSpec' objects>"
        'has_path': None, # (!) real value is "<method 'has_path' of 'panda3d.core.URLSpec' objects>"
        'has_port': None, # (!) real value is "<method 'has_port' of 'panda3d.core.URLSpec' objects>"
        'has_query': None, # (!) real value is "<method 'has_query' of 'panda3d.core.URLSpec' objects>"
        'has_scheme': None, # (!) real value is "<method 'has_scheme' of 'panda3d.core.URLSpec' objects>"
        'has_server': None, # (!) real value is "<method 'has_server' of 'panda3d.core.URLSpec' objects>"
        'has_username': None, # (!) real value is "<method 'has_username' of 'panda3d.core.URLSpec' objects>"
        'input': None, # (!) real value is "<method 'input' of 'panda3d.core.URLSpec' objects>"
        'isDefaultPort': None, # (!) real value is "<method 'isDefaultPort' of 'panda3d.core.URLSpec' objects>"
        'isSsl': None, # (!) real value is "<method 'isSsl' of 'panda3d.core.URLSpec' objects>"
        'is_default_port': None, # (!) real value is "<method 'is_default_port' of 'panda3d.core.URLSpec' objects>"
        'is_ssl': None, # (!) real value is "<method 'is_ssl' of 'panda3d.core.URLSpec' objects>"
        'length': None, # (!) real value is "<method 'length' of 'panda3d.core.URLSpec' objects>"
        'output': None, # (!) real value is "<method 'output' of 'panda3d.core.URLSpec' objects>"
        'path': None, # (!) real value is "<attribute 'path' of 'panda3d.core.URLSpec' objects>"
        'port': None, # (!) real value is "<attribute 'port' of 'panda3d.core.URLSpec' objects>"
        'query': None, # (!) real value is "<attribute 'query' of 'panda3d.core.URLSpec' objects>"
        'quote': None, # (!) real value is '<staticmethod(<built-in method quote of type object at 0x00007FFCFE26C1D0>)>'
        'quotePlus': None, # (!) real value is '<staticmethod(<built-in method quotePlus of type object at 0x00007FFCFE26C1D0>)>'
        'quote_plus': None, # (!) real value is '<staticmethod(<built-in method quote_plus of type object at 0x00007FFCFE26C1D0>)>'
        'scheme': None, # (!) real value is "<attribute 'scheme' of 'panda3d.core.URLSpec' objects>"
        'server': None, # (!) real value is "<attribute 'server' of 'panda3d.core.URLSpec' objects>"
        'server_and_port': None, # (!) real value is "<attribute 'server_and_port' of 'panda3d.core.URLSpec' objects>"
        'setAuthority': None, # (!) real value is "<method 'setAuthority' of 'panda3d.core.URLSpec' objects>"
        'setPath': None, # (!) real value is "<method 'setPath' of 'panda3d.core.URLSpec' objects>"
        'setPort': None, # (!) real value is "<method 'setPort' of 'panda3d.core.URLSpec' objects>"
        'setQuery': None, # (!) real value is "<method 'setQuery' of 'panda3d.core.URLSpec' objects>"
        'setScheme': None, # (!) real value is "<method 'setScheme' of 'panda3d.core.URLSpec' objects>"
        'setServer': None, # (!) real value is "<method 'setServer' of 'panda3d.core.URLSpec' objects>"
        'setServerAndPort': None, # (!) real value is "<method 'setServerAndPort' of 'panda3d.core.URLSpec' objects>"
        'setUrl': None, # (!) real value is "<method 'setUrl' of 'panda3d.core.URLSpec' objects>"
        'setUsername': None, # (!) real value is "<method 'setUsername' of 'panda3d.core.URLSpec' objects>"
        'set_authority': None, # (!) real value is "<method 'set_authority' of 'panda3d.core.URLSpec' objects>"
        'set_path': None, # (!) real value is "<method 'set_path' of 'panda3d.core.URLSpec' objects>"
        'set_port': None, # (!) real value is "<method 'set_port' of 'panda3d.core.URLSpec' objects>"
        'set_query': None, # (!) real value is "<method 'set_query' of 'panda3d.core.URLSpec' objects>"
        'set_scheme': None, # (!) real value is "<method 'set_scheme' of 'panda3d.core.URLSpec' objects>"
        'set_server': None, # (!) real value is "<method 'set_server' of 'panda3d.core.URLSpec' objects>"
        'set_server_and_port': None, # (!) real value is "<method 'set_server_and_port' of 'panda3d.core.URLSpec' objects>"
        'set_url': None, # (!) real value is "<method 'set_url' of 'panda3d.core.URLSpec' objects>"
        'set_username': None, # (!) real value is "<method 'set_username' of 'panda3d.core.URLSpec' objects>"
        'ssl': None, # (!) real value is "<attribute 'ssl' of 'panda3d.core.URLSpec' objects>"
        'unquote': None, # (!) real value is '<staticmethod(<built-in method unquote of type object at 0x00007FFCFE26C1D0>)>'
        'unquotePlus': None, # (!) real value is '<staticmethod(<built-in method unquotePlus of type object at 0x00007FFCFE26C1D0>)>'
        'unquote_plus': None, # (!) real value is '<staticmethod(<built-in method unquote_plus of type object at 0x00007FFCFE26C1D0>)>'
        'username': None, # (!) real value is "<attribute 'username' of 'panda3d.core.URLSpec' objects>"
    }


