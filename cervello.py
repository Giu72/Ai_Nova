import PyPDF2
import requests
from bs4 import BeautifulSoup

def carica_pdf(percorso):
    testo = ""
    try:
        with open(percorso, "rb") as f:
            reader = PyPDF2.PdfReader(f)
            for page in reader.pages:
                testo += page.extract_text()
    except:
        testo = "Errore caricamento PDF. "
    return testo

def carica_link(urls):
    contenuto = ""
    for url in urls:
        try:
            res = requests.get(url, timeout=5)
            soup = BeautifulSoup(res.text, 'html.parser')
            contenuto += soup.get_text()
        except:
            continue
    return contenuto

# Configura i tuoi link
links = [
    "https://www.inps.it/it/it/sostegni-sussidi-indennita.html",
    # Aggiungi gli altri qui...
]

# RIGA CORRETTA: Il nome del file deve essere IDENTICO a quello nella cartella
testo_totale = carica_pdf("Legge_bilancio2026.pdf") + carica_link(links)