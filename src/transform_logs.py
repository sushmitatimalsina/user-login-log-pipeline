import pandas as pd

def transform_logs(df):
    print("transforming login forms....")

    summary = df.groupby("user_id").size().reset_index(name="login_counts")
    return summary
