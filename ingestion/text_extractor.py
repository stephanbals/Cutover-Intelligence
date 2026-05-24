from pathlib import Path
from docx import Document
from PyPDF2 import PdfReader
import pandas as pd

# ---------------------------------------------------
# TXT EXTRACTION
# ---------------------------------------------------

def extract_txt(file_path):

    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:

        return f.read()

# ---------------------------------------------------
# DOCX EXTRACTION
# ---------------------------------------------------

def extract_docx(file_path):

    doc = Document(file_path)

    full_text = []

    for para in doc.paragraphs:

        full_text.append(para.text)

    return "\n".join(full_text)

# ---------------------------------------------------
# PDF EXTRACTION
# ---------------------------------------------------

def extract_pdf(file_path):

    reader = PdfReader(file_path)

    text = []

    for page in reader.pages:

        extracted = page.extract_text()

        if extracted:

            text.append(extracted)

    return "\n".join(text)

# ---------------------------------------------------
# CSV / XLSX EXTRACTION
# ---------------------------------------------------

def extract_spreadsheet(file_path):

    path = Path(file_path)

    if path.suffix == ".csv":

        df = pd.read_csv(file_path)

    else:

        df = pd.read_excel(file_path)

    return df.to_string()

# ---------------------------------------------------
# MAIN EXTRACTION ROUTER
# ---------------------------------------------------

def extract_text(file_path):

    suffix = Path(file_path).suffix.lower()

    if suffix == ".txt":

        return extract_txt(file_path)

    elif suffix == ".docx":

        return extract_docx(file_path)

    elif suffix == ".pdf":

        return extract_pdf(file_path)

    elif suffix in [".csv", ".xlsx"]:

        return extract_spreadsheet(file_path)

    else:

        return "Unsupported file type for extraction."