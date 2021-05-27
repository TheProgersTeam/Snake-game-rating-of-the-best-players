import requests


class Requests:
    #  We send the result of the player and his nickname
    def Post(player, score):
        url = "http://127.0.0.1:8000/api/add/"
        payload = {"data": {"player": player, "score": score}}
        headers = {'Content-Type': 'application/json'}
        requests.request("POST", url, headers=headers, json=payload)

    #  We get a list of the best players
    def Get():
        url = "http://127.0.0.1:8000/api/get/"
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        return response.json()
