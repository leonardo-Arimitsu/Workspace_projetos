import streamlit as st
import pandas as pd

st.title("Exemplos de tabelas")

dados={
    'Produto':["notebook", "Smartphone", "Teclado", "mickey Mouse"],
    'Quantidade':[151,30,25,50],
    'Preço (R$)':[3500,1800,300,2000]
}

# Converter os valores em tabela
df = pd.DataFrame(dados)

st.subheader("Opção 1: Tabela Estática")
st.table(df)

st.subheader("Opção 2: Tabela Dinâmica")
st.dataframe(df)