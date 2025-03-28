# modules/review_stage.py
import streamlit as st
from utils.exporter import export_matrix

def render():
    st.header("Revisão e Exportação da Matriz")
    
    cargo = st.session_state.get("cargo", "Não definido")
    # Removemos o contexto da revisão
    st.subheader("Resumo")
    st.write("**Cargo:**", cargo)
    st.write("**Hard Skills:**", st.session_state.get("hard_skills", []))
    st.write("**Objetivos:**", st.session_state.get("objetivos", {}))
    st.write("**Atividades:**", st.session_state.get("atividades", {}))
    
    st.subheader("Exportar Matriz")
    df = export_matrix()
    st.dataframe(df)  # Exibe a grade final com cada atividade em uma linha (80 linhas no total)
    
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="Download CSV",
        data=csv,
        file_name="skills_matrix - " + cargo + ".csv",
        mime="text/csv",
    )
