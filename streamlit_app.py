import streamlit as st

# Setup base
st.set_page_config(page_title="Rider Tracker", layout="centered")

# CSS TOTALE: Sovrascrive ogni regola del telefono
st.markdown("""
<style>
    /* Nasconde i menu inutili di Streamlit per guadagnare spazio */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    [data-testid="stAppViewBlockContainer"] { padding: 5px !important; margin: 0 !important; }

    /* CONTENITORE DASHBOARD: Forza la griglia fissa */
    .dashboard-wrapper {
        display: block;
        width: 100%;
        background-color: #000;
        padding: 5px;
    }
    
    .grid-row {
        display: flex !important;
        flex-direction: row !important;
        justify-content: space-around;
        margin-bottom: 8px;
    }

    .card {
        width: 31% !important; /* Forza 3 per riga */
        background-color: #121212;
        border: 1px solid #282828;
        border-radius: 8px;
        padding: 12px 0px;
        text-align: center;
    }

    .lbl { font-size: 9px; color: #888; font-weight: bold; }
    .val-c { color: #00CCBC; font-size: 15px; font-weight: bold; }
    .val-r { color: #FF4B4B; font-size: 15px; font-weight: bold; }

    /* BOTTONI ANDROID NATIVI */
    .stButton > button {
        width: 100% !important;
        height: 60px !important;
        background-color: #1a1a1a !important;
        border: 1px solid #00CCBC !important;
        border-radius: 12px !important;
        color: #00CCBC !important;
        font-weight: bold !important;
        margin-bottom: 10px;
    }
</style>
""", unsafe_allow_html=True)

# TITOLO
st.markdown("<h2 style='text-align:center; color:#00CCBC; margin:10px 0;'>RIDER PRO</h2>", unsafe_allow_html=True)

# LA GRIGLIA CHE NON SI ROMPE (HTML PURO)
st.markdown("""
<div class="dashboard-wrapper">
    <div class="grid-row">
        <div class="card"><div class="lbl">LORDO</div><div class="val-c">€0.00</div></div>
        <div class="card"><div class="lbl">NETTO</div><div class="val-r">€0.00</div></div>
        <div class="card"><div class="lbl">ORE</div><div class="val-c">0.0</div></div>
    </div>
    <div class="grid-row">
        <div class="card"><div class="lbl">LITRI</div><div class="val-c">0.0L</div></div>
        <div class="card"><div class="lbl">KM/L</div><div class="val-c">0.0</div></div>
        <div class="card"><div class="lbl">BENZINA</div><div class="val-c">€0.00</div></div>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("<div style='margin:15px 0; border-top:1px solid #333;'></div>", unsafe_allow_html=True)

# TASTI AZIONE
if st.button("➕ AGGIUNGI TURNO"):
    st.session_state.m = 't'
if st.button("⛽ SEGNA BENZINA"):
    st.session_state.m = 'b'

# DATA FISSA: 05 GENNAIO 2026
if st.session_state.get('m') == 't':
    st.markdown("<div style='background:#121212; padding:15px; border-radius:10px; border:1px solid #00CCBC;'>", unsafe_allow_html=True)
    st.write("Registrazione per: **05/01/2026**")
    st.number_input("Lordo €", step=0.50)
    st.number_input("KM", step=1)
    if st.button("SALVA DATI"): st.success("OK!")
    st.markdown("</div>", unsafe_allow_html=True)
