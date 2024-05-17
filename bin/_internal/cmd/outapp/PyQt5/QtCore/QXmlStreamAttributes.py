# encoding: utf-8
# module PyQt5.QtCore
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtCore.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum
import sip as __sip


class QXmlStreamAttributes(__sip.simplewrapper):
    """
    QXmlStreamAttributes()
    QXmlStreamAttributes(a0: QXmlStreamAttributes)
    """
    def append(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        append(self, namespaceUri: Optional[str], name: Optional[str], value: Optional[str])
        append(self, qualifiedName: Optional[str], value: Optional[str])
        append(self, attribute: QXmlStreamAttribute)
        """
        pass

    def at(self, i): # real signature unknown; restored from __doc__
        """ at(self, i: int) -> QXmlStreamAttribute """
        return QXmlStreamAttribute

    def clear(self): # real signature unknown; restored from __doc__
        """ clear(self) """
        pass

    def contains(self, value): # real signature unknown; restored from __doc__
        """ contains(self, value: QXmlStreamAttribute) -> bool """
        return False

    def count(self, value=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        count(self, value: QXmlStreamAttribute) -> int
        count(self) -> int
        """
        return 0

    def data(self): # real signature unknown; restored from __doc__
        """ data(self) -> Optional[PyQt5.sip.voidptr] """
        pass

    def fill(self, value, size=-1): # real signature unknown; restored from __doc__
        """ fill(self, value: QXmlStreamAttribute, size: int = -1) """
        pass

    def first(self): # real signature unknown; restored from __doc__
        """ first(self) -> QXmlStreamAttribute """
        return QXmlStreamAttribute

    def hasAttribute(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        hasAttribute(self, qualifiedName: Optional[str]) -> bool
        hasAttribute(self, namespaceUri: Optional[str], name: Optional[str]) -> bool
        """
        return False

    def indexOf(self, value, from_=0): # real signature unknown; restored from __doc__
        """ indexOf(self, value: QXmlStreamAttribute, from_: int = 0) -> int """
        return 0

    def insert(self, i, value): # real signature unknown; restored from __doc__
        """ insert(self, i: int, value: QXmlStreamAttribute) """
        pass

    def isEmpty(self): # real signature unknown; restored from __doc__
        """ isEmpty(self) -> bool """
        return False

    def last(self): # real signature unknown; restored from __doc__
        """ last(self) -> QXmlStreamAttribute """
        return QXmlStreamAttribute

    def lastIndexOf(self, value, from_=-1): # real signature unknown; restored from __doc__
        """ lastIndexOf(self, value: QXmlStreamAttribute, from_: int = -1) -> int """
        return 0

    def prepend(self, value): # real signature unknown; restored from __doc__
        """ prepend(self, value: QXmlStreamAttribute) """
        pass

    def remove(self, i, count=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        remove(self, i: int)
        remove(self, i: int, count: int)
        """
        pass

    def replace(self, i, value): # real signature unknown; restored from __doc__
        """ replace(self, i: int, value: QXmlStreamAttribute) """
        pass

    def size(self): # real signature unknown; restored from __doc__
        """ size(self) -> int """
        return 0

    def value(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        value(self, namespaceUri: Optional[str], name: Optional[str]) -> str
        value(self, qualifiedName: Optional[str]) -> str
        """
        return ""

    def __contains__(self, *args, **kwargs): # real signature unknown
        """ Return key in self. """
        pass

    def __delitem__(self, *args, **kwargs): # real signature unknown
        """ Delete self[key]. """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __getitem__(self, *args, **kwargs): # real signature unknown
        """ Return self[key]. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __iadd__(self, *args, **kwargs): # real signature unknown
        """ Implement self+=value. """
        pass

    def __init__(self, a0=None): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    def __len__(self, *args, **kwargs): # real signature unknown
        """ Return len(self). """
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __setitem__(self, *args, **kwargs): # real signature unknown
        """ Set self[key] to value. """
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __hash__ = None


