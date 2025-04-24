
from langgraph.graph import StateGraph, END
from agents.symptom_agent import SymptomAgent
from agents.triage_agent import TriageAgent
from agents.disposition_agent import DispositionAgent
from typing import TypedDict

# State schema defining how data flows through the graph
class TriageState(TypedDict):
    patient: dict
    symptom_description: str
    triage_reasoning: str
    care_recommendation: str

def build_triage_graph():
    symptom_agent = SymptomAgent()
    triage_agent = TriageAgent()
    disposition_agent = DispositionAgent()

    graph = StateGraph(state_schema=TriageState)

    # These names just identify the nodes — actual state keys come from return dicts
    graph.add_node("SymptomCollector", symptom_agent.run)
    graph.add_node("TriageClassifier", triage_agent.run)
    graph.add_node("DispositionPlanner", disposition_agent.run)

    graph.set_entry_point("SymptomCollector")
    graph.add_edge("SymptomCollector", "TriageClassifier")
    graph.add_edge("TriageClassifier", "DispositionPlanner")
    graph.add_edge("DispositionPlanner", END)

    return graph.compile()
