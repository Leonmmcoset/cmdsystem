# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .ostream import ostream

class OEncryptStream(ostream):
    """
    /**
     * An input stream object that uses OpenSSL to encrypt data to another
     * destination stream on-the-fly.
     *
     * Attach an OEncryptStream to an existing ostream that will accept encrypted
     * data, and write your unencrypted source data to the OEncryptStream.
     *
     * Seeking is not supported.
     */
    """
    def close(self, const_OEncryptStream_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        close(const OEncryptStream self)
        
        /**
         * Resets the EncryptStream to empty, but does not actually close the dest
         * ostream unless owns_dest was true.
         */
        """
        pass

    def open(self, const_OEncryptStream_self, ostream_dest, bool_owns_dest, str_password): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        open(const OEncryptStream self, ostream dest, bool owns_dest, str password)
        
        /**
         *
         */
        """
        pass

    def setAlgorithm(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_algorithm(const OEncryptStream self, str algorithm)
        
        /**
         * Specifies the encryption algorithm that should be used for future calls to
         * open().  The default is whatever is specified by the encryption-algorithm
         * config variable.  The complete set of available algorithms is defined by
         * the current version of OpenSSL.
         *
         * If an invalid algorithm is specified, there is no immediate error return
         * code, but open() will fail.
         */
        """
        pass

    def setIterationCount(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_iteration_count(const OEncryptStream self, int iteration_count)
        
        /**
         * Specifies the number of times to repeatedly hash the key before writing it
         * to the stream in future calls to open().  Its purpose is to make it
         * computationally more expensive for an attacker to search the key space
         * exhaustively.  This should be a multiple of 1,000 and should not exceed
         * about 65 million; the value 0 indicates just one application of the hashing
         * algorithm.
         *
         * The default is whatever is specified by the encryption-iteration-count
         * config variable.
         */
        """
        pass

    def setKeyLength(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_key_length(const OEncryptStream self, int key_length)
        
        /**
         * Specifies the length of the key, in bits, that should be used to encrypt
         * the stream in future calls to open().  The default is whatever is specified
         * by the encryption-key-length config variable.
         *
         * If an invalid key_length for the chosen algorithm is specified, there is no
         * immediate error return code, but open() will fail.
         */
        """
        pass

    def set_algorithm(self, const_OEncryptStream_self, str_algorithm): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_algorithm(const OEncryptStream self, str algorithm)
        
        /**
         * Specifies the encryption algorithm that should be used for future calls to
         * open().  The default is whatever is specified by the encryption-algorithm
         * config variable.  The complete set of available algorithms is defined by
         * the current version of OpenSSL.
         *
         * If an invalid algorithm is specified, there is no immediate error return
         * code, but open() will fail.
         */
        """
        pass

    def set_iteration_count(self, const_OEncryptStream_self, int_iteration_count): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_iteration_count(const OEncryptStream self, int iteration_count)
        
        /**
         * Specifies the number of times to repeatedly hash the key before writing it
         * to the stream in future calls to open().  Its purpose is to make it
         * computationally more expensive for an attacker to search the key space
         * exhaustively.  This should be a multiple of 1,000 and should not exceed
         * about 65 million; the value 0 indicates just one application of the hashing
         * algorithm.
         *
         * The default is whatever is specified by the encryption-iteration-count
         * config variable.
         */
        """
        pass

    def set_key_length(self, const_OEncryptStream_self, int_key_length): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_key_length(const OEncryptStream self, int key_length)
        
        /**
         * Specifies the length of the key, in bits, that should be used to encrypt
         * the stream in future calls to open().  The default is whatever is specified
         * by the encryption-key-length config variable.
         *
         * If an invalid key_length for the chosen algorithm is specified, there is no
         * immediate error return code, but open() will fail.
         */
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    algorithm = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    iteration_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    key_length = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__doc__': '/**\n * An input stream object that uses OpenSSL to encrypt data to another\n * destination stream on-the-fly.\n *\n * Attach an OEncryptStream to an existing ostream that will accept encrypted\n * data, and write your unencrypted source data to the OEncryptStream.\n *\n * Seeking is not supported.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.OEncryptStream' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE264320>'
        'algorithm': None, # (!) real value is "<attribute 'algorithm' of 'panda3d.core.OEncryptStream' objects>"
        'close': None, # (!) real value is "<method 'close' of 'panda3d.core.OEncryptStream' objects>"
        'iteration_count': None, # (!) real value is "<attribute 'iteration_count' of 'panda3d.core.OEncryptStream' objects>"
        'key_length': None, # (!) real value is "<attribute 'key_length' of 'panda3d.core.OEncryptStream' objects>"
        'open': None, # (!) real value is "<method 'open' of 'panda3d.core.OEncryptStream' objects>"
        'setAlgorithm': None, # (!) real value is "<method 'setAlgorithm' of 'panda3d.core.OEncryptStream' objects>"
        'setIterationCount': None, # (!) real value is "<method 'setIterationCount' of 'panda3d.core.OEncryptStream' objects>"
        'setKeyLength': None, # (!) real value is "<method 'setKeyLength' of 'panda3d.core.OEncryptStream' objects>"
        'set_algorithm': None, # (!) real value is "<method 'set_algorithm' of 'panda3d.core.OEncryptStream' objects>"
        'set_iteration_count': None, # (!) real value is "<method 'set_iteration_count' of 'panda3d.core.OEncryptStream' objects>"
        'set_key_length': None, # (!) real value is "<method 'set_key_length' of 'panda3d.core.OEncryptStream' objects>"
    }


