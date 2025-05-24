# Campus AI Assistance Platform

This repository contains a minimal skeleton for a campus assistance platform powered by AI tools. It includes a plugin framework, example plugins, and a small Flask app with placeholder templates.

## Quick Start

1. Create a virtual environment and install requirements:

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

2. Run the development server:

```bash
python app.py
```

The server exposes a simple chat UI at `http://localhost:5000`.

## Project Structure

- `campus_ai` – core library with the agent and plugin framework.
- `frontend` – minimal HTML templates for the chat interface and login page.
- `app.py` – Flask application wiring everything together.

This is only a starting point. Many features are unimplemented and left as TODOs.

