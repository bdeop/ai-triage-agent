import pandas as pd

def load_patient_case(patient_id):
    patients = pd.read_csv("data/patients.csv")
    conditions = pd.read_csv("data/conditions.csv")

    patient = patients[patients["Id"] == patient_id].iloc[0]
    patient_conditions = conditions[conditions["PATIENT"] == patient_id]

    symptoms = [f"{row['DESCRIPTION']}" for _, row in patient_conditions.iterrows()]

    return {
        "id": patient_id,
        "name": f"{patient['FIRST']} {patient['LAST']}",
        "age": patient['BIRTHDATE'],
        "gender": patient['GENDER'],
        "symptoms": symptoms
    }
