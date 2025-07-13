"""
Description: This code cleans the data by extracting dates and features specific to the data collected.

Output: 'df' -> a cleaned dataframe that will be transformed into a Stata .dta file.

Written by: Brian Murphy
"""

# %%
import numpy as np
import pandas as pd
import re
#import logging

#logging.basicConfig(level=logging.INFO)
#logger = logging.getLogger(__name__)


# %% 
def clean_data(df):

    df = df.loc[:, ~df.columns.str.lower().str.startswith("unnamed")]

    df.columns = [
        col.strip().lower()
        .replace(" ", "_")
        .replace("(", "")
        .replace(")", "")
        .replace("/", "_")
        .replace("-", "_")
        if isinstance(col, str) else ""
        for col in df.columns
    ]
    df = df.loc[:, df.columns != ""]


# %% 
    for col in df.select_dtypes(include='object').columns:
        df[col] = df[col].astype(str).str.encode('ascii', errors='replace').str.decode('ascii')

    def extract_dates(text):
        if pd.isna(text):
            return []
        return re.findall(r'\d{1,2}/\d{1,2}/\d{2,4}', str(text))

    def parse_date(date_str):
        try:
            return pd.to_datetime(date_str, errors='coerce', dayfirst=False)
        except:
            return pd.NaT
# %% 
    df['contact_dates'] = df.get('dates_contacted', '').apply(extract_dates)
    df['contact_dates'] = df['contact_dates'].apply(lambda dates: sorted([parse_date(d) for d in dates if parse_date(d) is not pd.NaT]))

    df['heard_back_dates'] = df.get('hear_back_date', '').apply(extract_dates)
    df['heard_back_dates'] = df['heard_back_dates'].apply(lambda dates: sorted([parse_date(d) for d in dates if parse_date(d) is not pd.NaT]))
# %% 
    # Create individual contacted and response columns
    for i in range(3):
        df[f'date_contacted{i+1}'] = df['contact_dates'].apply(lambda x: x[i] if len(x) > i else pd.NaT)

    for i in range(3):
        contact_col = f'date_contacted{i+1}'
        next_contact_col = f'date_contacted{i+2}'
        response_col = f'heard_back{i+1}'

        df[response_col] = df.apply(
            lambda row: (
                row['heard_back_dates'][0]
                if (
                    len(row['heard_back_dates']) > 0 and
                    row[contact_col] and
                    row['heard_back_dates'][0] >= row[contact_col] and
                    (
                        (i == 2) or
                        (row[next_contact_col] is pd.NaT or row['heard_back_dates'][0] < row[next_contact_col])
                    )
                )
                else pd.NaT
            ),
            axis=1
        )

        df[f'response_days{i+1}'] = (df[response_col] - df[contact_col]).dt.days
# %% 
    # Add No_Email, No_Phone, No_Contact, Submitted_FOIA flags
    df['no_email'] = df.get('contact_methods', '').str.contains(r'\bno\s*email\b', case=False, na=True)
    df['no_phone'] = df.get('contact_methods', '').str.contains(r'\bno\s*(call|phone)\b', case=False, na=True)
    df['submitted_foia'] = (
        df.get('contact_methods', '').str.contains(r'\bfoia\b', case=False, na=True) |
        df.get('dates_contacted', '').str.contains(r'\bfoia\b', case=False, na=True)
    )

# %% 
    df['no_contact'] = df.get('contact_methods', '').isna() | (df['contact_methods'].str.strip() == "")

    # Count number of attempts before first response
    def attempts_before_response(row):
        if len(row['heard_back_dates']) == 0:
            return None
        first_response = row['heard_back_dates'][0]
        count = 0
        for date in row['contact_dates']:
            if date < first_response:
                count += 1
            else:
                break
        return count + 1 if count < len(row['contact_dates']) else count

    df['attempts_before_response'] = df.apply(attempts_before_response, axis=1)

    def never_heard_back(row):
        if len(row['contact_dates']) > 0 and len(row['heard_back_dates']) == 0:
            return True
        return False

    df['never_heard_back'] = df.apply(never_heard_back, axis=1)

    return df

