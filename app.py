import streamlit as st

st.set_page_config(
    page_title="Placement Readiness Dashboard",
    layout="wide"
)

st.title("Placement Readiness Dashboard")

st.markdown(
    """
    This dashboard helps evaluate placement readiness
    using machine learning and skill analysis.

    Use the sidebar to navigate between pages.
    """
)

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Modules",
        "3"
    )

with col2:
    st.metric(
        "Model",
        "Random Forest"
    )

with col3:
    st.metric(
        "Prediction",
        "Placement"
    )

st.divider()

st.subheader("Project Features")

st.write(
    """
    - Placement Prediction
    - Readiness Score
    - Skill Recommendations
    - Analytics Dashboard
    - Student Insights
    """
)