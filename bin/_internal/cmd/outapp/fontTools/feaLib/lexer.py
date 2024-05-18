# encoding: utf-8
# module fontTools.feaLib.lexer
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\fontTools\feaLib\lexer.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import re as re # C:\Users\leonm\AppData\Local\Programs\Python\Python311\Lib\re\__init__.py
import os as os # C:\Users\leonm\AppData\Local\Programs\Python\Python311\Lib\os.py
import fontTools.feaLib.error as __fontTools_feaLib_error


# no functions
# classes

class FeatureLibError(Exception):
    # no doc
    def __init__(self, message, location): # reliably restored by inspect
        # no doc
        pass

    def __str__(self): # reliably restored by inspect
        # no doc
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class FeatureLibLocation(tuple):
    """ A location in a feature file """
    def _asdict(self): # reliably restored by inspect
        """ Return a new dict which maps field names to their values. """
        pass

    @classmethod
    def _make(cls, *args, **kwargs): # real signature unknown
        """ Make a new FeatureLibLocation object from a sequence or iterable """
        pass

    def _replace(self, **kwds): # reliably restored by inspect
        """ Return a new FeatureLibLocation object replacing specified fields with new values """
        pass

    def __getnewargs__(self): # reliably restored by inspect
        """ Return self as a plain tuple.  Used by copy and pickle. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(_cls, file, line, column): # reliably restored by inspect
        """ Create new instance of FeatureLibLocation(file, line, column) """
        pass

    def __repr__(self): # reliably restored by inspect
        """ Return a nicely formatted representation string """
        pass

    def __str__(self): # reliably restored by inspect
        # no doc
        pass

    column = _tuplegetter(2, 'Alias for field number 2')
    file = _tuplegetter(0, 'Alias for field number 0')
    line = _tuplegetter(1, 'Alias for field number 1')
    _fields = (
        'file',
        'line',
        'column',
    )
    _field_defaults = {}
    __annotations__ = {
        'column': int,
        'file': str,
        'line': '<value is a self-reference, replaced by this string>',
    }
    __match_args__ = (
        'file',
        'line',
        'column',
    )
    __orig_bases__ = (
        None, # (!) real value is '<function NamedTuple at 0x00000261F89C1C60>'
    )
    __slots__ = ()


class IncludedFeaNotFound(__fontTools_feaLib_error.FeatureLibError):
    # no doc
    def __init__(self, message, location): # reliably restored by inspect
        # no doc
        pass

    def __str__(self): # reliably restored by inspect
        # no doc
        pass


class IncludingLexer(object):
    """
    A Lexer that follows include statements.
    
        The OpenType feature file specification states that due to
        historical reasons, relative imports should be resolved in this
        order:
    
        1. If the source font is UFO format, then relative to the UFO's
           font directory
        2. relative to the top-level include file
        3. relative to the parent include file
    
        We only support 1 (via includeDir) and 2.
    """
    def make_lexer_(self, file_or_path): # real signature unknown; restored from __doc__
        """ IncludingLexer.make_lexer_(file_or_path) """
        pass

    def next(self): # real signature unknown; restored from __doc__
        """ IncludingLexer.next(self) """
        pass

    def scan_anonymous_block(self, tag): # real signature unknown; restored from __doc__
        """ IncludingLexer.scan_anonymous_block(self, tag) """
        pass

    def __init__(self, featurefile, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        IncludingLexer.__init__(self, featurefile, *, includeDir=None)
        Initializes an IncludingLexer.
        
                Behavior:
                    If includeDir is passed, it will be used to determine the top-level
                    include directory to use for all encountered include statements. If it is
                    not passed, ``os.path.dirname(featurefile)`` will be considered the
                    include directory.
        """
        pass

    def __iter__(self): # real signature unknown; restored from __doc__
        """ IncludingLexer.__iter__(self) """
        pass

    def __next__(self): # real signature unknown; restored from __doc__
        """ IncludingLexer.__next__(self) """
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __dict__ = None # (!) real value is 'mappingproxy({\'__module__\': \'fontTools.feaLib.lexer\', \'__doc__\': "A Lexer that follows include statements.\\n\\n    The OpenType feature file specification states that due to\\n    historical reasons, relative imports should be resolved in this\\n    order:\\n\\n    1. If the source font is UFO format, then relative to the UFO\'s\\n       font directory\\n    2. relative to the top-level include file\\n    3. relative to the parent include file\\n\\n    We only support 1 (via includeDir) and 2.\\n    ", \'__init__\': <cyfunction IncludingLexer.__init__ at 0x00000261F8B079F0>, \'__iter__\': <cyfunction IncludingLexer.__iter__ at 0x00000261F8B07AC0>, \'next\': <cyfunction IncludingLexer.next at 0x00000261F8B07B90>, \'__next__\': <cyfunction IncludingLexer.__next__ at 0x00000261F8B07D30>, \'make_lexer_\': <staticmethod(<cyfunction IncludingLexer.make_lexer_ at 0x00000261F8B07E00>)>, \'scan_anonymous_block\': <cyfunction IncludingLexer.scan_anonymous_block at 0x00000261F8B07ED0>, \'__dict__\': <attribute \'__dict__\' of \'IncludingLexer\' objects>, \'__weakref__\': <attribute \'__weakref__\' of \'IncludingLexer\' objects>})'


class Lexer(object):
    # no doc
    def location_(self): # real signature unknown; restored from __doc__
        """ Lexer.location_(self) """
        pass

    def next(self): # real signature unknown; restored from __doc__
        """ Lexer.next(self) """
        pass

    def next_(self): # real signature unknown; restored from __doc__
        """ Lexer.next_(self) """
        pass

    def scan_anonymous_block(self, tag): # real signature unknown; restored from __doc__
        """ Lexer.scan_anonymous_block(self, tag) """
        pass

    def scan_over_(self, valid): # real signature unknown; restored from __doc__
        """ Lexer.scan_over_(self, valid) """
        pass

    def scan_until_(self, stop_at): # real signature unknown; restored from __doc__
        """ Lexer.scan_until_(self, stop_at) """
        pass

    def __init__(self, text, filename): # real signature unknown; restored from __doc__
        """ Lexer.__init__(self, text, filename) """
        pass

    def __iter__(self): # real signature unknown; restored from __doc__
        """ Lexer.__iter__(self) """
        pass

    def __next__(self): # real signature unknown; restored from __doc__
        """ Lexer.__next__(self) """
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    ANONYMOUS_BLOCK = 'ANONYMOUS_BLOCK'
    CHAR_DIGIT_ = '0123456789'
    CHAR_HEXDIGIT_ = '0123456789ABCDEFabcdef'
    CHAR_LETTER_ = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    CHAR_NAME_CONTINUATION_ = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789_.+*:^~!/-'
    CHAR_NAME_START_ = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz_+*:.^~!\\'
    CHAR_NEWLINE_ = '\r\n'
    CHAR_SYMBOL_ = ",;:-+'{}[]<>()="
    CHAR_WHITESPACE_ = ' \t'
    CID = 'CID'
    COMMENT = 'COMMENT'
    FILENAME = 'FILENAME'
    FLOAT = 'FLOAT'
    GLYPHCLASS = 'GLYPHCLASS'
    HEXADECIMAL = 'HEXADECIMAL'
    MODE_FILENAME_ = 'FILENAME'
    MODE_NORMAL_ = 'NORMAL'
    NAME = 'NAME'
    NEWLINE = 'NEWLINE'
    NUMBER = 'NUMBER'
    NUMBERS = (
        'NUMBER',
        'HEXADECIMAL',
        'OCTAL',
    )
    OCTAL = 'OCTAL'
    RE_GLYPHCLASS = re.compile('^[A-Za-z_0-9.\\-]+$')
    STRING = 'STRING'
    SYMBOL = 'SYMBOL'
    __dict__ = None # (!) real value is 'mappingproxy({\'__module__\': \'fontTools.feaLib.lexer\', \'NUMBER\': \'NUMBER\', \'HEXADECIMAL\': \'HEXADECIMAL\', \'OCTAL\': \'OCTAL\', \'NUMBERS\': (\'NUMBER\', \'HEXADECIMAL\', \'OCTAL\'), \'FLOAT\': \'FLOAT\', \'STRING\': \'STRING\', \'NAME\': \'NAME\', \'FILENAME\': \'FILENAME\', \'GLYPHCLASS\': \'GLYPHCLASS\', \'CID\': \'CID\', \'SYMBOL\': \'SYMBOL\', \'COMMENT\': \'COMMENT\', \'NEWLINE\': \'NEWLINE\', \'ANONYMOUS_BLOCK\': \'ANONYMOUS_BLOCK\', \'CHAR_WHITESPACE_\': \' \\t\', \'CHAR_NEWLINE_\': \'\\r\\n\', \'CHAR_SYMBOL_\': ",;:-+\'{}[]<>()=", \'CHAR_DIGIT_\': \'0123456789\', \'CHAR_HEXDIGIT_\': \'0123456789ABCDEFabcdef\', \'CHAR_LETTER_\': \'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz\', \'CHAR_NAME_START_\': \'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz_+*:.^~!\\\\\', \'CHAR_NAME_CONTINUATION_\': \'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789_.+*:^~!/-\', \'RE_GLYPHCLASS\': re.compile(\'^[A-Za-z_0-9.\\\\-]+$\'), \'MODE_NORMAL_\': \'NORMAL\', \'MODE_FILENAME_\': \'FILENAME\', \'__init__\': <cyfunction Lexer.__init__ at 0x00000261F8B07030>, \'__iter__\': <cyfunction Lexer.__iter__ at 0x00000261F8B07100>, \'next\': <cyfunction Lexer.next at 0x00000261F8B07440>, \'__next__\': <cyfunction Lexer.__next__ at 0x00000261F8B07510>, \'location_\': <cyfunction Lexer.location_ at 0x00000261F8B075E0>, \'next_\': <cyfunction Lexer.next_ at 0x00000261F8B076B0>, \'scan_over_\': <cyfunction Lexer.scan_over_ at 0x00000261F8B07780>, \'scan_until_\': <cyfunction Lexer.scan_until_ at 0x00000261F8B07850>, \'scan_anonymous_block\': <cyfunction Lexer.scan_anonymous_block at 0x00000261F8B07920>, \'__dict__\': <attribute \'__dict__\' of \'Lexer\' objects>, \'__weakref__\': <attribute \'__weakref__\' of \'Lexer\' objects>, \'__doc__\': None})'


class NonIncludingLexer(IncludingLexer):
    """ Lexer that does not follow `include` statements, emits them as-is. """
    def __init__(self, featurefile, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        IncludingLexer.__init__(self, featurefile, *, includeDir=None)
        Initializes an IncludingLexer.
        
                Behavior:
                    If includeDir is passed, it will be used to determine the top-level
                    include directory to use for all encountered include statements. If it is
                    not passed, ``os.path.dirname(featurefile)`` will be considered the
                    include directory.
        """
        pass

    def __next__(self): # real signature unknown; restored from __doc__
        """ NonIncludingLexer.__next__(self) """
        pass


# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x00000261FA7963D0>'

__spec__ = None # (!) real value is "ModuleSpec(name='fontTools.feaLib.lexer', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x00000261FA7963D0>, origin='C:\\\\Users\\\\leonm\\\\PycharmProjects\\\\leonsystem\\\\venv\\\\Lib\\\\site-packages\\\\fontTools\\\\feaLib\\\\lexer.cp311-win_amd64.pyd')"

__test__ = {}

