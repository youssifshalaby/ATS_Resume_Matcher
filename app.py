import os
os.environ["STREAMLIT_SERVER_FILE_WATCHER_TYPE"] = "none"

import streamlit as st
from utils.pdf_loader import extract_text_from_pdf
from utils.score_engine import analyze_resume

# -----------------------------
# Page Configuration
# -----------------------------
st.image(
    "assets/banner2.png",
    width="stretch"
)
st.set_page_config(
    page_title="AI Resume Matcher",
    page_icon="📄",
    layout="wide"
)


st.title("📄 AI Resume Matcher")
st.write("Upload a Resume and compare it with a Job Description.")

with st.sidebar:

    st.image(
        "assets/cv.png"
    )

    st.title(
        "ATS Matcher"
    )

    st.write(
        """
        ✅ PDF Upload

        ✅ Semantic Matching

        ✅ Skill Extraction

        ✅ Missing Skills

        ✅ ATS Score
        """
    )
    st.divider()
    st.info("Built with Python, Streamlit, spaCy and Sentence Transformers.")

# -----------------------------
# User Inputs
# -----------------------------
resume_file = st.file_uploader(
    "Upload Resume (PDF)",
    type=["pdf"]
)

job_description = st.text_area(
    "Paste Job Description",
    height=250
)

col1, col2 = st.columns(2)

analyze = col1.button(
    "🚀 Analyze Resume",
    use_container_width=True
)

reset = col2.button(
    "🔄 Reset",
    use_container_width=True
)

# -----------------------------
# Analyze Button
# -----------------------------
if reset:
    st.rerun()

if analyze:

    if resume_file is None:
        st.warning("Please upload a resume.")
        st.stop()

    if not job_description.strip():
        st.warning("Please enter a job description.")
        st.stop()

    # Extract Resume Text
    try:
        resume_text = extract_text_from_pdf(resume_file)
    except Exception as e:
        st.error(f"Error extracting PDF: {e}")
        st.stop()
    # ---------------------------------
    with st.spinner("Analyzing resume using NLP model..."):

        result = analyze_resume(
            resume_text,
            job_description
        )


    st.success("Analysis Completed ✅")
    # Progress Bars
    st.divider()
    st.subheader("📊 Match Scores")

    col1, col2, col3 = st.columns(3)


    with col1:

        st.metric(
            label="🎯 Overall ATS Score",
            value=f"{result['final_score']}%"
        )

        st.progress(
            result["final_score"] / 100
        )



    with col2:

        st.metric(
            label="🧠 Semantic Similarity",
            value=f"{result['semantic_score']}%"
        )

        st.progress(
            result["semantic_score"] / 100
        )



    with col3:

        st.metric(
            label="🛠️ Skill Matching",
            value=f"{result['skill_score']}%"
        )

        st.progress(
            result["skill_score"] / 100
        )
    st.divider()
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Resume Skills")

        if result["resume_skills"]:
            st.write(result["resume_skills"])
        else:
            st.info("No skills found.")

    with col2:
        st.subheader("Job Skills")

        if result["job_skills"]:
            st.write(result["job_skills"])
        else:
            st.info("No skills found.")

    st.divider()

    col3, col4 = st.columns(2)

    with col3:
        st.subheader("✅ Matched Skills")

        if result["matched_skills"]:
            for skill in result["matched_skills"]:
                st.success(skill)
        else:
            st.warning("No matched skills.")

    with col4:
        st.subheader("❌ Missing Skills")

        if result["missing_skills"]:
            for skill in result["missing_skills"]:
                st.error(skill)
        else:
            st.success("No missing skills 🎉")
    
    st.divider()

    st.subheader("Recommendations 💡")


    for rec in result["recommendations"]:

        st.info(rec)
    
    st.divider()
    st.subheader("Resume Analysis 📄")


    analysis = result["resume_analysis"]


    col1, col2 = st.columns(2)


    with col1:

        st.metric(
            "Word Count",
            analysis["word_count"]
        )


    with col2:

        st.metric(
            "Characters",
            analysis["character_count"]
        )



    st.write("Detected Sections:")


    for section in analysis["sections"]:

        st.success(
            f"✓ {section}"
        )

    st.divider()

    st.caption(
        "© 2026 Youssef Shalaby | AI Resume Matcher | NLP Project"
    )