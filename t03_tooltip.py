#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import (QWidget, QToolTip, QPushButton, QDesktopWidget, QMessageBox, QApplication)
from PyQt5.QtGui import QFont    
from PyQt5.QtCore import QCoreApplication

# PyQt5チュートリアル日本語まとめ
# https://qiita.com/puuuii/items/92c0c8195aafe5904ab2


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        QToolTip.setFont(QFont("SansSerif", 10))

        self.setToolTip('This is a <b>QWidget</b> widget')

        btn = QPushButton('Button', self)
        btn.setToolTip('This is a <b>QPushButton</b> widget')
        btn.clicked.connect(QCoreApplication.instance().quit)
        btn.resize(btn.sizeHint())
        btn.move(50, 50)

        self.resize(300, 200)
        self.center()

        self.setWindowTitle('Tooltips')
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Message',
                                     "Are you sure to quit?", QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

