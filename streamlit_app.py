import streamlit as st

# Rimuoviamo ogni layout dinamico
st.set_page_config(layout="centered")

st.markdown("""
<style>
    /* Sfondo nero e rimozione spazi bianchi */
    .stApp { background-color: #000; }
    [data-testid="stAppViewBlockContainer"] { padding: 0px !important; margin: 0px !important; }
    
    /* LA GRIGLIA D'ACCIAIO: Larghezza fissa in pixel */
    .fixed-grid {
        display: flex !important;
        flex-direction: row !important;
        flex-wrap: nowrap !important; /* VIETA di andare a capo */
        justify-content: center !important;
        gap: 4px !important;
        width: 100% !important;
        margin-bottom: 5px !important;
    }

    .card {
        width: 110px !important; /* Larghezza fissa per farle stare affiancate */
        background-color: #121212;
        border: 1px solid #282828;
        border-radius: 8px;
        padding: 10px 0px;
        text-align: center;
        flex-shrink: 0 !important; /* Impedisce al telefono di schiacciarle */
    }

    .lbl { font-size: 10px; color: #888; font-weight: bold; }
    .val-c { color: #00CCBC; font-size: 16px; font-weight: bold; }
    .val-r { color: #FF4B4B; font-size: 16px; font-weight: bold; }

    /* BOTTONI GRANDI DA RIDER */
    .stButton > button {
        width: 95% !important;
        height: 60px !important;
        margin-left: 2.5%;
        background-color: #121212 !important;
        border: 1px solid #00CCBC !important;
        color: #00CCBC !important;
        border-radius: 12px !important;
        font-weight: bold !important;
    }
</style>
""", unsafe_allow_html=True)

st.markdown("<h3 style='text-align:center; color:#00CCBC; margin-top:10px;'>RIDER TRACKER PRO</h3>", unsafe_allow_html=True)

# DASHBOARD 3x3: Sezione Superiore
st.markdown("""
<div class="fixed-grid">
    <div class="card"><div class="lbl">LORDO</div><div class="val-c">€0.00</div></div>
    <div class="card"><div class="lbl">NETTO</div><div class="val-r">€0.00</div></div>
    <div class="card"><div class="lbl">ORE</div><div class="val-c">0.0</div></div>
</div>
<div class="fixed-grid">
    <div class="card"><div class="lbl">LITRI</div><div class="val-c">0.0L</div></div>
    <div class="card"><div class="lbl">KM/L</div><div class="val-c">0.0</div></div>
    <div class="card"><div class="lbl">BENZINA</div><div class="val-c">€0.00</div></div>
</div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# TASTI AZIONE GRANDI
if st.button("➕ AGGIUNGI TURNO"):
    st.session_state.m = 't'
if st.button("⛽ SEGNA BENZINA"):
    st.session_state.m = 'b'

# DATA AUTOMATICA 05/01/2026
if st.session_state.get('m') == 't':
    st.markdown("<div style='background:#121212; padding:20px; border:1px solid #00CCBC; border-radius:15px; margin:10px;'>", unsafe_allow_html=True)
    st.write("Turno del: **05 Gennaio 2026**")
    st.number_input("Quanto hai fatto? (€)", step=1.0)
    if st.button("SALVA DEFINITIVO"): st.success("Dato registrato!")
    st.markdown("</div>", unsafe_allow_html=True)
