import requests

url = "https://canvas.auckland.ac.nz/api/v1/courses"

headers = {
    "Authorization": "Bearer 你的token"
}

response = requests.get(url, headers=headers)

print(res.json())