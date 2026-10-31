import requests

response = requests.get("https://api.github.com/users/salihkkus")
data = response.json()

print(f"Public repo sayısı: {data['public_repos']}")
