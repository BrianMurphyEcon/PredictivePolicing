import pandas as pd
import numpy as np
import os

df = pd.read_csv(r"C:\Users\bmmur\UH-ECON Dropbox\Brian Murphy\Predictive Policing Team\Data\2017\for_python.csv")
df.head()

columns = ['State', 'Agency Type', 'Agency Name', 'Population1']
df[['State', 'Agency Type']] = df[['State', 'Agency Type']].fillna(method='ffill')

df = df[columns]

df = df.dropna(subset = 'Population1')

df['Population1'] = df['Population1'].astype(str)
df['Population1'] = df['Population1'].str.replace(',', '').astype(int)

df = df[(df['Population1'] >= 10000) & (df['Population1'] < 50000)]

people = ['Hallie', 'Zane', 'Khushi', 'David']

df['Person Assigned'] = np.random.choice(people, size=len(df))
df['Person Assigned'] = [people[i % len(people)] for i in range(len(df))]

df['Use Pred Pol'] = np.nan
df['Start Date'] = np.nan
df['End Date'] = np.nan
df['Size of Police Force'] = np.nan

df.info()

df.to_csv(r"C:\Users\bmmur\UH-ECON Dropbox\Brian Murphy\Predictive Policing Team\Data\2017\from_pythonv2.csv")
