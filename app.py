import streamlit as st

st.set_page_config(page_title="Análise Aviator – H2Bet", layout="centered")
st.title("🎯 Analisador de Velas – H2Bet Manual")

st.markdown("Cole abaixo as **últimas 20 velas** que você viu no jogo (ex: 1.2, 2.1, 10.5...)")

entrada = st.text_input("🔢 Digite as 20 velas separadas por vírgula")

if entrada:
    try:
        velas = [float(v.strip()) for v in entrada.split(",") if v.strip()]
        
        if len(velas) != 20:
            st.warning("⚠️ Você precisa inserir **exatamente 20 valores**.")
        else:
            maiores_10 = [v for v in velas if v >= 10]
            menores_2 = [v for v in velas if v < 2]
            ultimas_5 = velas[-5:]
            ultima_10x = max((i for i, v in enumerate(reversed(velas)) if v >= 10), default=None)

            # Métricas
            st.subheader("📊 Estatísticas")
            st.metric("Velas ≥ 10x", len(maiores_10))
            st.metric("Porcentagem ≥ 10x", f"{(len(maiores_10)/20)*100:.2f}%")
            st.metric("Velas < 2x", len(menores_2))

            if ultima_10x is not None:
                st.info(f"🕒 Já se passaram **{ultima_10x} velas** desde a última ≥ 10x")
            else:
                st.error("🚨 Nenhuma vela ≥ 10x nas últimas 20!")

            # Tendência simples
            st.subheader("📈 Análise de Tendência")

            if len(maiores_10) == 0:
                st.warning("🧊 Sessão FRIA: nenhuma vela ≥ 10x.")
            elif ultima_10x >= 10:
                st.success("🔥 Sessão pode estar esquentando.")
            else:
                st.info("📉 Sessão aparentemente neutra.")

            st.line_chart(velas)

            st.subheader("📋 Últimas 5 velas:")
            for i, v in enumerate(reversed(ultimas_5), 1):
                if v >= 10:
                    st.success(f"#{i} → 🔥 {v}x")
                elif v < 2:
                    st.error(f"#{i} → ⚠️ {v}x")
                else:
                    st.write(f"#{i} → {v}x")

    except Exception as e:
        st.error(f"❌ Erro: verifique se todos os valores são válidos. ({str(e)})")
else:
    st.info("Insira os dados para começar a análise.")
 streamlit as st


st.set_page_config(page_title="Aviator - Velas", layout="centered")
st.title("🎰 Monitor Manual de Velas – H2Bet")

st.markdown("Cole abaixo as **últimas 10 jogadas/velas** que você viu no site da H2Bet.")

# Campo de entrada
entrada = st.text_input("🔢 Exemplo: 1.2, 2.1, 10.5, 3.4, 12.3, 1.1, 1.9, 3.8, 8.4, 11.2")

# Quando o usuário digitar
if entrada:
    try:
        # Processar a entrada
        velas = [float(v.strip()) for v in entrada.split(",") if v.strip()]

        # Verifica se tem pelo menos 2 velas para exibir gráfico
        if len(velas) < 2:
            st.warning("⚠️ Insira pelo menos 2 valores numéricos separados por vírgula.")
        else:
            st.subheader("📊 Gráfico das últimas velas")
            st.line_chart(velas)

            st.subheader("📋 Detalhes:")
            acima_10 = [v for v in velas if v >= 10.0]
            for v in velas:
                if v >= 10.0:
                    st.success(f"🔥 Vela Alta: {v}x")
                elif v < 2.0:
                    st.error(f"🔻 Vela Baixa: {v}x")
                else:
                    st.write(f"{v}x")

            st.markdown("---")
            st.metric("Total analisado", len(velas))
            st.metric("Velas ≥ 10x", len(acima_10))
            st.metric("Porcentagem ≥ 10x", f"{(len(acima_10)/len(velas))*100:.2f}%")

    except ValueError:
        st.error("❌ Erro: Certifique-se de digitar apenas números separados por vírgula, como no exemplo acima.")
else:
    st.info("⌨️ Digite os valores das velas para começar.")
 as st

st.set_page_config(page_title="Aviator - Velas", layout="centered")
st.title("🎰 Monitor Manual de Velas – H2Bet")

st.markdown("Cole abaixo as **últimas 10 jogadas/velas** que você viu no site da H2Bet.")

# Campo de entrada
entrada = st.text_input("🔢 Exemplo: 1.2, 2.1, 10.5, 3.4, 12.3, 1.1, 1.9, 3.8, 8.4, 11.2")

# Quando o usuário digitar
if entrada:
    try:
        # Processar a entrada
        velas = [float(v.strip()) for v in entrada.split(",") if v.strip()]

        # Verifica se tem pelo menos 2 velas para exibir gráfico
        if len(velas) < 2:
            st.warning("⚠️ Insira pelo menos 2 valores numéricos separados por vírgula.")
        else:
            st.subheader("📊 Gráfico das últimas velas")
            st.line_chart(velas)

            st.subheader("📋 Detalhes:")
            acima_10 = [v for v in velas if v >= 10.0]
            for v in velas:
                if v >= 10.0:
                    st.success(f"🔥 Vela Alta: {v}x")
                elif v < 2.0:
                    st.error(f"🔻 Vela Baixa: {v}x")
                else:
                    st.write(f"{v}x")

            st.markdown("---")
            st.metric("Total analisado", len(velas))
            st.metric("Velas ≥ 10x", len(acima_10))
            st.metric("Porcentagem ≥ 10x", f"{(len(acima_10)/len(velas))*100:.2f}%")

    except ValueError:
        st.error("❌ Erro: Certifique-se de digitar apenas números separados por vírgula, como no exemplo acima.")
else:
    st.info("⌨️ Digite os valores das velas para começar.")
 streamlit as st
import random

st.set_page_config(page_title="Simulador Aviator", layout="centered")
st.title("🛩️ Simulador de Velas – Aviator")

# Entrada manual das velas
entrada = st.text_input("🔢 Cole as últimas 10 velas separadas por vírgula (ex: 1.2, 2.1, 10.5, 3.4...)")

if entrada:
    try:
        velas = [float(v.strip()) for v in entrada.split(",") if v.strip()]
        
        if len(velas) < 2:
            st.warning("⚠️ Insira pelo menos 2 valores.")
        else:
            st.line_chart(velas)

            if any(v >= 10 for v in velas):
                st.success("🚨 Alerta: vela maior ou igual a 10x detectada!")
            else:
                st.info("✅ Nenhuma vela >= 10x.")
    except ValueError:
        st.error("Erro: Insira apenas números separados por vírgula.")
else:
    st.info("Digite os valores para visualizar o gráfico.")

 import streamlit as st
import streamlit.components.v1 as components
import random
import time

st.set_page_config(page_title="Aviator Monitor", layout="centered")
st.title("🛩️ Monitor de Velas – Aviator")

# Histórico persistente
if 'historico' not in st.session_state:
    st.session_state.historico = []

# Função: gerar vela simulada
def gerar_vela():
    return round(random.uniform(1.00, 20.00), 2)

# Função: tocar som
def tocar_alerta():
    components.html("""
        <audio autoplay>
          <source src="https://www.soundjay.com/button/sounds/beep-07.mp3" type="audio/mpeg">
        </audio>
    """, height=0)

# Gerar nova vela
vela = gerar_vela()
st.session_state.historico.append(vela)

# Cálculos
total = len(st.session_state.historico)
acima_10 = len([v for v in st.session_state.historico if v >= 10.0])
porcentagem = (acima_10 / total) * 100 if total > 0 else 0
media_geral = sum(st.session_state.historico) / total
maior_valor = max(st.session_state.historico)
menor_valor = min(st.session_state.historico)

# Tempo desde último 10x
ultimo_10x = max((i for i, v in enumerate(st.session_state.historico) if v >= 10.0), default=None)
tempo_desde_10x = (total - ultimo_10x - 1) if ultimo_10x is not None else "Nunca"

# ==== INTERFACE ====

# Estatísticas principais
st.subheader("📊 Estatísticas em Tempo Real")
col1, col2, col3 = st.columns(3)
col1.metric("Total", total)
col2.metric("≥ 10x", acima_10)
col3.metric("Porcentagem", f"{porcentagem:.2f}%")

# Métricas adicionais
st.subheader("📌 Métricas Adicionais")
st.write(f"📌 Média geral: **{media_geral:.2f}x**")
st.write(f"📈 Maior vela: **{maior_valor:.2f}x**")
st.write(f"📉 Menor vela: **{menor_valor:.2f}x**")
st.write(f"🕒 Rodadas desde último 10x: **{tempo_desde_10x}**")

# Últimas velas
st.subheader("📈 Últimas 10 Velas:")
for v in reversed(st.session_state.historico[-10:]):
    if v >= 10.0:
        st.success(f"🔥 {v}x")
        tocar_alerta()
    elif v < 2.0:
        st.error(f"🔻 {v}x")
    else:
        st.write(f"{v}x")

# Gráfico de tendência
st.subheader("📉 Tendência das Últimas 30 Rodadas")
st.line_chart(st.session_state.historico[-30:])

# Atualiza a cada 5 segundos
time.sleep(5)
st.rerun()
 as st
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
