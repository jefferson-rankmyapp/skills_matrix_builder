# utils/session_manager.py
import streamlit as st

def init_session():
    if "cargo" not in st.session_state:
        st.session_state["cargo"] = ""
    if "contexto" not in st.session_state:
        st.session_state["contexto"] = ""
    if "hard_skills" not in st.session_state:
        st.session_state["hard_skills"] = []
    if "objetivos" not in st.session_state:
        st.session_state["objetivos"] = {}  # Estrutura: {skill: {nivel: objetivo}}
    if "atividades" not in st.session_state:
        st.session_state["atividades"] = {}  # Estrutura: {skill: {nivel: [atividade1, ..., atividade4]}}
