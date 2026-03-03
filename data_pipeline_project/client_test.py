import os
import requests
from dotenv import load_dotenv

# Cargar variables del .env
load_dotenv()

HOST = os.getenv("GATEWAY_HOST")
PORT = os.getenv("GATEWAY_PORT")

GATEWAY_URL = f"http://{HOST}:{PORT}/run-pipeline"

FILE_PATH = "data/iris.csv"


def upload_file():
    try:
        with open(FILE_PATH, "rb") as f:
            files = {
                "file": ("iris.csv", f, "text/csv")
            }

            print(f"Enviando archivo a {GATEWAY_URL}")
            response = requests.post(GATEWAY_URL, files=files)

        if response.status_code == 200:
            with open("output.png", "wb") as img:
                img.write(response.content)

            print("Imagen guardada como output.png")

        else:
            print("Error:", response.status_code)
            print(response.text)

    except Exception as e:
        print("Error en el cliente:", str(e))


if __name__ == "__main__":
    upload_file()