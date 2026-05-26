from pathlib import Path

from docx import Document
from PyPDF2 import PdfReader


# ---------------------------------------------------
# DETECT SOURCE CATEGORY
# ---------------------------------------------------

def detect_source_category(file_type):

    if file_type in [".txt"]:

        return "unstructured_text"

    elif file_type in [".docx", ".pdf"]:

        return "document"

    elif file_type in [".xlsx", ".csv"]:

        return "structured_data"

    elif file_type in [".png", ".jpg", ".jpeg"]:

        return "image"

    elif file_type in [".pptx"]:

        return "presentation"

    else:

        return "unknown"


# ---------------------------------------------------
# NORMALIZE TEXT
# ---------------------------------------------------

def normalize_text(raw_text):

    if not raw_text:

        return ""

    normalized = raw_text.strip()

    normalized = normalized.replace("\n\n", "\n")

    normalized = normalized.replace("\r", "")

    return normalized


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

    text = []

    for paragraph in doc.paragraphs:

        text.append(paragraph.text)

    return "\n".join(text)


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
# EXTRACT TEXT
# ---------------------------------------------------

def extract_text(file_path, file_type):

    try:

        if file_type == ".txt":

            return extract_txt(file_path)

        elif file_type == ".docx":

            return extract_docx(file_path)

        elif file_type == ".pdf":

            return extract_pdf(file_path)

        else:

            return ""

    except Exception:

        return ""


# ---------------------------------------------------
# BUILD EVIDENCE PACKET
# ---------------------------------------------------

def build_evidence_packet(saved_file):

    file_path = Path(saved_file["path"])

    file_type = file_path.suffix.lower()

    extracted_text = extract_text(
        file_path,
        file_type
    )

    packet = {

        "filename": saved_file["filename"],

        "path": saved_file["path"],

        "file_type": file_type,

        "source_category": detect_source_category(
            file_type
        ),

        "raw_text": extracted_text,

        "normalized_text": normalize_text(
            extracted_text
        ),

        "signal_candidates": []
    }

    return packet


# ---------------------------------------------------
# NORMALIZE EVIDENCE
# ---------------------------------------------------

def normalize_evidence(saved_files):

    normalized_packets = []

    for saved_file in saved_files:

        packet = build_evidence_packet(saved_file)

        normalized_packets.append(packet)

    return normalized_packets