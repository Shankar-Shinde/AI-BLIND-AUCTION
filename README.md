# AI Blind Auction

A simple web-based blind auction application with AI-powered bid suggestions. Built with Flask (Python) and deployed on Render.

## Live Demo
Visit the live app: [https://ai-blind-auction.onrender.com/](https://ai-blind-auction.onrender.com/)

## Features
- Create blind auctions for items.
- Place anonymous bids.
- Close auctions and reveal winners.
- AI bid suggestions (rule-based).

## How to Use

### 1. Create an Auction
- Enter the item name (e.g., "Laptop").
- Click "Create" – you'll get a unique Auction ID.

### 2. Place a Bid
- Enter the Auction ID.
- Add your name and bid amount.
- Click "Bid" – your bid is stored anonymously.

### 3. Get AI Suggestion
- Enter the item name.
- Click "Get AI Suggestion" – get a recommended bid amount.

### 4. Close Auction
- Enter the Auction ID.
- Click "Close" – bidding ends.

### 5. Reveal Winner
- Enter the Auction ID.
- Click "Reveal" – see the highest bidder and amount.

## Example Walkthrough
1. Create Auction: Item = "Gaming Laptop" → Auction ID: `abc123`
2. Place Bids:
   - Bidder: Alice, Amount: $800
   - Bidder: Bob, Amount: $750
3. AI Suggestion: Item = "Gaming Laptop" → Suggested: $500
4. Close Auction: ID = `abc123`
5. Reveal Winner: Winner = Alice ($800)

## Tech Stack
- Backend: Flask, Python
- Frontend: HTML, Bootstrap
- Deployment: Render (free)
- AI: Rule-based suggestions (expandable to OpenAI)

## Development
- Clone the repo: `git clone https://github.com/Shankar-Shinde/AI-BLIND-AUCTION.git`
- Install dependencies: `pip install -r requirements.txt`
- Run locally: `python app.py`
- Access at `http://127.0.0.1:5000`

## Enhancements
See [ENHANCEMENTS.md](ENHANCEMENTS.md) for planned features.

## License
MIT License.

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