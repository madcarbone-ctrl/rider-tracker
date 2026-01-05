import streamlit as st

# Blocchiamo il layout per evitare che il telefono lo allarghi
st.set_page_config(layout="centered")

st.markdown("""
<style>
    /* Nascondiamo i margini di Streamlit per recuperare spazio */
    [data-testid="stAppViewBlockContainer"] { padding: 5px !important; }
    .stApp { background-color: #000; }

    /* CONTENITORE DASHBOARD: Larghezza bloccata per Samsung A34 */
    .dashboard-container {
        width: 340px; /* Calibrato sui tuoi 1080px reali */
        margin: 0 auto;
        background-color: #000;
    }

    .grid-row {
        display: flex !important;
        flex-direction: row !important;
        flex-wrap: nowrap !important; /* VIETA l'incolonnamento */
        justify-content: space-between;
        margin-bottom: 6px;
    }

    .tile {
        width: 108px !important; /* 108px x 3 = 324px + margini = 340px */
        background: #121212;
        border: 1px solid #282828;
        border-radius: 8px;
        padding: 12px 0;
        text-align: center;
        flex-shrink: 0 !important;
    }

    .t { font-size: 10px; color: #888; font-weight: bold; margin-bottom: 2px; }
    .v-c { color: #00CCBC; font-size: 16px; font-weight: bold; }
    .v-r { color: #FF4B4B; font-size: 16px; font-weight: bold; }

    /* BOTTONI GRANDI TATTILI */
    .stButton > button {
        width: 340px !important;
        height: 60px !important;
        background: #111 !important;
        border: 1px solid #00CCBC !important;
        color: #00CCBC !important;
        border-radius: 12px !important;
        font-weight: bold !important;
        font-size: 16px !important;
        margin-top: 10px;
    }
</style>
""", unsafe_allow_html=True)

st.markdown("<h3 style='text-align:center; color:#00CCBC; width:340px; margin:10px auto;'>RIDER TRACKER PRO</h3>", unsafe_allow_html=True)

# DASHBOARD 3x3 IN PIXEL (Indistruttibile)
st.markdown("""
<div class="dashboard-container">
    <div class="grid-row">
        <div class="tile"><div class="t">LORDO</div><div class="v-c">€0.00</div></div>
        <div class="tile"><div class="t">NETTO</div><div class="v-r">€0.00</div></div>
        <div class="tile"><div class="t">ORE</div><div class="v-c">0.0</div></div>
    </div>
    <div class="grid-row">
        <div class="tile"><div class="t">LITRI</div><div class="v-c">0.0L</div></div>
        <div class="tile"><div class="t">KM/L</div><div class="v-c">0.0</div></div>
        <div class="tile"><div class="t">BENZINA</div><div class="v-c">€0.00</div></div>
    </div>
</div>
""", unsafe_allow_html=True)

st.write("---")

# TASTI AZIONE
if st.button("➕ NUOVO TURNO"):
    st.session_state.m = 't'
if st.button("⛽ RIFORNIMENTO"):
    st.session_state.m = 'b'

# MODULO INSERIMENTO (Oggi 05/01/2026)
if st.session_state.get('m') == 't':
    st.markdown("<div style='width:340px; margin:0 auto; background:#111; padding:15px; border-radius:10px; border:1px solid #00CCBC;'>", unsafe_allow_html=True)
    st.write("Turno del 05/01/2026")
    st.number_input("Guadagno €", format="%.2f")
    st.number_input("Chilometri", step=1)
    if st.button("CONFERMA SALVATAGGIO"): st.success("Salvato!")
    st.markdown("</div>", unsafe_allow_html=True)
