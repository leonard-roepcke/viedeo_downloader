from PyQt5.QtWidgets import (
    QHBoxLayout,
    QVBoxLayout,
    QPushButton,
    QLineEdit,
    QSizePolicy,
    QLabel,
    QWidget,
    QScrollArea,
    QSpacerItem
)
import os
import subprocess
import logic
from threads import DownloadThread
threads = []


# global merken
bottom_layout = None
scroll_content = None

def create_layout(layout):
    global bottom_layout, scroll_content

    # Oberer Streifen
    top_layout = QHBoxLayout()

    link_input = QLineEdit()
    link_input.setPlaceholderText("YouTube-Link hier einfügen...")
    link_input.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

    download_button = QPushButton("Download")
    download_button.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
    download_button.clicked.connect(
        lambda: start_download_and_update(link_input.text())
    )

    top_layout.addWidget(link_input)
    top_layout.addWidget(download_button)

    layout.addLayout(top_layout, stretch=0)

    # Unterer Bereich mit Scroll
    scroll = QScrollArea()
    scroll.setWidgetResizable(True)

    scroll_content = QWidget()
    bottom_layout = QVBoxLayout(scroll_content)

    scroll.setWidget(scroll_content)

    layout.addWidget(scroll, stretch=1)

    update_video_list()


def update_video_list():
    global bottom_layout, scroll_content

    # Alte Einträge löschen
    for i in reversed(range(bottom_layout.count())):
        item = bottom_layout.takeAt(i)
        widget = item.widget()
        if widget:
            widget.deleteLater()
        elif item.layout():
            clear_layout(item.layout())

    dir_path = os.path.dirname(os.path.abspath(__file__))
    videos_path = os.path.join(dir_path, "videos")
    os.makedirs(videos_path, exist_ok=True)

    files = [f for f in os.listdir(videos_path) if f.endswith(".mp4")]

    if not files:
        placeholder = QLabel("Keine Videos gefunden.")
        placeholder.setStyleSheet("color: gray;")
        bottom_layout.addWidget(placeholder)
    else:
        for filename in files:
            file_layout = QHBoxLayout()

            label = QLabel(filename)

            open_button = QPushButton("Open")
            open_button.setFixedWidth(80)

            open_button.clicked.connect(
                lambda checked, f=filename: subprocess.Popen(["xdg-open", os.path.join(videos_path, f)])
            )

            file_layout.addWidget(label)
            file_layout.addSpacerItem(QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))
            file_layout.addWidget(open_button)

            container = QWidget()
            container.setLayout(file_layout)
            bottom_layout.addWidget(container)

    bottom_layout.addStretch()  # schöner Abschluss


def clear_layout(layout):
    while layout.count():
        child = layout.takeAt(0)
        if child.widget():
            child.widget().deleteLater()
        elif child.layout():
            clear_layout(child.layout())


def start_download_and_update(link):
    clean_link = logic.clean_youtube_url(link)
    dir_path = os.path.dirname(os.path.abspath(__file__))
    videos_path = os.path.join(dir_path, "videos")
    os.makedirs(videos_path, exist_ok=True)

    thread = DownloadThread(clean_link, videos_path)
    thread.finished.connect(update_video_list)

    threads.append(thread)  

    thread.start()
