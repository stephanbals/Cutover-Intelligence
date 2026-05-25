import streamlit as st

from ingestion.uploader import handle_uploaded_files
from engine.evidence_normalizer import normalize_evidence
from engine.exposure_scoring import calculate_exposure_score
from engine.exposure_summary import generate_exposure_summary
from validators.signal_validator import validate_signals


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
    # PAGE STYLING
    # ---------------------------------------------------

    st.markdown(
        """
        <style>

        .stApp {
            background-color: #050816;
        }

        .modal-overlay {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background-color: rgba(0,0,0,0.82);
            z-index: 999;
        }

        .modal-container {
            position: fixed;
            top: 4%;
            left: 50%;
            transform: translateX(-50%);
            width: 78%;
            max-height: 88vh;
            overflow-y: auto;
            background-color: #0f172a;
            padding: 2rem;
            border-radius: 16px;
            border: 1px solid #334155;
            z-index: 1000;
            box-shadow: 0px 0px 40px rgba(0,0,0,0.55);
        }

        .modal-title {
            font-size: 2.2rem;
            font-weight: 700;
            margin-bottom: 0.2rem;
            color: white;
        }

        .modal-subtitle {
            color: #94a3b8;
            margin-bottom: 1.5rem;
        }

        .section-header {
            font-size: 1.15rem;
            font-weight: 700;
            margin-top: 1.4rem;
            margin-bottom: 0.5rem;
            color: white;
        }

        .section-text {
            color: #d1d5db;
            line-height: 1.7;
            font-size: 0.96rem;
        }

        </style>
        """,
        unsafe_allow_html=True
    )

    # ---------------------------------------------------
    # PAGE HEADER
    # ---------------------------------------------------

    st.title("Operational Exposure Snapshot")

    st.caption(
        "Evidence-first operational intelligence for complex transformations and cutovers."
    )

    # ---------------------------------------------------
    # ONBOARDING MODAL
    # ---------------------------------------------------

    if st.session_state.show_guidance:

        st.markdown(
            """
            <div class="modal-overlay"></div>
            """,
            unsafe_allow_html=True
        )

        st.markdown(
            """
            <div class="modal-container">
            """,
            unsafe_allow_html=True
        )

        close_col1, close_col2 = st.columns([20, 1])

        with close_col1:

            st.markdown(
                """
                <div class="modal-title">
                Cutover Intelligence
                </div>

                <div class="modal-subtitle">
                Operational Exposure & Execution Coherence Intelligence
                </div>
                """,
                unsafe_allow_html=True
            )

        with close_col2:

            if st.button("✕", key="close_modal"):

                st.session_state.show_guidance = False
                st.rerun()

        st.markdown(
            """
            <div class="section-header">
            WHAT THIS PLATFORM DOES
            </div>

            <div class="section-text">
            This platform analyzes operational evidence from complex transformations and cutovers to surface recurring operational fragility, dependency instability, rollback uncertainty, escalation patterns, readiness inconsistencies, and execution coherence risks across fragmented operational artifacts.
            </div>

            <div class="section-header">
            WHY THIS EXISTS
            </div>

            <div class="section-text">
            Large transformations often distribute operational reality across spreadsheets, RAID logs, meeting notes, escalation discussions, readiness trackers, governance layers, and inconsistent reporting structures.
            <br><br>
            The platform aggregates fragmented operational signals into a consolidated operational exposure assessment.
            </div>

            <div class="section-header">
            SUPPORTED TRANSFORMATION SCENARIOS
            </div>

            <div class="section-text">
            • SAP cutovers<br>
            • ERP transformations<br>
            • cloud migration cutovers<br>
            • SaaS/platform migrations<br>
            • infrastructure transitions<br>
            • major operational release waves<br>
            • multi-stream transformation programs
            </div>

            <div class="section-header">
            RECOMMENDED OPERATIONAL EVIDENCE
            </div>

            <div class="section-text">
            • RAID logs<br>
            • dependency registers<br>
            • risk registers<br>
            • cutover plans<br>
            • readiness reviews<br>
            • escalation logs<br>
            • meeting notes<br>
            • operational spreadsheets<br>
            • screenshots and exports<br>
            • governance reporting extracts
            </div>

            <div class="section-header">
            SUPPORTED FILE TYPES
            </div>

            <div class="section-text">
            • XLSX / CSV<br>
            • DOCX / PPTX / PDF / TXT<br>
            • PNG / JPG / JPEG
            </div>

            <div class="section-header">
            PRIVACY & OPERATIONAL TRUST
            </div>

            <div class="section-text">
            Uploaded operational evidence is processed only for the active assessment session.
            <br><br>
            Operational data is not intentionally retained, sold, or used for external model training or secondary purposes.
            <br><br>
            Please avoid uploading production credentials, personal employee data, or regulated customer information.
            </div>

            <div class="section-header">
            HOW TO USE
            </div>

            <div class="section-text">
            1. Fill in operational context fields<br>
            2. Upload operational evidence<br>
            3. Run assessment<br>
            4. Review operational fragility themes and exposure indicators
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown("<br>", unsafe_allow_html=True)

        if st.button("Enter Platform", key="enter_platform"):

            st.session_state.show_guidance = False
            st.rerun()

        st.markdown(
            """
            </div>
            """,
            unsafe_allow_html=True
        )

    # ---------------------------------------------------
    # TIER SELECTION
    # ---------------------------------------------------

    selected_tier = st.selectbox(
        "Select Intelligence Tier",
        [
            "FREE"
        ]
    )

    st.markdown("---")

    # ---------------------------------------------------
    # OPERATIONAL CONTEXT
    # ---------------------------------------------------

    st.header("Step 1 — Operational Context")

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

    st.markdown("---")

    # ---------------------------------------------------
    # FILE UPLOAD
    # ---------------------------------------------------

    st.header("Step 2 — Upload Operational Evidence")

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

    st.markdown("---")

    # ---------------------------------------------------
    # ANALYSIS BUTTON
    # ---------------------------------------------------

    run_analysis = st.button(
        "Run Operational Exposure Assessment",
        type="primary"
    )

    # ---------------------------------------------------
    # RUN ANALYSIS
    # ---------------------------------------------------

    if run_analysis:

        if not uploaded_files:

            st.error(
                "Please upload at least one operational evidence file."
            )

            return

        with st.spinner("Analyzing operational evidence..."):

            extracted_text = handle_uploaded_files(uploaded_files)

            normalized_evidence = normalize_evidence(extracted_text)

            validated_signals = validate_signals(normalized_evidence)

            exposure_results = calculate_exposure_score(validated_signals)

            exposure_summary = generate_exposure_summary(exposure_results)

        st.success(
            "Operational evidence analyzed successfully."
        )

        st.markdown("---")

        st.header("Primary Operational Fragility Themes")

        fragility_themes = exposure_results.get(
            "fragility_themes",
            []
        )

        if fragility_themes:

            for theme in fragility_themes:

                st.warning(theme)

        else:

            st.success(
                "No major recurring fragility themes detected."
            )

        st.markdown("---")

        st.header("Operational Exposure Assessment")

        st.error(
            f"""
Exposure Level: {exposure_results.get('exposure_level', 'UNKNOWN')}

Operational Exposure Score:
{exposure_results.get('exposure_score', 0)} / 150
"""
        )

        st.info(
            exposure_summary.get(
                "exposure_interpretation",
                "No exposure interpretation available."
            )
        )

        st.markdown("---")

        st.header("Operational Interpretation")

        st.write(
            exposure_summary.get(
                "operational_interpretation",
                "No operational interpretation available."
            )
        )

        st.markdown("---")

        st.info(
            """
This assessment was generated using the Free Operational Exposure tier.

Advanced intelligence tiers provide:

- deeper contradiction analysis
- operational weak-spot interpretation
- survivability trajectory analysis
- governance and execution intelligence
- executive operational review outputs

Advanced operational review packs available from €49 excl. VAT.
"""
        )