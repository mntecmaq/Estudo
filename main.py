import streamlit as st

# 1. Configuração da página (ajuda no mobile)
st.set_page_config(page_title="App Estudo", initial_sidebar_state="expanded")

# --- SIDEBAR ---
with st.sidebar:
    st.title("Navegação 🚀")
    
    # A Selectbox já retorna o valor selecionado instantaneamente
    pagina = st.selectbox(
        "Para onde vamos?",
        ["Home", "Relatórios", "Configurações"],
        index=0  # Começa na Home
    )
    
    st.divider()
    st.info("No celular, toque fora do menu para ele recolher automaticamente.")

# --- CONTEÚDO PRINCIPAL ---
# A lógica aqui é direta: mudou a selectbox, muda o conteúdo.
if pagina == "Home":
    st.header("🏠 Página Inicial")
    st.write("Você selecionou a Home. O conteúdo muda sem cliques duplos!")
    
elif pagina == "Relatórios":
    st.header("📊 Área de Dados")
    st.bar_chart([10, 30, 20, 50])
    
elif pagina == "Configurações":
    st.header("⚙️ Ajustes")
    st.toggle("Modo Escuro")
    st.slider("Volume da Notificação", 0, 100, 50)

