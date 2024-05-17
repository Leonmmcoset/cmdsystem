# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .ostream import ostream

class OSubStream(ostream):
    """
    /**
     * An ostream object that presents a subwindow into another ostream.  The
     * first character written to this stream will be the "start" character in the
     * dest istream; no characters may be written to character "end" or later
     * (unless end is zero).
     *
     * The dest stream must be one that we can randomly seek within.  The
     * resulting OSubStream will also support arbitrary seeks.
     */
    """
    def close(self, const_OSubStream_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        close(const OSubStream self)
        
        /**
         * Resets the SubStream to empty, but does not actually close the dest
         * ostream.
         */
        """
        pass

    def open(self, const_OSubStream_self, OStreamWrapper_dest, long_start, long_end, bool_append): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        open(const OSubStream self, OStreamWrapper dest, long start, long end, bool append)
        
        /**
         * Starts the SubStream reading from the indicated dest, with the first
         * character being the character at position "start" within the dest, for end
         * - start total characters.  The character at "end" within the dest will
         * never be read; this will appear to be EOF.
         *
         * If end is zero, it indicates that the OSubStream will continue until the
         * end of the dest stream.
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
        '__doc__': '/**\n * An ostream object that presents a subwindow into another ostream.  The\n * first character written to this stream will be the "start" character in the\n * dest istream; no characters may be written to character "end" or later\n * (unless end is zero).\n *\n * The dest stream must be one that we can randomly seek within.  The\n * resulting OSubStream will also support arbitrary seeks.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.OSubStream' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE278B70>'
        'close': None, # (!) real value is "<method 'close' of 'panda3d.core.OSubStream' objects>"
        'open': None, # (!) real value is "<method 'open' of 'panda3d.core.OSubStream' objects>"
    }


