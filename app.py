import streamlit as st
import openai

# Streamlit page configuration
st.set_page_config(page_title="Ana - Malque Publishing Assistant", page_icon="📚")

# Title and introduction
st.title("📚 Ana - Malque Publishing Assistant")
st.markdown("Hello, I'm **Ana**, the virtual assistant at Malque Publishing. 😊💜💛💜")
st.markdown("I'm here to assist you with any questions about our journals and services. How can I help you today? 📚")

# Sidebar for OpenAI API key input
api_key = st.sidebar.text_input("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", type="password")

# User input
user_input = st.text_input("Type your question:")

# Function to get response from Ana
def get_response(prompt, api_key):
    if not api_key:
        return "⚠️ Please enter your OpenAI API key in the sidebar."
    
    client = openai.OpenAI(api_key=api_key)
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are Ana, the virtual assistant at Malke Publishing, an expert in Open Journal Systems (OJS). You provide concise, kind, and attentive responses, using emojis when appropriate."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content.strip()

# Display Ana's response
if user_input:
    response = get_response(user_input, api_key)
    st.markdown(f"**Ana:** {response}")

# Footer
st.markdown("---")
st.markdown("🔗 [Malke Publishing](https://malque.pub) | ✉️ Contact: contact@malque.pub")
