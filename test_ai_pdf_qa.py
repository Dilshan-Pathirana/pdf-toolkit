from services.ai_qa import ask_ai_about_pdfs

pdf_files = ["sample_pdfs/sample 5.pdf"]
question = "what is this about"

print("Running AI test...\n")
try:
    answer = ask_ai_about_pdfs(pdf_files, question)
except Exception as e:
    print("Error:", e)
else:
    print("\nAI Answer:\n", answer)
