import json
import urllib.request

products = [
    {
        "name": "Мраморный органайзер",
        "description": "Набор для ручек, скрепок и заметок с латунной окантовкой.",
        "price": 6200,
        "image": "",
        "category": "Рабочий стол",
    },
    {
        "name": "Оливковый стакан",
        "description": "Керамический стакан для карандашей или салфеток.",
        "price": 3200,
        "image": "",
        "category": "Хранение",
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