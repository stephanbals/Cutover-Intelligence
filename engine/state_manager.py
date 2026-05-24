import json
from pathlib import Path
from datetime import datetime

# ---------------------------------------------------
# FILE PATHS
# ---------------------------------------------------

INTAKE_PATH = Path("state/intake.json")

SESSION_PATH = Path("state/session_state.json")

# ---------------------------------------------------
# SAVE INTAKE
# ---------------------------------------------------

def save_intake(intake_data):

    with open(INTAKE_PATH, "w") as f:
        json.dump(intake_data, f, indent=4)

# ---------------------------------------------------
# SAVE SESSION STATE
# ---------------------------------------------------

def save_session_state():

    session_state = {
        "current_stage": "intake",
        "validation_status": "pending",
        "workflow_lock": "open",
        "last_updated": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    with open(SESSION_PATH, "w") as f:
        json.dump(session_state, f, indent=4)

# ---------------------------------------------------
# LOAD INTAKE
# ---------------------------------------------------

def load_intake():

    if not INTAKE_PATH.exists():
        return {}

    with open(INTAKE_PATH, "r") as f:
        return json.load(f)

# ---------------------------------------------------
# LOAD SESSION STATE
# ---------------------------------------------------

def load_session_state():

    if not SESSION_PATH.exists():
        return {}

    with open(SESSION_PATH, "r") as f:
        return json.load(f)