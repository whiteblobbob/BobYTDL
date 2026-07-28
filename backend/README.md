# BobYTDL Backend 🐍

The backend service for **BobYTDL** is built with **FastAPI** and **yt-dlp**. It provides RESTful endpoints to process YouTube URLs, extract high-quality audio and video streams, and stream downloadable binary responses back to the client.

---

## 🛠️ Tech Stack

- **Framework**: [FastAPI](https://fastapi.tiangolo.com/)
- **Media Extraction**: [yt-dlp](https://github.com/yt-dlp/yt-dlp)
- **Audio/Video Processing**: [FFmpeg](https://ffmpeg.org/) (for MP3 audio conversion and MP4 video format merging)
- **ASGI Server**: [Uvicorn](https://www.uvicorn.org/)

---

## 📁 Directory Structure

```text
backend/
├── extracts/            # Output folder storing extracted MP3/MP4 files
├── cookies.txt          # Netscape YouTube cookies file (auth/rate-limit bypass)
├── cookies.txt.example  # Template for cookies configuration
├── Dockerfile           # Docker container configuration with FFmpeg preinstalled
├── main.py              # FastAPI endpoints & yt-dlp handlers
└── requirements.txt     # Python dependencies
```

---

## 📋 Prerequisites

- Python **3.10+**
- **FFmpeg** installed and accessible in system `PATH` (required by `yt-dlp` for audio extraction and format merging)
  - **Ubuntu/Debian**: `sudo apt update && sudo apt install -y ffmpeg`
  - **macOS**: `brew install ffmpeg`
  - **Windows**: Install via `winget install FFmpeg` or download from official website and add to System Environment Variables (`PATH`).

---

## 🚀 Local Development Setup

### 1. Create & Activate Virtual Environment

```bash
cd backend
python -m venv .venv

# On Linux/macOS:
source .venv/bin/activate

# On Windows:
.venv\Scripts\activate
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure Cookies (Recommended)

To prevent YouTube bot detection (`Sign in to confirm you’re not a bot`), copy the template and export your YouTube cookies:

```bash
cp cookies.txt.example cookies.txt
```

> Learn more about exporting cookies using browser extensions like *Get cookies.txt LOCALLY* or via `yt-dlp` documentation.

### 4. Run Development Server

```bash
uvicorn main:app --reload --port 8000
```

- API Base URL: [http://localhost:8000](http://localhost:8000)
- Interactive API Docs (Swagger UI): [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 📡 API Endpoints

### 1. Extract Audio
- **Endpoint**: `GET /download-audio`
- **Query Parameter**: `url` (string, required) - Full YouTube video URL.
- **Response**: Binary file stream (`audio/mpeg`).
- **Response Header**: `Content-Disposition: attachment; filename*=utf-8''<Filename>.mp3`
- **Example**:
  ```http
  GET /download-audio?url=https://www.youtube.com/watch?v=dQw4w9WgXcQ
  ```

### 2. Extract Video
- **Endpoint**: `GET /download-video`
- **Query Parameter**: `url` (string, required) - Full YouTube video URL.
- **Response**: Binary file stream (`video/mp4`).
- **Response Header**: `Content-Disposition: attachment; filename*=utf-8''<Filename>.mp4`
- **Example**:
  ```http
  GET /download-video?url=https://www.youtube.com/watch?v=dQw4w9WgXcQ
  ```

---

## 🐳 Standalone Docker Containerization

### Build Image
```bash
docker build -t bobytdl-backend .
```

### Run Container
```bash
docker run -d -p 8000:8000 -v $(pwd)/cookies.txt:/app/cookies.txt bobytdl-backend
```

