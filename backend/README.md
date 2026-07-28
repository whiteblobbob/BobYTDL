# BobMP3 Backend 🐍

The backend service for BobMP3 built with **FastAPI** and **yt-dlp**. It provides RESTful endpoints to process YouTube URLs, extract audio/video streams, and return downloadable files to the frontend.

## 🛠️ Tech Stack

- **Framework**: [FastAPI](https://fastapi.tiangolo.com/)
- **Media Extraction**: [yt-dlp](https://github.com/yt-dlp/yt-dlp)
- **Audio Processing**: [FFmpeg](https://ffmpeg.org/) (for MP3 extraction and encoding)
- **ASGI Server**: [Uvicorn](https://www.uvicorn.org/)

---

## 📋 Prerequisites

- Python **3.10+**
- **FFmpeg** installed and accessible in your system `PATH` (required by `yt-dlp` for audio extraction and video merging)

---

## 🚀 Local Development Setup

### 1. Create and Activate Virtual Environment

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

### 3. Setup Cookies (Optional / Recommended)

To avoid YouTube bot detection or rate limiting, copy the example cookies file and add valid cookies exported from your browser:

```bash
cp cookies.txt.example cookies.txt
```

### 4. Run Development Server

```bash
uvicorn main:app --reload --port 8000
```

The API will be available at [http://localhost:8000](http://localhost:8000). Interactive API docs (Swagger UI) are accessible at [http://localhost:8000/docs](http://localhost:8000/docs).

---

## 📡 API Endpoints

### 1. Extract Audio
- **Endpoint**: `GET /download-audio`
- **Query Parameter**: `url` (string, required) - Full YouTube video URL.
- **Response**: Binary file stream (`audio/mpeg`).
- **Example**:
  ```http
  GET /download-audio?url=https://www.youtube.com/watch?v=dQw4w9WgXcQ
  ```

### 2. Extract Video
- **Endpoint**: `GET /download-video`
- **Query Parameter**: `url` (string, required) - Full YouTube video URL.
- **Response**: Binary file stream (`video/mp4`).
- **Example**:
  ```http
  GET /download-video?url=https://www.youtube.com/watch?v=dQw4w9WgXcQ
  ```

---

## 🐳 Docker Containerization

### Build Image
```bash
docker build -t bobmp3-backend .
```

### Run Container
```bash
docker run -d -p 8000:8000 -v $(pwd)/cookies.txt:/app/cookies.txt bobmp3-backend
```
