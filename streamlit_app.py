import streamlit as st

# Setup per eliminare ogni margine e centrare la tabella
st.set_page_config(layout="centered")

st.markdown("""
<style>
    /* Sfondo nero e rimozione totale spazi di sistema */
    .stApp { background-color: #000; }
    [data-testid="stAppViewBlockContainer"] { padding: 0px !important; margin: 0px !important; }
    [data-testid="stHeader"], [data-testid="stToolbar"] {display:none !important;}

    /* TABELLA 3x3 INDISTRUTTIBILE PER MOBILE */
    .grid-9 {
        width: 100% !important;
        border-collapse: collapse;
        table-layout: fixed !important; /* Forza le 3 colonne a restare affiancate */
    }
    .cell {
        background: #121212;
        border: 1px solid #282828;
        padding: 18px 0;
        text-align: center;
        width: 33.33%;
    }
    .lbl { font-size: 10px; color: #888; font-weight: bold; text-transform: uppercase; margin-bottom: 4px; }
    .val-c { color: #00CCBC; font-size: 16px; font-weight: bold; }
    .val-r { color: #FF4B4B; font-size: 16px; font-weight: bold; }
</style>

<table class="grid-9">
  <tr>
    <td class="cell"><div class="lbl">LORDO</div><div class="val-c">€0.00</div></td>
    <td class="cell"><div class="lbl">NETTO</div><div class="val-r">€0.00</div></td>
    <td class="cell"><div class="lbl">ORE</div><div class="val-c">0.0</div></td>
  </tr>
  <tr>
    <td class="cell"><div class="lbl">LITRI</div><div class="val-c">0.0L</div></td>
    <td class="cell"><div class="lbl">KM/L</div><div class="val-c">0.0</div></td>
    <td class="cell"><div class="lbl">BENZINA</div><div class="val-c">€0.00</div></td>
  </tr>
  <tr>
    <td class="cell"><div class="lbl">DISTANZA</div><div class="val-c">0 KM</div></td>
    <td class="cell"><div class="lbl">MEDIA €</div><div class="val-c">€0.00</div></td>
    <td class="cell"><div class="lbl">CONSEGNE</div><div class="val-c">0</div></td>
  </tr>
</table>
""", unsafe_allow_html=True)
