import PyPDF2
import requests
from bs4 import BeautifulSoup

def carica_pdf(percorso):
    testo = ""
    with open(percorso, "rb") as f:
        reader = PyPDF2.PdfReader(f)
        for page in reader.pages:
            testo += page.extract_text()
    return testo

def carica_link(urls):
    contenuto = ""
    for url in urls:
        res = requests.get(url)
        soup = BeautifulSoup(res.text, 'html.parser')
        contenuto += soup.get_text()
    return contenuto

# Configura qui i tuoi 10 link
links = ["https://www.inps.it/it/it/sostegni-sussidi-indennita.html", "https://www.inps.it/it/it/sostegni-sussidi-indennita/per-disoccupati.html", "https://www.inps.it/it/it/lavoro/disoccupazione.html", "  https://www.inps.it/it/it/servizi/per-i-cittadini/assegno-di-inclusione-adi", "  https://www.inps.it/it/it/sostegni-sussidi-indennita/studio-e-formazione.html", "https://www.inps.it/it/it/sostegni-sussidi-indennita/per-nucleo-familiare.html", "https://www.inps.it/it/it/dettaglio-scheda.it.schede-servizio-strumento.schede-strumenti.assegno-per-il-nucleo-familiare-consultazione-degli-importi-anf-52810.assegno-per-il-nucleo-familiare-consultazione-degli-importi-anf.html", "  https://www.inps.it/it/it/sostegni-sussidi-indennita/per-disabili-invalidi-inabili.html", "https://www.inps.it/it/it/previdenza/domanda-di-pensione.html", "https://www.inps.it/it/it/lavoro/contributi-dipendenti-e-collaboratori.html" ] 
testo_totale = carica_pdf("bilancio_2026.pdf") + carica_link(links)