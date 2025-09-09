import streamlit as st

def imc(altura, peso):
    imc = peso/(altura**2)
    return imc
def c_imc(imc):
    if imc <=18.5:
        categoria = "Abaixo do peso"
    elif imc <=24.9:
        categoria = "Peso normal"
    elif imc <=29.9:
        categoria = "Sobre peso"
    elif imc <=34.9:
        categoria = "Obesidade I"
    elif imc <=39.9:
        categoria = "Obesidade II"
    else:
        categoria = "Obesidade III"
    return categoria

# ---------------------------
# Configuração da página
# ---------------------------
st.set_page_config(
    page_title="Calculadora de IMC",
    page_icon="⚖️",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# ---------------------------
# Cabeçalho
# ---------------------------
st.title("⚖️ Calculadora de IMC")
st.caption("Template decorativo — funcionalidade será feita em sala 🚀")

st.divider()

# ---------------------------
# Área de Destaque
# ---------------------------
col1, col2 = st.columns([2, 1])
with col1:
    st.subheader("Sobre o IMC")
    st.markdown(
        """
        O **Índice de Massa Corporal (IMC)** é uma medida usada para avaliar
        se uma pessoa está dentro de uma faixa considerada saudável de peso
        em relação à altura.

        👉 Neste app, você poderá:
        - Inserir seu peso e altura  
        - Calcular automaticamente o IMC  
        - Ver em qual **categoria** você se encontra  
        """
    )
with col2:
    st.image(
        "https://cdn-icons-png.flaticon.com/512/3103/3103446.png",
        caption="Ilustração IMC",
        use_column_width=True,
    )

st.divider()

# ---------------------------
# Espaço reservado para o formulário
# ---------------------------
st.markdown("## 📋 Área do formulário")

peso = st.number_input("Digite o seu peso:", min_value=10.0, max_value=300.0)
altura = st.number_input("Digite a sua altura:", min_value=1.0, max_value=3.0)
imc = peso/(altura**2)

botao_imc = st.button("CALCULAR")

st.divider()

# ---------------------------
# Seção de Resultados (Placeholder)
# ---------------------------
st.markdown("## 📊 Resultados")
colA, colB, colC = st.columns(3)
colA.metric("IMC", f"{imc}")
colB.metric("Categoria", f"{c_imc(imc)}")
colC.metric("Peso saudável", "--")

st.progress(0)  # Barra de progresso "decorativa"

st.warning("⚠️ Os resultados aparecerão aqui após o cálculo.")

st.divider()

# ---------------------------
# Tabela de Classificação
# ---------------------------
st.markdown(
    """
    ### Classificação (adultos)
    | IMC (kg/m²) | Categoria      |
    |-------------|----------------|
    | < 18,5      | Abaixo do peso |
    | 18,5 – 24,9 | Peso normal    |
    | 25,0 – 29,9 | Sobrepeso      |
    | 30,0 – 34,9 | Obesidade I    |
    | 35,0 – 39,9 | Obesidade II   |
    | ≥ 40,0      | Obesidade III  |
    """
)

st.divider()
st.caption("© 2025 • Template IMC para prática em sala")

if botao_imc:
    print()