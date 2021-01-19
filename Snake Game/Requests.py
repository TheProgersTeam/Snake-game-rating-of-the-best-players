import requests


class Requests:
    # Отправляем результат игрока и его ник
    def Post(player, score):
        url = "http://127.0.0.1:8000/api/add/"
        payload = {"data": {"player": player, "score": score}}
        headers = {'Content-Type': 'application/json'}
        requests.request("POST", url, headers=headers, json=payload)

    # Получаем список лучших игроков
    def Get():
        url = "http://127.0.0.1:8000/api/get/"
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        return response.json()
