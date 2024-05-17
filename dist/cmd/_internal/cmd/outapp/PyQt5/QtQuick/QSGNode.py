# encoding: utf-8
# module PyQt5.QtQuick
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtQuick.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import PyQt5.QtGui as __PyQt5_QtGui
import PyQt5.QtQml as __PyQt5_QtQml
import sip as __sip


class QSGNode(__sip.wrapper):
    """ QSGNode() """
    def appendChildNode(self, node, QSGNode=None): # real signature unknown; restored from __doc__
        """ appendChildNode(self, node: Optional[QSGNode]) """
        pass

    def childAtIndex(self, i): # real signature unknown; restored from __doc__
        """ childAtIndex(self, i: int) -> Optional[QSGNode] """
        pass

    def childCount(self): # real signature unknown; restored from __doc__
        """ childCount(self) -> int """
        return 0

    def firstChild(self): # real signature unknown; restored from __doc__
        """ firstChild(self) -> Optional[QSGNode] """
        pass

    def flags(self): # real signature unknown; restored from __doc__
        """ flags(self) -> QSGNode.Flags """
        pass

    def insertChildNodeAfter(self, node, QSGNode=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ insertChildNodeAfter(self, node: Optional[QSGNode], after: Optional[QSGNode]) """
        pass

    def insertChildNodeBefore(self, node, QSGNode=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ insertChildNodeBefore(self, node: Optional[QSGNode], before: Optional[QSGNode]) """
        pass

    def isSubtreeBlocked(self): # real signature unknown; restored from __doc__
        """ isSubtreeBlocked(self) -> bool """
        return False

    def lastChild(self): # real signature unknown; restored from __doc__
        """ lastChild(self) -> Optional[QSGNode] """
        pass

    def markDirty(self, bits, QSGNode_DirtyState=None, QSGNode_DirtyStateBit=None): # real signature unknown; restored from __doc__
        """ markDirty(self, bits: Union[QSGNode.DirtyState, QSGNode.DirtyStateBit]) """
        pass

    def nextSibling(self): # real signature unknown; restored from __doc__
        """ nextSibling(self) -> Optional[QSGNode] """
        pass

    def parent(self): # real signature unknown; restored from __doc__
        """ parent(self) -> Optional[QSGNode] """
        pass

    def prependChildNode(self, node, QSGNode=None): # real signature unknown; restored from __doc__
        """ prependChildNode(self, node: Optional[QSGNode]) """
        pass

    def preprocess(self): # real signature unknown; restored from __doc__
        """ preprocess(self) """
        pass

    def previousSibling(self): # real signature unknown; restored from __doc__
        """ previousSibling(self) -> Optional[QSGNode] """
        pass

    def removeAllChildNodes(self): # real signature unknown; restored from __doc__
        """ removeAllChildNodes(self) """
        pass

    def removeChildNode(self, node, QSGNode=None): # real signature unknown; restored from __doc__
        """ removeChildNode(self, node: Optional[QSGNode]) """
        pass

    def setFlag(self, a0, enabled=True): # real signature unknown; restored from __doc__
        """ setFlag(self, a0: QSGNode.Flag, enabled: bool = True) """
        pass

    def setFlags(self, a0, QSGNode_Flags=None, QSGNode_Flag=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ setFlags(self, a0: Union[QSGNode.Flags, QSGNode.Flag], enabled: bool = True) """
        pass

    def type(self): # real signature unknown; restored from __doc__
        """ type(self) -> QSGNode.NodeType """
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    def __len__(self, *args, **kwargs): # real signature unknown
        """ Return len(self). """
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    BasicNodeType = 0
    ClipNodeType = 3
    DirtyGeometry = 4096
    DirtyMaterial = 8192
    DirtyMatrix = 256
    DirtyNodeAdded = 1024
    DirtyNodeRemoved = 2048
    DirtyOpacity = 16384
    GeometryNodeType = 1
    OpacityNodeType = 4
    OwnedByParent = 1
    OwnsGeometry = 65536
    OwnsMaterial = 131072
    OwnsOpaqueMaterial = 262144
    TransformNodeType = 2
    UsePreprocess = 2


