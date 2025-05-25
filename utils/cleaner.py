import numpy as np
import pandas as pd

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

    for col in df.select_dtypes(include='object').columns:
        df[col] = df[col].astype(str).str.encode('ascii', errors='replace').str.decode('ascii')

    if 'dates_contacted' in df.columns and 'contact_methods' in df.columns:
        def split_contact_info(row):
            dates_raw = str(row['dates_contacted']).replace('\n', ';')
            methods_raw = str(row['contact_methods']).replace('\n', ';')

            date_parts = [d.strip() for d in dates_raw.split(';') if d.strip()]
            method_parts = [m.strip() for m in methods_raw.split(';') if m.strip()]

            max_len = max(len(date_parts), len(method_parts))
            date_parts += [np.nan] * (max_len - len(date_parts))
            method_parts += [np.nan] * (max_len - len(method_parts))

            return pd.Series([val for pair in zip(date_parts, method_parts) for val in pair])

        contact_expanded = df.apply(split_contact_info, axis=1)
        new_col_names = []
        for i in range(1, contact_expanded.shape[1] // 2 + 1):
            new_col_names.extend([f'datecontact{i}', f'contactmethod{i}'])
        contact_expanded.columns = new_col_names

        df = df.drop(columns=['dates_contacted', 'contact_methods']).join(contact_expanded)

    return df
