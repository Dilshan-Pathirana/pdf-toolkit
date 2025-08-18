import pikepdf

def compress_pdf(input_path, output_path):
    # Open the PDF
    pdf = pikepdf.open(input_path)

    # Save with default settings and "linearize" enabled (good for compression)
    pdf.save(output_path, linearize=True)
    pdf.close()
    return output_path
