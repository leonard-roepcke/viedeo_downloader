from PyQt5.QtWidgets import (
    QHBoxLayout,
    QVBoxLayout,
    QPushButton,
    QLineEdit,
    QSizePolicy,
    QWidget,
    QLabel
)
import logic  # Importiere die Logik für den Download

def create_layout(layout):
    # Oberer Streifen (Suchleiste + Button)
    top_layout = QHBoxLayout()

    # Eingabefeld für YouTube-Link
    link_input = QLineEdit()
    link_input.setPlaceholderText("YouTube-Link hier einfügen...")
    link_input.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

    # Download-Button
    download_button = QPushButton("Download")
    download_button.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
    download_button.clicked.connect(lambda: logic.start_download(logic.clean_youtube_url(link_input.text())))

    top_layout.addWidget(link_input)
    top_layout.addWidget(download_button)

    # Unterer Bereich (Platzhalter)
    bottom_layout = QVBoxLayout()
    placeholder = QLabel("Hier kommt später dein Download-Status hin.")
    placeholder.setStyleSheet("color: gray;")
    bottom_layout.addStretch()
    bottom_layout.addWidget(placeholder)
    bottom_layout.addStretch()

    # Gesamtlayout zusammensetzen
    layout.addLayout(top_layout, stretch=0)   # Oberer Streifen nimmt so viel Platz wie nötig
    layout.addLayout(bottom_layout, stretch=1)  # Unterer Teil füllt den Rest
