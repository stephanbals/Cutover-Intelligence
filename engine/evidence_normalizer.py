from pathlib import Path

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

    normalized = raw_text.strip()

    normalized = normalized.replace("\n\n", "\n")

    return normalized

# ---------------------------------------------------
# BUILD NORMALIZED EVIDENCE PACKET
# ---------------------------------------------------

def build_evidence_packet(registry_entry, extracted_text):

    packet = {

        "evidence_id": registry_entry["evidence_id"],

        "filename": registry_entry["filename"],

        "file_type": registry_entry["file_type"],

        "registered_at": registry_entry["registered_at"],

        "source_category": detect_source_category(
            registry_entry["file_type"]
        ),

        "raw_text": extracted_text,

        "normalized_text": normalize_text(extracted_text),

        "signal_candidates": []
    }

    return packet