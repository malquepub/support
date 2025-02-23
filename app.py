import streamlit as st
import openai

# Configurações iniciais do Streamlit
st.set_page_config(page_title="Ana - Malke Publishing", page_icon="📚")
st.title("Ana - Assistente Virtual da Malke Publishing")

# Mensagem de saudação (aparece apenas uma vez por sessão)
if 'greeted' not in st.session_state:
    st.session_state['greeted'] = True
    st.write("Hello, I am Ana from Malke Publishing. 😊💜💛💜")
    st.write("I’m here to assist you with any questions about our journals and services. How can I help you today? 📚")

# Função para gerar resposta com base no prompt e contexto fornecido
def generate_response(prompt):
    context = (
        "You are Ana, the assistant at Malke Publishing. You are an expert in Open Journal Systems (OJS) and provide "
        "support to authors and potential authors who wish to publish their articles in one of our publisher's journals. "
        "You are kind and attentive, providing concise answers. Use emojis when appropriate."
    )

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": context},
            {"role": "user", "content": prompt}
        ],
        max_tokens=200
    )

    return response['choices'][0]['message']['content'].strip()

# Entrada de texto do usuário
user_input = st.text_input("Digite sua pergunta:")

# Quando o usuário envia uma pergunta, gera uma resposta e exibe
if user_input:
    with st.spinner('Ana está digitando...'): 
        response = generate_response(user_input)
    st.write(response)
