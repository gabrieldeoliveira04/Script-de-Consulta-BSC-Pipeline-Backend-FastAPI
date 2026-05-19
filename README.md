# BSC Pipeline + Backend FastAPI

## Overview
Sistema para monitoramento de wallets públicas da Binance na Binance Smart Chain.

Fluxo:

BSC RPC
↓
Collector
↓
PostgreSQL
↓
FastAPI
↓
Swagger

## Features

- Consulta 3 wallets Binance
- Coleta automática de saldo USDT
- Persistência PostgreSQL
- Histórico de coletas
- Estatísticas
- Swagger automático

## Architecture

app/
├── api/
├── collector/
├── config/
├── database/
├── models/
├── schemas/
├── services/
└── utils/

## Technologies

- Python 3.12
- FastAPI
- SQLAlchemy
- PostgreSQL
- Docker
- web3.py

## Setup

docker compose up -d

pip install -r requirements.txt

cp .env.example .env

uvicorn app.main:app --reload

## Endpoints

GET /balances/latest

GET /balances/{wallet}/history

GET /stats

## Swagger

http://localhost:8000/docs