
def load_logs(df):
    print("saving processed data...")
    output_path = "user_login_log_pipeline/data/processed/login_summary.csv"
    df.to_csv(output_path,index=False)

    print(f"Processed data saved to {output_path}")