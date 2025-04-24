import streamlit as st
from orchestrator import build_triage_graph
from utils import load_patient_case

st.title("🏥 AI Triage Agent")

pid = st.text_input("Enter Patient ID to Simulate Intake")
if st.button("Run Triage") and pid:
    patient = load_patient_case(pid)  # returns patient dictionary
    graph = build_triage_graph()

    result = graph.invoke({"patient": patient})

    # Use state keys, not node names
    st.subheader("🗣️ Symptom Description")
    st.write(result["symptom_description"])

    st.subheader("⚠️ Triage Classification")
    st.write(result["triage_reasoning"])

    st.subheader("🩺 Recommended Action")
    st.write(result["care_recommendation"])
