# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .iostream import iostream

class SubStream(iostream):
    """
    /**
     * Combined ISubStream and OSubStream for bidirectional I/O.
     */
    """
    def close(self, const_SubStream_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        close(const SubStream self)
        
        /**
         * Resets the SubStream to empty, but does not actually close the nested
         * ostream.
         */
        """
        pass

    def open(self, const_SubStream_self, StreamWrapper_nested, long_start, long_end, bool_append): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        open(const SubStream self, StreamWrapper nested, long start, long end, bool append)
        
        /**
         * Starts the SubStream reading and writing from the indicated nested stream,
         * within the indicated range.  "end" is the first character outside of the
         * range.
         *
         * If end is zero, it indicates that the SubStream will continue until the end
         * of the nested stream.
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
        '__doc__': '/**\n * Combined ISubStream and OSubStream for bidirectional I/O.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.SubStream' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE278D40>'
        'close': None, # (!) real value is "<method 'close' of 'panda3d.core.SubStream' objects>"
        'open': None, # (!) real value is "<method 'open' of 'panda3d.core.SubStream' objects>"
    }


