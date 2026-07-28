# BobMP3 Frontend ⚡

The user interface for **BobMP3**, built with **Vue 3**, **TypeScript**, **Vite**, and **Tailwind CSS**.

## 🛠️ Tech Stack

- **Framework**: [Vue 3](https://vuejs.org/) (Composition API with `<script setup>`)
- **Build Tool**: [Vite](https://vite.dev/)
- **Language**: [TypeScript](https://www.typescriptlang.org/)
- **Styling**: [Tailwind CSS v4](https://tailwindcss.com/)
- **State Management**: [Pinia](https://pinia.vuejs.org/)

---

## 📋 Prerequisites

- **Node.js**: `^20.19.0` or `>=22.12.0`
- **npm**: `v10+`

---

## 🚀 Getting Started

### 1. Install Dependencies

```bash
cd frontend
npm install
```

### 2. Environment Configuration

Copy the example environment file and configure the backend URL:

```bash
cp .env.example .env
```

Ensure `.env` contains:
```env
VITE_API_URL=http://localhost:8001
```

### 3. Development Server

Start Vite dev server with hot-reload:

```bash
npm run dev
```

The application will be accessible at [http://localhost:5173](http://localhost:5173).

---

## 📜 Available Scripts

| Command | Description |
| :--- | :--- |
| `npm run dev` | Starts local development server |
| `npm run build` | Runs type checks and builds production bundle in `dist/` |
| `npm run preview` | Previews production build locally |
| `npm run type-check` | Runs `vue-tsc` for type checking |
| `npm run lint` | Runs linter checks (`oxlint` & `eslint`) |
| `npm run format` | Formats code with `oxfmt` |

---

## 🐳 Docker Deployment

### Build Image
```bash
docker build -t bobmp3-frontend .
```

### Run Container
```bash
docker run -d -p 8002:80 --env-file .env bobmp3-frontend
```
