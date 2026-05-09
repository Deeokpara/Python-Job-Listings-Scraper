from sqlalchemy import create_engine
import pandas as pd

df = pd.read_csv("data/jobs_cleaned.csv")

engine = create_engine("sqlite:///jobs.db")

df.to_sql("jobs", engine, if_exists="replace", index=False)

print("Database created successfully!")