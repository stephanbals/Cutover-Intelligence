# ---------------------------------------------------
# TIER CONFIGURATION
# ---------------------------------------------------

TIER_CONFIG = {

    "FREE": {

        "signal_detection": True,
        "exposure_summary": True,
        "exposure_scoring": True,

        "contradiction_analysis": False,
        "trajectory_analysis": False,
        "governance_analysis": False,
        "executive_summary": False
    },

    "TIER1": {

        "signal_detection": True,
        "exposure_summary": True,
        "exposure_scoring": True,

        "contradiction_analysis": True,
        "trajectory_analysis": False,
        "governance_analysis": False,
        "executive_summary": True
    },

    "TIER2": {

        "signal_detection": True,
        "exposure_summary": True,
        "exposure_scoring": True,

        "contradiction_analysis": True,
        "trajectory_analysis": True,
        "governance_analysis": False,
        "executive_summary": True
    },

    "TIER3": {

        "signal_detection": True,
        "exposure_summary": True,
        "exposure_scoring": True,

        "contradiction_analysis": True,
        "trajectory_analysis": True,
        "governance_analysis": True,
        "executive_summary": True
    }
}