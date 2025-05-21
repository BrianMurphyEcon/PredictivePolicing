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

    return df
