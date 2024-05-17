# encoding: utf-8
# module PyQt5.QtCore
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtCore.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum
import sip as __sip


class QMetaType(__sip.simplewrapper):
    """ QMetaType(type: int = QMetaType.Type.UnknownType) """
    def flags(self): # real signature unknown; restored from __doc__
        """ flags(self) -> QMetaType.TypeFlags """
        pass

    def id(self): # real signature unknown; restored from __doc__
        """ id(self) -> int """
        return 0

    def isRegistered(self, type=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        isRegistered(type: int) -> bool
        isRegistered(self) -> bool
        """
        return False

    def isValid(self): # real signature unknown; restored from __doc__
        """ isValid(self) -> bool """
        return False

    def metaObjectForType(self, type): # real signature unknown; restored from __doc__
        """ metaObjectForType(type: int) -> Optional[QMetaObject] """
        pass

    def name(self): # real signature unknown; restored from __doc__
        """ name(self) -> QByteArray """
        return QByteArray

    def type(self, typeName, p_str=None): # real signature unknown; restored from __doc__
        """ type(typeName: Optional[str]) -> int """
        return 0

    def typeFlags(self, type): # real signature unknown; restored from __doc__
        """ typeFlags(type: int) -> QMetaType.TypeFlags """
        pass

    def typeName(self, type): # real signature unknown; restored from __doc__
        """ typeName(type: int) -> Optional[str] """
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

    def __init__(self, type=None): # real signature unknown; restored from __doc__
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


    Bool = 1
    Char = 34
    Double = 6
    FirstGuiType = 64
    Float = 38
    Int = 2
    IsEnumeration = 16
    LastCoreType = 55
    Long = 32
    LongLong = 4
    MovableType = 4
    NeedsConstruction = 1
    NeedsDestruction = 2
    PointerToQObject = 8
    QBitArray = 13
    QBitmap = 73
    QBrush = 66
    QByteArray = 12
    QByteArrayList = 49
    QCborArray = 54
    QCborMap = 55
    QCborSimpleType = 52
    QCborValue = 53
    QChar = 7
    QColor = 67
    QColorSpace = 87
    QCursor = 74
    QDate = 14
    QDateTime = 16
    QEasingCurve = 29
    QFont = 64
    QIcon = 69
    QImage = 70
    QJsonArray = 47
    QJsonDocument = 48
    QJsonObject = 46
    QJsonValue = 45
    QKeySequence = 75
    QLine = 23
    QLineF = 24
    QLocale = 18
    QMatrix = 79
    QMatrix4x4 = 81
    QModelIndex = 42
    QObjectStar = 39
    QPalette = 68
    QPen = 76
    QPersistentModelIndex = 50
    QPixmap = 65
    QPoint = 25
    QPointF = 26
    QPolygon = 71
    QPolygonF = 86
    QQuaternion = 85
    QRect = 19
    QRectF = 20
    QRegExp = 27
    QRegion = 72
    QRegularExpression = 44
    QSize = 21
    QSizeF = 22
    QSizePolicy = 121
    QString = 10
    QStringList = 11
    QTextFormat = 78
    QTextLength = 77
    QTime = 15
    QTransform = 80
    QUrl = 17
    QUuid = 30
    QVariant = 41
    QVariantHash = 28
    QVariantList = 9
    QVariantMap = 8
    QVector2D = 82
    QVector3D = 83
    QVector4D = 84
    SChar = 40
    Short = 33
    UChar = 37
    UInt = 3
    ULong = 35
    ULongLong = 5
    UnknownType = 0
    User = 1024
    UShort = 36
    Void = 43
    VoidStar = 31
    __hash__ = None


