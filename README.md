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