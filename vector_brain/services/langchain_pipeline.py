"""
This module provides functionality for creating a LangChain-based question answering pipeline.
It combines a RAG API retriever with a local Ollama LLM to enable context-aware responses.
"""

from langchain.chains.retrieval_qa.base import RetrievalQA
from langchain.prompts import PromptTemplate
from langchain_community.chat_models import ChatOllama

from vector_brain.services.rag_api_retriever import RAGAPIRetriever


def create_langchain_pipeline():
    """Creates and returns a LangChain pipeline for question answering.

    The pipeline combines a RAG API retriever for context lookup with a local Ollama LLM.
    It uses a custom prompt template to format the context and question for the LLM.

    Returns:
        RetrievalQA: A configured QA chain that can answer questions using retrieved context.
    """
    retriever = RAGAPIRetriever.from_api(api_url="http://localhost:8000")

    llm = ChatOllama(model="llama3", base_url="http://localhost:11434")

    prompt_template = """
    Context: {context}

    Question: {question}

    Answer:
    """

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
