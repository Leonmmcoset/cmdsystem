# encoding: utf-8
# module PyQt5.QtCore
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtCore.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum
import sip as __sip


class QPersistentModelIndex(__sip.simplewrapper):
    """
    QPersistentModelIndex()
    QPersistentModelIndex(index: QModelIndex)
    QPersistentModelIndex(other: QPersistentModelIndex)
    """
    def child(self, row, column): # real signature unknown; restored from __doc__
        """ child(self, row: int, column: int) -> QModelIndex """
        return QModelIndex

    def column(self): # real signature unknown; restored from __doc__
        """ column(self) -> int """
        return 0

    def data(self, role=None): # real signature unknown; restored from __doc__
        """ data(self, role: int = Qt.ItemDataRole.DisplayRole) -> Any """
        pass

    def flags(self): # real signature unknown; restored from __doc__
        """ flags(self) -> Qt.ItemFlags """
        pass

    def isValid(self): # real signature unknown; restored from __doc__
        """ isValid(self) -> bool """
        return False

    def model(self): # real signature unknown; restored from __doc__
        """ model(self) -> Optional[QAbstractItemModel] """
        pass

    def parent(self): # real signature unknown; restored from __doc__
        """ parent(self) -> QModelIndex """
        return QModelIndex

    def row(self): # real signature unknown; restored from __doc__
        """ row(self) -> int """
        return 0

    def sibling(self, row, column): # real signature unknown; restored from __doc__
        """ sibling(self, row: int, column: int) -> QModelIndex """
        return QModelIndex

    def swap(self, other): # real signature unknown; restored from __doc__
        """ swap(self, other: QPersistentModelIndex) """
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

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
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

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



