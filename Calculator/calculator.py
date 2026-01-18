import sys
from functools import partial

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QGridLayout, QLabel, QPushButton, QWidget


class Calculator(QWidget):
    def __init__(self):
        super().__init__()

        self.buttons = [
            ["1", "2", "3", "C"],
            ["4", "5", "6", "D"],
            ["7", "8", "9", "/"],
            [".", "0", "*", "%"],
            ["^", "+", "-", "="],
        ]

        self.layout1 = QGridLayout()

        self.label = QLabel("0")
        self.label.setFont(QFont("IBM Plex Mono", 18))
        self.label.setFixedWidth(650)
        self.label.setFixedHeight(100)
        self.label.setStyleSheet("border: 2px solid #666;")
        self.label.setAlignment(
            Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter
        )
        self.layout1.addWidget(self.label, 0, 0, 1, 4)

        self.add_buttons()
        self.numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
        self.operators = ["+", "-", "*", "/", "%", "^", "="]

        self.setLayout(self.layout1)
        self.show()

    def add_buttons(self):
        for i in range(len(self.buttons)):
            for j in range(len(self.buttons[i])):
                btn_text = self.buttons[i][j]
                btn = QPushButton(btn_text)
                btn.setFont(QFont("IBM Plex Mono", 14))
                btn.clicked.connect(partial(self.button_click_event, btn_text))
                self.layout1.addWidget(btn, i + 1, j)

    def button_click_event(self, btn_text):
        old_text = self.label.text()
        if old_text == "0":
            old_text = ""
        new_text = ""
        if btn_text in self.numbers:
            new_text = old_text + btn_text
        if btn_text in self.operators:
            if old_text[-1] in self.operators:
                new_text = old_text[:-1] + btn_text
            else:
                new_text = old_text + btn_text
        if btn_text == ".":
            if old_text[-1] in self.numbers:
                new_text = old_text + btn_text
            elif old_text[-1] in self.operators:
                new_text = old_text + "0."
            elif old_text[-1] == ".":
                new_text = old_text
        if btn_text == "C":
            new_text = ""
        if btn_text == "D":
            new_text = old_text[:-1]
        if new_text == "":
            new_text = "0"
        if btn_text == "=":
            new_text = new_text.replace("=", "")
            new_text = new_text.replace("^", "**")
            new_text = str(eval(new_text))
        self.label.setText(new_text)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Calculator()
    sys.exit(app.exec_())