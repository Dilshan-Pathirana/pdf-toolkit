from PIL import Image

def images_to_pdf(image_files, output_pdf):
    images = [Image.open(img).convert("RGB") for img in image_files]
    images[0].save(output_pdf, save_all=True, append_images=images[1:])
    print(f"Images combined into {output_pdf}")
