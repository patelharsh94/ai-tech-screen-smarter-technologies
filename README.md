# Thoughtful AI - Smarter Technologies

## Overview
This project is a submission for the **Staff Software Engineer, AI** position at Smarter Technologies.

## About
This repository demonstrates AI and software engineering expertise, showcasing practical implementations and technical depth required for the role.

## Candidate Information
- **Website**: [patelharsh.com](https://patelharsh.com)
- **Position**: Staff Software Engineer, AI
- **Company**: Smarter Technologies

## Contents
- Implementation details
- Technical documentation
- Code examples and workflows

## Requirements
- Python 3.8+
- OpenAI API Key
- Dependencies listed in `requirements.txt`

## Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/patelharsh94/ai-tech-screen-smarter-technologies.git
cd ai-tech-screen-smarter-technologies
```

### 2. Create a Virtual Environment
```bash
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

### 3. Install Requirements
```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables
Create a `.env.local` file in the project root with your OpenAI API key:
```bash
OPENAI_API_KEY=sk_your_api_key_here
```

Or export it in your shell:
```bash
export OPENAI_API_KEY=sk_your_api_key_here
```

### 5. Run the Application
```bash
chainlit run app.py -w
```

The app will open at `http://localhost:8000` with hot-reload enabled (`-w` flag).

## Features
- 🎨 **Chainlit's Beautiful UI** - Modern, responsive chat interface for communicating with Thoughtful AI GPT
- ✅ **Smart Responses** - Answers default questions about Thoughtful AI services (EVA, CAM, PHIL)
- 🛡️ **Safe Handling** - Responds respectfully to malicious or out-of-scope questions  
- 🤷 **Graceful Unknowns** - Admits when it doesn't know something
- 🎯 **Guided Conversations** - Steers irrelevant questions back to Thoughtful AI services
- ⚡ **Real-time Streaming** - Responses stream in real-time for better UX

## Project Structure
```
├── app.py                   # Main Chainlit application
├── chainlit.md              # Welcome/splash screen
├── .chainlit/
│   └── config.toml          # Chainlit configuration
├── requirements.txt         # Python dependencies
├── .env.local               # Environment variables (create this)
└── README.md                # This file
```

## Customization

### Change the AI Model
Edit `app.py` and modify the `settings` dictionary:
```python
settings = {
    "model": "gpt-4o-mini",  # Use gpt-4o, gpt-4-turbo, gpt-3.5-turbo, etc.
    "temperature": 0.7,
}
```

### Customize the Welcome Screen
Edit `chainlit.md` to customize the welcome/splash screen shown to users.

### Configure Chat Profile
Edit `.chainlit/config.toml` to customize:
- Assistant name
- Avatar/icon
- Theme (dark/light)
- Chat input placeholder
- And more

## Troubleshooting

### `OPENAI_API_KEY not found` error
Make sure you've set your API key:
```bash
export OPENAI_API_KEY=sk_your_key
```
Or add it to `.env.local`

### Chainlit command not found
Make sure your virtual environment is activated:
```bash
source .venv/bin/activate
```

### Port 8000 already in use
Run on a different port:
```bash
chainlit run app.py -w
```

## Tech Stack
- **Frontend**: Chainlit UI
- **Backend**: Python with FastAPI (via Chainlit)
- **LLM**: OpenAI GPT-4o/GPT-4o-mini
- **Async**: Python AsyncIO for non-blocking I/O


## Contact & Links
- Portfolio: [patelharsh.com](https://patelharsh.com)
- Github: [Checkout My Cool Projects!](https://github.com/patelharsh94)
- Git Repo for this project: [Thoughtful AI](https://github.com/patelharsh94/ai-tech-screen-smarter-technologies)
- LinkedIn: [Connect with me on LinkedIn!](https://www.linkedin.com/in/harshpatel94)

---
*This is a submission for the Staff Software Engineer, AI position at Smarter Technologies.*