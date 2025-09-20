# app.py
import streamlit as st
import streamlit.components.v1 as components
import spacy
from spacy import displacy

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

st.title("🔎 Text Analysis Tool")
st.write("Nhập một đoạn văn bản để phân tích NLP (Tokenization, POS, NER).")

# Input text
user_input = st.text_area("Nhập văn bản:", "Bạn Nam hôm nay mắc mưa")

if st.button("Phân tích"):
    doc = nlp(user_input)

    # 1. Tokenization
    st.subheader("1️⃣ Danh sách Token sau khi Tokenization:")
    tokens = [token.text for token in doc]
    st.write(tokens)

    # 2. POS Tagging
    st.subheader("2️⃣ POS Tag cho từng Token:")
    pos_data = [(token.text, token.pos_, token.dep_) for token in doc]
    st.table(pos_data)

    # 3. Named Entity Recognition (NER)
    st.subheader("3️⃣ Named Entities (NER):")
    if doc.ents:
        ents = [(ent.text, ent.label_) for ent in doc.ents]
        st.table(ents)
        st.write("📌 Visualization:")
        html = displacy.render(doc, style="ent", jupyter=False)
        components.html(html, height=300, scrolling=True)
    else:
        st.write("❌ Không phát hiện Named Entities.")
