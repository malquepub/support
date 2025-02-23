import streamlit as st
import openai

# Configurar título do app
st.set_page_config(page_title="Ana - Assistente da Malke Publishing", page_icon="📚")

# Exibir título e introdução
st.title("📚 Ana - Assistente da Malke Publishing")
st.markdown("Olá, sou **Ana**, a assistente virtual da Malke Publishing. 😊💜💛💜")
st.markdown("Estou aqui para ajudar com dúvidas sobre nossos periódicos e serviços. Como posso ajudar você hoje? 📚")

# Caixa de entrada do usuário
user_input = st.text_input("Digite sua pergunta:")

# Configurar chave da OpenAI (substituir pela sua chave da API)
openai.api_key = "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"

# Configurar comportamento da assistente
def get_response(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "Você é Ana, a assistente virtual da Malke Publishing, especializada em Open Journal Systems (OJS). Você fornece respostas concisas e atenciosas, utilizando emojis quando apropriado."},
            {"role": "user", "content": prompt}
        ]
    )
    return response["choices"][0]["message"]["content"]

# Exibir resposta da assistente
if user_input:
    response = get_response(user_input)
    st.markdown(f"**Ana:** {response}")

# Rodapé
st.markdown("---")
st.markdown("🔗 [Malke Publishing](https://malque.pub) | ✉️ Contato: contact@malque.pub")
