'''
'''

import os
import uuid
import pandas as pd
from sklearn.preprocessing import StandardScaler

LOAD_DATA_DIR = "../load_service/datasets"
TRANSFORM_DIR = "transformed"

os.makedirs(TRANSFORM_DIR, exist_ok=True)

def transform_dataset(dataset_id: str):
    input_path = os.path.join(LOAD_DATA_DIR, f"{dataset_id}.csv")

    if not os.path.join(input_path):
        raise FileNotFoundError(f"Dataset {dataset_id} no encontrado")
    
    df = pd.read_csv(input_path)

    expected_columns = {
        "sepal length (cm)",
        "sepal width (cm)",
        "petal length (cm)",
        "petal width (cm)",
        "target"
    }

    if not expected_columns.issubset(set(df.columns)):
        raise ValueError("El archivo no tiene las columnas esperadas del dataset iris")
    
    features = df.drop(columns=["target"])
    target = df["target"]

    scaler = StandardScaler()
    scaled_features = scaler.fit_transform(features)

    df_scaled = pd.DataFrame(
        scaled_features,
        columns=features.columns
    )

    df_scaled["target"] = target

    transformed_id = dataset_id + "_T"

    output_path = os.path.join(TRANSFORM_DIR, f"{transformed_id}.csv")

    df_scaled.to_csv(output_path, index=False)

    return transformed_id
