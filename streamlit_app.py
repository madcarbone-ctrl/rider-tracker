import streamlit as st

st.set_page_config(layout="centered")

# CSS PER TRASFORMARE IL SITO IN UN'APP NATIVA
st.markdown("""
<style>
    .stApp { background-color: #000000; }
    [data-testid="stAppViewBlockContainer"] { padding: 5px !important; }
    
    /* TABELLA DASHBOARD: Questa non si sposta mai */
    .dashboard-table {
        width: 100%;
        border-collapse: separate;
        border-spacing: 5px;
        table-layout: fixed;
    }
    .card {
        background-color: #121212;
        border: 1px solid #282828;
        border-radius: 10px;
        padding: 12px 2px;
        text-align: center;
    }
    .lbl { font-size: 10px; color: #888; font-weight: bold; }
    .val-c { color: #00CCBC; font-size: 16px; font-weight: bold; }
    .val-r { color: #FF4B4B; font-size: 16px; font-weight: bold; }

    /* BOTTONI GRANDI */
    .stButton > button {
        width: 100% !important;
        height: 65px !important;
        background-color: #121212 !important;
        border: 1px solid #333 !important;
        border-radius: 15px !important;
        color: white !important;
        font-size: 18px !important;
        margin-bottom: 10px;
    }
</style>
""", unsafe_allow_html=True)

st.markdown("<h2 style='text-align:center; color:#00CCBC; margin-bottom:15px;'>RIDER PRO</h2>", unsafe_allow_html=True)

# DASHBOARD 3x3 IN TABELLA (Indistruttibile in verticale)
st.markdown("""
<table class="dashboard-table">
  <tr>
    <td><div class="card"><div class="lbl">LORDO</div><div class="val-c">€0.00</div></div></td>
    <td><div class="card"><div class="lbl">NETTO</div><div class="val-r">€0.00</div></div></td>
    <td><div class="card"><div class="lbl">ORE</div><div class="val-c">0.0</div></div></td>
  </tr>
  <tr>
    <td><div class="card"><div class="lbl">LITRI</div><div class="val-c">0.0L</div></div></td>
    <td><div class="card"><div class="lbl">KM/L</div><div class="val-c">0.0</div></div></td>
    <td><div class="card"><div class="lbl">BENZINA</div><div class="val-c">€0.00</div></div></td>
  </tr>
</table>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# TASTI AZIONE
if st.button("➕ NUOVO TURNO"): st.session_state.m = 't'
if st.button("⛽ BENZINA"): st.session_state.m = 'b'
if st.button("🕒 STORICO"): st.session_state.m = 's'

# DATA AUTOMATICA 05/01/2026
if st.session_state.get('m') == 't':
    st.markdown("<div style='border:1px solid #00CCBC; padding:15px; border-radius:15px;'>", unsafe_allow_html=True)
    st.write("Inserimento del 05 Gennaio 2026")
    st.number_input("Guadagno Lordo €", format="%.2f")
    st.number_input("Chilometri totali", step=1)
    if st.button("SALVA DATI"): st.success("OK!")
    st.markdown("</div>", unsafe_allow_html=True)
