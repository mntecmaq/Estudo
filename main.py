import streamlit as st

# 1. CSS para esconder a sidebar programaticamente
estilo_esconder_sidebar = """
    <style>
        [data-testid="stSidebar"][aria-expanded="true"] {
            display: none;
        }
    </style>
"""

# 2. Inicializamos uma variável para controlar a visibilidade
if 'mostrar_sidebar' not in st.session_state:
    st.session_state.mostrar_sidebar = False

# --- LÓGICA DE NAVEGAÇÃO ---
def clicar_item(pagina):
    st.session_state.pagina_atual = pagina
    # Aqui forçamos a sidebar a "sumir" mudando o estado
    st.session_state.mostrar_sidebar = False

# --- SIDEBAR ---
if st.session_state.mostrar_sidebar:
    with st.sidebar:
        st.title("Menu")
        if st.button("🏠 Home"):
            clicar_item("Home")
        if st.button("📊 Relatórios"):
            clicar_item("Relatórios")
else:
    # Se a sidebar estiver escondida, mostramos um botão para reabri-la
    if st.button("⬅️ Abrir Menu"):
        st.session_state.mostrar_sidebar = True
        st.rerun()

# --- CONTEÚDO ---
if 'pagina_atual' not in st.session_state:
    st.session_state.pagina_atual = "Home"

st.write(f"### Você está em: {st.session_state.pagina_atual}")
