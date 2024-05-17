# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


class TextEncoder(__dtoolconfig.DTOOL_SUPER_BASE):
    """
    /**
     * This class can be used to convert text between multiple representations,
     * e.g.  UTF-8 to UTF-16.  You may use it as a static class object, passing
     * the encoding each time, or you may create an instance and use that object,
     * which will record the current encoding and retain the current string.
     *
     * This class is also a base class of TextNode, which inherits this
     * functionality.
     */
    """
    def appendText(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        append_text(const TextEncoder self, object text)
        
        /**
         * Appends the indicates string to the end of the stored text.
         */
        """
        pass

    def appendUnicodeChar(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        append_unicode_char(const TextEncoder self, int character)
        
        /**
         * Appends a single character to the end of the stored text.  This may be a
         * wide character, up to 16 bits in Unicode.
         */
        """
        pass

    def appendWtext(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        append_wtext(const TextEncoder self, unicode text)
        
        /**
         * Appends the indicates string to the end of the stored wide-character text.
         */
        """
        pass

    def append_text(self, const_TextEncoder_self, object_text): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        append_text(const TextEncoder self, object text)
        
        /**
         * Appends the indicates string to the end of the stored text.
         */
        """
        pass

    def append_unicode_char(self, const_TextEncoder_self, int_character): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        append_unicode_char(const TextEncoder self, int character)
        
        /**
         * Appends a single character to the end of the stored text.  This may be a
         * wide character, up to 16 bits in Unicode.
         */
        """
        pass

    def append_wtext(self, const_TextEncoder_self, unicode_text): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        append_wtext(const TextEncoder self, unicode text)
        
        /**
         * Appends the indicates string to the end of the stored wide-character text.
         */
        """
        pass

    def clearText(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_text(const TextEncoder self)
        
        /**
         * Removes the text from the TextEncoder.
         */
        """
        pass

    def clear_text(self, const_TextEncoder_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_text(const TextEncoder self)
        
        /**
         * Removes the text from the TextEncoder.
         */
        """
        pass

    def decodeText(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        decode_text(TextEncoder self, object text)
        decode_text(object text, int encoding)
        
        /**
         * Returns the given wstring decoded to a single-byte string, via the current
         * encoding system.
         */
        
        /**
         * Returns the given wstring decoded to a single-byte string, via the given
         * encoding system.
         */
        """
        pass

    def decode_text(self, TextEncoder_self, object_text): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        decode_text(TextEncoder self, object text)
        decode_text(object text, int encoding)
        
        /**
         * Returns the given wstring decoded to a single-byte string, via the current
         * encoding system.
         */
        
        /**
         * Returns the given wstring decoded to a single-byte string, via the given
         * encoding system.
         */
        """
        pass

    def encodeWchar(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        encode_wchar(int ch, int encoding)
        
        /**
         * Encodes a single Unicode character into a one-, two-, three-, or four-byte
         * string, according to the given encoding system.
         */
        """
        pass

    def encodeWtext(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        encode_wtext(TextEncoder self, unicode wtext)
        encode_wtext(unicode wtext, int encoding)
        
        /**
         * Encodes a wide-text string into a single-char string, according to the
         * current encoding.
         */
        
        /**
         * Encodes a wide-text string into a single-char string, according to the
         * given encoding.
         */
        """
        pass

    def encode_wchar(self, int_ch, int_encoding): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        encode_wchar(int ch, int encoding)
        
        /**
         * Encodes a single Unicode character into a one-, two-, three-, or four-byte
         * string, according to the given encoding system.
         */
        """
        pass

    def encode_wtext(self, TextEncoder_self, unicode_wtext): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        encode_wtext(TextEncoder self, unicode wtext)
        encode_wtext(unicode wtext, int encoding)
        
        /**
         * Encodes a wide-text string into a single-char string, according to the
         * current encoding.
         */
        
        /**
         * Encodes a wide-text string into a single-char string, according to the
         * given encoding.
         */
        """
        pass

    def getDefaultEncoding(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_default_encoding()
        
        /**
         * Specifies the default encoding to be used for all subsequently created
         * TextEncoder objects.  See set_encoding().
         */
        """
        pass

    def getEncodedChar(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_encoded_char(TextEncoder self, int index)
        get_encoded_char(TextEncoder self, int index, int encoding)
        
        /**
         * Returns the nth char of the stored text, as a one-, two-, or three-byte
         * encoded string.
         */
        
        /**
         * Returns the nth char of the stored text, as a one-, two-, or three-byte
         * encoded string.
         */
        """
        pass

    def getEncoding(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_encoding(TextEncoder self)
        
        /**
         * Returns the encoding by which the string set via set_text() is to be
         * interpreted.  See set_encoding().
         */
        """
        pass

    def getNumChars(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_chars(TextEncoder self)
        
        /**
         * Returns the number of characters in the stored text.  This is a count of
         * wide characters, after the string has been decoded according to
         * set_encoding().
         */
        """
        pass

    def getText(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_text(TextEncoder self)
        get_text(TextEncoder self, int encoding)
        
        /**
         * Returns the current text, as encoded via the current encoding system.
         */
        
        /**
         * Returns the current text, as encoded via the indicated encoding system.
         */
        """
        pass

    def getTextAsAscii(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_text_as_ascii(TextEncoder self)
        
        /**
         * Returns the text associated with the node, converted as nearly as possible
         * to a fully-ASCII representation.  This means replacing accented letters
         * with their unaccented ASCII equivalents.
         *
         * It is possible that some characters in the string cannot be converted to
         * ASCII.  (The string may involve symbols like the copyright symbol, for
         * instance, or it might involve letters in some other alphabet such as Greek
         * or Cyrillic, or even Latin letters like thorn or eth that are not part of
         * the ASCII character set.)  In this case, as much of the string as possible
         * will be converted to ASCII, and the nonconvertible characters will remain
         * encoded in the encoding specified by set_encoding().
         */
        """
        pass

    def getUnicodeChar(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_unicode_char(TextEncoder self, int index)
        
        /**
         * Returns the Unicode value of the nth character in the stored text.  This
         * may be a wide character (greater than 255), after the string has been
         * decoded according to set_encoding().
         */
        """
        pass

    def getWtext(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_wtext(TextEncoder self)
        
        /**
         * Returns the text associated with the TextEncoder, as a wide-character
         * string.
         */
        """
        pass

    def getWtextAsAscii(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_wtext_as_ascii(TextEncoder self)
        
        /**
         * Returns the text associated with the node, converted as nearly as possible
         * to a fully-ASCII representation.  This means replacing accented letters
         * with their unaccented ASCII equivalents.
         *
         * It is possible that some characters in the string cannot be converted to
         * ASCII.  (The string may involve symbols like the copyright symbol, for
         * instance, or it might involve letters in some other alphabet such as Greek
         * or Cyrillic, or even Latin letters like thorn or eth that are not part of
         * the ASCII character set.)  In this case, as much of the string as possible
         * will be converted to ASCII, and the nonconvertible characters will remain
         * in their original form.
         */
        """
        pass

    def get_default_encoding(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_default_encoding()
        
        /**
         * Specifies the default encoding to be used for all subsequently created
         * TextEncoder objects.  See set_encoding().
         */
        """
        pass

    def get_encoded_char(self, TextEncoder_self, int_index): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_encoded_char(TextEncoder self, int index)
        get_encoded_char(TextEncoder self, int index, int encoding)
        
        /**
         * Returns the nth char of the stored text, as a one-, two-, or three-byte
         * encoded string.
         */
        
        /**
         * Returns the nth char of the stored text, as a one-, two-, or three-byte
         * encoded string.
         */
        """
        pass

    def get_encoding(self, TextEncoder_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_encoding(TextEncoder self)
        
        /**
         * Returns the encoding by which the string set via set_text() is to be
         * interpreted.  See set_encoding().
         */
        """
        pass

    def get_num_chars(self, TextEncoder_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_chars(TextEncoder self)
        
        /**
         * Returns the number of characters in the stored text.  This is a count of
         * wide characters, after the string has been decoded according to
         * set_encoding().
         */
        """
        pass

    def get_text(self, TextEncoder_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_text(TextEncoder self)
        get_text(TextEncoder self, int encoding)
        
        /**
         * Returns the current text, as encoded via the current encoding system.
         */
        
        /**
         * Returns the current text, as encoded via the indicated encoding system.
         */
        """
        pass

    def get_text_as_ascii(self, TextEncoder_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_text_as_ascii(TextEncoder self)
        
        /**
         * Returns the text associated with the node, converted as nearly as possible
         * to a fully-ASCII representation.  This means replacing accented letters
         * with their unaccented ASCII equivalents.
         *
         * It is possible that some characters in the string cannot be converted to
         * ASCII.  (The string may involve symbols like the copyright symbol, for
         * instance, or it might involve letters in some other alphabet such as Greek
         * or Cyrillic, or even Latin letters like thorn or eth that are not part of
         * the ASCII character set.)  In this case, as much of the string as possible
         * will be converted to ASCII, and the nonconvertible characters will remain
         * encoded in the encoding specified by set_encoding().
         */
        """
        pass

    def get_unicode_char(self, TextEncoder_self, int_index): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_unicode_char(TextEncoder self, int index)
        
        /**
         * Returns the Unicode value of the nth character in the stored text.  This
         * may be a wide character (greater than 255), after the string has been
         * decoded according to set_encoding().
         */
        """
        pass

    def get_wtext(self, TextEncoder_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_wtext(TextEncoder self)
        
        /**
         * Returns the text associated with the TextEncoder, as a wide-character
         * string.
         */
        """
        pass

    def get_wtext_as_ascii(self, TextEncoder_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_wtext_as_ascii(TextEncoder self)
        
        /**
         * Returns the text associated with the node, converted as nearly as possible
         * to a fully-ASCII representation.  This means replacing accented letters
         * with their unaccented ASCII equivalents.
         *
         * It is possible that some characters in the string cannot be converted to
         * ASCII.  (The string may involve symbols like the copyright symbol, for
         * instance, or it might involve letters in some other alphabet such as Greek
         * or Cyrillic, or even Latin letters like thorn or eth that are not part of
         * the ASCII character set.)  In this case, as much of the string as possible
         * will be converted to ASCII, and the nonconvertible characters will remain
         * in their original form.
         */
        """
        pass

    def hasText(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_text(TextEncoder self)
        
        /**
         *
         */
        """
        pass

    def has_text(self, TextEncoder_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_text(TextEncoder self)
        
        /**
         *
         */
        """
        pass

    def isWtext(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_wtext(TextEncoder self)
        
        /**
         * Returns true if any of the characters in the string returned by get_wtext()
         * are out of the range of an ASCII character (and, therefore, get_wtext()
         * should be called in preference to get_text()).
         */
        """
        pass

    def is_wtext(self, TextEncoder_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_wtext(TextEncoder self)
        
        /**
         * Returns true if any of the characters in the string returned by get_wtext()
         * are out of the range of an ASCII character (and, therefore, get_wtext()
         * should be called in preference to get_text()).
         */
        """
        pass

    def lower(self, str_source): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        lower(str source)
        lower(str source, int encoding)
        
        /**
         * Converts the string to lowercase, assuming the string is encoded in the
         * default encoding.
         */
        
        /**
         * Converts the string to lowercase, assuming the string is encoded in the
         * indicated encoding.
         */
        """
        pass

    def makeLower(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        make_lower(const TextEncoder self)
        
        /**
         * Adjusts the text stored within the encoder to all lowercase letters
         * (preserving accent marks correctly).
         */
        """
        pass

    def makeUpper(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        make_upper(const TextEncoder self)
        
        /**
         * Adjusts the text stored within the encoder to all uppercase letters
         * (preserving accent marks correctly).
         */
        """
        pass

    def make_lower(self, const_TextEncoder_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        make_lower(const TextEncoder self)
        
        /**
         * Adjusts the text stored within the encoder to all lowercase letters
         * (preserving accent marks correctly).
         */
        """
        pass

    def make_upper(self, const_TextEncoder_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        make_upper(const TextEncoder self)
        
        /**
         * Adjusts the text stored within the encoder to all uppercase letters
         * (preserving accent marks correctly).
         */
        """
        pass

    def reencodeText(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        reencode_text(str text, int from, int to)
        
        /**
         * Given the indicated text string, which is assumed to be encoded via the
         * encoding "from", decodes it and then reencodes it into the encoding "to",
         * and returns the newly encoded string.  This does not change or affect any
         * properties on the TextEncoder itself.
         */
        """
        pass

    def reencode_text(self, str_text, int_from, int_to): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        reencode_text(str text, int from, int to)
        
        /**
         * Given the indicated text string, which is assumed to be encoded via the
         * encoding "from", decodes it and then reencodes it into the encoding "to",
         * and returns the newly encoded string.  This does not change or affect any
         * properties on the TextEncoder itself.
         */
        """
        pass

    def setDefaultEncoding(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_default_encoding(int encoding)
        
        /**
         * Specifies the default encoding to be used for all subsequently created
         * TextEncoder objects.  See set_encoding().
         */
        """
        pass

    def setEncoding(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_encoding(const TextEncoder self, int encoding)
        
        /**
         * Specifies how the string set via set_text() is to be interpreted.  The
         * default, E_iso8859, means a standard string with one-byte characters (i.e.
         * ASCII).  Other encodings are possible to take advantage of character sets
         * with more than 256 characters.
         *
         * This affects only future calls to set_text(); it does not change text that
         * was set previously.
         */
        """
        pass

    def setText(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_text(const TextEncoder self, object text)
        set_text(const TextEncoder self, object text, int encoding)
        
        /**
         * Changes the text that is stored in the encoder.  The text should be encoded
         * according to the method indicated by set_encoding().  Subsequent calls to
         * get_text() will return this same string, while get_wtext() will return the
         * decoded version of the string.
         */
        
        /**
         * The two-parameter version of set_text() accepts an explicit encoding; the
         * text is immediately decoded and stored as a wide-character string.
         * Subsequent calls to get_text() will return the same text re-encoded using
         * whichever encoding is specified by set_encoding().
         */
        """
        pass

    def setUnicodeChar(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_unicode_char(const TextEncoder self, int index, int character)
        
        /**
         * Sets the Unicode value of the nth character in the stored text.  This may
         * be a wide character (greater than 255), after the string has been decoded
         * according to set_encoding().
         */
        """
        pass

    def setWtext(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_wtext(const TextEncoder self, unicode wtext)
        
        // Direct support for wide-character strings.  Now publishable with the new
        // wstring support in interrogate.
        
        /**
         * Changes the text that is stored in the encoder.  Subsequent calls to
         * get_wtext() will return this same string, while get_text() will return the
         * encoded version of the string.
         */
        """
        pass

    def set_default_encoding(self, int_encoding): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_default_encoding(int encoding)
        
        /**
         * Specifies the default encoding to be used for all subsequently created
         * TextEncoder objects.  See set_encoding().
         */
        """
        pass

    def set_encoding(self, const_TextEncoder_self, int_encoding): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_encoding(const TextEncoder self, int encoding)
        
        /**
         * Specifies how the string set via set_text() is to be interpreted.  The
         * default, E_iso8859, means a standard string with one-byte characters (i.e.
         * ASCII).  Other encodings are possible to take advantage of character sets
         * with more than 256 characters.
         *
         * This affects only future calls to set_text(); it does not change text that
         * was set previously.
         */
        """
        pass

    def set_text(self, const_TextEncoder_self, object_text): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_text(const TextEncoder self, object text)
        set_text(const TextEncoder self, object text, int encoding)
        
        /**
         * Changes the text that is stored in the encoder.  The text should be encoded
         * according to the method indicated by set_encoding().  Subsequent calls to
         * get_text() will return this same string, while get_wtext() will return the
         * decoded version of the string.
         */
        
        /**
         * The two-parameter version of set_text() accepts an explicit encoding; the
         * text is immediately decoded and stored as a wide-character string.
         * Subsequent calls to get_text() will return the same text re-encoded using
         * whichever encoding is specified by set_encoding().
         */
        """
        pass

    def set_unicode_char(self, const_TextEncoder_self, int_index, int_character): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_unicode_char(const TextEncoder self, int index, int character)
        
        /**
         * Sets the Unicode value of the nth character in the stored text.  This may
         * be a wide character (greater than 255), after the string has been decoded
         * according to set_encoding().
         */
        """
        pass

    def set_wtext(self, const_TextEncoder_self, unicode_wtext): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_wtext(const TextEncoder self, unicode wtext)
        
        // Direct support for wide-character strings.  Now publishable with the new
        // wstring support in interrogate.
        
        /**
         * Changes the text that is stored in the encoder.  Subsequent calls to
         * get_wtext() will return this same string, while get_text() will return the
         * encoded version of the string.
         */
        """
        pass

    def unicodeIsalpha(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        unicode_isalpha(int character)
        
        /**
         * Returns true if the indicated character is an alphabetic letter, false
         * otherwise.  This is akin to ctype's isalpha(), extended to Unicode.
         */
        """
        pass

    def unicodeIsdigit(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        unicode_isdigit(int character)
        
        /**
         * Returns true if the indicated character is a numeric digit, false
         * otherwise.  This is akin to ctype's isdigit(), extended to Unicode.
         */
        """
        pass

    def unicodeIslower(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        unicode_islower(int character)
        
        /**
         * Returns true if the indicated character is a lowercase letter, false
         * otherwise.  This is akin to ctype's islower(), extended to Unicode.
         */
        """
        pass

    def unicodeIspunct(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        unicode_ispunct(int character)
        
        /**
         * Returns true if the indicated character is a punctuation mark, false
         * otherwise.  This is akin to ctype's ispunct(), extended to Unicode.
         */
        """
        pass

    def unicodeIsspace(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        unicode_isspace(int character)
        
        /**
         * Returns true if the indicated character is a whitespace letter, false
         * otherwise.  This is akin to ctype's isspace(), extended to Unicode.
         */
        """
        pass

    def unicodeIsupper(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        unicode_isupper(int character)
        
        /**
         * Returns true if the indicated character is an uppercase letter, false
         * otherwise.  This is akin to ctype's isupper(), extended to Unicode.
         */
        """
        pass

    def unicodeTolower(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        unicode_tolower(int character)
        
        /**
         * Returns the uppercase equivalent of the given Unicode character.  This is
         * akin to ctype's tolower(), extended to Unicode.
         */
        """
        pass

    def unicodeToupper(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        unicode_toupper(int character)
        
        /**
         * Returns the uppercase equivalent of the given Unicode character.  This is
         * akin to ctype's toupper(), extended to Unicode.
         */
        """
        pass

    def unicode_isalpha(self, int_character): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        unicode_isalpha(int character)
        
        /**
         * Returns true if the indicated character is an alphabetic letter, false
         * otherwise.  This is akin to ctype's isalpha(), extended to Unicode.
         */
        """
        pass

    def unicode_isdigit(self, int_character): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        unicode_isdigit(int character)
        
        /**
         * Returns true if the indicated character is a numeric digit, false
         * otherwise.  This is akin to ctype's isdigit(), extended to Unicode.
         */
        """
        pass

    def unicode_islower(self, int_character): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        unicode_islower(int character)
        
        /**
         * Returns true if the indicated character is a lowercase letter, false
         * otherwise.  This is akin to ctype's islower(), extended to Unicode.
         */
        """
        pass

    def unicode_ispunct(self, int_character): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        unicode_ispunct(int character)
        
        /**
         * Returns true if the indicated character is a punctuation mark, false
         * otherwise.  This is akin to ctype's ispunct(), extended to Unicode.
         */
        """
        pass

    def unicode_isspace(self, int_character): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        unicode_isspace(int character)
        
        /**
         * Returns true if the indicated character is a whitespace letter, false
         * otherwise.  This is akin to ctype's isspace(), extended to Unicode.
         */
        """
        pass

    def unicode_isupper(self, int_character): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        unicode_isupper(int character)
        
        /**
         * Returns true if the indicated character is an uppercase letter, false
         * otherwise.  This is akin to ctype's isupper(), extended to Unicode.
         */
        """
        pass

    def unicode_tolower(self, int_character): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        unicode_tolower(int character)
        
        /**
         * Returns the uppercase equivalent of the given Unicode character.  This is
         * akin to ctype's tolower(), extended to Unicode.
         */
        """
        pass

    def unicode_toupper(self, int_character): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        unicode_toupper(int character)
        
        /**
         * Returns the uppercase equivalent of the given Unicode character.  This is
         * akin to ctype's toupper(), extended to Unicode.
         */
        """
        pass

    def upper(self, str_source): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        upper(str source)
        upper(str source, int encoding)
        
        /**
         * Converts the string to uppercase, assuming the string is encoded in the
         * default encoding.
         */
        
        /**
         * Converts the string to uppercase, assuming the string is encoded in the
         * indicated encoding.
         */
        """
        pass

    def __copy__(self, *args, **kwargs): # real signature unknown
        pass

    def __deepcopy__(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    text = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    default_encoding = 1
    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        'EIso8859': 0,
        'EUnicode': 2,
        'EUtf16be': 2,
        'EUtf8': 1,
        'E_iso8859': 0,
        'E_unicode': 2,
        'E_utf16be': 2,
        'E_utf8': 1,
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.core.TextEncoder' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.core.TextEncoder' objects>"
        '__doc__': '/**\n * This class can be used to convert text between multiple representations,\n * e.g.  UTF-8 to UTF-16.  You may use it as a static class object, passing\n * the encoding each time, or you may create an instance and use that object,\n * which will record the current encoding and retain the current string.\n *\n * This class is also a base class of TextNode, which inherits this\n * functionality.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.TextEncoder' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE25B850>'
        'appendText': None, # (!) real value is "<method 'appendText' of 'panda3d.core.TextEncoder' objects>"
        'appendUnicodeChar': None, # (!) real value is "<method 'appendUnicodeChar' of 'panda3d.core.TextEncoder' objects>"
        'appendWtext': None, # (!) real value is "<method 'appendWtext' of 'panda3d.core.TextEncoder' objects>"
        'append_text': None, # (!) real value is "<method 'append_text' of 'panda3d.core.TextEncoder' objects>"
        'append_unicode_char': None, # (!) real value is "<method 'append_unicode_char' of 'panda3d.core.TextEncoder' objects>"
        'append_wtext': None, # (!) real value is "<method 'append_wtext' of 'panda3d.core.TextEncoder' objects>"
        'clearText': None, # (!) real value is "<method 'clearText' of 'panda3d.core.TextEncoder' objects>"
        'clear_text': None, # (!) real value is "<method 'clear_text' of 'panda3d.core.TextEncoder' objects>"
        'decodeText': None, # (!) real value is "<method 'decodeText' of 'panda3d.core.TextEncoder' objects>"
        'decode_text': None, # (!) real value is "<method 'decode_text' of 'panda3d.core.TextEncoder' objects>"
        'default_encoding': None, # (!) real value is "<attribute 'default_encoding' of 'panda3d.core.TextEncoder'>"
        'encodeWchar': None, # (!) real value is '<staticmethod(<built-in method encodeWchar of type object at 0x00007FFCFE25B850>)>'
        'encodeWtext': None, # (!) real value is "<method 'encodeWtext' of 'panda3d.core.TextEncoder' objects>"
        'encode_wchar': None, # (!) real value is '<staticmethod(<built-in method encode_wchar of type object at 0x00007FFCFE25B850>)>'
        'encode_wtext': None, # (!) real value is "<method 'encode_wtext' of 'panda3d.core.TextEncoder' objects>"
        'getDefaultEncoding': None, # (!) real value is '<staticmethod(<built-in method getDefaultEncoding of type object at 0x00007FFCFE25B850>)>'
        'getEncodedChar': None, # (!) real value is "<method 'getEncodedChar' of 'panda3d.core.TextEncoder' objects>"
        'getEncoding': None, # (!) real value is "<method 'getEncoding' of 'panda3d.core.TextEncoder' objects>"
        'getNumChars': None, # (!) real value is "<method 'getNumChars' of 'panda3d.core.TextEncoder' objects>"
        'getText': None, # (!) real value is "<method 'getText' of 'panda3d.core.TextEncoder' objects>"
        'getTextAsAscii': None, # (!) real value is "<method 'getTextAsAscii' of 'panda3d.core.TextEncoder' objects>"
        'getUnicodeChar': None, # (!) real value is "<method 'getUnicodeChar' of 'panda3d.core.TextEncoder' objects>"
        'getWtext': None, # (!) real value is "<method 'getWtext' of 'panda3d.core.TextEncoder' objects>"
        'getWtextAsAscii': None, # (!) real value is "<method 'getWtextAsAscii' of 'panda3d.core.TextEncoder' objects>"
        'get_default_encoding': None, # (!) real value is '<staticmethod(<built-in method get_default_encoding of type object at 0x00007FFCFE25B850>)>'
        'get_encoded_char': None, # (!) real value is "<method 'get_encoded_char' of 'panda3d.core.TextEncoder' objects>"
        'get_encoding': None, # (!) real value is "<method 'get_encoding' of 'panda3d.core.TextEncoder' objects>"
        'get_num_chars': None, # (!) real value is "<method 'get_num_chars' of 'panda3d.core.TextEncoder' objects>"
        'get_text': None, # (!) real value is "<method 'get_text' of 'panda3d.core.TextEncoder' objects>"
        'get_text_as_ascii': None, # (!) real value is "<method 'get_text_as_ascii' of 'panda3d.core.TextEncoder' objects>"
        'get_unicode_char': None, # (!) real value is "<method 'get_unicode_char' of 'panda3d.core.TextEncoder' objects>"
        'get_wtext': None, # (!) real value is "<method 'get_wtext' of 'panda3d.core.TextEncoder' objects>"
        'get_wtext_as_ascii': None, # (!) real value is "<method 'get_wtext_as_ascii' of 'panda3d.core.TextEncoder' objects>"
        'hasText': None, # (!) real value is "<method 'hasText' of 'panda3d.core.TextEncoder' objects>"
        'has_text': None, # (!) real value is "<method 'has_text' of 'panda3d.core.TextEncoder' objects>"
        'isWtext': None, # (!) real value is "<method 'isWtext' of 'panda3d.core.TextEncoder' objects>"
        'is_wtext': None, # (!) real value is "<method 'is_wtext' of 'panda3d.core.TextEncoder' objects>"
        'lower': None, # (!) real value is '<staticmethod(<built-in method lower of type object at 0x00007FFCFE25B850>)>'
        'makeLower': None, # (!) real value is "<method 'makeLower' of 'panda3d.core.TextEncoder' objects>"
        'makeUpper': None, # (!) real value is "<method 'makeUpper' of 'panda3d.core.TextEncoder' objects>"
        'make_lower': None, # (!) real value is "<method 'make_lower' of 'panda3d.core.TextEncoder' objects>"
        'make_upper': None, # (!) real value is "<method 'make_upper' of 'panda3d.core.TextEncoder' objects>"
        'reencodeText': None, # (!) real value is '<staticmethod(<built-in method reencodeText of type object at 0x00007FFCFE25B850>)>'
        'reencode_text': None, # (!) real value is '<staticmethod(<built-in method reencode_text of type object at 0x00007FFCFE25B850>)>'
        'setDefaultEncoding': None, # (!) real value is '<staticmethod(<built-in method setDefaultEncoding of type object at 0x00007FFCFE25B850>)>'
        'setEncoding': None, # (!) real value is "<method 'setEncoding' of 'panda3d.core.TextEncoder' objects>"
        'setText': None, # (!) real value is "<method 'setText' of 'panda3d.core.TextEncoder' objects>"
        'setUnicodeChar': None, # (!) real value is "<method 'setUnicodeChar' of 'panda3d.core.TextEncoder' objects>"
        'setWtext': None, # (!) real value is "<method 'setWtext' of 'panda3d.core.TextEncoder' objects>"
        'set_default_encoding': None, # (!) real value is '<staticmethod(<built-in method set_default_encoding of type object at 0x00007FFCFE25B850>)>'
        'set_encoding': None, # (!) real value is "<method 'set_encoding' of 'panda3d.core.TextEncoder' objects>"
        'set_text': None, # (!) real value is "<method 'set_text' of 'panda3d.core.TextEncoder' objects>"
        'set_unicode_char': None, # (!) real value is "<method 'set_unicode_char' of 'panda3d.core.TextEncoder' objects>"
        'set_wtext': None, # (!) real value is "<method 'set_wtext' of 'panda3d.core.TextEncoder' objects>"
        'text': None, # (!) real value is "<attribute 'text' of 'panda3d.core.TextEncoder' objects>"
        'unicodeIsalpha': None, # (!) real value is '<staticmethod(<built-in method unicodeIsalpha of type object at 0x00007FFCFE25B850>)>'
        'unicodeIsdigit': None, # (!) real value is '<staticmethod(<built-in method unicodeIsdigit of type object at 0x00007FFCFE25B850>)>'
        'unicodeIslower': None, # (!) real value is '<staticmethod(<built-in method unicodeIslower of type object at 0x00007FFCFE25B850>)>'
        'unicodeIspunct': None, # (!) real value is '<staticmethod(<built-in method unicodeIspunct of type object at 0x00007FFCFE25B850>)>'
        'unicodeIsspace': None, # (!) real value is '<staticmethod(<built-in method unicodeIsspace of type object at 0x00007FFCFE25B850>)>'
        'unicodeIsupper': None, # (!) real value is '<staticmethod(<built-in method unicodeIsupper of type object at 0x00007FFCFE25B850>)>'
        'unicodeTolower': None, # (!) real value is '<staticmethod(<built-in method unicodeTolower of type object at 0x00007FFCFE25B850>)>'
        'unicodeToupper': None, # (!) real value is '<staticmethod(<built-in method unicodeToupper of type object at 0x00007FFCFE25B850>)>'
        'unicode_isalpha': None, # (!) real value is '<staticmethod(<built-in method unicode_isalpha of type object at 0x00007FFCFE25B850>)>'
        'unicode_isdigit': None, # (!) real value is '<staticmethod(<built-in method unicode_isdigit of type object at 0x00007FFCFE25B850>)>'
        'unicode_islower': None, # (!) real value is '<staticmethod(<built-in method unicode_islower of type object at 0x00007FFCFE25B850>)>'
        'unicode_ispunct': None, # (!) real value is '<staticmethod(<built-in method unicode_ispunct of type object at 0x00007FFCFE25B850>)>'
        'unicode_isspace': None, # (!) real value is '<staticmethod(<built-in method unicode_isspace of type object at 0x00007FFCFE25B850>)>'
        'unicode_isupper': None, # (!) real value is '<staticmethod(<built-in method unicode_isupper of type object at 0x00007FFCFE25B850>)>'
        'unicode_tolower': None, # (!) real value is '<staticmethod(<built-in method unicode_tolower of type object at 0x00007FFCFE25B850>)>'
        'unicode_toupper': None, # (!) real value is '<staticmethod(<built-in method unicode_toupper of type object at 0x00007FFCFE25B850>)>'
        'upper': None, # (!) real value is '<staticmethod(<built-in method upper of type object at 0x00007FFCFE25B850>)>'
    }
    EIso8859 = 0
    EUnicode = 2
    EUtf16be = 2
    EUtf8 = 1
    E_iso8859 = 0
    E_unicode = 2
    E_utf16be = 2
    E_utf8 = 1


