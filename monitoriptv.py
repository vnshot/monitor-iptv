import requests
import time
from datetime import datetime

# Lista de servidores para monitorar
servidores = [
    {"nome": "ninety", "url": "http://dns.phaptom.shop/get.php?username=58804112&password=50872250&type=m3u_plus&output=mpegts"},
    {"nome": "uniplay", "url": "http://venombite.top/get.php?username=303863753&password=D144S6660c&type=m3u_plus&output=hls"},
    {"nome": "elite", "url": "http://ufcc.asia/get.php?username=vinagikev&password=PX56AW7X2AP8&type=m3u_plus&output=ts"},
    {"nome": "club", "url": "http://xwkhb.info/get.php?username=TccDP3zF&password=Xw7N7e&type=m3u_plus&output=ts"},
    {"nome": "five", "url": "http://cdn4k.live/get.php?username=kjagayan&password=k96vjavkm&type=m3u_plus&output=ts"},
    {"nome": "now", "url": "http://l.m3u4.xyz/3sfj35gj2"},
]

# Caminho para o arquivo de log
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

# Loop para rodar a cada 5 minutos
print("Iniciando monitoramento...")
while True:
    check_urls()
    time.sleep(300)  # 300 segundos = 5 minutos