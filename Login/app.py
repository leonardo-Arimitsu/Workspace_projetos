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
    st.session_state=False

if "usuario" not in st.session_state:
    st.session_state=""

# Função para verificação de login
def verificar_login(usuario, senha):
    conexao=conectar()

    cursor= conexao.cursor()

    # Instruções de multiplas linhas
    sql="""
        select id, usuario
        from usuarios
        where usuario=%s
        and senha=%s
    """

    cursor.execute(sql, (usuario, senha))

    resultado=cursor.fetchone()

    cursor.close()

    conexao.close()

    return resultado

# Tela de login
if not st.session_state.logado:
    st.title("🔐Sistema de login")
    st.write("Informe suas credenciais para acessar o sistema.")
    st.divider()

    usuario=st.text_input(
        "Usuario"
    )

    senha=st.text_input(
        "Senha"
    )

if st.button("Entrar", use_container_width=True):
    if usuario and senha:
        try:
            resultado=verificar_login(
                usuario,
                senha
            )
            if resultado:
                st.session_state.logado=True
                st.session_state.usuario=resultado[1]
                st.success("Acesso autorizado!")
                st.rerun
            else:
                st.error("Usuario ou senha incorretos")
        except Exception as error:
            st.error("Erro ao acessar o banco:[erro]")
    else:
        st.warning("Preencha o usuario e a senha!")

# Redirecionando o usuario para o arquivo dashboard
else:
    dashboard.exibir()