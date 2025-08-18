from PyPDF2 import PdfReader, PdfWriter

def extract_pages(input_pdf, output_pdf, pages):
    reader = PdfReader(input_pdf)
    writer = PdfWriter()
    for page_num in pages:
        writer.add_page(reader.pages[page_num])
    with open(output_pdf, "wb") as f:
        writer.write(f)
    print(f"Extracted pages {pages} to {output_pdf}")
