from pathlib import Path


# ---------------------------------------------------
# UPLOAD DIRECTORY
# ---------------------------------------------------

UPLOAD_DIR = Path("state/uploads")

# Automatically create directory if missing
UPLOAD_DIR.mkdir(
    parents=True,
    exist_ok=True
)


# ---------------------------------------------------
# SAVE UPLOADED FILE
# ---------------------------------------------------

def save_uploaded_file(uploaded_file):

    # Build safe file path
    file_path = UPLOAD_DIR / uploaded_file.name

    # Save uploaded file
    with open(file_path, "wb") as f:

        f.write(
            uploaded_file.getbuffer()
        )

    # Return metadata
    return {

        "filename": uploaded_file.name,

        "path": str(file_path),

        "size_bytes": uploaded_file.size
    }