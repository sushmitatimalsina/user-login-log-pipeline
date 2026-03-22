import pandas as pd 

def extract_logs():
    print("Extracting logs...")

    file_path ="user_login_log_pipeline/data/raw/login_logs.csv"
    df = pd.read_csv(file_path)
    return df