from langchain_openai import ChatOpenAI

class SymptomClarifier:
    def __init__(self):
        self.llm = ChatOpenAI(model="gpt-4o", temperature=0.4)

    def run(self, state):
        description = state["symptom_description"]
        prompt = f"""
        You received this patient complaint: "{description}".
        Ask 1–2 clarifying questions a nurse might ask to better triage.
        Then simulate the patient's brief responses.
        Format:
        - Q: ...
        - A: ...
        """
        return {"clarification_notes": self.llm.predict(prompt)}
