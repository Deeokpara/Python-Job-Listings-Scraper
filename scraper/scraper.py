import pandas as pd
import requests
from bs4 import BeautifulSoup

url = "https://realpython.github.io/fake-jobs/"

response = requests.get(url)

soup = BeautifulSoup(response.text, "lxml")

jobs = soup.find_all("div", class_="card-content")

job_list = []

for job in jobs:
    title = job.find("h2").text.strip()
    company = job.find("h3").text.strip()
    location = job.find("p").text.strip()

    job_list.append({"title": title, "company": company, "location": location})

df = pd.DataFrame(job_list)

df.to_csv("data/jobs.csv", index=False)

print("Jobs scraped successfully!")
