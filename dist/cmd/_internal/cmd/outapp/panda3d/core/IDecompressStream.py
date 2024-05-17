# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .istream import istream

class IDecompressStream(istream):
    """
    /**
     * An input stream object that uses zlib to decompress (inflate) the input
     * from another source stream on-the-fly.
     *
     * Attach an IDecompressStream to an existing istream that provides compressed
     * data, and read the corresponding uncompressed data from the
     * IDecompressStream.
     *
     * Seeking is not supported.
     */
    """
    def close(self, const_IDecompressStream_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        close(const IDecompressStream self)
        
        /**
         * Resets the ZStream to empty, but does not actually close the source istream
         * unless owns_source was true.
         */
        """
        pass

    def open(self, const_IDecompressStream_self, istream_source, bool_owns_source): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        open(const IDecompressStream self, istream source, bool owns_source)
        
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
        '__doc__': '/**\n * An input stream object that uses zlib to decompress (inflate) the input\n * from another source stream on-the-fly.\n *\n * Attach an IDecompressStream to an existing istream that provides compressed\n * data, and read the corresponding uncompressed data from the\n * IDecompressStream.\n *\n * Seeking is not supported.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.IDecompressStream' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE27A4D0>'
        'close': None, # (!) real value is "<method 'close' of 'panda3d.core.IDecompressStream' objects>"
        'open': None, # (!) real value is "<method 'open' of 'panda3d.core.IDecompressStream' objects>"
    }


