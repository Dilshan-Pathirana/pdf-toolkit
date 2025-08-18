import pikepdf

def add_password(input_pdf, output_pdf, password):
    pdf = pikepdf.open(input_pdf)
    pdf.save(output_pdf, encryption=pikepdf.Encryption(owner=password, user=password, R=4))
    pdf.close()
    print(f"Password added to {output_pdf}")

def remove_password(input_pdf, output_pdf, password):
    pdf = pikepdf.open(input_pdf, password=password)
    pdf.save(output_pdf)
    pdf.close()
    print(f"Password removed, saved as {output_pdf}")
