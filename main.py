from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget
import layout_file

def main():
    app = QApplication([])
    window = QMainWindow()
    layout = QVBoxLayout()

    layout_file.create_layout(layout) 

    window.setCentralWidget(QWidget())
    window.centralWidget().setLayout(layout)
    window.show()
    app.exec_()


if __name__ == "__main__":
    main()