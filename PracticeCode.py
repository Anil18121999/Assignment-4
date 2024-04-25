import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLineEdit, QHBoxLayout

class AlphabetKeyboard(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Alphabetic Keyboard')
        self.setGeometry(100, 100, 300, 100)

        main_layout = QVBoxLayout()
        self.setLayout(main_layout)

        self.line_edit = QLineEdit()
        main_layout.addWidget(self.line_edit)

        button_layout = QVBoxLayout()
        main_layout.addLayout(button_layout)

        # Alphabetic and Numerical buttons
        letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
        for letter in letters:
            button = QPushButton(letter)
            button.clicked.connect(self.buttonClicked)
            button_layout.addWidget(button)

    def buttonClicked(self):
        sender = self.sender()
        text = sender.text()
        self.line_edit.insert(text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = AlphabetKeyboard()
    window.show()
    sys.exit(app.exec_())
