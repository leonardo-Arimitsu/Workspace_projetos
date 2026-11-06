import streamlit as st
import mysql.connector

conexao = mysql.connector.connect(
    host="localhost",
    user="ETECPJ2DSB",
    password="123456",
    database="login_DB"
)

if conexao.is_connected():
    st.success("Banco de dados conectado com sucesso")

conexao.close()