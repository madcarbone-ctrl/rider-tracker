import streamlit as st

st.set_page_config(layout="centered")

st.markdown("""
<style>
    .stApp { background-color: #000; }
    [data-testid="stAppViewBlockContainer"] { padding: 0px !important; margin: 0px !important; }
    [data-testid="stHeader"], [data-testid="stToolbar"] {display:none !important;}

    .grid-9 {
        width: 100% !important;
        border-collapse: collapse;
        table-layout: fixed !important;
    }
    .cell {
        background: #121212;
        border: 1px solid #282828;
        padding: 15px 0;
        text-align: center;
        width: 33.33%;
    }
    .lbl { font-size: 10px; color: #888; font-weight: bold; text-transform: uppercase; }
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
