import pandas as pd

def test_placeholder_data_integrity():
    """Teste fictício apenas para garantir que o pipeline CI está funcionando."""
    df = pd.DataFrame({"col1": [1, 2], "col2": [3, 4]})
    assert not df.empty
    assert list(df.columns) == ["col1", "col2"]
