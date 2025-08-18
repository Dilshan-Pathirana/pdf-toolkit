from services.merge import merge_pdfs
from services.split import split_pdf
from services.compress import compress_pdf
from services.extract import extract_pages
from services.pdf_to_images import pdf_to_images
from services.images_to_pdf import images_to_pdf
from services.password_pdf import add_password, remove_password
from services.ocr_pdf import ocr_pdf
from services.pdf_to_word import pdf_to_word
from services.ai_qa import ask_ai_about_pdfs

def main():
    print("PDF Toolkit Prototype")
    print("1) Merge PDFs")
    print("2) Split PDF")
    print("3) Compress PDF")
    print("4) Extract Pages")
    print("5) PDF → Images")
    print("6) Images → PDF")
    print("7) Add Password to PDF")
    print("8) Remove Password from PDF")
    print("9) OCR (Scan to Searchable PDF)")
    print("10) PDF → Word")
    print("11) AI PDF Question Answering")
    
    choice = input("Choose: ")

    if choice == "1":
        files = input("Enter PDF paths separated by commas:\n").split(",")
        output = input("Output file path: ")
        result = merge_pdfs([f.strip() for f in files], output)
        print("Merged to:", result)

    elif choice == "2":
        file = input("PDF file to split: ")
        folder = input("Output folder: ")
        split_pdf(file, folder)
        print("Splitting done!")

    elif choice == "3":
        file = input("PDF file to compress: ")
        output = input("Output file path: ")
        compress_pdf(file, output)
        print("Compressed to:", output)

    elif choice == "4":
        file = input("PDF file: ")
        pages = input("Pages to extract (comma-separated, 0-indexed): ").split(",")
        pages = [int(p.strip()) for p in pages]
        output = input("Output file path: ")
        extract_pages(file, output, pages)

    elif choice == "5":
        file = input("PDF file: ")
        folder = input("Output folder: ")
        pdf_to_images(file, folder)

    elif choice == "6":
        files = input("Enter image paths separated by commas:\n").split(",")
        output = input("Output PDF path: ")
        images_to_pdf([f.strip() for f in files], output)

    elif choice == "7":
        file = input("PDF file: ")
        password = input("Enter password: ")
        output = input("Output PDF path: ")
        add_password(file, output, password)

    elif choice == "8":
        file = input("PDF file: ")
        password = input("Current password: ")
        output = input("Output PDF path: ")
        remove_password(file, output, password)

    elif choice == "9":
        file = input("Scanned PDF file: ")
        output = input("Output searchable PDF path: ")
        ocr_pdf(file, output)

    elif choice == "10":
        file = input("PDF file: ")
        output = input("Output Word path: ")
        pdf_to_word(file, output)

    elif choice == "11":
        files = input("Enter PDF paths separated by commas:\n").split(",")
        question = input("Enter your question: ")
        answer = ask_ai_about_pdfs([f.strip() for f in files], question)
        print("\nAI Answer:\n", answer)

    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main()
