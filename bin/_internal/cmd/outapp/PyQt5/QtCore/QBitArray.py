# encoding: utf-8
# module PyQt5.QtCore
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtCore.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum
import sip as __sip


class QBitArray(__sip.simplewrapper):
    """
    QBitArray()
    QBitArray(size: int, value: bool = False)
    QBitArray(other: QBitArray)
    """
    def at(self, i): # real signature unknown; restored from __doc__
        """ at(self, i: int) -> bool """
        return False

    def bits(self): # real signature unknown; restored from __doc__
        """ bits(self) -> bytes """
        return b""

    def clear(self): # real signature unknown; restored from __doc__
        """ clear(self) """
        pass

    def clearBit(self, i): # real signature unknown; restored from __doc__
        """ clearBit(self, i: int) """
        pass

    def count(self, on=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        count(self) -> int
        count(self, on: bool) -> int
        """
        return 0

    def detach(self): # real signature unknown; restored from __doc__
        """ detach(self) """
        pass

    def fill(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        fill(self, val: bool, first: int, last: int)
        fill(self, value: bool, size: int = -1) -> bool
        """
        return False

    def fromBits(self, data, bytes=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ fromBits(data: Optional[bytes], len: int) -> QBitArray """
        pass

    def isDetached(self): # real signature unknown; restored from __doc__
        """ isDetached(self) -> bool """
        return False

    def isEmpty(self): # real signature unknown; restored from __doc__
        """ isEmpty(self) -> bool """
        return False

    def isNull(self): # real signature unknown; restored from __doc__
        """ isNull(self) -> bool """
        return False

    def resize(self, size): # real signature unknown; restored from __doc__
        """ resize(self, size: int) """
        pass

    def setBit(self, i, val=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setBit(self, i: int)
        setBit(self, i: int, val: bool)
        """
        pass

    def size(self): # real signature unknown; restored from __doc__
        """ size(self) -> int """
        return 0

    def swap(self, other): # real signature unknown; restored from __doc__
        """ swap(self, other: QBitArray) """
        pass

    def testBit(self, i): # real signature unknown; restored from __doc__
        """ testBit(self, i: int) -> bool """
        return False

    def toggleBit(self, i): # real signature unknown; restored from __doc__
        """ toggleBit(self, i: int) -> bool """
        return False

    def truncate(self, pos): # real signature unknown; restored from __doc__
        """ truncate(self, pos: int) """
        pass

    def __and__(self, *args, **kwargs): # real signature unknown
        """ Return self&value. """
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

    def __hash__(self, *args, **kwargs): # real signature unknown
        """ Return hash(self). """
        pass

    def __iand__(self, *args, **kwargs): # real signature unknown
        """ Return self&=value. """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    def __invert__(self, *args, **kwargs): # real signature unknown
        """ ~self """
        pass

    def __ior__(self, *args, **kwargs): # real signature unknown
        """ Return self|=value. """
        pass

    def __ixor__(self, *args, **kwargs): # real signature unknown
        """ Return self^=value. """
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

    def __or__(self, *args, **kwargs): # real signature unknown
        """ Return self|value. """
        pass

    def __rand__(self, *args, **kwargs): # real signature unknown
        """ Return value&self. """
        pass

    def __ror__(self, *args, **kwargs): # real signature unknown
        """ Return value|self. """
        pass

    def __rxor__(self, *args, **kwargs): # real signature unknown
        """ Return value^self. """
        pass

    def __xor__(self, *args, **kwargs): # real signature unknown
        """ Return self^value. """
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



