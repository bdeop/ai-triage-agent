import plotly.express as px
import pandas as pd

def plot_condition_timeline(conditions_df):
    df = conditions_df.copy()
    df["START"] = pd.to_datetime(df["START"], errors='coerce')
    df["STOP"] = pd.to_datetime(df["STOP"], errors='coerce')
    fig = px.timeline(df, x_start="START", x_end="STOP", y="DESCRIPTION", title="Patient Condition Timeline")
    fig.update_yaxes(autorange="reversed")
    return fig
