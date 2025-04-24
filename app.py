import streamlit as st
from orchestrator import build_triage_graph
from utils import load_patient_case
from visualization import plot_condition_timeline, format_vitals

st.set_page_config(page_title="AI Triage Agent", layout="wide")
st.title("🏥 AI Triage Agent for Hospital Intakes")

pid = st.text_input("Enter Patient ID")

if st.button("Run Triage") and pid:
    case = load_patient_case(pid)
    graph = build_triage_graph()
    result = graph.invoke({"patient": case})

    st.subheader("🗣️ Symptom Description")
    st.write(result["symptom_description"])

    st.subheader("❓ Clarification Dialogue")
    st.write(result["clarification_notes"])

    st.subheader("⚠️ Triage Reasoning")
    st.write(result["triage_reasoning"])

    st.subheader("🩺 Recommendation")
    st.write(result["care_recommendation"])

    st.subheader("📊 Vitals Summary")
    vital_df = format_vitals(case["vital_rows"])
    st.dataframe(vital_df, use_container_width=True)

    st.subheader("📅 Patient History Timeline")
    fig = plot_condition_timeline(case["conditions_df"])
    st.plotly_chart(fig, use_container_width=True)
