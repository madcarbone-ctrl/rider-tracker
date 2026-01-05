import streamlit as st

st.set_page_config(layout="centered")

st.markdown("""
<style>
    /* Rimuove ogni interferenza di Streamlit */
    .stApp { background-color: #000; }
    [data-testid="stAppViewBlockContainer"] { padding: 5px !important; }
    
    /* LA GRIGLIA CHE NON SI PIEGA: Usa Flex-Box con larghezza minima */
    .dashboard-fixed {
        display: flex !important;
        flex-direction: row !important;
        flex-wrap: nowrap !important; /* VIETA categoricamente l'incolonnamento */
        width: 100%;
        gap: 4px;
        margin-bottom: 8px;
    }

    .tile {
        flex: 1 1 0 !important; /* Forza le tre colonne a dividersi lo spazio 33/33/33 */
        min-width: 0 !important; /* Impedisce al sistema di espanderle */
        background: #111;
        border: 1px solid #282828;
        border-radius: 8px;
        padding: 12px 0;
        text-align: center;
    }

    .lbl { font-size: 9px; color: #888; font-weight: bold; }
    .val-c { color: #00CCBC; font-size: 15px; font-weight: bold; }
    .val-r { color: #FF4B4B; font-size: 15px; font-weight: bold; }

    /* BOTTONI ANDROID NATIVI */
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

# DASHBOARD 3x3 INDISTRUTTIBILE (HTML RIGIDO)
st.markdown("""
<div class="dashboard-fixed">
    <div class="tile"><div class="lbl">LORDO</div><div class="val-c">€0.00</div></div>
    <div class="tile"><div class="lbl">NETTO</div><div class="val-r">€0.00</div></div>
    <div class="tile"><div class="lbl">ORE</div><div class="val-c">0.0</div></div>
</div>
<div class="dashboard-fixed">
    <div class="tile"><div class="lbl">LITRI</div><div class="val-c">0.0L</div></div>
    <div class="tile"><div class="lbl">KM/L</div><div class="val-c">0.0</div></div>
    <div class="tile"><div class="lbl">BENZINA</div><div class="val-c">€0.00</div></div>
</div>
""", unsafe_allow_html=True)

st.write("---")

# TASTI AZIONE
if st.button("➕ AGGIUNGI TURNO"):
    st.session_state.m = 't'
if st.button("⛽ SEGNA BENZINA"):
    st.session_state.m = 'b'

# DATA FISSA: 05 GENNAIO 2026
if st.session_state.get('m') == 't':
    st.markdown("<div style='background:#111; padding:15px; border-radius:10px; border:1px solid #00CCBC;'>", unsafe_allow_html=True)
    st.write("Inserimento per: **05/01/2026**")
    st.number_input("Lordo €", step=0.50)
    if st.button("SALVA"): st.success("OK!")
    st.markdown("</div>", unsafe_allow_html=True)
