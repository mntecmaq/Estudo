import streamlit as st

# 1. Configuração para esconder a sidebar por padrão em telas pequenas
st.set_page_config(initial_sidebar_state="collapsed")

# 2. Função que processa a escolha e "limpa" o estado
def navegar_para(pagina):
    st.session_state.pagina_atual = pagina
    # Aqui, no Streamlit, a sidebar recolhe automaticamente no mobile 
    # após a interação que causa o "rerun" do script.

# 3. Inicializa a página padrão
if 'pagina_atual' not in st.session_state:
    st.session_state.pagina_atual = "Home"

# --- SIDEBAR ---
with st.sidebar:
    st.title("Menu Inteligente")
    
    # Criamos botões em vez de radio para forçar a ação de clique
    if st.button("🏠 Ir para Home"):
        navegar_para("Home")
        
    if st.button("📊 Ver Relatórios"):
        navegar_para("Relatórios")

# --- LÓGICA DE EXIBIÇÃO ---
if st.session_state.pagina_atual == "Home":
    st.header("Você está na Home")
    st.write("A sidebar deve ter recolhido se você estiver no celular.")

elif st.session_state.pagina_atual == "Relatórios":
    st.header("Relatórios Detalhados")
    st.line_chart([1, 5, 2, 6, 3])
