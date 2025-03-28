# utils/openai_assistant.py
import os
import openai
from dotenv import load_dotenv

# Carrega variáveis do .env
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def get_suggestion(prompt, model="gpt-4o-mini", temperature=0.7, max_tokens=150):
    """
    Envia um prompt para a API da OpenAI e retorna a sugestão usando a nova interface ChatCompletion.
    """
    try:
        response = openai.chat.completions.create(
            model=model,
            messages=[
                {"role": "user", "content": prompt}
            ],
            temperature=temperature,
            max_tokens=max_tokens
        )
        suggestion = response.choices[0].message.content.strip()
        return suggestion
    except Exception as e:
        return f"Erro ao obter sugestão: {e}"
