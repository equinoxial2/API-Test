@echo off
SETLOCAL ENABLEDELAYEDEXPANSION

:: Définir le chemin d'installation
set "PROJET_PATH=E:\MonProjetBinance"

:: Créer le dossier du projet
mkdir "%PROJET_PATH%"
cd /d "%PROJET_PATH%"

:: Initialiser Git
git init

:: Créer les fichiers de base
echo from fastapi import FastAPI>main.py
echo.>>main.py
echo app = FastAPI()>>main.py
echo.>>main.py
echo @app.get("/")>>main.py
echo def root():>>main.py
echo     return {"message": "Bienvenue sur l'API Binance de Frédéric"}>>main.py

:: Fichier README
echo # Projet Binance de Frédéric>README.md
echo.>>README.md
echo API simple en Python avec FastAPI, déployée localement.>>README.md

:: Fichier requirements.txt
echo fastapi>requirements.txt
echo uvicorn>>requirements.txt
echo python-dotenv>>requirements.txt

:: Fichier .gitignore
echo .env>.gitignore
echo __pycache__/>>.gitignore
echo *.pyc>>.gitignore

:: Fichier .env vide
echo # Clés API ici (facultatif)>.env

:: Ajout au dépôt Git
git add .
git commit -m "Initialisation du projet Binance"
echo.
echo ✅ Projet initialisé sur %PROJET_PATH%
echo Pour installer les dépendances : pip install -r requirements.txt
echo Pour lancer l'API : uvicorn main:app --reload
echo.
pause
