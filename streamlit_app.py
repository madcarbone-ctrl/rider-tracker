import streamlit as st
from datetime import datetime

# Configurazione per ignorare i limiti di larghezza mobile
st.set_page_config(page_title="Rider Tracker Pro", layout="wide")

st.markdown("""
<style>
    /* Forza il colore di sfondo nero ovunque */
    .stApp { background-color: #000000; }
    [data-testid="stAppViewBlockContainer"] { padding: 10px !important; }

    /* GRIGLIA FORZATA 3x3: Non si rompe su smartphone */
    .grid-container {
        display: grid;
        grid-template-columns: 1fr 1fr 1fr; /* Obbliga 3 colonne */
        gap: 6px;
        width: 100%;
    }
    
    .grid-item {
        background-color: #121212;
        border: 1px solid #282828;
        border-radius: 8px;
        padding: 10px 2px;
        text-align: center;
    }
    
    .label { font-size: 10px; color: #757575; font-weight: bold; margin-bottom: 2px; }
    .val-cyan { color: #00CCBC; font-size: 15px; font-weight: bold; }
    .val-red { color: #FF4B4B; font-size: 15px; font-weight: bold; }

    /* Bottoni Android Style */
    .stButton > button {
        width: 100%;
        border-radius: 12px;
        height: 55px;
        background-color: #121212;
        border: 1px solid #00CCBC;
        color: white;
        margin-top: 10px;
    }
</style>
""", unsafe_allow_html=True)

# Titolo compatto
st.markdown("<h3 style='text-align: center; color: #00CCBC;'>RIDER TRACKER PRO</h3>", unsafe_allow_html=True)

# DASHBOARD REALE (Stile il tuo primo screenshot)
st.markdown("""
<div class="grid-container">
    <div class="grid-item"><div class="label">LORDO</div><div class="val-cyan">€0.00</div></div>
    <div class="grid-item"><div class="label">NETTO</div><div class="val-red">€0.00</div></div>
    <div class="grid-item"><div class="label">ORE</div><div class="val-cyan">0.0</div></div>
    <div class="grid-item"><div class="label">LITRI</div><div class="val-cyan">0.0L</div></div>
    <div class="grid-item"><div class="label">KM/L</div><div class="val-cyan">0.0</div></div>
    <div class="grid-item"><div class="label">BENZINA</div><div class="val-cyan">€0.00</div></div>
</div>
""", unsafe_allow_html=True)

st.write("---")

# Pulsanti facili da premere
c1, c2 = st.columns(2)
with c1:
    if st.button("➕ TURNO"): st.session_state.m = 't'
with c2:
    if st.button("⛽ BENZINA"): st.session_state.m = 'b'

# Modulo Inserimento (Oggi: 5 Gen 2026)
if st.session_state.get('m') == 't':
    st.markdown("<div style='border:1px solid #00CCBC; padding:15px; border-radius:10px;'>", unsafe_allow_html=True)
    st.write("Nuovo Turno - 05/01/2026")
    st.number_input("Lordo €", format="%.2f")
    st.number_input("KM", step=1)
    if st.button("SALVA ORA"): st.success("Dato Salvato!")
    st.markdown("</div>", unsafe_allow_html=True)
