import pandas as pd

df = pd.read_csv("data/jobs.csv")

# Remove duplicates
df = df.drop_duplicates()

# Remove missing values
df = df.dropna()

# Standardize text
df["title"] = df["title"].str.title()
df["company"] = df["company"].str.title()
df["location"] = df["location"].str.title()

df.to_csv("data/jobs_cleaned.csv", index=False)

print("Data cleaned successfully!")