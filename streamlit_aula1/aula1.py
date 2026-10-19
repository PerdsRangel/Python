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

st.set_page_config(page_title= "Mercados Pedro - Produtos Gulosos", page_icon="mercadospedro.jpg", layout="centered")

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

preco_unitario = produtos[produto_selecionado]
st.metric(label=f"Preço Unitário ({produto_selecionado}):", value=f"R$ {preco_unitario:.2f}")

col1, col2 = st.columns(2)

with col1:
    qtd = st.number_input("Quantidade de itens", min_value=1, value=1, step=1)

with col2:
    valor_pago = st.number_input("Valor pago em dinheiro (R$)", min_value=0.0, value=0.0, step=1.0)

total_compra = preco_unitario * qtd
st.info(f"**Valor total da compra:** R$ {total_compra:.2f}")

if st.button("Calcular Troco", type="primary"):
    if valor_pago < total_compra:
        st.error(f"Falta dinheiro! O valor pago (R$ {valor_pago:.2f}) é menor que o total (R$ {total_compra:.2f}).")
    else:
        troco = valor_pago - total_compra
        st.success(f"**Troco a devolver:** R$ {troco:.2f}")
