# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .TiXmlNode import TiXmlNode

class TiXmlElement(TiXmlNode):
    """
    /** The element is a container class. It has a value, the element name,
        and can contain other elements, text, comments, and unknowns.
        Elements also contain an arbitrary number of attributes.
    */
    """
    def assign(self, const_TiXmlElement_self, const_TiXmlElement_base): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        assign(const TiXmlElement self, const TiXmlElement base)
        """
        pass

    def Attribute(self, TiXmlElement_self, str_name): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        Attribute(TiXmlElement self, str name)
        Attribute(TiXmlElement self, str name)
        
        /** Given an attribute name, Attribute() returns the value
                for the attribute of that name, or null if none exists.
            */
        
        /** Given an attribute name, Attribute() returns the value
                for the attribute of that name, or null if none exists.
                If the attribute exists and can be converted to an integer,
                the integer value will be put in the return 'i', if 'i'
                is non-null.
            */
        
        /** Given an attribute name, Attribute() returns the value
                for the attribute of that name, or null if none exists.
                If the attribute exists and can be converted to an double,
                the double value will be put in the return 'd', if 'd'
                is non-null.
            */
        """
        pass

    def FirstAttribute(self, const_TiXmlElement_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        FirstAttribute(const TiXmlElement self)
        FirstAttribute(TiXmlElement self)
        
        ///< Access the first attribute in this element.
        
        ///< Access the first attribute in this element.
        """
        pass

    def GetText(self, TiXmlElement_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        GetText(TiXmlElement self)
        
        /** Convenience function for easy access to the text inside an element. Although easy
                and concise, GetText() is limited compared to getting the TiXmlText child
                and accessing it directly.
        
                If the first child of 'this' is a TiXmlText, the GetText()
                returns the character string of the Text node, else null is returned.
        
                This is a convenient method for getting the text of simple contained text:
                @verbatim
                <foo>This is text</foo>
                const char* str = fooElement->GetText();
                @endverbatim
        
                'str' will be a pointer to "This is text".
        
                Note that this function can be misleading. If the element foo was created from
                this XML:
                @verbatim
                <foo><b>This is text</b></foo>
                @endverbatim
        
                then the value of str would be null. The first child node isn't a text node, it is
                another element. From this XML:
                @verbatim
                <foo>This is <b>text</b></foo>
                @endverbatim
                GetText() will return "This is ".
        
                WARNING: GetText() accesses a child node - don't become confused with the
                         similarly named TiXmlHandle::Text() and TiXmlNode::ToText() which are
                         safe type casts on the referenced node.
            */
        """
        pass

    def LastAttribute(self, const_TiXmlElement_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        LastAttribute(const TiXmlElement self)
        LastAttribute(TiXmlElement self)
        
        ///< Access the last attribute in this element.
        
        ///< Access the last attribute in this element.
        """
        pass

    def RemoveAttribute(self, const_TiXmlElement_self, str_name): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        RemoveAttribute(const TiXmlElement self, str name)
        RemoveAttribute(const TiXmlElement self, str name)
        
        /** Deletes an attribute with the given name.
            */
        
        ///< STL std::string form.
        """
        pass

    def SetAttribute(self, const_TiXmlElement_self, str_name, str__value): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        SetAttribute(const TiXmlElement self, str name, str _value)
        SetAttribute(const TiXmlElement self, str name, int _value)
        SetAttribute(const TiXmlElement self, str name, str _value)
        SetAttribute(const TiXmlElement self, str name, int value)
        
        /** Sets an attribute of name to a given value. The attribute
                will be created if it does not exist, or changed if it does.
            */
        
        /// STL std::string form.
        
        ///< STL std::string form.
        
        /** Sets an attribute of name to a given value. The attribute
                will be created if it does not exist, or changed if it does.
            */
        """
        pass

    def SetDoubleAttribute(self, const_TiXmlElement_self, str_name, double_value): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        SetDoubleAttribute(const TiXmlElement self, str name, double value)
        SetDoubleAttribute(const TiXmlElement self, str name, double value)
        
        ///< STL std::string form.
        
        /** Sets an attribute of name to a given value. The attribute
                will be created if it does not exist, or changed if it does.
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

    DtoolClassDict = {
        'Attribute': None, # (!) real value is "<method 'Attribute' of 'panda3d.core.TiXmlElement' objects>"
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        'FirstAttribute': None, # (!) real value is "<method 'FirstAttribute' of 'panda3d.core.TiXmlElement' objects>"
        'GetText': None, # (!) real value is "<method 'GetText' of 'panda3d.core.TiXmlElement' objects>"
        'LastAttribute': None, # (!) real value is "<method 'LastAttribute' of 'panda3d.core.TiXmlElement' objects>"
        'RemoveAttribute': None, # (!) real value is "<method 'RemoveAttribute' of 'panda3d.core.TiXmlElement' objects>"
        'SetAttribute': None, # (!) real value is "<method 'SetAttribute' of 'panda3d.core.TiXmlElement' objects>"
        'SetDoubleAttribute': None, # (!) real value is "<method 'SetDoubleAttribute' of 'panda3d.core.TiXmlElement' objects>"
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.core.TiXmlElement' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.core.TiXmlElement' objects>"
        '__doc__': '/** The element is a container class. It has a value, the element name,\n    and can contain other elements, text, comments, and unknowns.\n    Elements also contain an arbitrary number of attributes.\n*/',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.TiXmlElement' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE390E30>'
        'assign': None, # (!) real value is "<method 'assign' of 'panda3d.core.TiXmlElement' objects>"
    }


