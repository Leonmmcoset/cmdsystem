# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .PointerToBase_Connection import PointerToBase_Connection

class PointerTo_Connection(PointerToBase_Connection):
    # no doc
    def assign(self, const_PointerTo_self, const_Connection_copy): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        assign(const PointerTo self, const Connection copy)
        assign(const PointerTo self, Connection ptr)
        """
        pass

    def clear(self, const_PointerTo_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear(const PointerTo self)
        """
        pass

    def isNull(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_null(PointerTo self)
        """
        pass

    def is_null(self, PointerTo_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_null(PointerTo self)
        """
        pass

    def p(self, PointerTo_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        p(PointerTo self)
        
        // If your base class is a derivative of TypedObject, you might want to use
        // the DCAST macro defined in typedObject.h instead, e.g.  DCAST(MyType,
        // ptr).  This provides a clean downcast that doesn't require .p() or any
        // double-casting, and it can be run-time checked for correctness.
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
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.core.PointerTo_Connection' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.core.PointerTo_Connection' objects>"
        '__doc__': None,
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.PointerTo_Connection' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE389370>'
        'assign': None, # (!) real value is "<method 'assign' of 'panda3d.core.PointerTo_Connection' objects>"
        'clear': None, # (!) real value is "<method 'clear' of 'panda3d.core.PointerTo_Connection' objects>"
        'isNull': None, # (!) real value is "<method 'isNull' of 'panda3d.core.PointerTo_Connection' objects>"
        'is_null': None, # (!) real value is "<method 'is_null' of 'panda3d.core.PointerTo_Connection' objects>"
        'p': None, # (!) real value is "<method 'p' of 'panda3d.core.PointerTo_Connection' objects>"
    }


