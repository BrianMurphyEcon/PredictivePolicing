# Predictive Policing Data Pipeline

This project is a attempting to answer how police departments use predictive policing technology. 
The following code transforms raw police department data into a cleaned, Stata ready dataset.

---

## 📁 Project Structure

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

## 🚀 How to Run

### 1. Clone this repository

```bash
git clone https://github.com/yourusername/predictive-policing-pipeline.git
cd predictive-policing-pipeline/Code
