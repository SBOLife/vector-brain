"""This module provides functionality for creating a LangChain pipeline for question answering.

The pipeline combines document retrieval and language model capabilities to answer questions
based on retrieved context. It uses the Ollama LLM and a custom retriever implementation.
"""

from textwrap import dedent
from langchain.chains.retrieval_qa.base import RetrievalQA
from langchain.prompts import PromptTemplate
from langchain_community.chat_models import ChatOllama
from vector_brain_backend.services.rag_api_retriever import RAGAPIRetriever


def create_langchain_pipeline() -> RetrievalQA:
    """Creates and returns a LangChain pipeline for question answering."""
    retriever = RAGAPIRetriever(api_url="http://localhost:8000")

    llm = ChatOllama(
        model="llama3",
        base_url="http://localhost:11434",
        request_timeout=90,
        # streaming=True
    )

    prompt_template = dedent(
        """
        Context: {context}

        Question: {question}

        Answer:
    """
    ).strip()

    prompt = PromptTemplate(
        template=prompt_template, input_variables=["context", "question"]
    )

    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        chain_type="stuff",
        chain_type_kwargs={"prompt": prompt},
    )

    return qa_chain
