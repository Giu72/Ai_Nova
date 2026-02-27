import PyPDF2

def carica_pdf():
    testo = ""
    try:
        # Questo legge il tuo file PDF della legge
        with open("Legge_bilancio2026.pdf", "rb") as f:
            lettore = PyPDF2.PdfReader(f)
            for pagina in lettore.pages:
                testo += pagina.extract_text()
    except:
        testo = "Errore nella lettura del PDF."
    return testo

testo_totale = carica_pdf()