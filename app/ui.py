import streamlit as st

from ingestion.uploader import save_uploaded_file
from engine.evidence_normalizer import normalize_evidence
from engine.exposure_scoring import calculate_exposure_score
from engine.exposure_summary import generate_exposure_summary
from validators.signal_validator import validate_signals


# ---------------------------------------------------
# MAIN UI
# ---------------------------------------------------

def run_ui():

    # ---------------------------------------------------
    # SESSION STATE
    # ---------------------------------------------------

    if "show_guidance" not in st.session_state:

        st.session_state.show_guidance = True

    # ---------------------------------------------------
    # PAGE CONFIG
    # ---------------------------------------------------

    st.set_page_config(
        page_title="Cutover Intelligence",
        layout="wide"
    )

    # ---------------------------------------------------
    # GLOBAL STYLE
    # ---------------------------------------------------

    st.markdown(
        """
        <style>

        .stApp {
            background-color: #050816;
        }

        .main-title {
            font-size: 4rem;
            font-weight: 700;
            color: white;
            margin-bottom: 0.5rem;
            line-height: 1.1;
        }

        .main-subtitle {
            color: #94a3b8;
            font-size: 1.1rem;
            margin-bottom: 2rem;
            max-width: 1100px;
            line-height: 1.6;
        }

        .onboarding-card {

            background: #0f172a;

            border: 1px solid #334155;

            border-radius: 18px;

            padding: 2rem;

            box-shadow: 0px 0px 45px rgba(0,0,0,0.35);

            margin-top: 1rem;
            margin-bottom: 2rem;
        }

        .card-title {
            font-size: 2.2rem;
            font-weight: 700;
            color: white;
            margin-bottom: 0.3rem;
        }

        .card-subtitle {
            color: #94a3b8;
            margin-bottom: 1.5rem;
            font-size: 1rem;
        }

        .guidance-banner {

            background: rgba(59,130,246,0.12);

            border: 1px solid rgba(59,130,246,0.35);

            color: #dbeafe;

            padding: 1rem;

            border-radius: 12px;

            font-size: 1rem;

            font-weight: 600;

            margin-bottom: 1.5rem;
        }

        .section-header {

            color: white;

            font-size: 1.05rem;

            font-weight: 700;

            margin-top: 1.5rem;

            margin-bottom: 0.5rem;
        }

        .section-body {

            color: #d1d5db;

            line-height: 1.8;

            font-size: 0.96rem;
        }

        .scroll-cue {

            text-align: center;

            color: #94a3b8;

            font-size: 1rem;

            margin-top: 1rem;

            margin-bottom: 2rem;

            animation: pulse 2s infinite;
        }

        @keyframes pulse {

            0% { opacity: 0.4; }

            50% { opacity: 1; }

            100% { opacity: 0.4; }
        }

        </style>
        """,
        unsafe_allow_html=True
    )

    # ---------------------------------------------------
    # HEADER
    # ---------------------------------------------------

    st.markdown(
        """
        <div class="main-title">
        Detect Transformation Fragility Before Go-Live Failure
        </div>

        <div class="main-subtitle">

        Surface hidden operational, governance, and execution risks before they escalate into delays, rollback events, outages, or transformation failure.

        </div>
        """,
        unsafe_allow_html=True
    )

    # ---------------------------------------------------
    # ONBOARDING / INTRODUCTION
    # ---------------------------------------------------

    if st.session_state.show_guidance:

        with st.container():

            st.markdown(
                """
                <div class="onboarding-card">
                """,
                unsafe_allow_html=True
            )

            st.markdown(
                """
                <div class="guidance-banner">

                👇 Read this quick introduction, then click the ✕ in the top-right corner to start using the platform.

                </div>
                """,
                unsafe_allow_html=True
            )

            intro_col1, intro_col2 = st.columns([20, 1])

            with intro_col1:

                st.markdown(
                    """
                    <div class="card-title">
                    Cutover Intelligence
                    </div>

                    <div class="card-subtitle">
                    Operational Exposure & Execution Coherence Intelligence
                    </div>
                    """,
                    unsafe_allow_html=True
                )

            with intro_col2:

                if st.button("✕", key="close_guidance"):

                    st.session_state.show_guidance = False
                    st.rerun()

            # ---------------------------------------------------
            # WHY ORGANIZATIONS USE THIS
            # ---------------------------------------------------

            st.markdown(
                """
                <div class="section-header">
                WHY ORGANIZATIONS USE CUTOVER INTELLIGENCE
                </div>

                <div class="section-body">

                Large transformations often fail because critical operational signals remain fragmented across spreadsheets, RAID logs, readiness reporting, escalation chains, governance layers, and operational discussions.

                <br><br>

                By the time leadership sees the full picture:

                <br><br>

                • rollback windows are shrinking<br>
                • dependencies are already unstable<br>
                • business readiness diverges from reporting<br>
                • escalation paths become overloaded<br>
                • operational exposure has already materially increased

                <br><br>

                Cutover Intelligence consolidates fragmented operational evidence into a single operational exposure assessment before failures escalate into outages, delays, governance breakdown, or transformation paralysis.

                </div>
                """,
                unsafe_allow_html=True
            )

            # ---------------------------------------------------
            # WHAT THIS PLATFORM DOES
            # ---------------------------------------------------

            st.markdown(
                """
                <div class="section-header">
                WHAT THIS PLATFORM DOES
                </div>

                <div class="section-body">

                This platform analyzes operational evidence from complex transformations and cutovers to surface recurring operational fragility, dependency instability, rollback uncertainty, escalation patterns, readiness inconsistencies, and execution coherence risks across fragmented operational artifacts.

                </div>
                """,
                unsafe_allow_html=True
            )

            # ---------------------------------------------------
            # WITHOUT THIS VISIBILITY
            # ---------------------------------------------------

            st.markdown(
                """
                <div class="section-header">
                WITHOUT THIS VISIBILITY
                </div>

                <div class="section-body">

                Organizations often detect serious transformation fragility too late.

                <br><br>

                Typical consequences include:

                <br><br>

                • failed go-lives<br>
                • delayed deployments<br>
                • rollback events<br>
                • operational disruption<br>
                • leadership blind spots<br>
                • governance escalation failures<br>
                • cross-stream coordination collapse<br>
                • expensive operational firefighting

                </div>
                """,
                unsafe_allow_html=True
            )

            # ---------------------------------------------------
            # SUPPORTED SCENARIOS
            # ---------------------------------------------------

            st.markdown(
                """
                <div class="section-header">
                SUPPORTED TRANSFORMATION SCENARIOS
                </div>

                <div class="section-body">

                • SAP cutovers<br>
                • ERP transformations<br>
                • cloud migration cutovers<br>
                • SaaS/platform migrations<br>
                • infrastructure transitions<br>
                • major operational release waves<br>
                • multi-stream transformation programs

                </div>
                """,
                unsafe_allow_html=True
            )

            # ---------------------------------------------------
            # INTENDED FOR
            # ---------------------------------------------------

            st.markdown(
                """
                <div class="section-header">
                INTENDED FOR
                </div>

                <div class="section-body">

                • transformation leadership<br>
                • PMO and governance teams<br>
                • SAP / ERP transformation programs<br>
                • cutover managers<br>
                • operational readiness teams<br>
                • enterprise migration leadership<br>
                • executive transformation oversight

                </div>
                """,
                unsafe_allow_html=True
            )

            # ---------------------------------------------------
            # EVIDENCE TYPES
            # ---------------------------------------------------

            st.markdown(
                """
                <div class="section-header">
                RECOMMENDED OPERATIONAL EVIDENCE
                </div>

                <div class="section-body">

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
                """,
                unsafe_allow_html=True
            )

            # ---------------------------------------------------
            # FILE TYPES
            # ---------------------------------------------------

            st.markdown(
                """
                <div class="section-header">
                SUPPORTED FILE TYPES
                </div>

                <div class="section-body">

                • XLSX / CSV<br>
                • DOCX / PPTX / PDF / TXT<br>
                • PNG / JPG / JPEG

                </div>
                """,
                unsafe_allow_html=True
            )

            # ---------------------------------------------------
            # PRIVACY
            # ---------------------------------------------------

            st.markdown(
                """
                <div class="section-header">
                PRIVACY & OPERATIONAL TRUST
                </div>

                <div class="section-body">

                Uploaded operational evidence is processed only for the active assessment session.

                <br><br>

                Operational data is not intentionally retained, sold, or used for external model training or secondary purposes.

                <br><br>

                Closing the browser or tab clears the active operational assessment session.

                <br><br>

                Please avoid uploading production credentials, personal employee data, or regulated customer information.

                </div>
                """,
                unsafe_allow_html=True
            )

            # ---------------------------------------------------
            # HOW TO USE
            # ---------------------------------------------------

            st.markdown(
                """
                <div class="section-header">
                HOW TO USE
                </div>

                <div class="section-body">

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
    # SCROLL CUE
    # ---------------------------------------------------

    st.markdown(
        """
        <div class="scroll-cue">

        ↓ Upload operational evidence to surface hidden transformation fragility, dependency exposure, and operational risk signals. No uploaded information is retained. Closing the browser or tab clears the active assessment session. ↓

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
    # RUN ANALYSIS
    # ---------------------------------------------------

    run_analysis = st.button(
        "Run Operational Exposure Assessment",
        type="primary"
    )

    # ---------------------------------------------------
    # EXECUTE ANALYSIS
    # ---------------------------------------------------

    if run_analysis:

        if not uploaded_files:

            st.error(
                "Please upload at least one operational evidence file."
            )

            return

        with st.spinner("Analyzing operational evidence..."):

            saved_files = []

            for uploaded_file in uploaded_files:

                saved_file = save_uploaded_file(uploaded_file)

                saved_files.append(saved_file)

            normalized_packets = normalize_evidence(saved_files)

            validated_signals = validate_signals(normalized_packets)

            exposure_results = calculate_exposure_score(
                validated_signals
            )

            exposure_summary = generate_exposure_summary(
                exposure_results
            )

        # ---------------------------------------------------
        # RESULTS
        # ---------------------------------------------------

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
Exposure Level:
{exposure_results.get('exposure_level', 'UNKNOWN')}

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