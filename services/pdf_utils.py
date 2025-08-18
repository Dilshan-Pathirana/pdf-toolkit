import pdfplumber
from services.ocr_pdf import ocr_pdf
import os
import tempfile

def extract_text_from_pdf(file_path):
    """
    Extracts text from a PDF. If the PDF is scanned, run OCR first.
    Returns the extracted text as a string.
    """
    text = ""
    try:
        # Try extracting normal text first
        with pdfplumber.open(file_path) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"
    except:
        pass

    # If no text was found, assume scanned PDF and run OCR
    if not text.strip():
        print(f"No text found in {file_path}, running OCR...")
        # create a temp file for OCR output
        with tempfile.NamedTemporaryFile(suffix=".pdf", delete=False) as tmp:
            ocr_pdf(file_path, tmp.name)
            text = extract_text_from_pdf(tmp.name)
        os.remove(tmp.name)

    return text

def extract_texts_from_multiple_pdfs(file_paths):
    """
    Returns a list of text content from multiple PDFs.
    """
    texts = []
    for file_path in file_paths:
        print(f"Processing: {file_path}")
        text = extract_text_from_pdf(file_path)
        texts.append(text)
    return texts
