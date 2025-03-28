# modules/hard_skills_stage.py
import streamlit as st
from utils.openai_assistant import get_suggestion

def render():
    st.header("Definição das Hard Skills")
    
    # Recupera as informações de cargo e descrição (contexto) armazenadas na etapa "Input Inicial"
    cargo = st.session_state.get("cargo", "")
    descricao = st.session_state.get("contexto", "")
    
    if not cargo or not descricao:
        st.warning("Por favor, preencha as informações iniciais do cargo na etapa 'Input Inicial'.")
        return

    # Botão para gerar automaticamente as hard skills com base no cargo e descrição
    if st.button("Gerar Hard Skills", key="gerar_hard_skills"):
        prompt = (
            f"Com base no cargo '{cargo}' e na seguinte descrição:\n{descricao}\n"
            "Liste quatro hard skills essenciais para esse cargo, evitando citar tecnologias específicas, salvo quando estritamente necessário. "
            "Responda apenas com as hard skills, cada uma em uma nova linha."
        )
        suggestion = get_suggestion(prompt, model="gpt-4o-mini", max_tokens=150)
        # Processa a resposta: separa as skills por linha e remove espaços em branco
        hard_skills = [skill.strip() for skill in suggestion.split("\n") if skill.strip()]
        
        if len(hard_skills) != 4:
            st.warning("A sugestão não retornou exatamente 4 hard skills. Por favor, edite manualmente ou tente novamente.")
        st.session_state["hard_skills"] = hard_skills

    # Se ainda não houver hard skills definidas, inicializa com 4 campos vazios
    if "hard_skills" not in st.session_state or not st.session_state["hard_skills"]:
        st.session_state["hard_skills"] = ["", "", "", ""]

    st.subheader("Hard Skills Sugeridas e Editáveis")
    skills_editaveis = []
    for i, skill in enumerate(st.session_state["hard_skills"]):
        nova_skill = st.text_input(f"Skill {i+1}", value=skill, key=f"skill_{i}")
        skills_editaveis.append(nova_skill)
    st.session_state["hard_skills"] = skills_editaveis
    
    if st.button("Salvar Hard Skills", key="salvar_hard_skills"):
        # Validação: deve haver exatamente 4 hard skills não vazias
        if len(st.session_state["hard_skills"]) != 4 or any(not s.strip() for s in st.session_state["hard_skills"]):
            st.error("Por favor, preencha exatamente 4 hard skills válidas.")
        else:
            st.success("Hard skills salvas!")
