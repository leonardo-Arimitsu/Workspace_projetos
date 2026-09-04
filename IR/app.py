# mostrar imposto de renda
# pedir salario bruto
# calcular porcentual de desconto

# --------------------------
# Importação da Bibliotecas
# --------------------------

import streamlit as st
import pandas as pd

# ------------------------
# Configuração da página
# ------------------------

st.set_page_config(
    page_title="Calculo de Imposto de Renda",
    page_icon="📉",
    layout="centered"
)
 
st.title("Tabela de imposto de Renda")

# ---------------------------
# Tabela de Imposto de Renda
# ---------------------------

dados={
    'salario':["Até 2.428,80", "2.428,81 – 2.826,65", "2.826,66 – 3.751,05", "3.751,06 – 4.664,68", "Acima de 4.664,68"],
    'aliquota':["Isento", "7,5%", "15%", "22,5%", "27,5%"],
    'Dedução':["Jorge você não paga cara", "182.16", "394.16", "675.49", "908.73"]
}

df = pd.DataFrame(dados)
st.table(df)

# -------------------
# Calculo de Imposto
# -------------------

salario = st.number_input("Digite seu sálario: ")

# ----------------------------
# Botão para realizar calculo
# ----------------------------

calcular = st.button("⌨️ Calcular")

if calcular:

    # ------------------------------------
    # Condições para o calculo de imposto
    # ------------------------------------

    if salario <= 2428.80:
        st.write("Você é isento de imposto de renda")

    elif salario >= 2428.81 and salario <= 2826.65:
        reducao = salario*(7.5/100)-182.16
        st.write(f"Você tem que pagar {reducao:.2f} de imposto") # a vida é complicada tem que pagar imposto

    elif salario >= 2826.66 and salario <= 3751.05:
        reducao = salario*(15/100)-394.16
        st.write(f"Você tem que pagar {reducao:.2f} de imposto")

    elif salario >= 3751.06 and salario <= 4664.68:
        reducao = salario*(22.5/100)-675.49
        st.write(f"Você tem que pagar {reducao:.2f} de imposto")

    else:
        reducao = salario*(27.5/100)-908.73
        st.write(f"Você tem que pagar {reducao:.2f} de imposto")