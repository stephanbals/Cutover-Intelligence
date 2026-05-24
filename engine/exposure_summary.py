# ---------------------------------------------------
# GENERATE EXPOSURE SUMMARY
# ---------------------------------------------------

def generate_exposure_summary(evidence_packets):

    signal_counter = {}

    # ---------------------------------------------------
    # COUNT SIGNALS
    # ---------------------------------------------------

    for packet in evidence_packets:

        for signal in packet["signal_candidates"]:

            # -------------------------------------------
            # HANDLE STRUCTURED SIGNAL OBJECTS
            # -------------------------------------------

            if isinstance(signal, dict):

                signal_name = signal["signal"]

            # -------------------------------------------
            # HANDLE LEGACY STRING SIGNALS
            # -------------------------------------------

            else:

                signal_name = signal

            if signal_name not in signal_counter:

                signal_counter[signal_name] = 0

            signal_counter[signal_name] += 1

    # ---------------------------------------------------
    # BUILD SUMMARY
    # ---------------------------------------------------

    summary_lines = []

    for signal, count in signal_counter.items():

        if count >= 3:

            summary_lines.append(
                f"Repeated operational concern detected around '{signal}' across multiple evidence sources."
            )

        elif count == 2:

            summary_lines.append(
                f"Operational concern related to '{signal}' detected in more than one evidence source."
            )

    # ---------------------------------------------------
    # FALLBACK
    # ---------------------------------------------------

    if not summary_lines:

        summary_lines.append(
            "No major repeated operational fragility patterns detected."
        )

    return summary_lines