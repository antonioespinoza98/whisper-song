import os
import subprocess
from typing import Union
import yt_dlp as youtube_dl

def download_audio(url: Union[str, None], savePath: Union[str, None]):
    if not url:
        raise ValueError("URL is required")
    if not savePath:
        raise ValueError("Save path is required")
    
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': savePath,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    
    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
    except youtube_dl.utils.DownloadError as e:
        raise RuntimeError(f"Error during audio download: {e}")



def extract_audio(url: Union[str, None],
                   ExecPath: Union[str, None],
                     savePath: Union[str, None]):
    
    if not url:
        raise ValueError("URL is required")
    if not savePath:
        raise ValueError("Save path is required")
    
    else:
        try:
            command = [
                ExecPath,
                '-i', url, # input file
                '-q:a', '0', # audio quality
                '-map', 'a', # audio only
                savePath
            ]

            subprocess.run(command, check=True)

        except subprocess.CalledProcessError as e:
            raise RuntimeError(f"Error during audio extraction: {e}")
        

def convert(exec_path: Union[str, None],
            wav_file: Union[str, None],
              mp3_file: Union[str, None]):
    
    # ffmpeg command to convert WAV to MP3
    command = [exec_path, "-i", wav_file, "-q:a", "0", mp3_file]
    subprocess.run(command, check=True)


