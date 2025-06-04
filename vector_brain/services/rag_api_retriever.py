"""This module provides a retriever implementation for fetching documents through a RAG API endpoint.

The module contains the RAGAPIRetriever class which handles both synchronous and asynchronous
HTTP requests to retrieve relevant documents based on query strings from a specified API endpoint.
"""

import asyncio
import httpx
from langchain.schema import BaseRetriever, Document


class RAGAPIRetriever(BaseRetriever):
    """A retriever that fetches relevant documents through a RAG API endpoint.

    This retriever makes HTTP POST requests to a specified API endpoint to retrieve
    documents based on a query string. It implements both synchronous and asynchronous
    retrieval methods.

    Args:
        api_url (str): The base URL of the RAG API endpoint.
    """

    def __init__(self, api_url: str):
        self.api_url = api_url

    async def _aget_relevant_documents(self, query: str, *, run_manager=None):
        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{self.api_url}/api/v1/rag/query", json={"prompt": query}
            )
            response.raise_for_status()
            results = response.json().get("results", [])

        docs = [Document(page_content=res) for res in results]
        return docs

    def get_relevant_documents(
        self,
        query: str,
        *,
        callbacks=None,
        tags=None,
        metadata=None,
        **kwargs,
    ):
        return asyncio.run(self._aget_relevant_documents(query))
