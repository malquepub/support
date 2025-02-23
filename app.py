import streamlit as st
import openai

# ------------------------------
# CONFIGURATION
# ------------------------------
# Set your OpenAI API key directly in the code (ensure you keep this secure)
API_KEY = "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"  # Replace with your actual OpenAI API key

# Verify if the API key is set and valid
if not API_KEY or not API_KEY.startswith("sk-"):
    st.error("❌ Invalid API key format. Please check and provide a valid OpenAI API key.")
else:
    openai.api_key = API_KEY

# Streamlit page configuration
st.set_page_config(page_title="Ana - Malke Publishing Assistant", page_icon="📚")

# Title and introduction
st.title("📚 Ana - Malke Publishing Assistant")
st.markdown("Hello, I'm **Ana**, the virtual assistant at Malke Publishing. 😊💜💛💜")
st.markdown("I'm here to assist you with any questions about our journals and services. How can I help you today? 📚")

# User input field
user_input = st.text_input("Type your question:")

# Function to get response from Ana using the updated OpenAI API
def get_response(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are Ana, the virtual assistant at Malke Publishing, an expert in Open Journal Systems (OJS). You provide concise, kind, and attentive responses, using emojis when appropriate."},
                {"role": "user", "content": prompt}
            ]
        )
        return response["choices"][0]["message"]["content"].strip()

    except Exception as e:
        st.error(f"❌ An unexpected error occurred: {str(e)}")
        return "Sorry, something went wrong. Please try again later."

# Display Ana's response
if user_input:
    response = get_response(user_input)
    st.markdown(f"**Ana:** {response}")

# Footer
st.markdown("---")
st.markdown("🔗 [Malke Publishing](https://malque.pub) | ✉️ Contact: contact@malque.pub")
