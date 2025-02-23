import streamlit as st
import openai

# ------------------------------ 
# CONFIGURATION 
# ------------------------------
API_KEY = "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"  # Substitua pela sua chave da OpenAI
ASSISTANT_ID = "asst_6mxGRBwNtDBa4F9203Z2S0sM"  # ID do seu assistente criado

openai.api_key = API_KEY

# ------------------------------ 
# STREAMLIT CONFIGURATION 
# ------------------------------
st.set_page_config(page_title="Ana - Malke Publishing Assistant", page_icon="📚")

st.title("📚 Ana - Malke Publishing Assistant")
st.markdown("Hello, I'm **Ana**, the virtual assistant at Malke Publishing. 😊💜💛💜")
st.markdown("I'm here to assist you with any questions about our journals and services. How can I help you today? 📚")

# User input field
user_input = st.text_input("Type your question:")

# ------------------------------
# FUNCTION TO INTERACT WITH ASSISTANT
# ------------------------------
def get_response(prompt):
    try:
        # Step 1: Create a new thread
        thread = openai.beta.threads.create()

        # Step 2: Add user message to the thread
        openai.beta.threads.messages.create(
            thread_id=thread["id"],
            role="user",
            content=prompt
        )

        # Step 3: Run the assistant on the thread
        run = openai.beta.threads.runs.create(
            thread_id=thread["id"],
            assistant_id=ASSISTANT_ID
        )

        # Step 4: Poll until completion
        import time
        while True:
            status = openai.beta.threads.runs.retrieve(
                thread_id=thread["id"],
                run_id=run["id"]
            )
            if status["status"] == "completed":
                break
            time.sleep(1)  # Wait a bit before checking again

        # Step 5: Retrieve the latest messages
        messages = openai.beta.threads.messages.list(thread_id=thread["id"])
        response = messages["data"][0]["content"][0]["text"]["value"]
        return response

    except Exception as e:
        st.error(f"❌ An error occurred: {e}")
        return "Sorry, something went wrong. Please try again later."

# ------------------------------
# DISPLAY ANA'S RESPONSE
# ------------------------------
if user_input:
    response = get_response(user_input)
    st.markdown(f"**Ana:** {response}")

# ------------------------------
# FOOTER
# ------------------------------
st.markdown("---")
st.markdown("🔗 [Malke Publishing](https://malque.pub) | ✉️ Contact: contact@malque.pub")
