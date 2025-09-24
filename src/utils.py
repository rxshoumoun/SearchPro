import re
from typing import Dict, Any
import streamlit as st

def format_to_plaintext(markdown_text: str) -> str:
    """Processes and parses markdown text to remove formatting."""
    # Remove headings
    text = re.sub(r'#+\s', '', markdown_text)
    # Remove horizontal rules
    text = re.sub(r'\n---\n', '\n', text)
    # Remove bold and italics
    text = re.sub(r'\*\*(.*?)\*\*|__(.*?)__', r'\1\2', text)
    text = re.sub(r'\*(.*?)\*|_(.*?)_', r'\1\2', text)
    # Remove list items
    text = re.sub(r'^\s*[\*\-\+]\s+', '', text, flags=re.MULTILINE)
    text = re.sub(r'^\s*\d+\.\s+', '', text, flags=re.MULTILINE)
    # Remove blockquotes and code blocks
    text = re.sub(r'^>\s*', '', text, flags=re.MULTILINE)
    text = re.sub(r'```.*?```', '', text, flags=re.DOTALL)
    text = re.sub(r'`(.*?)`', r'\1', text)
    # Clean up extra newlines
    text = re.sub(r'\n{3,}', '\n\n', text)
    return text.strip()

def process_research_callback(state: Dict[str, Any], spinners: Dict[str, Any]) -> None:
    """Handle research process callbacks and update UI."""
    current_agent = state.get("current_agent", "")
    
    if current_agent == "researcher":
        with spinners["research"]:
            st.info("🔍 Research Specialist is gathering information...")
            if state.get("findings", {}).get("research"):
                st.success("✅ Research phase completed")
    
    elif current_agent == "analyst":
        with spinners["research"]:
            st.success("✅ Research phase completed")
        with spinners["analysis"]:
            st.info("📊 Data Analyst is processing information...")
            if state.get("findings", {}).get("analysis"):
                st.success("✅ Analysis phase completed")
    
    elif current_agent == "writer":
        with spinners["research"]:
            st.success("✅ Research phase completed")
        with spinners["analysis"]:
            st.success("✅ Analysis phase completed")
        with spinners["writing"]:
            st.info("📝 Report Writer is composing the final document...")
            if state.get("final_report"):
                st.success("✅ Writing phase completed")