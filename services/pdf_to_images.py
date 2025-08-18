from pdf2image import convert_from_path

def pdf_to_images(input_pdf, output_folder):
    images = convert_from_path(input_pdf)
    for i, img in enumerate(images):
        img.save(f"{output_folder}/page_{i+1}.png", "PNG")
    print(f"PDF converted to images in {output_folder}")
