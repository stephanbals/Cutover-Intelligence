```python
import streamlit as st

from ingestion.uploader import handle_uploaded_files
from engine.evidence_normalizer import normalize_evidence
from engine.exposure_scoring import calculate_exposure_score
from engine.exposure_summary import generate_exposure_summary
from validators.signal_validator import validate_signals


# ---------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------

st.set_page_config(
    page_title="Cutover Intelligence",
    page_icon="⚠️",
    layout="wide"
)


# ---------------------------------------------------
# SESSION STATE
# ---------------------------------------------------

if "show_guidance" not in st.session_state:
    st.session_state.show_guidance = True


# ---------------------------------------------------
# MAIN UI
# ---------------------------------------------------


def run_ui():

    # ---------------------------------------------------
    # HEADER
    # ---------------------------------------------------

    st.title("Cutover Intelligence")
    st.caption("Operational Exposure & Execution Coherence Intelligence")

    st.markdown("---")

    # ---------------------------------------------------
    # ONBOARDING / TRUST MODAL
    # ---------------------------------------------------

    if st.session_state.show_guidance:

        modal_container = st.container(border=True)

        with modal_container:

            header_col1, header_col2 = st.columns([20, 1])

            with header_col1:
                st.subheader("What Operational Risks Can This Detect & How To Use")

            with header_col2:

                if st.button("✕", key="close_guidance"):
                    st.session_state.show_guidance = False
                    st.rerun()

            st.info("""
WHAT THIS PLATFORM DOES

This platform analyzes operational evidence from complex transformations and cutovers to surface recurring operational fragility, dependency instability, rollback uncertainty, escalation patterns, readiness inconsistencies, and execution coherence risks across fragmented operational artifacts.

WHY THIS EXISTS

Large transformations often distribute operational reality across spreadsheets, RAID logs, meeting notes, escalation discussions, readiness trackers, governance layers, and inconsistent reporting structures.

The platform aggregates fragmented operational signals into a consolidated operational exposure assessment.

SUPPORTED TRANSFORMATION SCENARIOS

- SAP cutovers
- ERP transformations
- cloud migration cutovers
- SaaS/platform migrations
- infrastructure transitions
- major operational release waves
- multi-stream transformation programs

WHAT THE FREE TIER PROVIDES

The Free Tier currently provides deterministic evidence-first operational exposure analysis including:

- recurring fragility signal detection
- operational exposure scoring
- contradiction visibility
- escalation pattern concentration
- rollback concern aggregation
- dependency instability surfacing
- operational interpretation generation

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
- governance reporting extracts
- hypercare planning evidence

SUPPORTED FILE TYPES

- XLSX / CSV
- DOCX / PPTX / PDF / TXT
- PNG / JPG / JPEG
- Email exports
- Teams notes
- SharePoint extracts

PRIVACY & OPERATIONAL TRUST

Uploaded operational evidence is processed only for the active assessment session.

Operational data is not intentionally retained, sold, or used for external model training or secondary purposes.

Please avoid uploading production credentials, personal employee data, or regulated customer information.

HOW TO USE

1. Fill in operational context fields
2. Upload operational evidence
3. Run assessment
4. Review operational fragility themes and exposure indicators
            """)

            if st.button("Enter Platform", key="enter_platform"):
                st.session_state.show_guidance = False
                st.rerun()

        st.markdown("---")

    # ---------------------------------------------------
    # OPERATIONAL CONTEXT
    # ---------------------------------------------------

    st.header("Operational Context")

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
        "Any Other Optional Operational Observations?"
    )

    selected_tier = st.selectbox(
        "Assessment Tier",
        [
            "FREE"
        ]
    )

    st.markdown("---")

    # ---------------------------------------------------
    # FILE UPLOADS
    # ---------------------------------------------------

    st.header("Operational Evidence Upload")

    st.warning(
        "Please avoid uploading production credentials, personal employee data, or regulated customer information."
    )

    uploaded_files = st.file_uploader(
        "Upload Operational Evidence",
        type=[
            "xlsx",
            "csv",
            "docx",
            "pptx",
            "pdf",
            "txt",
            "png",
            "jpg",
            "jpeg"
        ],
        accept_multiple_files=True
    )

    # ---------------------------------------------------
    # RUN ANALYSIS
    # ---------------------------------------------------

    st.markdown("---")

    run_analysis = st.button(
        "Run Operational Exposure Assessment",
        type="primary"
    )

    # ---------------------------------------------------
    # ANALYSIS EXECUTION
    # ---------------------------------------------------

    if run_analysis:

        if not uploaded_files:
            st.error("Please upload at least one operational evidence file.")
            return

        with st.spinner("Analyzing operational evidence..."):

            extracted_text = handle_uploaded_files(uploaded_files)

            normalized_evidence = normalize_evidence(extracted_text)

            validated_signals = validate_signals(normalized_evidence)

            exposure_results = calculate_exposure_score(validated_signals)

            exposure_summary = generate_exposure_summary(exposure_results)

        st.success("Operational evidence analyzed successfully.")

        st.markdown("---")

        # ---------------------------------------------------
        # OPERATIONAL CONTEXT OUTPUT
        # ---------------------------------------------------

        st.header("Operational Context")

        st.json(
            {
                "project_name": project_name,
                "systems": systems,
                "timeline": timeline,
                "deployment_type": deployment_type,
                "observations": observations,
                "selected_tier": selected_tier,
                "any other affected programs/changes/releases": affected_programs
            }
        )

        st.markdown("---")

        # ---------------------------------------------------
        # FRAGILITY THEMES
        # ---------------------------------------------------

        st.header("Primary Operational Fragility Themes")

        fragility_themes = exposure_results.get("fragility_themes", [])

        if fragility_themes:
            for theme in fragility_themes:
                st.markdown(f"- {theme}")
        else:
            st.write("No major recurring fragility themes detected.")

        st.markdown("---")

        # ---------------------------------------------------
        # EXPOSURE ASSESSMENT
        # ---------------------------------------------------

        st.header("Operational Exposure Assessment")

        st.subheader(
            f"Exposure Level: {exposure_results.get('exposure_level', 'UNKNOWN')}"
        )

        st.metric(
            "Operational Exposure Score",
            exposure_results.get("exposure_score", 0)
        )

        st.subheader("Exposure Interpretation")

        st.write(
            exposure_summary.get(
                "exposure_interpretation",
                "No exposure interpretation available."
            )
        )

        st.subheader("Operational Interpretation")

        st.write(
            exposure_summary.get(
                "operational_interpretation",
                "No operational interpretation available."
            )
        )

        st.markdown("---")

        # ---------------------------------------------------
        # FREE TIER UPSELL
        # ---------------------------------------------------

        st.info("""
This assessment was generated using the Free Operational Exposure demonstration tier.

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


# ---------------------------------------------------
# RUN APPLICATION
# ---------------------------------------------------

if __name__ == "__main__":
    run_ui()
```
