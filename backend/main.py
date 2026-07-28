import yt_dlp
import typing
import os
from pathlib import Path
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from fastapi.responses import FileResponse

def download_video(url: str):
    with yt_dlp.YoutubeDL({
        "cookiefile": "cookies.txt",
        "outtmpl": "./extracts/%(title)s.%(ext)s",  # absolute path avoids permission issues
        "format": "bestvideo[vcodec^=avc]+bestaudio/best",
        "merge_output_format": "mp4",
    }) as ydl:
        return ydl.extract_info(url)

def download_audio(url: str):
    with yt_dlp.YoutubeDL({
        "cookiefile": "cookies.txt",
        "outtmpl": "./extracts/%(title)s.%(ext)s",  # absolute path avoids permission issues
        "format": "bestaudio/best",            # explicitly request audio
        "postprocessors": [{
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": "192",
        }],
    }) as ydl:
        return ydl.extract_info(url)

Path("./extracts/").mkdir(parents=True, exist_ok=True)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # restrict this to your frontend URL in production
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["Content-Disposition"],  # add this
)

@app.get("/download-audio")
async def get_download_audio(url: str):
    raw_info: typing.Any = download_audio(url)
    info = raw_info['requested_downloads'][0]  # fix: use the query param, not a hardcoded URL
    path = info["filepath"]
    filename = os.path.basename(path)

    return FileResponse(path, media_type="audio/mpeg", filename=filename)

@app.get("/download-video")
async def get_download_video(url: str):
    raw_info: typing.Any = download_video(url)
    info = raw_info['requested_downloads'][0]  # fix: use the query param, not a hardcoded URL
    path = info["filepath"]
    filename = os.path.basename(path)

    return FileResponse(path, media_type="video/mp4", filename=filename)