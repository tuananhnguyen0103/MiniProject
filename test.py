import requests

API_URL = "https://3b21-34-105-78-109.ngrok-free.app/predict"
IMAGE_PATH = rf"C:\Myfolder\UTEHY\Python\MiniProject\download (1).jfif"

with open(IMAGE_PATH, "rb") as f:
    files = {"file": f}
    response = requests.post(API_URL, files=files)

print("status_code =", response.status_code)
print(response.json())