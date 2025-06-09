import requests
import time
from datetime import datetime
import os

servidores = [
    {"nome": "ninety", "url": os.getenv("NINETY_URL")},
    {"nome": "uniplay", "url": os.getenv("UNIPLAY_URL")},
    {"nome": "elite", "url": os.getenv("ELITE_URL")},
    {"nome": "club", "url": os.getenv("CLUB_URL")},
    {"nome": "five", "url": os.getenv("FIVE_URL")},
    {"nome": "now", "url": os.getenv("NOW_URL")},
]

LOG_FILE = "monitoramento.log"

def check_urls():
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
    for servidor in servidores:
        try:
            response = requests.get(servidor["url"], headers=headers, timeout=10)
            status = f"{datetime.now()}: {servidor['nome']} ({servidor['url']}) - {'OK' if response.status_code == 200 else f'Falhou (Status: {response.status_code})'}"
            print(status)
            with open(LOG_FILE, "a") as log_file:
                log_file.write(status + "\n")
        except requests.RequestException as e:
            status = f"{datetime.now()}: {servidor['nome']} ({servidor['url']}) - Falhou (Erro: {str(e)})"
            print(status)
            with open(LOG_FILE, "a") as log_file:
                log_file.write(status + "\n")

print("Iniciando monitoramento...")
while True:
    check_urls()
    time.sleep(300)
