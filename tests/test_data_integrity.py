import os
import pytest
import pandas as pd

DATA_PATH = "src/data/df_com_cluster_id.parquet"

REQUIRED_COLUMNS = [
    "year_month",
    "item",
    "store_code",
    "region",
    "sales",
    "mean_price",
    "time_index",
    "month_sin",
    "month_cos",
    "item_mean_sales",
    "store_mean_sales",
    "store_item_mean_sales",
    "cluster_id"
]

def test_data_file_exists():
    """Verifica se o arquivo parquet existe."""
    assert os.path.exists(DATA_PATH), f"Arquivo {DATA_PATH} não encontrado!"

def test_data_columns():
    """Verifica se todas as colunas obrigatórias estão presentes."""
    df = pd.read_parquet(DATA_PATH)
    for col in REQUIRED_COLUMNS:
        assert col in df.columns, f"Coluna obrigatória ausente: {col}"

def test_no_nulls_in_critical_fields():
    """Garante que colunas críticas não possuem valores nulos."""
    df = pd.read_parquet(DATA_PATH)

    critical_cols = ["sales", "mean_price", "cluster_id"]

    for col in critical_cols:
        assert df[col].notna().all(), f"Valores nulos encontrados em: {col}"
