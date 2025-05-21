# utils/loader.py

import os
import pandas as pd
from config import CSV_FILE  # type: ignore

def load_csv_data():
    if not os.path.exists(CSV_FILE):
        raise FileNotFoundError(f"CSV file not found at: {CSV_FILE}")
    return pd.read_csv(CSV_FILE, encoding='cp1252')
