from pathlib import Path

# ---------------------------------------------------
# UPLOAD DIRECTORY
# ---------------------------------------------------

UPLOAD_DIR = Path("state/uploads")

# ---------------------------------------------------
# SAVE UPLOADED FILE
# ---------------------------------------------------

def save_uploaded_file(uploaded_file):

    file_path = UPLOAD_DIR / uploaded_file.name

    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    return {
        "filename": uploaded_file.name,
        "path": str(file_path)
    }