import streamlit as st
from main import load_code, embed_texts, search, generate_answer

st.set_page_config(page_title="Codebase AI", layout="centered")

st.title("💡 Codebase Knowledge AI")
st.write("Ask questions about your codebase")

# Load data once
@st.cache_resource
def setup():
    texts, file_names = load_code("my_project")
    vectors = embed_texts(texts)
    return texts, file_names, vectors

texts, file_names, vectors = setup()

# User input
query = st.text_input("Ask your question:")

if st.button("Get Answer"):
    if query:
        results = search(query, texts, file_names, vectors)
        answer = generate_answer(query, results)

        st.subheader("🧠 Answer:")
        st.write(answer)
    else:
        st.warning("Please enter a question")