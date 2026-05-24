# ---------------------------------------------------
# CONTRADICTION PATTERNS
# ---------------------------------------------------

CONTRADICTION_PATTERNS = [

    (
        ["stable", "validated", "approved"],
        ["unclear", "pending", "unresolved"]
    ),

    (
        ["ready", "complete"],
        ["concern", "risk", "fragility"]
    ),

    (
        ["frozen", "locked"],
        ["change", "changing", "late"]
    ),

    (
        ["supported", "covered"],
        ["unclear", "missing", "pending"]
    )
]

# ---------------------------------------------------
# DETECT CONTRADICTIONS
# ---------------------------------------------------

def detect_contradictions(evidence_packets):

    findings = []

    combined_text = ""

    # ---------------------------------------------------
    # MERGE ALL EVIDENCE TEXT
    # ---------------------------------------------------

    for packet in evidence_packets:

        combined_text += " "

        combined_text += packet.get(
            "extracted_text",
            ""
        ).lower()

    # ---------------------------------------------------
    # CHECK PATTERNS
    # ---------------------------------------------------

    for positive_group, negative_group in CONTRADICTION_PATTERNS:

        positive_found = any(
            word in combined_text
            for word in positive_group
        )

        negative_found = any(
            word in combined_text
            for word in negative_group
        )

        if positive_found and negative_found:

            findings.append(

                f"""
                Contradictory operational signals detected between:

                Positive indicators:
                {", ".join(positive_group)}

                Conflicting indicators:
                {", ".join(negative_group)}
                """
            )

    return findings