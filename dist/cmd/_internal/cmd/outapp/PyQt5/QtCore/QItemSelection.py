# encoding: utf-8
# module PyQt5.QtCore
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtCore.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum
import sip as __sip


class QItemSelection(__sip.simplewrapper):
    """
    QItemSelection()
    QItemSelection(topLeft: QModelIndex, bottomRight: QModelIndex)
    QItemSelection(a0: QItemSelection)
    """
    def append(self, range): # real signature unknown; restored from __doc__
        """ append(self, range: QItemSelectionRange) """
        pass

    def clear(self): # real signature unknown; restored from __doc__
        """ clear(self) """
        pass

    def contains(self, index): # real signature unknown; restored from __doc__
        """ contains(self, index: QModelIndex) -> bool """
        return False

    def count(self, range=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        count(self, range: QItemSelectionRange) -> int
        count(self) -> int
        """
        return 0

    def first(self): # real signature unknown; restored from __doc__
        """ first(self) -> QItemSelectionRange """
        return QItemSelectionRange

    def indexes(self): # real signature unknown; restored from __doc__
        """ indexes(self) -> List[QModelIndex] """
        return []

    def indexOf(self, value, from_=0): # real signature unknown; restored from __doc__
        """ indexOf(self, value: QItemSelectionRange, from_: int = 0) -> int """
        return 0

    def insert(self, i, range): # real signature unknown; restored from __doc__
        """ insert(self, i: int, range: QItemSelectionRange) """
        pass

    def isEmpty(self): # real signature unknown; restored from __doc__
        """ isEmpty(self) -> bool """
        return False

    def last(self): # real signature unknown; restored from __doc__
        """ last(self) -> QItemSelectionRange """
        return QItemSelectionRange

    def lastIndexOf(self, value, from_=-1): # real signature unknown; restored from __doc__
        """ lastIndexOf(self, value: QItemSelectionRange, from_: int = -1) -> int """
        return 0

    def merge(self, other, command, QItemSelectionModel_SelectionFlags=None, QItemSelectionModel_SelectionFlag=None): # real signature unknown; restored from __doc__
        """ merge(self, other: QItemSelection, command: Union[QItemSelectionModel.SelectionFlags, QItemSelectionModel.SelectionFlag]) """
        pass

    def move(self, from_, to): # real signature unknown; restored from __doc__
        """ move(self, from_: int, to: int) """
        pass

    def prepend(self, range): # real signature unknown; restored from __doc__
        """ prepend(self, range: QItemSelectionRange) """
        pass

    def removeAll(self, range): # real signature unknown; restored from __doc__
        """ removeAll(self, range: QItemSelectionRange) -> int """
        return 0

    def removeAt(self, i): # real signature unknown; restored from __doc__
        """ removeAt(self, i: int) """
        pass

    def replace(self, i, range): # real signature unknown; restored from __doc__
        """ replace(self, i: int, range: QItemSelectionRange) """
        pass

    def select(self, topLeft, bottomRight): # real signature unknown; restored from __doc__
        """ select(self, topLeft: QModelIndex, bottomRight: QModelIndex) """
        pass

    def split(self, range, other, result, QItemSelection=None): # real signature unknown; restored from __doc__
        """ split(range: QItemSelectionRange, other: QItemSelectionRange, result: Optional[QItemSelection]) """
        pass

    def swap(self, i, j): # real signature unknown; restored from __doc__
        """ swap(self, i: int, j: int) """
        pass

    def takeAt(self, i): # real signature unknown; restored from __doc__
        """ takeAt(self, i: int) -> QItemSelectionRange """
        return QItemSelectionRange

    def takeFirst(self): # real signature unknown; restored from __doc__
        """ takeFirst(self) -> QItemSelectionRange """
        return QItemSelectionRange

    def takeLast(self): # real signature unknown; restored from __doc__
        """ takeLast(self) -> QItemSelectionRange """
        return QItemSelectionRange

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

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
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


