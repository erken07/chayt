from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import QWidget, QApplication, QTextEdit, QVBoxLayout, QLineEdit, QMainWindow

class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.setFixedSize(QSize(400, 600))

        self.setWindowTitle("My App")
        self.textedit = QTextEdit()
        #textedit.setFixedSize(QSize(400, 300))
        self.lineedit = QLineEdit()
        #lineedit.setFixedSize(QSize(400, 50))
        self.lineedit.setMaxLength(20)
        self.lineedit.setPlaceholderText("Enter your text")
        layout = QVBoxLayout()
        layout.addWidget(self.textedit)
        layout.addWidget(self.lineedit)
        self.setLayout(layout)
        #widget.setReadOnly(True) # раскомментируйте, чтобы сделать доступным только для чтения

        self.lineedit.returnPressed.connect(self.return_pressed)
        self.lineedit.selectionChanged.connect(self.selection_changed)
        self.lineedit.textChanged.connect(self.text_changed)
        self.lineedit.textEdited.connect(self.text_edited)

        #self.setCentralWidget(self.lineedit)
        self.show()


    def return_pressed(self):
        print("Return pressed!")
        self.textedit.setText("BOOM!")

    def selection_changed(self):
        print("Selection changed")
        print(self.textedit.selectedText())

    def text_changed(self, s):
        print("Text changed...")
        print(s)

    def text_edited(self, s):
        print("Text edited...")
        print(s)

app = QApplication([])

window = MainWindow()

app.exec()
