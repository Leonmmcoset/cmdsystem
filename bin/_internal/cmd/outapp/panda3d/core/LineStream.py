# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .ostream import ostream

class LineStream(ostream):
    """
    /**
     * This is a special ostream that writes to a memory buffer, like ostrstream.
     * However, its contents can be continuously extracted as a sequence of lines
     * of text.
     *
     * Unlike ostrstream, which can only be extracted from once (and then the
     * buffer freezes and it can no longer be written to), the LineStream is not
     * otherwise affected when a line of text is extracted.  More text can still
     * be written to it and continuously extracted.
     */
    """
    def getLine(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_line(const LineStream self)
        
        /**
         * Extracts and returns the next line (or partial line) of text available in
         * the LineStream object.  Once the line has been extracted, you may call
         * has_newline() to determine whether or not there was an explicit newline
         * character written following this line.
         */
        """
        pass

    def get_line(self, const_LineStream_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_line(const LineStream self)
        
        /**
         * Extracts and returns the next line (or partial line) of text available in
         * the LineStream object.  Once the line has been extracted, you may call
         * has_newline() to determine whether or not there was an explicit newline
         * character written following this line.
         */
        """
        pass

    def hasNewline(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_newline(LineStream self)
        
        /**
         * Returns true if the line of text most recently returned by get_line() was
         * written out with a terminating newline, or false if a newline character has
         * not yet been written to the LineStream.
         */
        """
        pass

    def has_newline(self, LineStream_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_newline(LineStream self)
        
        /**
         * Returns true if the line of text most recently returned by get_line() was
         * written out with a terminating newline, or false if a newline character has
         * not yet been written to the LineStream.
         */
        """
        pass

    def isTextAvailable(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_text_available(LineStream self)
        
        /**
         * Returns true if there is at least one line of text (or even a partial line)
         * available in the LineStream object.  If this returns true, the line may
         * then be retrieved via get_line().
         */
        """
        pass

    def is_text_available(self, LineStream_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_text_available(LineStream self)
        
        /**
         * Returns true if there is at least one line of text (or even a partial line)
         * available in the LineStream object.  If this returns true, the line may
         * then be retrieved via get_line().
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
        '__doc__': '/**\n * This is a special ostream that writes to a memory buffer, like ostrstream.\n * However, its contents can be continuously extracted as a sequence of lines\n * of text.\n *\n * Unlike ostrstream, which can only be extracted from once (and then the\n * buffer freezes and it can no longer be written to), the LineStream is not\n * otherwise affected when a line of text is extracted.  More text can still\n * be written to it and continuously extracted.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.LineStream' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE25C500>'
        'getLine': None, # (!) real value is "<method 'getLine' of 'panda3d.core.LineStream' objects>"
        'get_line': None, # (!) real value is "<method 'get_line' of 'panda3d.core.LineStream' objects>"
        'hasNewline': None, # (!) real value is "<method 'hasNewline' of 'panda3d.core.LineStream' objects>"
        'has_newline': None, # (!) real value is "<method 'has_newline' of 'panda3d.core.LineStream' objects>"
        'isTextAvailable': None, # (!) real value is "<method 'isTextAvailable' of 'panda3d.core.LineStream' objects>"
        'is_text_available': None, # (!) real value is "<method 'is_text_available' of 'panda3d.core.LineStream' objects>"
    }


