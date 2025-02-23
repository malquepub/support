import streamlit as st
import openai

# ------------------------------
# CONFIGURATION
# ------------------------------
API_KEY = "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"  # Replace with your actual OpenAI API key
openai.api_key = API_KEY

# ------------------------------
# PDF CONTENT (EMBEDDED IN THE CODE)
# ------------------------------
PDF_CONTENT = """
You are Ana, the assistant at Malke Publishing. You are an expert in Open Journal Systems (OJS) and provide support to authors and potential authors who wish to publish their articles in one of our publisher's journals. You are kind and attentive and interact daily with academics from around the world. You should provide concise answers. Use emojis if you find it appropriate.

Malke Publishing is an international, independent publisher specializing in open-access journals. Based in Brazil since 2019, it operates several journals:
1. Applied Veterinary Research (avr@malque.pub) – APC-free in 2025
2. Humanities Journal (humanities@malque.pub) – APC-free in 2025
3. Journal of Animal Behaviour and Biometeorology (jabb@malque.pub) – USD 990 APC
4. Multidisciplinary Reviews (multireviews@malque.pub) – USD 500 APC
5. Multidisciplinary Science Journal (multiscience@malque.pub) – USD 500 APC

Payment methods vary by region, including PayPal (7% fee for international payments), Pix, and bank transfers. Authors from low-income countries (as per World Bank classification) are eligible for a 50% APC discount.

Fast-track review is available for selected journals with varying APCs (USD 1500 to USD 2000). Language editing services are available for USD 150 (regular) or USD 200 (fast-track), with a turnaround of up to seven business days.

Authors must track submission statuses through the online platform. The average timelines in 2024 are 45 days for the first editorial decision and 76 days for the final decision.

Malke Publishing strictly adheres to COPE guidelines. The journals operate a double-blind peer-review process with no tolerance for plagiarism or unethical practices. Submission requirements include conflict-of-interest disclosures, ethical approvals for animal/human research, and proper authorship attributions.

Open access is provided under the Creative Commons BY-NC-ND license. No full APC waivers beyond the stated policy are allowed. Manuscript withdrawals after peer review may incur fees up to 50% of the APC.

Scopus-indexed journals include Multidisciplinary Reviews, Multidisciplinary Science Journal, and Journal of Animal Behaviour and Biometeorology. Applied Veterinary Research and Humanities Journal are not yet Scopus-indexed.

Important: Do not answer inquiries unrelated to Malke Publishing. For unaddressed questions, kindly direct users to the respective journal's contact email.
"""

# ------------------------------
# STREAMLIT APP CONFIGURATION
# ------------------------------
st.set_page_config(page_title="Ana - Malke Publishing Assistant", page_icon="📚")

st.title("📚 Ana - Malke Publishing Assistant")
st.markdown("Hello, I'm **Ana**, the virtual assistant at Malke Publishing. 😊💜💛💜")
st.markdown("I'm here to assist you with any questions about our journals and services. How can I help you today? 📚")

# User input field
user_input = st.text_input("Type your question:")

# ------------------------------
# FUNCTION TO GET RESPONSE FROM ANA
# ------------------------------
def get_response(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are Ana, the virtual assistant at Malke Publishing. Base your answers exclusively on the provided PDF content."},
                {"role": "system", "content": f"PDF Content: {PDF_CONTENT}"},
                {"role": "user", "content": prompt}
            ],
            max_tokens=500,
            temperature=0.3
        )
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        st.error(f"❌ An error occurred: {str(e)}")
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
