# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


class OpenSSLWrapper(__dtoolconfig.DTOOL_SUPER_BASE):
    """
    /**
     * Provides an interface wrapper around the OpenSSL library, to ensure that
     * the library is properly initialized in the application, and to provide some
     * hooks into global OpenSSL context data.
     */
    """
    def clearCertificates(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_certificates(const OpenSSLWrapper self)
        
        /**
         * Removes all the certificates from the global store, including the compiled-
         * in certificates loaded from ca_bundle_data.c.  You can add new certificates
         * by calling load_certificates().
         */
        """
        pass

    def clear_certificates(self, const_OpenSSLWrapper_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_certificates(const OpenSSLWrapper self)
        
        /**
         * Removes all the certificates from the global store, including the compiled-
         * in certificates loaded from ca_bundle_data.c.  You can add new certificates
         * by calling load_certificates().
         */
        """
        pass

    def getGlobalPtr(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_global_ptr()
        
        /**
         *
         */
        """
        pass

    def get_global_ptr(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_global_ptr()
        
        /**
         *
         */
        """
        pass

    def loadCertificates(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        load_certificates(const OpenSSLWrapper self, const Filename filename)
        
        /**
         * Reads the PEM-formatted certificate(s) (delimited by -----BEGIN
         * CERTIFICATE----- and -----END CERTIFICATE-----) from the indicated file and
         * adds them to the global store object, retrieved via get_x509_store().
         *
         * Returns the number of certificates read on success, or 0 on failure.
         *
         * You should call this only with trusted, locally-stored certificates; not
         * with certificates received from an untrusted source.
         */
        """
        pass

    def loadCertificatesFromDerRam(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        load_certificates_from_der_ram(const OpenSSLWrapper self, str data)
        load_certificates_from_der_ram(const OpenSSLWrapper self, str data, int data_size)
        
        /**
         * Reads a chain of trusted certificates from the indicated data buffer and
         * adds them to the X509_STORE object.  The data buffer should be DER-
         * formatted.  Returns the number of certificates read on success, or 0 on
         * failure.
         *
         * You should call this only with trusted, locally-stored certificates; not
         * with certificates received from an untrusted source.
         */
        
        /**
         * Reads a chain of trusted certificates from the indicated data buffer and
         * adds them to the X509_STORE object.  The data buffer should be DER-
         * formatted.  Returns the number of certificates read on success, or 0 on
         * failure.
         *
         * You should call this only with trusted, locally-stored certificates; not
         * with certificates received from an untrusted source.
         */
        """
        pass

    def loadCertificatesFromPemRam(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        load_certificates_from_pem_ram(const OpenSSLWrapper self, str data)
        load_certificates_from_pem_ram(const OpenSSLWrapper self, str data, int data_size)
        
        /**
         * Reads a chain of trusted certificates from the indicated data buffer and
         * adds them to the X509_STORE object.  The data buffer should be PEM-
         * formatted.  Returns the number of certificates read on success, or 0 on
         * failure.
         *
         * You should call this only with trusted, locally-stored certificates; not
         * with certificates received from an untrusted source.
         */
        
        /**
         * Reads a chain of trusted certificates from the indicated data buffer and
         * adds them to the X509_STORE object.  The data buffer should be PEM-
         * formatted.  Returns the number of certificates read on success, or 0 on
         * failure.
         *
         * You should call this only with trusted, locally-stored certificates; not
         * with certificates received from an untrusted source.
         */
        """
        pass

    def load_certificates(self, const_OpenSSLWrapper_self, const_Filename_filename): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        load_certificates(const OpenSSLWrapper self, const Filename filename)
        
        /**
         * Reads the PEM-formatted certificate(s) (delimited by -----BEGIN
         * CERTIFICATE----- and -----END CERTIFICATE-----) from the indicated file and
         * adds them to the global store object, retrieved via get_x509_store().
         *
         * Returns the number of certificates read on success, or 0 on failure.
         *
         * You should call this only with trusted, locally-stored certificates; not
         * with certificates received from an untrusted source.
         */
        """
        pass

    def load_certificates_from_der_ram(self, const_OpenSSLWrapper_self, str_data): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        load_certificates_from_der_ram(const OpenSSLWrapper self, str data)
        load_certificates_from_der_ram(const OpenSSLWrapper self, str data, int data_size)
        
        /**
         * Reads a chain of trusted certificates from the indicated data buffer and
         * adds them to the X509_STORE object.  The data buffer should be DER-
         * formatted.  Returns the number of certificates read on success, or 0 on
         * failure.
         *
         * You should call this only with trusted, locally-stored certificates; not
         * with certificates received from an untrusted source.
         */
        
        /**
         * Reads a chain of trusted certificates from the indicated data buffer and
         * adds them to the X509_STORE object.  The data buffer should be DER-
         * formatted.  Returns the number of certificates read on success, or 0 on
         * failure.
         *
         * You should call this only with trusted, locally-stored certificates; not
         * with certificates received from an untrusted source.
         */
        """
        pass

    def load_certificates_from_pem_ram(self, const_OpenSSLWrapper_self, str_data): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        load_certificates_from_pem_ram(const OpenSSLWrapper self, str data)
        load_certificates_from_pem_ram(const OpenSSLWrapper self, str data, int data_size)
        
        /**
         * Reads a chain of trusted certificates from the indicated data buffer and
         * adds them to the X509_STORE object.  The data buffer should be PEM-
         * formatted.  Returns the number of certificates read on success, or 0 on
         * failure.
         *
         * You should call this only with trusted, locally-stored certificates; not
         * with certificates received from an untrusted source.
         */
        
        /**
         * Reads a chain of trusted certificates from the indicated data buffer and
         * adds them to the X509_STORE object.  The data buffer should be PEM-
         * formatted.  Returns the number of certificates read on success, or 0 on
         * failure.
         *
         * You should call this only with trusted, locally-stored certificates; not
         * with certificates received from an untrusted source.
         */
        """
        pass

    def notifyDebugSslErrors(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        notify_debug_ssl_errors(const OpenSSLWrapper self)
        
        /**
         * As notify_ssl_errors(), but sends the output to debug instead of warning.
         */
        """
        pass

    def notifySslErrors(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        notify_ssl_errors(const OpenSSLWrapper self)
        
        /**
         * A convenience function that is itself a wrapper around the OpenSSL
         * convenience function to output the recent OpenSSL errors.  This function
         * sends the error string to express_cat.warning().  If REPORT_OPENSSL_ERRORS
         * is not defined, the function does nothing.
         */
        """
        pass

    def notify_debug_ssl_errors(self, const_OpenSSLWrapper_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        notify_debug_ssl_errors(const OpenSSLWrapper self)
        
        /**
         * As notify_ssl_errors(), but sends the output to debug instead of warning.
         */
        """
        pass

    def notify_ssl_errors(self, const_OpenSSLWrapper_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        notify_ssl_errors(const OpenSSLWrapper self)
        
        /**
         * A convenience function that is itself a wrapper around the OpenSSL
         * convenience function to output the recent OpenSSL errors.  This function
         * sends the error string to express_cat.warning().  If REPORT_OPENSSL_ERRORS
         * is not defined, the function does nothing.
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
        '__doc__': '/**\n * Provides an interface wrapper around the OpenSSL library, to ensure that\n * the library is properly initialized in the application, and to provide some\n * hooks into global OpenSSL context data.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.OpenSSLWrapper' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE2792B0>'
        'clearCertificates': None, # (!) real value is "<method 'clearCertificates' of 'panda3d.core.OpenSSLWrapper' objects>"
        'clear_certificates': None, # (!) real value is "<method 'clear_certificates' of 'panda3d.core.OpenSSLWrapper' objects>"
        'getGlobalPtr': None, # (!) real value is '<staticmethod(<built-in method getGlobalPtr of type object at 0x00007FFCFE2792B0>)>'
        'get_global_ptr': None, # (!) real value is '<staticmethod(<built-in method get_global_ptr of type object at 0x00007FFCFE2792B0>)>'
        'loadCertificates': None, # (!) real value is "<method 'loadCertificates' of 'panda3d.core.OpenSSLWrapper' objects>"
        'loadCertificatesFromDerRam': None, # (!) real value is "<method 'loadCertificatesFromDerRam' of 'panda3d.core.OpenSSLWrapper' objects>"
        'loadCertificatesFromPemRam': None, # (!) real value is "<method 'loadCertificatesFromPemRam' of 'panda3d.core.OpenSSLWrapper' objects>"
        'load_certificates': None, # (!) real value is "<method 'load_certificates' of 'panda3d.core.OpenSSLWrapper' objects>"
        'load_certificates_from_der_ram': None, # (!) real value is "<method 'load_certificates_from_der_ram' of 'panda3d.core.OpenSSLWrapper' objects>"
        'load_certificates_from_pem_ram': None, # (!) real value is "<method 'load_certificates_from_pem_ram' of 'panda3d.core.OpenSSLWrapper' objects>"
        'notifyDebugSslErrors': None, # (!) real value is "<method 'notifyDebugSslErrors' of 'panda3d.core.OpenSSLWrapper' objects>"
        'notifySslErrors': None, # (!) real value is "<method 'notifySslErrors' of 'panda3d.core.OpenSSLWrapper' objects>"
        'notify_debug_ssl_errors': None, # (!) real value is "<method 'notify_debug_ssl_errors' of 'panda3d.core.OpenSSLWrapper' objects>"
        'notify_ssl_errors': None, # (!) real value is "<method 'notify_ssl_errors' of 'panda3d.core.OpenSSLWrapper' objects>"
    }


