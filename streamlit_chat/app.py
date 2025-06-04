"""
Streamlit chat application for VectorBrain RAG system.
This module implements a simple chat interface using Streamlit to interact with
a RAG-based question answering system.
"""

import traceback
import streamlit as st
from vector_brain.services.langchain_pipeline import create_langchain_pipeline


st.set_page_config(page_title="VectorBrain Chat", page_icon="🧠")

st.title("🧠 VectorBrain RAG Chat")

qa_chain = create_langchain_pipeline()

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_input = st.text_input("Type your question:")

if st.button("Send"):
    if user_input.strip() == "":
        st.warning("⚠️ Please, type a question.")
    else:
        with st.spinner("🔍 Generating Answer..."):
            try:
                response = qa_chain.run(user_input)
                st.session_state.chat_history.append((user_input, response))
            except Exception as e:
                st.error(f"❌ Error: {e}")
                st.text(traceback.format_exc())

st.write("### 📝 Chat history:")
for i, (q, a) in enumerate(st.session_state.chat_history):
    st.write(f"**Q{i+1}:** {q}")
    st.write(f"**A{i+1}:** {a}")
