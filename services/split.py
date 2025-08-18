from PyPDF2 import PdfReader, PdfWriter

def split_pdf(input_path, output_folder):
    reader = PdfReader(input_path)
    for i, page in enumerate(reader.pages):
        writer = PdfWriter()
        writer.add_page(page)
        output_path = f"{output_folder}/page_{i+1}.pdf"
        with open(output_path, "wb") as f:
            writer.write(f)
    return True
