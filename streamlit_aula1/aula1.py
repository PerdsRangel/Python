import streamlit as st
import pandas as pd

st.write("Olá, Mundo!")

nome = "Pedro"
idade = 18

st.write ("Olá, ", nome, " de ", idade, " anos.")

df = pd.DataFrame({
  'first column': ["Português", "Matemática", "Python", "Frame"],
  'second column': [5, 9, 7, 10]
})
st.title("Meu primeiro dash")
st.subheader("Pedro Rangel")
df

st.title("Caixa de Supermercado")

produtos = {
    "Arroz": 25.90,
    "Água": 8.50,
    "Feijão": 6.20,
    "Batata": 5.80,
    "Café": 14.90,
    "Sal": 4.20
}

produto_selecionado = st.selectbox(
    "Escolha um produto.",
    options=list(produtos.keys())
)

def calcular_preco(produto, qtd):
    preco = produtos[produto]
    return preco * qtd

st.divider()
st.metric(label="Preço:", value=f"R$ {produtos[produto_selecionado]:.2f}")