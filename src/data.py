# src/data.py
from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parent.parent
DATA_PATH = ROOT / "precios commodities.xlsx"

def load_dataset(sheet_name: str = "Hoja1") -> pd.DataFrame:
    """Carga y devuelve un DataFrame completo del Excel."""
    return pd.read_excel(DATA_PATH, sheet_name=sheet_name, parse_dates=['fecha'])

def load_all() -> pd.DataFrame:
    """Carga todos los datos de commodities en un único DataFrame con fecha como índice."""
    df = load_dataset("Hoja1")
    df.set_index('fecha', inplace=True)
    return df

def load_commodity(commodity: str) -> pd.DataFrame:
    """Carga una serie específica del commodity dado."""
    df = load_all()
    return df[[commodity.lower()]].dropna()

