import streamlit as st
from datetime import datetime

# CONFIGURAZIONE SMARTPHONE
st.set_page_config(page_title="Rider Tracker Pro", layout="centered")

# CSS AGGRESSIVO PER SMARTPHONE (Forza la visualizzazione mobile)
st.markdown("""
<style>
    /* Elimina i margini vuoti ai lati su Android */
    [data-testid="stAppViewBlockContainer"] {
        padding: 10px !important;
        max-width: 100% !important;
    }
    
    /* Forza la griglia 3x3 su schermi stretti */
    .mobile-grid {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 8px;
        margin-bottom: 15px;
    }
    
    .mobile-card {
        background-color: #1a1a1a;
        border: 1px solid #333;
        border-radius: 10px;
        padding: 8px 2px;
        text-align: center;
    }
    
    .lbl { font-size: 9px; color: #888; text-transform: uppercase; margin-bottom: 2px; }
    .val-c { color: #00CCBC; font-size: 14px; font-weight: bold; }
    .val-r { color: #FF4B4B; font-size: 14px; font-weight: bold; }

    /* Bottoni grandi per dita (Rider Style) */
    .stButton > button {
        width: 100% !important;
        height: 60px !important;
        background-color: #1a1a1a !important;
        border: 1px solid #444 !important;
        border-radius: 15px !important;
        color: white !important;
        font-weight: bold !important;
        font-size: 16px !important;
    }
</style>
""", unsafe_allow_html=True)

st.markdown("<h2 style='text-align: center; color: #00CCBC; margin-bottom: 20px;'>RIDER TRACKER PRO</h2>", unsafe_allow_html=True)

# DASHBOARD 3x3 REALE PER MOBILE
st.markdown("""
<div class="mobile-grid">
    <div class="mobile-card"><div class="lbl">LORDO</div><div class="val-c">€0.00</div></div>
    <div class="mobile-card"><div class="lbl">NETTO</div><div class="val-r">€0.00</div></div>
    <div class="mobile-card"><div class="lbl">ORE</div><div class="val-c">0.0</div></div>
    <div class="mobile-card"><div class="lbl">LITRI</div><div class="val-c">0.0L</div></div>
    <div class="mobile-card"><div class="lbl">KM/L</div><div class="val-c">0.0</div></div>
    <div class="mobile-card"><div class="lbl">BENZINA</div><div class="val-c">€0.00</div></div>
</div>
""", unsafe_allow_html=True)

st.write("---")

# TASTI AZIONE GRANDI
if st.button("➕ NUOVO TURNO"):
    st.session_state.m = 't'
if st.button("⛽ BENZINA"):
    st.session_state.m = 'b'
if st.button("🕒 STORICO"):
    st.session_state.m = 's'

# LOGICA MODULI (Oggi: 5 Gen 2026)
m = st.session_state.get('m')
if m == 't':
    st.info("Inserimento Turno - 05/01/2026")
    st.number_input("Guadagno (€)", step=0.5)
    st.number_input("KM totali", step=1)
    if st.button("CONFERMA SALVATAGGIO"): st.success("Dato inserito!")

if m == 'b':
    st.warning("Rifornimento Benzina")
    st.number_input("Spesa (€)", step=1.0)
    if st.button("SALVA BENZINA"): st.success("Benzina salvata!")
