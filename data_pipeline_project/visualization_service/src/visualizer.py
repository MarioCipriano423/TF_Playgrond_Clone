# pyright: reportMissingImports=false
# pyright: reportMissingModuleSource=false
'''
'''

import os
import pandas as pd
import matplotlib.pyplot as plt

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

TRANSFORM_DIR = "/data/transformed"
PLOTS_DIR = "/data/plots"

os.makedirs(PLOTS_DIR, exist_ok=True)

def generate_visualization(transformed_id: str):
    input_path = os.path.join(TRANSFORM_DIR, f"{transformed_id}.csv")

    if not os.path.exists(input_path):
        raise FileNotFoundError(f"Trandormed dataset {transformed_id} no encontrado")
    
    df = pd.read_csv(input_path)

    required_columns = {
        "Id",
        "SepalLengthCm",
        "SepalWidthCm",
        "PetalLengthCm",
        "PetalWidthCm",
        "Species"
    }

    for col in required_columns:
        if col not in df.columns:
            raise ValueError(f"Columna requerida '{col}' no encontrada")
        
    plt.figure()
    for target_value in df["Species"].unique():
        subset = df[df["Species"] == target_value]

        plt.scatter(
            subset["SepalLengthCm"],
            subset["PetalLengthCm"],
            label=f"Class {target_value}"
        )

    plt.xlabel("Sepal Length (normalized)")
    plt.ylabel("Petal Length (normalized)")
    plt.title("Iris Distribution (Normalized)")
    plt.legend()

    plot_filename = f"{transformed_id}.png"
    plot_path = os.path.join(PLOTS_DIR, plot_filename)

    plt.savefig(plot_path)
    plt.close()

    return {
        "transformed_id": transformed_id,
        "plot_url": f"/plots/{plot_filename}"
    }