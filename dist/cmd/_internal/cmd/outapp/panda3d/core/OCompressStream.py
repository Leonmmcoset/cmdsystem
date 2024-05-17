# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .ostream import ostream

class OCompressStream(ostream):
    """
    /**
     * An input stream object that uses zlib to compress (deflate) data to another
     * destination stream on-the-fly.
     *
     * Attach an OCompressStream to an existing ostream that will accept
     * compressed data, and write your uncompressed source data to the
     * OCompressStream.
     *
     * Seeking is not supported.
     */
    """
    def close(self, const_OCompressStream_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        close(const OCompressStream self)
        
        /**
         * Resets the ZStream to empty, but does not actually close the dest ostream
         * unless owns_dest was true.
         */
        """
        pass

    def open(self, const_OCompressStream_self, ostream_dest, bool_owns_dest, int_compression_level): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        open(const OCompressStream self, ostream dest, bool owns_dest, int compression_level)
        
        /**
         *
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
        '__doc__': '/**\n * An input stream object that uses zlib to compress (deflate) data to another\n * destination stream on-the-fly.\n *\n * Attach an OCompressStream to an existing ostream that will accept\n * compressed data, and write your uncompressed source data to the\n * OCompressStream.\n *\n * Seeking is not supported.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.OCompressStream' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE27A6A0>'
        'close': None, # (!) real value is "<method 'close' of 'panda3d.core.OCompressStream' objects>"
        'open': None, # (!) real value is "<method 'open' of 'panda3d.core.OCompressStream' objects>"
    }


