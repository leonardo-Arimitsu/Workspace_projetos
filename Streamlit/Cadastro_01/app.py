# --------------------------
# Importação da Bibliotecas
# --------------------------

import streamlit as st
import pandas as pd
import os
from datetime import date

# -----------------------
# Fundação: Novo Cliente
# -----------------------

def novo_cliente():
    st.session_state["nome"] = ""
    st.session_state["endereco"] = ""
    st.session_state["dt_nasc"] = date.today()
    st.session_state["tipo_cliente"] = "Pessoa Fisica"

# -------
# Titulo
# -------

st.title("👨‍💼 Cadastro de Clientes")

# -------------------
# Campos do Cadastro
# -------------------

nome=st.text_input("Digite o nome do cliente: ", key="nome")
endereco=st.text_input("Digite o enderço do cliente", key="endereco")
data_nasc=st.date_input(
    "Selecione a data de nascimento do Cliente",
    key="dt_nasc",
    format="DD/MM/YYYY",
    value=None, # Campo data Vazio
    min_value=date(1900, 1, 1),
    max_value=date.today()
)
tipo_cliente=st.selectbox("Selecione o tipo Cliente", ["Pessoa Física", "Pessoa Jurídica"], key="tipo_cliente")

# -------
# Botões
# -------

col1, col2 = st.columns(2)
with col1:
    cadastrar=st.button(
        "Cadastrar Clientes", 
        use_container_width=True)

with col2:
    novo=st.button(
    "Novo Cadastro", 
    on_click=novo_cliente, 
    use_container_width=True)