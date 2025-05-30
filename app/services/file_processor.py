from bs4 import BeautifulSoup
import markdown
import textract

def extract_text_from_pdf(filepath: str) -> str:
    """
    Extract text from a PDF file.
    """
    return textract.process(filepath).decode("utf-8")

def extract_text_from_html(filepath: str) -> str:
    """
    Extract text from a HTML file.
    """
    with open(filepath, "r") as f:
        soup = BeautifulSoup(f, "html.parser")
        return soup.get_text()

def extract_text_from_markdown(filepath: str) -> str:
    """
    Extract text from a Markdown file.
    """
    with open(filepath, "r") as f:
        return markdown.markdown(f.read())

def extract_text_from_text(filepath: str) -> str:
    """
    Extract text from a Text file.
    """
    with open(filepath, "r") as f:
        return f.read(
            
        )