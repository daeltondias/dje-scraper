from database import salvar_publicacoes
from scraper import extrair_publicacoes
import schedule
import time

def iniciar():
    dados = extrair_publicacoes()
    salvar_publicacoes(dados)
    print("Scraping finalizado e salvo no MongoDB.")

# if __name__ == "__main__":
#     iniciar()

# Agendar para 12:00 todos os dias
schedule.every().day.at("12:00").do(iniciar)

while True:
    schedule.run_pending()
    time.sleep(1)


    
