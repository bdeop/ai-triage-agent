from langgraph.graph import StateGraph, END
from typing import TypedDict
from agents.symptom_agent import SymptomAgent
from agents.triage_agent import TriageAgent
from agents.disposition_agent import DispositionAgent
from agents.clarifier_agent import SymptomClarifier

class TriageState(TypedDict):
    patient: dict
    symptom_description: str
    clarification_notes: str
    triage_reasoning: str
    care_recommendation: str

def build_triage_graph():
    symptom_agent = SymptomAgent()
    clarifier = SymptomClarifier()
    triage_agent = TriageAgent()
    disposition_agent = DispositionAgent()

    graph = StateGraph(state_schema=TriageState)
    graph.add_node("SymptomCollector", symptom_agent.run)
    graph.add_node("Clarifier", clarifier.run)
    graph.add_node("TriageClassifier", triage_agent.run)
    graph.add_node("DispositionPlanner", disposition_agent.run)

    graph.set_entry_point("SymptomCollector")
    graph.add_edge("SymptomCollector", "Clarifier")
    graph.add_edge("Clarifier", "TriageClassifier")
    graph.add_edge("TriageClassifier", "DispositionPlanner")
    graph.add_edge("DispositionPlanner", END)

    return graph.compile()
