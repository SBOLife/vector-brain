"""Module for extracting text content from various file formats.

This module provides functions to extract text from PDF, DOCX and TXT files.
The main entry point is the extract_text() function which handles different
file types based on their extensions.
"""

import os
from typing import Union
from io import BytesIO
import pdfplumber
import docx


def extract_text_from_pdf(file: BytesIO) -> str:
    """Extract text content from a PDF document.

    Args:
        file (BytesIO): The PDF file object to extract content from

    Returns:
        str: The extracted text content from all pages, joined with newlines
    """
    with pdfplumber.open(file) as pdf:
        return "\n".join(
            page.extract_text() for page in pdf.pages if page.extract_text()
        )


def extract_text_from_docx(file: BytesIO) -> str:
    """Extract text content from a Word document.

    Args:
        file (BytesIO): The Word document file object to extract content from

    Returns:
        str: The extracted text content from all paragraphs, joined with newlines
    """
    document = docx.Document(file)
    return "\n".join(paragraph.text for paragraph in document.paragraphs)


def extract_text_from_txt(file: BytesIO) -> str:
    """Extract text content from a text file.

    Args:
        file (BytesIO): The text file object to extract content from

    Returns:
        str: The extracted text content decoded as UTF-8
    """
    return file.read().decode("utf-8")


def extract_text(file: BytesIO, filename: str) -> Union[str, None]:
    """Extract text content from a file based on its extension.

    Args:
        file (BytesIO): The file object to extract content from
        filename (str): Name of the file including extension

    Returns:
        Union[str, None]: The extracted text content if successful, None if unsupported file type
    """

    extractors = {
        ".pdf": extract_text_from_pdf,
        ".docx": extract_text_from_docx,
        ".txt": extract_text_from_txt,
    }

    _, extension = os.path.splitext(filename)

    extractor = extractors.get(extension)
    return extractor(file) if extractor else None
