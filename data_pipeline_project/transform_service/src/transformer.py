# pyright: reportMissingImports=false
# pyright: reportMissingModuleSource=false
'''
'''

import os
import pandas as pd
from sklearn.preprocessing import StandardScaler

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

LOAD_DATA_DIR = "/data/datasets"
TRANSFORM_DIR = "/data/transformed"

os.makedirs(TRANSFORM_DIR, exist_ok=True)

def transform_dataset(dataset_id: str):
    input_path = os.path.join(LOAD_DATA_DIR, f"{dataset_id}.csv")

    if not os.path.join(input_path):
        raise FileNotFoundError(f"Dataset {dataset_id} no encontrado")
    
    df = pd.read_csv(input_path)

    expected_columns = {
        "Id",
        "SepalLengthCm",
        "SepalWidthCm",
        "PetalLengthCm",
        "PetalWidthCm",
        "Species"
    }

    if not expected_columns.issubset(set(df.columns)):
        raise ValueError("El archivo no tiene las columnas esperadas del dataset iris")
    
    features = df.drop(columns=["Species"])
    target = df["Species"]

    scaler = StandardScaler()
    scaled_features = scaler.fit_transform(features)

    df_scaled = pd.DataFrame(
        scaled_features,
        columns=features.columns
    )

    df_scaled["Species"] = target

    transformed_id = dataset_id + "_T"

    output_path = os.path.join(TRANSFORM_DIR, f"{transformed_id}.csv")

    df_scaled.to_csv(output_path, index=False)

    return transformed_id
