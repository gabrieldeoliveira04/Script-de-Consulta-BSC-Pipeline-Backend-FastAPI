# BSC Pipeline + Backend FastAPI

Sistema para monitoramento de wallets públicas da Binance Smart Chain (BSC), desenvolvido como parte de um desafio técnico. O projeto coleta saldos de carteiras públicas da Binance, persiste os dados em PostgreSQL e expõe uma API REST documentada com FastAPI.

## Live API

API Online:

https://bsc-monitor-api.onrender.com

Swagger:

https://bsc-monitor-api.onrender.com/docs
---

## Overview

Fluxo da aplicação:

```txt
BSC RPC
   ↓
Collector
   ↓
PostgreSQL
   ↓
FastAPI
   ↓
Swagger / API
```

O sistema consulta wallets públicas da Binance utilizando `web3.py`, coleta saldos de tokens BEP-20 e armazena os dados em banco relacional para exposição via API.

---

## Features

### Blockchain

- Conexão com Binance Smart Chain via RPC
- Consulta de saldo BEP-20
- Monitoramento de wallets públicas Binance
- Conversão automática de valores brutos

### Pipeline

- Coleta automática de dados
- Scheduler interno executando em background
- Persistência em PostgreSQL
- Histórico completo de coletas

### API

- FastAPI
- Swagger automático
- Response models com Pydantic
- Estrutura modular

### Deploy

- API hospedada no Render
- PostgreSQL cloud
- Banco criado automaticamente no startup
- Variáveis via `.env`

---

## Wallets monitoradas

Binance Hot Wallet 8

```txt
0xF977814e90dA44bFA03b6295A0616a897441aceC
```

Binance 14

```txt
0x28C6c06298d514Db089934071355E5743bf21d60
```

Binance 7

```txt
0x3f5CE5FBFe3E9af3971dD833D26bA9b5C936f0bE
```

Token monitorado:

USDT (BEP20)

```txt
0x55d398326f99059fF775485246999027B3197955
```

---

## API Endpoints

### Health Check

```http
GET /
```

Response:

```json
{
  "status":"online"
}
```

---

### Latest Balances

Retorna o último snapshot de todas as wallets.

```http
GET /balances/latest
```

Exemplo:

```json
[
  {
    "wallet_address":"0xF...",
    "balance":2.81
  }
]
```

---

### Wallet History

Retorna histórico completo de uma carteira.

```http
GET /balances/{wallet}/history
```

Exemplo:

```http
GET /balances/0x28C6.../history
```

---

### Statistics

Retorna estatísticas gerais.

```http
GET /stats
```

Exemplo:

```json
{
  "total_records":12,

  "wallet_with_highest_balance":{
      "wallet":"0x28...",
      "balance":3633.78
  }
}
```

---

### Manual Collection Endpoint

Endpoint administrativo utilizado para disparar coletas manuais.

```http
POST /admin/collect
```

---

## Project Architecture

```txt
app/

├── api/
│   └── API routes

├── collector/
│   └── Blockchain collection logic

├── config/
│   └── Environment configuration

├── database/
│   └── SQLAlchemy connection

├── models/
│   └── Database models

├── schemas/
│   └── Pydantic schemas

├── services/
│   └── BSC + scheduler services

└── utils/
    └── ABI and helpers
```

---

## Technologies

- Python 3.12
- FastAPI
- SQLAlchemy
- PostgreSQL
- Docker
- Render
- web3.py
- APScheduler
- Pydantic
- Uvicorn

---

## Running locally

Clone:

```bash
git clone URL
```

Install:

```bash
pip install -r requirements.txt
```

Create environment variables:

```bash
cp .env.example .env
```

Start database:

```bash
docker compose up -d
```

Run application:

```bash
./start.sh
```

Swagger:

```txt
http://localhost:8000/docs
```

---

## Environment variables

```env
RPC_URL=

DATABASE_URL=

TOKEN_ADDRESS=

WALLET_1=
WALLET_2=
WALLET_3=
```

---

## Technical decisions

- SQLAlchemy ORM utilizado para modelagem
- Scheduler automático para coleta periódica
- Banco criado automaticamente no startup
- API desacoplada do processo de coleta
- Configuração baseada em ambiente
- Estrutura modular para escalabilidade

## Swagger

http://localhost:8000/docs
