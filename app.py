import streamlit as st
import openai

# Configure a chave de API da OpenAI (recomenda-se usar st.secrets para segurança)
openai.api_key = st.secrets["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"]

# ID do assistente criado na plataforma OpenAI
ASSISTANT_ID = "asst_6mxGRBwNtDBa4F9203Z2S0sM"

st.title("Ana - Malke Publishing Virtual Assistant")

# Inicializar o histórico de conversas
if "messages" not in st.session_state:
    st.session_state.messages = []

# Exibir o histórico de mensagens
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Campo de entrada para o usuário
prompt = st.chat_input("Digite sua mensagem...")

if prompt:
    # Adiciona a mensagem do usuário ao histórico
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Exibir a mensagem do usuário
    with st.chat_message("user"):
        st.markdown(prompt)

    # Envia a mensagem para o assistente e obtém a resposta
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[{"role": m["role"], "content": m["content"]} for m in st.session_state.messages],
            tools=["assistant"],
            tool_choice={"type": "assistant", "id": ASSISTANT_ID}
        )

        assistant_response = response.choices[0].message["content"]

        # Adiciona a resposta ao histórico de mensagens
        st.session_state.messages.append({"role": "assistant", "content": assistant_response})

        # Exibir a resposta do assistente
        with st.chat_message("assistant"):
            st.markdown(assistant_response)

    except Exception as e:
        st.error(f"Erro ao se comunicar com o assistente: {e}")
