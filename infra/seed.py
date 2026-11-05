import json
import urllib.request

products = [
    {
        "name": "Тестовая кружка",
        "description": "Демо-товар для проверки каталога и оформления заказа",
        "price": 1290,
        "image": "https://images.unsplash.com/photo-1514228742587-6b1558fef93a?auto=format&fit=crop&w=900&q=80",
        "category": "Демо",
    },
    {
        "name": "Латунные ярлыки",
        "description": "Набор ярлыков и закладка для коробок, книг и документов.",
        "price": 1800,
        "image": "",
        "category": "Аксессуары",
    },
    {
        "name": "Льняной блокнот",
        "description": "Плотная бумага, мягкая обложка и спокойный бежевый тон.",
        "price": 2400,
        "image": "",
        "category": "Бумага",
    },
]

for payload in products:
    request = urllib.request.Request(
        "http://127.0.0.1:8000/products",
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    with urllib.request.urlopen(request) as response:
        print(response.status, response.read().decode("utf-8"))