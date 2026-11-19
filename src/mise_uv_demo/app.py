import os

import streamlit as st

from mise_uv_demo import count_characters, count_unique_words, count_words

greeting = os.environ.get("APP_GREETING", "Hello!")
st.set_page_config(page_title=greeting)
st.title(greeting)

text = st.text_area("Text", "mise and uv make setup smooth")
words, unique_words, characters = st.columns(3)
words.metric("Words", count_words(text))
unique_words.metric("Unique words", count_unique_words(text))
characters.metric("Characters", count_characters(text))
