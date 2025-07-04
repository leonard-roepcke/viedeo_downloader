from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget
import layout_file

def main():
    app = QApplication([])
    window = QMainWindow()
    window.setWindowTitle("Youtube Downloader")
    window.setGeometry(100, 100, 800, 600)
    layout = QVBoxLayout()
    layout_file.create_layout(layout) 
    
    container = QWidget()
    container.setLayout(layout)

    

    window.setCentralWidget(container)
    window.show()
    app.exec_()


if __name__ == "__main__":
    main()