# ---------------------------------------------------
# SEVERITY WEIGHTS
# ---------------------------------------------------

SEVERITY_WEIGHTS = {

    "high": 3,
    "medium": 2,
    "low": 1
}

# ---------------------------------------------------
# LEGACY SIGNAL SEVERITY MAP
# ---------------------------------------------------

LEGACY_SIGNAL_SEVERITY = {

    "rollback": "high",
    "escalation": "high",
    "untested": "high",
    "fragility": "high",

    "dependency": "medium",
    "unclear": "medium",
    "pending": "medium",
    "partially": "medium",
    "unstable": "medium",
    "incomplete": "medium",

    "concern": "low",
    "risk": "low",
    "weak": "low",
    "uncertain": "low"
}

# ---------------------------------------------------
# CALCULATE EXPOSURE SCORE
# ---------------------------------------------------

def calculate_exposure_score(evidence_packets):

    total_score = 0

    # ---------------------------------------------------
    # SCORE SIGNALS
    # ---------------------------------------------------

    for packet in evidence_packets:

        for signal in packet["signal_candidates"]:

            # -------------------------------------------
            # NEW STRUCTURED SIGNALS
            # -------------------------------------------

            if isinstance(signal, dict):

                severity = signal["severity"]

            # -------------------------------------------
            # LEGACY STRING SIGNALS
            # -------------------------------------------

            else:

                severity = LEGACY_SIGNAL_SEVERITY.get(
                    signal,
                    "low"
                )

            total_score += SEVERITY_WEIGHTS.get(
                severity,
                0
            )

    # ---------------------------------------------------
    # DETERMINE EXPOSURE LEVEL
    # ---------------------------------------------------

    if total_score >= 40:

        exposure_level = "HIGH"

    elif total_score >= 20:

        exposure_level = "MEDIUM"

    else:

        exposure_level = "LOW"

    return {

        "total_score": total_score,

        "exposure_level": exposure_level
    }