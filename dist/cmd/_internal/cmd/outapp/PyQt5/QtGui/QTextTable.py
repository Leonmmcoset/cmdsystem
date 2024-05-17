# encoding: utf-8
# module PyQt5.QtGui
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtGui.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


from .QTextFrame import QTextFrame

class QTextTable(QTextFrame):
    """ QTextTable(doc: Optional[QTextDocument]) """
    def appendColumns(self, count): # real signature unknown; restored from __doc__
        """ appendColumns(self, count: int) """
        pass

    def appendRows(self, count): # real signature unknown; restored from __doc__
        """ appendRows(self, count: int) """
        pass

    def cellAt(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        cellAt(self, row: int, col: int) -> QTextTableCell
        cellAt(self, position: int) -> QTextTableCell
        cellAt(self, c: QTextCursor) -> QTextTableCell
        """
        return QTextTableCell

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def columns(self): # real signature unknown; restored from __doc__
        """ columns(self) -> int """
        return 0

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def format(self): # real signature unknown; restored from __doc__
        """ format(self) -> QTextTableFormat """
        return QTextTableFormat

    def insertColumns(self, pos, num): # real signature unknown; restored from __doc__
        """ insertColumns(self, pos: int, num: int) """
        pass

    def insertRows(self, pos, num): # real signature unknown; restored from __doc__
        """ insertRows(self, pos: int, num: int) """
        pass

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def mergeCells(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        mergeCells(self, row: int, col: int, numRows: int, numCols: int)
        mergeCells(self, cursor: QTextCursor)
        """
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def removeColumns(self, pos, num): # real signature unknown; restored from __doc__
        """ removeColumns(self, pos: int, num: int) """
        pass

    def removeRows(self, pos, num): # real signature unknown; restored from __doc__
        """ removeRows(self, pos: int, num: int) """
        pass

    def resize(self, rows, cols): # real signature unknown; restored from __doc__
        """ resize(self, rows: int, cols: int) """
        pass

    def rowEnd(self, c): # real signature unknown; restored from __doc__
        """ rowEnd(self, c: QTextCursor) -> QTextCursor """
        return QTextCursor

    def rows(self): # real signature unknown; restored from __doc__
        """ rows(self) -> int """
        return 0

    def rowStart(self, c): # real signature unknown; restored from __doc__
        """ rowStart(self, c: QTextCursor) -> QTextCursor """
        return QTextCursor

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setFormat(self, aformat): # real signature unknown; restored from __doc__
        """ setFormat(self, aformat: QTextTableFormat) """
        pass

    def splitCell(self, row, col, numRows, numCols): # real signature unknown; restored from __doc__
        """ splitCell(self, row: int, col: int, numRows: int, numCols: int) """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, doc, QTextDocument=None): # real signature unknown; restored from __doc__
        pass


