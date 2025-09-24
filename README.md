# SearchPro Research Agent 🤖

An AI-powered research assistant that generates comprehensive reports using a multi-agent system.

## Features

- 🔍 Multi-agent research system (Researcher, Analyst, Writer)
- 📊 Real-time progress tracking
- 💾 Automatic caching of research results
- 📝 Export reports in Markdown or Plain Text
- 🔄 Access to previous research history

## Prerequisites

- Python 3.8+
- Google API Key with Gemini API access
- Git

## Installation

1. Clone the repository:
```bash
git clone https://github.com/rxshoumoun/searchpro.git
cd searchpro
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
streamlit run main.py
```

## Usage

1. Enter your Google API key in the sidebar
2. Input your research topic
3. Click "Run Research"
4. Wait for all three phases to complete
5. Download your report in preferred format

## Project Structure

```
searchpro/
├── main.py           # Main application
├── agents.py         # AI agents implementation
├── database.py       # Database operations
├── documentation.py  # App documentation
├── styles.py         # UI styling
└── utils.py         # Helper functions
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first.

---
Made with ❤️ by **Rohan Jadhav**