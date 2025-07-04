from pytube import YouTube
import os

def start_download(link):
    # Hier kommt die Logik für den Download
    yt = YouTube(link)
    stream = yt.streams.get_highest_resolution()
    dir_path = os.path.dirname(os.path.abspath(__file__))
    stream.download(output_path=dir_path, filename=yt.title + '.mp4')