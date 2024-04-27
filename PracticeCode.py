# import sys
# from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLineEdit, QHBoxLayout

# class AlphabetKeyboard(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.initUI()

#     def initUI(self):
#         self.setWindowTitle('Alphabetic Keyboard')
#         self.setGeometry(100, 100, 300, 100)

#         main_layout = QVBoxLayout()
#         self.setLayout(main_layout)

#         self.line_edit = QLineEdit()
#         main_layout.addWidget(self.line_edit)

#         button_layout = QVBoxLayout()
#         main_layout.addLayout(button_layout)

#         # Alphabetic and Numerical buttons
#         letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
#         for letter in letters:
#             button = QPushButton(letter)
#             button.clicked.connect(self.buttonClicked)
#             button_layout.addWidget(button)

#     def buttonClicked(self):
#         sender = self.sender()
#         text = sender.text()
#         self.line_edit.insert(text)

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     window = AlphabetKeyboard()
#     window.show()
#     sys.exit(app.exec_())
        # if (self.type_mode == 'numeric'):
                
        #         self.pushButton_2.clicked.connect(lambda _, value = str("1"): self.set_value_to_lineEdit(self.line_edit, value))
        #         self.pushButton_3.clicked.connect(lambda _, value = str("2"): self.set_value_to_lineEdit(self.line_edit, value)) 
        #         self.pushButton_5.clicked.connect(lambda _, value = str("3"): self.set_value_to_lineEdit(self.line_edit, value))
        #         self.pushButton_6.clicked.connect(lambda _, value = str(self.pushButton_6.text()): self.set_value_to_lineEdit(self.line_edit, value))
        #         self.pushButton_7.clicked.connect(lambda _, value = str(self.pushButton_7.text()): self.set_value_to_lineEdit(self.line_edit, value)) 
                # self.pushButton_8.clicked.connect(lambda _, value = str(self.pushButton_8.text()): self.set_value_to_lineEdit(self.line_edit, value)) 
        #         # self.pushButton_9.clicked.connect(lambda _, value = str(self.pushButton_9.text()): self.set_value_to_lineEdit(self.line_edit, value)) 
        #         # self.pushButton_10.clicked.connect(lambda _, value = str(self.pushButton_10.text()): self.set_value_to_lineEdit(self.line_edit, value))
        #         # self.pushButton_11.clicked.connect(lambda _, value = str(self.pushButton_11.text()): self.set_value_to_lineEdit(self.line_edit, value)) 
        #         # self.pushButton_4.clicked.connect(lambda _, value = str(self.pushButton_4.text()): self.set_value_to_lineEdit(self.line_edit, value)) 
        #         # self.pushButton_12.clicked.connect(lambda _, value = str(self.pushButton_12.text()): self.set_value_to_lineEdit(self.line_edit, value)) 
        #         # self.pushButton_13.clicked.connect(lambda _, value = str(self.pushButton_13.text()): self.set_value_to_lineEdit(self.line_edit, value))
        #         # self.pushButton_14.clicked.connect(lambda _, value = str(self.pushButton_14.text()): self.set_value_to_lineEdit(self.line_edit, value)) 
        #         # self.pushButton_15.clicked.connect(lambda _, value = str(self.pushButton_15.text()): self.set_value_to_lineEdit(self.line_edit, value)) 
        #         # self.pushButton_16.clicked.connect(lambda _, value = str(self.pushButton_16.text()): self.set_value_to_lineEdit(self.line_edit, value)) 
        #         # self.pushButton_17.clicked.connect(lambda _, value = str(self.pushButton_17.text()): self.set_value_to_lineEdit(self.line_edit, value))
        #         # self.pushButton_18.clicked.connect(lambda _, value = str(self.pushButton_18.text()): self.set_value_to_lineEdit(self.line_edit, value)) 
        #         # self.pushButton_19.clicked.connect(lambda _, value = str(self.pushButton_19.text()): self.set_value_to_lineEdit(self.line_edit, value)) 
        #         # self.pushButton_20.clicked.connect(lambda _, value = str(self.pushButton_20.text()): self.set_value_to_lineEdit(self.line_edit, value)) 
        #         # self.pushButton_22.clicked.connect(lambda _, value = str(self.pushButton_22.text()): self.set_value_to_lineEdit(self.line_edit, value))
        #         # self.pushButton_23.clicked.connect(lambda _, value = str(self.pushButton_23.text()): self.set_value_to_lineEdit(self.line_edit, value)) 
        #         # self.pushButton_24.clicked.connect(lambda _, value = str(self.pushButton_24.text()): self.set_value_to_lineEdit(self.line_edit, value)) 
        #         # self.pushButton_25.clicked.connect(lambda _, value = str(self.pushButton_25.text()): self.set_value_to_lineEdit(self.line_edit, value)) 
        #         # self.pushButton_26.clicked.connect(lambda _, value = str(self.pushButton_26.text()): self.set_value_to_lineEdit(self.line_edit, value))
        #         # self.pushButton_27.clicked.connect(lambda _, value = str(self.pushButton_27.text()): self.set_value_to_lineEdit(self.line_edit, value)) 
        #         # self.pushButton_28.clicked.connect(lambda _, value = str(self.pushButton_28.text()): self.set_value_to_lineEdit(self.line_edit, value))
        # elif( self.type_mode == 'capital'):
        #         print("elif of capital")
        #         self.pushButton_2.clicked.connect(lambda _, value = str("Q"): self.set_value_to_lineEdit(self.line_edit, value))
        #         self.pushButton_3.clicked.connect(lambda _, value = str("W"): self.set_value_to_lineEdit(self.line_edit, value)) 
        #         self.pushButton_5.clicked.connect(lambda _, value = str("E"): self.set_value_to_lineEdit(self.line_edit, value))
        #         self.pushButton_6.clicked.connect(lambda _, value = str(self.pushButton_6.text()): self.set_value_to_lineEdit(self.line_edit, value))
        #         self.pushButton_7.clicked.connect(lambda _, value = str(self.pushButton_7.text()): self.set_value_to_lineEdit(self.line_edit, value)) 
        #         self.pushButton_8.clicked.connect(lambda _, value = str(self.pushButton_8.text()): self.set_value_to_lineEdit(self.line_edit, value)) 
        #         # self.pushButton_9.clicked.connect(lambda _, value = str(self.pushButton_9.text()): self.set_value_to_lineEdit(self.line_edit, value)) 
        #         # self.pushButton_10.clicked.connect(lambda _, value = str(self.pushButton_10.text()): self.set_value_to_lineEdit(self.line_edit, value))
        #         # self.pushButton_11.clicked.connect(lambda _, value = str(self.pushButton_11.text()): self.set_value_to_lineEdit(self.line_edit, value)) 
        #         # self.pushButton_4.clicked.connect(lambda _, value = str(self.pushButton_4.text()): self.set_value_to_lineEdit(self.line_edit, value)) 
        #         # self.pushButton_12.clicked.connect(lambda _, value = str(self.pushButton_12.text()): self.set_value_to_lineEdit(self.line_edit, value)) 
        #         # self.pushButton_13.clicked.connect(lambda _, value = str(self.pushButton_13.text()): self.set_value_to_lineEdit(self.line_edit, value))
        #         # self.pushButton_14.clicked.connect(lambda _, value = str(self.pushButton_14.text()): self.set_value_to_lineEdit(self.line_edit, value)) 
        #         # self.pushButton_15.clicked.connect(lambda _, value = str(self.pushButton_15.text()): self.set_value_to_lineEdit(self.line_edit, value)) 
        #         # self.pushButton_16.clicked.connect(lambda _, value = str(self.pushButton_16.text()): self.set_value_to_lineEdit(self.line_edit, value)) 
        #         # self.pushButton_17.clicked.connect(lambda _, value = str(self.pushButton_17.text()): self.set_value_to_lineEdit(self.line_edit, value))
        #         # self.pushButton_18.clicked.connect(lambda _, value = str(self.pushButton_18.text()): self.set_value_to_lineEdit(self.line_edit, value)) 
        #         # self.pushButton_19.clicked.connect(lambda _, value = str(self.pushButton_19.text()): self.set_value_to_lineEdit(self.line_edit, value)) 
        #         # self.pushButton_20.clicked.connect(lambda _, value = str(self.pushButton_20.text()): self.set_value_to_lineEdit(self.line_edit, value)) 
        #         # self.pushButton_22.clicked.connect(lambda _, value = str(self.pushButton_22.text()): self.set_value_to_lineEdit(self.line_edit, value))
        #         # self.pushButton_23.clicked.connect(lambda _, value = str(self.pushButton_23.text()): self.set_value_to_lineEdit(self.line_edit, value)) 
        #         # self.pushButton_24.clicked.connect(lambda _, value = str(self.pushButton_24.text()): self.set_value_to_lineEdit(self.line_edit, value)) 
        #         # self.pushButton_25.clicked.connect(lambda _, value = str(self.pushButton_25.text()): self.set_value_to_lineEdit(self.line_edit, value)) 
        #         # self.pushButton_26.clicked.connect(lambda _, value = str(self.pushButton_26.text()): self.set_value_to_lineEdit(self.line_edit, value))
        #         # self.pushButton_27.clicked.connect(lambda _, value = str(self.pushButton_27.text()): self.set_value_to_lineEdit(self.line_edit, value)) 
        
        #         # self.pushButton_28.clicked.connect(lambda _, value = str(self.pushButton_28.text()): self.set_value_to_lineEdit(self.line_edit, value))
        # elif( self.type_mode == 'small'):
        #         self.pushButton_2.clicked.connect(lambda _, value = str("q"): self.set_value_to_lineEdit(self.line_edit, value))
        #         self.pushButton_3.clicked.connect(lambda _, value = str("w"): self.set_value_to_lineEdit(self.line_edit, value)) 
        #         self.pushButton_5.clicked.connect(lambda _, value = str("e"): self.set_value_to_lineEdit(self.line_edit, value))        
        # else:
        #      print("mode not valide")    
        # for button in self.buttons():
        #         button.clicked.connect(lambda _, value = str(button.text()): self.set_value_to_lineEdit(self.line_edit, value))
        #         print("button value :" + str(button.text()))
                # button.clicked.connect(functools.partial(self.set_value_to_lineEdit, self.line_edit, button.text()))
# import sys
# from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit


# class VirtualKeyboard(QWidget):
#     def __init__(self):
#         super().__init__()

#         self.setWindowTitle('Virtual Keyboard')
#         self.setGeometry(100, 100, 400, 200)

#         self.uppercase_mode = False  # Track uppercase mode

#         self.layout = QVBoxLayout()

#         self.line_edit = QLineEdit()
#         self.layout.addWidget(self.line_edit)

#         self.keyboard_layout = QVBoxLayout()

#         self.row_layouts = []  # Store row layouts

#         self.create_keyboard_row('1234567890')
#         self.create_keyboard_row('qwertyuiop')
#         self.create_keyboard_row('asdfghjkl')
#         self.create_keyboard_row('zxcvbnm')

#         self.switch_case_button = QPushButton('caps')
#         self.switch_case_button.clicked.connect(self.switch_case)
#         self.keyboard_layout.addWidget(self.switch_case_button)

#         self.layout.addLayout(self.keyboard_layout)
#         self.setLayout(self.layout)

#     def create_keyboard_row(self, characters):
#         row_layout = QHBoxLayout()
#         self.row_layouts.append(row_layout)  # Add row layout to list
#         for char in characters:
#             button = QPushButton(char)
#             button.clicked.connect(lambda _, ch=char: self.add_to_line_edit(ch.upper() if self.uppercase_mode else ch.lower()))
#             row_layout.addWidget(button)
#         self.keyboard_layout.addLayout(row_layout)

#     def add_to_line_edit(self, text):
#         self.line_edit.setText(self.line_edit.text() + text)

#     def switch_case(self):
#         # Toggle uppercase mode
#         self.uppercase_mode = not self.uppercase_mode
#         if self.uppercase_mode:
#             self.switch_case_button.setText('CAPS')
#             self.update_button_texts(lambda ch: ch.upper())
#         else:
#             self.switch_case_button.setText('caps')
#             self.update_button_texts(lambda ch: ch.lower())

#     def update_button_texts(self, transformation):
#         # Update text of all buttons according to transformation function
#         for row_layout in self.row_layouts:
#             if row_layout is not None:
#                 for button_index in range(row_layout.count()):
#                     button = row_layout.itemAt(button_index).widget()
#                     button.setText(transformation(button.text()))


# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     window = VirtualKeyboard()
#     window.show()
#     sys.exit(app.exec_())




from PyQt5.QtWidgets import QApplication, QWidget, QPushButton

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 300, 200)
        self.setWindowTitle('Button Text Example')

        self.button = QPushButton('Initial Text', self)
        self.button2 = QPushButton('2222Initial Text', self)
        self.button.clicked.connect(self.changeText)

    def changeText(self):
        # Disconnect the existing connection before changing the text
        self.button.clicked.disconnect(self.changeText)
        
        self.button.setText('New Text')
        current_text = self.button.text()
        print("Current Button Text:", current_text)
        
        # Reconnect the signal for future clicks
        self.button.clicked.connect(self.changeText)

def main():
    app = QApplication([])
    widget = MyWidget()
    widget.show()
    app.exec_()

if __name__ == '__main__':
    main()
