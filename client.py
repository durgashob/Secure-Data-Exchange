# client.py
import requests
import base64
import os

file_path = "example.txt"  # Change to your file name
if not os.path.exists(file_path):
    print(f"File '{file_path}' not found! Please put your file in this folder.")
    exit()

# Read and Base64 encode the file
with open(file_path, "rb") as f:
    encoded = base64.b64encode(f.read()).decode()

data = {
    "file": encoded,
    "filename": os.path.basename(file_path)
}

# Send file to server
try:
    response = requests.post("https://localhost:5000/upload", data=data, verify=False)
    print(response.text)
except requests.exceptions.RequestException as e:
    print("Error sending file:", e)