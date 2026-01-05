import streamlit as st

st.set_page_config(layout="wide")

# CSS ESTREMO: Obbliga il telefono a non incolonnare
st.markdown("""
<style>
    /* Rimuove i blocchi di Streamlit che causano l'incolonnamento */
    [data-testid="column"] {
        width: 32% !important;
        flex: 1 1 32% !important;
        min-width: 32% !important;
    }
    [data-testid="stHorizontalBlock"] {
        display: flex !important;
        flex-direction: row !important;
        flex-wrap: nowrap !important;
    }
    .stApp { background-color: black; }
    
    /* Box Dashboard */
    .box {
        background-color: #121212;
        border: 1px solid #333;
        border-radius: 8px;
        padding: 10px 2px;
        text-align: center;
    }
    .t { font-size: 10px; color: #888; }
    .v-c { color: #00CCBC; font-size: 16px; font-weight: bold; }
    .v-r { color: #FF4B4B; font-size: 16px; font-weight: bold; }
</style>
""", unsafe_allow_html=True)

st.markdown("<h3 style='text-align:center;color:#00CCBC;'>RIDER TRACKER PRO</h3>", unsafe_allow_html=True)

# DASHBOARD 3x3 FORZATA
# Riga 1
c1, c2, c3 = st.columns(3)
c1.markdown('<div class="box"><div class="t">LORDO</div><div class="v-c">€0.00</div></div>', unsafe_allow_html=True)
c2.markdown('<div class="box"><div class="t">NETTO</div><div class="v-r">€0.00</div></div>', unsafe_allow_html=True)
c3.markdown('<div class="box"><div class="t">ORE</div><div class="v-c">0.0</div></div>', unsafe_allow_html=True)

st.write("") # Spazio

# Riga 2
c4, c5, c6 = st.columns(3)
c4.markdown('<div class="box"><div class="t">LITRI</div><div class="v-c">0.0L</div></div>', unsafe_allow_html=True)
c5.markdown('<div class="box"><div class="t">KM/L</div><div class="v-c">0.0</div></div>', unsafe_allow_html=True)
c6.markdown('<div class="box"><div class="t">BENZINA</div><div class="v-c">€0.00</div></div>', unsafe_allow_html=True)

st.write("---")

# TASTI GRANDI
if st.button("➕ NUOVO TURNO (05/01/2026)"): st.info("Inserisci dati turno")
if st.button("⛽ RIFORNIMENTO BENZINA"): st.warning("Inserisci spesa benzina")
if st.button("🕒 VEDI STORICO"): st.write("Storico vuoto")
