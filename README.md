# 🚀 OmniOps-Swarm: Autonomous Multi-Domain SRE Orchestration Agent

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-009688.svg)](https://fastapi.tiangolo.com/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.25+-FF4B4B.svg)](https://streamlit.io/)
[![NVIDIA Nemotron](https://img.shields.io/badge/NVIDIA-Nemotron--3--70b-76B900.svg)](https://build.nvidia.com/)

**OmniOps-Swarm** is an autonomous, multi-domain Site Reliability Engineering (SRE) agent that ingests real-time production telemetry, researches live documentation and advisories, and automatically generates production-ready remediation patches across application code, SQL database migrations, and Terraform infrastructure configurations in seconds.

---

## 📌 Architecture & Features

Traditional SRE tools alert engineers when an issue occurs, but leave cross-domain debugging and code generation to humans. **OmniOps-Swarm** automates the entire incident lifecycle:

1. **Telemetry Ingestion (`FastAPI` & `watchtower`):** Ingests real-time error payloads, stack traces, and system failure metrics via webhooks or dashboard triggers.
2. **Autonomous AI Brain (`brain`):** Connects to **NVIDIA Nemotron** via the official **Nebius Token Factory SDK** (`https://api.studio.nebius.ai/v1/`) to evaluate incident context and plan fixes.
3. **Real-time Web Research (`brain/researcher.py`):** Queries **Tavily Search** to fetch official documentation, live CVE advisories, and version deprecation guidelines.
4. **Multi-Domain Patch Generation (`executor`):** Simultaneously crafts coordinated, production-ready diffs across:
   * 🐍 **Application Code (`app/api.py`):** Fixes syntax bugs, memory leaks, and deprecations.
   * 🗄️ **Database Migrations (`migrations/`):** Generates non-blocking concurrent SQL index creation and query fixes.
   * 🏗️ **Infrastructure-as-Code (`infra/`):** Produces Terraform specs and Kubernetes autoscaling configurations.
5. **Isolated Sandbox Verification (`sandbox`):** Staging layer that validates patch syntax and verifies safety before deployment execution.
6. **Enterprise Resilience:** Features an automated fallback boundary to guarantee continuous uptime and telemetry testing under billing, network, or external API limits.

---

## ⚡ Offline Simulation & Resiliency Mode

To guarantee continuous uptime during evaluation and account for external API rate limits or authentication availability (such as Nebius platform billing verifications), **OmniOps-Swarm** includes a built-in **Simulation Mode**:

* **Live SDK First:** The codebase leverages production-grade `openai` client connections pointing to the live Nebius Token Factory endpoint (`https://api.studio.nebius.ai/v1/`).
* **Graceful Fallback:** If an external API key is missing or encounters a `401 Unauthorized` / billing boundary, the system gracefully degrades to a deterministic simulation engine.
* **Seamless Testing:** This allows judges and reviewers to test the entire end-to-end multi-domain patch workflow (UI, telemetry ingestion, diff generation, and sandbox staging) locally without requiring live API keys.
---

## 🛠️ Project Structure

```text
OmniOps-Swarm/
├── app/
│   └── api.py                  # Core application logic & data models
├── brain/
│   ├── nemotron_engine.py       # NVIDIA Nemotron LLM integration & fallback layer
│   └── researcher.py            # Tavily Search API research runner
├── executor/
│   └── writer.py                # Multi-domain patch generator (Code, SQL, Terraform)
├── infra/
│   └── k8s_cluster.tf           # Terraform infrastructure specifications
├── migrations/
│   └── index_optimization.sql  # Database migration scripts
├── sandbox/
│   └── runner.py                # Isolated patch validation runner
├── watchtower/
│   ├── ingest.py                # Telemetry ingestion engine
│   └── webhook.py               # Alert webhook listener
├── app_ui.py                    # Streamlit operator dashboard
├── main.py                      # FastAPI backend server
├── requirements.txt             # Python dependencies
└── README.md                    # Project documentation

Quick Start Guide
1. Clone the Repository & Install Dependencies

Bash-
(git clone [https://github.com/YOUR_USERNAME/OmniOps-Swarm.git](https://github.com/YOUR_USERNAME/OmniOps-Swarm.git)
cd OmniOps-Swarm
pip install -r requirements.txt)

2. Set Up Environment Variables
Create a .env file in the root directory:
Code Snippet
NEBIUS_API_KEY=your_nebius_api_key_here
TAVILY_API_KEY=your_tavily_api_key_here

3. Launch the Application
Start the FastAPI backend and Streamlit dashboard:

Terminal 1 (Backend API):
Bash-
python main.py

terminal 2 (Operator Dashboard):

Bash-
streamlit run app_ui.py

Open your browser to http://localhost:8501 to access the real-time OmniOps-Swarm SRE console.

Tech Stack
Language: Python 3.10+

AI Model: NVIDIA Nemotron-3-70b-Aero via Nebius Token Factory SDK

Research API: Tavily Web Search API

Backend Framework: FastAPI & Uvicorn

Frontend UI: Streamlit (Dark Mode Console)

DevOps / IaC: Terraform, Git Automation, Container Sandboxing