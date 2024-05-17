# encoding: utf-8
# module PyQt5.QtCore
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtCore.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum
import sip as __sip


class QModelIndex(__sip.simplewrapper):
    """
    QModelIndex()
    QModelIndex(a0: QModelIndex)
    QModelIndex(a0: QPersistentModelIndex)
    """
    def child(self, arow, acolumn): # real signature unknown; restored from __doc__
        """ child(self, arow: int, acolumn: int) -> QModelIndex """
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

    def internalId(self): # real signature unknown; restored from __doc__
        """ internalId(self) -> int """
        return 0

    def internalPointer(self): # real signature unknown; restored from __doc__
        """ internalPointer(self) -> Any """
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

    def sibling(self, arow, acolumn): # real signature unknown; restored from __doc__
        """ sibling(self, arow: int, acolumn: int) -> QModelIndex """
        return QModelIndex

    def siblingAtColumn(self, column): # real signature unknown; restored from __doc__
        """ siblingAtColumn(self, column: int) -> QModelIndex """
        return QModelIndex

    def siblingAtRow(self, row): # real signature unknown; restored from __doc__
        """ siblingAtRow(self, row: int) -> QModelIndex """
        return QModelIndex

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

    def __init__(self, a0=None): # real signature unknown; restored from __doc__ with multiple overloads
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



