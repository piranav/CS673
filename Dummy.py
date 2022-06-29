import pandas as pd

demo = pd.read_csv("Clean Data/Key demographics 2019.csv")
income = pd.read_csv("Clean Data/Key income 2019.csv")
income = income.drop(columns={"GEO_ID"})
job = pd.read_csv("Clean Data/Key job 2019.csv")
job = job.drop(columns={"GEO_ID"})

df_1 = pd.merge(demo,income, on = "tract")
df_2 = pd.merge(df_1, job, on ="tract")
df_2.to_csv("./Clean Data/2019_data.csv")