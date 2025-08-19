from pathlib import Path
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch
from services.pdf_utils import extract_texts_from_multiple_pdfs

print(torch.cuda.is_available())
print(torch.cuda.get_device_name(0))


# --------------------------
# Force GPU usage
# --------------------------
if not torch.cuda.is_available():
    raise RuntimeError("CUDA GPU is not available! Please run on a system with a GPU.")

device = torch.device("cuda")

# --------------------------
# Load GPT-Neo onto GPU
# --------------------------
MODEL_NAME = "EleutherAI/gpt-neo-1.3B"    # You can try 2.7B if you have more VRAM

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForCausalLM.from_pretrained(MODEL_NAME)

# Use half precision to save VRAM
model = model.half().to(device)
model.eval()


def ask_ai_about_pdfs(pdf_paths, question, max_tokens=256):
    """
    Extract text from multiple PDFs and answer a question using GPT-Neo on GPU only.
    """
    # 1) Extract text
    pdf_texts = extract_texts_from_multiple_pdfs(pdf_paths)
    combined_text = "\n\n".join(pdf_texts)

    # You can truncate here to avoid sending huge context:
    combined_text = combined_text[:3000]

    # 2) Build prompt
    prompt = (
        "You are an expert assistant. Answer the following question based on the documents.\n\n"
        f"Documents:\n{combined_text}\n\nQuestion: {question}\nAnswer:"
    )

    # 3) Tokenize and send to GPU
    inputs = tokenizer(prompt, return_tensors="pt", truncation=True).to(device)

    # 4) Generate
    with torch.no_grad():   # faster inference
        outputs = model.generate(
            **inputs,
            max_new_tokens=max_tokens,
            do_sample=True,
            temperature=0.7,
            top_p=0.9
        )

    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    answer = response[len(prompt):].strip()
    return answer
