from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate

class SymptomAgent:
    def __init__(self):
        self.llm = ChatOpenAI(model="gpt-4o", temperature=0.3)

    def run(self, state):
        # Assumes state has "patient"
        patient = state["patient"]
        prompt = PromptTemplate.from_template("""
        Simulate a patient describing symptoms in natural language.

        Patient Info:
        Name: {name}
        Age: {age}
        Gender: {gender}
        Known Conditions: {symptoms}

        Return a realistic complaint as a single paragraph.
        """)
        response = self.llm.predict(prompt.format(**patient))
        return {"symptom_description": response}
