# pyright: reportMissingImports=false
# pyright: reportMissingModuleSource=false
'''
'''
import requests

GATEWAY_URL = "http://localhost:8000/run-pipeline"


def upload_file():

    with open("data/iris.csv", "rb") as f:
        files = {
            "file": ("iris.csv", f, "text/csv")
        }

        print(f"Enviando archivo a {GATEWAY_URL}")
        response = requests.post(GATEWAY_URL, files=files)

    if response.status_code != 200:
        print("Error:", response.status_code)
        print(response.text)
        return

    data = response.json()

    plot_url = data["plot_url"]

    # ⚠️ el gateway normalmente debe regresarte la URL completa
    image_url = f"http://localhost:8000{plot_url}"

    print("Descargando imagen desde:", image_url)

    img_response = requests.get(image_url)

    if img_response.status_code == 200:
        with open("output.png", "wb") as img:
            img.write(img_response.content)

        print("Imagen guardada como output.png")

    else:
        print("Error descargando imagen:", img_response.status_code)


if __name__ == "__main__":
    upload_file()
