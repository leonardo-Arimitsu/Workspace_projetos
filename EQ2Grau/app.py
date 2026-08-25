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

# -------------------------
# Criação da função limpar
# -------------------------
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
            x1 = -b+math.sqrt(delta)/2*a
            x2 = -b-math.sqrt(delta)/2*a

            st.success("A equação possui duas raízes reais distintas")

            st.write(f"**x1 = {x1:.2f}**")
            st.write(f"**x2 = {x2:.2f}**")

# -------------------------
# Gráfico
# -------------------------

st.subheader("📊 Gráfico da Equação")

xv = -b/(2*a)

x = np.linspace(xv-10, xv+10, 500)
y = a*x**2 +b*x+c

fig, ax = plt.subplot(figsize=(8, 5))

ax.plot(x, y, linewidth=2, label="f(x)")

# -------------------------
# Eixos
# -------------------------

ax.axhline(0, linewidth=1)
ax.axvline(0, linewidth=1)

# -------------------------
# Vértice
# -------------------------

yv = a*xv**2+b*xv+c

ax.scatter(
    xv,
    yv,
    s=80,
    label="Vértice"
)

# -------------------------
# Raízes
# -------------------------

if delta>=0:
    if x1 is not None:
        ax.scatter(
            x1,
            0,
            s=80,
            label="Raíz x1"
        )
    if x2 is not None and delta >0:
        ax.scatter(
            x2,
            0,
            s=80,
            label="Raíz x2"
        )

ax.set_title(f"f(x) = {a}x² + {b}x + {c}")
ax.set_xlabel("x")
ax.set_ylabel("f(x)")
ax.grid(True)
ax.legend()

set.pylot(fig)

# -------------------------
# Informações adicionais
# -------------------------

st.subheader("📋 Informações Adicionais")