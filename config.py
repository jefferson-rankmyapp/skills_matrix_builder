# config.py
import os
from dotenv import load_dotenv

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

DEBUG = os.getenv("DEBUG", "False") == "True"
APP_NAME = os.getenv("APP_NAME", "People.AI - Assistente de Matriz de Habilidades")