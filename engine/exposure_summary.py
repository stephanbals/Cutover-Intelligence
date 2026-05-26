# ---------------------------------------------------
# GENERATE EXPOSURE SUMMARY
# ---------------------------------------------------

def generate_exposure_summary(exposure_results):

    exposure_level = exposure_results.get(
        "exposure_level",
        "UNKNOWN"
    )

    exposure_score = exposure_results.get(
        "exposure_score",
        0
    )

    fragility_themes = exposure_results.get(
        "fragility_themes",
        []
    )

    # ---------------------------------------------------
    # BUILD INTERPRETATION
    # ---------------------------------------------------

    if exposure_level == "HIGH":

        interpretation = (
            "High operational fragility detected across uploaded operational evidence."
        )

    elif exposure_level == "MEDIUM":

        interpretation = (
            "Moderate operational instability patterns detected across uploaded evidence."
        )

    else:

        interpretation = (
            "Limited recurring operational fragility currently detected."
        )

    # ---------------------------------------------------
    # BUILD OPERATIONAL SUMMARY
    # ---------------------------------------------------

    operational_summary = (
        f"Calculated operational exposure score: "
        f"{exposure_score}"
    )

    # ---------------------------------------------------
    # INCLUDE THEMES
    # ---------------------------------------------------

    if fragility_themes:

        operational_summary += (
            "\n\nPrimary operational themes detected:\n- "
            + "\n- ".join(fragility_themes)
        )

    # ---------------------------------------------------
    # RETURN SUMMARY OBJECT
    # ---------------------------------------------------

    return {

        "exposure_interpretation": interpretation,

        "operational_interpretation": operational_summary
    }