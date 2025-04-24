from langchain_openai import ChatOpenAI

class TriageAgent:
    def __init__(self):
        self.llm = ChatOpenAI(model="gpt-4o", temperature=0.2)

    def run(self, state):
        description = state["symptom_description"]
        prompt = f"""
        You are a triage nurse. Read the patient complaint and determine urgency.

        Complaint: "{description}"

        Think step by step to determine the most appropriate triage level.
        Classify as one of:
        - EMERGENCY
        - URGENT
        - ROUTINE

        Return format:
        Reasoning: ...
        Urgency: ...
        """
        response = self.llm.predict(prompt)
        return {"triage_reasoning": response}
