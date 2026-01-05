import streamlit as st

# Setup pagina
st.set_page_config(layout="centered")

# CSS PER FISSARE LA TABELLA (Niente più incolonnamento)
st.markdown("""
<style>
    .stApp { background-color: #000; }
    [data-testid="stAppViewBlockContainer"] { padding: 5px !important; }

    /* Forza la tabella a rimanere in 3 colonne */
    .fixed-table {
        width: 100%;
        border-collapse: separate;
        border-spacing: 4px;
        display: table !important; /* Forza il comportamento tabella */
    }
    .t-row { display: table-row !important; }
    .t-cell {
        display: table-cell !important;
        width: 33.33% !important; /* Forza larghezza fissa */
        background: #111;
        border: 1px solid #222;
        border-radius: 8px;
        padding: 12px 2px;
        text-align: center;
        vertical-align: middle;
    }
    .lbl { font-size: 9px; color: #888; font-weight: bold; text-transform: uppercase; }
    .val-c { color: #00CCBC; font-size: 14px; font-weight: bold; }
    .val-r { color: #FF4B4B; font-size: 14px; font-weight: bold; }

    /* Bottoni grandi stile App */
    .stButton > button {
        width: 100% !important;
        height: 60px !important;
        background: #111 !important;
        border: 1px solid #00CCBC !important;
        color: #00CCBC !important;
        border-radius: 12px !important;
        font-weight: bold !important;
        margin-top: 10px;
    }
</style>
""", unsafe_allow_html=True)

st.markdown("<h3 style='text-align:center; color:#00CCBC;'>RIDER TRACKER PRO</h3>", unsafe_allow_html=True)

# LA TABELLA RIGIDA (Come il tuo primo screenshot)
st.markdown("""
<table class="fixed-table">
  <tr class="t-row">
    <td class="t-cell"><div class="lbl">LORDO</div><div class="val-c">€0.00</div></td>
    <td class="t-cell"><div class="lbl">NETTO</div><div class="val-r">€0.00</div></td>
    <td class="t-cell"><div class="lbl">ORE</div><div class="val-c">0.0</div></td>
  </tr>
  <tr class="t-row">
    <td class="t-cell"><div class="lbl">LITRI</div><div class="val-c">0.0L</div></td>
    <td class="t-cell"><div class="lbl">KM/L</div><div class="val-c">0.0</div></td>
    <td class="t-cell"><div class="lbl">BENZINA</div><div class="val-c">€0.00</div></td>
  </tr>
</table>
""", unsafe_allow_html=True)

st.write("---")

# TASTI AZIONE
if st.button("➕ AGGIUNGI TURNO"):
    st.session_state.m = 't'
if st.button("⛽ SEGNA BENZINA"):
    st.session_state.m = 'b'

# Inserimento (Oggi 05/01/2026)
if st.session_state.get('m') == 't':
    st.markdown("<div style='background:#111; padding:15px; border-radius:10px; border:1px solid #00CCBC;'>", unsafe_allow_html=True)
    st.write("Registra Turno: **05 Gennaio 2026**")
    st.number_input("Guadagno Lordo €", step=1.0)
    if st.button("SALVA ORA"): st.success("Dato inserito!")
    st.markdown("</div>", unsafe_allow_html=True)
