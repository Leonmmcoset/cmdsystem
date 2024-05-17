# encoding: utf-8
# module panda3d.direct
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\direct.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import panda3d.core as __panda3d_core


class DCKeywordList(__dtoolconfig.DTOOL_SUPER_BASE):
    """
    /**
     * This is a list of keywords (see DCKeyword) that may be set on a particular
     * field.
     */
    """
    def compareKeywords(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        compare_keywords(DCKeywordList self, const DCKeywordList other)
        
        /**
         * Returns true if this list has the same keywords as the other list, false if
         * some keywords differ.  Order is not considered important.
         */
        """
        pass

    def compare_keywords(self, DCKeywordList_self, const_DCKeywordList_other): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        compare_keywords(DCKeywordList self, const DCKeywordList other)
        
        /**
         * Returns true if this list has the same keywords as the other list, false if
         * some keywords differ.  Order is not considered important.
         */
        """
        pass

    def getKeyword(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_keyword(DCKeywordList self, int n)
        
        /**
         * Returns the nth keyword in the list.
         */
        """
        pass

    def getKeywordByName(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_keyword_by_name(DCKeywordList self, str name)
        
        /**
         * Returns the keyword in the list with the indicated name, or NULL if there
         * is no keyword in the list with that name.
         */
        """
        pass

    def getNumKeywords(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_keywords(DCKeywordList self)
        
        /**
         * Returns the number of keywords in the list.
         */
        """
        pass

    def get_keyword(self, DCKeywordList_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_keyword(DCKeywordList self, int n)
        
        /**
         * Returns the nth keyword in the list.
         */
        """
        pass

    def get_keyword_by_name(self, DCKeywordList_self, str_name): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_keyword_by_name(DCKeywordList self, str name)
        
        /**
         * Returns the keyword in the list with the indicated name, or NULL if there
         * is no keyword in the list with that name.
         */
        """
        pass

    def get_num_keywords(self, DCKeywordList_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_keywords(DCKeywordList self)
        
        /**
         * Returns the number of keywords in the list.
         */
        """
        pass

    def hasKeyword(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_keyword(DCKeywordList self, const DCKeyword keyword)
        has_keyword(DCKeywordList self, str name)
        
        /**
         * Returns true if this list includes the indicated keyword, false otherwise.
         */
        
        /**
         * Returns true if this list includes the indicated keyword, false otherwise.
         */
        """
        pass

    def has_keyword(self, DCKeywordList_self, const_DCKeyword_keyword): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_keyword(DCKeywordList self, const DCKeyword keyword)
        has_keyword(DCKeywordList self, str name)
        
        /**
         * Returns true if this list includes the indicated keyword, false otherwise.
         */
        
        /**
         * Returns true if this list includes the indicated keyword, false otherwise.
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
        '__doc__': '/**\n * This is a list of keywords (see DCKeyword) that may be set on a particular\n * field.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.direct.DCKeywordList' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFDC68DD950>'
        'compareKeywords': None, # (!) real value is "<method 'compareKeywords' of 'panda3d.direct.DCKeywordList' objects>"
        'compare_keywords': None, # (!) real value is "<method 'compare_keywords' of 'panda3d.direct.DCKeywordList' objects>"
        'getKeyword': None, # (!) real value is "<method 'getKeyword' of 'panda3d.direct.DCKeywordList' objects>"
        'getKeywordByName': None, # (!) real value is "<method 'getKeywordByName' of 'panda3d.direct.DCKeywordList' objects>"
        'getNumKeywords': None, # (!) real value is "<method 'getNumKeywords' of 'panda3d.direct.DCKeywordList' objects>"
        'get_keyword': None, # (!) real value is "<method 'get_keyword' of 'panda3d.direct.DCKeywordList' objects>"
        'get_keyword_by_name': None, # (!) real value is "<method 'get_keyword_by_name' of 'panda3d.direct.DCKeywordList' objects>"
        'get_num_keywords': None, # (!) real value is "<method 'get_num_keywords' of 'panda3d.direct.DCKeywordList' objects>"
        'hasKeyword': None, # (!) real value is "<method 'hasKeyword' of 'panda3d.direct.DCKeywordList' objects>"
        'has_keyword': None, # (!) real value is "<method 'has_keyword' of 'panda3d.direct.DCKeywordList' objects>"
    }


