import streamlit as st
import streamlit.components.v1 as components
import random
import time

st.set_page_config(page_title="Aviator Monitor", layout="centered")
st.title("🛩️ Simulador de Velas – Aviator")

# Inicializar histórico no cache
if 'historico' not in st.session_state:
    st.session_state.historico = []

def gerar_vela():
    return round(random.uniform(1.00, 20.00), 2)

def tocar_alarme():
    components.html("""
        <audio autoplay>
            <source src="https://www.soundjay.com/button/sounds/beep-07.mp3" type="audio/mpeg">
        </audio>
    """, height=0)

def prever_vela(historico):
    ultimas = historico[-5:]
    # Regra simples: Se últimas 5 rodadas foram < 5x, alerta de possível vela alta
    if len(ultimas) == 5 and all(v < 5.0 for v in ultimas):
        return True
    return False

# Gerar nova vela
nova_vela = gerar_vela()
st.session_state.historico.append(nova_vela)

# Mostrar histórico
st.subheader("📈 Histórico de Velas:")
st.line_chart(st.session_state.historico[-20:])  # gráfico das últimas 20

# Mostrar lista
for i, v in enumerate(reversed(st.session_state.historico[-10:])):
    if v >= 10.0:
        st.success(f"🔥 Vela Alta #{len(st.session_state.historico)-i}: {v}x")
        tocar_alarme()
    else:
        st.write(f"Vela #{len(st.session_state.historico)-i}: {v}x")

# Previsão baseada no histórico
if prever_vela(st.session_state.historico):
    st.warning("🎯 Alta Possibilidade de Vela 10x na Próxima Rodada!")

# Auto refresh a cada 5 segundos
time.sleep(5)
st.rerun()
 streamlit as st
import streamlit.components.v1 as components
import random
import time

st.set_page_config(page_title="Aviator Monitor", layout="centered")
st.title("🛩️ Simulador de Velas – Aviator")

# Inicializar histórico no cache
if 'historico' not in st.session_state:
    st.session_state.historico = []

def gerar_vela():
    return round(random.uniform(1.00, 20.00), 2)

def tocar_alarme():
    components.html("""
        <audio autoplay>
            <source src="https://www.soundjay.com/button/sounds/beep-07.mp3" type="audio/mpeg">
        </audio>
    """, height=0)

def prever_vela(historico):
    ultimas = historico[-5:]
    # Regra simples: Se últimas 5 rodadas foram < 5x, alerta de possível vela alta
    if len(ultimas) == 5 and all(v < 5.0 for v in ultimas):
        return True
    return False

# Gerar nova vela
nova_vela = gerar_vela()
st.session_state.historico.append(nova_vela)

# Mostrar histórico
st.subheader("📈 Histórico de Velas:")
st.line_chart(st.session_state.historico[-20:])  # gráfico das últimas 20

# Mostrar lista
for i, v in enumerate(reversed(st.session_state.historico[-10:])):
    if v >= 10.0:
        st.success(f"🔥 Vela Alta #{len(st.session_state.historico)-i}: {v}x")
        tocar_alarme()
    
    else:
        st.write(f"Vela #{len(st.session_state.historico)-i}: {v}x")

# Previsão baseada no histórico
if prever_vela(st.session_state.historico):
    st.warning("🎯 Alta Possibilidade de Vela 10x na Próxima Rodada!")

# Auto refresh a cada 5 segundos
time.sleep(5)
st.rerun()
 streamlit as st
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
