# modules/activities_stage.py
import streamlit as st
from utils.openai_assistant import get_suggestion
import json
import re

def render():
    st.header("Mapeamento das Atividades Típicas por Nível e Objetivo")
    
    # Verifica se as hard skills e os objetivos foram definidos
    hard_skills = st.session_state.get("hard_skills", [])
    objetivos = st.session_state.get("objetivos", {})
    
    if not hard_skills or len(hard_skills) != 4:
        st.warning("Por favor, defina as 4 hard skills na etapa anterior.")
        return
    if not objetivos or any(skill not in objetivos for skill in hard_skills):
        st.warning("Por favor, defina os objetivos para todas as hard skills antes de prosseguir.")
        return

    # Define os 5 níveis
    niveis = ["Assistente", "Júnior", "Pleno", "Sênior", "Especialista"]

    # Inicializa a estrutura de atividades no session_state, se necessário
    if "atividades" not in st.session_state:
        st.session_state["atividades"] = {}
    for skill in hard_skills:
        if skill not in st.session_state["atividades"]:
            st.session_state["atividades"][skill] = {nivel: ["" for _ in range(4)] for nivel in niveis}

    # Para cada hard skill, gera ou edita as atividades
    for skill in hard_skills:
        st.subheader(f"Atividades para a hard skill: {skill}")
        
        # Botão de "Ajuda do Assistente" para gerar atividades para essa skill com base nos objetivos
        if st.button(f"Ajuda do Assistente para atividades em {skill}", key=f"assist_atividades_{skill}"):
            # Monta prompt incorporando os objetivos para cada nível desta hard skill
            objetivos_skill = objetivos.get(skill, {})
            prompt_objetivos = "\n".join([f"{nivel}: {objetivos_skill.get(nivel, 'não definido')}" for nivel in niveis])
            prompt = (
                f"Considere a hard skill \"{skill}\" no contexto de um cargo com os seguintes objetivos para cada nível:\n"
                f"{prompt_objetivos}\n\n"
                "Para cada nível (Assistente, Júnior, Pleno, Sênior, Especialista), liste 4 atividades típicas que se espera que um profissional execute de forma eficaz, "
                "considerando o nível de maturidade e os objetivos informados. "
                "Formate a resposta no seguinte formato JSON, onde cada chave é o nome do nível e o valor é uma lista de 4 atividades, por exemplo:\n"
                "{\n  \"Assistente\": [\"Atividade 1\", \"Atividade 2\", \"Atividade 3\", \"Atividade 4\"],\n  ...\n}\n"
            )
            suggestion = get_suggestion(prompt, model="gpt-4o-mini", max_tokens=500)
            # Remove eventuais delimitadores Markdown
            suggestion_clean = re.sub(r"^```(json)?\s*|```$", "", suggestion, flags=re.MULTILINE).strip()
            try:
                atividades_geradas = json.loads(suggestion_clean)
                # Valida se todos os níveis foram retornados e se cada nível tem 4 atividades
                valid = True
                for nivel in niveis:
                    if nivel not in atividades_geradas or not isinstance(atividades_geradas[nivel], list) or len(atividades_geradas[nivel]) != 4:
                        valid = False
                        break
                if valid:
                    # Atualiza as atividades para essa skill
                    st.session_state["atividades"][skill] = {nivel: [atividade.strip() for atividade in atividades_geradas[nivel]] for nivel in niveis}
                    st.success(f"Atividades para {skill} atualizadas com sucesso!")
                else:
                    st.warning("A resposta do assistente não contém as atividades esperadas para todos os níveis. Edite manualmente.")
            except Exception as e:
                st.error(f"Erro ao processar a sugestão: {e}. Resposta recebida: {suggestion_clean}")

        # Exibe os campos editáveis para cada nível e suas 4 atividades
        for nivel in niveis:
            st.markdown(f"**Nível {nivel}:**")
            atividades_editaveis = []
            for i in range(4):
                key = f"{skill}_{nivel}_atividade_{i}"
                valor = st.text_input(f"Atividade {i+1}:", value=st.session_state["atividades"][skill][nivel][i], key=key)
                atividades_editaveis.append(valor)
            st.session_state["atividades"][skill][nivel] = atividades_editaveis

    # Botão para salvar as atividades atualizadas
    if st.button("Salvar Todas as Atividades", key="salvar_atividades"):
        erro = False
        for skill in hard_skills:
            for nivel in niveis:
                for i, atividade in enumerate(st.session_state["atividades"][skill][nivel]):
                    if not atividade.strip():
                        st.error(f"O campo Atividade {i+1} do nível {nivel} na hard skill '{skill}' está vazio.")
                        erro = True
        if not erro:
            st.success("Todas as atividades foram salvas com sucesso!")
