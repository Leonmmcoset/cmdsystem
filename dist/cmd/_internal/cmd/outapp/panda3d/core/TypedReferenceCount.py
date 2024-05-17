# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .TypedObject import TypedObject

from .ReferenceCount import ReferenceCount

class TypedReferenceCount(TypedObject, ReferenceCount):
    """
    /**
     * A base class for things which need to inherit from both TypedObject and
     * from ReferenceCount.  It's convenient to define this intermediate base
     * class instead of multiply inheriting from the two classes each time they
     * are needed, so that we can sensibly pass around pointers to things which
     * are both TypedObjects and ReferenceCounters.
     *
     * See also TypedObject for detailed instructions.
     */
    """
    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def upcastToReferenceCount(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        upcast_to_ReferenceCount(const TypedReferenceCount self)
        
        upcast from TypedReferenceCount to ReferenceCount
        """
        pass

    def upcastToTypedObject(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        upcast_to_TypedObject(const TypedReferenceCount self)
        
        upcast from TypedReferenceCount to TypedObject
        """
        pass

    def upcast_to_ReferenceCount(self, const_TypedReferenceCount_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        upcast_to_ReferenceCount(const TypedReferenceCount self)
        
        upcast from TypedReferenceCount to ReferenceCount
        """
        pass

    def upcast_to_TypedObject(self, const_TypedReferenceCount_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        upcast_to_TypedObject(const TypedReferenceCount self)
        
        upcast from TypedReferenceCount to TypedObject
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
        '__doc__': "/**\n * A base class for things which need to inherit from both TypedObject and\n * from ReferenceCount.  It's convenient to define this intermediate base\n * class instead of multiply inheriting from the two classes each time they\n * are needed, so that we can sensibly pass around pointers to things which\n * are both TypedObjects and ReferenceCounters.\n *\n * See also TypedObject for detailed instructions.\n */",
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.TypedReferenceCount' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE278260>'
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE278260>)>'
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE278260>)>'
        'upcastToReferenceCount': None, # (!) real value is "<method 'upcastToReferenceCount' of 'panda3d.core.TypedReferenceCount' objects>"
        'upcastToTypedObject': None, # (!) real value is "<method 'upcastToTypedObject' of 'panda3d.core.TypedReferenceCount' objects>"
        'upcast_to_ReferenceCount': None, # (!) real value is "<method 'upcast_to_ReferenceCount' of 'panda3d.core.TypedReferenceCount' objects>"
        'upcast_to_TypedObject': None, # (!) real value is "<method 'upcast_to_TypedObject' of 'panda3d.core.TypedReferenceCount' objects>"
    }


