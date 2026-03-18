import streamlit as st
import random

# Configuração da página
st.set_page_config(page_title="Jogo da Forca Python", page_icon="🪑")

# Lista de palavras para o jogo
PALAVRAS = ["PYTHON", "STREAMLIT", "PROGRAMACAO", "INTELIGENCIA", "DADOS", "COMPUTADOR"]

def inicializar_jogo():
    st.session_state.palavra = random.choice(PALAVRAS).upper()
    st.session_state.letras_corretas = set()
    st.session_state.letras_erradas = set()
    st.session_state.tentativas_restantes = 6
    st.session_state.jogando = True

# Inicializa o estado do jogo se não existir
if 'palavra' not in st.session_state:
    inicializar_jogo()

st.title("🪑 Jogo da Forca")

# Exibição da palavra oculta
palavra_exibida = ""
for letra in st.session_state.palavra:
    if letra in st.session_state.letras_corretas:
        palavra_exibida += letra + " "
    else:
        palavra_exibida += "_ "

st.header(f"`{palavra_exibida.strip()}`")

# Informações de status
col1, col2 = st.columns(2)
with col1:
    st.write(f"❤️ Tentativas restantes: **{st.session_state.tentativas_restantes}**")
with col2:
    st.write(f"🚫 Letras erradas: {', '.join(st.session_state.letras_erradas)}")

# Lógica do palpite
if st.session_state.tentativas_restantes > 0 and "_" in palavra_exibida:
    with st.form(key='chute_form', clear_on_submit=True):
        letra_chute = st.text_input("Digite uma letra:").upper()
        botao_chutar = st.form_submit_button("Chutar")

    if botao_chutar and letra_chute:
        if len(letra_chute) != 1 or not letra_chute.isalpha():
            st.warning("Por favor, digite apenas uma letra.")
        elif letra_chute in st.session_state.letras_corretas or letra_chute in st.session_state.letras_erradas:
            st.info(f"Você já tentou a letra {letra_chute}!")
        elif letra_chute in st.session_state.palavra:
            st.session_state.letras_corretas.add(letra_chute)
            st.success(f"Boa! A letra {letra_chute} existe na palavra.")
            st.rerun()
        else:
            st.session_state.letras_erradas.add(letra_chute)
            st.session_state.tentativas_restantes -= 1
            st.error(f"Putz! A letra {letra_chute} não existe.")
            st.rerun()

# Verificação de vitória ou derrota
if "_" not in palavra_exibida:
    st.balloons()
    st.success(f"Parabéns! Você venceu! A palavra era: **{st.session_state.palavra}**")
    if st.button("Jogar Novamente"):
        inicializar_jogo()
        st.rerun()

elif st.session_state.tentativas_restantes <= 0:
    st.error(f"Game Over! A palavra era: **{st.session_state.palavra}**")
    if st.button("Tentar Novamente"):
        inicializar_jogo()
        st.rerun()
