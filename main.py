from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import QWidget, QApplication, QTextEdit, QVBoxLayout, QLineEdit, QMainWindow

class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.setFixedSize(QSize(400, 600))

        self.setWindowTitle("My App")
        self.textedit = QTextEdit()
        
        self.username = QLineEdit()
        self.username.setText('qwerty')
        self.lineedit = QLineEdit()
        #lineedit.setFixedSize(QSize(400, 50))
        self.lineedit.setMaxLength(20)
        self.lineedit.setPlaceholderText("Enter your text")
        
        layout = QVBoxLayout()
        layout.addWidget(self.textedit)
        layout.addWidget(self.username)
        layout.addWidget(self.lineedit)
        self.setLayout(layout)
        #widget.setReadOnly(True) # раскомментируйте, чтобы сделать доступным только для чтения

        self.lineedit.returnPressed.connect(self.return_pressed)
        self.show()
        self.lineedit.setFocus()


    def return_pressed(self):
        print("Return pressed!")
        message = self.username.text() + ': ' + self.lineedit.text()
        self.textedit.append(message)
        self.lineedit.setText("")

app = QApplication([])

window = MainWindow()

app.exec()
