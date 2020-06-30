# coding=utf-8

import random
import base64
import static.logo
from PyQt5.QtGui import (
    QIcon,
    QPixmap,
)
from PyQt5.QtWidgets import (
    QMainWindow,
    QWidget,
    QGridLayout,
    QPushButton,
    QPlainTextEdit,
    QLabel,
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.namePool = QPlainTextEdit(self)
        self.itemPool = QPlainTextEdit(self)
        self.result = QPlainTextEdit(self)

        self.nameLabel = QLabel("Name", self.namePool)
        self.itemLabel = QLabel("Item", self.itemPool)
        self.resultLabel = QLabel("Result", self.itemPool)

        self.lotteryButton = QPushButton("Start", self)

        self.init_ui()

    def init_ui(self):
        self.lotteryButton.clicked.connect(self.gen)

        grid = QGridLayout()
        grid.addWidget(self.nameLabel, 1, 0)
        grid.addWidget(self.itemLabel, 1, 1)
        grid.addWidget(self.namePool, 2, 0)
        grid.addWidget(self.itemPool, 2, 1)
        grid.addWidget(self.resultLabel, 3, 0)
        grid.addWidget(self.lotteryButton, 3, 1)
        grid.addWidget(self.result, 4, 0, 1, 2)

        widget = QWidget(self)
        widget.setLayout(grid)
        self.setCentralWidget(widget)

        rawimg = base64.b64decode(static.logo.icon)
        pix = QPixmap()
        pix.loadFromData(rawimg)
        icon = QIcon()
        icon.addPixmap(pix, QIcon.Normal, QIcon.Off)
        self.setWindowIcon(icon)
        self.setWindowTitle("EzLottery")
        self.statusBar().showMessage("Ready")

    def gen(self):
        nameList = list(filter(None, self.namePool.toPlainText().split("\n")))
        itemList = list(filter(None, self.itemPool.toPlainText().split("\n")))

        random.shuffle(nameList)
        random.shuffle(itemList)
        print(nameList, itemList)

        res = ""
        for i in range(0, min([len(nameList), len(itemList)])):
            res += nameList[i] + " " + itemList[i] + "\n"
        self.result.setPlainText(res)

        self.statusBar().showMessage("Generated")
