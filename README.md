# BobMP3 🎵🎬

BobMP3 is a web application for extracting audio (MP3) and video (MP4) from YouTube URLs. It features a FastAPI backend utilizing `yt-dlp` and a Vue 3 frontend built with Vite, TypeScript, and Tailwind CSS.

## 🏗️ Project Architecture

```
BobMP3/
├── backend/            # FastAPI Python backend (yt-dlp, FFmpeg integration)
├── frontend/           # Vue 3 + TypeScript + Vite frontend
└── docker-compose.yml  # Container orchestration for production & local setup
```

- **[Backend](backend/README.md)**: Handles media download requests using `yt-dlp`, converts audio/video streams, and returns file downloads via FastAPI.
- **[Frontend](frontend/README.md)**: Provides a minimal user interface to input YouTube links and trigger audio/video downloads.

---

## 🚀 Quick Start with Docker Compose

The easiest way to run the full stack is using Docker Compose.

### Prerequisites
- [Docker](https://docs.docker.com/get-docker/) & [Docker Compose](https://docs.docker.com/compose/)

### 1. Environment & Cookie Configuration

Before launching, set up the necessary environment files:

```bash
# Frontend environment setup
cp frontend/.env.example frontend/.env

# Backend cookies setup (optional, required if YouTube requires auth/cookies)
cp backend/cookies.txt.example backend/cookies.txt
```

Ensure `frontend/.env` contains your backend API URL (e.g., `VITE_API_URL=http://localhost:8001`).

### 2. Start Services

```bash
docker compose up -d --build
```

### 3. Access Services

- **Frontend App**: [http://localhost:8002](http://localhost:8002)
- **Backend API**: [http://localhost:8001](http://localhost:8001)
- **API Docs (Swagger)**: [http://localhost:8001/docs](http://localhost:8001/docs)

---

## 🛠️ Local Development (Without Docker)

To run the services separately without containers:

### Backend Setup
```bash
cd backend
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload --port 8000
```
For detailed backend documentation, see [`backend/README.md`](backend/README.md).

### Frontend Setup
```bash
cd frontend
npm install
npm run dev
```
For detailed frontend documentation, see [`frontend/README.md`](frontend/README.md).

---

## 📄 License

MIT
