# preprocessing layer

import PyPDF2

def extract_text(filepath):
    text = ""

    if filepath.endswith(".pdf"):
        with open(filepath, 'rb') as f:
            reader = PyPDF2.PdfReader(f)
            for page in reader.pages:
                text += page.extract_text()

    elif filepath.endswith(".txt"):
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            text = f.read()

    else:
        text = "Unsupported file format"

    return text