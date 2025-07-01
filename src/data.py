# src/data.py
from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]        
DATA_PATH = ROOT / "precios commodities.xlsx"       

def load_dataset(sheet_name: str = "Maíz") -> pd.DataFrame:
    """
    Devuelve un DataFrame con la hoja indicada.
    """
    return pd.read_excel(DATA_PATH, sheet_name=sheet_name)
