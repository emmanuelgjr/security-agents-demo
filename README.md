# Security Agents Demo with CrewAI

This repo demonstrates a simple security automation flow using 3 collaborative agents built with [CrewAI](https://github.com/joaomdmoura/crewAI):

- **Phishing Detector Agent**: Scans emails for signs of phishing.
- **Threat Intelligence Agent**: Enriches suspected phishing emails with basic threat context.
- **Auto-Response Agent**: Suggests or generates a response (block/report).

## How it works

You provide sample emails. The agents work together to analyze and automate triage.

## Setup

```bash
# Clone and enter the repo
git clone https://github.com/yourname/security-agents-demo.git
cd security-agents-demo

# (Optional) Create virtual env
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install requirements
pip install -r requirements.txt

# Run the demo
python main.py
