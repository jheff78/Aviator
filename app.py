 import streamlit as st
import requests

# 🌐 Buscar velas da API externa
def obter_velas_da_api():
    try:
        url = "https://aviator-api-bz4x.onrender.com/velas"
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            return response.json(), None
        else:
            return None, f"❌ Erro {response.status_code} ao buscar velas da API."
    except Exception as e:
        return None, f"❌ Erro de conexão: {e}"

# 🚀 Analisador de Velas
def analisar_velas(velas_raw):
    try:
        velas = [float(v.strip().replace('x', '').replace(',', '.')) for v in velas_raw]
        if len(velas) != 20:
            return None, "⚠️ Precisamos de exatamente 20 velas."
        acima_10x = [v for v in velas if v > 10]
        prob = len(acima_10x) / len(velas) * 100
        return prob, None
    except Exception as e:
        return None, f"❌ Erro ao processar as velas: {e}"

# 🟢 Execução principal
def main():
    st.markdown("<h1 style='text-align: center;'>📊 Aviator - Analisador de Velas</h1>", unsafe_allow_html=True)

    dados, erro = obter_velas_da_api()

    # Exibe erro de conexão
    if erro:
        st.error(erro)
        return

    # Verifica estrutura do JSON
    if not isinstance(dados, dict) or "velas" not in dados:
        st.error("❌ Dados inválidos recebidos da API.")
        return

    velas_raw = dados["velas"]

    # Verifica se é uma lista
    if not isinstance(velas_raw, list):
        st.error("❌ O formato das velas está incorreto.")
        return

    prob, erro_analise = analisar_velas(velas_raw)

    if erro_analise:
        st.warning(erro_analise)
    else:
        st.success(f"🎯 Probabilidade de vir acima de 10x: **{prob:.2f}%**")

# 🔁 Chamada da função principal
if __name__ == "__main__":
    main()
