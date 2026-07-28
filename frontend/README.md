# BobYTDL Frontend ⚡

The client web interface for **BobYTDL**, built with **Vue 3**, **TypeScript**, **Vite**, and **Tailwind CSS**.

---

## 🛠️ Tech Stack

- **Framework**: [Vue 3](https://vuejs.org/) (Composition API with `<script setup>`)
- **Build Tool**: [Vite](https://vite.dev/)
- **Language**: [TypeScript](https://www.typescriptlang.org/)
- **Styling**: [Tailwind CSS v4](https://tailwindcss.com/)
- **State Management**: [Pinia](https://pinia.vuejs.org/)

---

## 📁 Directory Structure

```text
frontend/
├── public/              # Static public assets
├── src/
│   ├── App.vue          # Main download interface component
│   ├── main.ts          # Application entrypoint & Pinia state initialization
│   └── assets/          # Component stylesheets & design assets
├── .env.example         # Environment template (API URL setup)
├── Dockerfile           # Multi-stage NGINX production container configuration
├── package.json         # Dependencies & package scripts
├── tsconfig.json        # TypeScript configuration
└── vite.config.ts       # Vite build & plugin settings
```

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

Copy the example environment file and set the backend API endpoint:

```bash
cp .env.example .env
```

Set the target API URL in `.env`:
```env
VITE_API_URL=http://localhost:8001
```

> For standalone local backend development without Docker, set `VITE_API_URL=http://localhost:8000`.

### 3. Start Development Server

Launch Vite development server with Hot Module Replacement (HMR):

```bash
npm run dev
```

The application will be accessible at [http://localhost:5173](http://localhost:5173) (or the port specified by Vite).

---

## 📜 Available Scripts

| Command | Description |
| :--- | :--- |
| `npm run dev` | Starts local Vite development server |
| `npm run build` | Runs TypeScript checks and builds production bundle into `dist/` |
| `npm run preview` | Previews the compiled production build locally |
| `npm run type-check` | Runs `vue-tsc` for strict type checking |
| `npm run lint` | Runs combined code quality linter (`oxlint` & `eslint`) |
| `npm run format` | Formats source code with `oxfmt` |

---

## 🐳 Standalone Docker Deployment

### Build Image
```bash
docker build -t bobytdl-frontend .
```

### Run Container
```bash
docker run -d -p 8002:80 --env-file .env bobytdl-frontend
```

