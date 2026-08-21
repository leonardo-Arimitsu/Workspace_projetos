# --------------------------
# Importação das bibliotecas
# --------------------------
import streamlit as st
import numpy as np # Biblioteca cientifica
import matplotlib.pyplot as plt #Biblioteca de construção grafica
import math

# -------------------------
# Configuração da páagina
# -------------------------

st.set_page_config(
    page_title="Equação do segundo grau",
    page_icon="📈",
    layout="centered"
)

# -------------------------
# Inicialização das variáveis
# -------------------------

if "a" not in st.session_state:
    st.session_state.a=1

if "b" not in st.session_state:
    st.session_state.b=0

if "c" not in st.session_state:
    st.session_state.c=0

def limpar():
    st.session_state.a=1
    st.session_state.b=0
    st.session_state.c=0

# -------------------------
# Interface
# -------------------------
st.title("🧮 Calculadora de Equações do Segundo Grau 🖩")

st.latex(r"ax^2 + xb + c")

st.write("Informe os coeficientes da equação:")

a = st.number_input("Coeficiente de a: ", key="a")
b = st.number_input("Coeficiente de b: ", key="b")
c = st.number_input("Coeficiente de c: ", key="c")

col1,col2 = st.columns(2)

with col1:
    calcular = st.button("⌨️ Calcular")

with col2:
    limpar = st.button("🆕 Novo Calculo", on_click=limpar)

# -------------------------
# Calcular
# -------------------------

if calcular:
    if a == 0:
        st.error("O coeficiente 'a' deve ser diferente de 0!")
    else:
        delta = b**2 - 4*a*c

        st.subheader("Resultado")

        st.write(f"**🔺= {delta:.1f}**")

        x1 = None
        x2 = None

        if delta < 0:
            st.warning("Está equação não possui raizes reais")
        elif delta == 0:
            x1 = -b/(2*a)
            st.success("A equação possui duas raízes iguais")
            st.write(f"**x1 = x2 = {x1:.1f}**")
        else:
            pass