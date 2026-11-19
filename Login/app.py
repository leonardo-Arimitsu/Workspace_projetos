
from conexao import conectar
import streamlit as st
import dashboard

# Configurando a página
st.set_page_config(
    page_title="Sistema de login",
    page_icon="🔐",
    layout="centered"
)

# Controle da sessão
if "logado" not in st.session_state:
    st.session_state.logado = False

if "usuario" not in st.session_state:
    st.session_state.usuario = ""

# Função para verificação de login
def verificar_login(usuario, senha):

    conexao = conectar()
    cursor = conexao.cursor()

    # Instruções de multiplas linhas
    sql = """
        SELECT id, usuario
        FROM usuarios
        WHERE usuario = %s
        AND senha = %s
    """

    cursor.execute(sql, (usuario, senha))

    resultado = cursor.fetchone()

    cursor.close()
    conexao.close()

    return resultado


# Tela de login
if not st.session_state.logado:

    st.title("🔐 Sistema de login")
    st.write("Informe suas credenciais para acessar o sistema.")
    st.divider()

    usuario = st.text_input("Usuário")

    senha = st.text_input(
        "Senha",
        type="password"
    )

    if st.button("Entrar", use_container_width=True):

        if usuario and senha:

            try:
                resultado = verificar_login(
                    usuario,
                    senha
                )

                if resultado:

                    st.session_state.logado = True
                    st.session_state.usuario = resultado[1]

                    st.success("Acesso autorizado!")

                    st.rerun()

                else:
                    st.error("Usuário ou senha incorretos!")

            except Exception as error:
                st.error(f"Erro ao acessar o banco: {error}")

        else:
            st.warning("Preencha o usuário e a senha!")

# Redirecionamento para o dashboard
if st.session_state.logado:

    dashboard.exibir()