# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


class TiXmlAttributeSet(__dtoolconfig.DTOOL_SUPER_BASE):
    """
    /*  A class used to manage a group of attributes.
        It is only used internally, both by the ELEMENT and the DECLARATION.
    
        The set can be changed transparent to the Element and Declaration
        classes that use it, but NOT transparent to the Attribute
        which has to implement a next() and previous() method. Which makes
        it a bit problematic and prevents the use of STL.
    
        This version is implemented with circular lists because:
            - I like circular lists
            - it demonstrates some independence from the (typical) doubly linked list.
    */
    """
    def Add(self, const_TiXmlAttributeSet_self, TiXmlAttribute_attribute): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        Add(const TiXmlAttributeSet self, TiXmlAttribute attribute)
        """
        pass

    def Find(self, TiXmlAttributeSet_self, str__name): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        Find(TiXmlAttributeSet self, str _name)
        Find(TiXmlAttributeSet self, str _name)
        """
        pass

    def FindOrCreate(self, const_TiXmlAttributeSet_self, str__name): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        FindOrCreate(const TiXmlAttributeSet self, str _name)
        FindOrCreate(const TiXmlAttributeSet self, str _name)
        """
        pass

    def First(self, const_TiXmlAttributeSet_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        First(const TiXmlAttributeSet self)
        First(TiXmlAttributeSet self)
        """
        pass

    def Last(self, const_TiXmlAttributeSet_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        Last(const TiXmlAttributeSet self)
        Last(TiXmlAttributeSet self)
        """
        pass

    def Remove(self, const_TiXmlAttributeSet_self, TiXmlAttribute_attribute): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        Remove(const TiXmlAttributeSet self, TiXmlAttribute attribute)
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    DtoolClassDict = {
        'Add': None, # (!) real value is "<method 'Add' of 'panda3d.core.TiXmlAttributeSet' objects>"
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        'Find': None, # (!) real value is "<method 'Find' of 'panda3d.core.TiXmlAttributeSet' objects>"
        'FindOrCreate': None, # (!) real value is "<method 'FindOrCreate' of 'panda3d.core.TiXmlAttributeSet' objects>"
        'First': None, # (!) real value is "<method 'First' of 'panda3d.core.TiXmlAttributeSet' objects>"
        'Last': None, # (!) real value is "<method 'Last' of 'panda3d.core.TiXmlAttributeSet' objects>"
        'Remove': None, # (!) real value is "<method 'Remove' of 'panda3d.core.TiXmlAttributeSet' objects>"
        '__doc__': '/*  A class used to manage a group of attributes.\n    It is only used internally, both by the ELEMENT and the DECLARATION.\n\n    The set can be changed transparent to the Element and Declaration\n    classes that use it, but NOT transparent to the Attribute\n    which has to implement a next() and previous() method. Which makes\n    it a bit problematic and prevents the use of STL.\n\n    This version is implemented with circular lists because:\n        - I like circular lists\n        - it demonstrates some independence from the (typical) doubly linked list.\n*/',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.TiXmlAttributeSet' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE391570>'
    }


