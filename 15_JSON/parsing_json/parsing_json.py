import json

with open('data.json', 'r')as file:
    data = json.load(file)

for user in data:
    print(f"Nume:{user['nume']}")
    print(f"Varsta:{user['varsta']}")
    print(f"Email:{user['email']}")
    print("-" *20)