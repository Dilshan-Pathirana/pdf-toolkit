from pathlib import Path
from gpt4all import GPT4All
from services.pdf_utils import extract_texts_from_multiple_pdfs

# Custom folder for AI models
CUSTOM_MODEL_PATH = Path(r"D:\AI models\PDF toolset")
CUSTOM_MODEL_PATH.mkdir(parents=True, exist_ok=True)  # ensure folder exists

# GPT4All model filename
MODEL_NAME = "Meta-Llama-3-8B-Instruct.Q4_0.gguf"

def ask_ai_about_pdfs(pdf_paths, question):
    """
    Extract text from multiple PDFs and answer a question using GPT4All offline.
    """

    # 1️⃣ Extract text from all PDFs
    pdf_texts = extract_texts_from_multiple_pdfs(pdf_paths)
    combined_text = "\n\n".join(pdf_texts)

    # 2️⃣ Load GPT4All (downloads first time if needed, saves to custom path)
    model = GPT4All(
        model_name=MODEL_NAME,
        model_path=CUSTOM_MODEL_PATH,
        verbose=True
    )

    # 3️⃣ Start chat session and generate answer
    with model.chat_session() as session:
        prompt = (
            "You are an expert assistant. Answer the following question based on the documents.\n\n"
            f"Documents:\n{combined_text}\n\nQuestion: {question}\nAnswer:"
        )
        response = session.generate(prompt, max_tokens=1024)
        return response
