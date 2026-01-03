# app.py
import streamlit as st
from deep_translator import GoogleTranslator
from gtts import gTTS
import tempfile

st.set_page_config(page_title="Language Translator", layout="centered")
st.title("🌐 Language Translator")

# --- User Input ---
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

# --- Translate Button ---
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

            # --- Optional: Text-to-Speech ---
            if st.button("🔊 Play Translation"):
                tts = gTTS(translated_text, lang=tgt_code)
                with tempfile.NamedTemporaryFile(delete=True) as fp:
                    tts.save(f"{fp.name}.mp3")
                    st.audio(f"{fp.name}.mp3", format="audio/mp3")

            # --- Optional: Copy Button ---
            if st.button("📋 Copy Translation"):
                st.code(translated_text)
                st.success("Copied! (You can select and Ctrl+C)")

        except Exception as e:
            st.error(f"Translation failed: {e}")
