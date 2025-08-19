from services.merge import merge_pdfs
from services.split import split_pdf
from services.compress import compress_pdf
from services.extract import extract_pages
from services.pdf_to_images import pdf_to_images
from services.images_to_pdf import images_to_pdf
from services.password_pdf import add_password, remove_password
from services.ocr_pdf import ocr_pdf
from services.pdf_to_word import pdf_to_word
from services.ai_qa import ask_ai_about_pdfs   # Gemma-3 offline AI

def get_file_list(prompt):
    """Helper to get a list of file paths from user input."""
    return [f.strip() for f in input(prompt).split(",")]

def main():
    print("PDF Toolkit Prototype (with Gemma-3 Offline AI)")
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
    print("11) AI PDF Question Answering (Gemma-3 Offline)")

    choice = input("Choose: ").strip()

    if choice == "1":
        files = get_file_list("Enter PDF paths separated by commas:\n")
        output = input("Output file path: ").strip()
        print("Merged to:", merge_pdfs(files, output))

    elif choice == "2":
        file = input("PDF file to split: ").strip()
        folder = input("Output folder: ").strip()
        split_pdf(file, folder)
        print("Splitting done!")

    elif choice == "3":
        file = input("PDF file to compress: ").strip()
        output = input("Output file path: ").strip()
        compress_pdf(file, output)
        print("Compressed to:", output)

    elif choice == "4":
        file = input("PDF file: ").strip()
        pages = [int(p.strip()) for p in input("Pages to extract (comma-separated, 0-indexed): ").split(",")]
        output = input("Output file path: ").strip()
        extract_pages(file, output, pages)

    elif choice == "5":
        file = input("PDF file: ").strip()
        folder = input("Output folder: ").strip()
        pdf_to_images(file, folder)

    elif choice == "6":
        files = get_file_list("Enter image paths separated by commas:\n")
        output = input("Output PDF path: ").strip()
        images_to_pdf(files, output)

    elif choice == "7":
        file = input("PDF file: ").strip()
        pwd = input("Enter password: ").strip()
        output = input("Output PDF path: ").strip()
        add_password(file, output, pwd)

    elif choice == "8":
        file = input("PDF file: ").strip()
        pwd = input("Current password: ").strip()
        output = input("Output PDF path: ").strip()
        remove_password(file, output, pwd)

    elif choice == "9":
        file = input("Scanned PDF file: ").strip()
        output = input("Output searchable PDF path: ").strip()
        ocr_pdf(file, output)

    elif choice == "10":
        file = input("PDF file: ").strip()
        output = input("Output Word path: ").strip()
        pdf_to_word(file, output)

    elif choice == "11":
        files = get_file_list("Enter PDF paths separated by commas:\n")
        question = input("Enter your question: ").strip()
        print("\nProcessing PDFs and running Gemma-3 offline AI...\n")
        try:
            answer = ask_ai_about_pdfs(files, question)
        except Exception as e:
            print("Error running AI:", e)
        else:
            print("\nAI Answer:\n", answer)

    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main()
