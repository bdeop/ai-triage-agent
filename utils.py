import pandas as pd


def load_patient_case(patient_id):
    patients = pd.read_csv("data/patients.csv")
    conditions = pd.read_csv("data/conditions.csv")
    observations = pd.read_csv("data/observations.csv")

    patient = patients[patients["Id"] == patient_id].iloc[0]
    patient_conditions = conditions[conditions["PATIENT"] == patient_id]
    patient_obs = observations[observations["PATIENT"] == patient_id]

    # Extract relevant vitals (you can expand this as needed)
    vital_rows = patient_obs[patient_obs["DESCRIPTION"].isin([
        "Systolic Blood Pressure", "Diastolic Blood Pressure", "Body Temperature"
    ])].to_dict(orient="records")  # ← returns a list of dicts

    return {
        "id": patient_id,
        "name": f"{patient['FIRST']} {patient['LAST']}",
        "age": patient['BIRTHDATE'],
        "gender": patient['GENDER'],
        "symptoms": [row['DESCRIPTION'] for _, row in patient_conditions.iterrows()],
        "vital_rows": vital_rows,
        "conditions_df": patient_conditions
    }
