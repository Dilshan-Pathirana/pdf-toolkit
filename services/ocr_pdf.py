from pdf2image import convert_from_path
import pytesseract
from PyPDF2 import PdfReader, PdfWriter
import io

def ocr_pdf(input_pdf, output_pdf):
    images = convert_from_path(input_pdf)  # Poppler must be in PATH
    writer = PdfWriter()
    
    for img in images:
        pdf_bytes = pytesseract.image_to_pdf_or_hocr(img, extension='pdf')
        pdf_stream = io.BytesIO(pdf_bytes) # type: ignore
        temp_reader = PdfReader(pdf_stream)
        writer.add_page(temp_reader.pages[0])
    
    with open(output_pdf, "wb") as f:
        writer.write(f)
    
    print(f"OCR completed: {output_pdf}")
