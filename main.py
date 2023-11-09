import requests


url = f"https://ddragon.leagueoflegends.com/cdn/13.22.1/data/en_US/champion/Zoe.json"

requisicao = requests.get(url)
print(requisicao)

dic = requisicao.json()
print(dic222)
