# translation_app.py
import streamlit as st
from deep_translator import GoogleTranslator
from gtts import gTTS #Converts text into spoken audio
import tempfile # creating temporary files so as audio files don’t stay on disk permanently

st.set_page_config(page_title="Language Translator", layout="centered")
st.title("🌐 Language Translator")


text_to_translate = st.text_area("Enter text to translate:", height=150)

# Supported languages for GoogleTranslator
languages = {
    "English": "en",
    "French": "fr",
    "Spanish": "es",
    "German": "de",
    "Italian": "it",
    "Portuguese": "pt",
    "Russian": "ru",
    "Chinese (Simplified)": "zh-CN",
    "Japanese": "ja",
    "Korean": "ko",
}

source_lang = st.selectbox("Source Language", ["auto"] + list(languages.keys()))
target_lang = st.selectbox("Target Language", list(languages.keys()), index=0)

# Translate Button 
if st.button("Translate"):
    if not text_to_translate.strip():
        st.warning("Please enter some text to translate!")
    else:
        # Map language names to codes
        src_code = "auto" if source_lang == "auto" else languages[source_lang]
        tgt_code = languages[target_lang]

        try:
            # Translate text
            translated_text = GoogleTranslator(source=src_code, target=tgt_code).translate(text_to_translate)
            st.success("✅ Translation Complete")
            st.text_area("Translated Text:", translated_text, height=150)


        except Exception as e:
            st.error(f"Translation failed: {e}")
