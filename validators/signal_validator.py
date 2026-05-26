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

def validate_signals(evidence_packets):

    validated_packets = []

    # ---------------------------------------------------
    # PROCESS ALL PACKETS
    # ---------------------------------------------------

    for packet in evidence_packets:

        text = str(
            packet.get(
                "normalized_text",
                ""
            )
        ).lower()

        detected_signals = []

        # ---------------------------------------------------
        # DETECT SIGNAL KEYWORDS
        # ---------------------------------------------------

        for keyword in RISK_KEYWORDS:

            if keyword in text:

                detected_signals.append(keyword)

        # ---------------------------------------------------
        # ATTACH SIGNALS TO PACKET
        # ---------------------------------------------------

        packet["signal_candidates"] = detected_signals

        validated_packets.append(packet)

    # ---------------------------------------------------
    # RETURN VALIDATED PACKETS
    # ---------------------------------------------------

    return validated_packets