---
title: LLM Analysis Quiz Solver
# TDS LLM Analysis Quiz — Sohini’s Version

## 🚀 Project Overview

This project implements a solver for the “LLM Analysis Quiz” assignment:  
- Accepts POST requests with quiz URL, email & secret  
- Uses a headless browser + LLM + data processing pipeline  
- Automatically solves quiz tasks with scraping / CSV / audio / data analysis  

## 🔧 Tech Stack & Tools

- 🐍 Python 3.12  
- FastAPI for HTTP API  
- Playwright for browser automation (JS-rendered pages)  
- pandas, BeautifulSoup for data processing  
- :contentReference[oaicite:0]{index=0} + :contentReference[oaicite:1]{index=1} (Gemini) for LLM-based reasoning  
- :contentReference[oaicite:2]{index=2} for exposing the local server publicly  
- `.env` for configuration (email, secret, API key)

## 🛠️ How to Run Locally (dev setup)

```bash
git clone https://github.com/23f2005416/p2-llm-analysis-quiz.git
cd p2-llm-analysis-quiz

python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install fastapi "uvicorn[standard]" playwright python-dotenv requests httpx pydantic pandas beautifulsoup4
python -m playwright install chromium

cp .env.example .env  # or manually create .env with EMAIL, SECRET, GOOGLE_API_KEY

uv run python main.py   # start server
```

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.


