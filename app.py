import streamlit as st
import openai

# ------------------------------
# CONFIGURATION
# ------------------------------
# Set your OpenAI API key directly in the code (ensure you keep this secure)
API_KEY = "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"  # Replace with your actual OpenAI API key
openai.api_key = API_KEY

# Streamlit page configuration
st.set_page_config(page_title="Ana - Malke Publishing Assistant", page_icon="📚")

# Title and introduction
st.title("📚 Ana - Malke Publishing Assistant")
st.markdown("Hello, I'm **Ana**, the virtual assistant at Malke Publishing. 😊💜💛💜")
st.markdown("I'm here to assist you with any questions about our journals and services. How can I help you today? 📚")

# User input field
user_input = st.text_input("Type your question:")

# Function to get response from Ana using the updated OpenAI API (v1.0.0 and above)
def get_response(prompt):
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=f"You are Ana, the virtual assistant at Malke Publishing, an expert in Open Journal Systems (OJS). Answer concisely and kindly. Use emojis when appropriate. User: {prompt}",
            max_tokens=150,
            temperature=0.7
        )
        return response['choices'][0]['text'].strip()

    except Exception as e:
        st.error("❌ An unexpected error occurred. Please ensure you are using the latest version of the OpenAI library.")
        st.write("**Tip:** Run `pip install --upgrade openai` to update to the latest version.")
        st.write(f"**Error details:** {str(e)}")
        return "Sorry, something went wrong. Please try again later."

# Display Ana's response
if user_input:
    response = get_response(user_input)
    st.markdown(f"**Ana:** {response}")

# Footer
st.markdown("---")
st.markdown("🔗 [Malke Publishing](https://malque.pub) | ✉️ Contact: contact@malque.pub")
