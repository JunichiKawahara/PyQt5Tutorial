#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QWidget

# PyQt5チュートリアル日本語まとめ
# https://qiita.com/puuuii/items/92c0c8195aafe5904ab2

if __name__ == '__main__':

    app = QApplication(sys.argv)

    w = QWidget()
    w.resize(250, 150)
    w.move(300, 300)
    w.setWindowTitle('Simple')
    w.show()

    sys.exit(app.exec_())
