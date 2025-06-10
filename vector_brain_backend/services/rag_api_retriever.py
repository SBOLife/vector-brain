"""RAG API Retriever module for querying external RAG endpoints.

This module provides functionality to retrieve relevant documents from a RAG
(Retrieval-Augmented Generation) API endpoint. It implements both synchronous
and asynchronous retrieval methods through HTTP requests.
"""

import asyncio
from typing import List
import httpx
from langchain.schema import BaseRetriever, Document
from pydantic import Field


class RAGAPIRetriever(BaseRetriever):
    """A retriever that queries a RAG API endpoint to get relevant documents."""

    api_url: str = Field(...)

    async def aget_relevant_documents(self, query: str, **kwargs) -> List[Document]:
        async with httpx.AsyncClient(timeout=300) as client:
            response = await client.post(
                f"{self.api_url}/api/v1/rag/query", json={"prompt": query}
            )
            response.raise_for_status()
            results = response.json().get("results", [])

        return [Document(page_content=res) for res in results]

    def get_relevant_documents(
        self,
        query: str,
        *,
        callbacks=None,
        tags=None,
        metadata=None,
        **kwargs,
    ) -> List[Document]:
        return asyncio.run(self.aget_relevant_documents(query))
