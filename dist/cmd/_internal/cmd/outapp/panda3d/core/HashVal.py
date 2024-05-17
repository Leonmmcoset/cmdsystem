# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


class HashVal(__dtoolconfig.DTOOL_SUPER_BASE):
    """
    /**
     * Stores a 128-bit value that represents the hashed contents (typically MD5)
     * of a file or buffer.
     */
    """
    def asBin(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        as_bin(HashVal self)
        
        /**
         * Returns the HashVal as a 16-byte binary string.
         */
        """
        pass

    def asDec(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        as_dec(HashVal self)
        
        /**
         * Returns the HashVal as a string with four decimal numbers.
         */
        """
        pass

    def asHex(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        as_hex(HashVal self)
        
        /**
         * Returns the HashVal as a 32-byte hexadecimal string.
         */
        """
        pass

    def assign(self, const_HashVal_self, const_HashVal_copy): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        assign(const HashVal self, const HashVal copy)
        """
        pass

    def as_bin(self, HashVal_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        as_bin(HashVal self)
        
        /**
         * Returns the HashVal as a 16-byte binary string.
         */
        """
        pass

    def as_dec(self, HashVal_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        as_dec(HashVal self)
        
        /**
         * Returns the HashVal as a string with four decimal numbers.
         */
        """
        pass

    def as_hex(self, HashVal_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        as_hex(HashVal self)
        
        /**
         * Returns the HashVal as a 32-byte hexadecimal string.
         */
        """
        pass

    def compareTo(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        compare_to(HashVal self, const HashVal other)
        
        /**
         *
         */
        """
        pass

    def compare_to(self, HashVal_self, const_HashVal_other): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        compare_to(HashVal self, const HashVal other)
        
        /**
         *
         */
        """
        pass

    def hashBuffer(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        hash_buffer(const HashVal self, str buffer, int length)
        
        /**
         * Generates the hash value by hashing the indicated data.  This method is
         * only defined if we have the OpenSSL library (which provides md5
         * functionality) available.
         */
        """
        pass

    def hashBytes(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        hash_bytes(const HashVal self, bytes data)
        
        /**
         * Generates the hash value by hashing the indicated data.  This method is
         * only defined if we have the OpenSSL library (which provides md5
         * functionality) available.
         */
        """
        pass

    def hashFile(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        hash_file(const HashVal self, const Filename filename)
        
        /**
         * Generates the hash value from the indicated file.  Returns true on success,
         * false if the file cannot be read.  This method is only defined if we have
         * the OpenSSL library (which provides md5 functionality) available.
         */
        """
        pass

    def hashRamfile(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        hash_ramfile(const HashVal self, const Ramfile ramfile)
        
        /**
         * Generates the hash value by hashing the indicated data.  This method is
         * only defined if we have the OpenSSL library (which provides md5
         * functionality) available.
         */
        """
        pass

    def hashStream(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        hash_stream(const HashVal self, istream stream)
        
        /**
         * Generates the hash value from the indicated file.  Returns true on success,
         * false if the file cannot be read.  This method is only defined if we have
         * the OpenSSL library (which provides md5 functionality) available.
         */
        """
        pass

    def hashString(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        hash_string(const HashVal self, str data)
        
        /**
         * Generates the hash value by hashing the indicated data.  This method is
         * only defined if we have the OpenSSL library (which provides md5
         * functionality) available.
         */
        """
        pass

    def hash_buffer(self, const_HashVal_self, str_buffer, int_length): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        hash_buffer(const HashVal self, str buffer, int length)
        
        /**
         * Generates the hash value by hashing the indicated data.  This method is
         * only defined if we have the OpenSSL library (which provides md5
         * functionality) available.
         */
        """
        pass

    def hash_bytes(self, const_HashVal_self, bytes_data): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        hash_bytes(const HashVal self, bytes data)
        
        /**
         * Generates the hash value by hashing the indicated data.  This method is
         * only defined if we have the OpenSSL library (which provides md5
         * functionality) available.
         */
        """
        pass

    def hash_file(self, const_HashVal_self, const_Filename_filename): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        hash_file(const HashVal self, const Filename filename)
        
        /**
         * Generates the hash value from the indicated file.  Returns true on success,
         * false if the file cannot be read.  This method is only defined if we have
         * the OpenSSL library (which provides md5 functionality) available.
         */
        """
        pass

    def hash_ramfile(self, const_HashVal_self, const_Ramfile_ramfile): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        hash_ramfile(const HashVal self, const Ramfile ramfile)
        
        /**
         * Generates the hash value by hashing the indicated data.  This method is
         * only defined if we have the OpenSSL library (which provides md5
         * functionality) available.
         */
        """
        pass

    def hash_stream(self, const_HashVal_self, istream_stream): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        hash_stream(const HashVal self, istream stream)
        
        /**
         * Generates the hash value from the indicated file.  Returns true on success,
         * false if the file cannot be read.  This method is only defined if we have
         * the OpenSSL library (which provides md5 functionality) available.
         */
        """
        pass

    def hash_string(self, const_HashVal_self, str_data): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        hash_string(const HashVal self, str data)
        
        /**
         * Generates the hash value by hashing the indicated data.  This method is
         * only defined if we have the OpenSSL library (which provides md5
         * functionality) available.
         */
        """
        pass

    def inputBinary(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        input_binary(const HashVal self, istream in)
        
        /**
         * Inputs the HashVal as a binary stream of bytes in order.  This is not the
         * same order expected by read_stream().
         */
        """
        pass

    def inputDec(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        input_dec(const HashVal self, istream in)
        
        /**
         * Inputs the HashVal as four unsigned decimal integers.
         */
        """
        pass

    def inputHex(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        input_hex(const HashVal self, istream in)
        
        /**
         * Inputs the HashVal as a 32-digit hexadecimal number.
         */
        """
        pass

    def input_binary(self, const_HashVal_self, istream_in): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        input_binary(const HashVal self, istream in)
        
        /**
         * Inputs the HashVal as a binary stream of bytes in order.  This is not the
         * same order expected by read_stream().
         */
        """
        pass

    def input_dec(self, const_HashVal_self, istream_in): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        input_dec(const HashVal self, istream in)
        
        /**
         * Inputs the HashVal as four unsigned decimal integers.
         */
        """
        pass

    def input_hex(self, const_HashVal_self, istream_in): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        input_hex(const HashVal self, istream in)
        
        /**
         * Inputs the HashVal as a 32-digit hexadecimal number.
         */
        """
        pass

    def mergeWith(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        merge_with(const HashVal self, const HashVal other)
        
        /**
         * Generates a new HashVal representing the xor of this one and the other one.
         */
        """
        pass

    def merge_with(self, const_HashVal_self, const_HashVal_other): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        merge_with(const HashVal self, const HashVal other)
        
        /**
         * Generates a new HashVal representing the xor of this one and the other one.
         */
        """
        pass

    def output(self, HashVal_self, ostream_out): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        output(HashVal self, ostream out)
        
        /**
         *
         */
        """
        pass

    def outputBinary(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        output_binary(HashVal self, ostream out)
        
        /**
         * Outputs the HashVal as a binary stream of bytes in order.  This is not the
         * same order generated by write_stream().
         */
        """
        pass

    def outputDec(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        output_dec(HashVal self, ostream out)
        
        /**
         * Outputs the HashVal as four unsigned decimal integers.
         */
        """
        pass

    def outputHex(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        output_hex(HashVal self, ostream out)
        
        /**
         * Outputs the HashVal as a 32-digit hexadecimal number.
         */
        """
        pass

    def output_binary(self, HashVal_self, ostream_out): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        output_binary(HashVal self, ostream out)
        
        /**
         * Outputs the HashVal as a binary stream of bytes in order.  This is not the
         * same order generated by write_stream().
         */
        """
        pass

    def output_dec(self, HashVal_self, ostream_out): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        output_dec(HashVal self, ostream out)
        
        /**
         * Outputs the HashVal as four unsigned decimal integers.
         */
        """
        pass

    def output_hex(self, HashVal_self, ostream_out): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        output_hex(HashVal self, ostream out)
        
        /**
         * Outputs the HashVal as a 32-digit hexadecimal number.
         */
        """
        pass

    def readDatagram(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        read_datagram(const HashVal self, DatagramIterator source)
        
        /**
         *
         */
        """
        pass

    def readStream(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        read_stream(const HashVal self, StreamReader source)
        
        /**
         *
         */
        """
        pass

    def read_datagram(self, const_HashVal_self, DatagramIterator_source): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        read_datagram(const HashVal self, DatagramIterator source)
        
        /**
         *
         */
        """
        pass

    def read_stream(self, const_HashVal_self, StreamReader_source): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        read_stream(const HashVal self, StreamReader source)
        
        /**
         *
         */
        """
        pass

    def setFromBin(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_from_bin(const HashVal self, bytes text)
        
        /**
         * Sets the HashVal from a 16-byte binary string.  Returns true if successful,
         * false otherwise.
         */
        """
        pass

    def setFromDec(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_from_dec(const HashVal self, str text)
        
        /**
         * Sets the HashVal from a string with four decimal numbers.  Returns true if
         * valid, false otherwise.
         */
        """
        pass

    def setFromHex(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_from_hex(const HashVal self, str text)
        
        /**
         * Sets the HashVal from a 32-byte hexademical string.  Returns true if
         * successful, false otherwise.
         */
        """
        pass

    def set_from_bin(self, const_HashVal_self, bytes_text): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_from_bin(const HashVal self, bytes text)
        
        /**
         * Sets the HashVal from a 16-byte binary string.  Returns true if successful,
         * false otherwise.
         */
        """
        pass

    def set_from_dec(self, const_HashVal_self, str_text): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_from_dec(const HashVal self, str text)
        
        /**
         * Sets the HashVal from a string with four decimal numbers.  Returns true if
         * valid, false otherwise.
         */
        """
        pass

    def set_from_hex(self, const_HashVal_self, str_text): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_from_hex(const HashVal self, str text)
        
        /**
         * Sets the HashVal from a 32-byte hexademical string.  Returns true if
         * successful, false otherwise.
         */
        """
        pass

    def writeDatagram(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        write_datagram(HashVal self, Datagram destination)
        
        /**
         *
         */
        """
        pass

    def writeStream(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        write_stream(HashVal self, StreamWriter destination)
        
        /**
         *
         */
        """
        pass

    def write_datagram(self, HashVal_self, Datagram_destination): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        write_datagram(HashVal self, Datagram destination)
        
        /**
         *
         */
        """
        pass

    def write_stream(self, HashVal_self, StreamWriter_destination): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        write_stream(HashVal self, StreamWriter destination)
        
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

    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.core.HashVal' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.core.HashVal' objects>"
        '__doc__': '/**\n * Stores a 128-bit value that represents the hashed contents (typically MD5)\n * of a file or buffer.\n */',
        '__eq__': None, # (!) real value is "<slot wrapper '__eq__' of 'panda3d.core.HashVal' objects>"
        '__ge__': None, # (!) real value is "<slot wrapper '__ge__' of 'panda3d.core.HashVal' objects>"
        '__gt__': None, # (!) real value is "<slot wrapper '__gt__' of 'panda3d.core.HashVal' objects>"
        '__hash__': None, # (!) real value is "<slot wrapper '__hash__' of 'panda3d.core.HashVal' objects>"
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.HashVal' objects>"
        '__le__': None, # (!) real value is "<slot wrapper '__le__' of 'panda3d.core.HashVal' objects>"
        '__lt__': None, # (!) real value is "<slot wrapper '__lt__' of 'panda3d.core.HashVal' objects>"
        '__ne__': None, # (!) real value is "<slot wrapper '__ne__' of 'panda3d.core.HashVal' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE278600>'
        '__repr__': None, # (!) real value is "<slot wrapper '__repr__' of 'panda3d.core.HashVal' objects>"
        '__str__': None, # (!) real value is "<slot wrapper '__str__' of 'panda3d.core.HashVal' objects>"
        'asBin': None, # (!) real value is "<method 'asBin' of 'panda3d.core.HashVal' objects>"
        'asDec': None, # (!) real value is "<method 'asDec' of 'panda3d.core.HashVal' objects>"
        'asHex': None, # (!) real value is "<method 'asHex' of 'panda3d.core.HashVal' objects>"
        'as_bin': None, # (!) real value is "<method 'as_bin' of 'panda3d.core.HashVal' objects>"
        'as_dec': None, # (!) real value is "<method 'as_dec' of 'panda3d.core.HashVal' objects>"
        'as_hex': None, # (!) real value is "<method 'as_hex' of 'panda3d.core.HashVal' objects>"
        'assign': None, # (!) real value is "<method 'assign' of 'panda3d.core.HashVal' objects>"
        'compareTo': None, # (!) real value is "<method 'compareTo' of 'panda3d.core.HashVal' objects>"
        'compare_to': None, # (!) real value is "<method 'compare_to' of 'panda3d.core.HashVal' objects>"
        'hashBuffer': None, # (!) real value is "<method 'hashBuffer' of 'panda3d.core.HashVal' objects>"
        'hashBytes': None, # (!) real value is "<method 'hashBytes' of 'panda3d.core.HashVal' objects>"
        'hashFile': None, # (!) real value is "<method 'hashFile' of 'panda3d.core.HashVal' objects>"
        'hashRamfile': None, # (!) real value is "<method 'hashRamfile' of 'panda3d.core.HashVal' objects>"
        'hashStream': None, # (!) real value is "<method 'hashStream' of 'panda3d.core.HashVal' objects>"
        'hashString': None, # (!) real value is "<method 'hashString' of 'panda3d.core.HashVal' objects>"
        'hash_buffer': None, # (!) real value is "<method 'hash_buffer' of 'panda3d.core.HashVal' objects>"
        'hash_bytes': None, # (!) real value is "<method 'hash_bytes' of 'panda3d.core.HashVal' objects>"
        'hash_file': None, # (!) real value is "<method 'hash_file' of 'panda3d.core.HashVal' objects>"
        'hash_ramfile': None, # (!) real value is "<method 'hash_ramfile' of 'panda3d.core.HashVal' objects>"
        'hash_stream': None, # (!) real value is "<method 'hash_stream' of 'panda3d.core.HashVal' objects>"
        'hash_string': None, # (!) real value is "<method 'hash_string' of 'panda3d.core.HashVal' objects>"
        'inputBinary': None, # (!) real value is "<method 'inputBinary' of 'panda3d.core.HashVal' objects>"
        'inputDec': None, # (!) real value is "<method 'inputDec' of 'panda3d.core.HashVal' objects>"
        'inputHex': None, # (!) real value is "<method 'inputHex' of 'panda3d.core.HashVal' objects>"
        'input_binary': None, # (!) real value is "<method 'input_binary' of 'panda3d.core.HashVal' objects>"
        'input_dec': None, # (!) real value is "<method 'input_dec' of 'panda3d.core.HashVal' objects>"
        'input_hex': None, # (!) real value is "<method 'input_hex' of 'panda3d.core.HashVal' objects>"
        'mergeWith': None, # (!) real value is "<method 'mergeWith' of 'panda3d.core.HashVal' objects>"
        'merge_with': None, # (!) real value is "<method 'merge_with' of 'panda3d.core.HashVal' objects>"
        'output': None, # (!) real value is "<method 'output' of 'panda3d.core.HashVal' objects>"
        'outputBinary': None, # (!) real value is "<method 'outputBinary' of 'panda3d.core.HashVal' objects>"
        'outputDec': None, # (!) real value is "<method 'outputDec' of 'panda3d.core.HashVal' objects>"
        'outputHex': None, # (!) real value is "<method 'outputHex' of 'panda3d.core.HashVal' objects>"
        'output_binary': None, # (!) real value is "<method 'output_binary' of 'panda3d.core.HashVal' objects>"
        'output_dec': None, # (!) real value is "<method 'output_dec' of 'panda3d.core.HashVal' objects>"
        'output_hex': None, # (!) real value is "<method 'output_hex' of 'panda3d.core.HashVal' objects>"
        'readDatagram': None, # (!) real value is "<method 'readDatagram' of 'panda3d.core.HashVal' objects>"
        'readStream': None, # (!) real value is "<method 'readStream' of 'panda3d.core.HashVal' objects>"
        'read_datagram': None, # (!) real value is "<method 'read_datagram' of 'panda3d.core.HashVal' objects>"
        'read_stream': None, # (!) real value is "<method 'read_stream' of 'panda3d.core.HashVal' objects>"
        'setFromBin': None, # (!) real value is "<method 'setFromBin' of 'panda3d.core.HashVal' objects>"
        'setFromDec': None, # (!) real value is "<method 'setFromDec' of 'panda3d.core.HashVal' objects>"
        'setFromHex': None, # (!) real value is "<method 'setFromHex' of 'panda3d.core.HashVal' objects>"
        'set_from_bin': None, # (!) real value is "<method 'set_from_bin' of 'panda3d.core.HashVal' objects>"
        'set_from_dec': None, # (!) real value is "<method 'set_from_dec' of 'panda3d.core.HashVal' objects>"
        'set_from_hex': None, # (!) real value is "<method 'set_from_hex' of 'panda3d.core.HashVal' objects>"
        'writeDatagram': None, # (!) real value is "<method 'writeDatagram' of 'panda3d.core.HashVal' objects>"
        'writeStream': None, # (!) real value is "<method 'writeStream' of 'panda3d.core.HashVal' objects>"
        'write_datagram': None, # (!) real value is "<method 'write_datagram' of 'panda3d.core.HashVal' objects>"
        'write_stream': None, # (!) real value is "<method 'write_stream' of 'panda3d.core.HashVal' objects>"
    }


