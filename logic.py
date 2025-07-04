import yt_dlp
import os
from urllib.parse import urlparse, parse_qs

import layout_file

def clean_youtube_url(url):
    parsed = urlparse(url)
    query = parse_qs(parsed.query)
    video_id = query.get("v", [None])[0]
    if video_id:
        return f"https://www.youtube.com/watch?v={video_id}"
    return None

def start_download(link):
    print(f"Starting download for: {link}")
    
    dir_path = os.path.dirname(os.path.abspath(__file__))

    # Zielordner: "videos" im gleichen Verzeichnis
    videos_path = os.path.join(dir_path, "videos")

    # Ordner erstellen, falls er nicht existiert
    os.makedirs(videos_path, exist_ok=True)


    # yt-dlp Optionen
    ydl_opts = {
        'outtmpl': os.path.join(videos_path, '%(title)s.%(ext)s'),
        'format': 'bestvideo+bestaudio/best',  # beste Qualität
        'merge_output_format': 'mp4'           # zusammenführen, falls Video+Audio getrennt
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([link])
    
    layout_file.update_video_list()