# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .istream import istream

class ISubStream(istream):
    """
    /**
     * An istream object that presents a subwindow into another istream.  The
     * first character read from this stream will be the "start" character from
     * the source istream; just before the file pointer reaches the "end"
     * character, eof is returned.
     *
     * The source stream must be one that we can randomly seek within.  The
     * resulting ISubStream will also support arbitrary seeks.
     */
    """
    def close(self, const_ISubStream_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        close(const ISubStream self)
        
        /**
         * Resets the SubStream to empty, but does not actually close the source
         * istream.
         */
        """
        pass

    def open(self, const_ISubStream_self, IStreamWrapper_source, long_start, long_end): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        open(const ISubStream self, IStreamWrapper source, long start, long end)
        
        /**
         * Starts the SubStream reading from the indicated source, with the first
         * character being the character at position "start" within the source, for
         * end - start total characters.  The character at "end" within the source
         * will never be read; this will appear to be EOF.
         *
         * If end is zero, it indicates that the ISubStream will continue until the
         * end of the source stream.
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
        '__doc__': '/**\n * An istream object that presents a subwindow into another istream.  The\n * first character read from this stream will be the "start" character from\n * the source istream; just before the file pointer reaches the "end"\n * character, eof is returned.\n *\n * The source stream must be one that we can randomly seek within.  The\n * resulting ISubStream will also support arbitrary seeks.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.ISubStream' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE2789A0>'
        'close': None, # (!) real value is "<method 'close' of 'panda3d.core.ISubStream' objects>"
        'open': None, # (!) real value is "<method 'open' of 'panda3d.core.ISubStream' objects>"
    }


