import streamlit as st

# Configuração da página
st.set_page_config(page_title="Meu App com Sidebar", layout="wide")

# --- SIDEBAR ---
with st.sidebar:
    st.title("Menu de Navegação")
    opcao = st.radio(
        "Escolha uma página:",
        ("Home", "Relatórios", "Configurações")
    )
    
    st.info("Dica: Você pode adicionar filtros e logos aqui!")

# --- CONTEÚDO PRINCIPAL ---
if opcao == "Home":
    st.header("Bem-vindo à Home")
    st.write("Esta é a área principal do seu aplicativo.")

elif opcao == "Relatórios":
    st.header("Página de Relatórios")
    st.bar_chart({"Dados": [10, 20, 15, 25, 30]})

elif opcao == "Configurações":
    st.header("Configurações")
    st.checkbox("Ativar notificações")
