# AI Blind Auction Platform

A full-stack web application to host and participate in **blind auctions** with integrated AI-powered features.

## Features

- **User Authentication**: Sign up, sign in, and profile management.
- **Blind Bidding**: Place secret bids on auction items; no one can see others' bids.
- **Auction Management**: Timed auctions, automatic winner reveal, and results.
- **AI Integration**:
  - Starting price suggestion for items.
  - In-app AI assistant for help and suggestions.
- **Real-time Notifications**: Auction updates and results (Socket.IO).
- **Admin Dashboard**: Manage users, auctions, and monitor bids.

---

## Tech Stack

- **Frontend**: React.js
- **Backend**: Node.js, Express.js
- **Database**: MongoDB (with Mongoose)
- **AI Service**: Node/Python microservice (OpenAI API; modular)
- **Deployment**: Docker, docker-compose

---

## Getting Started

### Prerequisites

- Node.js (v18+), npm
- MongoDB (local/cloud)
- Docker & docker-compose (recommended)
- OpenAI API Key (for AI features)

### Run with Docker

```bash
docker-compose up
```

### Run Manually

#### Backend
```bash
cd backend
npm install
npm run dev
```

#### Frontend
```bash
cd frontend
npm install
npm start
```

#### AI Service
(see `ai-service/README.md`)

---

## Folder Structure

- `backend/`: REST API, business logic, data models
- `frontend/`: React SPA client app
- `ai-service/`: AI integration (REST/microservice or scripts)

---

## Free Hosting Recommendations

- **Frontend (React):**
  - [Vercel](https://vercel.com/), [Netlify](https://www.netlify.com/), [GitHub Pages](https://pages.github.com/)
- **Backend (Express/MongoDB):**
  - [Render](https://render.com/), [Railway](https://railway.app/), [Fly.io](https://fly.io/), [MongoDB Atlas](https://www.mongodb.com/atlas/database)
- **AI Service:**
  - [OpenAI](https://platform.openai.com/account/api-keys) (free trial credits)

---

## Deploying for Free

- Deploy frontend on Vercel, Netlify, or GitHub Pages.
- Deploy backend on Render, Railway, or Fly.io (free tier for backend, Atlas for DB).
- Add your OpenAI API Key in backend `.env` to enable AI-powered features.

---

## License

MIT

---

> **Status:** Work-in-progress, see roadmap and open issues for planned features and improvements.