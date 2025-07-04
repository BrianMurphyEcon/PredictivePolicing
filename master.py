import sys
import os

from utils.loader import load_csv_data
from utils.cleaner import clean_data
from config import DTA_FILE

def main():
    print("Loading data...")
    df = load_csv_data()

    print("Cleaning data...")
    df_clean = clean_data(df)

    print("Done! Preview:")
    print(df_clean.head())

    print(f"Saving cleaned data to: {DTA_FILE}")
    drop_cols = ['contact_dates', 'heard_back_dates']
    df_clean = df_clean.drop(columns=[col for col in drop_cols if col in df_clean.columns])
    df_clean.to_stata(DTA_FILE, write_index=False, version=117)

if __name__ == "__main__":
    main()