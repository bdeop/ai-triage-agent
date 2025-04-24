import plotly.express as px
import pandas as pd

def plot_condition_timeline(conditions_df):
    df = conditions_df.copy()
    df["START"] = pd.to_datetime(df["START"], errors='coerce')
    df["STOP"] = pd.to_datetime(df["STOP"], errors='coerce')
    df = df.sort_values("START", ascending=False).head(15)
    df["CATEGORY"] = df.get("CATEGORY", "Unknown")

    fig = px.timeline(
        df,
        x_start="START", x_end="STOP", y="DESCRIPTION",
        color="CATEGORY",
        hover_data=["CODE", "START", "STOP"],
        title="🩺 Patient Condition Timeline"
    )
    fig.update_yaxes(autorange="reversed")
    fig.update_layout(height=500, margin=dict(l=0, r=0, t=30, b=0))
    return fig

def format_vitals(vital_rows):
    data = []
    for row in vital_rows:
        data.append({
            "Measurement": row["DESCRIPTION"],
            "Value": f"{row['VALUE']} {row['UNITS']}",
            "Date": row.get("DATE", "N/A")
        })
    return pd.DataFrame(data)
