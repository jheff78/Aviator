import streamlit as st

st.set_page_config(page_title="Analisador Aviator", layout="centered")
st.title("🎯 Analisador de Velas – H2Bet Manual")
st.markdown("Cole abaixo as **últimas 20 velas** (ex: `1.2, 10.5, 3.4...`)")

entrada = st.text_input("🕹️ Digite as 20 velas separadas por vírgula")

if entrada:
    try:
        velas = [float(v.strip()) for v in entrada.split(",") if v.strip()]

        if len(velas) != 20:
            st.warning("⚠️ Você precisa inserir **exatamente 20 valores numéricos.**")
        else:
            # Cálculo
            maiores_10 = [v for v in velas if v >= 10]
            menores_2 = [v for v in velas if v < 2]
            ultimas_5 = velas[-5:]

            ultima_10x_index = next((i for i, v in enumerate(reversed(velas)) if v >= 10), None)

            st.subheader("📊 Estatísticas")
            st.metric("Velas ≥ 10x", len(maiores_10))
            st.metric("Velas < 2x", len(menores_2))
            st.metric("Porcentagem ≥ 10x", f"{(len(maiores_10) / 20) * 100:.2f}%")

            if ultima_10x_index is not None:
                st.info(f"⏱️ {ultima_10x_index} velas se passaram desde a última ≥ 10x")
            else:
                st.error("🚨 Nenhuma ≥ 10x nas últimas 20!")

            st.subheader("📈 Tendência")
            if len(maiores_10) == 0:
                st.warning("🧊 Sessão FRIA: nenhuma ≥ 10x")
            elif ultima_10x_index >= 10:
                st.success("🔥 Sessão pode estar ESQUENTANDO")
            else:
                st.info("📉 Sessão ESTÁVEL")

            st.subheader("📉 Gráfico das 20 velas")
            st.line_chart(velas)

            st.subheader("📋 Últimas 5 velas:")
            for i, v in enumerate(reversed(ultimas_5), 1):
                if v >= 10:
                    st.success(f"#{i}: 🔥 {v}x")
                elif v < 2:
                    st.error(f"#{i}: ⚠️ {v}x")
                else:
                    st.write(f"#{i}: {v}x")

    except Exception as e:
        st.error(f"❌ Erro ao processar os dados: {str(e)}")
else:
    st.info("👆 Insira as velas para começar a análise.")
