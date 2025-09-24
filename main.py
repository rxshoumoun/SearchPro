import streamlit as st
import os
from agents import run_research_team
from database import Database
from documentation import show_documentation
from utils import format_to_plaintext, process_research_callback
from styles import PAGE_CONFIG, apply_custom_styling, create_footer

# Initialize database
db = Database()

# Configure page
st.set_page_config(**PAGE_CONFIG)
apply_custom_styling()

# Create tabs for navigation
tab1, tab2 = st.tabs(["🔍 Research", "📚 Documentation"])

with tab1:
    # Sidebar for API key and history
    with st.sidebar:
        st.subheader("API Configuration")
        api_key = st.text_input("Enter Google API Key", type="password")
        
        st.markdown("---")
        st.header("Previous Reports")
        recent_research = db.get_recent_research()
        
        if recent_research:
            for i, entry in enumerate(recent_research):
                if st.button(f"📄 {entry['topic']}", key=f"history_{i}"):
                    if "current_report" in st.session_state:
                        del st.session_state["current_report"]
                    st.session_state["selected_report"] = entry
                    st.rerun()

    # Main research interface
    st.title("🤖 SearchPro Research Agent")
    st.write("Enter a research topic and let the AI research team generate a detailed report for you.")

    topic = st.text_input("Enter research topic", "")
    col1, col2 = st.columns(2)
    
    with col1:
        research_button = st.button("Run Research")
    with col2:
        clear_button = st.button("🗑️ Clear Previous Output")

    # Handle button actions and display reports
    if clear_button:
        if "current_report" in st.session_state:
            del st.session_state["current_report"]
        if "selected_report" in st.session_state:
            del st.session_state["selected_report"]
        st.rerun()

    if research_button and topic.strip():
        if not api_key:
            st.error("Please enter your Google API key in the sidebar first.")
        else:
            os.environ["GOOGLE_API_KEY"] = api_key
            
            # Initialize progress tracking
            spinners = {
                "research": st.empty(),
                "analysis": st.empty(),
                "writing": st.empty()
            }
            
            with st.spinner("Research in progress..."):
                try:
                    result = run_research_team(
                        topic, 
                        lambda state: process_research_callback(state, spinners)
                    )
                    
                    if result and result.get("final_report"):
                        st.success("✨ Research completed successfully!")
                        db.cache_research(topic, result["final_report"])
                        st.session_state["current_report"] = {
                            "topic": topic,
                            "report": result["final_report"],
                            "date": "Just now"
                        }
                except Exception as e:
                    st.error(f"An error occurred: {str(e)}")

    # Display reports
    report_container = st.container()
    with report_container:
        if "current_report" in st.session_state:
            entry = st.session_state["current_report"]
            st.subheader("Current Research Report")
            st.markdown(f"**Topic:** {entry['topic']}")
            st.markdown(entry['report'])
            
            # Download buttons
            col1, col2 = st.columns(2)
            with col1:
                st.download_button(
                    label="Download as Markdown",
                    data=entry["report"],
                    file_name=f"{entry['topic'].replace(' ', '_')}_report.md",
                    mime="text/markdown"
                )
            with col2:
                plain_text = format_to_plaintext(entry["report"])
                st.download_button(
                    label="Download as Plain Text",
                    data=plain_text,
                    file_name=f"{entry['topic'].replace(' ', '_')}_report.txt",
                    mime="text/plain"
                )
        
        # Show selected report from history if available
        elif "selected_report" in st.session_state:
            entry = st.session_state["selected_report"]
            st.subheader("Selected Report from History")
            st.markdown(f"**Topic:** {entry['topic']}")
            st.markdown(f"**Date:** {entry['date']}")
            st.markdown(entry['report'])
            
            # Download buttons
            col1, col2 = st.columns(2)
            with col1:
                st.download_button(
                    label="Download MD",
                    data=entry["report"],
                    file_name=f"{entry['topic'].replace(' ', '_')}_report.md",
                    mime="text/markdown",
                    key=f"selected_md"
                )
            with col2:
                plain_text = format_to_plaintext(entry["report"])
                st.download_button(
                    label="Download TXT",
                    data=plain_text,
                    file_name=f"{entry['topic'].replace(' ', '_')}_report.txt",
                    mime="text/plain",
                    key=f"selected_txt"
                )

with tab2:
    show_documentation()

create_footer()