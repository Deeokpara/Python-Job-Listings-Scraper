import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/jobs_cleaned.csv")

st.title("Python Job Listings Dashboard")

st.write("Dataset Preview")
st.dataframe(df)

st.subheader("Top Job Locations")

location_counts = df["location"].value_counts().head(10)

fig, ax = plt.subplots()

location_counts.plot(kind="bar", ax=ax)

st.pyplot(fig)