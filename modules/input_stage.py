# modules/input_stage.py
import streamlit as st

def render():
    st.header("Informações Iniciais do Cargo")
    cargo = st.text_input("Informe o nome do cargo:", value=st.session_state.get("cargo", ""))
    contexto = st.text_area("Descreva o contexto e as responsabilidades do cargo:", value=st.session_state.get("contexto", ""))
    
    if st.button("Salvar e Continuar"):
        st.session_state["cargo"] = cargo
        st.session_state["contexto"] = contexto
        st.success("Informações iniciais salvas!")

    st.header("Documentação - Guia do People.AI")
    with st.expander("Clique para ver o guia completo"):
        doc_text = """
        # People.AI - Assistente para Matriz de Habilidades

        Bem-vindo ao **People.AI**! 🚀

        Se você chegou até aqui, é porque quer criar uma matriz de habilidades estruturada, clara e super útil para acompanhar o desenvolvimento profissional da sua equipe. O **People.AI** veio para tornar esse processo mais fácil e inteligente!

        Nosso assistente usa inteligência artificial para sugerir **Hard Skills**, definir **objetivos por nível** e listar **atividades típicas** que cada profissional deve dominar ao longo do tempo.

        Agora, bora entender como tudo funciona? 👇

        ---

        ## 🎯 Passo 1: Definição do Cargo e Contexto
        Aqui é onde tudo começa! Para que possamos sugerir uma matriz de habilidades coerente, precisamos entender qual cargo estamos mapeando. Você só precisa:
        1. **Selecionar o cargo** da pessoa que deseja mapear.
        2. **Descrever em detalhes** o que esse cargo faz na empresa. Você também pode colar o descritivo do cargo no campo de texto.
        3. **Clicar no botão "Ajuda do Assistente"** caso queira sugestões automáticas.
        Depois disso, avançamos para as **Hard Skills**!

        ---

        ## 🛠️ Passo 2: Definição das Hard Skills
        Nesta etapa, vamos definir as **quatro principais Hard Skills** para o cargo.
        - O assistente já sugere quatro opções baseadas no cargo e na descrição fornecida.
        - Se quiser, você pode editar as sugestões ou inserir suas próprias habilidades.
        - O ideal é que as Hard Skills sejam amplas o suficiente para cobrir as principais competências do cargo, mas sem mencionar tecnologias específicas (a menos que seja realmente necessário).

        ---

        ## 🎯 Passo 3: Definição de Objetivos por Nível
        Agora que temos as Hard Skills, precisamos definir **o que um profissional precisa atingir em cada nível de maturidade**.
        Cada Hard Skill será detalhada em **cinco níveis**:
        1. **Assistente**
        2. **Júnior**
        3. **Pleno**
        4. **Sênior**
        5. **Especialista**

        - O assistente gera automaticamente um objetivo para cada nível.
        - Você pode revisar e editar cada objetivo antes de seguir para a próxima etapa.
        - Lembre-se: o objetivo deve **evoluir em complexidade** à medida que o profissional sobe de nível!

        ---

        ## 🏗️ Passo 4: Atividades Típicas por Nível e Objetivo
        Agora que temos os objetivos bem definidos, precisamos quebrá-los em **atividades típicas**.
        - Para cada **objetivo de cada nível**, o assistente gera **quatro atividades típicas**.
        - Essas atividades representam **ações concretas** que o profissional deve realizar para atingir aquele objetivo.
        - Você pode revisar e ajustar cada uma delas!

        Isso nos leva à **matriz final**! 🎉

        ---

        ## 📋 Passo 5: Revisão e Exportação
        Aqui você pode visualizar toda a matriz, fazer ajustes finais e exportar o resultado. O formato final conterá:
        - **Cargo**
        - **Hard Skills**
        - **Níveis**
        - **Objetivos**
        - **Atividades típicas**

        - O assistente exibe a matriz em formato de tabela.
        - Você pode fazer um **download em CSV** para compartilhar ou importar em outras ferramentas.

        ---

        ## 🎉 Pronto! Agora é só usar a Matriz de Habilidades!
        Parabéns! Agora você tem uma matriz de habilidades **completa**, estruturada e pronta para ajudar no desenvolvimento profissional da sua equipe. 🚀

        Se precisar de ajustes, você sempre pode voltar a qualquer etapa e modificar as informações.

        Divirta-se explorando o **People.AI** e criando matrizes de habilidades cada vez melhores! 💡😃
        """
        st.markdown(doc_text)