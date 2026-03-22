from extract_logs import extract_logs
from transform_logs import transform_logs
from load_logs import load_logs


def run_pipeline():
    print("Starting Login Data Pipeline...")

    df = extract_logs()
    transformed_df = transform_logs(df)
    load_logs(transformed_df)

    print("Pipeline completed successfully!")


if __name__ == "__main__":
    run_pipeline()