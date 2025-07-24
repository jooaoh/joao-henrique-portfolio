import streamlit as st
import requests

# Define o estilo CSS para aplicar o tema escuro em todo o aplicativo
st.markdown(
    """
    <style>
    .stApp {background-color: #1a1a1a; color: #ffffff;}
    </style>
    """,
    unsafe_allow_html=True
)

# Cria a barra lateral para navegação
st.sidebar.title("Navegação")
if st.sidebar.button("Currículo"):
    st.session_state.page = "curriculo"
if st.sidebar.button("Projetos"):
    st.session_state.page = "projetos"
if st.sidebar.button("Arquivos"):
    st.session_state.page = "arquivos"

# Inicializa a sessão, se ainda não existir
if "page" not in st.session_state:
    st.session_state.page = "curriculo"

# Conteúdo baseado na página selecionada
if st.session_state.page == "curriculo":
    st.header("Sobre Mim")
    col1, col2 = st.columns([3, 1])
    with col1:
        st.write("")
        st.write("")
        st.write("Olá! Eu sou João Henrique. Trabalho com dados desde 2021.")
        st.write("Atuário formado pela UERJ | Analista de Dados Jr. - Gallagher Re")
        st.write("Excel, Power BI, Python, R Studio")
        st.write("https://www.linkedin.com/in/jo%C3%A3o-henrique-thole-ribeiro-4355ba1ba/")
    with col2:
        st.image("assets/CorpJoaoH.jpeg", width=800)  # Caminho relativo

    # URL de visualização direta do PDF no Google Drive
    pdf_id = "168wtaEWKim5yEfDvIbAU1Rl4Mfke8wL7"
    pdf_view_url = f"https://drive.google.com/file/d/{pdf_id}/preview"
    
    try:
        # Tentativa de baixar o PDF para o botão de download
        pdf_download_url = f"https://drive.google.com/uc?export=download&id={pdf_id}"
        pdf_content = requests.get(pdf_download_url, headers={"User-Agent": "Mozilla/5.0"}).content
                
        # Exibir PDF usando <iframe> com link de visualização
        pdf_display = f'<iframe src="{pdf_view_url}" width="100%" height="600" type="application/pdf"></iframe>'
        st.components.v1.html(pdf_display, height=600, scrolling=True)
    except requests.RequestException as e:
        st.error(f"Erro ao carregar o PDF: {e}. Verifique as permissões do Google Drive ou considere hospedar o arquivo em outro serviço (ex.: Dropbox).")

elif st.session_state.page == "projetos":
    st.header("Meus Projetos")
    st.subheader("1. Automação - Facilities")
    st.write("[joaohenrique.thole@gmail.com](mailto:joaohenrique.thole@gmail.com)")

elif st.session_state.page == "arquivos":
    st.header("Arquivos")
    st.write("Esta seção está em desenvolvimento. Adicione aqui os arquivos que deseja compartilhar!")
    st.write("[joaohenrique.thole@gmail.com](mailto:joaohenrique.thole@gmail.com)")


#git init
#git add .
#git commit -m "Initial commit with updated app"
#git remote add origin https://github.com/jooaoh/joao-henrique-portfolio.git
#git push -u origin main