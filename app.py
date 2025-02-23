import streamlit as st
import openai

# ------------------------------
# CONFIGURATION
# ------------------------------
# Set your OpenAI API key directly in the code (ensure you keep this secure)
openai.api_key = "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"  # Replace with your actual OpenAI API key

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
        response = openai.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are Ana, the virtual assistant at Malke Publishing, an expert in Open Journal Systems (OJS). You provide concise, kind, and attentive responses, using emojis when appropriate."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content.strip()

    except Exception as e:
        st.error(f"❌ An error occurred: {str(e)}")
        return "Sorry, something went wrong. Please try again later."

# Display Ana's response
if user_input:
    response = get_response(user_input)
    st.markdown(f"**Ana:** {response}")

# Footer
st.markdown("---")
st.markdown("🔗 [Malke Publishing](https://malque.pub) | ✉️ Contact: contact@malque.pub")
