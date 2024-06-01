from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import os
import sys
import time
# from main_un import *
# from ceshi_format import *
# from format_tab import *

def start():
    # !/usr/bin/env python
    from PyQt5 import QtCore, QtGui, QtWidgets
    from PyQt5.QtPrintSupport import QPrinter, QPrintDialog, QPrintPreviewDialog

    class ImageViewer(QtWidgets.QMainWindow):
        def __init__(self):
            super(ImageViewer, self).__init__()
            self.imageLabel = QtWidgets.QLabel()
            self.imageLabel.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
            self.imageLabel.setBackgroundRole(QtGui.QPalette.Dark)
            self.imageLabel.setSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
            # self.imageLabel.setSizePolicy(QtWidgets.QSizePolicy.Maximum,QtWidgets.QSizePolicy.Maximum)
            self.imageLabel.setScaledContents(True)
            self.scrollArea = QtWidgets.QScrollArea()
            self.scrollArea.setBackgroundRole(QtGui.QPalette.Dark)
            self.scrollArea.setWidget(self.imageLabel)
            self.setCentralWidget(self.scrollArea)
            self.createActions()
            self.createMenus()

            self.setAcceptDrops(True)  #

            self.setWindowTitle("Picsee")
            self.resize(500, 400)

        def open(self):
            fileName, filetype = QtWidgets.QFileDialog.getOpenFileName(self, "Open File",
                                                                       QtCore.QDir.currentPath())
            if fileName:
                image = QtGui.QImage(fileName)
                if image.isNull():
                    QtWidgets.QMessageBox.information(self, "Picsee",
                                                      "Cannot load %s." % fileName)
                    return
                self.imageLabel.setPixmap(QtGui.QPixmap.fromImage(image))
                self.scaleFactor = 1.0
                self.printAct.setEnabled(True)
                self.fitToWindowAct.setEnabled(True)
                self.updateActions()
                if not self.fitToWindowAct.isChecked():
                    self.imageLabel.adjustSize()

        def dragEnterEvent(self, event):  # 拖动开始时，以及刚进入目标控件时调用
            event.acceptProposedAction()  # 必须要有

        def dropEvent(self, event):
            if event.mimeData().hasUrls():
                urls = event.mimeData().urls()
                try:
                    url = urls[0]
                    fileName = str(url.toLocalFile())
                    if fileName:
                        image = QtGui.QImage(fileName)
                        if image.isNull():
                            QtWidgets.QMessageBox.information(self, "Picsee",
                                                              "Cannot load %s." % fileName)
                            return
                        self.imageLabel.setPixmap(QtGui.QPixmap.fromImage(image))
                        self.scaleFactor = 1.0
                        self.printAct.setEnabled(True)
                        self.fitToWindowAct.setEnabled(True)
                        self.updateActions()
                        if not self.fitToWindowAct.isChecked():
                            self.imageLabel.adjustSize()
                except:
                    pass
            else:
                super(ImageViewer, self).dropEvent(event)

        def handlePrint(self, printer):  # 打印
            painter = QtGui.QPainter(printer)  # 使用painter 绘制文字、pixmap等在printer上
            painter.setRenderHint(QtGui.QPainter.Antialiasing)  # 抗锯齿#可有可无
            pix = self.imageLabel.pixmap()
            size = self.scaleFactor * pix.size()
            painter.drawPixmap(0, 0, size.width(), size.height(), pix)

        def printPreview(self):  # 打印预览
            dialog = QPrintPreviewDialog()
            dialog.paintRequested.connect(self.handlePrint)
            dialog.exec_()

        def print_setup(self):  # 打印，无预览
            printer = QPrinter()
            painter.setRenderHint(QPainter.Antialiasing)  # 抗锯齿
            dialog = QPrintDialog(printer, self)
            if dialog.exec_() == QDialog.Accepted:
                self.handlePrint(printer)

        def zoomIn(self):
            self.scaleImage(1.25)

        def zoomOut(self):
            self.scaleImage(0.8)

        def normalSize(self):
            self.imageLabel.adjustSize()
            self.scaleFactor = 1.0

        def fitToWindow(self):
            fitToWindow = self.fitToWindowAct.isChecked()
            self.scrollArea.setWidgetResizable(fitToWindow)
            if not fitToWindow:
                self.normalSize()
            self.updateActions()

        def about(self):
            QtWidgets.QMessageBox.about(self, "About Picsee",
                                        "For <strong>CMD System</strong> to see images.")

        def createActions(self):
            self.openAct = QtWidgets.QAction("&Open...", self, shortcut="Ctrl+O",
                                             triggered=self.open)
            self.printAct = QtWidgets.QAction("&Print...", self, shortcut="Ctrl+P",
                                              enabled=False, triggered=self.printPreview)
            self.exitAct = QtWidgets.QAction("E&xit", self, shortcut="Ctrl+Q",
                                             triggered=self.close)
            self.zoomInAct = QtWidgets.QAction("Zoom &In (25%)", self,
                                               shortcut="Ctrl++", enabled=False, triggered=self.zoomIn)
            self.zoomOutAct = QtWidgets.QAction("Zoom &Out (25%)", self,
                                                shortcut="Ctrl+-", enabled=False, triggered=self.zoomOut)
            self.normalSizeAct = QtWidgets.QAction("&Normal Size", self,
                                                   shortcut="Ctrl+S", enabled=False, triggered=self.normalSize)
            self.fitToWindowAct = QtWidgets.QAction("&Fit to Window", self,
                                                    enabled=False, checkable=True, shortcut="Ctrl+F",
                                                    triggered=self.fitToWindow)
            self.aboutAct = QtWidgets.QAction("&About", self, triggered=self.about)
            self.aboutQtAct = QtWidgets.QAction("About &Qt", self,
                                                triggered=QtWidgets.qApp.aboutQt)

        def createMenus(self):
            self.fileMenu = QtWidgets.QMenu("&File", self)
            self.fileMenu.addAction(self.openAct)
            self.fileMenu.addAction(self.printAct)
            self.fileMenu.addSeparator()
            self.fileMenu.addAction(self.exitAct)
            self.viewMenu = QtWidgets.QMenu("&View", self)
            self.viewMenu.addAction(self.zoomInAct)
            self.viewMenu.addAction(self.zoomOutAct)
            self.viewMenu.addAction(self.normalSizeAct)
            self.viewMenu.addSeparator()
            self.viewMenu.addAction(self.fitToWindowAct)
            self.helpMenu = QtWidgets.QMenu("&Help", self)
            self.helpMenu.addAction(self.aboutAct)
            self.helpMenu.addAction(self.aboutQtAct)
            self.menuBar().addMenu(self.fileMenu)
            self.menuBar().addMenu(self.viewMenu)
            self.menuBar().addMenu(self.helpMenu)

        def updateActions(self):
            self.zoomInAct.setEnabled(not self.fitToWindowAct.isChecked())
            self.zoomOutAct.setEnabled(not self.fitToWindowAct.isChecked())
            self.normalSizeAct.setEnabled(not self.fitToWindowAct.isChecked())

        def scaleImage(self, factor):
            self.scaleFactor *= factor
            self.imageLabel.resize(self.scaleFactor * self.imageLabel.pixmap().size())
            self.adjustScrollBar(self.scrollArea.horizontalScrollBar(), factor)
            self.adjustScrollBar(self.scrollArea.verticalScrollBar(), factor)
            self.zoomInAct.setEnabled(self.scaleFactor < 3.0)
            self.zoomOutAct.setEnabled(self.scaleFactor > 0.333)

        def adjustScrollBar(self, scrollBar, factor):
            scrollBar.setValue(int(factor * scrollBar.value()
                                   + ((factor - 1) * scrollBar.pageStep() / 2)))
    import sys
    app = QtWidgets.QApplication(sys.argv)
    imageViewer = ImageViewer()
    imageViewer.show()
    sys.exit(app.exec_())