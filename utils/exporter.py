# utils/exporter.py
import pandas as pd
import streamlit as st

def export_matrix():
    cargo = st.session_state.get("cargo", "Não definido")
    # Removemos o contexto da matriz exportada
    hard_skills = st.session_state.get("hard_skills", [])
    objetivos = st.session_state.get("objetivos", {})
    atividades = st.session_state.get("atividades", {})

    # Cria uma linha para cada atividade (4 atividades por combinação de hard skill e nível)
    data = []
    niveis = ["Assistente", "Júnior", "Pleno", "Sênior", "Especialista"]
    for skill in hard_skills:
        for nivel in niveis:
            objetivo = objetivos.get(skill, {}).get(nivel, "")
            atividades_list = atividades.get(skill, {}).get(nivel, [])
            for atividade in atividades_list:
                row = {
                    "Cargo": cargo,
                    "Hard Skill": skill,
                    "Nível": nivel,
                    "Objetivo": objetivo,
                    "Atividade": atividade
                }
                data.append(row)
    df = pd.DataFrame(data)
    return df
