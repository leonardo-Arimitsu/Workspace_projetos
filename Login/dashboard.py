import streamlit as st
from conexao import conectar

# Função principal do Dashboard

def exibir():
    st.title("📊Dashboard Administração")
    st.write(
        f"Bem-vindo(a), {st.session_state.usuario}!"
    )

    # <hr>
    st.divider()

    # Menu lateral
    st.sidebar.title("Menu principal")
    menu = st.sidebar.selectbox(
        "Selecione uma opção",
        [
            "Dashboard",
            "Cadastro de Usuários",
            "Consultar Usuários",       
        ]
    )

    # Botão sair
    st.sidebar.divider()
    if st.sidebar.button(
        "🚪Sair"
    ):