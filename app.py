import streamlit as st
from transformers import pipeline

translator = pipeline("translation", model="Helsinki-NLP/opus-mt-mul-en")

# Streamlit UI
st.set_page_config(page_title="Language Translator",page_icon="🌐", layout="centered")

st.markdown(""" 
    <style>
    .stTextArea label{
        font-weight: bold;
        color: #333;
    }
    .stButton>button{
        background-color: #4CAF50;
        color: white;
        font-weight: bold;
        border-radius: 8px;
        padding: 0.5rem 1.5rem;
    }
    .stButton>button:hover{
        background-color: #45a049;
        color:white;
    }
    .stButton>button:focus{
        outline:none;
        box-shadow:none;
    }
    </style>
""",unsafe_allow_html=True)


st.markdown("<h1 style='text-align:center;'> Language Translator (Multilingual → English)</h1>",unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:gray;'>Translate text from any language into English using Hugging Face models.</p>",unsafe_allow_html=True)


with st.container():
    # st.markdown("<div class='main'>", unsafe_allow_html=True)

    input_text = st.text_area("✍️ Enter text in any language:", "Bonjour, je suis ravi de vous rencontrer.")

    if st.button("Translate"):
        if input_text.strip():
            try:
                result = translator(input_text)
                translation = result[0]['translation_text']
                st.success("✅ Translated Output:")
                st.write(f"**{translation}**")
            except Exception as e:
                st.error(f"Translation failed: {e}")
        else:
            st.warning("Please enter some text to translate.")

    # st.markdown("</div>", unsafe_allow_html=True)

st.markdown("---")
st.markdown("<div style='text-align: center; color: gray;'>Built with ❤️ using Streamlit and Hugging Face</div>", unsafe_allow_html=True)