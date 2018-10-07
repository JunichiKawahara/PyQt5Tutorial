#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QMainWindow, QMenu, QAction, qApp, QApplication
from PyQt5.QtGui import QIcon

# PyQt5チュートリアル日本語まとめ
# https://qiita.com/puuuii/items/b2a368bab2d6d6eae584


class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        # Status Bar
        self.statusbar = self.statusBar()
        self.statusbar.showMessage('Ready')

        # Simple Menu
        exitAct = QAction(QIcon('exit.png'), '&Exit', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip('Exit application')
        exitAct.triggered.connect(qApp.quit)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAct)

        #Sub Menu
        impMenu = QMenu('Import', self)
        impAct = QAction('Import mail', self)
        impMenu.addAction(impAct)

        newAct = QAction('New', self)

        fileMenu.addAction(newAct)
        fileMenu.addMenu(impMenu)

        # Check Menu
        viewMenu = menubar.addMenu('View')

        viewStatAct = QAction('View statusbar', self)
        viewStatAct.setCheckable(True)
        viewStatAct.setStatusTip('View statusbar')
        viewStatAct.setChecked(True)
        viewStatAct.toggled.connect(self.toggleMenu)

        viewMenu.addAction(viewStatAct)

        # Toolbar
        self.toolbar = self.addToolBar('Exit')
        self.toolbar.addAction(exitAct)

        # 表示
        self.setGeometry(300, 300, 350, 150)
        self.setWindowTitle('Statusbar')
        self.show()

    def toggleMenu(self, state):
        if state:
            self.statusbar.show()
        else:
            self.statusbar.hide()

    def contextMenuEvent(self, event):
        cmenu = QMenu(self)

        newAct = cmenu.addAction("New")
        opnAct = cmenu.addAction("Open")
        quitAct = cmenu.addAction("Quit")
        action = cmenu.exec_(self.mapToGlobal(event.pos()))

        if action == quitAct:
            qApp.quit()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
