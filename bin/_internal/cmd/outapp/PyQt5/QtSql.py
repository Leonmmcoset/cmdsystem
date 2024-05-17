# encoding: utf-8
# module PyQt5.QtSql
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtSql.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import PyQt5.QtWidgets as __PyQt5_QtWidgets
import sip as __sip


# no functions
# classes

class QSql(__sip.simplewrapper):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    AfterLastRow = -2
    AllTables = 255
    BeforeFirstRow = -1
    Binary = 4
    HighPrecision = 0
    In = 1
    InOut = 3
    LowPrecisionDouble = 4
    LowPrecisionInt32 = 1
    LowPrecisionInt64 = 2
    Out = 2
    SystemTables = 2
    Tables = 1
    Views = 4


class QSqlDatabase(__sip.simplewrapper):
    """
    QSqlDatabase()
    QSqlDatabase(other: QSqlDatabase)
    QSqlDatabase(type: Optional[str])
    QSqlDatabase(driver: Optional[QSqlDriver])
    """
    def addDatabase(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        addDatabase(type: Optional[str], connectionName: Optional[str] = '') -> QSqlDatabase
        addDatabase(driver: Optional[QSqlDriver], connectionName: Optional[str] = '') -> QSqlDatabase
        """
        pass

    def cloneDatabase(self, other, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        cloneDatabase(other: QSqlDatabase, connectionName: Optional[str]) -> QSqlDatabase
        cloneDatabase(other: Optional[str], connectionName: Optional[str]) -> QSqlDatabase
        """
        return QSqlDatabase

    def close(self): # real signature unknown; restored from __doc__
        """ close(self) """
        pass

    def commit(self): # real signature unknown; restored from __doc__
        """ commit(self) -> bool """
        return False

    def connectionName(self): # real signature unknown; restored from __doc__
        """ connectionName(self) -> str """
        return ""

    def connectionNames(self): # real signature unknown; restored from __doc__
        """ connectionNames() -> List[str] """
        return []

    def connectOptions(self): # real signature unknown; restored from __doc__
        """ connectOptions(self) -> str """
        return ""

    def contains(self, connectionName, p_str=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ contains(connectionName: Optional[str] = '') -> bool """
        pass

    def database(self, connectionName, p_str=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ database(connectionName: Optional[str] = '', open: bool = True) -> QSqlDatabase """
        pass

    def databaseName(self): # real signature unknown; restored from __doc__
        """ databaseName(self) -> str """
        return ""

    def driver(self): # real signature unknown; restored from __doc__
        """ driver(self) -> Optional[QSqlDriver] """
        pass

    def driverName(self): # real signature unknown; restored from __doc__
        """ driverName(self) -> str """
        return ""

    def drivers(self): # real signature unknown; restored from __doc__
        """ drivers() -> List[str] """
        return []

    def exec(self, query, p_str=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ exec(self, query: Optional[str] = '') -> QSqlQuery """
        pass

    def exec_(self, query, p_str=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ exec_(self, query: Optional[str] = '') -> QSqlQuery """
        pass

    def hostName(self): # real signature unknown; restored from __doc__
        """ hostName(self) -> str """
        return ""

    def isDriverAvailable(self, name, p_str=None): # real signature unknown; restored from __doc__
        """ isDriverAvailable(name: Optional[str]) -> bool """
        return False

    def isOpen(self): # real signature unknown; restored from __doc__
        """ isOpen(self) -> bool """
        return False

    def isOpenError(self): # real signature unknown; restored from __doc__
        """ isOpenError(self) -> bool """
        return False

    def isValid(self): # real signature unknown; restored from __doc__
        """ isValid(self) -> bool """
        return False

    def lastError(self): # real signature unknown; restored from __doc__
        """ lastError(self) -> QSqlError """
        return QSqlError

    def numericalPrecisionPolicy(self): # real signature unknown; restored from __doc__
        """ numericalPrecisionPolicy(self) -> QSql.NumericalPrecisionPolicy """
        pass

    def open(self, user=None, p_str=None, *args=None, **kwargs=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        open(self) -> bool
        open(self, user: Optional[str], password: Optional[str]) -> bool
        """
        return False

    def password(self): # real signature unknown; restored from __doc__
        """ password(self) -> str """
        return ""

    def port(self): # real signature unknown; restored from __doc__
        """ port(self) -> int """
        return 0

    def primaryIndex(self, tablename, p_str=None): # real signature unknown; restored from __doc__
        """ primaryIndex(self, tablename: Optional[str]) -> QSqlIndex """
        return QSqlIndex

    def record(self, tablename, p_str=None): # real signature unknown; restored from __doc__
        """ record(self, tablename: Optional[str]) -> QSqlRecord """
        return QSqlRecord

    def registerSqlDriver(self, name, p_str=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ registerSqlDriver(name: Optional[str], creator: Optional[QSqlDriverCreatorBase]) """
        pass

    def removeDatabase(self, connectionName, p_str=None): # real signature unknown; restored from __doc__
        """ removeDatabase(connectionName: Optional[str]) """
        pass

    def rollback(self): # real signature unknown; restored from __doc__
        """ rollback(self) -> bool """
        return False

    def setConnectOptions(self, options, p_str=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ setConnectOptions(self, options: Optional[str] = '') """
        pass

    def setDatabaseName(self, name, p_str=None): # real signature unknown; restored from __doc__
        """ setDatabaseName(self, name: Optional[str]) """
        pass

    def setHostName(self, host, p_str=None): # real signature unknown; restored from __doc__
        """ setHostName(self, host: Optional[str]) """
        pass

    def setNumericalPrecisionPolicy(self, precisionPolicy): # real signature unknown; restored from __doc__
        """ setNumericalPrecisionPolicy(self, precisionPolicy: QSql.NumericalPrecisionPolicy) """
        pass

    def setPassword(self, password, p_str=None): # real signature unknown; restored from __doc__
        """ setPassword(self, password: Optional[str]) """
        pass

    def setPort(self, p): # real signature unknown; restored from __doc__
        """ setPort(self, p: int) """
        pass

    def setUserName(self, name, p_str=None): # real signature unknown; restored from __doc__
        """ setUserName(self, name: Optional[str]) """
        pass

    def tables(self, type=None): # real signature unknown; restored from __doc__
        """ tables(self, type: QSql.TableType = QSql.Tables) -> List[str] """
        return []

    def transaction(self): # real signature unknown; restored from __doc__
        """ transaction(self) -> bool """
        return False

    def userName(self): # real signature unknown; restored from __doc__
        """ userName(self) -> str """
        return ""

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class QSqlDriver(__PyQt5_QtCore.QObject):
    """ QSqlDriver(parent: Optional[QObject] = None) """
    def beginTransaction(self): # real signature unknown; restored from __doc__
        """ beginTransaction(self) -> bool """
        return False

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def close(self): # real signature unknown; restored from __doc__
        """ close(self) """
        pass

    def commitTransaction(self): # real signature unknown; restored from __doc__
        """ commitTransaction(self) -> bool """
        return False

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def createResult(self): # real signature unknown; restored from __doc__
        """ createResult(self) -> Optional[QSqlResult] """
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def dbmsType(self): # real signature unknown; restored from __doc__
        """ dbmsType(self) -> QSqlDriver.DbmsType """
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def escapeIdentifier(self, identifier, p_str=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ escapeIdentifier(self, identifier: Optional[str], type: QSqlDriver.IdentifierType) -> str """
        pass

    def formatValue(self, field, trimStrings=False): # real signature unknown; restored from __doc__
        """ formatValue(self, field: QSqlField, trimStrings: bool = False) -> str """
        return ""

    def handle(self): # real signature unknown; restored from __doc__
        """ handle(self) -> Any """
        pass

    def hasFeature(self, f): # real signature unknown; restored from __doc__
        """ hasFeature(self, f: QSqlDriver.DriverFeature) -> bool """
        return False

    def isIdentifierEscaped(self, identifier, p_str=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ isIdentifierEscaped(self, identifier: Optional[str], type: QSqlDriver.IdentifierType) -> bool """
        pass

    def isOpen(self): # real signature unknown; restored from __doc__
        """ isOpen(self) -> bool """
        return False

    def isOpenError(self): # real signature unknown; restored from __doc__
        """ isOpenError(self) -> bool """
        return False

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def lastError(self): # real signature unknown; restored from __doc__
        """ lastError(self) -> QSqlError """
        return QSqlError

    def notification(self, *args, **kwargs): # real signature unknown
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
        pass

    def numericalPrecisionPolicy(self): # real signature unknown; restored from __doc__
        """ numericalPrecisionPolicy(self) -> QSql.NumericalPrecisionPolicy """
        pass

    def open(self, db, p_str=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ open(self, db: Optional[str], user: Optional[str] = '', password: Optional[str] = '', host: Optional[str] = '', port: int = -1, options: Optional[str] = '') -> bool """
        pass

    def primaryIndex(self, tableName, p_str=None): # real signature unknown; restored from __doc__
        """ primaryIndex(self, tableName: Optional[str]) -> QSqlIndex """
        return QSqlIndex

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def record(self, tableName, p_str=None): # real signature unknown; restored from __doc__
        """ record(self, tableName: Optional[str]) -> QSqlRecord """
        return QSqlRecord

    def rollbackTransaction(self): # real signature unknown; restored from __doc__
        """ rollbackTransaction(self) -> bool """
        return False

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setLastError(self, e): # real signature unknown; restored from __doc__
        """ setLastError(self, e: QSqlError) """
        pass

    def setNumericalPrecisionPolicy(self, precisionPolicy): # real signature unknown; restored from __doc__
        """ setNumericalPrecisionPolicy(self, precisionPolicy: QSql.NumericalPrecisionPolicy) """
        pass

    def setOpen(self, o): # real signature unknown; restored from __doc__
        """ setOpen(self, o: bool) """
        pass

    def setOpenError(self, e): # real signature unknown; restored from __doc__
        """ setOpenError(self, e: bool) """
        pass

    def sqlStatement(self, type, tableName, p_str=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ sqlStatement(self, type: QSqlDriver.StatementType, tableName: Optional[str], rec: QSqlRecord, preparedStatement: bool) -> str """
        pass

    def stripDelimiters(self, identifier, p_str=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ stripDelimiters(self, identifier: Optional[str], type: QSqlDriver.IdentifierType) -> str """
        pass

    def subscribedToNotifications(self): # real signature unknown; restored from __doc__
        """ subscribedToNotifications(self) -> List[str] """
        return []

    def subscribeToNotification(self, name, p_str=None): # real signature unknown; restored from __doc__
        """ subscribeToNotification(self, name: Optional[str]) -> bool """
        return False

    def tables(self, tableType): # real signature unknown; restored from __doc__
        """ tables(self, tableType: QSql.TableType) -> List[str] """
        return []

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def unsubscribeFromNotification(self, name, p_str=None): # real signature unknown; restored from __doc__
        """ unsubscribeFromNotification(self, name: Optional[str]) -> bool """
        return False

    def __init__(self, parent, QObject=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    BatchOperations = 8
    BLOB = 2
    DB2 = 8
    DeleteStatement = 4
    EventNotifications = 11
    FieldName = 0
    FinishQuery = 12
    InsertStatement = 3
    Interbase = 7
    LastInsertId = 7
    LowPrecisionNumbers = 10
    MSSqlServer = 1
    MultipleResultSets = 13
    MySqlServer = 2
    NamedPlaceholders = 5
    Oracle = 4
    OtherSource = 2
    PositionalPlaceholders = 6
    PostgreSQL = 3
    PreparedQueries = 4
    QuerySize = 1
    SelectStatement = 1
    SelfSource = 1
    SimpleLocking = 9
    SQLite = 6
    Sybase = 5
    TableName = 1
    Transactions = 0
    Unicode = 3
    UnknownDbms = 0
    UnknownSource = 0
    UpdateStatement = 2
    WhereStatement = 0


class QSqlDriverCreatorBase(__sip.wrapper):
    """
    QSqlDriverCreatorBase()
    QSqlDriverCreatorBase(a0: QSqlDriverCreatorBase)
    """
    def createObject(self): # real signature unknown; restored from __doc__
        """ createObject(self) -> Optional[QSqlDriver] """
        pass

    def __init__(self, a0=None): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class QSqlError(__sip.simplewrapper):
    """
    QSqlError(driverText: Optional[str] = '', databaseText: Optional[str] = '', type: QSqlError.ErrorType = QSqlError.NoError, errorCode: Optional[str] = '')
    QSqlError(driverText: Optional[str], databaseText: Optional[str], type: QSqlError.ErrorType, number: int)
    QSqlError(other: QSqlError)
    """
    def databaseText(self): # real signature unknown; restored from __doc__
        """ databaseText(self) -> str """
        return ""

    def driverText(self): # real signature unknown; restored from __doc__
        """ driverText(self) -> str """
        return ""

    def isValid(self): # real signature unknown; restored from __doc__
        """ isValid(self) -> bool """
        return False

    def nativeErrorCode(self): # real signature unknown; restored from __doc__
        """ nativeErrorCode(self) -> str """
        return ""

    def number(self): # real signature unknown; restored from __doc__
        """ number(self) -> int """
        return 0

    def setDatabaseText(self, databaseText, p_str=None): # real signature unknown; restored from __doc__
        """ setDatabaseText(self, databaseText: Optional[str]) """
        pass

    def setDriverText(self, driverText, p_str=None): # real signature unknown; restored from __doc__
        """ setDriverText(self, driverText: Optional[str]) """
        pass

    def setNumber(self, number): # real signature unknown; restored from __doc__
        """ setNumber(self, number: int) """
        pass

    def setType(self, type): # real signature unknown; restored from __doc__
        """ setType(self, type: QSqlError.ErrorType) """
        pass

    def swap(self, other): # real signature unknown; restored from __doc__
        """ swap(self, other: QSqlError) """
        pass

    def text(self): # real signature unknown; restored from __doc__
        """ text(self) -> str """
        return ""

    def type(self): # real signature unknown; restored from __doc__
        """ type(self) -> QSqlError.ErrorType """
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


    ConnectionError = 1
    NoError = 0
    StatementError = 2
    TransactionError = 3
    UnknownError = 4
    __hash__ = None


class QSqlField(__sip.simplewrapper):
    """
    QSqlField(fieldName: Optional[str] = '', type: QVariant.Type = QVariant.Invalid)
    QSqlField(fieldName: Optional[str], type: QVariant.Type, tableName: Optional[str])
    QSqlField(other: QSqlField)
    """
    def clear(self): # real signature unknown; restored from __doc__
        """ clear(self) """
        pass

    def defaultValue(self): # real signature unknown; restored from __doc__
        """ defaultValue(self) -> Any """
        pass

    def isAutoValue(self): # real signature unknown; restored from __doc__
        """ isAutoValue(self) -> bool """
        return False

    def isGenerated(self): # real signature unknown; restored from __doc__
        """ isGenerated(self) -> bool """
        return False

    def isNull(self): # real signature unknown; restored from __doc__
        """ isNull(self) -> bool """
        return False

    def isReadOnly(self): # real signature unknown; restored from __doc__
        """ isReadOnly(self) -> bool """
        return False

    def isValid(self): # real signature unknown; restored from __doc__
        """ isValid(self) -> bool """
        return False

    def length(self): # real signature unknown; restored from __doc__
        """ length(self) -> int """
        return 0

    def name(self): # real signature unknown; restored from __doc__
        """ name(self) -> str """
        return ""

    def precision(self): # real signature unknown; restored from __doc__
        """ precision(self) -> int """
        return 0

    def requiredStatus(self): # real signature unknown; restored from __doc__
        """ requiredStatus(self) -> QSqlField.RequiredStatus """
        pass

    def setAutoValue(self, autoVal): # real signature unknown; restored from __doc__
        """ setAutoValue(self, autoVal: bool) """
        pass

    def setDefaultValue(self, value): # real signature unknown; restored from __doc__
        """ setDefaultValue(self, value: Any) """
        pass

    def setGenerated(self, gen): # real signature unknown; restored from __doc__
        """ setGenerated(self, gen: bool) """
        pass

    def setLength(self, fieldLength): # real signature unknown; restored from __doc__
        """ setLength(self, fieldLength: int) """
        pass

    def setName(self, name, p_str=None): # real signature unknown; restored from __doc__
        """ setName(self, name: Optional[str]) """
        pass

    def setPrecision(self, precision): # real signature unknown; restored from __doc__
        """ setPrecision(self, precision: int) """
        pass

    def setReadOnly(self, readOnly): # real signature unknown; restored from __doc__
        """ setReadOnly(self, readOnly: bool) """
        pass

    def setRequired(self, required): # real signature unknown; restored from __doc__
        """ setRequired(self, required: bool) """
        pass

    def setRequiredStatus(self, status): # real signature unknown; restored from __doc__
        """ setRequiredStatus(self, status: QSqlField.RequiredStatus) """
        pass

    def setSqlType(self, type): # real signature unknown; restored from __doc__
        """ setSqlType(self, type: int) """
        pass

    def setTableName(self, tableName, p_str=None): # real signature unknown; restored from __doc__
        """ setTableName(self, tableName: Optional[str]) """
        pass

    def setType(self, type): # real signature unknown; restored from __doc__
        """ setType(self, type: QVariant.Type) """
        pass

    def setValue(self, value): # real signature unknown; restored from __doc__
        """ setValue(self, value: Any) """
        pass

    def tableName(self): # real signature unknown; restored from __doc__
        """ tableName(self) -> str """
        return ""

    def type(self): # real signature unknown; restored from __doc__
        """ type(self) -> QVariant.Type """
        pass

    def typeID(self): # real signature unknown; restored from __doc__
        """ typeID(self) -> int """
        return 0

    def value(self): # real signature unknown; restored from __doc__
        """ value(self) -> Any """
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


    Optional = 0
    Required = 1
    Unknown = -1
    __hash__ = None


class QSqlRecord(__sip.simplewrapper):
    """
    QSqlRecord()
    QSqlRecord(other: QSqlRecord)
    """
    def append(self, field): # real signature unknown; restored from __doc__
        """ append(self, field: QSqlField) """
        pass

    def clear(self): # real signature unknown; restored from __doc__
        """ clear(self) """
        pass

    def clearValues(self): # real signature unknown; restored from __doc__
        """ clearValues(self) """
        pass

    def contains(self, name, p_str=None): # real signature unknown; restored from __doc__
        """ contains(self, name: Optional[str]) -> bool """
        return False

    def count(self): # real signature unknown; restored from __doc__
        """ count(self) -> int """
        return 0

    def field(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        field(self, i: int) -> QSqlField
        field(self, name: Optional[str]) -> QSqlField
        """
        return QSqlField

    def fieldName(self, i): # real signature unknown; restored from __doc__
        """ fieldName(self, i: int) -> str """
        return ""

    def indexOf(self, name, p_str=None): # real signature unknown; restored from __doc__
        """ indexOf(self, name: Optional[str]) -> int """
        return 0

    def insert(self, pos, field): # real signature unknown; restored from __doc__
        """ insert(self, pos: int, field: QSqlField) """
        pass

    def isEmpty(self): # real signature unknown; restored from __doc__
        """ isEmpty(self) -> bool """
        return False

    def isGenerated(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        isGenerated(self, i: int) -> bool
        isGenerated(self, name: Optional[str]) -> bool
        """
        return False

    def isNull(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        isNull(self, i: int) -> bool
        isNull(self, name: Optional[str]) -> bool
        """
        return False

    def keyValues(self, keyFields): # real signature unknown; restored from __doc__
        """ keyValues(self, keyFields: QSqlRecord) -> QSqlRecord """
        return QSqlRecord

    def remove(self, pos): # real signature unknown; restored from __doc__
        """ remove(self, pos: int) """
        pass

    def replace(self, pos, field): # real signature unknown; restored from __doc__
        """ replace(self, pos: int, field: QSqlField) """
        pass

    def setGenerated(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setGenerated(self, name: Optional[str], generated: bool)
        setGenerated(self, i: int, generated: bool)
        """
        pass

    def setNull(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setNull(self, i: int)
        setNull(self, name: Optional[str])
        """
        pass

    def setValue(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setValue(self, i: int, val: Any)
        setValue(self, name: Optional[str], val: Any)
        """
        pass

    def value(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        value(self, i: int) -> Any
        value(self, name: Optional[str]) -> Any
        """
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

    def __init__(self, other=None): # real signature unknown; restored from __doc__ with multiple overloads
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

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __hash__ = None


class QSqlIndex(QSqlRecord):
    """
    QSqlIndex(cursorName: Optional[str] = '', name: Optional[str] = '')
    QSqlIndex(other: QSqlIndex)
    """
    def append(self, field, desc=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        append(self, field: QSqlField)
        append(self, field: QSqlField, desc: bool)
        """
        pass

    def cursorName(self): # real signature unknown; restored from __doc__
        """ cursorName(self) -> str """
        return ""

    def isDescending(self, i): # real signature unknown; restored from __doc__
        """ isDescending(self, i: int) -> bool """
        return False

    def name(self): # real signature unknown; restored from __doc__
        """ name(self) -> str """
        return ""

    def setCursorName(self, cursorName, p_str=None): # real signature unknown; restored from __doc__
        """ setCursorName(self, cursorName: Optional[str]) """
        pass

    def setDescending(self, i, desc): # real signature unknown; restored from __doc__
        """ setDescending(self, i: int, desc: bool) """
        pass

    def setName(self, name, p_str=None): # real signature unknown; restored from __doc__
        """ setName(self, name: Optional[str]) """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass


class QSqlQuery(__sip.simplewrapper):
    """
    QSqlQuery(r: Optional[QSqlResult])
    QSqlQuery(query: Optional[str] = '', db: QSqlDatabase = QSqlDatabase())
    QSqlQuery(db: QSqlDatabase)
    QSqlQuery(other: QSqlQuery)
    """
    def addBindValue(self, val, type, QSql_ParamType=None, QSql_ParamTypeFlag=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ addBindValue(self, val: Any, type: Union[QSql.ParamType, QSql.ParamTypeFlag] = QSql.In) """
        pass

    def at(self): # real signature unknown; restored from __doc__
        """ at(self) -> int """
        return 0

    def bindValue(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        bindValue(self, placeholder: Optional[str], val: Any, type: Union[QSql.ParamType, QSql.ParamTypeFlag] = QSql.In)
        bindValue(self, pos: int, val: Any, type: Union[QSql.ParamType, QSql.ParamTypeFlag] = QSql.In)
        """
        pass

    def boundValue(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        boundValue(self, placeholder: Optional[str]) -> Any
        boundValue(self, pos: int) -> Any
        """
        pass

    def boundValues(self): # real signature unknown; restored from __doc__
        """ boundValues(self) -> Dict[str, Any] """
        return {}

    def clear(self): # real signature unknown; restored from __doc__
        """ clear(self) """
        pass

    def driver(self): # real signature unknown; restored from __doc__
        """ driver(self) -> Optional[QSqlDriver] """
        pass

    def exec(self, query=None, p_str=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        exec(self, query: Optional[str]) -> bool
        exec(self) -> bool
        """
        return False

    def execBatch(self, mode=None): # real signature unknown; restored from __doc__
        """ execBatch(self, mode: QSqlQuery.BatchExecutionMode = QSqlQuery.ValuesAsRows) -> bool """
        return False

    def executedQuery(self): # real signature unknown; restored from __doc__
        """ executedQuery(self) -> str """
        return ""

    def exec_(self, query=None, p_str=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        exec_(self, query: Optional[str]) -> bool
        exec_(self) -> bool
        """
        return False

    def finish(self): # real signature unknown; restored from __doc__
        """ finish(self) """
        pass

    def first(self): # real signature unknown; restored from __doc__
        """ first(self) -> bool """
        return False

    def isActive(self): # real signature unknown; restored from __doc__
        """ isActive(self) -> bool """
        return False

    def isForwardOnly(self): # real signature unknown; restored from __doc__
        """ isForwardOnly(self) -> bool """
        return False

    def isNull(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        isNull(self, field: int) -> bool
        isNull(self, name: Optional[str]) -> bool
        """
        return False

    def isSelect(self): # real signature unknown; restored from __doc__
        """ isSelect(self) -> bool """
        return False

    def isValid(self): # real signature unknown; restored from __doc__
        """ isValid(self) -> bool """
        return False

    def last(self): # real signature unknown; restored from __doc__
        """ last(self) -> bool """
        return False

    def lastError(self): # real signature unknown; restored from __doc__
        """ lastError(self) -> QSqlError """
        return QSqlError

    def lastInsertId(self): # real signature unknown; restored from __doc__
        """ lastInsertId(self) -> Any """
        pass

    def lastQuery(self): # real signature unknown; restored from __doc__
        """ lastQuery(self) -> str """
        return ""

    def next(self): # real signature unknown; restored from __doc__
        """ next(self) -> bool """
        return False

    def nextResult(self): # real signature unknown; restored from __doc__
        """ nextResult(self) -> bool """
        return False

    def numericalPrecisionPolicy(self): # real signature unknown; restored from __doc__
        """ numericalPrecisionPolicy(self) -> QSql.NumericalPrecisionPolicy """
        pass

    def numRowsAffected(self): # real signature unknown; restored from __doc__
        """ numRowsAffected(self) -> int """
        return 0

    def prepare(self, query, p_str=None): # real signature unknown; restored from __doc__
        """ prepare(self, query: Optional[str]) -> bool """
        return False

    def previous(self): # real signature unknown; restored from __doc__
        """ previous(self) -> bool """
        return False

    def record(self): # real signature unknown; restored from __doc__
        """ record(self) -> QSqlRecord """
        return QSqlRecord

    def result(self): # real signature unknown; restored from __doc__
        """ result(self) -> Optional[QSqlResult] """
        pass

    def seek(self, index, relative=False): # real signature unknown; restored from __doc__
        """ seek(self, index: int, relative: bool = False) -> bool """
        return False

    def setForwardOnly(self, forward): # real signature unknown; restored from __doc__
        """ setForwardOnly(self, forward: bool) """
        pass

    def setNumericalPrecisionPolicy(self, precisionPolicy): # real signature unknown; restored from __doc__
        """ setNumericalPrecisionPolicy(self, precisionPolicy: QSql.NumericalPrecisionPolicy) """
        pass

    def size(self): # real signature unknown; restored from __doc__
        """ size(self) -> int """
        return 0

    def value(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        value(self, i: int) -> Any
        value(self, name: Optional[str]) -> Any
        """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    ValuesAsColumns = 1
    ValuesAsRows = 0


class QSqlQueryModel(__PyQt5_QtCore.QAbstractTableModel):
    """ QSqlQueryModel(parent: Optional[QObject] = None) """
    def beginInsertColumns(self, parent, first, last): # real signature unknown; restored from __doc__
        """ beginInsertColumns(self, parent: QModelIndex, first: int, last: int) """
        pass

    def beginInsertRows(self, parent, first, last): # real signature unknown; restored from __doc__
        """ beginInsertRows(self, parent: QModelIndex, first: int, last: int) """
        pass

    def beginMoveColumns(self, *args, **kwargs): # real signature unknown
        pass

    def beginMoveRows(self, *args, **kwargs): # real signature unknown
        pass

    def beginRemoveColumns(self, parent, first, last): # real signature unknown; restored from __doc__
        """ beginRemoveColumns(self, parent: QModelIndex, first: int, last: int) """
        pass

    def beginRemoveRows(self, parent, first, last): # real signature unknown; restored from __doc__
        """ beginRemoveRows(self, parent: QModelIndex, first: int, last: int) """
        pass

    def beginResetModel(self): # real signature unknown; restored from __doc__
        """ beginResetModel(self) """
        pass

    def canFetchMore(self, parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ canFetchMore(self, parent: QModelIndex = QModelIndex()) -> bool """
        pass

    def changePersistentIndex(self, *args, **kwargs): # real signature unknown
        pass

    def changePersistentIndexList(self, *args, **kwargs): # real signature unknown
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def clear(self): # real signature unknown; restored from __doc__
        """ clear(self) """
        pass

    def columnCount(self, parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ columnCount(self, parent: QModelIndex = QModelIndex()) -> int """
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def createIndex(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def data(self, item, role=None): # real signature unknown; restored from __doc__
        """ data(self, item: QModelIndex, role: int = Qt.DisplayRole) -> Any """
        pass

    def decodeData(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def encodeData(self, *args, **kwargs): # real signature unknown
        pass

    def endInsertColumns(self): # real signature unknown; restored from __doc__
        """ endInsertColumns(self) """
        pass

    def endInsertRows(self): # real signature unknown; restored from __doc__
        """ endInsertRows(self) """
        pass

    def endMoveColumns(self, *args, **kwargs): # real signature unknown
        pass

    def endMoveRows(self, *args, **kwargs): # real signature unknown
        pass

    def endRemoveColumns(self): # real signature unknown; restored from __doc__
        """ endRemoveColumns(self) """
        pass

    def endRemoveRows(self): # real signature unknown; restored from __doc__
        """ endRemoveRows(self) """
        pass

    def endResetModel(self): # real signature unknown; restored from __doc__
        """ endResetModel(self) """
        pass

    def fetchMore(self, parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ fetchMore(self, parent: QModelIndex = QModelIndex()) """
        pass

    def headerData(self, section, orientation, role=None): # real signature unknown; restored from __doc__
        """ headerData(self, section: int, orientation: Qt.Orientation, role: int = Qt.DisplayRole) -> Any """
        pass

    def indexInQuery(self, item): # real signature unknown; restored from __doc__
        """ indexInQuery(self, item: QModelIndex) -> QModelIndex """
        pass

    def insertColumns(self, column, count, parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ insertColumns(self, column: int, count: int, parent: QModelIndex = QModelIndex()) -> bool """
        pass

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def lastError(self): # real signature unknown; restored from __doc__
        """ lastError(self) -> QSqlError """
        return QSqlError

    def persistentIndexList(self, *args, **kwargs): # real signature unknown
        pass

    def query(self): # real signature unknown; restored from __doc__
        """ query(self) -> QSqlQuery """
        return QSqlQuery

    def queryChange(self): # real signature unknown; restored from __doc__
        """ queryChange(self) """
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def record(self, row=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        record(self, row: int) -> QSqlRecord
        record(self) -> QSqlRecord
        """
        return QSqlRecord

    def removeColumns(self, column, count, parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ removeColumns(self, column: int, count: int, parent: QModelIndex = QModelIndex()) -> bool """
        pass

    def resetInternalData(self, *args, **kwargs): # real signature unknown
        pass

    def roleNames(self): # real signature unknown; restored from __doc__
        """ roleNames(self) -> Dict[int, QByteArray] """
        return {}

    def rowCount(self, parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ rowCount(self, parent: QModelIndex = QModelIndex()) -> int """
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setHeaderData(self, section, orientation, value, role=None): # real signature unknown; restored from __doc__
        """ setHeaderData(self, section: int, orientation: Qt.Orientation, value: Any, role: int = Qt.EditRole) -> bool """
        return False

    def setLastError(self, error): # real signature unknown; restored from __doc__
        """ setLastError(self, error: QSqlError) """
        pass

    def setQuery(self, query, p_str=None, *args=None, **kwargs=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setQuery(self, query: QSqlQuery)
        setQuery(self, query: Optional[str], db: QSqlDatabase = QSqlDatabase())
        """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, parent, QObject=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass


class QSqlRelation(__sip.simplewrapper):
    """
    QSqlRelation()
    QSqlRelation(aTableName: Optional[str], indexCol: Optional[str], displayCol: Optional[str])
    QSqlRelation(a0: QSqlRelation)
    """
    def displayColumn(self): # real signature unknown; restored from __doc__
        """ displayColumn(self) -> str """
        return ""

    def indexColumn(self): # real signature unknown; restored from __doc__
        """ indexColumn(self) -> str """
        return ""

    def isValid(self): # real signature unknown; restored from __doc__
        """ isValid(self) -> bool """
        return False

    def swap(self, other): # real signature unknown; restored from __doc__
        """ swap(self, other: QSqlRelation) """
        pass

    def tableName(self): # real signature unknown; restored from __doc__
        """ tableName(self) -> str """
        return ""

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class QSqlRelationalDelegate(__PyQt5_QtWidgets.QItemDelegate):
    """ QSqlRelationalDelegate(parent: Optional[QObject] = None) """
    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def createEditor(self, parent, QWidget=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ createEditor(self, parent: Optional[QWidget], option: QStyleOptionViewItem, index: QModelIndex) -> Optional[QWidget] """
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def drawBackground(self, *args, **kwargs): # real signature unknown
        pass

    def drawCheck(self, *args, **kwargs): # real signature unknown
        pass

    def drawDecoration(self, *args, **kwargs): # real signature unknown
        pass

    def drawDisplay(self, *args, **kwargs): # real signature unknown
        pass

    def drawFocus(self, *args, **kwargs): # real signature unknown
        pass

    def editorEvent(self, *args, **kwargs): # real signature unknown
        pass

    def eventFilter(self, *args, **kwargs): # real signature unknown
        pass

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setEditorData(self, editor, QWidget=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ setEditorData(self, editor: Optional[QWidget], index: QModelIndex) """
        pass

    def setModelData(self, editor, QWidget=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ setModelData(self, editor: Optional[QWidget], model: Optional[QAbstractItemModel], index: QModelIndex) """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, parent, QObject=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass


class QSqlTableModel(QSqlQueryModel):
    """ QSqlTableModel(parent: Optional[QObject] = None, db: QSqlDatabase = QSqlDatabase()) """
    def beforeDelete(self, *args, **kwargs): # real signature unknown
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
        pass

    def beforeInsert(self, *args, **kwargs): # real signature unknown
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
        pass

    def beforeUpdate(self, *args, **kwargs): # real signature unknown
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
        pass

    def beginInsertColumns(self, *args, **kwargs): # real signature unknown
        pass

    def beginInsertRows(self, *args, **kwargs): # real signature unknown
        pass

    def beginMoveColumns(self, *args, **kwargs): # real signature unknown
        pass

    def beginMoveRows(self, *args, **kwargs): # real signature unknown
        pass

    def beginRemoveColumns(self, *args, **kwargs): # real signature unknown
        pass

    def beginRemoveRows(self, *args, **kwargs): # real signature unknown
        pass

    def beginResetModel(self, *args, **kwargs): # real signature unknown
        pass

    def changePersistentIndex(self, *args, **kwargs): # real signature unknown
        pass

    def changePersistentIndexList(self, *args, **kwargs): # real signature unknown
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def clear(self): # real signature unknown; restored from __doc__
        """ clear(self) """
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def createIndex(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def data(self, idx, role=None): # real signature unknown; restored from __doc__
        """ data(self, idx: QModelIndex, role: int = Qt.ItemDataRole.DisplayRole) -> Any """
        pass

    def database(self): # real signature unknown; restored from __doc__
        """ database(self) -> QSqlDatabase """
        return QSqlDatabase

    def decodeData(self, *args, **kwargs): # real signature unknown
        pass

    def deleteRowFromTable(self, row): # real signature unknown; restored from __doc__
        """ deleteRowFromTable(self, row: int) -> bool """
        return False

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def editStrategy(self): # real signature unknown; restored from __doc__
        """ editStrategy(self) -> QSqlTableModel.EditStrategy """
        pass

    def encodeData(self, *args, **kwargs): # real signature unknown
        pass

    def endInsertColumns(self, *args, **kwargs): # real signature unknown
        pass

    def endInsertRows(self, *args, **kwargs): # real signature unknown
        pass

    def endMoveColumns(self, *args, **kwargs): # real signature unknown
        pass

    def endMoveRows(self, *args, **kwargs): # real signature unknown
        pass

    def endRemoveColumns(self, *args, **kwargs): # real signature unknown
        pass

    def endRemoveRows(self, *args, **kwargs): # real signature unknown
        pass

    def endResetModel(self, *args, **kwargs): # real signature unknown
        pass

    def fieldIndex(self, fieldName, p_str=None): # real signature unknown; restored from __doc__
        """ fieldIndex(self, fieldName: Optional[str]) -> int """
        return 0

    def filter(self): # real signature unknown; restored from __doc__
        """ filter(self) -> str """
        return ""

    def flags(self, index): # real signature unknown; restored from __doc__
        """ flags(self, index: QModelIndex) -> Qt.ItemFlags """
        pass

    def headerData(self, section, orientation, role=None): # real signature unknown; restored from __doc__
        """ headerData(self, section: int, orientation: Qt.Orientation, role: int = Qt.ItemDataRole.DisplayRole) -> Any """
        pass

    def indexInQuery(self, item): # real signature unknown; restored from __doc__
        """ indexInQuery(self, item: QModelIndex) -> QModelIndex """
        pass

    def insertRecord(self, row, record): # real signature unknown; restored from __doc__
        """ insertRecord(self, row: int, record: QSqlRecord) -> bool """
        return False

    def insertRowIntoTable(self, values): # real signature unknown; restored from __doc__
        """ insertRowIntoTable(self, values: QSqlRecord) -> bool """
        return False

    def insertRows(self, row, count, parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ insertRows(self, row: int, count: int, parent: QModelIndex = QModelIndex()) -> bool """
        pass

    def isDirty(self, index=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        isDirty(self, index: QModelIndex) -> bool
        isDirty(self) -> bool
        """
        return False

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def orderByClause(self): # real signature unknown; restored from __doc__
        """ orderByClause(self) -> str """
        return ""

    def persistentIndexList(self, *args, **kwargs): # real signature unknown
        pass

    def primaryKey(self): # real signature unknown; restored from __doc__
        """ primaryKey(self) -> QSqlIndex """
        return QSqlIndex

    def primaryValues(self, row): # real signature unknown; restored from __doc__
        """ primaryValues(self, row: int) -> QSqlRecord """
        return QSqlRecord

    def primeInsert(self, *args, **kwargs): # real signature unknown
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
        pass

    def queryChange(self, *args, **kwargs): # real signature unknown
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def record(self, row=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        record(self) -> QSqlRecord
        record(self, row: int) -> QSqlRecord
        """
        return QSqlRecord

    def removeColumns(self, column, count, parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ removeColumns(self, column: int, count: int, parent: QModelIndex = QModelIndex()) -> bool """
        pass

    def removeRows(self, row, count, parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ removeRows(self, row: int, count: int, parent: QModelIndex = QModelIndex()) -> bool """
        pass

    def resetInternalData(self, *args, **kwargs): # real signature unknown
        pass

    def revert(self): # real signature unknown; restored from __doc__
        """ revert(self) """
        pass

    def revertAll(self): # real signature unknown; restored from __doc__
        """ revertAll(self) """
        pass

    def revertRow(self, row): # real signature unknown; restored from __doc__
        """ revertRow(self, row: int) """
        pass

    def rowCount(self, parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ rowCount(self, parent: QModelIndex = QModelIndex()) -> int """
        pass

    def select(self): # real signature unknown; restored from __doc__
        """ select(self) -> bool """
        return False

    def selectRow(self, row): # real signature unknown; restored from __doc__
        """ selectRow(self, row: int) -> bool """
        return False

    def selectStatement(self): # real signature unknown; restored from __doc__
        """ selectStatement(self) -> str """
        return ""

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setData(self, index, value, role=None): # real signature unknown; restored from __doc__
        """ setData(self, index: QModelIndex, value: Any, role: int = Qt.ItemDataRole.EditRole) -> bool """
        return False

    def setEditStrategy(self, strategy): # real signature unknown; restored from __doc__
        """ setEditStrategy(self, strategy: QSqlTableModel.EditStrategy) """
        pass

    def setFilter(self, filter, p_str=None): # real signature unknown; restored from __doc__
        """ setFilter(self, filter: Optional[str]) """
        pass

    def setLastError(self, *args, **kwargs): # real signature unknown
        pass

    def setPrimaryKey(self, key): # real signature unknown; restored from __doc__
        """ setPrimaryKey(self, key: QSqlIndex) """
        pass

    def setQuery(self, query): # real signature unknown; restored from __doc__
        """ setQuery(self, query: QSqlQuery) """
        pass

    def setRecord(self, row, record): # real signature unknown; restored from __doc__
        """ setRecord(self, row: int, record: QSqlRecord) -> bool """
        return False

    def setSort(self, column, order): # real signature unknown; restored from __doc__
        """ setSort(self, column: int, order: Qt.SortOrder) """
        pass

    def setTable(self, tableName, p_str=None): # real signature unknown; restored from __doc__
        """ setTable(self, tableName: Optional[str]) """
        pass

    def sort(self, column, order): # real signature unknown; restored from __doc__
        """ sort(self, column: int, order: Qt.SortOrder) """
        pass

    def submit(self): # real signature unknown; restored from __doc__
        """ submit(self) -> bool """
        return False

    def submitAll(self): # real signature unknown; restored from __doc__
        """ submitAll(self) -> bool """
        return False

    def tableName(self): # real signature unknown; restored from __doc__
        """ tableName(self) -> str """
        return ""

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def updateRowInTable(self, row, values): # real signature unknown; restored from __doc__
        """ updateRowInTable(self, row: int, values: QSqlRecord) -> bool """
        return False

    def __init__(self, parent, QObject=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    OnFieldChange = 0
    OnManualSubmit = 2
    OnRowChange = 1


class QSqlRelationalTableModel(QSqlTableModel):
    """ QSqlRelationalTableModel(parent: Optional[QObject] = None, db: QSqlDatabase = QSqlDatabase()) """
    def beginInsertColumns(self, *args, **kwargs): # real signature unknown
        pass

    def beginInsertRows(self, *args, **kwargs): # real signature unknown
        pass

    def beginMoveColumns(self, *args, **kwargs): # real signature unknown
        pass

    def beginMoveRows(self, *args, **kwargs): # real signature unknown
        pass

    def beginRemoveColumns(self, *args, **kwargs): # real signature unknown
        pass

    def beginRemoveRows(self, *args, **kwargs): # real signature unknown
        pass

    def beginResetModel(self, *args, **kwargs): # real signature unknown
        pass

    def changePersistentIndex(self, *args, **kwargs): # real signature unknown
        pass

    def changePersistentIndexList(self, *args, **kwargs): # real signature unknown
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def clear(self): # real signature unknown; restored from __doc__
        """ clear(self) """
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def createIndex(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def data(self, item, role=None): # real signature unknown; restored from __doc__
        """ data(self, item: QModelIndex, role: int = Qt.ItemDataRole.DisplayRole) -> Any """
        pass

    def decodeData(self, *args, **kwargs): # real signature unknown
        pass

    def deleteRowFromTable(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def encodeData(self, *args, **kwargs): # real signature unknown
        pass

    def endInsertColumns(self, *args, **kwargs): # real signature unknown
        pass

    def endInsertRows(self, *args, **kwargs): # real signature unknown
        pass

    def endMoveColumns(self, *args, **kwargs): # real signature unknown
        pass

    def endMoveRows(self, *args, **kwargs): # real signature unknown
        pass

    def endRemoveColumns(self, *args, **kwargs): # real signature unknown
        pass

    def endRemoveRows(self, *args, **kwargs): # real signature unknown
        pass

    def endResetModel(self, *args, **kwargs): # real signature unknown
        pass

    def indexInQuery(self, *args, **kwargs): # real signature unknown
        pass

    def insertRowIntoTable(self, values): # real signature unknown; restored from __doc__
        """ insertRowIntoTable(self, values: QSqlRecord) -> bool """
        return False

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def orderByClause(self): # real signature unknown; restored from __doc__
        """ orderByClause(self) -> str """
        return ""

    def persistentIndexList(self, *args, **kwargs): # real signature unknown
        pass

    def primaryValues(self, *args, **kwargs): # real signature unknown
        pass

    def queryChange(self, *args, **kwargs): # real signature unknown
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def relation(self, column): # real signature unknown; restored from __doc__
        """ relation(self, column: int) -> QSqlRelation """
        return QSqlRelation

    def relationModel(self, column): # real signature unknown; restored from __doc__
        """ relationModel(self, column: int) -> Optional[QSqlTableModel] """
        pass

    def removeColumns(self, column, count, parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ removeColumns(self, column: int, count: int, parent: QModelIndex = QModelIndex()) -> bool """
        pass

    def resetInternalData(self, *args, **kwargs): # real signature unknown
        pass

    def revertRow(self, row): # real signature unknown; restored from __doc__
        """ revertRow(self, row: int) """
        pass

    def select(self): # real signature unknown; restored from __doc__
        """ select(self) -> bool """
        return False

    def selectStatement(self): # real signature unknown; restored from __doc__
        """ selectStatement(self) -> str """
        return ""

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setData(self, item, value, role=None): # real signature unknown; restored from __doc__
        """ setData(self, item: QModelIndex, value: Any, role: int = Qt.ItemDataRole.EditRole) -> bool """
        return False

    def setJoinMode(self, joinMode): # real signature unknown; restored from __doc__
        """ setJoinMode(self, joinMode: QSqlRelationalTableModel.JoinMode) """
        pass

    def setLastError(self, *args, **kwargs): # real signature unknown
        pass

    def setPrimaryKey(self, *args, **kwargs): # real signature unknown
        pass

    def setQuery(self, *args, **kwargs): # real signature unknown
        pass

    def setRelation(self, column, relation): # real signature unknown; restored from __doc__
        """ setRelation(self, column: int, relation: QSqlRelation) """
        pass

    def setTable(self, tableName, p_str=None): # real signature unknown; restored from __doc__
        """ setTable(self, tableName: Optional[str]) """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def updateRowInTable(self, row, values): # real signature unknown; restored from __doc__
        """ updateRowInTable(self, row: int, values: QSqlRecord) -> bool """
        return False

    def __init__(self, parent, QObject=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    InnerJoin = 0
    LeftJoin = 1


class QSqlResult(__sip.wrapper):
    """ QSqlResult(db: Optional[QSqlDriver]) """
    def addBindValue(self, val, type, QSql_ParamType=None, QSql_ParamTypeFlag=None): # real signature unknown; restored from __doc__
        """ addBindValue(self, val: Any, type: Union[QSql.ParamType, QSql.ParamTypeFlag]) """
        pass

    def at(self): # real signature unknown; restored from __doc__
        """ at(self) -> int """
        return 0

    def bindingSyntax(self): # real signature unknown; restored from __doc__
        """ bindingSyntax(self) -> QSqlResult.BindingSyntax """
        pass

    def bindValue(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        bindValue(self, pos: int, val: Any, type: Union[QSql.ParamType, QSql.ParamTypeFlag])
        bindValue(self, placeholder: Optional[str], val: Any, type: Union[QSql.ParamType, QSql.ParamTypeFlag])
        """
        pass

    def bindValueType(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        bindValueType(self, placeholder: Optional[str]) -> QSql.ParamType
        bindValueType(self, pos: int) -> QSql.ParamType
        """
        pass

    def boundValue(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        boundValue(self, placeholder: Optional[str]) -> Any
        boundValue(self, pos: int) -> Any
        """
        pass

    def boundValueCount(self): # real signature unknown; restored from __doc__
        """ boundValueCount(self) -> int """
        return 0

    def boundValueName(self, pos): # real signature unknown; restored from __doc__
        """ boundValueName(self, pos: int) -> str """
        return ""

    def boundValues(self): # real signature unknown; restored from __doc__
        """ boundValues(self) -> List[Any] """
        return []

    def clear(self): # real signature unknown; restored from __doc__
        """ clear(self) """
        pass

    def data(self, i): # real signature unknown; restored from __doc__
        """ data(self, i: int) -> Any """
        pass

    def driver(self): # real signature unknown; restored from __doc__
        """ driver(self) -> Optional[QSqlDriver] """
        pass

    def exec(self): # real signature unknown; restored from __doc__
        """ exec(self) -> bool """
        return False

    def executedQuery(self): # real signature unknown; restored from __doc__
        """ executedQuery(self) -> str """
        return ""

    def exec_(self): # real signature unknown; restored from __doc__
        """ exec_(self) -> bool """
        return False

    def fetch(self, i): # real signature unknown; restored from __doc__
        """ fetch(self, i: int) -> bool """
        return False

    def fetchFirst(self): # real signature unknown; restored from __doc__
        """ fetchFirst(self) -> bool """
        return False

    def fetchLast(self): # real signature unknown; restored from __doc__
        """ fetchLast(self) -> bool """
        return False

    def fetchNext(self): # real signature unknown; restored from __doc__
        """ fetchNext(self) -> bool """
        return False

    def fetchPrevious(self): # real signature unknown; restored from __doc__
        """ fetchPrevious(self) -> bool """
        return False

    def handle(self): # real signature unknown; restored from __doc__
        """ handle(self) -> Any """
        pass

    def hasOutValues(self): # real signature unknown; restored from __doc__
        """ hasOutValues(self) -> bool """
        return False

    def isActive(self): # real signature unknown; restored from __doc__
        """ isActive(self) -> bool """
        return False

    def isForwardOnly(self): # real signature unknown; restored from __doc__
        """ isForwardOnly(self) -> bool """
        return False

    def isNull(self, i): # real signature unknown; restored from __doc__
        """ isNull(self, i: int) -> bool """
        return False

    def isSelect(self): # real signature unknown; restored from __doc__
        """ isSelect(self) -> bool """
        return False

    def isValid(self): # real signature unknown; restored from __doc__
        """ isValid(self) -> bool """
        return False

    def lastError(self): # real signature unknown; restored from __doc__
        """ lastError(self) -> QSqlError """
        return QSqlError

    def lastInsertId(self): # real signature unknown; restored from __doc__
        """ lastInsertId(self) -> Any """
        pass

    def lastQuery(self): # real signature unknown; restored from __doc__
        """ lastQuery(self) -> str """
        return ""

    def numRowsAffected(self): # real signature unknown; restored from __doc__
        """ numRowsAffected(self) -> int """
        return 0

    def prepare(self, query, p_str=None): # real signature unknown; restored from __doc__
        """ prepare(self, query: Optional[str]) -> bool """
        return False

    def record(self): # real signature unknown; restored from __doc__
        """ record(self) -> QSqlRecord """
        return QSqlRecord

    def reset(self, sqlquery, p_str=None): # real signature unknown; restored from __doc__
        """ reset(self, sqlquery: Optional[str]) -> bool """
        return False

    def savePrepare(self, sqlquery, p_str=None): # real signature unknown; restored from __doc__
        """ savePrepare(self, sqlquery: Optional[str]) -> bool """
        return False

    def setActive(self, a): # real signature unknown; restored from __doc__
        """ setActive(self, a: bool) """
        pass

    def setAt(self, at): # real signature unknown; restored from __doc__
        """ setAt(self, at: int) """
        pass

    def setForwardOnly(self, forward): # real signature unknown; restored from __doc__
        """ setForwardOnly(self, forward: bool) """
        pass

    def setLastError(self, e): # real signature unknown; restored from __doc__
        """ setLastError(self, e: QSqlError) """
        pass

    def setQuery(self, query, p_str=None): # real signature unknown; restored from __doc__
        """ setQuery(self, query: Optional[str]) """
        pass

    def setSelect(self, s): # real signature unknown; restored from __doc__
        """ setSelect(self, s: bool) """
        pass

    def size(self): # real signature unknown; restored from __doc__
        """ size(self) -> int """
        return 0

    def __init__(self, db, QSqlDriver=None): # real signature unknown; restored from __doc__
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    NamedBinding = 1
    PositionalBinding = 0


# variables with complex values



