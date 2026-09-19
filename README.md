# Autonomous Multi-Agent System for Stock Market News Analysis and Trend Prediction

## 📌 Project Overview

This project is an educational AI-based multi-agent system designed to analyze stock market information from multiple sources and generate a combined market signal.

The system combines:

- Real-time stock market data
- Real-time financial news
- News sentiment analysis
- Market impact analysis
- Technical indicators
- Machine learning prediction
- Multi-agent decision logic
- Audit logging
- Web-based dashboard

The current implementation uses **Reliance Industries (RELIANCE.NS)** as the primary example stock.

---

## 🎯 Project Objective

The main objective of this project is to demonstrate how multiple specialized AI agents can work together to analyze stock-market information.

Instead of relying on a single model, the system divides the task into multiple agents.

### Main workflow

```text
Stock Market Data
        ↓
Market Data Agent
        ↓
ML Prediction Agent
        ↓
        ┌──────────────────┐
News →  │ News Collector   │
        │      Agent       │
        └────────┬─────────┘
                 ↓
          News Sentiment
             Agent
                 ↓
          Market Agent
                 ↓
          Trend Agent
                 ↓
        Decision Agent
                 ↓
       Final Model Signal
                 ↓
            Dashboard
                 ↓
           Audit Trail


---

## 🤖 System Components

### 1. News Collector Agent
Collects financial news from available news sources.

### 2. News Sentiment Agent
Analyzes news and classifies sentiment as Positive, Negative, or Neutral.

### 3. Market Agent
Analyzes market-related information and generates a market direction.

### 4. Trend Agent
Identifies the current stock trend, such as Uptrend or Downtrend.

### 5. ML Prediction Agent
Uses machine learning models and historical stock data to predict market direction.

### 6. Decision Agent
Combines agent outputs to generate a final educational market signal.

### 7. Audit Logger
Stores agent results, timestamps, and stock symbols for transparency and review.

---

## 🛠️ Technologies Used

- Python
- Flask
- Pandas
- NumPy
- Scikit-learn
- yfinance
- HTML
- CSS
- JavaScript
- Chart.js
- Git and GitHub

---

## ⚠️ Project Disclaimer

This project is developed for educational and research purposes.

The generated market signals are model outputs and are not guaranteed predictions or financial advice.


---

## 📂 Project Folder Structure

```text
Stock-Market-Multi-Agent/
│
├── agents/
│   ├── news_agent.py
│   ├── market_agent.py
│   ├── trend_agent.py
│   └── ...
│
├── dashboard/
│   ├── app.py
│   ├── templates/
│   │   ├── index.html
│   │   └── error.html
│   └── static/
│       └── style.css
│
├── data/
│   ├── prepare_dataset.py
│   └── multi_stock_ml_dataset.csv
│
├── models/
│   ├── ml_analysis.py
│   └── train_and_save_model.py
│
├── utils/
│   ├── audit_logger.py
│   └── audit_log.json
│
├── main.py
├── requirements.txt
└── README.md
```

---

## 💻 Dashboard Features

- Dynamic stock symbol search
- Real-time stock information
- Stock price chart
- Financial news analysis
- Market trend prediction
- Machine learning model comparison
- Feature importance display
- Agent audit trail
- Invalid stock error handling

---

## 🔮 Future Scope

- Integration of advanced language models
- Improved sentiment analysis
- Additional technical indicators
- More machine learning algorithms
- Historical prediction performance tracking
- Human approval before any real-world action
- Improved multi-agent communication


---

## ⚙️ Installation and Execution

### 1. Clone the Repository

```bash
git clone https://github.com/Ankushy98/Stock-Market-Multi-Agent.git
cd Stock-Market-Multi-Agent
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

### 3. Activate Virtual Environment

**Windows PowerShell:**

```powershell
.\venv\Scripts\Activate.ps1
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Prepare the Dataset

```bash
python data\prepare_dataset.py RELIANCE.NS TCS.NS INFY.NS
```

### 6. Run the Dashboard

```bash
python -m dashboard.app
```

### 7. Open in Browser

```text
http://127.0.0.1:5000/?symbol=RELIANCE.NS
```


### Supported Stock Symbols

The dashboard supports analysis of valid stock symbols available through the configured market-data source.

Users can enter stock symbols dynamically, for example:

- RELIANCE.NS — Reliance Industries
- TCS.NS — Tata Consultancy Services
- INFY.NS — Infosys
- HDFCBANK.NS — HDFC Bank
- ICICIBANK.NS — ICICI Bank
- SBIN.NS — State Bank of India
- AAPL — Apple Inc.
- MSFT — Microsoft

**Note:** Availability depends on the market-data source, valid ticker format, and available historical data.