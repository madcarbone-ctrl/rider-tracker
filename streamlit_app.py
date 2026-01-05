import streamlit as st
from datetime import datetime

# CONFIGURAZIONE ANDROID NATIVE
st.set_page_config(page_title="Rider Tracker Pro", layout="wide")

# STILE CSS PER FORZARE LA GRIGLIA 3x3 (Come il tuo screenshot)
st.markdown("""
<style>
    [data-testid="stAppViewBlockContainer"] { padding: 10px; background-color: #000000; }
    .main { background-color: #000000; }
    
    /* Griglia Dashboard */
    .row-container {
        display: flex;
        justify-content: space-between;
        margin-bottom: 10px;
        gap: 5px;
    }
    .card {
        background-color: #161616;
        border-radius: 12px;
        padding: 10px 5px;
        text-align: center;
        flex: 1;
        border: 1px solid #262626;
    }
    .label { font-size: 10px; color: #888; margin-bottom: 5px; }
    .val-cyan { color: #00CCBC; font-size: 16px; font-weight: bold; }
    .val-red { color: #FF4B4B; font-size: 16px; font-weight: bold; }

    /* Bottoni Android Style */
    div.stButton > button {
        width: 100%;
        background-color: #161616;
        color: white;
        border: 1px solid #333;
        border-radius: 10px;
        padding: 15px;
    }
</style>
""", unsafe_allow_html=True)

st.markdown("<h2 style='text-align: center; color: #00CCBC;'>RIDER TRACKER PRO</h2>", unsafe_allow_html=True)

# DASHBOARD 3x3 COMPATTA
st.markdown("""
<div class="row-container">
    <div class="card"><div class="label">LORDO</div><div class="val-cyan">€0.00</div></div>
    <div class="card"><div class="label">NETTO</div><div class="val-red">€0.00</div></div>
    <div class="card"><div class="label">ORE</div><div class="val-cyan">0.0</div></div>
</div>
<div class="row-container">
    <div class="card"><div class="label">LITRI</div><div class="val-cyan">0.0L</div></div>
    <div class="card"><div class="label">KM/L</div><div class="val-cyan">0.0</div></div>
    <div class="card"><div class="label">BENZINA</div><div class="val-cyan">€0.00</div></div>
</div>
""", unsafe_allow_html=True)

st.write("---")

# TASTI AZIONE COLORATI
col1, col2 = st.columns(2)
with col1:
    if st.button("➕ NUOVO TURNO"):
        st.session_state.mode = 'turno'
with col2:
    if st.button("⛽ RIFORNIMENTO"):
        st.session_state.mode = 'benzina'

if st.button("🕒 VEDI STORICO COMPLETO"):
    st.session_state.mode = 'storico'

# LOGICA MODULI (Data Auto: 05 Gen 2026)
mode = st.session_state.get('mode', None)

if mode == 'turno':
    st.markdown("<h3 style='color:#00CCBC'>Dati Turno</h3>", unsafe_allow_html=True)
    st.date_input("Data", datetime(2026, 1, 5)) # Forza data oggi
    st.number_input("Lordo Incassato (€)", format="%.2f")
    st.number_input("Chilometri Fatti", step=1)
    if st.button("SALVA"): st.success("Salvato!")

if mode == 'benzina':
    st.markdown("<h3 style='color:#FFA500'>Dati Benzina</h3>", unsafe_allow_html=True)
    st.number_input("Euro spesi (€)", format="%.2f")
    st.number_input("Prezzo al litro", format="%.3f")
    if st.button("REGISTRA"): st.success("Registrato!")
