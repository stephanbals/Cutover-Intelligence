import json
import uuid
from pathlib import Path
from datetime import datetime

# ---------------------------------------------------
# REGISTRY FILE
# ---------------------------------------------------

REGISTRY_FILE = Path("state/file_registry.json")

# ---------------------------------------------------
# LOAD REGISTRY
# ---------------------------------------------------

def load_registry():

    if not REGISTRY_FILE.exists():

        return []

    with open(REGISTRY_FILE, "r") as f:

        return json.load(f)

# ---------------------------------------------------
# SAVE REGISTRY
# ---------------------------------------------------

def save_registry(registry_data):

    with open(REGISTRY_FILE, "w") as f:

        json.dump(registry_data, f, indent=4)

# ---------------------------------------------------
# REGISTER FILE
# ---------------------------------------------------

def register_file(file_data):

    registry = load_registry()

    registry_entry = {

        "evidence_id": str(uuid.uuid4()),

        "filename": file_data["filename"],

        "path": file_data["path"],

        "file_type": Path(file_data["filename"]).suffix,

        "registered_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    registry.append(registry_entry)

    save_registry(registry)

    return registry_entry