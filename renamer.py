import pandas as pd
import random

df = pd.read_excel(r"C:\Users\bmmur\UH-ECON Dropbox\Brian Murphy\RA-TA\Predictive Policing Team\Data\temp\renamer.xlsx")

# Replace 'Khushi' with a random choice
df['Person Assigned'] = df['Person Assigned'].apply(
    lambda x: random.choice(['Hallie', 'Zane', 'David']) if x == 'Khushi' else x
)

# Save back to Excel
df.to_excel(r"C:\Users\bmmur\UH-ECON Dropbox\Brian Murphy\RA-TA\Predictive Policing Team\Data\temp\renamer2.xlsx", index=False)
