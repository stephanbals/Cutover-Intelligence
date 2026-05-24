# ---------------------------------------------------
# SIGNAL KEYWORDS
# ---------------------------------------------------

RISK_KEYWORDS = [

    "untested",
    "unclear",
    "pending",
    "under discussion",
    "partially",
    "concern",
    "risk",
    "weak",
    "uncertain",
    "rollback",
    "dependency",
    "escalation",
    "fragility",
    "incomplete",
    "unstable"
]

# ---------------------------------------------------
# VALIDATE SIGNALS
# ---------------------------------------------------

def validate_signals(evidence_packet):

    text = evidence_packet["normalized_text"].lower()

    detected_signals = []

    for keyword in RISK_KEYWORDS:

        if keyword in text:

            detected_signals.append(keyword)

    return detected_signals