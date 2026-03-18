import streamlit as st
import pandas as pd
from supabase import create_client

# 1. Conexão com o Supabase
url = st.secrets["SUPABASE_URL"]
key = st.secrets["SUPABASE_KEY"]
supabase = create_client(url, key)

def carregar_dashboard():
    st.title("📊 Painel de Controle de Estoque")

    # 2. Buscar dados da VIEW que criamos no SQL
    # A View 'estoque_atual' já faz todo o cálculo de (Entradas - Saídas)
    resposta = supabase.table("estoque_atual").select("*").execute()
    df_estoque = pd.DataFrame(resposta.data)

    if df_estoque.empty:
        st.info("Nenhum dado de estoque encontrado. Comece cadastrando produtos e entradas.")
        return

    # 3. Métricas Principais (Cards)
    total_itens = len(df_estoque)
    itens_baixo_estoque = df_estoque[df_estoque['saldo_atual'] <= df_estoque['estoque_minimo']]
    
    col1, col2, col3 = st.columns(3)
    col1.metric("Produtos Cadastrados", total_itens)
    col2.metric("Itens Críticos", len(itens_baixo_estoque), delta_color="inverse")
    col3.metric("Total em Saldo", int(df_estoque['saldo_atual'].sum()))

    st.divider()

    # 4. Alerta de Reposição (Apenas o que está acabando)
    if not itens_baixo_estoque.empty:
        st.error("⚠️ **Atenção: Itens abaixo do estoque mínimo!**")
        st.dataframe(
            itens_baixo_estoque[['produto_nome', 'saldo_atual', 'estoque_minimo']],
            use_container_width=True,
            hide_index=True
        )
    else:
        st.success("✅ Todos os itens estão com estoque em dia.")

    # 5. Gráfico de Barras - Saldo por Produto
    st.subheader("Estoque por Item")
    st.bar_chart(data=df_estoque, x="produto_nome", y="saldo_atual")

    # 6. Tabela Geral Detalhada
    with st.expander("Ver Inventário Completo"):
        st.table(df_estoque[['produto_nome', 'entradas', 'saidas', 'saldo_atual', 'estoque_minimo']])

# Execução do Dashboard
# carregar_dashboard()
