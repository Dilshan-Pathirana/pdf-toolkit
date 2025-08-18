from pdf2docx import Converter

def pdf_to_word(input_pdf, output_docx):
    cv = Converter(input_pdf)
    cv.convert(output_docx)  # remove start/end, it converts the whole PDF by default
    cv.close()
    print(f"Converted {input_pdf} to {output_docx}")
