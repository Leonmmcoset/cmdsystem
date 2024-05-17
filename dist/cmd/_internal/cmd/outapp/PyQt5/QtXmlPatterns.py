# encoding: utf-8
# module PyQt5.QtXmlPatterns
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtXmlPatterns.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


# no functions
# classes

class QAbstractMessageHandler(__PyQt5_QtCore.QObject):
    """ QAbstractMessageHandler(parent: Optional[QObject] = None) """
    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def handleMessage(self, type, description, p_str=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ handleMessage(self, type: QtMsgType, description: Optional[str], identifier: QUrl, sourceLocation: QSourceLocation) """
        pass

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def message(self, type, description, p_str=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ message(self, type: QtMsgType, description: Optional[str], identifier: QUrl = QUrl(), sourceLocation: QSourceLocation = QSourceLocation()) """
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, parent, QObject=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass


class QAbstractUriResolver(__PyQt5_QtCore.QObject):
    """ QAbstractUriResolver(parent: Optional[QObject] = None) """
    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def resolve(self, relative, baseURI): # real signature unknown; restored from __doc__
        """ resolve(self, relative: QUrl, baseURI: QUrl) -> QUrl """
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, parent, QObject=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass


class QAbstractXmlNodeModel(__sip.simplewrapper):
    """ QAbstractXmlNodeModel() """
    def attributes(self, element): # real signature unknown; restored from __doc__
        """ attributes(self, element: QXmlNodeModelIndex) -> List[QXmlNodeModelIndex] """
        return []

    def baseUri(self, ni): # real signature unknown; restored from __doc__
        """ baseUri(self, ni: QXmlNodeModelIndex) -> QUrl """
        pass

    def compareOrder(self, ni1, ni2): # real signature unknown; restored from __doc__
        """ compareOrder(self, ni1: QXmlNodeModelIndex, ni2: QXmlNodeModelIndex) -> QXmlNodeModelIndex.DocumentOrder """
        pass

    def createIndex(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        createIndex(self, data: int) -> QXmlNodeModelIndex
        createIndex(self, data: int, additionalData: int) -> QXmlNodeModelIndex
        createIndex(self, pointer: Any, additionalData: int = 0) -> QXmlNodeModelIndex
        """
        return QXmlNodeModelIndex

    def documentUri(self, ni): # real signature unknown; restored from __doc__
        """ documentUri(self, ni: QXmlNodeModelIndex) -> QUrl """
        pass

    def elementById(self, NCName): # real signature unknown; restored from __doc__
        """ elementById(self, NCName: QXmlName) -> QXmlNodeModelIndex """
        return QXmlNodeModelIndex

    def kind(self, ni): # real signature unknown; restored from __doc__
        """ kind(self, ni: QXmlNodeModelIndex) -> QXmlNodeModelIndex.NodeKind """
        pass

    def name(self, ni): # real signature unknown; restored from __doc__
        """ name(self, ni: QXmlNodeModelIndex) -> QXmlName """
        return QXmlName

    def namespaceBindings(self, n): # real signature unknown; restored from __doc__
        """ namespaceBindings(self, n: QXmlNodeModelIndex) -> List[QXmlName] """
        return []

    def nextFromSimpleAxis(self, axis, origin): # real signature unknown; restored from __doc__
        """ nextFromSimpleAxis(self, axis: QAbstractXmlNodeModel.SimpleAxis, origin: QXmlNodeModelIndex) -> QXmlNodeModelIndex """
        return QXmlNodeModelIndex

    def nodesByIdref(self, NCName): # real signature unknown; restored from __doc__
        """ nodesByIdref(self, NCName: QXmlName) -> List[QXmlNodeModelIndex] """
        return []

    def root(self, n): # real signature unknown; restored from __doc__
        """ root(self, n: QXmlNodeModelIndex) -> QXmlNodeModelIndex """
        return QXmlNodeModelIndex

    def sourceLocation(self, index): # real signature unknown; restored from __doc__
        """ sourceLocation(self, index: QXmlNodeModelIndex) -> QSourceLocation """
        return QSourceLocation

    def stringValue(self, n): # real signature unknown; restored from __doc__
        """ stringValue(self, n: QXmlNodeModelIndex) -> str """
        return ""

    def typedValue(self, n): # real signature unknown; restored from __doc__
        """ typedValue(self, n: QXmlNodeModelIndex) -> Any """
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    FirstChild = 1
    NextSibling = 3
    Parent = 0
    PreviousSibling = 2


class QAbstractXmlReceiver(__sip.simplewrapper):
    """ QAbstractXmlReceiver() """
    def atomicValue(self, value): # real signature unknown; restored from __doc__
        """ atomicValue(self, value: Any) """
        pass

    def attribute(self, name, value): # real signature unknown; restored from __doc__
        """ attribute(self, name: QXmlName, value: str) """
        pass

    def characters(self, value): # real signature unknown; restored from __doc__
        """ characters(self, value: str) """
        pass

    def comment(self, value, p_str=None): # real signature unknown; restored from __doc__
        """ comment(self, value: Optional[str]) """
        pass

    def endDocument(self): # real signature unknown; restored from __doc__
        """ endDocument(self) """
        pass

    def endElement(self): # real signature unknown; restored from __doc__
        """ endElement(self) """
        pass

    def endOfSequence(self): # real signature unknown; restored from __doc__
        """ endOfSequence(self) """
        pass

    def namespaceBinding(self, name): # real signature unknown; restored from __doc__
        """ namespaceBinding(self, name: QXmlName) """
        pass

    def processingInstruction(self, target, value, p_str=None): # real signature unknown; restored from __doc__
        """ processingInstruction(self, target: QXmlName, value: Optional[str]) """
        pass

    def startDocument(self): # real signature unknown; restored from __doc__
        """ startDocument(self) """
        pass

    def startElement(self, name): # real signature unknown; restored from __doc__
        """ startElement(self, name: QXmlName) """
        pass

    def startOfSequence(self): # real signature unknown; restored from __doc__
        """ startOfSequence(self) """
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class QSimpleXmlNodeModel(QAbstractXmlNodeModel):
    """ QSimpleXmlNodeModel(namePool: QXmlNamePool) """
    def attributes(self, *args, **kwargs): # real signature unknown
        pass

    def baseUri(self, node): # real signature unknown; restored from __doc__
        """ baseUri(self, node: QXmlNodeModelIndex) -> QUrl """
        pass

    def createIndex(self, *args, **kwargs): # real signature unknown
        pass

    def elementById(self, id): # real signature unknown; restored from __doc__
        """ elementById(self, id: QXmlName) -> QXmlNodeModelIndex """
        return QXmlNodeModelIndex

    def namePool(self): # real signature unknown; restored from __doc__
        """ namePool(self) -> QXmlNamePool """
        return QXmlNamePool

    def namespaceBindings(self, a0): # real signature unknown; restored from __doc__
        """ namespaceBindings(self, a0: QXmlNodeModelIndex) -> List[QXmlName] """
        return []

    def nextFromSimpleAxis(self, *args, **kwargs): # real signature unknown
        pass

    def nodesByIdref(self, idref): # real signature unknown; restored from __doc__
        """ nodesByIdref(self, idref: QXmlName) -> List[QXmlNodeModelIndex] """
        return []

    def stringValue(self, node): # real signature unknown; restored from __doc__
        """ stringValue(self, node: QXmlNodeModelIndex) -> str """
        return ""

    def __init__(self, namePool): # real signature unknown; restored from __doc__
        pass


class QSourceLocation(__sip.simplewrapper):
    """
    QSourceLocation()
    QSourceLocation(other: QSourceLocation)
    QSourceLocation(u: QUrl, line: int = -1, column: int = -1)
    """
    def column(self): # real signature unknown; restored from __doc__
        """ column(self) -> int """
        return 0

    def isNull(self): # real signature unknown; restored from __doc__
        """ isNull(self) -> bool """
        return False

    def line(self): # real signature unknown; restored from __doc__
        """ line(self) -> int """
        return 0

    def setColumn(self, newColumn): # real signature unknown; restored from __doc__
        """ setColumn(self, newColumn: int) """
        pass

    def setLine(self, newLine): # real signature unknown; restored from __doc__
        """ setLine(self, newLine: int) """
        pass

    def setUri(self, newUri): # real signature unknown; restored from __doc__
        """ setUri(self, newUri: QUrl) """
        pass

    def uri(self): # real signature unknown; restored from __doc__
        """ uri(self) -> QUrl """
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



class QXmlSerializer(QAbstractXmlReceiver):
    """ QXmlSerializer(query: QXmlQuery, outputDevice: Optional[QIODevice]) """
    def atomicValue(self, value): # real signature unknown; restored from __doc__
        """ atomicValue(self, value: Any) """
        pass

    def attribute(self, name, value): # real signature unknown; restored from __doc__
        """ attribute(self, name: QXmlName, value: str) """
        pass

    def characters(self, value): # real signature unknown; restored from __doc__
        """ characters(self, value: str) """
        pass

    def codec(self): # real signature unknown; restored from __doc__
        """ codec(self) -> Optional[QTextCodec] """
        pass

    def comment(self, value, p_str=None): # real signature unknown; restored from __doc__
        """ comment(self, value: Optional[str]) """
        pass

    def endDocument(self): # real signature unknown; restored from __doc__
        """ endDocument(self) """
        pass

    def endElement(self): # real signature unknown; restored from __doc__
        """ endElement(self) """
        pass

    def endOfSequence(self): # real signature unknown; restored from __doc__
        """ endOfSequence(self) """
        pass

    def namespaceBinding(self, nb): # real signature unknown; restored from __doc__
        """ namespaceBinding(self, nb: QXmlName) """
        pass

    def outputDevice(self): # real signature unknown; restored from __doc__
        """ outputDevice(self) -> Optional[QIODevice] """
        pass

    def processingInstruction(self, name, value, p_str=None): # real signature unknown; restored from __doc__
        """ processingInstruction(self, name: QXmlName, value: Optional[str]) """
        pass

    def setCodec(self, codec, QTextCodec=None): # real signature unknown; restored from __doc__
        """ setCodec(self, codec: Optional[QTextCodec]) """
        pass

    def startDocument(self): # real signature unknown; restored from __doc__
        """ startDocument(self) """
        pass

    def startElement(self, name): # real signature unknown; restored from __doc__
        """ startElement(self, name: QXmlName) """
        pass

    def startOfSequence(self): # real signature unknown; restored from __doc__
        """ startOfSequence(self) """
        pass

    def __init__(self, query, outputDevice, QIODevice=None): # real signature unknown; restored from __doc__
        pass


class QXmlFormatter(QXmlSerializer):
    """ QXmlFormatter(query: QXmlQuery, outputDevice: Optional[QIODevice]) """
    def atomicValue(self, value): # real signature unknown; restored from __doc__
        """ atomicValue(self, value: Any) """
        pass

    def attribute(self, name, value): # real signature unknown; restored from __doc__
        """ attribute(self, name: QXmlName, value: str) """
        pass

    def characters(self, value): # real signature unknown; restored from __doc__
        """ characters(self, value: str) """
        pass

    def comment(self, value, p_str=None): # real signature unknown; restored from __doc__
        """ comment(self, value: Optional[str]) """
        pass

    def endDocument(self): # real signature unknown; restored from __doc__
        """ endDocument(self) """
        pass

    def endElement(self): # real signature unknown; restored from __doc__
        """ endElement(self) """
        pass

    def endOfSequence(self): # real signature unknown; restored from __doc__
        """ endOfSequence(self) """
        pass

    def indentationDepth(self): # real signature unknown; restored from __doc__
        """ indentationDepth(self) -> int """
        return 0

    def processingInstruction(self, name, value, p_str=None): # real signature unknown; restored from __doc__
        """ processingInstruction(self, name: QXmlName, value: Optional[str]) """
        pass

    def setIndentationDepth(self, depth): # real signature unknown; restored from __doc__
        """ setIndentationDepth(self, depth: int) """
        pass

    def startDocument(self): # real signature unknown; restored from __doc__
        """ startDocument(self) """
        pass

    def startElement(self, name): # real signature unknown; restored from __doc__
        """ startElement(self, name: QXmlName) """
        pass

    def startOfSequence(self): # real signature unknown; restored from __doc__
        """ startOfSequence(self) """
        pass

    def __init__(self, query, outputDevice, QIODevice=None): # real signature unknown; restored from __doc__
        pass


class QXmlItem(__sip.simplewrapper):
    """
    QXmlItem()
    QXmlItem(other: QXmlItem)
    QXmlItem(node: QXmlNodeModelIndex)
    QXmlItem(atomicValue: Any)
    """
    def isAtomicValue(self): # real signature unknown; restored from __doc__
        """ isAtomicValue(self) -> bool """
        return False

    def isNode(self): # real signature unknown; restored from __doc__
        """ isNode(self) -> bool """
        return False

    def isNull(self): # real signature unknown; restored from __doc__
        """ isNull(self) -> bool """
        return False

    def toAtomicValue(self): # real signature unknown; restored from __doc__
        """ toAtomicValue(self) -> Any """
        pass

    def toNodeModelIndex(self): # real signature unknown; restored from __doc__
        """ toNodeModelIndex(self) -> QXmlNodeModelIndex """
        return QXmlNodeModelIndex

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class QXmlName(__sip.simplewrapper):
    """
    QXmlName()
    QXmlName(namePool: QXmlNamePool, localName: Optional[str], namespaceUri: Optional[str] = '', prefix: Optional[str] = '')
    QXmlName(other: QXmlName)
    """
    def fromClarkName(self, clarkName, p_str=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ fromClarkName(clarkName: Optional[str], namePool: QXmlNamePool) -> QXmlName """
        pass

    def isNCName(self, candidate, p_str=None): # real signature unknown; restored from __doc__
        """ isNCName(candidate: Optional[str]) -> bool """
        return False

    def isNull(self): # real signature unknown; restored from __doc__
        """ isNull(self) -> bool """
        return False

    def localName(self, query): # real signature unknown; restored from __doc__
        """ localName(self, query: QXmlNamePool) -> str """
        return ""

    def namespaceUri(self, query): # real signature unknown; restored from __doc__
        """ namespaceUri(self, query: QXmlNamePool) -> str """
        return ""

    def prefix(self, query): # real signature unknown; restored from __doc__
        """ prefix(self, query: QXmlNamePool) -> str """
        return ""

    def toClarkName(self, query): # real signature unknown; restored from __doc__
        """ toClarkName(self, query: QXmlNamePool) -> str """
        return ""

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



class QXmlNamePool(__sip.simplewrapper):
    """
    QXmlNamePool()
    QXmlNamePool(other: QXmlNamePool)
    """
    def __init__(self, other=None): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class QXmlNodeModelIndex(__sip.simplewrapper):
    """
    QXmlNodeModelIndex()
    QXmlNodeModelIndex(other: QXmlNodeModelIndex)
    """
    def additionalData(self): # real signature unknown; restored from __doc__
        """ additionalData(self) -> int """
        return 0

    def data(self): # real signature unknown; restored from __doc__
        """ data(self) -> int """
        return 0

    def internalPointer(self): # real signature unknown; restored from __doc__
        """ internalPointer(self) -> Any """
        pass

    def isNull(self): # real signature unknown; restored from __doc__
        """ isNull(self) -> bool """
        return False

    def model(self): # real signature unknown; restored from __doc__
        """ model(self) -> Optional[QAbstractXmlNodeModel] """
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

    def __init__(self, other=None): # real signature unknown; restored from __doc__ with multiple overloads
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


    Attribute = 1
    Comment = 2
    Document = 4
    Element = 8
    Follows = 1
    Is = 0
    Namespace = 16
    Precedes = -1
    ProcessingInstruction = 32
    Text = 64


class QXmlQuery(__sip.simplewrapper):
    """
    QXmlQuery()
    QXmlQuery(other: QXmlQuery)
    QXmlQuery(np: QXmlNamePool)
    QXmlQuery(queryLanguage: QXmlQuery.QueryLanguage, pool: QXmlNamePool = QXmlNamePool())
    """
    def bindVariable(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        bindVariable(self, name: QXmlName, value: QXmlItem)
        bindVariable(self, name: QXmlName, a1: Optional[QIODevice])
        bindVariable(self, name: QXmlName, query: QXmlQuery)
        bindVariable(self, localName: Optional[str], value: QXmlItem)
        bindVariable(self, localName: Optional[str], a1: Optional[QIODevice])
        bindVariable(self, localName: Optional[str], query: QXmlQuery)
        """
        pass

    def evaluateTo(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        evaluateTo(self, result: Optional[QXmlResultItems])
        evaluateTo(self, callback: Optional[QAbstractXmlReceiver]) -> bool
        evaluateTo(self, target: Optional[QIODevice]) -> bool
        """
        return False

    def evaluateToString(self): # real signature unknown; restored from __doc__
        """ evaluateToString(self) -> str """
        return ""

    def evaluateToStringList(self): # real signature unknown; restored from __doc__
        """ evaluateToStringList(self) -> List[str] """
        return []

    def initialTemplateName(self): # real signature unknown; restored from __doc__
        """ initialTemplateName(self) -> QXmlName """
        return QXmlName

    def isValid(self): # real signature unknown; restored from __doc__
        """ isValid(self) -> bool """
        return False

    def messageHandler(self): # real signature unknown; restored from __doc__
        """ messageHandler(self) -> Optional[QAbstractMessageHandler] """
        pass

    def namePool(self): # real signature unknown; restored from __doc__
        """ namePool(self) -> QXmlNamePool """
        return QXmlNamePool

    def networkAccessManager(self): # real signature unknown; restored from __doc__
        """ networkAccessManager(self) -> Optional[QNetworkAccessManager] """
        pass

    def queryLanguage(self): # real signature unknown; restored from __doc__
        """ queryLanguage(self) -> QXmlQuery.QueryLanguage """
        pass

    def setFocus(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setFocus(self, item: QXmlItem)
        setFocus(self, documentURI: QUrl) -> bool
        setFocus(self, document: Optional[QIODevice]) -> bool
        setFocus(self, focus: Optional[str]) -> bool
        """
        return False

    def setInitialTemplateName(self, name, p_str=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setInitialTemplateName(self, name: QXmlName)
        setInitialTemplateName(self, name: Optional[str])
        """
        pass

    def setMessageHandler(self, messageHandler, QAbstractMessageHandler=None): # real signature unknown; restored from __doc__
        """ setMessageHandler(self, messageHandler: Optional[QAbstractMessageHandler]) """
        pass

    def setNetworkAccessManager(self, newManager, QNetworkAccessManager=None): # real signature unknown; restored from __doc__
        """ setNetworkAccessManager(self, newManager: Optional[QNetworkAccessManager]) """
        pass

    def setQuery(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setQuery(self, sourceCode: Optional[str], documentUri: QUrl = QUrl())
        setQuery(self, sourceCode: Optional[QIODevice], documentUri: QUrl = QUrl())
        setQuery(self, queryURI: QUrl, baseUri: QUrl = QUrl())
        """
        pass

    def setUriResolver(self, resolver, QAbstractUriResolver=None): # real signature unknown; restored from __doc__
        """ setUriResolver(self, resolver: Optional[QAbstractUriResolver]) """
        pass

    def uriResolver(self): # real signature unknown; restored from __doc__
        """ uriResolver(self) -> Optional[QAbstractUriResolver] """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    XQuery10 = 1
    XSLT20 = 2


class QXmlResultItems(__sip.simplewrapper):
    """ QXmlResultItems() """
    def current(self): # real signature unknown; restored from __doc__
        """ current(self) -> QXmlItem """
        return QXmlItem

    def hasError(self): # real signature unknown; restored from __doc__
        """ hasError(self) -> bool """
        return False

    def next(self): # real signature unknown; restored from __doc__
        """ next(self) -> QXmlItem """
        return QXmlItem

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class QXmlSchema(__sip.simplewrapper):
    """
    QXmlSchema()
    QXmlSchema(other: QXmlSchema)
    """
    def documentUri(self): # real signature unknown; restored from __doc__
        """ documentUri(self) -> QUrl """
        pass

    def isValid(self): # real signature unknown; restored from __doc__
        """ isValid(self) -> bool """
        return False

    def load(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        load(self, source: QUrl) -> bool
        load(self, source: Optional[QIODevice], documentUri: QUrl = QUrl()) -> bool
        load(self, data: Union[QByteArray, bytes, bytearray], documentUri: QUrl = QUrl()) -> bool
        """
        return False

    def messageHandler(self): # real signature unknown; restored from __doc__
        """ messageHandler(self) -> Optional[QAbstractMessageHandler] """
        pass

    def namePool(self): # real signature unknown; restored from __doc__
        """ namePool(self) -> QXmlNamePool """
        return QXmlNamePool

    def networkAccessManager(self): # real signature unknown; restored from __doc__
        """ networkAccessManager(self) -> Optional[QNetworkAccessManager] """
        pass

    def setMessageHandler(self, handler, QAbstractMessageHandler=None): # real signature unknown; restored from __doc__
        """ setMessageHandler(self, handler: Optional[QAbstractMessageHandler]) """
        pass

    def setNetworkAccessManager(self, networkmanager, QNetworkAccessManager=None): # real signature unknown; restored from __doc__
        """ setNetworkAccessManager(self, networkmanager: Optional[QNetworkAccessManager]) """
        pass

    def setUriResolver(self, resolver, QAbstractUriResolver=None): # real signature unknown; restored from __doc__
        """ setUriResolver(self, resolver: Optional[QAbstractUriResolver]) """
        pass

    def uriResolver(self): # real signature unknown; restored from __doc__
        """ uriResolver(self) -> Optional[QAbstractUriResolver] """
        pass

    def __init__(self, other=None): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class QXmlSchemaValidator(__sip.simplewrapper):
    """
    QXmlSchemaValidator()
    QXmlSchemaValidator(schema: QXmlSchema)
    """
    def messageHandler(self): # real signature unknown; restored from __doc__
        """ messageHandler(self) -> Optional[QAbstractMessageHandler] """
        pass

    def namePool(self): # real signature unknown; restored from __doc__
        """ namePool(self) -> QXmlNamePool """
        return QXmlNamePool

    def networkAccessManager(self): # real signature unknown; restored from __doc__
        """ networkAccessManager(self) -> Optional[QNetworkAccessManager] """
        pass

    def schema(self): # real signature unknown; restored from __doc__
        """ schema(self) -> QXmlSchema """
        return QXmlSchema

    def setMessageHandler(self, handler, QAbstractMessageHandler=None): # real signature unknown; restored from __doc__
        """ setMessageHandler(self, handler: Optional[QAbstractMessageHandler]) """
        pass

    def setNetworkAccessManager(self, networkmanager, QNetworkAccessManager=None): # real signature unknown; restored from __doc__
        """ setNetworkAccessManager(self, networkmanager: Optional[QNetworkAccessManager]) """
        pass

    def setSchema(self, schema): # real signature unknown; restored from __doc__
        """ setSchema(self, schema: QXmlSchema) """
        pass

    def setUriResolver(self, resolver, QAbstractUriResolver=None): # real signature unknown; restored from __doc__
        """ setUriResolver(self, resolver: Optional[QAbstractUriResolver]) """
        pass

    def uriResolver(self): # real signature unknown; restored from __doc__
        """ uriResolver(self) -> Optional[QAbstractUriResolver] """
        pass

    def validate(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        validate(self, source: QUrl) -> bool
        validate(self, source: Optional[QIODevice], documentUri: QUrl = QUrl()) -> bool
        validate(self, data: Union[QByteArray, bytes, bytearray], documentUri: QUrl = QUrl()) -> bool
        """
        return False

    def __init__(self, schema=None): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



# variables with complex values



