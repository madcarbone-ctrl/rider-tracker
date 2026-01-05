import streamlit as st

# Setup che forza la pagina a non allargarsi inutilmente
st.set_page_config(page_title="Rider Tracker", layout="centered")

# CSS ESTREMO: Questo cancella le regole di Streamlit che incolonnano tutto
st.markdown("""
<style>
    /* Rimuove i margini di Streamlit che rubano spazio */
    [data-testid="stAppViewBlockContainer"] { padding: 5px !important; margin: 0 !important; }
    .stApp { background-color: #000; }

    /* CONTENITORE UNICO: Non permette di andare a capo */
    .super-grid {
        display: block;
        width: 100%;
        text-align: center;
        background: #000;
    }

    .row {
        display: flex !important;
        flex-direction: row !important;
        flex-wrap: nowrap !important; /* VIETATO andare a capo */
        justify-content: center;
        gap: 4px;
        margin-bottom: 5px;
    }

    .tile {
        width: 31% !important; /* Tre tiles occupano il 93%, perfetto per il Samsung */
        background: #111;
        border: 1px solid #222;
        border-radius: 8px;
        padding: 10px 0;
    }

    .t { font-size: 9px; color: #777; font-weight: bold; margin-bottom: 2px; }
    .v-c { color: #00CCBC; font-size: 15px; font-weight: bold; }
    .v-r { color: #FF4B4B; font-size: 15px; font-weight: bold; }

    /* BOTTONI GRANDI */
    .stButton > button {
        width: 100% !important;
        height: 55px !important;
        background: #111 !important;
        border: 1px solid #00CCBC !important;
        color: #00CCBC !important;
        border-radius: 12px !important;
        font-weight: bold !important;
        margin-bottom: 8px;
    }
</style>
""", unsafe_allow_html=True)

st.markdown("<h3 style='text-align:center; color:#00CCBC; margin:10px 0;'>RIDER TRACKER PRO</h3>", unsafe_allow_html=True)

# DASHBOARD BLOCCATA IN 3 COLONNE (HTML puro)
st.markdown("""
<div class="super-grid">
    <div class="row">
        <div class="tile"><div class="t">LORDO</div><div class="v-c">€0.00</div></div>
        <div class="tile"><div class="t">NETTO</div><div class="v-r">€0.00</div></div>
        <div class="tile"><div class="t">ORE</div><div class="v-c">0.0</div></div>
    </div>
    <div class="row">
        <div class="tile"><div class="t">LITRI</div><div class="v-c">0.0L</div></div>
        <div class="tile"><div class="t">KM/L</div><div class="v-c">0.0</div></div>
        <div class="tile"><div class="t">BENZINA</div><div class="v-c">€0.00</div></div>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("<div style='height:1px; background:#333; margin:15px 0;'></div>", unsafe_allow_html=True)

# TASTI AZIONE
if st.button("➕ AGGIUNGI TURNO"):
    st.session_state.m = 't'
if st.button("⛽ SEGNA BENZINA"):
    st.session_state.m = 'b'

# MODULO INSERIMENTO
if st.session_state.get('m') == 't':
    st.markdown("<div style='background:#111; padding:15px; border-radius:10px; border:1px solid #00CCBC;'>", unsafe_allow_html=True)
    st.write("Registra Turno: **05/01/2026**")
    st.number_input("Lordo €", step=0.50)
    st.number_input("Chilometri", step=1)
    if st.button("CONFERMA"): st.success("OK!")
    st.markdown("</div>", unsafe_allow_html=True)
