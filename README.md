# BobYTDL 🎵🎬

**BobYTDL** is a full-stack web application designed for downloading and extracting audio (MP3) and video (MP4) from YouTube URLs. It features a high-performance **FastAPI** backend leveraging **yt-dlp** and **FFmpeg**, alongside a modern **Vue 3** frontend built with **Vite**, **TypeScript**, and **Tailwind CSS**.

---

## ✨ Features

- 🎧 **Audio Extraction**: Download YouTube audio automatically converted to MP3 format (192 kbps).
- 📹 **Video Extraction**: Download YouTube videos merged into high-quality MP4 format.
- ⚡ **Fast & Lightweight**: Asynchronous FastAPI endpoints paired with Vite for near-instant client delivery.
- 🍪 **Cookie Authentication Support**: Integrated `cookies.txt` support to bypass YouTube bot detection and rate limits.
- 🐳 **Docker Containerization**: Full multi-container orchestration using Docker Compose.

---

## 🏗️ Project Architecture

```text
BobYTDL/
├── backend/            # FastAPI Python backend (yt-dlp, FFmpeg integration)
│   ├── extracts/       # Temporary media output directory
│   ├── cookies.txt     # YouTube cookie file for authentication
│   ├── main.py         # API endpoints & extraction logic
│   └── Dockerfile      # Backend Docker image configuration
├── frontend/           # Vue 3 + TypeScript + Vite frontend UI
│   ├── src/            # Vue components, styles & logic
│   └── Dockerfile      # NGINX frontend image configuration
└── docker-compose.yml  # Multi-container orchestration
```

- **[Backend](backend/README.md)**: Handles media download requests using `yt-dlp`, processes audio/video streams, and serves binary downloads via FastAPI.
- **[Frontend](frontend/README.md)**: Provides an interactive interface to input YouTube links and download extracted files.

---

## 🚀 Quick Start with Docker Compose

The simplest way to run the full application stack is using Docker Compose.

### Prerequisites
- [Docker](https://docs.docker.com/get-docker/) & [Docker Compose](https://docs.docker.com/compose/)

### 1. External Docker Network Setup

The `docker-compose.yml` uses an external network named `public-proxy-net`. If it does not exist yet, create it with:

```bash
docker network create public-proxy-net
```

### 2. Environment & Cookie Configuration

Set up the required configuration files before launching:

```bash
# Setup Frontend environment configuration
cp frontend/.env.example frontend/.env

# Setup Backend cookies configuration (recommended for YouTube auth)
cp backend/cookies.txt.example backend/cookies.txt
```

Ensure `frontend/.env` contains the backend API URL:
```env
VITE_API_URL=http://localhost:8001
```

### 3. Start Services

```bash
docker compose up -d --build
```

### 4. Access Services

- **Frontend App**: [http://localhost:8002](http://localhost:8002)
- **Backend API**: [http://localhost:8001](http://localhost:8001)
- **API Docs (Swagger UI)**: [http://localhost:8001/docs](http://localhost:8001/docs)

---

## 🛠️ Local Development (Without Docker)

To run the services locally without Docker:

### Backend Setup
```bash
cd backend
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload --port 8000
```
> **Note**: Ensure **FFmpeg** is installed on your system and available in system `PATH`.
For full backend instructions, see [`backend/README.md`](backend/README.md).

### Frontend Setup
```bash
cd frontend
npm install
npm run dev
```
> **Note**: Ensure `frontend/.env` specifies `VITE_API_URL=http://localhost:8000` when running backend locally.
For full frontend instructions, see [`frontend/README.md`](frontend/README.md).

---

## 📄 License

MIT
