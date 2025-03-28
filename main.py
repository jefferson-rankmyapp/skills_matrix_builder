# main.py
import streamlit as st
from config import APP_NAME
from modules import input_stage, hard_skills_stage, objectives_stage, activities_stage, review_stage, documentation_stage
from utils.session_manager import init_session

def main():
    st.set_page_config(page_title=APP_NAME, layout="wide")
    st.title(APP_NAME)

    # Inicializa a sessão com os dados necessários
    init_session()

    # Navegação por etapas
    etapas = [
        "1. Input Inicial",
        "2. Definição das Hard Skills",
        "3. Definição dos Objetivos",
        "4. Mapeamento das Atividades",
        "5. Revisão e Exportação"
        
    ]
    
    etapa_atual = st.sidebar.radio("Selecione a etapa", etapas)
    
    if etapa_atual == "1. Input Inicial":
        input_stage.render()
    elif etapa_atual == "2. Definição das Hard Skills":
        hard_skills_stage.render()
    elif etapa_atual == "3. Definição dos Objetivos":
        objectives_stage.render()
    elif etapa_atual == "4. Mapeamento das Atividades":
        activities_stage.render()
    elif etapa_atual == "5. Revisão e Exportação":
        review_stage.render()

if __name__ == '__main__':
    main()
