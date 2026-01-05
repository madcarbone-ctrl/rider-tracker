import streamlit as st

st.set_page_config(layout="centered")

# CSS DEFINITIVO PER SMARTPHONE (Forza la riga orizzontale)
st.markdown("""
<style>
    .stApp { background-color: #000; }
    [data-testid="stAppViewBlockContainer"] { padding: 5px !important; }
    
    /* IL CONTENITORE: Forza tutto su una riga senza andare a capo */
    .row-wrapper {
        white-space: nowrap !important; /* VIETA di andare a capo */
        overflow-x: hidden;
        width: 100%;
        margin-bottom: 5px;
        display: block;
    }

    .tile {
        display: inline-block !important; /* Forza l'affiancamento */
        width: 31% !important; /* Tre per riga */
        background: #111;
        border: 1px solid #222;
        border-radius: 8px;
        padding: 10px 0;
        text-align: center;
        margin: 1%;
        vertical-align: top;
    }

    .lbl { font-size: 9px; color: #888; font-weight: bold; }
    .val-c { color: #00CCBC; font-size: 15px; font-weight: bold; }
    .val-r { color: #FF4B4B; font-size: 15px; font-weight: bold; }

    /* BOTTONI GRANDI */
    .stButton > button {
        width: 100% !important;
        height: 60px !important;
        background: #111 !important;
        border: 1px solid #00CCBC !important;
        color: #00CCBC !important;
        border-radius: 12px !important;
        font-weight: bold !important;
    }
</style>
""", unsafe_allow_html=True)

st.markdown("<h3 style='text-align:center; color:#00CCBC;'>RIDER TRACKER PRO</h3>", unsafe_allow_html=True)

# DASHBOARD INDISTRUTTIBILE (Niente più colonne Streamlit)
st.markdown("""
<div class="row-wrapper">
    <div class="tile"><div class="lbl">LORDO</div><div class="val-c">€0.00</div></div>
    <div class="tile"><div class="lbl">NETTO</div><div class="val-r">€0.00</div></div>
    <div class="tile"><div class="lbl">ORE</div><div class="val-c">0.0</div></div>
</div>
<div class="row-wrapper">
    <div class="tile"><div class="lbl">LITRI</div><div class="val-c">0.0L</div></div>
    <div class="tile"><div class="lbl">KM/L</div><div class="val-c">0.0</div></div>
    <div class="tile"><div class="lbl">BENZINA</div><div class="val-c">€0.00</div></div>
</div>
""", unsafe_allow_html=True)

st.write("---")

# TASTI AZIONE
if st.button("➕ AGGIUNGI TURNO"): st.session_state.m = 't'
if st.button("⛽ SEGNA BENZINA"): st.session_state.m = 'b'

# DATA FISSA: 05/01/2026
if st.session_state.get('m') == 't':
    st.markdown("<div style='background:#111; padding:15px; border-radius:10px; border:1px solid #00CCBC;'>", unsafe_allow_html=True)
    st.write("Registrazione per: **05 Gennaio 2026**")
    st.number_input("Guadagno €", format="%.2f")
    if st.button("SALVA"): st.success("Dato inserito!")
    st.markdown("</div>", unsafe_allow_html=True)
