# Predictive Policing Project

The following code transforms raw police department data into a cleaned, Stata ready dataset.

---

## Project Structure

<pre>
Predictive Policing Team/
├── Code/
│   ├── master.py               # Main script: runs full pipeline
│   ├── config.py               # Shared file paths
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── loader.py           # Loads raw CSV data
│   │   └── cleaner.py          # Cleans and formats the data
├── Data/
</pre>

---

## What This Code Does

- Drops junk columns (e.g., `Unnamed: 0`)  
- Replaces problematic characters for Stata compatibility  
... and More!

---

## Notes

- Raw and cleaned data are **not included** in the repository.
- File paths are managed in `config.py` and should be adjusted if cloning on a new computer.  