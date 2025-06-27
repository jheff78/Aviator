import streamlit as st
import random

st.set_page_config(page_title="Aviator Monitor", layout="centered")
st.title("🎰 Simulador de Velas - Aviator")

def gerar_velas():
    return [round(random.uniform(1.00, 20.00), 2) for _ in range(10)]

velas = gerar_velas()

st.subheader("Últimas Velas:")
for v in velas:
    if v >= 10:
        st.markdown(f"<span style='color:red; font-weight:bold;'>🔥 {v}x</span>", unsafe_allow_html=True)
    else:
        st.markdown(f"{v}x")

st.button("🔄 Atualizar Velas")
