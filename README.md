# AI Triage Agent for Simulated Hospital Intake

This project simulates a hospital triage process using an AI agent powered by GPT-4o. The system converses with synthetic patients from the Synthea dataset, classifies urgency, and recommends the next steps for care.

---

## Features

- Collects symptom descriptions using LLM
- Classifies triage urgency using chain-of-thought reasoning
- Suggests clinical actions (ER, labs, or primary care)
- Modular LangGraph-based multi-agent orchestration
- Streamlit UI for easy interaction

---

## Project Structure

```
ai_triage_agent/
├── data/                   # Place patients.csv and conditions.csv from Synthea
├── diag/                   # Diagrams (Flow and sequence) in platuml format
├── agents/                 # Modular agents (symptom, clarifier, triage, disposition)
├── utils.py                # Data loading utilities
├── orchestrator.py         # LangGraph agent workflow
├── app.py                  # Streamlit app entry point
├── requirements.txt        # Python dependencies
```

---

## Step-by-Step Local Setup

### Step 1: Clone or unzip the project

```bash
unzip ai_triage_agent.zip
cd ai_triage_agent
```

### Step 2: Add Synthetic Data

Place the following files from Synthea into the `data/` directory:
- `patients.csv`
- `conditions.csv`
- `observations.csv`

You can download them from https://synthea.mitre.org/downloads

Download this dataset:
https://synthetichealth.github.io/synthea-sample-data/downloads/latest/synthea_sample_data_csv_latest.zip
---

### Step 3: Create Virtual Environment and Install Requirements

```bash
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

---

### Step 4: Set OpenAI API Key

Set your OpenAI key as an environment variable or in a `.env` file.

```bash
export OPENAI_API_KEY=sk-xxxxxxxxxx
```

Or in `.env` (optional):
```
OPENAI_API_KEY=sk-xxxxxxxxxx
```

---

### Step 5: Run the Streamlit App

```bash
./venv/bin/python -m streamlit run app.py
```

Enter a valid patient ID from the dataset to simulate a triage process.

---

## Example Use

Patient ID: `6ce0bda7-716f-c904-cdc8-39076db16016`

You can find all patient IDs in data/patients.csv file.

Expected Output:
- Symptom: "I feel chest tightness and shortness of breath."
- Triage: EMERGENCY
- Recommendation: Refer to ER immediately.

---

## Powered By

- [LangGraph](https://github.com/langchain-ai/langgraph)
- [OpenAI GPT-4o](https://platform.openai.com/)
- [Synthea](https://synthetichealth.github.io/synthea/)
