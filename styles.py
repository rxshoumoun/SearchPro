import streamlit as st

# Page Configuration
PAGE_CONFIG = {
    "page_title": "SearchPro",
    "page_icon": "🤖",
    "layout": "wide",
    "initial_sidebar_state": "expanded"
}

# CSS Styles
CUSTOM_CSS = """
<style>
    .stButton button {
        width: 100%;
    }
    .research-phase {
        margin-bottom: 1rem;
    }
    .report-container {
        margin-top: 2rem;
        padding: 1rem;
        border-radius: 0.5rem;
    }
</style>
"""

def apply_custom_styling():
    """Apply custom styling to the Streamlit app."""
    st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

def create_footer():
    """Create centered footer with attribution."""
    st.markdown("---")
    with st.container():
        col1, col2, col3 = st.columns(3)
        with col2:
            st.markdown(
                "<div style='text-align: center'>Made with ❤️ by Rxshomoun</div>", 
                unsafe_allow_html=True
            )