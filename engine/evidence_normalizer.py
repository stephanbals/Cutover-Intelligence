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

    if not raw_text:

        return ""

    normalized = raw_text.strip()

    normalized = normalized.replace("\n\n", "\n")

    normalized = normalized.replace("\r", "")

    return normalized


# ---------------------------------------------------
# BUILD EVIDENCE PACKET
# ---------------------------------------------------

def build_evidence_packet(saved_file):

    file_path = Path(saved_file["path"])

    file_type = file_path.suffix.lower()

    packet = {

        "filename": saved_file["filename"],

        "path": saved_file["path"],

        "file_type": file_type,

        "source_category": detect_source_category(
            file_type
        ),

        "raw_text": "",

        "normalized_text": "",

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