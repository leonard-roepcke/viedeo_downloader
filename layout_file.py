from PyQt5.QtWidgets import (
    QHBoxLayout,
    QVBoxLayout,
    QPushButton,
    QLineEdit,
    QSizePolicy,
    QLabel
)
import os
import subprocess
import logic  # deine Logik

# Wir speichern das Layout global, damit du es immer wieder updaten kannst
bottom_layout = None

def create_layout(layout):
    global bottom_layout  # wichtig: global merken!

    # Oberer Streifen (Suchleiste + Button)
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

    # Unterer Bereich (initial leer, wird später befüllt)
    bottom_layout = QVBoxLayout()

    # Gesamtlayout zusammensetzen
    layout.addLayout(top_layout, stretch=0)
    layout.addLayout(bottom_layout, stretch=1)

    # Erste Befüllung
    update_video_list()

def update_video_list():
    global bottom_layout

    # Vorherige Widgets entfernen
    while bottom_layout.count():
        child = bottom_layout.takeAt(0)
        if child.widget():
            child.widget().deleteLater()
        elif child.layout():
            clear_layout(child.layout())

    # Neuen Inhalt aufbauen
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

            open_button.clicked.connect(
                lambda checked, f=filename: subprocess.Popen(["xdg-open", os.path.join(videos_path, f)])
            )

            file_layout.addWidget(label)
            file_layout.addWidget(open_button)

            bottom_layout.addLayout(file_layout)

def clear_layout(layout):
    while layout.count():
        child = layout.takeAt(0)
        if child.widget():
            child.widget().deleteLater()
        elif child.layout():
            clear_layout(child.layout())

# Hilfsfunktion: Download + Liste aktualisieren
def start_download_and_update(link):
    clean_link = logic.clean_youtube_url(link)
    logic.start_download(clean_link)
    update_video_list()
