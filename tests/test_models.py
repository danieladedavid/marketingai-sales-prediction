import os
import pickle
import pytest
import pandas as pd

MODEL_PATH = "src/models/best_model.pkl"
PREPROCESS_PATH = "src/models/preprocess_predicao.pkl"

def test_model_files_exist():
    """Verifica se os arquivos essenciais do modelo existem."""
    assert os.path.exists(MODEL_PATH), "best_model.pkl não encontrado!"
    assert os.path.exists(PREPROCESS_PATH), "preprocess_predicao.pkl não encontrado!"

def test_model_loading():
    """Verifica se o modelo e o preprocessador carregam corretamente."""
    with open(MODEL_PATH, "rb") as f:
        model = pickle.load(f)

    with open(PREPROCESS_PATH, "rb") as f:
        preprocess = pickle.load(f)

    assert model is not None, "Falha ao carregar o modelo!"
    assert preprocess is not None, "Falha ao carregar o preprocessador!"

def test_model_prediction():
    """Testa se o modelo consegue gerar uma previsão com um exemplo mínimo."""

    # Exemplo mínimo (ajuste conforme suas features finais)
    example = pd.DataFrame([{
        "time_index": 120,
        "month_sin": 0.5,
        "month_cos": -0.5,
        "mean_price": 10.99,
        "item_mean_sales": 30,
        "store_mean_sales": 50,
        "store_item_mean_sales": 40,
        "cluster_id": 2
    }])

    # Carregar objetos
    with open(MODEL_PATH, "rb") as f:
        model = pickle.load(f)

    with open(PREPROCESS_PATH, "rb") as f:
        preprocess = pickle.load(f)

    # Transformar entrada
    X_input = preprocess.transform(example)

    # Previsão
    pred = model.predict(X_input)

    assert pred is not None, "Modelo não retornou previsão!"
    assert len(pred) == 1, "Previsão deve retornar um único valor!"
