import os
import streamlit as st

class Config:
    '''Klasa przechowująca konfigurację i ścieżki projektu HockeyML.'''
    
    # Ścieżki systemowe
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    DATA_DIR = os.path.join(BASE_DIR, 'data')
    LOG_DIR = os.path.join(BASE_DIR, 'logs')
    DB_PATH = os.path.join(DATA_DIR, 'hockey_data.db')
    
    # Ustawienia bazy danych
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{DB_PATH}'
    
    # Klucze API (pobierane z .streamlit/secrets.toml)
    try:
        THE_ODDS_API_KEY = st.secrets['THE_ODDS_API_KEY']
        RAPID_API_KEY = st.secrets['RAPID_API_KEY']
        RAPID_API_HOST = st.secrets['RAPID_API_HOST']
    except (FileNotFoundError, KeyError):
        THE_ODDS_API_KEY = os.getenv('THE_ODDS_API_KEY', '')
        RAPID_API_KEY = os.getenv('RAPID_API_KEY', '')
        RAPID_API_HOST = os.getenv('RAPID_API_HOST', '')

    # Konfiguracja MoneyPuck - Sezon 2025
    MONEYPUCK_TEAMS_URL = 'https://moneypuck.com/moneypuck/playerData/seasonSummary/2025/regular/teams.csv'
    
    # Konfiguracja MoneyPuck - Dane historyczne (2008-2024)
    MONEYPUCK_HISTORICAL_TEAMS_URL = 'https://peter-tanner.com/moneypuck/downloads/historicalOneRowPerSeason/teams_2008_to_2024.zip'

    # Ścieżki lokalne dla plików
    MONEYPUCK_LOCAL_PATH = os.path.join(DATA_DIR, 'moneypuck_teams.csv')

    # Stałe projektowe
    SNAPSHOT_TIMES = ['09:00', '21:00']
    DEFAULT_MARKET = 'h2h'
    REGIONS = 'us,eu'

# Inicjalizacja struktury folderów
os.makedirs(Config.DATA_DIR, exist_ok=True)
os.makedirs(Config.LOG_DIR, exist_ok=True)