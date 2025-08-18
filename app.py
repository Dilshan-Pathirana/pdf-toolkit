from services.merge import merge_pdfs
from services.split import split_pdf
from services.compress import compress_pdf

def main():
    print("PDF Toolkit Prototype")
    print("1) Merge PDFs")
    print("2) Split PDF")
    print("3) Compress PDF")
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


if __name__ == "__main__":
    main()
