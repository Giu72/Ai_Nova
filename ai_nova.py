
import streamlit as st
import google.generativeai as genai
from cervello import testo_totale # Assicurati che cervello.py sia corretto

# 1. Configurazione Interfaccia
st.set_page_config(page_title="Ai-Nova 2026", page_icon="🤖")
st.title("🤖 Ai-Nova: Assistente Diritti Sociali")
st.markdown("Chiedimi info su NASpI, ADI e Legge di Bilancio 2026.")
# 2. Configurazione AI (Usa i Secrets di Streamlit per sicurezza)
api_key = "AIzaSyDic62vIr0-PfZrrG4-eHkACYDaV2tVS0"
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-1.5-flash')

# 3. Gestione Memoria Chat
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 4. Azione al messaggio dell'utente
if prompt := st.chat_input("Scrivi qui la tua domanda..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Sto consultando i documenti..."):
            # Costruiamo il prompt usando il testo_totale che arriva da cervello.py
            full_prompt = f"""
            Sei 'Ai-Nova', un assistente esperto in diritti sociali.
            USA SOLO IL CONTESTO SEGUENTE:
            {testo_totale}
            
            DOMANDA: {prompt}
            """
            response = model.generate_content(full_prompt)
            st.markdown(response.text)
            
    st.session_state.messages.append({"role": "assistant", "content": response.text})