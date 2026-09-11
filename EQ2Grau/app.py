import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import math

# ------------------------
# Configuração da página
# ------------------------

st.set_page_config(
    page_title="Equação do segundo grau",
    page_icon="📈",
    layout="centered"
)

# ----------------------------
# Inicialização das variáveis
# ----------------------------

if "a" not in st.session_state:
    st.session_state.a = 1

if "b" not in st.session_state:
    st.session_state.b = 0

if "c" not in st.session_state:
    st.session_state.c = 0

# -------------------------
# Função limpar
# -------------------------

def limpar_campos():
    st.session_state.a = 1
    st.session_state.b = 0
    st.session_state.c = 0

# ----------
# Interface
# ----------

st.title("🧮 Calculadora de Equações do Segundo Grau 🖩")

st.latex(r"ax^2 + bx + c")

st.write("Informe os coeficientes da equação:")

a = st.number_input("Coeficiente de a:", key="a")
b = st.number_input("Coeficiente de b:", key="b")
c = st.number_input("Coeficiente de c:", key="c")

col1, col2 = st.columns(2)

with col1:
    calcular = st.button("⌨️ Calcular")

with col2:
    st.button(
        "🆕 Novo Cálculo",
        on_click=limpar_campos
    )

# ----------------
# Variáveis
# ----------------

delta = None
x1 = None
x2 = None

# ----------------
# Calcular
# ----------------

if calcular:

    if a == 0:
        st.error("O coeficiente 'a' deve ser diferente de 0!")

    else:
        delta = b**2 - 4*a*c

        st.subheader("Resultado")

        st.write(f"**🔺 Δ = {delta:.1f}**")

        if delta < 0:

            st.warning(
                "Esta equação não possui raízes reais."
            )

        elif delta == 0:

            x1 = -b / (2*a)

            st.success(
                "A equação possui duas raízes iguais."
            )

            st.write(f"**x1 = x2 = {x1:.2f}**")

        else:

            x1 = (-b + math.sqrt(delta)) / (2*a)
            x2 = (-b - math.sqrt(delta)) / (2*a)

            st.success(
                "A equação possui duas raízes reais distintas."
            )

            st.write(f"**x1 = {x1:.2f}**")
            st.write(f"**x2 = {x2:.2f}**")

# ----------------
# Gráfico
# ----------------

st.subheader("📊 Gráfico da Equação")

if a != 0:

    xv = -b / (2*a)

    x = np.linspace(xv - 10, xv + 10, 500)
    y = a*x**2 + b*x + c

    fig, ax = plt.subplots(figsize=(8, 5))

    ax.plot(
        x,
        y,
        linewidth=2,
        label="f(x)"
    )

    # Eixos
    ax.axhline(0, linewidth=1)
    ax.axvline(0, linewidth=1)

    # Vértice
    yv = a*xv**2 + b*xv + c

    ax.scatter(
        xv,
        yv,
        s=80,
        label="Vértice"
    )

    # Raízes
    if delta is not None and delta >= 0:

        if x1 is not None:
            ax.scatter(
                x1,
                0,
                s=80,
                label="Raiz x1"
            )

        if x2 is not None and delta > 0:
            ax.scatter(
                x2,
                0,
                s=80,
                label="Raiz x2"
            )

    ax.set_title(
        f"f(x) = {a}x² + {b}x + {c}"
    )

    ax.set_xlabel("x")
    ax.set_ylabel("f(x)")
    ax.grid(True)
    ax.legend()

    st.pyplot(fig)

else:

    st.warning(
        "O gráfico só pode ser exibido para uma equação do segundo grau, "
        "portanto 'a' deve ser diferente de 0."
    )

# -----------------------
# Informações adicionais
# -----------------------

st.subheader("📋 Informações Adicionais")

if a > 0:

    st.write(
        "A parábola possui a concavidade voltada para cima."
    )

elif a < 0:

    st.write(
        "A parábola possui a concavidade voltada para baixo."
    )

else:

    st.write(
        "Não é uma equação do segundo grau."
    )
