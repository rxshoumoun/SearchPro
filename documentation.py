import streamlit as st

def show_documentation():
    st.title("📚 SearchPro Documentation")
    
    st.header("Getting Started")
    st.markdown("""
    1. **API Key Setup**
        - Get your Google API key from [Google Cloud Console](https://console.cloud.google.com/)
        - Enable the Gemini API for your project
        - Enter the API key in the sidebar configuration
    
    2. **Running a Research Query**
        - Enter your research topic in the input field
        - Click "Run Research" to start the process
        - Watch as the AI team works through three phases:
            * 🔍 Research Phase
            * 📊 Analysis Phase
            * 📝 Writing Phase
    
    3. **Viewing Results**
        - The final report will appear below the research area
        - Download options:
            * Markdown format (.md)
            * Plain text format (.txt)
    
    4. **Managing Reports**
        - Access previous reports from the sidebar
        - Clear output using the "Clear Previous Output" button
        - Each report is automatically saved for future reference
    """)
    
    st.header("Features")
    st.markdown("""
    - **Multi-Agent Research System**
        * Research Specialist
        * Data Analyst
        * Report Writer
    
    - **Automatic Caching**
        * All research results are cached
        * Quick access to previous reports
    
    - **Export Options**
        * Markdown format with formatting
        * Plain text format without formatting
    
    - **Progress Tracking**
        * Real-time progress indicators
        * Phase completion notifications
    """)
    
    st.header("Troubleshooting")
    st.markdown("""
    **Common Issues:**
    
    1. **API Key Error**
        - Ensure your API key is valid
        - Check if the Gemini API is enabled
        - Verify your project has billing enabled
    
    2. **No Results**
        - Try rephrasing your research topic
        - Ensure your topic is specific enough
        - Check your internet connection
    
    3. **Slow Response**
        - Complex topics may take longer to process
        - Multiple agents work sequentially
        - Wait for all phases to complete
    """)
    
    st.header("Contact & Support")
    st.markdown("""
    - Report issues on GitHub
    - Contact: chunghavati@gmail.com
    - Version: 1.0.0
    """)