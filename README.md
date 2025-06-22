# API FastAPI de Frédéric

API minimaliste en FastAPI avec un endpoint de prix simulé. Ce dépôt contient également un petit proxy Flask vers l'API Binance.

## Installation

```bash
pip install -r requirements.txt
```

## Exécution

### Démarrer l'API FastAPI

```bash
uvicorn server:app --reload
```

### Démarrer le proxy Flask

```bash
python server_copy.py
```
