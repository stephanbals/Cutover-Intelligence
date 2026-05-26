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

        signal_candidates = packet.get(
            "signal_candidates",
            []
        )

        for signal in signal_candidates:

            # -------------------------------------------
            # STRUCTURED SIGNAL OBJECTS
            # -------------------------------------------

            if isinstance(signal, dict):

                severity = signal.get(
                    "severity",
                    "low"
                )

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

    # ---------------------------------------------------
    # BUILD FRAGILITY THEMES
    # ---------------------------------------------------

    fragility_themes = []

    if total_score >= 40:

        fragility_themes.append(
            "High concentration of recurring operational fragility indicators detected."
        )

        fragility_themes.append(
            "Escalation, rollback, dependency, or readiness instability signals appear repeatedly across evidence sources."
        )

    elif total_score >= 20:

        fragility_themes.append(
            "Moderate operational instability patterns detected across uploaded evidence."
        )

    else:

        fragility_themes.append(
            "Limited recurring operational fragility currently detected."
        )

    # ---------------------------------------------------
    # RETURN RESULTS
    # ---------------------------------------------------

    return {

        "exposure_score": total_score,

        "exposure_level": exposure_level,

        "fragility_themes": fragility_themes
    }