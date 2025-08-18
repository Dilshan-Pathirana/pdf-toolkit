from langchain.llms import GPT4All
from langchain.chains.question_answering import load_qa_chain
from langchain.docstore.document import Document
from services.pdf_utils import extract_texts_from_multiple_pdfs

# Path to your downloaded GPT4All model
MODEL_PATH = "models/gpt4all-lora-quantized.bin"

def ask_ai_about_pdfs(pdf_paths, question):
    """
    Extract text from PDFs and ask a local GPT4All model.
    """
    # Step 1: Extract text from PDFs
    pdf_texts = extract_texts_from_multiple_pdfs(pdf_paths)

    # Step 2: Prepare LangChain Documents
    documents = [Document(page_content=text) for text in pdf_texts]

    # Step 3: Initialize GPT4All LLM
    llm = GPT4All(model=MODEL_PATH, verbose=False)

    # Step 4: Load a question-answering chain
    chain = load_qa_chain(llm, chain_type="stuff")

    # Step 5: Run the chain
    answer = chain.run(input_documents=documents, question=question)
    return answer
