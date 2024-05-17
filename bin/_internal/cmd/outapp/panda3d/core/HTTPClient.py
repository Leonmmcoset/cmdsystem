# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .ReferenceCount import ReferenceCount

class HTTPClient(ReferenceCount):
    """
    /**
     * Handles contacting an HTTP server and retrieving a document.  Each
     * HTTPClient object represents a separate context, and stores its own list of
     * cookies, passwords, and certificates; however, a given HTTPClient is
     * capable of making multiple simultaneous requests to the same or different
     * servers.
     *
     * It is up to the programmer whether one HTTPClient should be used to
     * retrieve all documents, or a separate one should be created each time.
     * There is a default, global HTTPClient available in
     * HTTPClient::get_global_ptr().
     */
    """
    def addDirectHost(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_direct_host(const HTTPClient self, str hostname)
        
        /**
         * Adds the indicated name to the set of hostnames that are connected to
         * directly, without using a proxy.  This name may be either a DNS name or an
         * IP address, and it may include the * as a wildcard character.
         */
        """
        pass

    def addPreapprovedServerCertificateFilename(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_preapproved_server_certificate_filename(const HTTPClient self, const URLSpec url, const Filename filename)
        
        /**
         * Adds the certificate defined in the indicated PEM filename as a "pre-
         * approved" certificate for the indicated server, defined by the hostname and
         * port (only) from the given URL.
         *
         * If the server offers this particular certificate on a secure connection, it
         * will be accepted without question.  This is particularly useful for
         * communicating with a server using a known self-signed certificate.
         *
         * See also the similar add_preapproved_server_certificate_pem(), and the
         * weaker add_preapproved_server_certificate_name().
         */
        """
        pass

    def addPreapprovedServerCertificateName(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_preapproved_server_certificate_name(const HTTPClient self, const URLSpec url, str name)
        
        /**
         * Adds the certificate *name* only, as a "pre-approved" certificate name for
         * the indicated server, defined by the hostname and port (only) from the
         * given URL.
         *
         * This is a weaker function than
         * add_preapproved_server_certificate_filename().  This checks only the
         * subject name of the certificate, without checking for a particular
         * certificate by key.  This means that a variety of server certificates may
         * match the indicated name.
         *
         * Because this is a weaker verification, it only applies to server
         * certificates that are signed by a recognized certificate authority.  Thus,
         * it cannot be used to pre-approve self-signed certificates, but it can be
         * used to accept a server certificate offered by a different hostname than
         * the one in the cert itself.
         *
         * The certificate name should be formatted in the form
         * type0=value0/type1=value1/type2=...
         */
        """
        pass

    def addPreapprovedServerCertificatePem(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_preapproved_server_certificate_pem(const HTTPClient self, const URLSpec url, str pem)
        
        /**
         * Adds the certificate defined in the indicated data string, formatted as a
         * PEM block, as a "pre-approved" certificate for the indicated server,
         * defined by the hostname and port (only) from the given URL.
         *
         * If the server offers this particular certificate on a secure connection, it
         * will be accepted without question.  This is particularly useful for
         * communicating with a server using a known self-signed certificate.
         *
         * See also the similar add_preapproved_server_certificate_filename(), and the
         * weaker add_preapproved_server_certificate_name().
         */
        """
        pass

    def addProxy(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_proxy(const HTTPClient self, str scheme, const URLSpec proxy)
        
        /**
         * Adds the indicated proxy host as a proxy for communications on the given
         * scheme.  Usually the scheme is "http" or "https".  It may be the empty
         * string to indicate a general proxy.  The proxy string may be the empty URL
         * to indicate a direct connection.
         */
        """
        pass

    def add_direct_host(self, const_HTTPClient_self, str_hostname): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_direct_host(const HTTPClient self, str hostname)
        
        /**
         * Adds the indicated name to the set of hostnames that are connected to
         * directly, without using a proxy.  This name may be either a DNS name or an
         * IP address, and it may include the * as a wildcard character.
         */
        """
        pass

    def add_preapproved_server_certificate_filename(self, const_HTTPClient_self, const_URLSpec_url, const_Filename_filename): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_preapproved_server_certificate_filename(const HTTPClient self, const URLSpec url, const Filename filename)
        
        /**
         * Adds the certificate defined in the indicated PEM filename as a "pre-
         * approved" certificate for the indicated server, defined by the hostname and
         * port (only) from the given URL.
         *
         * If the server offers this particular certificate on a secure connection, it
         * will be accepted without question.  This is particularly useful for
         * communicating with a server using a known self-signed certificate.
         *
         * See also the similar add_preapproved_server_certificate_pem(), and the
         * weaker add_preapproved_server_certificate_name().
         */
        """
        pass

    def add_preapproved_server_certificate_name(self, const_HTTPClient_self, const_URLSpec_url, str_name): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_preapproved_server_certificate_name(const HTTPClient self, const URLSpec url, str name)
        
        /**
         * Adds the certificate *name* only, as a "pre-approved" certificate name for
         * the indicated server, defined by the hostname and port (only) from the
         * given URL.
         *
         * This is a weaker function than
         * add_preapproved_server_certificate_filename().  This checks only the
         * subject name of the certificate, without checking for a particular
         * certificate by key.  This means that a variety of server certificates may
         * match the indicated name.
         *
         * Because this is a weaker verification, it only applies to server
         * certificates that are signed by a recognized certificate authority.  Thus,
         * it cannot be used to pre-approve self-signed certificates, but it can be
         * used to accept a server certificate offered by a different hostname than
         * the one in the cert itself.
         *
         * The certificate name should be formatted in the form
         * type0=value0/type1=value1/type2=...
         */
        """
        pass

    def add_preapproved_server_certificate_pem(self, const_HTTPClient_self, const_URLSpec_url, str_pem): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_preapproved_server_certificate_pem(const HTTPClient self, const URLSpec url, str pem)
        
        /**
         * Adds the certificate defined in the indicated data string, formatted as a
         * PEM block, as a "pre-approved" certificate for the indicated server,
         * defined by the hostname and port (only) from the given URL.
         *
         * If the server offers this particular certificate on a secure connection, it
         * will be accepted without question.  This is particularly useful for
         * communicating with a server using a known self-signed certificate.
         *
         * See also the similar add_preapproved_server_certificate_filename(), and the
         * weaker add_preapproved_server_certificate_name().
         */
        """
        pass

    def add_proxy(self, const_HTTPClient_self, str_scheme, const_URLSpec_proxy): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_proxy(const HTTPClient self, str scheme, const URLSpec proxy)
        
        /**
         * Adds the indicated proxy host as a proxy for communications on the given
         * scheme.  Usually the scheme is "http" or "https".  It may be the empty
         * string to indicate a general proxy.  The proxy string may be the empty URL
         * to indicate a direct connection.
         */
        """
        pass

    def assign(self, const_HTTPClient_self, const_HTTPClient_copy): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        assign(const HTTPClient self, const HTTPClient copy)
        """
        pass

    def base64Decode(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        base64_decode(str s)
        
        /**
         * Implements HTTPAuthorization::base64_decode().  This is provided here just
         * as a convenient place to publish it for access by the scripting language;
         * C++ code should probably use HTTPAuthorization directly.
         */
        """
        pass

    def base64Encode(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        base64_encode(str s)
        
        /**
         * Implements HTTPAuthorization::base64_encode().  This is provided here just
         * as a convenient place to publish it for access by the scripting language;
         * C++ code should probably use HTTPAuthorization directly.
         */
        """
        pass

    def base64_decode(self, str_s): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        base64_decode(str s)
        
        /**
         * Implements HTTPAuthorization::base64_decode().  This is provided here just
         * as a convenient place to publish it for access by the scripting language;
         * C++ code should probably use HTTPAuthorization directly.
         */
        """
        pass

    def base64_encode(self, str_s): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        base64_encode(str s)
        
        /**
         * Implements HTTPAuthorization::base64_encode().  This is provided here just
         * as a convenient place to publish it for access by the scripting language;
         * C++ code should probably use HTTPAuthorization directly.
         */
        """
        pass

    def clearAllCookies(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_all_cookies(const HTTPClient self)
        
        /**
         * Removes the all stored cookies from the client.
         */
        """
        pass

    def clearAllPreapprovedServerCertificates(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_all_preapproved_server_certificates(const HTTPClient self)
        
        /**
         * Removes all preapproved server certificates for all servers.
         */
        """
        pass

    def clearCookie(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_cookie(const HTTPClient self, const HTTPCookie cookie)
        
        /**
         * Removes the cookie with the matching domain/path/name from the client's
         * list of cookies.  Returns true if it was removed, false if the cookie was
         * not matched.
         */
        """
        pass

    def clearDirectHost(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_direct_host(const HTTPClient self)
        
        /**
         * Resets the set of direct hosts to empty.  Subsequent calls to
         * add_direct_host() may be made to build up the list of hosts that do not
         * require a proxy connection.
         */
        """
        pass

    def clearPreapprovedServerCertificates(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_preapproved_server_certificates(const HTTPClient self, const URLSpec url)
        
        /**
         * Removes all preapproved server certificates for the indicated server and
         * port.
         */
        """
        pass

    def clearProxy(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_proxy(const HTTPClient self)
        
        /**
         * Resets the proxy spec to empty.  Subsequent calls to add_proxy() may be
         * made to build up the set of proxy servers.
         */
        """
        pass

    def clear_all_cookies(self, const_HTTPClient_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_all_cookies(const HTTPClient self)
        
        /**
         * Removes the all stored cookies from the client.
         */
        """
        pass

    def clear_all_preapproved_server_certificates(self, const_HTTPClient_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_all_preapproved_server_certificates(const HTTPClient self)
        
        /**
         * Removes all preapproved server certificates for all servers.
         */
        """
        pass

    def clear_cookie(self, const_HTTPClient_self, const_HTTPCookie_cookie): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_cookie(const HTTPClient self, const HTTPCookie cookie)
        
        /**
         * Removes the cookie with the matching domain/path/name from the client's
         * list of cookies.  Returns true if it was removed, false if the cookie was
         * not matched.
         */
        """
        pass

    def clear_direct_host(self, const_HTTPClient_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_direct_host(const HTTPClient self)
        
        /**
         * Resets the set of direct hosts to empty.  Subsequent calls to
         * add_direct_host() may be made to build up the list of hosts that do not
         * require a proxy connection.
         */
        """
        pass

    def clear_preapproved_server_certificates(self, const_HTTPClient_self, const_URLSpec_url): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_preapproved_server_certificates(const HTTPClient self, const URLSpec url)
        
        /**
         * Removes all preapproved server certificates for the indicated server and
         * port.
         */
        """
        pass

    def clear_proxy(self, const_HTTPClient_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_proxy(const HTTPClient self)
        
        /**
         * Resets the proxy spec to empty.  Subsequent calls to add_proxy() may be
         * made to build up the set of proxy servers.
         */
        """
        pass

    def copyCookiesFrom(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        copy_cookies_from(const HTTPClient self, const HTTPClient other)
        
        /**
         * Copies all the cookies from the indicated HTTPClient into this one.
         * Existing cookies in this client are not affected, unless they are shadowed
         * by the new cookies.
         */
        """
        pass

    def copy_cookies_from(self, const_HTTPClient_self, const_HTTPClient_other): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        copy_cookies_from(const HTTPClient self, const HTTPClient other)
        
        /**
         * Copies all the cookies from the indicated HTTPClient into this one.
         * Existing cookies in this client are not affected, unless they are shadowed
         * by the new cookies.
         */
        """
        pass

    def getCipherList(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_cipher_list(HTTPClient self)
        
        /**
         * Returns the set of ciphers as set by set_cipher_list().  See
         * set_cipher_list().
         */
        """
        pass

    def getCookie(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_cookie(HTTPClient self, const HTTPCookie cookie)
        
        /**
         * Looks up and returns the cookie in the client matching the given cookie's
         * domain/path/name.  If there is no matching cookie, returns an empty cookie.
         */
        """
        pass

    def getDirectHostSpec(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_direct_host_spec(HTTPClient self)
        
        /**
         * Returns the set of hosts that should be connected to directly, without
         * using a proxy, as a semicolon-separated list of hostnames that may contain
         * wildcard characters ("*").
         */
        """
        pass

    def getDocument(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_document(const HTTPClient self, const URLSpec url)
        
        /**
         * Opens the named document for reading.  Returns a new HTTPChannel object
         * whether the document is successfully read or not; you can test is_valid()
         * and get_return_code() to determine whether the document was retrieved.
         */
        """
        pass

    def getGlobalPtr(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_global_ptr()
        
        /**
         * Returns the default global HTTPClient.
         */
        """
        pass

    def getHeader(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_header(const HTTPClient self, const URLSpec url)
        
        /**
         * Like get_document(), except only the header associated with the document is
         * retrieved.  This may be used to test for existence of the document; it
         * might also return the size of the document (if the server gives us this
         * information).
         */
        """
        pass

    def getHttpVersion(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_http_version(HTTPClient self)
        
        /**
         * Returns the client's current setting for HTTP version.  See
         * set_http_version().
         */
        """
        pass

    def getHttpVersionString(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_http_version_string(HTTPClient self)
        
        /**
         * Returns the current HTTP version setting as a string, e.g.  "HTTP/1.0" or
         * "HTTP/1.1".
         */
        """
        pass

    def getProxiesForUrl(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_proxies_for_url(HTTPClient self, const URLSpec url)
        
        /**
         * Fills up the indicated vector with the list of URLSpec objects, in the
         * order in which they should be tried, that are appropriate proxies to try
         * for the indicated URL.  The empty URL is returned for a direct connection.
         *
         * It is the user's responsibility to empty this vector before calling this
         * method; otherwise, the proxy URL's will simply be appended to the existing
         * list.
         */
        
        /**
         * Returns a semicolon-delimited list of proxies, in the order in which they
         * should be tried, that are appropriate for the indicated URL.  The keyword
         * DIRECT indicates a direct connection should be tried.
         */
        """
        pass

    def getProxySpec(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_proxy_spec(HTTPClient self)
        
        /**
         * Returns the complete set of proxies to use for all schemes.  This is a
         * string of the form specified by set_proxy_spec(), above.  Note that the
         * string returned by this function may not be exactly the same as the string
         * passed into set_proxy_spec(), since the string is regenerated from the
         * internal storage structures and may therefore be reordered.
         */
        """
        pass

    def getTryAllDirect(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_try_all_direct(HTTPClient self)
        
        /**
         * Returns whether a failed connection through a proxy will be followed up by
         * a direct connection attempt, false otherwise.
         */
        """
        pass

    def getUsername(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_username(HTTPClient self, str server, str realm)
        
        /**
         * Returns the username:password string set for this server/realm pair, or
         * empty string if nothing has been set.  See set_username().
         */
        """
        pass

    def getVerifySsl(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_verify_ssl(HTTPClient self)
        
        /**
         * Returns whether the client will insist on verifying the identity of the
         * servers it connects to via SSL (that is, https).  See set_verify_ssl().
         */
        """
        pass

    def get_cipher_list(self, HTTPClient_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_cipher_list(HTTPClient self)
        
        /**
         * Returns the set of ciphers as set by set_cipher_list().  See
         * set_cipher_list().
         */
        """
        pass

    def get_cookie(self, HTTPClient_self, const_HTTPCookie_cookie): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_cookie(HTTPClient self, const HTTPCookie cookie)
        
        /**
         * Looks up and returns the cookie in the client matching the given cookie's
         * domain/path/name.  If there is no matching cookie, returns an empty cookie.
         */
        """
        pass

    def get_direct_host_spec(self, HTTPClient_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_direct_host_spec(HTTPClient self)
        
        /**
         * Returns the set of hosts that should be connected to directly, without
         * using a proxy, as a semicolon-separated list of hostnames that may contain
         * wildcard characters ("*").
         */
        """
        pass

    def get_document(self, const_HTTPClient_self, const_URLSpec_url): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_document(const HTTPClient self, const URLSpec url)
        
        /**
         * Opens the named document for reading.  Returns a new HTTPChannel object
         * whether the document is successfully read or not; you can test is_valid()
         * and get_return_code() to determine whether the document was retrieved.
         */
        """
        pass

    def get_global_ptr(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_global_ptr()
        
        /**
         * Returns the default global HTTPClient.
         */
        """
        pass

    def get_header(self, const_HTTPClient_self, const_URLSpec_url): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_header(const HTTPClient self, const URLSpec url)
        
        /**
         * Like get_document(), except only the header associated with the document is
         * retrieved.  This may be used to test for existence of the document; it
         * might also return the size of the document (if the server gives us this
         * information).
         */
        """
        pass

    def get_http_version(self, HTTPClient_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_http_version(HTTPClient self)
        
        /**
         * Returns the client's current setting for HTTP version.  See
         * set_http_version().
         */
        """
        pass

    def get_http_version_string(self, HTTPClient_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_http_version_string(HTTPClient self)
        
        /**
         * Returns the current HTTP version setting as a string, e.g.  "HTTP/1.0" or
         * "HTTP/1.1".
         */
        """
        pass

    def get_proxies_for_url(self, HTTPClient_self, const_URLSpec_url): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_proxies_for_url(HTTPClient self, const URLSpec url)
        
        /**
         * Fills up the indicated vector with the list of URLSpec objects, in the
         * order in which they should be tried, that are appropriate proxies to try
         * for the indicated URL.  The empty URL is returned for a direct connection.
         *
         * It is the user's responsibility to empty this vector before calling this
         * method; otherwise, the proxy URL's will simply be appended to the existing
         * list.
         */
        
        /**
         * Returns a semicolon-delimited list of proxies, in the order in which they
         * should be tried, that are appropriate for the indicated URL.  The keyword
         * DIRECT indicates a direct connection should be tried.
         */
        """
        pass

    def get_proxy_spec(self, HTTPClient_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_proxy_spec(HTTPClient self)
        
        /**
         * Returns the complete set of proxies to use for all schemes.  This is a
         * string of the form specified by set_proxy_spec(), above.  Note that the
         * string returned by this function may not be exactly the same as the string
         * passed into set_proxy_spec(), since the string is regenerated from the
         * internal storage structures and may therefore be reordered.
         */
        """
        pass

    def get_try_all_direct(self, HTTPClient_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_try_all_direct(HTTPClient self)
        
        /**
         * Returns whether a failed connection through a proxy will be followed up by
         * a direct connection attempt, false otherwise.
         */
        """
        pass

    def get_username(self, HTTPClient_self, str_server, str_realm): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_username(HTTPClient self, str server, str realm)
        
        /**
         * Returns the username:password string set for this server/realm pair, or
         * empty string if nothing has been set.  See set_username().
         */
        """
        pass

    def get_verify_ssl(self, HTTPClient_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_verify_ssl(HTTPClient self)
        
        /**
         * Returns whether the client will insist on verifying the identity of the
         * servers it connects to via SSL (that is, https).  See set_verify_ssl().
         */
        """
        pass

    def hasCookie(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_cookie(HTTPClient self, const HTTPCookie cookie)
        
        /**
         * Returns true if there is a cookie in the client matching the given cookie's
         * domain/path/name, false otherwise.
         */
        """
        pass

    def has_cookie(self, HTTPClient_self, const_HTTPCookie_cookie): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_cookie(HTTPClient self, const HTTPCookie cookie)
        
        /**
         * Returns true if there is a cookie in the client matching the given cookie's
         * domain/path/name, false otherwise.
         */
        """
        pass

    def initRandomSeed(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        init_random_seed()
        
        /**
         * This may be called once, presumably at the beginning of an application, to
         * initialize OpenSSL's random seed.  On Windows, it is particularly important
         * to call this at startup if you are going to be performing any https
         * operations or otherwise use encryption, since the Windows algorithm for
         * getting a random seed takes 2-3 seconds at startup, but can take 30 seconds
         * or more after you have opened a 3-D graphics window and started rendering.
         *
         * There is no harm in calling this method multiple times, or in not calling
         * it at all.
         */
        """
        pass

    def init_random_seed(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        init_random_seed()
        
        /**
         * This may be called once, presumably at the beginning of an application, to
         * initialize OpenSSL's random seed.  On Windows, it is particularly important
         * to call this at startup if you are going to be performing any https
         * operations or otherwise use encryption, since the Windows algorithm for
         * getting a random seed takes 2-3 seconds at startup, but can take 30 seconds
         * or more after you have opened a 3-D graphics window and started rendering.
         *
         * There is no harm in calling this method multiple times, or in not calling
         * it at all.
         */
        """
        pass

    def loadCertificates(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        load_certificates(const HTTPClient self, const Filename filename)
        
        /**
         * Reads the certificate(s) (delimited by -----BEGIN CERTIFICATE----- and
         * -----END CERTIFICATE-----) from the indicated file and makes them known as
         * trusted public keys for validating future connections.  Returns true on
         * success, false otherwise.
         */
        """
        pass

    def loadClientCertificate(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        load_client_certificate(const HTTPClient self)
        
        /**
         * Attempts to load the certificate named by set_client_certificate_filename()
         * immediately, and returns true if successful, false otherwise.
         *
         * Normally this need not be explicitly called, since it will be called
         * automatically if the server requests a certificate, but it may be useful to
         * determine ahead of time if the certificate can be loaded correctly.
         */
        """
        pass

    def load_certificates(self, const_HTTPClient_self, const_Filename_filename): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        load_certificates(const HTTPClient self, const Filename filename)
        
        /**
         * Reads the certificate(s) (delimited by -----BEGIN CERTIFICATE----- and
         * -----END CERTIFICATE-----) from the indicated file and makes them known as
         * trusted public keys for validating future connections.  Returns true on
         * success, false otherwise.
         */
        """
        pass

    def load_client_certificate(self, const_HTTPClient_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        load_client_certificate(const HTTPClient self)
        
        /**
         * Attempts to load the certificate named by set_client_certificate_filename()
         * immediately, and returns true if successful, false otherwise.
         *
         * Normally this need not be explicitly called, since it will be called
         * automatically if the server requests a certificate, but it may be useful to
         * determine ahead of time if the certificate can be loaded correctly.
         */
        """
        pass

    def makeChannel(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        make_channel(const HTTPClient self, bool persistent_connection)
        
        /**
         * Returns a new HTTPChannel object that may be used for reading multiple
         * documents using the same connection, for greater network efficiency than
         * calling HTTPClient::get_document() repeatedly (which would force a new
         * connection for each document).
         *
         * Also, HTTPChannel has some additional, less common interface methods than
         * the basic interface methods that exist on HTTPClient; if you wish to call
         * any of these methods you must first obtain an HTTPChannel.
         *
         * Pass true for persistent_connection to gain this network efficiency.  If,
         * on the other hand, your intention is to use the channel to retrieve only
         * one document, then pass false to inform the server that we will be dropping
         * the connection after the first document.
         */
        """
        pass

    def make_channel(self, const_HTTPClient_self, bool_persistent_connection): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        make_channel(const HTTPClient self, bool persistent_connection)
        
        /**
         * Returns a new HTTPChannel object that may be used for reading multiple
         * documents using the same connection, for greater network efficiency than
         * calling HTTPClient::get_document() repeatedly (which would force a new
         * connection for each document).
         *
         * Also, HTTPChannel has some additional, less common interface methods than
         * the basic interface methods that exist on HTTPClient; if you wish to call
         * any of these methods you must first obtain an HTTPChannel.
         *
         * Pass true for persistent_connection to gain this network efficiency.  If,
         * on the other hand, your intention is to use the channel to retrieve only
         * one document, then pass false to inform the server that we will be dropping
         * the connection after the first document.
         */
        """
        pass

    def parseHttpVersionString(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        parse_http_version_string(str version)
        
        /**
         * Matches the string representing a particular HTTP version against any of
         * the known versions and returns the appropriate enumerated value, or
         * HV_other if the version is unknown.
         */
        """
        pass

    def parse_http_version_string(self, str_version): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        parse_http_version_string(str version)
        
        /**
         * Matches the string representing a particular HTTP version against any of
         * the known versions and returns the appropriate enumerated value, or
         * HV_other if the version is unknown.
         */
        """
        pass

    def postForm(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        post_form(const HTTPClient self, const URLSpec url, str body)
        
        /**
         * Posts form data to a particular URL and retrieves the response.  Returns a
         * new HTTPChannel object whether the document is successfully read or not;
         * you can test is_valid() and get_return_code() to determine whether the
         * document was retrieved.
         */
        """
        pass

    def post_form(self, const_HTTPClient_self, const_URLSpec_url, str_body): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        post_form(const HTTPClient self, const URLSpec url, str body)
        
        /**
         * Posts form data to a particular URL and retrieves the response.  Returns a
         * new HTTPChannel object whether the document is successfully read or not;
         * you can test is_valid() and get_return_code() to determine whether the
         * document was retrieved.
         */
        """
        pass

    def sendCookies(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        send_cookies(const HTTPClient self, ostream out, const URLSpec url)
        
        /**
         * Writes to the indicated ostream a "Cookie" header line for sending the
         * cookies appropriate to the indicated URL along with an HTTP request.  This
         * also removes expired cookies.
         */
        """
        pass

    def send_cookies(self, const_HTTPClient_self, ostream_out, const_URLSpec_url): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        send_cookies(const HTTPClient self, ostream out, const URLSpec url)
        
        /**
         * Writes to the indicated ostream a "Cookie" header line for sending the
         * cookies appropriate to the indicated URL along with an HTTP request.  This
         * also removes expired cookies.
         */
        """
        pass

    def setCipherList(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_cipher_list(const HTTPClient self, str cipher_list)
        
        /**
         * Specifies the set of ciphers that are to be made available for SSL
         * connections.  This is a string as described in the ciphers(1) man page of
         * the OpenSSL documentation (or see
         * https://www.openssl.org/docs/man1.1.1/man1/ciphers.html ).  If this isn't
         * specified, the default is provided by the Config file.  You may also specify
         * "DEFAULT" to use the built-in OpenSSL default value.
         */
        """
        pass

    def setClientCertificateFilename(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_client_certificate_filename(const HTTPClient self, const Filename filename)
        
        /**
         * Sets the filename of the pem-formatted file that will be read for the
         * client public and private keys if an SSL server requests a certificate.
         * Either this or set_client_certificate_pem() may be used to specify a client
         * certificate.
         */
        """
        pass

    def setClientCertificatePassphrase(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_client_certificate_passphrase(const HTTPClient self, str passphrase)
        
        /**
         * Sets the passphrase used to decrypt the private key in the certificate
         * named by set_client_certificate_filename() or set_client_certificate_pem().
         */
        """
        pass

    def setClientCertificatePem(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_client_certificate_pem(const HTTPClient self, str pem)
        
        /**
         * Sets the pem-formatted contents of the certificate that will be parsed for
         * the client public and private keys if an SSL server requests a certificate.
         * Either this or set_client_certificate_filename() may be used to specify a
         * client certificate.
         */
        """
        pass

    def setCookie(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_cookie(const HTTPClient self, const HTTPCookie cookie)
        
        /**
         * Stores the indicated cookie in the client's list of cookies, as if it had
         * been received from a server.
         */
        """
        pass

    def setDirectHostSpec(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_direct_host_spec(const HTTPClient self, str direct_host_spec)
        
        /**
         * Specifies the set of hosts that should be connected to directly, without
         * using a proxy.  This is a semicolon-separated list of hostnames that may
         * contain wildcard characters ("*").
         */
        """
        pass

    def setHttpVersion(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_http_version(const HTTPClient self, int version)
        
        /**
         * Specifies the version of HTTP that the client uses to identify itself to
         * the server.  The default is HV_11, or HTTP 1.0; you can set this to HV_10
         * (HTTP 1.0) to request the server use the older interface.
         */
        """
        pass

    def setProxySpec(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_proxy_spec(const HTTPClient self, str proxy_spec)
        
        /**
         * Specifies the complete set of proxies to use for all schemes.  This is
         * either a semicolon-delimited set of hostname:ports, or a semicolon-
         * delimited set of pairs of the form "scheme=hostname:port", or a
         * combination.  Use the keyword DIRECT, or an empty string, to represent a
         * direct connection.  A particular scheme and/or proxy host may be listed
         * more than once.  This is a convenience function that can be used in place
         * of explicit calls to add_proxy() for each scheme/proxy pair.
         */
        """
        pass

    def setTryAllDirect(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_try_all_direct(const HTTPClient self, bool try_all_direct)
        
        /**
         * If this is set true, then after a connection attempt through a proxy fails,
         * we always try a direct connection, regardless of whether the host is listed
         * on the direct_host_spec list.  If this is false, a direct attempt is not
         * made when we have a proxy in effect, even if the proxy fails.
         */
        """
        pass

    def setUsername(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_username(const HTTPClient self, str server, str realm, str username)
        
        /**
         * Specifies the username:password string corresponding to a particular server
         * and/or realm, when demanded by the server.  Either or both of the server or
         * realm may be empty; if so, they match anything.  Also, the server may be
         * set to the special string `"*proxy"`, which will match any proxy server.
         *
         * If the username is set to the empty string, this clears the password for
         * the particular server/realm pair.
         */
        """
        pass

    def setVerifySsl(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_verify_ssl(const HTTPClient self, int verify_ssl)
        
        /**
         * Specifies whether the client will insist on verifying the identity of the
         * servers it connects to via SSL (that is, https).
         *
         * The parameter value is an enumerated type which indicates the level of
         * security to which the client will insist upon.
         */
        """
        pass

    def set_cipher_list(self, const_HTTPClient_self, str_cipher_list): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_cipher_list(const HTTPClient self, str cipher_list)
        
        /**
         * Specifies the set of ciphers that are to be made available for SSL
         * connections.  This is a string as described in the ciphers(1) man page of
         * the OpenSSL documentation (or see
         * https://www.openssl.org/docs/man1.1.1/man1/ciphers.html ).  If this isn't
         * specified, the default is provided by the Config file.  You may also specify
         * "DEFAULT" to use the built-in OpenSSL default value.
         */
        """
        pass

    def set_client_certificate_filename(self, const_HTTPClient_self, const_Filename_filename): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_client_certificate_filename(const HTTPClient self, const Filename filename)
        
        /**
         * Sets the filename of the pem-formatted file that will be read for the
         * client public and private keys if an SSL server requests a certificate.
         * Either this or set_client_certificate_pem() may be used to specify a client
         * certificate.
         */
        """
        pass

    def set_client_certificate_passphrase(self, const_HTTPClient_self, str_passphrase): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_client_certificate_passphrase(const HTTPClient self, str passphrase)
        
        /**
         * Sets the passphrase used to decrypt the private key in the certificate
         * named by set_client_certificate_filename() or set_client_certificate_pem().
         */
        """
        pass

    def set_client_certificate_pem(self, const_HTTPClient_self, str_pem): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_client_certificate_pem(const HTTPClient self, str pem)
        
        /**
         * Sets the pem-formatted contents of the certificate that will be parsed for
         * the client public and private keys if an SSL server requests a certificate.
         * Either this or set_client_certificate_filename() may be used to specify a
         * client certificate.
         */
        """
        pass

    def set_cookie(self, const_HTTPClient_self, const_HTTPCookie_cookie): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_cookie(const HTTPClient self, const HTTPCookie cookie)
        
        /**
         * Stores the indicated cookie in the client's list of cookies, as if it had
         * been received from a server.
         */
        """
        pass

    def set_direct_host_spec(self, const_HTTPClient_self, str_direct_host_spec): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_direct_host_spec(const HTTPClient self, str direct_host_spec)
        
        /**
         * Specifies the set of hosts that should be connected to directly, without
         * using a proxy.  This is a semicolon-separated list of hostnames that may
         * contain wildcard characters ("*").
         */
        """
        pass

    def set_http_version(self, const_HTTPClient_self, int_version): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_http_version(const HTTPClient self, int version)
        
        /**
         * Specifies the version of HTTP that the client uses to identify itself to
         * the server.  The default is HV_11, or HTTP 1.0; you can set this to HV_10
         * (HTTP 1.0) to request the server use the older interface.
         */
        """
        pass

    def set_proxy_spec(self, const_HTTPClient_self, str_proxy_spec): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_proxy_spec(const HTTPClient self, str proxy_spec)
        
        /**
         * Specifies the complete set of proxies to use for all schemes.  This is
         * either a semicolon-delimited set of hostname:ports, or a semicolon-
         * delimited set of pairs of the form "scheme=hostname:port", or a
         * combination.  Use the keyword DIRECT, or an empty string, to represent a
         * direct connection.  A particular scheme and/or proxy host may be listed
         * more than once.  This is a convenience function that can be used in place
         * of explicit calls to add_proxy() for each scheme/proxy pair.
         */
        """
        pass

    def set_try_all_direct(self, const_HTTPClient_self, bool_try_all_direct): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_try_all_direct(const HTTPClient self, bool try_all_direct)
        
        /**
         * If this is set true, then after a connection attempt through a proxy fails,
         * we always try a direct connection, regardless of whether the host is listed
         * on the direct_host_spec list.  If this is false, a direct attempt is not
         * made when we have a proxy in effect, even if the proxy fails.
         */
        """
        pass

    def set_username(self, const_HTTPClient_self, str_server, str_realm, str_username): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_username(const HTTPClient self, str server, str realm, str username)
        
        /**
         * Specifies the username:password string corresponding to a particular server
         * and/or realm, when demanded by the server.  Either or both of the server or
         * realm may be empty; if so, they match anything.  Also, the server may be
         * set to the special string `"*proxy"`, which will match any proxy server.
         *
         * If the username is set to the empty string, this clears the password for
         * the particular server/realm pair.
         */
        """
        pass

    def set_verify_ssl(self, const_HTTPClient_self, int_verify_ssl): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_verify_ssl(const HTTPClient self, int verify_ssl)
        
        /**
         * Specifies whether the client will insist on verifying the identity of the
         * servers it connects to via SSL (that is, https).
         *
         * The parameter value is an enumerated type which indicates the level of
         * security to which the client will insist upon.
         */
        """
        pass

    def writeCookies(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        write_cookies(HTTPClient self, ostream out)
        
        /**
         * Outputs the complete list of cookies stored on the client, for all domains,
         * including the expired cookies (which will normally not be sent back to a
         * host).
         */
        """
        pass

    def write_cookies(self, HTTPClient_self, ostream_out): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        write_cookies(HTTPClient self, ostream out)
        
        /**
         * Outputs the complete list of cookies stored on the client, for all domains,
         * including the expired cookies (which will normally not be sent back to a
         * host).
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

    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        'VSNoDateCheck': 1,
        'VSNoVerify': 0,
        'VSNormal': 2,
        'VS_no_date_check': 1,
        'VS_no_verify': 0,
        'VS_normal': 2,
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.core.HTTPClient' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.core.HTTPClient' objects>"
        '__doc__': '/**\n * Handles contacting an HTTP server and retrieving a document.  Each\n * HTTPClient object represents a separate context, and stores its own list of\n * cookies, passwords, and certificates; however, a given HTTPClient is\n * capable of making multiple simultaneous requests to the same or different\n * servers.\n *\n * It is up to the programmer whether one HTTPClient should be used to\n * retrieve all documents, or a separate one should be created each time.\n * There is a default, global HTTPClient available in\n * HTTPClient::get_global_ptr().\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.HTTPClient' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE26C910>'
        'addDirectHost': None, # (!) real value is "<method 'addDirectHost' of 'panda3d.core.HTTPClient' objects>"
        'addPreapprovedServerCertificateFilename': None, # (!) real value is "<method 'addPreapprovedServerCertificateFilename' of 'panda3d.core.HTTPClient' objects>"
        'addPreapprovedServerCertificateName': None, # (!) real value is "<method 'addPreapprovedServerCertificateName' of 'panda3d.core.HTTPClient' objects>"
        'addPreapprovedServerCertificatePem': None, # (!) real value is "<method 'addPreapprovedServerCertificatePem' of 'panda3d.core.HTTPClient' objects>"
        'addProxy': None, # (!) real value is "<method 'addProxy' of 'panda3d.core.HTTPClient' objects>"
        'add_direct_host': None, # (!) real value is "<method 'add_direct_host' of 'panda3d.core.HTTPClient' objects>"
        'add_preapproved_server_certificate_filename': None, # (!) real value is "<method 'add_preapproved_server_certificate_filename' of 'panda3d.core.HTTPClient' objects>"
        'add_preapproved_server_certificate_name': None, # (!) real value is "<method 'add_preapproved_server_certificate_name' of 'panda3d.core.HTTPClient' objects>"
        'add_preapproved_server_certificate_pem': None, # (!) real value is "<method 'add_preapproved_server_certificate_pem' of 'panda3d.core.HTTPClient' objects>"
        'add_proxy': None, # (!) real value is "<method 'add_proxy' of 'panda3d.core.HTTPClient' objects>"
        'assign': None, # (!) real value is "<method 'assign' of 'panda3d.core.HTTPClient' objects>"
        'base64Decode': None, # (!) real value is '<staticmethod(<built-in method base64Decode of type object at 0x00007FFCFE26C910>)>'
        'base64Encode': None, # (!) real value is '<staticmethod(<built-in method base64Encode of type object at 0x00007FFCFE26C910>)>'
        'base64_decode': None, # (!) real value is '<staticmethod(<built-in method base64_decode of type object at 0x00007FFCFE26C910>)>'
        'base64_encode': None, # (!) real value is '<staticmethod(<built-in method base64_encode of type object at 0x00007FFCFE26C910>)>'
        'clearAllCookies': None, # (!) real value is "<method 'clearAllCookies' of 'panda3d.core.HTTPClient' objects>"
        'clearAllPreapprovedServerCertificates': None, # (!) real value is "<method 'clearAllPreapprovedServerCertificates' of 'panda3d.core.HTTPClient' objects>"
        'clearCookie': None, # (!) real value is "<method 'clearCookie' of 'panda3d.core.HTTPClient' objects>"
        'clearDirectHost': None, # (!) real value is "<method 'clearDirectHost' of 'panda3d.core.HTTPClient' objects>"
        'clearPreapprovedServerCertificates': None, # (!) real value is "<method 'clearPreapprovedServerCertificates' of 'panda3d.core.HTTPClient' objects>"
        'clearProxy': None, # (!) real value is "<method 'clearProxy' of 'panda3d.core.HTTPClient' objects>"
        'clear_all_cookies': None, # (!) real value is "<method 'clear_all_cookies' of 'panda3d.core.HTTPClient' objects>"
        'clear_all_preapproved_server_certificates': None, # (!) real value is "<method 'clear_all_preapproved_server_certificates' of 'panda3d.core.HTTPClient' objects>"
        'clear_cookie': None, # (!) real value is "<method 'clear_cookie' of 'panda3d.core.HTTPClient' objects>"
        'clear_direct_host': None, # (!) real value is "<method 'clear_direct_host' of 'panda3d.core.HTTPClient' objects>"
        'clear_preapproved_server_certificates': None, # (!) real value is "<method 'clear_preapproved_server_certificates' of 'panda3d.core.HTTPClient' objects>"
        'clear_proxy': None, # (!) real value is "<method 'clear_proxy' of 'panda3d.core.HTTPClient' objects>"
        'copyCookiesFrom': None, # (!) real value is "<method 'copyCookiesFrom' of 'panda3d.core.HTTPClient' objects>"
        'copy_cookies_from': None, # (!) real value is "<method 'copy_cookies_from' of 'panda3d.core.HTTPClient' objects>"
        'getCipherList': None, # (!) real value is "<method 'getCipherList' of 'panda3d.core.HTTPClient' objects>"
        'getCookie': None, # (!) real value is "<method 'getCookie' of 'panda3d.core.HTTPClient' objects>"
        'getDirectHostSpec': None, # (!) real value is "<method 'getDirectHostSpec' of 'panda3d.core.HTTPClient' objects>"
        'getDocument': None, # (!) real value is "<method 'getDocument' of 'panda3d.core.HTTPClient' objects>"
        'getGlobalPtr': None, # (!) real value is '<staticmethod(<built-in method getGlobalPtr of type object at 0x00007FFCFE26C910>)>'
        'getHeader': None, # (!) real value is "<method 'getHeader' of 'panda3d.core.HTTPClient' objects>"
        'getHttpVersion': None, # (!) real value is "<method 'getHttpVersion' of 'panda3d.core.HTTPClient' objects>"
        'getHttpVersionString': None, # (!) real value is "<method 'getHttpVersionString' of 'panda3d.core.HTTPClient' objects>"
        'getProxiesForUrl': None, # (!) real value is "<method 'getProxiesForUrl' of 'panda3d.core.HTTPClient' objects>"
        'getProxySpec': None, # (!) real value is "<method 'getProxySpec' of 'panda3d.core.HTTPClient' objects>"
        'getTryAllDirect': None, # (!) real value is "<method 'getTryAllDirect' of 'panda3d.core.HTTPClient' objects>"
        'getUsername': None, # (!) real value is "<method 'getUsername' of 'panda3d.core.HTTPClient' objects>"
        'getVerifySsl': None, # (!) real value is "<method 'getVerifySsl' of 'panda3d.core.HTTPClient' objects>"
        'get_cipher_list': None, # (!) real value is "<method 'get_cipher_list' of 'panda3d.core.HTTPClient' objects>"
        'get_cookie': None, # (!) real value is "<method 'get_cookie' of 'panda3d.core.HTTPClient' objects>"
        'get_direct_host_spec': None, # (!) real value is "<method 'get_direct_host_spec' of 'panda3d.core.HTTPClient' objects>"
        'get_document': None, # (!) real value is "<method 'get_document' of 'panda3d.core.HTTPClient' objects>"
        'get_global_ptr': None, # (!) real value is '<staticmethod(<built-in method get_global_ptr of type object at 0x00007FFCFE26C910>)>'
        'get_header': None, # (!) real value is "<method 'get_header' of 'panda3d.core.HTTPClient' objects>"
        'get_http_version': None, # (!) real value is "<method 'get_http_version' of 'panda3d.core.HTTPClient' objects>"
        'get_http_version_string': None, # (!) real value is "<method 'get_http_version_string' of 'panda3d.core.HTTPClient' objects>"
        'get_proxies_for_url': None, # (!) real value is "<method 'get_proxies_for_url' of 'panda3d.core.HTTPClient' objects>"
        'get_proxy_spec': None, # (!) real value is "<method 'get_proxy_spec' of 'panda3d.core.HTTPClient' objects>"
        'get_try_all_direct': None, # (!) real value is "<method 'get_try_all_direct' of 'panda3d.core.HTTPClient' objects>"
        'get_username': None, # (!) real value is "<method 'get_username' of 'panda3d.core.HTTPClient' objects>"
        'get_verify_ssl': None, # (!) real value is "<method 'get_verify_ssl' of 'panda3d.core.HTTPClient' objects>"
        'hasCookie': None, # (!) real value is "<method 'hasCookie' of 'panda3d.core.HTTPClient' objects>"
        'has_cookie': None, # (!) real value is "<method 'has_cookie' of 'panda3d.core.HTTPClient' objects>"
        'initRandomSeed': None, # (!) real value is '<staticmethod(<built-in method initRandomSeed of type object at 0x00007FFCFE26C910>)>'
        'init_random_seed': None, # (!) real value is '<staticmethod(<built-in method init_random_seed of type object at 0x00007FFCFE26C910>)>'
        'loadCertificates': None, # (!) real value is "<method 'loadCertificates' of 'panda3d.core.HTTPClient' objects>"
        'loadClientCertificate': None, # (!) real value is "<method 'loadClientCertificate' of 'panda3d.core.HTTPClient' objects>"
        'load_certificates': None, # (!) real value is "<method 'load_certificates' of 'panda3d.core.HTTPClient' objects>"
        'load_client_certificate': None, # (!) real value is "<method 'load_client_certificate' of 'panda3d.core.HTTPClient' objects>"
        'makeChannel': None, # (!) real value is "<method 'makeChannel' of 'panda3d.core.HTTPClient' objects>"
        'make_channel': None, # (!) real value is "<method 'make_channel' of 'panda3d.core.HTTPClient' objects>"
        'parseHttpVersionString': None, # (!) real value is '<staticmethod(<built-in method parseHttpVersionString of type object at 0x00007FFCFE26C910>)>'
        'parse_http_version_string': None, # (!) real value is '<staticmethod(<built-in method parse_http_version_string of type object at 0x00007FFCFE26C910>)>'
        'postForm': None, # (!) real value is "<method 'postForm' of 'panda3d.core.HTTPClient' objects>"
        'post_form': None, # (!) real value is "<method 'post_form' of 'panda3d.core.HTTPClient' objects>"
        'sendCookies': None, # (!) real value is "<method 'sendCookies' of 'panda3d.core.HTTPClient' objects>"
        'send_cookies': None, # (!) real value is "<method 'send_cookies' of 'panda3d.core.HTTPClient' objects>"
        'setCipherList': None, # (!) real value is "<method 'setCipherList' of 'panda3d.core.HTTPClient' objects>"
        'setClientCertificateFilename': None, # (!) real value is "<method 'setClientCertificateFilename' of 'panda3d.core.HTTPClient' objects>"
        'setClientCertificatePassphrase': None, # (!) real value is "<method 'setClientCertificatePassphrase' of 'panda3d.core.HTTPClient' objects>"
        'setClientCertificatePem': None, # (!) real value is "<method 'setClientCertificatePem' of 'panda3d.core.HTTPClient' objects>"
        'setCookie': None, # (!) real value is "<method 'setCookie' of 'panda3d.core.HTTPClient' objects>"
        'setDirectHostSpec': None, # (!) real value is "<method 'setDirectHostSpec' of 'panda3d.core.HTTPClient' objects>"
        'setHttpVersion': None, # (!) real value is "<method 'setHttpVersion' of 'panda3d.core.HTTPClient' objects>"
        'setProxySpec': None, # (!) real value is "<method 'setProxySpec' of 'panda3d.core.HTTPClient' objects>"
        'setTryAllDirect': None, # (!) real value is "<method 'setTryAllDirect' of 'panda3d.core.HTTPClient' objects>"
        'setUsername': None, # (!) real value is "<method 'setUsername' of 'panda3d.core.HTTPClient' objects>"
        'setVerifySsl': None, # (!) real value is "<method 'setVerifySsl' of 'panda3d.core.HTTPClient' objects>"
        'set_cipher_list': None, # (!) real value is "<method 'set_cipher_list' of 'panda3d.core.HTTPClient' objects>"
        'set_client_certificate_filename': None, # (!) real value is "<method 'set_client_certificate_filename' of 'panda3d.core.HTTPClient' objects>"
        'set_client_certificate_passphrase': None, # (!) real value is "<method 'set_client_certificate_passphrase' of 'panda3d.core.HTTPClient' objects>"
        'set_client_certificate_pem': None, # (!) real value is "<method 'set_client_certificate_pem' of 'panda3d.core.HTTPClient' objects>"
        'set_cookie': None, # (!) real value is "<method 'set_cookie' of 'panda3d.core.HTTPClient' objects>"
        'set_direct_host_spec': None, # (!) real value is "<method 'set_direct_host_spec' of 'panda3d.core.HTTPClient' objects>"
        'set_http_version': None, # (!) real value is "<method 'set_http_version' of 'panda3d.core.HTTPClient' objects>"
        'set_proxy_spec': None, # (!) real value is "<method 'set_proxy_spec' of 'panda3d.core.HTTPClient' objects>"
        'set_try_all_direct': None, # (!) real value is "<method 'set_try_all_direct' of 'panda3d.core.HTTPClient' objects>"
        'set_username': None, # (!) real value is "<method 'set_username' of 'panda3d.core.HTTPClient' objects>"
        'set_verify_ssl': None, # (!) real value is "<method 'set_verify_ssl' of 'panda3d.core.HTTPClient' objects>"
        'writeCookies': None, # (!) real value is "<method 'writeCookies' of 'panda3d.core.HTTPClient' objects>"
        'write_cookies': None, # (!) real value is "<method 'write_cookies' of 'panda3d.core.HTTPClient' objects>"
    }
    VSNoDateCheck = 1
    VSNormal = 2
    VSNoVerify = 0
    VS_normal = 2
    VS_no_date_check = 1
    VS_no_verify = 0


