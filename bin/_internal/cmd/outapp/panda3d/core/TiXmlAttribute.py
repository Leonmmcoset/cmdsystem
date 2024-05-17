# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .TiXmlBase import TiXmlBase

class TiXmlAttribute(TiXmlBase):
    """
    /** An attribute is a name-value pair. Elements have an arbitrary
        number of attributes, each with a unique name.
    
        @note The attributes are not TiXmlNodes, since they are not
              part of the tinyXML document object model. There are other
              suggested ways to look at this problem.
    */
    """
    def DoubleValue(self, TiXmlAttribute_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        DoubleValue(TiXmlAttribute self)
        
        ///< Return the value of this attribute, converted to a double.
        """
        pass

    def IntValue(self, TiXmlAttribute_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        IntValue(TiXmlAttribute self)
        
        ///< Return the value of this attribute, converted to an integer.
        """
        pass

    def Name(self, TiXmlAttribute_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        Name(TiXmlAttribute self)
        
        ///< Return the name of this attribute.
        """
        pass

    def NameTStr(self, TiXmlAttribute_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        NameTStr(TiXmlAttribute self)
        
        // Get the tinyxml string representation
        """
        pass

    def Next(self, const_TiXmlAttribute_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        Next(const TiXmlAttribute self)
        Next(TiXmlAttribute self)
        
        /// Get the next sibling attribute in the DOM. Returns null at end.
        """
        pass

    def Previous(self, const_TiXmlAttribute_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        Previous(const TiXmlAttribute self)
        Previous(TiXmlAttribute self)
        
        /// Get the previous sibling attribute in the DOM. Returns null at beginning.
        """
        pass

    def SetDocument(self, const_TiXmlAttribute_self, TiXmlDocument_doc): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        SetDocument(const TiXmlAttribute self, TiXmlDocument doc)
        
        // [internal use]
        // Set the document pointer so the attribute can report errors.
        """
        pass

    def SetDoubleValue(self, const_TiXmlAttribute_self, double__value): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        SetDoubleValue(const TiXmlAttribute self, double _value)
        
        ///< Set the value from a double.
        """
        pass

    def SetIntValue(self, const_TiXmlAttribute_self, int__value): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        SetIntValue(const TiXmlAttribute self, int _value)
        
        ///< Set the value from an integer.
        """
        pass

    def SetName(self, const_TiXmlAttribute_self, str__name): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        SetName(const TiXmlAttribute self, str _name)
        SetName(const TiXmlAttribute self, str _name)
        
        ///< Set the name of this attribute.
        
        /// STL std::string form.
        """
        pass

    def SetValue(self, const_TiXmlAttribute_self, str__value): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        SetValue(const TiXmlAttribute self, str _value)
        SetValue(const TiXmlAttribute self, str _value)
        
        ///< Set the value.
        
        /// STL std::string form.
        """
        pass

    def Value(self, TiXmlAttribute_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        Value(TiXmlAttribute self)
        
        ///< Return the value of this attribute.
        """
        pass

    def ValueStr(self, TiXmlAttribute_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        ValueStr(TiXmlAttribute self)
        
        ///< Return the value of this attribute.
        """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __hash__(self, *args, **kwargs): # real signature unknown
        """ Return hash(self). """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    DtoolClassDict = {
        'DoubleValue': None, # (!) real value is "<method 'DoubleValue' of 'panda3d.core.TiXmlAttribute' objects>"
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        'IntValue': None, # (!) real value is "<method 'IntValue' of 'panda3d.core.TiXmlAttribute' objects>"
        'Name': None, # (!) real value is "<method 'Name' of 'panda3d.core.TiXmlAttribute' objects>"
        'NameTStr': None, # (!) real value is "<method 'NameTStr' of 'panda3d.core.TiXmlAttribute' objects>"
        'Next': None, # (!) real value is "<method 'Next' of 'panda3d.core.TiXmlAttribute' objects>"
        'Previous': None, # (!) real value is "<method 'Previous' of 'panda3d.core.TiXmlAttribute' objects>"
        'SetDocument': None, # (!) real value is "<method 'SetDocument' of 'panda3d.core.TiXmlAttribute' objects>"
        'SetDoubleValue': None, # (!) real value is "<method 'SetDoubleValue' of 'panda3d.core.TiXmlAttribute' objects>"
        'SetIntValue': None, # (!) real value is "<method 'SetIntValue' of 'panda3d.core.TiXmlAttribute' objects>"
        'SetName': None, # (!) real value is "<method 'SetName' of 'panda3d.core.TiXmlAttribute' objects>"
        'SetValue': None, # (!) real value is "<method 'SetValue' of 'panda3d.core.TiXmlAttribute' objects>"
        'Value': None, # (!) real value is "<method 'Value' of 'panda3d.core.TiXmlAttribute' objects>"
        'ValueStr': None, # (!) real value is "<method 'ValueStr' of 'panda3d.core.TiXmlAttribute' objects>"
        '__doc__': '/** An attribute is a name-value pair. Elements have an arbitrary\n    number of attributes, each with a unique name.\n\n    @note The attributes are not TiXmlNodes, since they are not\n          part of the tinyXML document object model. There are other\n          suggested ways to look at this problem.\n*/',
        '__eq__': None, # (!) real value is "<slot wrapper '__eq__' of 'panda3d.core.TiXmlAttribute' objects>"
        '__ge__': None, # (!) real value is "<slot wrapper '__ge__' of 'panda3d.core.TiXmlAttribute' objects>"
        '__gt__': None, # (!) real value is "<slot wrapper '__gt__' of 'panda3d.core.TiXmlAttribute' objects>"
        '__hash__': None, # (!) real value is "<slot wrapper '__hash__' of 'panda3d.core.TiXmlAttribute' objects>"
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.TiXmlAttribute' objects>"
        '__le__': None, # (!) real value is "<slot wrapper '__le__' of 'panda3d.core.TiXmlAttribute' objects>"
        '__lt__': None, # (!) real value is "<slot wrapper '__lt__' of 'panda3d.core.TiXmlAttribute' objects>"
        '__ne__': None, # (!) real value is "<slot wrapper '__ne__' of 'panda3d.core.TiXmlAttribute' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE3913A0>'
    }


