# Predictive Policing Project

This project is a attempting to answer how police departments use predictive policing technology. 
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
│   └── PoliceDept/
│       ├── Algorithmic Policing Data.csv   # Raw input file
│       └── cleaned_data.dta                # Final output (Stata)
</pre>

---

## How to Run

### 1. Clone this repository

```bash
git clone https://github.com/yourusername/predictive-policing-pipeline.git
cd predictive-policing-pipeline/Code
```

## 2. Set up your environment

This project requires:

- Python 3.9+
- `pandas`, `numpy`

### If using Anaconda:

```bash
conda install pandas numpy
```

```bash
pip install pandas numpy
```
## 3.Run 
```bash
python master.py
```
This will:

- Load the raw CSV file
- Clean and standardize column names
- Export the cleaned dataset as a Stata `.dta` file

---

## What It Does

- Drops junk columns (e.g., `Unnamed: 0`)  
- Replaces problematic characters for Stata compatibility  
... and More!

---

## Notes

- Raw and cleaned data are **not included** in the repository to protect the output.  
- File paths are managed in `config.py` and should be adjusted if cloning on a new computer.  

---

## Contributors

- Brian Murphy (Lead)  
- Hallie, Zane, Khushi, David (Research Assistants)

---

## License

This project is private and intended for academic research use only.

