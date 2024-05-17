# encoding: utf-8
# module PyQt5.QtCore
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtCore.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum
import sip as __sip


class QMetaObject(__sip.simplewrapper):
    """
    QMetaObject()
    QMetaObject(a0: QMetaObject)
    """
    def checkConnectArgs(self, signal, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        checkConnectArgs(signal: Optional[str], method: Optional[str]) -> bool
        checkConnectArgs(signal: QMetaMethod, method: QMetaMethod) -> bool
        """
        return False

    def classInfo(self, index): # real signature unknown; restored from __doc__
        """ classInfo(self, index: int) -> QMetaClassInfo """
        return QMetaClassInfo

    def classInfoCount(self): # real signature unknown; restored from __doc__
        """ classInfoCount(self) -> int """
        return 0

    def classInfoOffset(self): # real signature unknown; restored from __doc__
        """ classInfoOffset(self) -> int """
        return 0

    def className(self): # real signature unknown; restored from __doc__
        """ className(self) -> Optional[str] """
        pass

    def connectSlotsByName(self, o, QObject=None): # real signature unknown; restored from __doc__
        """ connectSlotsByName(o: Optional[QObject]) """
        pass

    def constructor(self, index): # real signature unknown; restored from __doc__
        """ constructor(self, index: int) -> QMetaMethod """
        return QMetaMethod

    def constructorCount(self): # real signature unknown; restored from __doc__
        """ constructorCount(self) -> int """
        return 0

    def enumerator(self, index): # real signature unknown; restored from __doc__
        """ enumerator(self, index: int) -> QMetaEnum """
        return QMetaEnum

    def enumeratorCount(self): # real signature unknown; restored from __doc__
        """ enumeratorCount(self) -> int """
        return 0

    def enumeratorOffset(self): # real signature unknown; restored from __doc__
        """ enumeratorOffset(self) -> int """
        return 0

    def indexOfClassInfo(self, name, p_str=None): # real signature unknown; restored from __doc__
        """ indexOfClassInfo(self, name: Optional[str]) -> int """
        return 0

    def indexOfConstructor(self, constructor, p_str=None): # real signature unknown; restored from __doc__
        """ indexOfConstructor(self, constructor: Optional[str]) -> int """
        return 0

    def indexOfEnumerator(self, name, p_str=None): # real signature unknown; restored from __doc__
        """ indexOfEnumerator(self, name: Optional[str]) -> int """
        return 0

    def indexOfMethod(self, method, p_str=None): # real signature unknown; restored from __doc__
        """ indexOfMethod(self, method: Optional[str]) -> int """
        return 0

    def indexOfProperty(self, name, p_str=None): # real signature unknown; restored from __doc__
        """ indexOfProperty(self, name: Optional[str]) -> int """
        return 0

    def indexOfSignal(self, signal, p_str=None): # real signature unknown; restored from __doc__
        """ indexOfSignal(self, signal: Optional[str]) -> int """
        return 0

    def indexOfSlot(self, slot, p_str=None): # real signature unknown; restored from __doc__
        """ indexOfSlot(self, slot: Optional[str]) -> int """
        return 0

    def inherits(self, metaObject, QMetaObject=None): # real signature unknown; restored from __doc__
        """ inherits(self, metaObject: Optional[QMetaObject]) -> bool """
        return False

    def invokeMethod(self, obj, QObject=None, *args, **kwargs): # real signature unknown; restored from __doc__ with multiple overloads
        """
        invokeMethod(obj: Optional[QObject], member: Optional[str], type: Qt.ConnectionType, ret: QGenericReturnArgument, value0: QGenericArgument = QGenericArgument(0, 0), value1: QGenericArgument = QGenericArgument(0, 0), value2: QGenericArgument = QGenericArgument(0, 0), value3: QGenericArgument = QGenericArgument(0, 0), value4: QGenericArgument = QGenericArgument(0, 0), value5: QGenericArgument = QGenericArgument(0, 0), value6: QGenericArgument = QGenericArgument(0, 0), value7: QGenericArgument = QGenericArgument(0, 0), value8: QGenericArgument = QGenericArgument(0, 0), value9: QGenericArgument = QGenericArgument(0, 0)) -> Any
        invokeMethod(obj: Optional[QObject], member: Optional[str], ret: QGenericReturnArgument, value0: QGenericArgument = QGenericArgument(0, 0), value1: QGenericArgument = QGenericArgument(0, 0), value2: QGenericArgument = QGenericArgument(0, 0), value3: QGenericArgument = QGenericArgument(0, 0), value4: QGenericArgument = QGenericArgument(0, 0), value5: QGenericArgument = QGenericArgument(0, 0), value6: QGenericArgument = QGenericArgument(0, 0), value7: QGenericArgument = QGenericArgument(0, 0), value8: QGenericArgument = QGenericArgument(0, 0), value9: QGenericArgument = QGenericArgument(0, 0)) -> Any
        invokeMethod(obj: Optional[QObject], member: Optional[str], type: Qt.ConnectionType, value0: QGenericArgument = QGenericArgument(0, 0), value1: QGenericArgument = QGenericArgument(0, 0), value2: QGenericArgument = QGenericArgument(0, 0), value3: QGenericArgument = QGenericArgument(0, 0), value4: QGenericArgument = QGenericArgument(0, 0), value5: QGenericArgument = QGenericArgument(0, 0), value6: QGenericArgument = QGenericArgument(0, 0), value7: QGenericArgument = QGenericArgument(0, 0), value8: QGenericArgument = QGenericArgument(0, 0), value9: QGenericArgument = QGenericArgument(0, 0)) -> Any
        invokeMethod(obj: Optional[QObject], member: Optional[str], value0: QGenericArgument = QGenericArgument(0, 0), value1: QGenericArgument = QGenericArgument(0, 0), value2: QGenericArgument = QGenericArgument(0, 0), value3: QGenericArgument = QGenericArgument(0, 0), value4: QGenericArgument = QGenericArgument(0, 0), value5: QGenericArgument = QGenericArgument(0, 0), value6: QGenericArgument = QGenericArgument(0, 0), value7: QGenericArgument = QGenericArgument(0, 0), value8: QGenericArgument = QGenericArgument(0, 0), value9: QGenericArgument = QGenericArgument(0, 0)) -> Any
        """
        pass

    def method(self, index): # real signature unknown; restored from __doc__
        """ method(self, index: int) -> QMetaMethod """
        return QMetaMethod

    def methodCount(self): # real signature unknown; restored from __doc__
        """ methodCount(self) -> int """
        return 0

    def methodOffset(self): # real signature unknown; restored from __doc__
        """ methodOffset(self) -> int """
        return 0

    def normalizedSignature(self, method, p_str=None): # real signature unknown; restored from __doc__
        """ normalizedSignature(method: Optional[str]) -> QByteArray """
        return QByteArray

    def normalizedType(self, type, p_str=None): # real signature unknown; restored from __doc__
        """ normalizedType(type: Optional[str]) -> QByteArray """
        return QByteArray

    def property(self, index): # real signature unknown; restored from __doc__
        """ property(self, index: int) -> QMetaProperty """
        return QMetaProperty

    def propertyCount(self): # real signature unknown; restored from __doc__
        """ propertyCount(self) -> int """
        return 0

    def propertyOffset(self): # real signature unknown; restored from __doc__
        """ propertyOffset(self) -> int """
        return 0

    def superClass(self): # real signature unknown; restored from __doc__
        """ superClass(self) -> Optional[QMetaObject] """
        pass

    def userProperty(self): # real signature unknown; restored from __doc__
        """ userProperty(self) -> QMetaProperty """
        return QMetaProperty

    def __init__(self, a0=None): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""




