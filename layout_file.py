from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QHBoxLayout
def create_layout(layout):
    layout_2 = QHBoxLayout()
    layout_2.addWidget(QPushButton("Hi"))
    layout_2.addWidget(QPushButton("Hello"))

    layout.addLayout(layout_2)
    layout.addWidget(QPushButton("Hi"))
