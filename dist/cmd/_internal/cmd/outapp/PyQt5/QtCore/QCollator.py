# encoding: utf-8
# module PyQt5.QtCore
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtCore.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum
import sip as __sip


class QCollator(__sip.simplewrapper):
    """
    QCollator(locale: QLocale = QLocale())
    QCollator(a0: QCollator)
    """
    def caseSensitivity(self): # real signature unknown; restored from __doc__
        """ caseSensitivity(self) -> Qt.CaseSensitivity """
        pass

    def compare(self, s1, p_str=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ compare(self, s1: Optional[str], s2: Optional[str]) -> int """
        pass

    def ignorePunctuation(self): # real signature unknown; restored from __doc__
        """ ignorePunctuation(self) -> bool """
        return False

    def locale(self): # real signature unknown; restored from __doc__
        """ locale(self) -> QLocale """
        return QLocale

    def numericMode(self): # real signature unknown; restored from __doc__
        """ numericMode(self) -> bool """
        return False

    def setCaseSensitivity(self, cs): # real signature unknown; restored from __doc__
        """ setCaseSensitivity(self, cs: Qt.CaseSensitivity) """
        pass

    def setIgnorePunctuation(self, on): # real signature unknown; restored from __doc__
        """ setIgnorePunctuation(self, on: bool) """
        pass

    def setLocale(self, locale): # real signature unknown; restored from __doc__
        """ setLocale(self, locale: QLocale) """
        pass

    def setNumericMode(self, on): # real signature unknown; restored from __doc__
        """ setNumericMode(self, on: bool) """
        pass

    def sortKey(self, string, p_str=None): # real signature unknown; restored from __doc__
        """ sortKey(self, string: Optional[str]) -> QCollatorSortKey """
        return QCollatorSortKey

    def swap(self, other): # real signature unknown; restored from __doc__
        """ swap(self, other: QCollator) """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



