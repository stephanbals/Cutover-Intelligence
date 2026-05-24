import streamlit as st

from engine.state_manager import (
    save_intake,
    save_session_state,
    load_intake
)

from ingestion.uploader import save_uploaded_file
from ingestion.text_extractor import extract_text
from ingestion.file_registry import register_file

from engine.evidence_normalizer import build_evidence_packet
from validators.signal_validator import validate_signals
from engine.exposure_summary import generate_exposure_summary
from engine.exposure_scoring import calculate_exposure_score
from engine.tier_config import TIER_CONFIG
from engine.contradiction_analysis import detect_contradictions


# ---------------------------------------------------
# MAIN UI
# ---------------------------------------------------

def run_ui():

    # ---------------------------------------------------
    # PAGE CONFIG
    # ---------------------------------------------------

    st.set_page_config(
        page_title="Cutover Intelligence",
        layout="wide"
    )

    # ---------------------------------------------------
    # SESSION STATE
    # ---------------------------------------------------

    if "show_guidance" not in st.session_state:
        st.session_state.show_guidance = False

    # ---------------------------------------------------
    # PAGE TITLE
    # ---------------------------------------------------

    st.title("Operational Exposure Snapshot")

    st.caption(
        "Evidence-first operational intelligence for complex transformations and cutovers."
    )

    # ---------------------------------------------------
    # TIER SELECTION
    # ---------------------------------------------------

    selected_tier = st.selectbox(
        "Select Intelligence Tier",
        [
            "FREE",
            "TIER1",
            "TIER2",
            "TIER3"
        ]
    )

    tier_settings = TIER_CONFIG[selected_tier]

    # ---------------------------------------------------
    # HEADER
    # ---------------------------------------------------

    col1, col2 = st.columns([6, 2])

    with col1:
        st.subheader(
            "Step 1 — Operational Context"
        )

    with col2:

        if st.button(
            "What Operational Risks Can This Detect & How To Use"
        ):
            st.session_state.show_guidance = True

    # ---------------------------------------------------
    # GUIDANCE PANEL
    # ---------------------------------------------------

    if st.session_state.show_guidance:

        with st.container():

            header_col1, header_col2 = st.columns([20, 1])

            with header_col1:

                st.subheader(
                    "Operational Exposure Intelligence"
                )

            with header_col2:

                if st.button("✕"):

                    st.session_state.show_guidance = False
                    st.rerun()

            st.info("""
WHAT THIS PLATFORM DOES

This platform analyzes operational evidence from complex transformations and cutovers to identify recurring operational fragility signals, dependency exposure, rollback concerns, escalation patterns, readiness inconsistencies, and survivability risks across fragmented operational artifacts.

WHY THIS EXISTS

Large transformations often distribute operational reality across spreadsheets, RAID logs, meeting notes, escalation discussions, readiness trackers, and inconsistent reporting structures.

The platform aggregates these fragmented operational signals into a consolidated operational exposure view.

WHAT THE FREE TIER PROVIDES

The Free Tier provides deterministic evidence-first operational exposure analysis, including:

- recurring fragility signal detection
- operational exposure scoring
- contradiction detection
- repeated escalation pattern visibility
- rollback and dependency concern aggregation

RECOMMENDED OPERATIONAL EVIDENCE

- RAID logs
- dependency registers
- risk registers
- cutover plans
- readiness reviews
- escalation logs
- meeting notes
- operational spreadsheets
- screenshots and exports

SUPPORTED FILE TYPES

- XLSX / CSV
- DOCX / PPTX / PDF / TXT
- PNG / JPG / JPEG
- Email exports
- Teams notes
- SharePoint extracts
            """)

    # ---------------------------------------------------
    # OPERATIONAL CONTEXT
    # ---------------------------------------------------

    project_name = st.text_input(
        "Project Name"
    )

    systems = st.text_area(
        "Systems Involved"
    )

    timeline = st.text_input(
        "Timeline / Deployment Window"
    )

    deployment_type = st.selectbox(
        "Deployment Type",
        [
            "SAP Cutover",
            "Cloud Migration",
            "Infrastructure Migration",
            "ERP Transformation",
            "Major Release",
            "Platform Migration",
            "Other"
        ]
    )

    affected_programs = st.text_area(
        "Any Other Projects, Programs, Releases, or Transformations Potentially Influenced by This Operational Change?"
    )

    observations = st.text_area(
        "Any other Optional Operational Observations the user of the Platform would like to give at this moment in time?"
    )

    # ---------------------------------------------------
    # EVIDENCE UPLOADS
    # ---------------------------------------------------

    st.subheader(
        "Step 2 — Operational Evidence Upload"
    )

    risk_files = st.file_uploader(
        "Upload Risk Files",
        accept_multiple_files=True,
        type=[
            "txt",
            "csv",
            "docx",
            "pdf",
            "xlsx",
            "pptx"
        ],
        key="risk_files"
    )

    dependency_files = st.file_uploader(
        "Upload Dependency Files",
        accept_multiple_files=True,
        type=[
            "txt",
            "csv",
            "docx",
            "pdf",
            "xlsx",
            "pptx"
        ],
        key="dependency_files"
    )

    uploaded_files = st.file_uploader(
        "Upload Additional Operational Evidence",
        accept_multiple_files=True,
        type=[
            "txt",
            "csv",
            "docx",
            "pdf",
            "xlsx",
            "pptx",
            "png",
            "jpg",
            "jpeg"
        ],
        key="general_files"
    )

    # ---------------------------------------------------
    # ANALYZE BUTTON
    # ---------------------------------------------------

    if st.button("Analyze Operational Exposure"):

        intake_data = {
            "project_name": project_name,
            "systems": systems,
            "timeline": timeline,
            "deployment_type": deployment_type,
            "observations": observations,
            "selected_tier": selected_tier,
            "any other affected programs/changes/releases": affected_programs,
        }

        # ---------------------------------------------------
        # SAVE STATE
        # ---------------------------------------------------

        save_intake(intake_data)

        save_session_state()

        # ---------------------------------------------------
        # PROCESS EVIDENCE
        # ---------------------------------------------------

        uploaded_file_data = []

        all_uploaded_files = []

        if risk_files:
            all_uploaded_files.extend(risk_files)

        if dependency_files:
            all_uploaded_files.extend(dependency_files)

        if uploaded_files:
            all_uploaded_files.extend(uploaded_files)

        if all_uploaded_files:

            with st.spinner(
                "Analyzing operational evidence..."
            ):

                for uploaded_file in all_uploaded_files:

                    # ---------------------------------------
                    # SAVE FILE
                    # ---------------------------------------

                    file_data = save_uploaded_file(
                        uploaded_file
                    )

                    # ---------------------------------------
                    # REGISTER FILE
                    # ---------------------------------------

                    registry_entry = register_file(
                        file_data
                    )

                    # ---------------------------------------
                    # EXTRACT TEXT
                    # ---------------------------------------

                    extracted_text = extract_text(
                        file_data["path"]
                    )

                    # ---------------------------------------
                    # BUILD EVIDENCE PACKET
                    # ---------------------------------------

                    evidence_packet = build_evidence_packet(
                        registry_entry,
                        extracted_text
                    )

                    evidence_packet[
                        "extracted_preview"
                    ] = extracted_text[:1000]

                    # ---------------------------------------
                    # VALIDATE SIGNALS
                    # ---------------------------------------

                    detected_signals = validate_signals(
                        evidence_packet
                    )

                    evidence_packet[
                        "signal_candidates"
                    ] = detected_signals

                    uploaded_file_data.append(
                        evidence_packet
                    )

        # ---------------------------------------------------
        # SUCCESS
        # ---------------------------------------------------

        st.success(
            "Operational evidence analyzed successfully."
        )

        # ---------------------------------------------------
        # OPERATIONAL CONTEXT DISPLAY
        # ---------------------------------------------------

        st.subheader(
            "Operational Context"
        )

        loaded_intake = load_intake()

        st.markdown(f"""
### Project Overview

**Project Name**  
{loaded_intake.get("project_name", "")}

**Deployment Type**  
{loaded_intake.get("deployment_type", "")}

**Timeline / Deployment Window**  
{loaded_intake.get("timeline", "")}

---

### Systems Involved

{loaded_intake.get("systems", "")}

---

### Affected Programs / Releases

{loaded_intake.get("any other affected programs/changes/releases", "")}

---

### Operational Observations

{loaded_intake.get("observations", "")}
        """)

        # ---------------------------------------------------
        # DISPLAY EVIDENCE
        # ---------------------------------------------------

        if uploaded_file_data:

            with st.expander(
                "View Processed Operational Evidence"
            ):

                st.json(uploaded_file_data)

            # ---------------------------------------------------
            # EXPOSURE SUMMARY
            # ---------------------------------------------------

            if tier_settings["exposure_summary"]:

                exposure_summary = generate_exposure_summary(
                    uploaded_file_data
                )

                st.subheader(
                    "Primary Operational Fragility Themes"
                )

                fragility_map = {
                    "unclear": "Rollback and operational ownership uncertainty",
                    "rollback": "Rollback survivability uncertainty",
                    "dependency": "Dependency ambiguity and sequencing instability",
                    "incomplete": "Incomplete readiness validation",
                    "pending": "Pending operational approvals and unresolved actions",
                    "escalation": "Escalation instability and coordination pressure",
                    "concern": "Operational concern concentration across evidence sources",
                    "partially": "Partial readiness and fragmented validation coverage"
                }

                displayed_fragilities = set()

                for item in exposure_summary:

                    cleaned_item = (
                        item
                        .replace(
                            "Repeated operational concern detected around",
                            ""
                        )
                        .replace(
                            "Operational concern related to",
                            ""
                        )
                        .replace(
                            "detected in more than one evidence source.",
                            ""
                        )
                        .replace(
                            "across multiple evidence sources.",
                            ""
                        )
                        .replace(
                            "'",
                            ""
                        )
                        .strip()
                        .lower()
                    )

                    if cleaned_item in fragility_map:

                        readable_fragility = fragility_map[
                            cleaned_item
                        ]

                        if readable_fragility not in displayed_fragilities:

                            st.warning(
                                readable_fragility
                            )

                            displayed_fragilities.add(
                                readable_fragility
                            )

            # ---------------------------------------------------
            # EXPOSURE SCORE
            # ---------------------------------------------------

            if tier_settings["exposure_scoring"]:

                exposure_score = calculate_exposure_score(
                    uploaded_file_data
                )

                st.subheader(
                    "Operational Exposure Assessment"
                )

                st.error(
                    f"""
Exposure Level: {exposure_score['exposure_level']}

Operational Exposure Score: {exposure_score['total_score']} / 150
"""
                )

                score = exposure_score[
                    "total_score"
                ]

                if score <= 20:
                    interpretation = "Minimal Operational Exposure"

                elif score <= 40:
                    interpretation = "Moderate Operational Exposure"

                elif score <= 60:
                    interpretation = "Elevated Operational Exposure"

                elif score <= 80:
                    interpretation = "High Operational Exposure"

                else:
                    interpretation = "Severe Operational Exposure"

                st.info(
                    f"""
Exposure Interpretation

{interpretation}

This assessment identified recurring operational fragility indicators across multiple operational evidence sources.
"""
                )

            # ---------------------------------------------------
            # OPERATIONAL INTERPRETATION
            # ---------------------------------------------------

            st.subheader(
                "Operational Interpretation"
            )

            st.write("""
The uploaded operational evidence suggests recurring operational uncertainty patterns across rollback planning, dependency coordination, readiness validation, and escalation management.

Several evidence sources contain indicators of execution instability, unresolved operational ambiguity, and coordination fragility that may require additional operational review.
            """)

            # ---------------------------------------------------
            # CONTRADICTIONS
            # ---------------------------------------------------

            if tier_settings["contradiction_analysis"]:

                contradictions = detect_contradictions(
                    uploaded_file_data
                )

                if contradictions:

                    st.subheader(
                        "Operational Contradictions"
                    )

                    for contradiction in contradictions:

                        st.info(
                            contradiction
                        )

            # ---------------------------------------------------
            # COMMERCIAL FOOTER
            # ---------------------------------------------------

            st.markdown("---")

            st.caption("""
This assessment was generated using the Free Operational Exposure Intelligence demonstration tier.

Advanced intelligence tiers provide:

- deeper contradiction analysis
- operational weak-spot interpretation
- survivability trajectory analysis
- governance and execution intelligence
- executive operational review outputs

Advanced packs available from €49 excl. VAT.

Contact:
Stephan.Bals@SB3PMAdvisory.com
            """)