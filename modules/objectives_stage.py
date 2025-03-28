# modules/objectives_stage.py
import streamlit as st
from utils.openai_assistant import get_suggestion
import json
import re

def render():
    st.header("Definição de Objetivos por Nível para Cada Hard Skill")
    
    # Verifica se as hard skills foram definidas na etapa anterior
    hard_skills = st.session_state.get("hard_skills", [])
    if not hard_skills or len(hard_skills) != 4:
        st.warning("Por favor, defina as 4 hard skills na etapa anterior.")
        return

    # Define os 5 níveis
    niveis = ["Assistente", "Júnior", "Pleno", "Sênior", "Especialista"]

    # Inicializa a estrutura de objetivos para cada hard skill, se necessário
    if "objetivos" not in st.session_state:
        st.session_state["objetivos"] = {}
    for skill in hard_skills:
        if skill not in st.session_state["objetivos"]:
            st.session_state["objetivos"][skill] = {nivel: "" for nivel in niveis}

    # Para cada hard skill, exibe os campos editáveis para os 5 níveis
    for skill in hard_skills:
        st.subheader(f"Objetivos para a hard skill: {skill}")
        
        # Botão de "Ajuda do Assistente" para gerar os 5 objetivos para essa skill
        if st.button(f"Ajuda do Assistente para {skill}", key=f"assist_obj_{skill}"):
            prompt = (
                f"Considere a hard skill \"{skill}\" no contexto de um cargo com as seguintes características:\n"
                f"Cargo: {st.session_state.get('cargo', 'não definido')}\n"
                f"Descrição: {st.session_state.get('contexto', 'não definido')}\n\n"
                "Para essa habilidade, forneça objetivos de desenvolvimento para cada nível de maturidade, "
                "que devem aumentar em complexidade e responsabilidade, conforme descrito abaixo:\n"
                "1. Assistente: objetivos básicos e de apoio.\n"
                "2. Júnior: objetivos com maior autonomia e execução de tarefas simples.\n"
                "3. Pleno: objetivos que envolvem planejamento e execução de processos mais complexos.\n"
                "4. Sênior: objetivos voltados à liderança, supervisão e resolução de problemas avançados.\n"
                "5. Especialista: objetivos que envolvem inovação, definição de padrões e orientação estratégica.\n\n"
                "Responda no seguinte formato JSON, onde cada chave é o nome do nível e o valor é o objetivo para esse nível:\n"
                "{\n  \"Assistente\": \"...\",\n  \"Júnior\": \"...\",\n  \"Pleno\": \"...\",\n  \"Sênior\": \"...\",\n  \"Especialista\": \"...\"\n}\n"
            )
            suggestion = get_suggestion(prompt, model="gpt-4o-mini", max_tokens=300)
            # Remove delimitadores de código Markdown, se presentes
            suggestion_clean = re.sub(r"^```(json)?\s*|```$", "", suggestion, flags=re.MULTILINE).strip()
            try:
                # Tenta converter a resposta em JSON
                objetivos_gerados = json.loads(suggestion_clean)
                # Valida se todos os níveis foram retornados
                if all(nivel in objetivos_gerados for nivel in niveis):
                    st.session_state["objetivos"][skill] = {nivel: objetivos_gerados[nivel].strip() for nivel in niveis}
                    st.success(f"Objetivos para {skill} atualizados com sucesso!")
                else:
                    st.warning("A resposta do assistente não contém os 5 níveis esperados. Edite manualmente.")
            except Exception as e:
                st.error(f"Erro ao processar a sugestão: {e}. Resposta recebida: {suggestion_clean}")
        
        # Exibe os campos editáveis para cada nível
        for nivel in niveis:
            key = f"{skill}_{nivel}_objetivo"
            if nivel not in st.session_state["objetivos"][skill]:
                st.session_state["objetivos"][skill][nivel] = ""
            valor = st.text_area(f"{nivel}:", value=st.session_state["objetivos"][skill].get(nivel, ""), key=key)
            st.session_state["objetivos"][skill][nivel] = valor

    # Botão para salvar os objetivos atualizados
    if st.button("Salvar Todos os Objetivos", key="salvar_objetivos"):
        erro = False
        for skill in hard_skills:
            for nivel in niveis:
                if not st.session_state["objetivos"][skill][nivel].strip():
                    st.error(f"O objetivo para o nível {nivel} da hard skill '{skill}' está vazio.")
                    erro = True
        if not erro:
            st.success("Todos os objetivos foram salvos com sucesso!")
