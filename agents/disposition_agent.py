from langchain_openai import ChatOpenAI

class DispositionAgent:
    def __init__(self):
        self.llm = ChatOpenAI(model="gpt-4o", temperature=0.2)

    def run(self, state):
        urgency = state["triage_reasoning"]
        description = state["symptom_description"]
        prompt = f"""
        Based on this triage level and description, suggest the next step.

        Triage: {urgency}
        Description: "{description}"

        Options: refer to ER, lab tests, outpatient visit, etc.
        """
        response = self.llm.predict(prompt)
        return {"care_recommendation": response}

