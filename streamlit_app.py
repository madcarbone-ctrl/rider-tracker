import streamlit as st
from datetime import datetime

# CONFIGURAZIONE APP PROFESSIONAL
st.set_page_config(page_title="Rider Tracker Pro", layout="centered")

# DATA AUTOMATICA (Oggi: 5 Gen 2026)
oggi = datetime.now()
mesi = ["Gen", "Feb", "Mar", "Apr", "Mag", "Giu", "Lug", "Ago", "Set", "Ott", "Nov", "Dic"]

# STILE GRAFICO PREMIUM (Colori approvati)
st.markdown("""
<style>
    .main { background-color: #000000; color: white; }
    .card { background-color: #1a1a1a; border-radius: 15px; padding: 15px; text-align: center; border: 1px solid #333; }
    .label { font-size: 12px; color: #888; text-transform: uppercase; }
    .valore-ciano { color: #00CCBC; font-size: 20px; font-weight: bold; }
    .valore-rosso { color: #FF4B4B; font-size: 20px; font-weight: bold; }
    
    /* Finestre Moduli */
    .border-turno { border: 2px solid #00CCBC; border-radius: 20px; padding: 20px; }
    .border-benzina { border: 2px solid #FFA500; border-radius: 20px; padding: 20px; }
</style>
""", unsafe_allow_html=True)

# TITOLO APP
st.markdown("<h1 style='text-align: center; color: #00CCBC;'>RIDER TRACKER PRO V1.0</h1>", unsafe_allow_html=True)

# 1. DASHBOARD 3x3
c1, c2, c3 = st.columns(3)
with c1:
    st.markdown('<div class="card"><div class="label">LORDO</div><div class="valore-ciano">€0.00</div></div>', unsafe_allow_html=True)
    st.markdown('<br><div class="card"><div class="label">LITRI STIM.</div><div class="valore-ciano">0.0L</div></div>', unsafe_allow_html=True)
with c2:
    st.markdown('<div class="card"><div class="label">NETTO</div><div class="valore-rosso">€0.00</div></div>', unsafe_allow_html=True)
    st.markdown('<br><div class="card"><div class="label">KM/L</div><div class="valore-ciano">0.0</div></div>', unsafe_allow_html=True)
with c3:
    st.markdown('<div class="card"><div class="label">ORE</div><div class="valore-ciano">0.0</div></div>', unsafe_allow_html=True)
    st.markdown('<br><div class="card"><div class="label">SPESA BENZ.</div><div class="valore-ciano">€0.00</div></div>', unsafe_allow_html=True)

st.write("---")

# 2. TASTI AZIONE PRINCIPALI
col_a, col_b, col_c = st.columns(3)
btn_turno = col_a.button("➕ TURNO")
btn_benzina = col_b.button("⛽ BENZINA")
btn_storico = col_c.button("🕒 STORICO")

# Logica finestre
if btn_turno: st.session_state.app_mode = "turno"
if btn_benzina: st.session_state.app_mode = "benzina"
if btn_storico: st.session_state.app_mode = "storico"

# 3. MODULO NUOVO TURNO (Bordo Ciano)
if st.session_state.get("app_mode") == "turno":
    st.markdown('<div class="border-turno">', unsafe_allow_html=True)
    st.subheader("Nuovo Turno")
    d1, d2, d3 = st.columns(3)
    d1.selectbox("Giorno", list(range(1, 32)), index=oggi.day-1) # Auto 5
    d2.selectbox("Mese", mesi, index=oggi.month-1) # Auto Gen
    d3.selectbox("Anno", [2025, 2026], index=1) # Auto 2026
    
    st.number_input("Lordo (€)", step=1.0, format="%.2f")
    st.number_input("Chilometri percorsi", step=1.0)
    if st.button("SALVA DATI"):
        st.success("Turno salvato con successo!")
        st.session_state.app_mode = None
    st.markdown('</div>', unsafe_allow_html=True)

# 4. MODULO BENZINA (Bordo Arancio)
if st.session_state.get("app_mode") == "benzina":
    st.markdown('<div class="border-benzina">', unsafe_allow_html=True)
    st.subheader("Rifornimento")
    st.number_input("Euro spesi (€)", step=1.0, format="%.2f")
    st.number_input("Prezzo al Litro (€/L)", format="%.3f")
    if st.button("SALVA BENZINA"):
        st.success("Rifornimento registrato!")
        st.session_state.app_mode = None
    st.markdown('</div>', unsafe_allow_html=True)

# 5. STORICO ATTIVITÀ
if st.session_state.get("app_mode") == "storico":
    st.subheader("Storico Attività")
    st.markdown("""
        <div style='border-left: 5px solid #00CCBC; background: #222; padding: 15px; margin-bottom: 10px;'>
            <small style='color:#888;'>TURNO - 05/01/2026</small><br>
            <b style='font-size:22px;'>€42.50</b> <span style='float:right; color:#FF4B4B; font-weight:bold;'>X</span><br>
            <small>32 KM | 4.5 ORE</small>
        </div>
    """, unsafe_allow_html=True)
    if st.button("CHIUDI"): st.session_state.app_mode = None
