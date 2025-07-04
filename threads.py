from PyQt5.QtCore import QThread, pyqtSignal
import os
import yt_dlp

class DownloadThread(QThread):
    finished = pyqtSignal()

    def __init__(self, link, output_path):
        super().__init__()
        self.link = link
        self.output_path = output_path

    def run(self):
        # Hier läuft dein Download im Hintergrund-Thread
        ydl_opts = {
            'outtmpl': os.path.join(self.output_path, '%(title)s.%(ext)s'),
            'format': 'bestvideo+bestaudio/best',
            'merge_output_format': 'mp4',
            'noplaylist': True,
            'concurrent_fragment_downloads': 1 
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([self.link])

        # Signal: Download abgeschlossen
        self.finished.emit()
